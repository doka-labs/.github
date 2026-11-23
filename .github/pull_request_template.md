## Summary

- Problem and resulting behavior:
- Why this change is needed now:
- Risk and rollback:

## Contract Impact

Use `unchanged` or `changed` for each row. Explain changed behavior and link the
relevant tests or documentation; for an unaffected contract, a short reason is
enough.

| Contract | Disposition | Impact and evidence |
| --- | --- | --- |
| Public API, workflow inputs, or command line |  |  |
| Behavior and data integrity |  |  |
| Security and privacy boundaries |  |  |
| Compatibility and supported versions |  |  |
| Dependencies |  |  |

## Evidence Impact

| Evidence path | Disposition | Impact and evidence |
| --- | --- | --- |
| Positive, negative, and regression tests |  |  |
| Documentation and changelog |  |  |
| Package and release evidence |  |  |

## Validation

Use `passed`, `not applicable`, or `pending` for each row. Give the exact
command or CI job and its result. Explain `not applicable`, and resolve
`pending` before requesting review. A local run does not establish hosted
release or publication evidence.

| Check | Status | Command, result, or reason |
| --- | --- | --- |
| Required CI checks |  |  |
| Relevant local tests |  |  |
| Other targeted checks |  |  |

## Review Checklist

- [ ] The change follows the contributing guide, `.editorconfig`, and the Code of Conduct.
- [ ] Documentation, API baselines, and the changelog reflect changed contracts.
- [ ] New dependencies and public options have an active consumer and the required approval.
- [ ] Logs, SQL, fixtures, and attachments contain no secrets or confidential production data.
- [ ] Suspected vulnerabilities are reported privately as the security policy describes.
