"""Exercise the released CLI at the consumer's authored and generated file boundaries."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_consumer_contract import APPROVED_PROJECT_LAYOUT, ROOT, SQL_SERVER_PACKAGE, read_toml


READMES = ("README.md", "profile/README.md")
REPLAY_INPUTS = {
    "resolved-config.json", "source-snapshot.json", "render-snapshot.json",
    "import-capture.json", "layout.json", "profile-state.json",
}

AUTHORED_DRIFT_DIAGNOSTIC = (
    "generation provenance authored inputs changed: configuration bytes differ from the recorded generation"
)


def read_json(path):
    """Read a generated JSON document without importing Sourcefield implementation code."""
    return json.loads(path.read_text(encoding="utf-8"))


def project_layout(state):
    """Select the project geometry that canonical prose changes must preserve."""
    return {node["id"]: ([node["x"], node["y"]], node["radius"], node["weight"])
            for node in state["nodes"] if node["kind"] == "project"}


@unittest.skipUnless(os.environ.get("SOURCEFIELD_INSTALLATION"), "Set SOURCEFIELD_INSTALLATION for released CLI tests")
class ReleasedGenerationTests(unittest.TestCase):
    """Generate only isolated fixtures using the externally installed CLI and runtime."""

    @classmethod
    def setUpClass(cls):
        """Require a complete installation when integration testing is explicitly enabled."""
        cls.installation = Path(os.environ["SOURCEFIELD_INSTALLATION"]).resolve()
        for relative in ("sourcefield", "runtime/runtime-manifest.json", "runtime/pkg/sourcefield_wasm_bg.wasm"):
            if not (cls.installation / relative).is_file():
                raise RuntimeError(f"Released Sourcefield installation is incomplete: {relative}")

    def setUp(self):
        """Copy consumer inputs and outputs; generation restores the excluded runtime package."""
        temporary = tempfile.TemporaryDirectory(prefix="doka-consumer-contract-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for relative in ("config", "assets", "docs"):
            ignore = shutil.ignore_patterns("pkg") if relative == "docs" else None
            shutil.copytree(ROOT / relative, self.root / relative, ignore=ignore)

        for relative in (*READMES, ".sourcefield-owned.json"):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)

    def _command(self, *extra):
        """Run offline generation with explicit runtime, README destinations, and history preservation."""
        command = [
            str(self.installation / "sourcefield"), "generate",
            "--root", str(self.root), "--offline",
            "--fallback-snapshot", "assets/source-snapshot.json",
            "--runtime", str(self.installation / "runtime"),
            "--readme", READMES[0], "--readme", READMES[1], "--no-history", *extra,
        ]

        return subprocess.run(command, cwd=self.root, capture_output=True, text=True, timeout=45, check=False)

    def _generate(self, *extra):
        """Require successful fixture generation before reading its emitted artifacts."""
        result = self._command(*extra)
        self.assertEqual(result.returncode, 0, result.stderr)

        return read_json(self.root / "assets/profile-state.json")

    def _owned_outputs(self):
        """Capture managed output bytes and both authored README destinations for atomicity checks."""
        ownership = read_json(self.root / ".sourcefield-owned.json")
        paths = {*ownership["files"], *READMES, ".sourcefield-owned.json"}
        return {relative: (self.root / relative).read_bytes() for relative in sorted(paths)}

    def _history(self):
        """Capture every retained archive and the historical index byte for byte."""
        return {path.name: path.read_bytes() for path in (self.root / "docs/history").iterdir() if path.is_file()}

    def _assert_generation_record(self):
        """Require the schema 2 record to bind current authored bytes and exactly six captured input roles."""
        record = read_json(self.root / "assets/generation-record.json")
        inputs = {name: hashlib.sha256((self.root / "assets" / name).read_bytes()).hexdigest()
                  for name in REPLAY_INPUTS}

        self.assertEqual(record["schema_version"], 2)
        self.assertEqual(record["inputs"], inputs)
        self.assertEqual(record["authored_config_sha256"],
                         hashlib.sha256((self.root / "config/profile.toml").read_bytes()).hexdigest())

        return record

    def _change_canonical_summary(self):
        """Edit one real organization project without changing the profile's presentation inputs."""
        path = self.root / "config/organization.toml"
        organization = read_toml(path)
        project = next(project for project in organization["projects"] if project["id"] == "mysql")
        summary = "Consumer contract canonical summary."
        path.write_text(path.read_text(encoding="utf-8").replace(
            f"summary = {json.dumps(project['summary'])}", f"summary = {json.dumps(summary)}", 1,
        ), encoding="utf-8")

        return summary

    def test_offline_regeneration_is_deterministic_and_preserves_history(self):
        """Repeated consumer generation preserves all retained states and managed output bytes."""
        # Arrange
        history = self._history()
        profile = read_toml(self.root / "config/profile.toml")
        organization = read_toml(self.root / "config/organization.toml")
        self._generate()
        outputs = self._owned_outputs()

        # Act
        state = self._generate()

        # Assert
        self.assertEqual(self._owned_outputs(), outputs)
        self.assertEqual(self._history(), history)
        index = read_json(self.root / "docs/history/index.json")
        self.assertLessEqual(len(index["states"]), profile["collection"]["history_limit"])
        self.assertEqual({entry["file"] for entry in index["states"]}, set(history) - {"index.json"})
        self.assertEqual({node["id"] for node in state["nodes"] if node["kind"] == "project"}, {
            f"project:{organization['id']}/{project['id']}" for project in organization["projects"]
        })
        self.assertTrue({
            f"package:{package['id']}" for publication in organization["publications"]
            for package in publication["packages"]
        }.issubset({node["id"] for node in state["nodes"] if node["kind"] == "package"}))
        self.assertEqual(state["profile"]["maintainer"], organization["maintainer"])
        self.assertEqual(state["profile"]["organization"], organization["owner"])
        private = next(node for node in state["nodes"] if node["id"].endswith("/relational-lab"))
        self.assertIsNone(private["url"])
        for relative in READMES:
            readme = (self.root / relative).read_text(encoding="utf-8")
            self.assertIn(f"| {private['label']} | {private['summary']} |", readme)
            self.assertNotIn(f"[{private['label']}]", readme)

    def test_shorter_history_is_preserved_without_filling_the_retention_cap(self):
        """A retention limit is an upper bound, including when only one archive exists."""
        # Arrange
        index_path = self.root / "docs/history/index.json"
        index = read_json(index_path)
        retained = index["states"][:1]
        for entry in index["states"][1:]:
            (index_path.parent / entry["file"]).unlink()

        index["states"] = retained
        index_path.write_text(json.dumps(index) + "\n", encoding="utf-8")
        # Adopt this deliberately shortened fixture once so its ownership matches the initial history.
        (self.root / ".sourcefield-owned.json").unlink()
        self._generate("--adopt-existing")
        history = self._history()

        # Act
        self._generate()

        # Assert
        self.assertEqual(self._history(), history)
        self.assertEqual(read_json(index_path)["states"], retained)

    def test_offline_preview_preserves_dated_source_and_records_distinct_effective_input(self):
        """Preview preserves the actual public Live capture while binding its separate undated rendering input."""
        # Arrange
        source_path = self.root / "assets/source-snapshot.json"
        source_bytes = source_path.read_bytes()
        captured = read_json(source_path)
        history = self._history()

        # Act
        state = self._generate()

        # Assert
        self.assertEqual(captured["mode"], "live")
        self.assertTrue(captured["fetched_at"])
        self.assertIsNone(captured["private_repository_count"])
        self.assertEqual(source_path.read_bytes(), source_bytes)
        current = read_json(source_path)
        self.assertEqual(current["fetched_at"], captured["fetched_at"])
        self.assertEqual(current["sources"], captured["sources"])
        render_path = self.root / "assets/render-snapshot.json"
        effective = read_json(render_path)
        self.assertEqual(effective["mode"], "preview")
        self.assertEqual(effective["fetched_at"], "")
        self.assertIsNone(effective["private_repository_count"])
        self.assertEqual(state["mode"], "preview")
        self.assertNotEqual(render_path.read_bytes(), source_bytes)
        self._assert_generation_record()
        self.assertEqual(self._history(), history)

    def test_locked_replay_preserves_dated_source_and_recorded_effective_preview(self):
        """Replay preserves raw source provenance and the exact already captured Preview without rewriting history."""
        # Arrange
        source_path = self.root / "assets/source-snapshot.json"
        source_bytes = source_path.read_bytes()
        captured = read_json(source_path)
        history = self._history()
        self._generate()
        render_path = self.root / "assets/render-snapshot.json"
        render_bytes = render_path.read_bytes()
        outputs = self._owned_outputs()

        # Act
        state = self._generate("--locked")

        # Assert
        self.assertEqual(source_path.read_bytes(), source_bytes)
        self.assertEqual(read_json(source_path)["fetched_at"], captured["fetched_at"])
        self.assertEqual(read_json(source_path)["mode"], captured["mode"])
        self.assertEqual(read_json(source_path)["sources"], captured["sources"])
        self.assertEqual(render_path.read_bytes(), render_bytes)
        self.assertEqual(read_json(render_path)["mode"], "preview")
        self.assertEqual(read_json(render_path)["fetched_at"], "")
        self.assertIsNone(read_json(render_path)["private_repository_count"])
        self.assertEqual(state["mode"], "preview")
        self._assert_generation_record()
        self.assertEqual(self._owned_outputs(), outputs)
        self.assertEqual(self._history(), history)

    def test_canonical_summary_reaches_state_and_both_readmes_without_moving_projects(self):
        """The local import is the active consumer source of project prose."""
        # Arrange
        original = self._generate()
        summary = self._change_canonical_summary()

        # Act
        state = self._generate()

        # Assert
        project = next(node for node in state["nodes"] if node["id"] == "project:doka-labs/mysql")
        self.assertEqual(project["summary"], summary)
        self.assertEqual(project_layout(state), project_layout(original))
        self.assertNotEqual(state["semantic_hash"], original["semantic_hash"])
        for relative in READMES:
            self.assertIn(summary, (self.root / relative).read_text(encoding="utf-8"))

    def test_generated_layout_preserves_approved_projects_and_sql_server_fifth_row(self):
        """Authored anchors remain effective after import namespacing and released generation."""
        # Arrange
        profile = read_toml(self.root / "config/profile.toml")
        organization = read_toml(self.root / "config/organization.toml")
        publication = next(item for item in organization["publications"] if item["id"] == "safe-migrations")

        # Act
        state = self._generate()

        # Assert
        nodes = {node["id"]: node for node in state["nodes"]}
        self.assertEqual(project_layout(state), APPROVED_PROJECT_LAYOUT)
        for identifier, anchor in profile["layout"]["overrides"].items():
            self.assertEqual([nodes[identifier]["x"], nodes[identifier]["y"]], anchor, identifier)
        package = nodes[f"package:{SQL_SERVER_PACKAGE}"]
        self.assertEqual(package["surface_label"], "SQL Server")
        self.assertEqual([package["x"], package["y"]], [666.0, 1372.0])
        ordered = sorted(publication["packages"], key=lambda item: nodes[f"package:{item['id']}"]["y"])
        self.assertEqual(ordered[4]["id"], SQL_SERVER_PACKAGE)
        self.assertEqual(nodes["project:doka-labs/safe-migrations"]["icon"], "builtin:database-safe")
        self.assertGreaterEqual(state["canvas"]["height"], profile["render"]["height"])

    def test_locked_replay_uses_captured_import_and_restores_missing_outputs(self):
        """Replay reproduces captured content even if the current local organization was edited."""
        # Arrange
        self._generate()
        outputs = self._owned_outputs()
        self._change_canonical_summary()
        (self.root / "assets/sourcefield.dark.svg").unlink()
        (self.root / "docs/profile-state.json").unlink()

        # Act
        self._generate("--locked")

        # Assert
        self.assertEqual(self._owned_outputs(), outputs)

    def test_missing_canonical_manifest_leaves_outputs_unchanged(self):
        """Ordinary generation cannot replace valid outputs after losing its shared authored input."""
        # Arrange
        self._generate()
        (self.root / "config/organization.toml").unlink()
        outputs = self._owned_outputs()

        # Act
        result = self._command()

        # Assert
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot read local organization manifest", result.stderr)
        self.assertEqual(self._owned_outputs(), outputs)

    def test_corrupt_captured_snapshot_fails_replay_without_mutating_outputs(self):
        """A valid JSON snapshot with changed bytes must fail the recorded replay digest."""
        # Arrange
        self._generate()
        snapshot = self.root / "assets/source-snapshot.json"
        snapshot.write_bytes(snapshot.read_bytes() + b"\n")
        outputs = self._owned_outputs()

        # Act
        result = self._command("--locked")

        # Assert
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("generation provenance input digest mismatch: source-snapshot.json", result.stderr)
        self.assertEqual(self._owned_outputs(), outputs)

    def test_changed_profile_rejects_locked_replay_without_mutating_outputs(self):
        """Locked replay requires the captured consumer profile even when its change is only a comment."""
        # Arrange
        self._generate()
        profile = self.root / "config/profile.toml"
        profile.write_bytes(profile.read_bytes() + b"\n# Consumer-authored drift.\n")
        outputs = self._owned_outputs()

        # Act
        result = self._command("--locked")

        # Assert
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(AUTHORED_DRIFT_DIAGNOSTIC, result.stderr)
        self.assertEqual(self._owned_outputs(), outputs)

    def test_corrupt_effective_render_snapshot_fails_replay_without_mutating_outputs(self):
        """The schema 2 record rejects changed effective rendering bytes independently of the durable source."""
        # Arrange
        self._generate()
        source_bytes = (self.root / "assets/source-snapshot.json").read_bytes()
        render_path = self.root / "assets/render-snapshot.json"
        render_path.write_bytes(render_path.read_bytes() + b"\n")
        outputs = self._owned_outputs()

        # Act
        result = self._command("--locked")

        # Assert
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("generation provenance input digest mismatch: render-snapshot.json", result.stderr)
        self.assertEqual((self.root / "assets/source-snapshot.json").read_bytes(), source_bytes)
        self.assertEqual(self._owned_outputs(), outputs)


if __name__ == "__main__":
    unittest.main()
