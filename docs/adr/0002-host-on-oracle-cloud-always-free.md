# 2. Host on Oracle Cloud Always Free

- **Status:** Accepted
- **Date:** 2026-10-29

## Context

The project must cost nothing to host. The first plan used AWS (CloudFront, S3, EC2, RDS, SES, Secrets Manager) at about US$25-30 a month, paid from new-account credits. Credits run out, and the app should stay live while internship applications are open.

The API runs Spring Boot and Tesseract OCR, which together need more memory than most free app hosts give (often 512 MB, with the app put to sleep when idle). The project also needs separate staging and production environments, infrastructure as code and a real deployment pipeline.

## Decision

Host both environments on Oracle Cloud Infrastructure (OCI) Always Free, in the Singapore region:

- Two Ampere A1 VMs (1 OCPU and 6 GB each): one for staging, one for production.
- Each VM runs Docker Compose with Caddy (HTTPS and the static React build), the Spring Boot API and PostgreSQL.
- Quote files and nightly database dumps go to OCI Object Storage; email goes through OCI Email Delivery; secrets live in OCI Vault and GitHub environment secrets.
- A free DuckDNS subdomain per environment, with Let's Encrypt certificates from Caddy.
- Images are pushed to GitHub Container Registry. Infrastructure is written in Terraform with the OCI provider.

## Alternatives considered

| Option | Why not |
| --- | --- |
| AWS with new-account credits | Free only until the credits run out; the app would have to be torn down mid-application season |
| Render or Koyeb free tier + Neon Postgres | 512 MB memory and sleep on idle are too tight for Spring Boot plus OCR; less infrastructure to show |
| Cloudflare Pages for the frontend, API elsewhere | Frontend and API on different sites would break the HTTP-only session cookie; one hostname per environment keeps it same-site |

## Consequences

- Hosting cost is US$0 a month. Oracle asks for a card to verify the account, but an Always Free-only account is not charged unless upgraded.
- The two VMs use the full free compute allowance, so there is no third environment.
- Oracle may reclaim a VM that stays idle for 7 days, and free ARM capacity is sometimes unavailable. Both are tracked as risk R9.
- PostgreSQL is self-managed, so backups (nightly `pg_dump` to Object Storage, plus one before each release) and restore drills are part of the work.
- The same containers run locally (Docker Compose with MinIO in place of Object Storage), on staging and on production.
