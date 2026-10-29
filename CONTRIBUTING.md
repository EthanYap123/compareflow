# Contributing

## Branches

`main` is always releasable. Every change goes through a short-lived branch and a pull request.

Branch names use a type prefix:

```
feat/request-form
fix/gst-rounding
docs/phase-2-requirements
chore/ci-cache
```

## Commits

Commits follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(api): add quote upload endpoint
fix(web): keep source highlight after zoom
docs: add phase 1 risk register
```

Common types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`, `build`.

## Pull requests

- One change per PR, linked to its user story or issue (for example `US-03`).
- CI must be green before merging.
- Squash-merge, then delete the branch.

## Definition of done

A change is done when:

1. Its acceptance criteria are met.
2. Tests are added or updated and pass in CI.
3. Security and lint checks pass.
4. Docs (README, OpenAPI spec, ADRs) are updated if behaviour changed.
5. It has been merged to `main` and deployed to staging.

## Architecture decisions

Significant decisions are recorded as ADRs in [`docs/adr/`](docs/adr/).
