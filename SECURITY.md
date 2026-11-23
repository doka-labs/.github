# Security Policy

This policy applies to every Doka Labs repository. A repository with its own
`SECURITY.md` adds its scope, threat model, security invariants, and supported
versions there and follows this policy for reporting and disclosure.

Do not report a vulnerability in a public issue, pull request, discussion, or
attachment.

## Supported Versions

A repository's own security policy lists its supported versions. A repository
without one receives security fixes in its latest release only.

## Reporting a Vulnerability

Use two private channels:

1. GitHub private vulnerability reporting: the **Report a vulnerability** button
   on the **Security** tab of the affected repository. This is preferred for a
   technical report with a reproducer.
2. Email `doka-labs@tuta.com` with the subject `Security report` when you cannot
   use the GitHub form. The absence of the form is not a request to disclose
   publicly.

Include as much of the following as possible:

- the affected repository, package, and version or exact source revision;
- the runtime, framework, provider, and database engine versions that apply;
- a minimal synthetic reproducer with the expected and the observed behavior;
- the required privileges, the input an attacker controls, and the potential
  impact;
- known mitigations; and
- any intended disclosure schedule.

Do not send production dumps, live credentials, access tokens, private signing
keys, customer data, internal host names, or unredacted connection strings. Ask
before sending sensitive catalog, trace, or validation details.

### Encrypted reporting

No long-lived public PGP key is published. If a report needs encrypted
transport, open the contact through GitHub private vulnerability reporting or
send a short clear-text email that asks for encryption. The maintainer replies
in that thread with the fingerprint of a key created for this report, and all
later attachments and messages stay encrypted. The key stays limited to the
one report and never goes stale.

## Response and Coordinated Disclosure

Doka Labs is maintained by a single maintainer, who handles intake,
reproduction, severity and ownership assessment, the fix, regression tests,
release, and advisory. The targets below are response objectives, not a
guaranteed service level:

| Stage | Target |
| --- | --- |
| Acknowledgment | Within 5 business days |
| Initial triage | Within 10 business days; names any information still needed |
| Fix and advisory | Within 90 days of confirmation; critical or actively exploited defects first |

A vulnerability of medium or higher severity that is publicly known is fixed
and released within 60 days, as the
[OpenSSF Best Practices criteria][openssf] require; the 90-day private target
does not extend this.

When a target cannot be met, for example during an absence of the maintainer,
the reporter is told and given a new date. If no acknowledgment arrives, follow
up through the other private channel. If that follow-up also receives no
answer within 10 business days, the reporter may disclose publicly.

Disclosure timing and credit are agreed with the reporter. Reporters are
credited unless they ask to stay anonymous. No embargo is promised on behalf of
a reporter without their agreement, and the report is used only to fix the
vulnerability.

## Upstream Findings

No vulnerability class is excluded in advance. A defect in a dependency, such as
.NET, EF Core, a database provider or engine, GitHub, or NuGet.org, has a
different owner, but it can still expose a defect in a Doka Labs repository, so
the actual boundary is triaged first. A report is shared with an upstream
project only with the reporter's agreement, and the reporter's credit travels
with it.

## Fix Requirements

A confirmed vulnerability fix:

1. names the root cause, the affected boundary, and the affected versions;
2. adds positive and negative regression tests for the reachable path;
3. updates the repository's security documentation when an assumption or
   trust boundary changed;
4. passes the repository's normal qualification and release checks; and
5. is published with the affected and fixed versions, impact, mitigations, and
   CVE or GHSA identifiers when available, while private reproduction details
   stay private until coordinated disclosure permits publication.

Release notes name the publicly known vulnerabilities a release fixes.

## This Organization Profile Repository

The `doka-labs/.github` repository holds this policy and generates the
organization profile with Sourcefield. Report Sourcefield CLI, collection,
import, generation, installation, or browser-runtime vulnerabilities through
the pinned upstream [Sourcefield security policy][sourcefield]. Include the
exact release or source SHA, a minimal reproduction, the input an attacker
controls, and the expected impact. Use synthetic data and redact sensitive
captures.

This repository controls which facts become public, collection credentials,
workflow permissions, and repository and Pages publication. Required
boundaries include local canonical content, remote metadata, retained captures
and history, generated SVG and JSON, and browser input. Approved private
summaries are public by design; see [Privacy](PRIVACY.md).

Keep the release lock and the reusable workflow source SHA identical. Use the
authenticated matching CLI and browser pair and the scripts from that source
revision. Sourcefield validates input, escapes output, and constrains
filesystem ownership; these controls do not guarantee that reviewed releases or
arbitrary prose are free of vulnerabilities. Inspect credentials, permissions,
and output before publishing.

Generation has read-only repository permissions. The publication job checks
the expected HEAD and applies owned files; deployment depends on successful
publication of that same candidate. Do not bypass these checks to publish
stale inputs. Runtime output and caches remain ignored by Git while the
validated complete runtime is included in Pages.

[openssf]: https://github.com/ossf/best-practices-badge/blob/main/docs/criteria.md
[sourcefield]: https://github.com/kdominic89/sourcefield/blob/ef93cf245ab5dd510132e61ec3cfce64ffafa17a/SECURITY.md
