# Support

This policy applies to every Doka Labs repository and routes questions and
reports to the channel that can handle them safely. A repository with its own
`SUPPORT.md` adds its documentation, report details, ownership, and supported
versions there and follows this policy for everything else.

Public support is best effort. It is not a commercial support agreement, a
response-time guarantee, or an emergency incident-response service.

## Choose the Correct Channel

| Request | Channel | Public? |
| --- | --- | --- |
| Suspected security vulnerability | Follow the [Security Policy](SECURITY.md) | No |
| Harassment or other conduct concern | Follow the [Code of Conduct](CODE_OF_CONDUCT.md) | No |
| Reproducible defect | Bug report form of the affected repository | Yes |
| Feature or compatibility proposal | Feature request form of the affected repository | Yes |
| Usage, configuration, or capability question | Support question form of the affected repository | Yes |

Do not send ordinary usage questions to the private security or conduct
channels. Do not post vulnerabilities, credentials, confidential customer
information, or production data in public issues, pull requests, or
attachments.

Issues are available only while GitHub Issues are enabled and only to people
with read access to the repository. For a private repository, this policy does
not create a separate general-support mailbox.

## Before Opening an Issue

Check the repository's README, documentation, samples, support matrix, and
existing issues. Reduce the behavior to the smallest synthetic case that still
shows it.

An actionable report normally includes:

- the exact package version, or the source revision for an unpublished build;
- the .NET, framework, provider, driver, and database engine versions that
  apply, and the operating system and architecture;
- relevant proxy, pooler, cluster, or managed-service topology;
- a minimal synthetic reproduction and the exact commands that run it;
- the expected and the actual outcome, with any stable failure code and
  exception type; and
- the last working version when reporting a regression.

When no database is involved, say so and omit the database details. Do not
invent environment information to complete a form. Use fenced code blocks for
code, SQL, selected logs, query plans, and stack traces. A small executable
repository is preferred when a fragment cannot preserve the behavior.

## Safe Diagnostic Sharing

Use disposable databases and synthetic data for reproductions. Replace
sensitive names and values consistently, so that relationships, ordering, and
identifier behavior stay reproducible.

Remove passwords, tokens, connection strings, private signing material,
personal data, customer and tenant identifiers, internal host names,
confidential schema names, and production paths from every public report and
attachment. Generated SQL, logs, query plans, reports, and traces can contain
mapped names or application values; review them before sharing. The absence of
credentials does not make a diagnostic artifact safe to publish. Do not upload
production dumps, backups, or complete unredacted logs.

If an operation fails in production, preserve the original error, the database
state, and the available evidence before any recovery attempt, and use your
tested recovery procedure. Do not delete migration history, weaken a safety
setting, or repeat an unknown destructive operation merely to make an issue
reproducible.

## Supported Scope

Each repository's support matrix is authoritative for its packages, runtimes,
providers, and engines. This policy does not extend that matrix or promise a
release date.

A report is assessed at the repository's boundary before it is redirected. If
the evidence locates a defect in a dependency, such as .NET, EF Core, a
provider, a driver, or a database engine, the maintainer links a minimal
upstream reproduction and keeps any repository-specific impact and regression
test. A dependency boundary alone is not a reason to redirect a report.

General application architecture, database administration, unsupported
versions or configurations, and automatic reconstruction of unknown legacy
data are not maintained contracts. They may receive guidance without expanding
the support matrix.

## Response and Lifecycle

Doka Labs is maintained by a single maintainer. Priority follows security
impact, data integrity, regressions in the supported matrix, reproducibility,
and the number of affected users, not the order of submission. The maintainer
may ask for a smaller reproduction or further sanitized evidence.

An issue may be closed as a duplicate, as documented expected behavior, as an
unsupported configuration, or as an upstream defect, or when essential
reproduction details stay unavailable. The reason and relevant references are
recorded, and new evidence can justify reopening it.

An accepted feature request, a merged change, or a closed issue does not prove
that a package is available; only a published release does.

Security reports follow the targets of the [Security Policy](SECURITY.md);
those targets do not apply to ordinary support.
