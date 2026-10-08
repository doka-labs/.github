# Validation

Verified locally on October 8, 2026 with the published Sourcefield `v0.1.1` CLI and matching
browser runtime at source commit `b12eb4c72d60fbc075776a6ccc4bc15736db28af`. The installation
was authenticated against the immutable release, both archive digests, and GitHub attestations.
This report records consumer upgrade checks on macOS; it does not claim a hosted consumer run
or a new public deployment.

## Current output

The regenerated output is explicitly **Preview**, state `D339988187297421`, with 21 nodes,
35 edges, four projects, ten NuGet packages, and a 1800 by 1552 canvas. It uses the latest
published consumer inputs from commit `10a7ab01bead284d6d03a2eb24d7ac41dea2475f`.

The retained `assets/source-snapshot.json` is byte-identical to that published input. Its original
Live status and collection date, `2026-10-07T10:18:38.951719124+00:00`, remain intact. Offline
generation performs no new collection. Its separate `assets/render-snapshot.json` is an undated
Preview, and the schema 2 generation record binds exactly six captured inputs and the authored
profile digest. Versions and metrics in this preview are retained observations, not new queries.

The authored configuration, approved geometry, safe motif, SQL Server fifth package row,
maintainer attribution, and collection scope remain unchanged. All 24 retained archive files and
their index remain byte-identical. Both READMEs receive the same generated project/package tables;
their authored prose and destination links are preserved.

## Executed checks

| Check | Result |
| --- | --- |
| Published release, native/browser archives, checksums, and attestations | Passed; authenticated matching v0.1.1 installation |
| Consumer tests with the released installation | 15 passed, zero skipped; authored contracts and positive/negative generation, replay, privacy, geometry, history, and atomicity |
| Lock, update-workflow pin, and shared tooling revision | Passed; all select the released source commit |
| Complete generated artifact validation | Passed; 21 nodes, 35 edges, ten packages, matching WASM/runtime |
| Both workflow files with actionlint | Passed |
| Actual released runtime in Chromium | Passed; WASM, fallback, themes, geometry, interaction, pause, and reduced motion |
| Historical browser selection | All 24 archives load with matching node counts; current view restores |
| README/mobile comparison | Before/after SVGs inspected at 820 and 343 content pixels |
| Locked native replay | All candidate files reproduce byte for byte |
| Missing retained offline capture | Fails without changing other files or substituting the authoring seed |
| Retained capture without the authoring seed | Generation succeeds and retains the expected source and current state |
| Two fresh Git clones through shared candidate/publication tools | Passed; raw capture and all archives preserved, ignored WASM regenerated and never staged |
| Recovery and source preservation | Original and published trees retained externally; Git bundles verify; other consumer and generator files unchanged |
| Documentation, references, ASCII, Python syntax, and final candidate digests | Passed |

Representative commands actually run, with external paths abbreviated:

```sh
SOURCEFIELD_INSTALLATION=/path/to/verified/installation \
  python3 -B -m unittest discover -s tests -p 'test_*.py' -v

python3 -B "$SOURCEFIELD_SOURCE/scripts/check_pin.py" \
  --lock sourcefield.lock.json --workflow .github/workflows/update-profile.yml \
  --own-commit b12eb4c72d60fbc075776a6ccc4bc15736db28af

python3 -B "$SOURCEFIELD_SOURCE/scripts/validate_artifact.py" \
  --root /path/to/verified/candidate --workflow-root /path/to/consumer --require-wasm

actionlint .github/workflows/update-profile.yml .github/workflows/validate.yml

node "$SOURCEFIELD_SOURCE/scripts/verify-browser.mjs" \
  --site /path/to/verified/candidate/docs --output /path/to/external/evidence \
  --playwright-module /path/to/existing/playwright/index.mjs \
  --browser /path/to/existing/chromium
```

Detailed logs, recovery files, digests, publication fixtures, and comparison screenshots are
retained outside this repository. Neither compiled binaries nor browser test tooling are tracked.

## Publication boundary

The user updated the repository Actions allowlist, and its exact new reusable workflow entry was
verified through the GitHub API on October 8, 2026; see [Setup](SETUP.md). Existing permissions,
schedule, checked publication, and deployment ordering remain unchanged.

Commit, push, hosted validation, and the subsequent Update SOURCEFIELD publication/Pages run
remain separate steps. Local checks do not establish hosted success. The immutable upstream
release passed its own CI; this consumer's upgraded workflow still needs its hosted Ubuntu run.
