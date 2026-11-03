# Validation

Verified locally on November 3, 2026 with the published Sourcefield `v0.1.3` CLI and matching
browser runtime at source commit `ef93cf245ab5dd510132e61ec3cfce64ffafa17a`. The immutable
release, lock asset, native/browser archive digests and source-bound GitHub attestations passed
verification before the executable was used. This report records local upgrade checks; hosted
validation and publication remain separate.

## Prepared upgrade and preserved output

The lock, reusable workflow, validation tooling checkout and executing-identity argument all
select that same source commit. Caller permissions, schedule `17 3 * * *` UTC, two-README
selection, serialization, checked publication and Pages deployment ordering are unchanged.

The active repository's configuration, generated output, captures, ownership manifest, both
READMEs and all 24 retained archives plus their index remain unchanged. A separate offline
candidate uses the new released pair. Its complete graph equals the existing graph: state
`81F371AB75D6FFBF`, 21 nodes, 35 edges, four projects, ten packages and a 1800 by 1552 canvas.
The `3 public / 1 private repos` caption and unlinked private RelationalLab remain intact.

Both READMEs, the canonical manifest, layout configuration, retained source capture and history
are byte-identical in that candidate. It is explicitly Preview and performs no fresh collection;
its package observations are retained values, not a claim about current NuGet releases. The
candidate's schema 2 generation record binds the v0.1.3 identity and its six captured inputs.
Locked replay reproduced all 77 candidate files byte for byte.

Only the next successful strict live Update SOURCEFIELD run publishes refreshed output and
replay records for the new pair. The pin update does not relabel the existing generated record.
The canonical manifest adds no new fields, so the personal consumer's existing v0.1.2 pin remains
compatible while it awaits its own upgrade.

## Executed checks

| Check | Result |
| --- | --- |
| Immutable release, lock, native/browser archives and attestations | Passed |
| Existing consumer tests with the released installation | 15 passed; zero skipped |
| Lock, reusable workflow and both validation identities | Passed |
| Both workflows with actionlint | Passed |
| Isolated offline candidate and complete artifact validation | Passed; required real WASM present |
| Graph, layout, README, source capture and history preservation | Passed by exact comparisons |
| Locked replay with the new CLI/runtime pair | All 77 candidate files reproduced byte for byte |
| Released runtime in Chromium, desktop and mobile | Passed; dark/light, WASM, keyboard, links, pause, reduced motion and mobile inspector close |
| Static/image surfaces and retained-history browser handling | Passed in the same browser gate |

Representative commands actually run, with external paths abbreviated:

```sh
SOURCEFIELD_INSTALLATION=/path/to/verified/installation \
  python3 -B -m unittest discover -s tests -p 'test_*.py' -v

python3 -B "$SOURCEFIELD_SOURCE/scripts/check_pin.py" \
  --lock sourcefield.lock.json --workflow .github/workflows/update-profile.yml \
  --own-commit ef93cf245ab5dd510132e61ec3cfce64ffafa17a

python3 -B "$SOURCEFIELD_SOURCE/scripts/consumer_candidate.py" \
  --source /path/to/consumer --destination /path/to/new/candidate \
  --installation "$SOURCEFIELD_INSTALLATION" \
  --readmes '["README.md", "profile/README.md"]' --offline

python3 -B "$SOURCEFIELD_SOURCE/scripts/validate_artifact.py" \
  --root /path/to/verified/candidate --workflow-root /path/to/consumer --require-wasm

actionlint .github/workflows/update-profile.yml .github/workflows/validate.yml

node "$SOURCEFIELD_SOURCE/scripts/verify-browser.mjs" \
  --site /path/to/verified/candidate/docs --playwright-module /path/to/playwright/index.mjs \
  --browser /path/to/installed/chromium --output /path/to/browser-evidence
```

The browser run used explicit installed Node and Chromium paths. Initial local launch attempts
found neither `node` on PATH nor Playwright's optional headless-shell executable; the successful
run selected the existing Node and matching full Chromium installation. No product change or
browser sandbox bypass was needed. The upstream Rust and implementation suites were not rerun
for this consumer pin/documentation update; no new tests were added.

Exact commands, authentication logs, preservation hashes and browser screenshots are retained
outside the repository under the git-profile review directory.

## Publication prerequisite

GitHub's repository selected-actions policy was read on November 3, 2026. It still permits the
older workflow pins and does not yet contain this required entry:

```text
kdominic89/sourcefield/.github/workflows/generate.yml@ef93cf245ab5dd510132e61ec3cfce64ffafa17a
```

Add that entry in **Settings > Actions > General** alongside the existing allowed patterns.
This local upgrade does not modify repository settings. After commit and push, confirm
Validate SOURCEFIELD, then run Update SOURCEFIELD and verify repository publication and Pages.
No new hosted run or public deployment is claimed by this report.
