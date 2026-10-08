# Primary sources

Selected release and consumer upgrade contracts checked on October 8, 2026. Upstream source documentation below was
read at commit `b12eb4c72d60fbc075776a6ccc4bc15736db28af`, the source of immutable release `v0.1.1`.
These links explain the contracts; successful local or hosted execution requires separate evidence.

| Consumer contract | Primary source |
| --- | --- |
| Matched release lock, verified shared installation, workflow pin, and candidate publication | [Pinned Sourcefield distribution](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/distribution.md) |
| Explicit destinations, retained/raw and effective render inputs, schema 2 replay, and recovery | [Pinned Sourcefield operations](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/operations.md) |
| Canonical content imports and consumer layout | [Pinned Sourcefield configuration](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/configuration.md) |
| Built-in icon identity, including `database-safe` | [Pinned Sourcefield icons](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/icons.md) |
| Caller-owned permissions, checked publication, and deployment order | [Pinned consumer workflow template](https://github.com/kdominic89/sourcefield/blob/b12eb4c72d60fbc075776a6ccc4bc15736db28af/docs/consumer-workflow.yml.template) |
| GitHub reusable workflow calling convention and immutable SHA references | [GitHub reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows) |
| Organization profile README placement | [GitHub organization profiles](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile) |
| Pages artifact and deployment job requirements | [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) |
| NuGet owner/family discovery, prereleases, and paging | [NuGet SearchQueryService](https://learn.microsoft.com/en-us/nuget/api/search-query-service-resource) |
| Package version list resource | [NuGet PackageBaseAddress](https://learn.microsoft.com/en-us/nuget/api/package-base-address-resource) |

Organization descriptions, project status, private summaries, and maintainer attribution are approved
authored facts in `config/organization.toml`. The owner-approved updates include NestedSet,
SafeMigrations SQLite and SQL Server adapters, three NuGet columns, and the built-in safe motif.
Package links identify published registry entries; their current versions and counts are collected.

The [SQL Server package](https://www.nuget.org/packages/Doka.EntityFrameworkCore.SafeMigrations.SqlServer/)
and its [official flat-container version list](https://api.nuget.org/v3-flatcontainer/doka.entityframeworkcore.safemigrations.sqlserver/index.json)
provided publication evidence on October 7, 2026: the captured list contained `10.4.6`, `10.4.7`, and
`10.4.8`. That is a dated observation supporting the package identity, not a permanent current-version
claim or a version to copy into authored profile content.

Action commits and their released-template evidence are listed in [Action pins](ACTION-PINS.md).
The organization repository is [doka-labs/.github](https://github.com/doka-labs/.github); its Pages
address is [doka-labs.github.io/.github](https://doka-labs.github.io/.github/).
