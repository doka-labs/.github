# Privacy

The organization profile publishes curated project descriptions, technology labels and six NuGet
packages. RelationalLab is private; its owner-approved name and short stack description are public
by design. No repository URL or implementation details are emitted for that private project.
The `private-abstract` label means curated public description, not anonymization.

Collection reads public organization metadata, public repository metadata and NuGet package metadata.
It does not enumerate the maintainer's repositories, query personal contributions, or count private
repositories. The maintainer link is editorial attribution, not a collection source. Personal projects,
hardware, learning memberships and other personal profile content are absent from the configuration.

Use `GH_TOKEN` or `GITHUB_TOKEN` only through the environment. Never store credentials in configuration,
fixtures, output or history. Errors are bounded and redacted before publication.

Everything in assets and deployed docs is public. History preserves previously published content;
removal from current configuration does not erase old history or Git commits. Review all publication
surfaces if information needs to be withdrawn. No external fonts or analytics are embedded.
External links contact GitHub or NuGet only when followed.

Validation checks structure and common unsafe content. It cannot establish editorial approval or
prove that arbitrary prose contains no secret. Review public content before publishing.
