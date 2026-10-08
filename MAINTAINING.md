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

A supplied maintainer role must remain nonempty after trimming whitespace. This rule also applies
to retained archives from older generators: a supplied blank role rejects generation. Omitted
optional maintainer attribution is valid; supplied attribution requires a nonblank role. Inspect
history before an upgrade; do not silently rewrite or discard an archive to bypass admission.

Select both `README.md` and `profile/README.md` during generation. Their managed project and package
sections use complete marker pairs; leave authored text outside those markers intact. Omission of a
README never authorizes its deletion. Preview in a separate directory using the pinned shared tools
and matching installation described in [Setup](SETUP.md).

Run consumer checks and inspect generated output and the actual browser. Confirm both themes, static
rendering, accessible links, mobile layout, retained history, pause, and reduced motion. Offline output
must retain its offline status. The wrapper selects
`--fallback-snapshot assets/source-snapshot.json` for retained observations and live fallback.
Offline generation and replay preserve that existing capture byte for byte, including its date,
source statuses, and approved observations. The separate `assets/render-snapshot.json` records
effective privacy-filtered input; offline Preview is undated there. Keep both snapshots and the
matching generation record tracked. A previously approved raw aggregate can remain retained while
current rendering omits it. Locked replay uses the recorded effective input rather than today's
credential selection.

Generation-record envelope schema 2 binds six fixed inputs. Only envelope schema 2 is supported.
Older generator records require regeneration with a matching CLI/runtime pair. Validation
distinguishes record schema, generator identity, authored-input drift, and capture corruption.
Regenerate with the matching pair after an implementation upgrade before validating or replaying.

Missing offline/replay observations or required import captures fail without seed substitution.
A first online refresh may collect without a prior capture or seed; malformed existing captures,
unsupported snapshot schemas, and filesystem errors remain fatal. `config/offline-snapshot.json`
remains an initial direct native offline-authoring seed. Offline, no-history, and replay runs retain
existing archive/index bytes; allowed live generation applies rolling retention. Strict live failures
block scheduled publication; investigate source status instead of deleting warnings or treating
fallback observations as current.

## Repository caption

The canonical manifest owns `repository_caption = { source = "selected-projects" }`.
The organization hub shows `3 public / 1 private repos` in SVG text and its accessible label.
This counts the four curated projects, including the private, unlinked RelationalLab; it is not
an account inventory and needs no token for private repositories. Both profiles import this
same caption setting. Labels and the suffix can be edited in the manifest without another
Sourcefield release once all importers support the field.

## Generator upgrades

The root `sourcefield.lock.json`, update workflow's reusable reference, and validation workflow's shared
tooling checkout must select the same full source SHA. Native CLI and browser archives must come from
that release. Obtain an authenticated new lock, then use `scripts/check_pin.py --prepare` from the
reviewed Sourcefield checkout to prepare the paired
lock/update-workflow change in a new external review directory. Inspect both files and the validation
tooling checkout and identity-check argument, then verify consumer candidates before adoption.
Update the exact reusable-workflow allowlist entry in this repository when the reviewed source SHA
changes; leave its existing allowed Actions intact. Ordinary content refreshes do not upgrade the generator.

Upgrade every importer before publishing a newly supported field in the canonical manifest.
The personal profile currently imports this repository's `main`; its `v0.1.1` generator cannot
read `repository_caption`. Publish its upgrade to `v0.1.2` before publishing this manifest.
Existing captures remain usable during that first upgrade. Subsequent caption edits need only
a normal profile refresh in each consumer, with no release or pin change.

A rollback to `v0.1.1` must restore the compatible manifest, captures, generated state, ownership,
and release pins together. That version rejects caption fields in configuration and states;
do not replay caption-bearing input or archives with the older executable.

Shared tooling must come from the selected commit. Runtime files such as `docs/pkg/` and
`docs/runtime-manifest.json`, installations, caches, and `dist/` remain ignored. The Pages artifact
includes the complete runtime even though Git does not. Generator, collection, rendering, and runtime
implementation changes belong in the upstream repository. The generator verifies the complete raw
installed runtime before projecting profile identity, palette, favicon, and page metadata into output.
The projected manifest updates those output digests while retaining generator identity. Generated
`docs/` is not a replacement for the raw runtime supplied through `--runtime`.

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
Restore retained source and effective render snapshots together with their matching generation record.

For interrupted generation, preserve the transaction journal and recovery material and confirm no
writer remains. Follow the pinned upstream
[recovery procedure](https://github.com/kdominic89/sourcefield/blob/cd2e2b6779c82a3f64346a47d40da4967fcc0dc5/docs/operations.md#publication-and-interruption),
including exact lock-token verification when a lock exists. Restore the complete matching runtime,
data, and index set. Do not remove a stale lock or mix old executable/new state without diagnosis.
Actions artifacts are temporary operational copies; retain separate recovery material when required.
