# Setup

This is the public `doka-labs/.github` organization profile repository. GitHub displays
`profile/README.md` on the organization overview; the root README also receives the managed
project and package sections. The interactive site is
[https://doka-labs.github.io/.github/](https://doka-labs.github.io/.github/).

## Repository automation

Select **Settings > Pages > Build and deployment > GitHub Actions** and review the `github-pages`
environment and deployment branch policy. Confirm that organization policy permits the configured
Actions and repository publication permissions. In **Settings > Actions > General**, retain the
existing selected-actions policy, including this exact reusable workflow entry:

```text
kdominic89/sourcefield/.github/workflows/generate.yml@b12eb4c72d60fbc075776a6ccc4bc15736db28af
```

The repository allowlist was verified on October 8, 2026 to include this entry. The rule authorizes
only this workflow at this commit; it does not change other repositories or allow every external
action. See
[GitHub's documented workflow allowlist syntax](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-select-actions-and-reusable-workflows-to-run).

The update workflow supports manual dispatch and the daily cron `17 3 * * *` (03:17 UTC).
It calls Sourcefield's read-only reusable generator at
`b12eb4c72d60fbc075776a6ccc4bc15736db28af`, matching `sourcefield.lock.json`. Strict live collection
must succeed before publication. The caller uploads the complete candidate Pages artifact, checks
the expected repository HEAD, publishes only owned output and selected READMEs, and then deploys.
A push or pull request runs a read-only validation job using shared tooling from the same source SHA:
lock/pin checks, authenticated release installation, consumer tests, offline candidate generation,
and complete artifact validation.

Use **Actions > Update SOURCEFIELD > Run workflow** for an intentional refresh. Check the completed
repository publication and Pages deployment, then verify the served page. Configured automation or
a locally generated candidate does not prove a public deployment succeeded. If deployment fails
after repository publication, retry deployment of that same saved artifact.

## Optional local preview

Local preview uses Python 3.11+ and shared tooling from a Sourcefield checkout at exactly
`b12eb4c72d60fbc075776a6ccc4bc15736db28af`. Confirm that checkout with `git rev-parse HEAD` before
using its scripts. A shared installation must contain the verified native CLI and matching browser
runtime selected by this consumer's lock. Reuse that installation across consumers; no per-repository
manual installation or Rust build is needed.

If this machine has no matching installation, bootstrap once into a new directory using the pinned
checkout and GitHub CLI with release and attestation verification support. This initial step needs
network access and suitable read authentication:

```sh
SOURCEFIELD_SOURCE=/path/to/pinned/sourcefield
export SOURCEFIELD_INSTALLATION=/path/to/shared/sourcefield-v0.1.1
CONSUMER_REPOSITORY=/path/to/doka-labs

python3 -B "$SOURCEFIELD_SOURCE/scripts/bootstrap_release.py" \
  --lock "$CONSUMER_REPOSITORY/sourcefield.lock.json" \
  --destination "$SOURCEFIELD_INSTALLATION"
```

Keep existing installations intact. The bootstrap verifies the immutable release, archive digests,
and attestations before publishing a matched CLI/runtime pair. See the pinned upstream
[installation contract](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/distribution.md#verified-installation).

Check the consumer pin, then generate into a new external directory:

```sh
python3 -B "$SOURCEFIELD_SOURCE/scripts/check_pin.py" \
  --lock "$CONSUMER_REPOSITORY/sourcefield.lock.json" \
  --workflow "$CONSUMER_REPOSITORY/.github/workflows/update-profile.yml"

python3 -B "$SOURCEFIELD_SOURCE/scripts/consumer_candidate.py" \
  --source "$CONSUMER_REPOSITORY" \
  --destination /path/to/new-external-preview \
  --installation "$SOURCEFIELD_INSTALLATION" \
  --readmes '["README.md", "profile/README.md"]' \
  --offline

python3 -B -m http.server 8000 \
  --bind 127.0.0.1 --directory /path/to/new-external-preview/docs
```

Open `http://127.0.0.1:8000/` for module and WASM loading. The candidate tool reads tracked consumer
inputs; it omits untracked new files. Use the reviewed committed input set for this path, and handle
pre-commit review separately. The destination must not already exist. The wrapper selects
`--fallback-snapshot assets/source-snapshot.json` for retained observations and live fallback.
Offline generation and locked replay require this capture and preserve its existing bytes, original
date, source statuses, and package observations. Missing offline/replay captures fail without
substituting the empty authoring seed. Neither mode performs fresh collection.

The separate `assets/render-snapshot.json` stores effective policy-filtered rendering input. Offline
Preview has empty `fetched_at` there while the retained source capture keeps its genuine date. Keep
both snapshots and the matching generation record tracked. `--offline --locked` verifies recorded
inputs and generator identity and reuses the recorded effective input without applying today's
credential selection. Envelope schema 2 binds six fixed inputs. Only envelope schema 2 is supported.
Older generator records require regeneration with a matching CLI/runtime pair.

Omit `--offline` for a strict online refresh. Its first run can collect without a previous capture or
`config/offline-snapshot.json`. Malformed existing captures, unsupported snapshot schemas, and
filesystem errors remain fatal; strict incomplete or failed collection leaves output unchanged.
Without a usable dated prior capture,
collection failure cannot succeed through fallback. The empty seed remains an initial direct native
offline-authoring input. These rules apply to the selected published v0.1.1 release.

## Consumer checks

From the consumer repository, run:

```sh
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

Installed-runtime integration probes require `SOURCEFIELD_INSTALLATION` to identify the matching
shared installation. Check the output for skipped probes when that installation is unavailable.
Inspect dark, light, and static SVGs, both READMEs, current and retained historical browser views,
mobile layout, keyboard navigation, pause, and reduced motion before publication. The generator's
Rust and browser implementation tests belong upstream.
