# Architecture

This repository is the configuration and public output consumer for the doka-labs organization
profile. Sourcefield owns generation and the browser runtime in
[kdominic89/sourcefield](https://github.com/kdominic89/sourcefield). The consumer selects immutable
release `v0.1.1`, source commit `b12eb4c72d60fbc075776a6ccc4bc15736db28af`.

## Ownership

| Surface | Owner and purpose |
| --- | --- |
| `config/organization.toml` | Canonical public doka-labs facts: projects, technologies, publications, packages, icons, and maintainer attribution |
| `config/profile.toml` | Organization presentation, local manifest import, collection policy, placement, radii, and weights |
| `sourcefield.lock.json` | Matched immutable native CLI and browser release identities and archive digests |
| `.github/workflows/` | Consumer validation, refresh schedule, repository publication, and Pages deployment |
| `assets/` and generated `docs/` text | Captured inputs, ownership inventory, current state, rendered output, and retained history |
| `README.md` and `profile/README.md` | Authored context with explicitly managed project and package sections |
| `tests/` | Consumer configuration, publication, and presentation contracts |

The local import in `config/profile.toml` composes `config/organization.toml`. Organization facts
are edited once in that manifest; the profile keeps its own layout. The maintainer is
[kdominic89](https://github.com/kdominic89), Administrator & Core Maintainer. Approved private-project
summaries remain public editorial content, without private repository URLs or implementation details.

Package discovery is scoped to doka-labs and the configured NuGet families. The three publication
columns retain full package identities in links and use presentation labels where configured.
Versions and package counts come from collection; they are not authored constants. SafeMigrations
uses the built-in `database-safe` icon selected by the canonical manifest.

## Generation and publication

The update workflow calls the full-SHA reusable `generate.yml`; its SHA must equal the root lock.
Generation uses the matching CLI/runtime pair and returns a validated complete candidate with both
selected READMEs. It has read-only repository permissions and does not publish.

Push and pull request validation check out the same pinned shared tooling, verify the lock and caller
pin, bootstrap the matched release pair, run consumer checks, and generate/validate an isolated offline
candidate with read-only permissions. The manual and daily refresh use strict live collection.
Publication is serialized: upload the candidate's complete Pages artifact first, then apply owned
files and the selected README sections against the expected source HEAD. Repository publication must
succeed before the dependent Pages deployment. An obsolete source revision or failed push stops deployment.

The browser runtime, including `docs/pkg/` and `docs/runtime-manifest.json`, is supplied by the
release and included in the complete Pages artifact. Generation verifies the raw installed runtime
before projecting organization identity into site metadata and updating the projected manifest.
Generated `docs/` is output, not a substitute for the installed raw runtime. Runtime files, local caches, and `dist/` remain
ignored by Git. This repository contains no copied Rust workspace or runtime build pipeline.

## State and recovery

The consumer wrapper selects `assets/source-snapshot.json` as retained observation input.
Offline generation and locked replay preserve its exact bytes, original date, and source statuses.
The separate `assets/render-snapshot.json` records the effective input: an offline Preview is undated,
while the retained Live capture keeps its actual date. A generation-record schema 2 envelope binds
six captured inputs and the exact authored configuration and generator identity. Regenerate with the
matched release pair after an upgrade; older generator records cannot be replayed by the new pair.

Offline updates require the retained observation capture; they do not substitute the empty native
first-authoring seed. A first online refresh may collect without a prior capture or seed. Malformed
existing captures, missing required imports, and strict collection failures prevent publication.
Preview and fallback data must not be relabeled as live. Offline, replay, and no-history generation
retain the existing archive/index bytes; successful live refresh applies rolling retention.

Migration converts retained legacy state and archives to schema 3 while preserving their facts
and timestamps. A complete original recovery copy is kept outside the repository. The configured
`history_limit = 24` is rolling retention, not a promise of all-time history. Recover a complete
matching data/runtime set; see [Maintenance](MAINTAINING.md).

README SVGs are image surfaces. Accessible project/package links and the Pages link remain outside
them. Pages provides the interactive field, semantic navigation, pause, and reduced-motion behavior
from the pinned runtime. See [Sources](SOURCES.md) for the upstream contracts.
