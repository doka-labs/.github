# Project Governance

This document defines how every Doka Labs repository is governed: who holds
which role, how decisions are made and changes accepted, and which continuity
limits are carried openly. A repository may name additional decision triggers,
roadmap, and release procedures in its own documentation; it follows this
document for everything else.

## Roles

The repositories are hosted by the Doka Labs GitHub organization. Dominic
Kalkbrenner (`@kdominic89`) holds the maintainer roles below.

| Role | Responsibilities | Holder |
| --- | --- | --- |
| Lead maintainer | Direction, public API, support matrix, dependencies, final decision | Dominic Kalkbrenner |
| Release maintainer | Version choice, signed tags, publication approval, release recovery | Dominic Kalkbrenner |
| Security responder | Private intake, triage, remediation, coordinated disclosure | Dominic Kalkbrenner |
| Reviewer | Independent review of correctness, compatibility, security, and evidence | Per pull request |
| Contributor | Focused changes with tests, documentation, and review responses | Anyone |

Contributors follow the [contributing guide](CONTRIBUTING.md). One person may
hold several roles. That concentration does not satisfy an independent-review,
continuity, or bus-factor criterion. A team membership, a CODEOWNERS entry, a
bot or AI review, or a successful workflow does not prove independent human
review. A role or access change requires the lead maintainer's approval, an
update of this table, and a readback of the affected GitHub, NuGet, signing, and
publication settings; a title without the required access is not an active role.

## Decision Model

Issues and pull requests are the normal public record. The lead maintainer
accepts or rejects routine changes after the applicable checks and review.

A material decision is recorded as a MADR decision record when it affects:

- public API or package boundaries;
- supported framework, provider, or database policy;
- security, privacy, diagnostics, or data-integrity semantics;
- dependency, build, test, or release authority;
- compatibility or servicing commitments; or
- architectural ownership or dependency direction.

An accepted record names its actual decision makers and acceptance history;
retrospective documentation must not invent earlier approval. A proposed
record is not authority to weaken a check or accept a risk. When evidence
changes an accepted decision, it is amended or superseded explicitly, never
silently reinterpreted in code.

When reviewers disagree, the options and evidence are recorded. The lead
maintainer decides and records the reason; unresolved objections stay in the
record.

## Change Acceptance

Every change to a repository whose default branch is protected goes through a
pull request. The initial development of a new repository and the organization
profile repository `doka-labs/.github` may commit directly to `main`.

A change is acceptable when:

- its problem and scope are clear and it adds no unrelated surface;
- every applicable automated check passes;
- behavior changes carry proportionate positive and negative tests;
- public API, compatibility, security, documentation, and release impacts are
  named; and
- review findings are resolved or recorded transparently.

Approval applies to the reviewed commit only, and a material change after
approval needs a new review. Automated checks support human review and do not
replace it.

If the normal path is unavailable during an incident, the reason and the exact
actions are recorded, privately where needed, and reviewed afterwards. An
incident never authorizes moving a release tag, replacing a published artifact,
or bypassing package identity checks.

## Release Authority

Only the release maintainer chooses a public version, creates the signed tag,
approves a protected publication, and decides the recovery from a partial
publication. Passing CI does not authorize a release.

## Conflicts of Interest

An author does not count as an independent reviewer of their own change. A
person directly involved in a conduct or security report does not decide it
when an unconflicted responder is available. If no independent path exists,
that limitation is disclosed rather than presenting the outcome as
independent. The [Code of Conduct](CODE_OF_CONDUCT.md) owns conduct
enforcement and the [Security Policy](SECURITY.md) owns vulnerability handling.

## Continuity

There is one release-capable maintainer. The repositories therefore do not
claim continuity after the loss of that person or a bus factor of two, as the
[OpenSSF Best Practices criteria][openssf] define them.

Continuity becomes claimable only after a second maintainer or a tested
succession arrangement has independently usable legal authority and access to
GitHub, NuGet, vulnerability reports, signing, publication approval, and
recovery, and a test showed that changes can be accepted and published within
one week without the unavailable person. Public evidence may name the
arrangement and its last test date, never credentials. Recovery credentials and
private report archives stay outside the repositories.

## Review Cadence

This document is reviewed at least once per calendar year and whenever a role
holder, organization setting, signing identity, trusted publisher, support
line, or decision process changes.

[openssf]: https://www.bestpractices.dev/en/criteria/1
