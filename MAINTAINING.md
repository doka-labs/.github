# Maintenance

Edit doka-labs facts in `config/organization.toml`. Keep profile placement, radii, weights, rendering,
collection, and presentation settings in `config/profile.toml`. Its local import brings the canonical
manifest into the organization profile. Edit neither generated SVG/JSON nor managed README sections
as the content source.

## Content refresh

Review project summaries, visibility, package identities, and maintainer attribution before generating.
Approved private summaries must not expose repository URLs or implementation details. Package versions
and counts are observed registry data. New publication families need deliberate manifest changes;
discovery stays inside the configured owner and package-ID prefixes.

Select both `README.md` and `profile/README.md` during generation. Their managed project and package
sections use complete marker pairs; leave authored text outside those markers intact. Omission of a
README never authorizes its deletion. Preview in a separate directory using the pinned shared tools
and matching installation described in [Setup](SETUP.md).

Run consumer checks and inspect generated output and the actual browser. Confirm both themes, static
rendering, accessible links, mobile layout, retained history, pause, and reduced motion. Offline output
must retain its offline status. Keep `config/offline-snapshot.json` as an empty, explicitly Preview
seed required by the released CLI. Default offline preview uses this seed; recorded current observations
are reproduced with `--offline --locked`, matching retained inputs and generator identity. Strict live
failures block scheduled publication; investigate source status instead of deleting warnings or treating
fallback observations as current.

## Generator upgrades

The root `sourcefield.lock.json`, update workflow's reusable reference, and validation workflow's shared
tooling checkout must select the same full source SHA. Native CLI and browser archives must come from
that release. Obtain an authenticated new lock, then use `scripts/check_pin.py --prepare` from the
reviewed Sourcefield checkout to prepare the paired
lock/update-workflow change in a new external review directory. Inspect both files and the validation
tooling checkout and identity-check argument, then verify consumer candidates before adoption.
Update the exact reusable-workflow allowlist entry in this repository when the reviewed source SHA
changes; leave its existing allowed Actions intact. Ordinary content refreshes do not upgrade the generator.

Shared tooling must come from the selected commit. Runtime files such as `docs/pkg/` and
`docs/runtime-manifest.json`, installations, caches, and `dist/` remain ignored. The Pages artifact
includes the complete runtime even though Git does not. Generator, collection, rendering, and runtime
implementation changes belong in the upstream repository.

## Publication failures

The update workflow preserves cron `17 3 * * *` UTC and explicit two-README selection. The reusable
job generates with read-only permissions. The caller serializes publication, uploads the Pages artifact
before repository mutation, and checks the expected source HEAD before applying only owned files.
Pages deploys after successful repository publication. An upload failure or source conflict leaves the
candidate unpublished; inspect and retry from a valid source revision.

If the repository publication succeeded and deployment failed, retry deployment of the same artifact
using its saved artifact identity. Do not recollect new observations merely to retry deployment.
Verify the served page after the deployment completes; local checks do not establish public success.

## History and recovery

The migration preserves the facts and timestamps of the retained legacy archives in schema 3.
Original working files, matching runtime, and Git history have a separate external recovery copy.
`collection.history_limit = 24` governs ongoing rolling retention. It does not retain every historical
snapshot forever. Keep captured inputs, generation records, and the generated ownership inventory
tracked so a previous consumer revision and its immutable release can be replayed.

For interrupted generation, preserve the transaction journal and recovery material and confirm no
writer remains. Follow the pinned upstream
[recovery procedure](https://github.com/kdominic89/sourcefield/blob/9c69b59c0d85eb26418fb7c7800be2b54ac55a8b/docs/operations.md#publication-and-interruption),
including exact lock-token verification when a lock exists. Restore the complete matching runtime,
data, and index set. Do not remove a stale lock or mix old executable/new state without diagnosis.
Actions artifacts are temporary operational copies; retain separate recovery material when required.
