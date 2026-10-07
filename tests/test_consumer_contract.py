"""Protect approved organization content without requiring an installed generator."""

from pathlib import Path
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
SQL_SERVER_PACKAGE = "Doka.EntityFrameworkCore.SafeMigrations.SqlServer"
APPROVED_PROJECT_LAYOUT = {
    "project:doka-labs/mysql": ([470.0, 345.0], 48.0, 0.8),
    "project:doka-labs/nested-set": ([1280.0, 685.0], 48.0, 0.8),
    "project:doka-labs/relational-lab": ([520.0, 685.0], 42.0, 0.8),
    "project:doka-labs/safe-migrations": ([1330.0, 345.0], 51.0, 0.8),
}


def read_toml(path):
    """Read an authored TOML document using the standard library."""
    return tomllib.loads(path.read_text(encoding="utf-8"))


class AuthoredOrganizationTests(unittest.TestCase):
    """Keep the approved consumer identity, canonical content, and layout explicit."""

    def test_profile_imports_canonical_content_and_maintainer_once(self):
        """The profile owns presentation while the local organization owns shared content."""
        # Arrange
        profile = read_toml(ROOT / "config/profile.toml")
        organization = read_toml(ROOT / "config/organization.toml")

        # Act
        imports = profile["imports"]

        # Assert
        self.assertEqual(imports, [{"id": organization["id"], "source": {
            "kind": "local", "path": "organization.toml",
        }}])
        self.assertEqual(organization["id"], "doka-labs")
        self.assertEqual(organization["owner"], "doka-labs")
        self.assertEqual(profile["profile"]["organization"], organization["owner"])
        self.assertEqual(profile["profile"]["username"], organization["owner"])
        self.assertEqual(profile["profile"]["variant"], "organization")
        self.assertEqual(organization["maintainer"], {
            "username": "kdominic89",
            "role": "Administrator & Core Maintainer",
            "url": "https://github.com/kdominic89",
        })
        self.assertFalse({"domains", "projects", "publications", "technologies", "maintainer"} & profile.keys())
        self.assertFalse(any(key.startswith("maintainer") for key in profile["profile"]))
        self.assertEqual(profile["collection"]["github_organizations"], [organization["owner"]])
        self.assertEqual(profile["collection"]["nuget_owner"], organization["owner"])
        self.assertFalse(profile["collection"].get("github_user"))
        self.assertFalse(profile["collection"]["collect_contributions"])
        self.assertFalse(profile["collection"]["collect_private_repository_count"])

    def test_private_project_has_only_abstract_public_content(self):
        """RelationalLab remains an authored abstract project with no repository destination."""
        # Arrange
        organization = read_toml(ROOT / "config/organization.toml")

        # Act
        private_projects = [project for project in organization["projects"]
                            if project["visibility"] == "private-abstract"]

        # Assert
        self.assertEqual([project["id"] for project in private_projects], ["relational-lab"])
        self.assertEqual(private_projects[0]["label"], "RelationalLab")
        self.assertFalse({"url", "repository"} & private_projects[0].keys())

    def test_safe_migrations_declares_safe_motif_and_sql_server_fifth_row(self):
        """The approved SQL Server adapter extends the existing package column by one row."""
        # Arrange
        organization = read_toml(ROOT / "config/organization.toml")
        profile = read_toml(ROOT / "config/profile.toml")
        project = next(project for project in organization["projects"] if project["id"] == "safe-migrations")
        publication = next(item for item in organization["publications"] if item["id"] == "safe-migrations")

        # Act
        package = next(package for package in publication["packages"] if package["id"] == SQL_SERVER_PACKAGE)
        anchors = {package["id"]: profile["layout"]["overrides"][f"package:{package['id']}"]
                   for package in publication["packages"]}

        # Assert
        self.assertEqual(project["icon"], "builtin:database-safe")
        self.assertIn("SQL Server", project["summary"])
        self.assertIn("SQL Server", profile["presentation"]["supporting_stack"])
        self.assertEqual(package["summary"], "SQL Server adapter")
        self.assertEqual(package["url"], f"https://www.nuget.org/packages/{SQL_SERVER_PACKAGE}/")
        self.assertEqual(publication["label_overrides"][SQL_SERVER_PACKAGE], "SQL Server")
        self.assertEqual(anchors[SQL_SERVER_PACKAGE], [666.0, 1372.0])
        self.assertEqual(sorted(anchor[1] for anchor in anchors.values()), [1012.0, 1102.0, 1192.0, 1282.0, 1372.0])
        self.assertEqual(profile["render"]["height"], 1552)

    def test_approved_project_anchors_radii_and_weights_remain_explicit(self):
        """Extraction must preserve the four approved project positions and ring sizes."""
        # Arrange
        profile = read_toml(ROOT / "config/profile.toml")

        # Act
        layout = {identifier: (profile["layout"]["overrides"][identifier],
                               profile["layout"]["radii"][identifier],
                               profile["layout"]["weights"][identifier])
                  for identifier in APPROVED_PROJECT_LAYOUT}

        # Assert
        self.assertEqual(layout, APPROVED_PROJECT_LAYOUT)


if __name__ == "__main__":
    unittest.main()
