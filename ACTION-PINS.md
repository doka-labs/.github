# GitHub Action pins

The consumer uses the fixed references in the released Sourcefield
[consumer template](https://github.com/kdominic89/sourcefield/blob/9c69b59c0d85eb26418fb7c7800be2b54ac55a8b/docs/consumer-workflow.yml.template).
Their official commit identities were checked on October 7, 2026. Release labels are descriptive;
the executable reference is the full commit SHA. This is a fixed-release adoption, not a claim that
these actions are the newest releases.

| Action | Template release label | Verified commit |
| --- | --- | --- |
| actions/checkout | v7.0.1 | [3d3c42e5aac5ba805825da76410c181273ba90b1](https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1) |
| actions/download-artifact | v8.0.1 | [3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c](https://github.com/actions/download-artifact/commit/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c) |
| actions/upload-pages-artifact | v5.0.0 | [fc324d3547104276b827a68afc52ff2a11cc49c9](https://github.com/actions/upload-pages-artifact/commit/fc324d3547104276b827a68afc52ff2a11cc49c9) |
| actions/deploy-pages | v5.0.1 | [368f82528645a54fb793d4d04e342629a3f51346](https://github.com/actions/deploy-pages/commit/368f82528645a54fb793d4d04e342629a3f51346) |

The update workflow pins
`kdominic89/sourcefield/.github/workflows/generate.yml@9c69b59c0d85eb26418fb7c7800be2b54ac55a8b`.
That reference equals `sourcefield.lock.json` and selects the source of immutable `v0.1.0`.
Shared `scripts/check_pin.py` validates the lock/update-workflow agreement; the reusable workflow
checks its own executing source identity as well. The validation workflow checks out shared tooling
at that same SHA, verifies the lock/update-workflow agreement, and uses the released CLI/runtime pair
for consumer tests and an isolated offline candidate. Its job has read-only repository permissions.

See GitHub's [reusable workflow guidance](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
for literal SHA references. Pinning preserves selected identity; review job permissions and behavior
when adopting a different release.
