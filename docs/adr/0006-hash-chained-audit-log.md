# 6. Keep the audit log append-only and hash-chained

- **Status:** Accepted
- **Date:** 2026-11-14

## Context

The audit log is the record that shows why a supplier was chosen and who approved it (US-12). Requirements v1.0 say entries can never be changed or deleted, even by admins, and that any change to an entry must be detected (FR-20). OWASP's logging guidance says to "build in tamper detection". Users can also ask to be anonymised (FR-27), which must not break the log.

## Decision

Protect `audit_event` in three layers:

1. **Permissions.** The API connects as a database role with only `INSERT` and `SELECT` on `audit_event`. Migrations run as a separate owner role.
2. **Trigger.** A trigger raises an error on any `UPDATE` or `DELETE` of `audit_event`, so even the owner role cannot change rows by mistake.
3. **Hash chain.** Each company has its own chain. A new event stores `hash = SHA-256(previous hash + this event's content)`, with the previous hash read under a per-company lock so two events never claim the same place. A check walks the chain and reports the first entry whose hash does not match. It runs nightly and from an admin screen.

Events store user IDs, never names or emails, so anonymising a user changes only `app_user`.

## Alternatives considered

| Option | Why not |
| --- | --- |
| Permissions only | Stops the app, but a person with database access could change a row and nobody would know |
| Write events to a separate log service or object storage with retention lock | More moving parts and cost; the chain gives tamper evidence inside the free setup |
| Store names and emails in events | Anonymising a user would mean editing events, which breaks FR-20 |

## Consequences

- Any edit, deletion or reordering of events is detected by the chain check, though not prevented for someone who controls the whole database and recomputes every hash. Copying the latest hash into the nightly backup in Object Storage makes that harder to hide.
- Writing an event takes a per-company lock, so events for one company are written one at a time. This is fine for a small company's volume.
- The chain check needs a test that edits a row directly in the database and expects the check to fail.
