# Security

Report vulnerabilities in this organization's configuration or publication workflow through
[GitHub private vulnerability reporting](https://github.com/doka-labs/.github/security/advisories/new)
when that repository feature is available. This document does not establish another organization
security contact. Do not place credentials or private project information in public issues.

Report Sourcefield CLI, collection, import, generation, installation, or browser-runtime vulnerabilities
through the pinned upstream
[security policy](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/SECURITY.md).
Include the exact release/source SHA, minimal reproduction, input an attacker controls, and expected
impact. Use synthetic data and redact sensitive captures.

This consumer controls which facts become public, collection credentials, workflow permissions,
and repository/Pages publication. Required boundaries include local canonical content, remote metadata,
retained captures/history, generated SVG/JSON, and browser input. Approved private summaries are public
by design; see [Privacy](PRIVACY.md).

Keep the release lock and reusable workflow source SHA identical. Use the authenticated matching
CLI/browser pair and scripts from that source revision. Sourcefield validates input, escapes output,
and constrains filesystem ownership; these controls do not guarantee that reviewed releases or arbitrary
prose are vulnerability-free. Inspect credentials, permissions, and output before publishing.

Generation has read-only repository permissions. The consumer publication job checks the expected
HEAD and applies owned files; deployment depends on successful publication of that same candidate.
Do not bypass these checks to publish stale inputs. Runtime output and caches remain ignored by Git
while the validated complete runtime is included in Pages.
