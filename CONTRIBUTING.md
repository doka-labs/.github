# Contributing

Contributions here cover public organization content, consumer configuration, documentation, workflows,
and bounded consumer tests. Sourcefield's generator and browser runtime are maintained
[upstream](https://github.com/kdominic89/sourcefield). Use ASCII and US English, follow `.editorconfig`,
and separate logical groups with blank lines.

Edit shared doka-labs facts, projects, package identities, icons, and maintainer attribution in
`config/organization.toml`. Use `config/profile.toml` for placement, rendering, collection, and
presentation. Preserve its local organization import and the intended full identities in public links.
Do not infer private-project internals or label planned packages as published. Versions and counts
are collection results, not authored profile constants.

Keep changes limited to their purpose. Update consumer checks for meaningful configuration or
publication contracts, including rejected inputs. From the repository, run:

```sh
python3 -B -m unittest discover -s tests -p 'test_*.py'
```

Provide `SOURCEFIELD_INSTALLATION` for installed-runtime integration probes and report any skipped
checks. Use the matching CLI/browser pair and pinned shared candidate tooling for previews; see
[Setup](SETUP.md). The candidate tool includes tracked inputs only. Review untracked new inputs
separately before relying on a committed-checkout preview.

For content or presentation changes, inspect generated SVGs, managed sections in both READMEs, and
the browser's current/history views, narrow layout, keyboard access, pause, and reduced motion.
Consumer CI uses the pinned shared tools for offline candidate generation; it does not establish live
collection or deployment.

Keep runtime output, installations, caches, screenshots, and distribution archives out of Git.
Intentional generated public text and retained input/history records remain tracked under the
ownership manifest. Do not hand-edit generated artifacts to repair upstream behavior. A generator
upgrade changes its authenticated lock and matching workflow references together after review.
