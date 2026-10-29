# 1. Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-10-29

## Context

CompareFlow is built over 16 weeks across several SDLC phases. Decisions made early (stack, hosting, data model) need to be explained later, both to reviewers and to future me.

## Decision

Record each significant architecture decision as a short Markdown file in `docs/adr/`, numbered in order, using the format: Context, Decision, Consequences.

## Consequences

- Decisions and their reasons stay next to the code they affect.
- A decision that changes gets a new ADR that supersedes the old one, instead of editing history.
