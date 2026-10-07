# Validation

Verified locally on October 7, 2026 against the published Sourcefield `v0.1.0` CLI and matching
browser runtime at source commit `9c69b59c0d85eb26418fb7c7800be2b54ac55a8b`. This is consumer
migration evidence; it does not claim a new GitHub CI run or public deployment.

## Current candidate

The checked-in current output is explicitly **Preview**, state `550C4EAA33EE3591`, with 21 nodes,
35 edges, four projects, ten NuGet packages, and a 1800 by 1552 canvas. Public observations were
collected successfully in an isolated, unpublished Git fixture. Regenerating the consumer from those
observations offline retains honest Preview status and does not claim published import provenance.
The minimal tracked Preview seed contains no maintained package versions or fabricated metrics.

The approved project/domain/publication positions, nine original package anchors, project radii,
and weights are preserved. SQL Server occupies the fifth SafeMigrations row. The added row grows the
canvas by 90 units; the footer separator remains 64 units below the last package version line.
Derived technology positions use the released stable-ID layout; those nodes are not drawn in the
README or browser Field SVG.

## Executed checks

| Check | Result |
| --- | --- |
| Published lock, release signatures/attestations, native and browser archive digests | Passed |
| Released migration/recovery mapping | All 52 mapped source/recovery/output file digests match |
| Historical archive migration | All 24 original archive facts, hashes, and timestamps retained |
| Consumer Python tests with `SOURCEFIELD_INSTALLATION` | 12 passed; positive/negative generation, replay, atomicity, layout, privacy, and shorter-history coverage |
| Shared pin check and artifact validator | Passed; 21 nodes, 35 edges, ten packages, zero warnings |
| Both workflow files with `actionlint` | Passed |
| Released runtime in actual Chromium | Passed; approved safe icon, WASM, fallback, field geometry, interaction, pause, and reduced motion |
| Actual migrated browser history | All 24 archives load; node counts match; current view restores |
| README/mobile SVG comparison | Captured and inspected at 820 and 343 content pixels before/after |
| Fresh tracked checkout through shared candidate tooling | Passed without Rust compilation; matching ignored WASM/runtime restored |
| Locked candidate from fresh checkout | Current state, all three SVGs, and history index reproduce byte for byte |
| Actual strict live rolling retention in isolated fixture | Passed; new live archive prepended, oldest removed, 24 retained |
| Offline history boundary | Existing live archives remain unchanged; previews create no live archive |
| Full recovery rehearsal | All 87 original working/runtime files restore with matching digests; full Git bundle verifies |
| Documentation, local references, pins, and ASCII checks | Passed |

Representative commands actually run against isolated fixtures:

```sh
SOURCEFIELD_INSTALLATION=/path/to/verified/installation \
  python3 -B -m unittest discover -s tests -p 'test_*.py' -v

python3 -B "$SOURCEFIELD_SOURCE/scripts/check_pin.py" \
  --lock sourcefield.lock.json --workflow .github/workflows/update-profile.yml \
  --own-commit 9c69b59c0d85eb26418fb7c7800be2b54ac55a8b

python3 -B "$SOURCEFIELD_SOURCE/scripts/validate_artifact.py" \
  --root /path/to/verified/candidate --workflow-root /path/to/consumer --require-wasm

actionlint .github/workflows/update-profile.yml .github/workflows/validate.yml

node "$SOURCEFIELD_SOURCE/scripts/verify-browser.mjs" \
  --site /path/to/verified/candidate/docs --output /path/to/external/evidence \
  --playwright-module /path/to/existing/playwright/index.mjs \
  --browser /path/to/existing/chromium
```

The paths above represent the actual external installation and isolated candidate used for these
checks. The consumer carries neither a Rust workspace nor copied generator/browser test tooling.
Detailed logs, original bytes, digests, migration mappings, and screenshots are retained separately.

## Publication boundary

The repository Actions allowlist was verified on October 7, 2026 to include the exact pinned
Sourcefield reusable workflow listed in [Setup](SETUP.md); existing policy settings were unchanged.
The user added the entry, and the agent verified it through the GitHub API. Hosted Actions,
repository publication, Pages deployment, and the served public page require verification after the
reviewed change is pushed. Local tests do not establish hosted success. macOS execution
is verified here; this consumer's new workflow has not yet executed on its Ubuntu runner.
