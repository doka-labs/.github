# Consumer and deployment contents

This repository contains organization/profile configuration, the immutable Sourcefield release lock,
consumer workflows/tests, authored documentation, both managed READMEs, and intentional public text
artifacts. Captured inputs, generation records, generated ownership inventory, and rolling history
support reproducible output. The generator's Rust workspace and implementation/build scripts belong
in the upstream Sourcefield repository.

The selected release `v0.1.1` at `b12eb4c72d60fbc075776a6ccc4bc15736db28af` supplies a verified native
CLI and matching complete browser runtime. A shared installation can serve multiple consumers.
The lock records archive identities and digests; see [Setup](SETUP.md) and [Action pins](ACTION-PINS.md).

A generated candidate contains the complete Pages site and explicitly selected `README.md` and
`profile/README.md` updates. Generated ownership identifies which files may be replaced or pruned;
managed READMEs are selected authored files, not cleanup targets. The candidate preparation tool
copies tracked input paths and does not include untracked files or upload Git metadata.

Keep `assets/source-snapshot.json`, `assets/render-snapshot.json`, and the matching generation
record tracked. Offline generation and locked replay preserve existing source capture bytes, date,
and source statuses; the effective render input is separate and offline Preview is undated there.
Envelope schema 2 binds six fixed inputs. Older records fail the exact recorded generator identity
check; regenerate with a matching CLI/runtime pair after upgrading. Missing offline/replay captures
fail. First online refresh can collect without a prior capture or seed; malformed captures and
unsupported snapshot schemas remain fatal.

`docs/pkg/`, `docs/runtime-manifest.json`, native installations, caches, `dist/`, screenshots, and
transaction/recovery artifacts remain ignored or outside the repository. The complete Pages artifact
includes the matching browser runtime. Uploading that artifact precedes checked repository publication;
deployment follows successful publication. Git source alone therefore omits runtime files that
must be restored from the locked release for a complete offline site.

Migration recovery preserves the original complete files and runtime outside the repository.
Restore both snapshots and their matching generation record with the complete data/runtime set.
The profile's ongoing history limit is 24; retained repository history is not an all-time archive.
