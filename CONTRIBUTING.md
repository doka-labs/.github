# Contributing

Contributions are welcome. This guide applies to every Doka Labs repository. A
repository with its own `CONTRIBUTING.md` adds its prerequisites, build and
test commands, required checks, and product rules there and follows this guide
for everything else.

Roles, decisions, and change acceptance are defined in the
[Project Governance](GOVERNANCE.md). Participation follows the
[Code of Conduct](CODE_OF_CONDUCT.md). Report suspected vulnerabilities
privately as described in the [Security Policy](SECURITY.md), and use the
[Support](SUPPORT.md) guidance for questions and defects. Do not put
production data, credentials, connection strings, or unredacted reports into
issues, pull requests, test fixtures, or logs.

## General Rules

- Write all repository content in US English and ASCII, including comments,
  documentation, and commit messages. Exceptions:
  - files a tool generates stay as written, such as EF compiled models with a
    byte order mark;
  - test data that verifies Unicode handling may contain the characters it
    tests; use an escape sequence such as `\u00A0` where a character is hard to
    tell apart from another;
  - Markdown diagrams and tables may use box-drawing characters, arrows, and
    the status marks check mark (U+2713), ballot X (U+2717), and warning sign
    (U+26A0); and
  - real names keep their spelling, for example in a license or a credit.
- Follow the repository's `.editorconfig`.
- Keep each change focused on one concern and consistent with the surrounding
  code and its boundaries.
- Fix the cause of a warning or a failing check instead of suppressing it.
- Do not introduce a third-party dependency without prior agreement in an
  issue. A dependency change keeps the lock files committed and reviews the
  complete affected graph, including transitive changes.
- Add no configuration value, flag, or public member without an active
  consumer.
- Keep test fixtures and samples synthetic; do not copy confidential schemas,
  identities, or data.
- Do not track build output, caches, test results, or personal IDE and OS
  metadata.
- Update the documentation that owns a changed behavior instead of creating a
  competing copy, and back claims about external behavior with dated primary
  sources.

## Tests

- Add regression tests for every bug fix and tests for new behavior, covering
  successful, rejected, and boundary cases.
- Each test has one Arrange, Act, and Assert sequence, separated by blank lines
  and marked with `// Arrange`, `// Act`, and `// Assert`. It verifies one
  independently observable behavior; use separate tests for distinct positive
  and negative cases. A scenario whose steps depend on each other keeps them in
  one Act phase and explains the dependency.
- Name test methods `Method_Scenario_ExpectedBehavior`, for example
  `ImportAsync_DuplicateKeyInStrictMode_RejectsAllRows`. A target engine or
  provider belongs to the scenario part.
- Use theory data for independently repeatable inputs so each case can be
  reported and rerun on its own.
- Shared fixtures may share immutable setup, but every test owns its mutable
  state and cleanup. A filtered run of a single test must work without another
  test running first.
- Coordinate concurrency with barriers, not sleeps, and keep timings
  diagnostic: no test or check may fail because of runner speed or load.

## .NET Repositories

- Keep nullable analysis and warnings-as-errors clean.
- Use the existing Rider layout. Do not run `dotnet format whitespace`; its
  output does not match that layout.
- Document public APIs with XML comments, and internal APIs where it helps IDE
  users. Explain non-obvious choices with a short WHY comment instead of
  narrating the code.
- Leave a blank line after control-flow blocks and multiline initializations
  and before `return`, except in a block of only two lines, and separate
  logical groups with blank lines.
- Keep project-wide imports in the existing `Imports.cs` files and file-specific
  imports local.
- Repository-owned asynchronous operations, including test and benchmark
  helpers and callbacks, take an explicit `CancellationToken` as their last
  parameter and forward it through cancellable work; do not add overloads
  without a token. Pass `CancellationToken.None` explicitly only where the
  entry point has no token or the operation must deliberately finish.
  Framework and runner signatures stay unchanged. Cleanup that must complete
  despite cancellation takes no token, does not inherit a canceled one, and
  explains why in a short comment.
- Record public API changes in `PublicAPI.Unshipped.txt`. Solve internal
  problems through existing public contracts; a new public method, overload, or
  option needs demonstrated necessity, reviewed alternatives, and agreement
  before implementation.
- Keep an intentionally synchronous call under test synchronous and mark it
  with a single-use inspection comment such as
  `// ReSharper disable once MethodHasAsyncOverload` plus a short reason. Do not
  disable inspections or analyzer rules for a whole file.

## Architecture Decisions

Material architecture decisions are recorded as MADR 4.0.0 records with the
Doka profile, in the location and with the template the repository names.
Each considered option lists real advantages and disadvantages, and every
supersedes or amends relationship is recorded on both sides.

## Pull Requests

- Target the branch of the affected release line, normally `main`.
- Use the pull request template. Describe the problem, the approach, the
  compatibility and security impact, and the exact commands you ran with their
  results. State which checks were not run and why an area is unaffected.
- All required checks must pass before merge. Do not create a release tag or
  publish a package to test a pull request.
- Review applies to the exact head of the pull request. A material change to
  source, tests, dependencies, workflows, generated files, or evidence requires
  a new review, and a green check does not replace inspecting the affected
  contract.

## Issues

Use the issue forms of the affected repository for defects, feature requests,
and questions. Include the exact versions involved and a minimal synthetic
reproduction.

## This Organization Profile Repository

Contributions to `doka-labs/.github` cover public organization content,
consumer configuration, documentation, workflows, and bounded consumer tests.
Sourcefield's generator and browser runtime are maintained
[upstream](https://github.com/kdominic89/sourcefield). Separate logical groups
with blank lines.

Edit shared doka-labs facts, projects, package identities, icons, and
maintainer attribution in `config/organization.toml`. Use `config/profile.toml`
for placement, rendering, collection, and presentation. Preserve its local
organization import and the intended full identities in public links. Do not
infer private-project internals or label planned packages as published.
Versions and counts are collection results, not authored profile constants.

Update consumer checks for meaningful configuration or publication contracts,
including rejected inputs. From the repository, run:

```sh
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

Provide `SOURCEFIELD_INSTALLATION` for installed-runtime integration probes and
report any skipped checks. Use the matching CLI and browser pair and the pinned
shared candidate tooling for previews; see [Setup](SETUP.md). The candidate
tool includes tracked inputs only. Review untracked new inputs separately
before relying on a committed-checkout preview.

For content or presentation changes, inspect generated SVGs, managed sections
in both READMEs, and the browser's current and history views, narrow layout,
keyboard access, pause, and reduced motion. Consumer CI uses the pinned shared
tools for offline candidate generation; it does not establish live collection
or deployment.

Keep runtime output, installations, caches, screenshots, and distribution
archives out of Git. Intentional generated public text and retained input and
history records remain tracked under the ownership manifest. Do not hand-edit
generated artifacts to repair upstream behavior. A generator upgrade changes
its authenticated lock and matching workflow references together after review.
