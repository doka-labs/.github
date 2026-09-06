# Validation

Verified locally on September 6, 2026. This report describes the organization port; it does not
claim a GitHub CI run or deployment before publication.

| Check | Result |
| --- | --- |
| Full workspace unit tests | 61 passed, including organization scope and raw-output regression |
| Python tooling and generated geometry | 15 passed |
| Node runtime and helper tests | 16 passed |
| Rustfmt, all-target check, strict Clippy, private rustdoc | Passed |
| wasm32 check and release WASM build | Passed with wasm-pack 0.15.0 |
| Canonical artifact validation | 15 nodes, 25 edges, three projects, six packages |
| Real Chromium suite | 12 interaction groups, 14 ring directions, six signals, three radial curves |
| Browser runtime | Native WASM/WebGL2 and forced JavaScript/Canvas2D fallback passed |
| Accessibility and layout | Keyboard, touch, mobile, light/dark and reduced-motion checks passed |
| Browser errors and CSP | No errors or violations in normal load |
| Strict live collection | Public organization GitHub and six NuGet packages collected successfully |

Reproduce with the commands in [Setup](SETUP.md). Browser screenshots and JSON are emitted to
ignored `dist/browser-checks/`. Release WASM/glue are ignored and built again for deployment.
The checked-in artifact is an offline preview. Live verification wrote only temporary outputs.

The scoped snapshot regression first reproduced personal observations in the raw source file.
The shared scope boundary now runs before both raw persistence and graph construction; the test
checks every generated file and verifies that approved organization/package data is preserved.

The initial publication still requires creating the public doka-labs/.github repository, enabling
Pages with GitHub Actions and running the update workflow. No remote settings are changed by local
verification. See [Setup](SETUP.md#github-pages) for those explicit publication steps.
