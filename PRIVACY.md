# Privacy

The organization profile publishes curated project descriptions, technology labels, maintainer
attribution, and NuGet package information. RelationalLab is private; its approved name and abstract
summary are intentionally public. The `private-abstract` label does not anonymize that content.
Its private repository URL and implementation details are not publication inputs.

Canonical public content lives in `config/organization.toml`. Collection policy in
`config/profile.toml` selects doka-labs public organization/repository metadata and the configured
NuGet owner and families. It does not collect personal contributions or private repository counts.
The maintainer link identifies kdominic89 as Administrator & Core Maintainer; it is editorial
attribution, not permission to collect the maintainer's other repositories.

Supply any collection credentials through the environment or an explicitly selected workflow secret.
Never place tokens in configuration, captures, fixtures, output, or history. The normal workflow uses
the built-in token for public GitHub collection and does not inherit all caller secrets. Upstream
validation, scoped source status, and redacted diagnostics support this boundary; editorial review
is still necessary because structural validation cannot prove arbitrary prose contains no secret.

The current reusable workflow exposes optional `PROFILE_TOKEN` separately from the typed private
aggregate selection. Its presence alone never enables collection. This organization profile does
not select personal/private aggregate collection; a maintainer link is not that selection.

Offline generation and locked replay preserve an existing approved `assets/source-snapshot.json`
byte for byte, including its date, source statuses, and earlier observations. An approved raw capture
can retain a prior aggregate while current policy omits it from rendering; disabling current rendering
does not erase retained public input. `assets/render-snapshot.json` separately records the effective
policy-filtered input. Offline Preview is undated there. Locked replay reuses the recorded effective
input rather than today's credential selection. Keep both snapshots and their generation record.

A first online refresh can collect without a prior capture or seed. Missing offline/replay captures
fail, and malformed existing captures remain fatal. This distinction does not authorize access to
private source or relax the organization profile's configured collection scope.

Published assets, both managed READMEs, the complete Pages artifact, and retained history are public.
Removing content from current configuration does not erase earlier history or Git commits. Rolling
retention is limited by `history_limit = 24`; separate migration recovery copies require their own
access control. Review all affected publication and recovery surfaces when withdrawing information.

The pinned browser runtime uses local resources without embedded analytics or external fonts.
Following an external project or package link contacts its destination service. For upstream privacy
or collection defects, use the reporting path in [Security](SECURITY.md).
