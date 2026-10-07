# Consumer and deployment contents

This repository contains organization/profile configuration, the immutable Sourcefield release lock,
consumer workflows/tests, authored documentation, both managed READMEs, and intentional public text
artifacts. Captured inputs, generation records, generated ownership inventory, and rolling history
support reproducible output. The generator's Rust workspace and implementation/build scripts belong
in the upstream Sourcefield repository.

The selected release `v0.1.0` at `9c69b59c0d85eb26418fb7c7800be2b54ac55a8b` supplies a verified native
CLI and matching complete browser runtime. A shared installation can serve multiple consumers.
The lock records archive identities and digests; see [Setup](SETUP.md) and [Action pins](ACTION-PINS.md).

A generated candidate contains the complete Pages site and explicitly selected `README.md` and
`profile/README.md` updates. Generated ownership identifies which files may be replaced or pruned;
managed READMEs are selected authored files, not cleanup targets. The candidate preparation tool
copies tracked input paths and does not include untracked files or upload Git metadata.

`docs/pkg/`, `docs/runtime-manifest.json`, native installations, caches, `dist/`, screenshots, and
transaction/recovery artifacts remain ignored or outside the repository. The complete Pages artifact
includes the matching browser runtime. Uploading that artifact precedes checked repository publication;
deployment follows successful publication. Git source alone therefore omits runtime files that
must be restored from the locked release for a complete offline site.

Migration recovery preserves the original complete files and runtime outside the repository.
The profile's ongoing history limit is 24; retained repository history is not an all-time archive.
