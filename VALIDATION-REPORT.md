# Validation

Verified locally on October 9, 2026 with the published Sourcefield `v0.1.2` CLI and matching
browser runtime at source commit `cd2e2b6779c82a3f64346a47d40da4967fcc0dc5`. The installation
was authenticated against the immutable release, both archive digests, and GitHub attestations.
This report records the consumer upgrade on macOS; it does not claim hosted validation or a
new public deployment.

## Current output

The regenerated output is explicitly **Preview**, state `81F371AB75D6FFBF`, with 21 nodes,
35 edges, four projects, ten NuGet packages, and the unchanged 1800 by 1552 canvas. The latest published baseline
consumer revision is `d77db45129f83d55f29af2edae9d932ce70293ea`.

The canonical manifest enables `repository_caption = { source = "selected-projects" }`.
The organization hub shows `3 public / 1 private repos`, with the same accessible label.
RelationalLab remains a private, unlinked abstraction. These are curated project counts, not
an account inventory. Project and observation data remain unchanged. Graph differences are the caption, semantic
hash and explicit offline Preview mode, date and source-status flags.

The retained `assets/source-snapshot.json` is byte-identical to the baseline. Its Live status
and original collection date, `2026-10-08T10:38:04.800390734+00:00`, remain intact. Offline
generation performs no collection. The effective `assets/render-snapshot.json` is materialized as
an undated Preview from those retained observations. The schema 2 record binds six captured inputs
and the authored profile digest to the released generator identity.

Project/package content, geometry, maintainer attribution, collection settings, both README
files, and all 24 retained archives plus their index remain byte-identical. The canonical
manifest differs only by the caption setting. Installed runtime files are generated from the
matching release; compiled WASM and its runtime manifest remain ignored by Git.

## Executed checks

| Check | Result |
| --- | --- |
| Release, native/browser digests and attestations | Passed; authentic matching v0.1.2 installation |
| Existing consumer tests with that installation | 15 passed, zero skipped; no new tests added |
| Lock, reusable workflow and both validation identities | Passed; all select the released source SHA |
| Complete generated artifact validation | Passed; 21 nodes, 35 edges, ten packages, matching runtime/WASM |
| Both workflows with actionlint | Passed |
| Data, layout, README and history preservation | Passed by exact byte/hash comparison |
| Locked native replay | All 77 candidate files reproduce byte for byte |
| Both consumers using the same new canonical manifest | Passed; identical captured manifest bytes and caption, no other graph changes |
| Released runtime in Chromium | Passed at 1200/390 pixels: WASM, captions/ARIA, reduced motion, no horizontal overflow, usable mobile inspector close |
| Retained historical browser view | One archive loads and returns to the current caption; all 24 archives are retained and validated |
| README width comparison | Before/after screenshots at 820 and 343 content pixels; new caption does not overlap project text |

Representative commands actually run, with external paths abbreviated:

```sh
SOURCEFIELD_INSTALLATION=/path/to/verified/installation \
  python3 -B -m unittest discover -s tests -p 'test_*.py' -v

python3 -B "$SOURCEFIELD_SOURCE/scripts/check_pin.py" \
  --lock sourcefield.lock.json --workflow .github/workflows/update-profile.yml \
  --own-commit cd2e2b6779c82a3f64346a47d40da4967fcc0dc5

python3 -B "$SOURCEFIELD_SOURCE/scripts/consumer_candidate.py" \
  --source /path/to/prepared/consumer --destination /path/to/new/candidate \
  --installation "$SOURCEFIELD_INSTALLATION" \
  --readmes '["README.md", "profile/README.md"]' --offline

python3 -B "$SOURCEFIELD_SOURCE/scripts/validate_artifact.py" \
  --root /path/to/verified/candidate --workflow-root /path/to/prepared/consumer --require-wasm

actionlint .github/workflows/update-profile.yml .github/workflows/validate.yml
```

The focused browser probe, screenshots, exact commands, preservation comparisons and replay
logs are retained externally. The upstream generator suites were not rerun for this consumer
upgrade. The personal-profile proof uses a truthful local import of the unpublished canonical
manifest in an external fixture; it is not evidence of a published remote manifest revision.
The personal product repository was not modified.

## Publication boundary

The exact new reusable-workflow allowlist entry was read back from GitHub on October 9, 2026;
see [Setup](SETUP.md). Existing permissions, schedule, publication and deployment ordering stay
unchanged.

Publish the personal consumer's v0.1.2 upgrade before publishing this caption-bearing canonical
manifest. Its current v0.1.1 generator imports this repository's `main` and rejects the new field.
The compatible personal upgrade is prepared externally; it has not been applied or published.
See [Maintenance](MAINTAINING.md#generator-upgrades) for sequencing and rollback requirements.

Commit, push, hosted Validate SOURCEFIELD, and the subsequent Update SOURCEFIELD publication
and Pages deployment remain separate steps. Local success does not establish hosted success.
