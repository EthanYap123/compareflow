# CompareFlow

Compare supplier quotes and get a purchase approved, with every number traced back to its source.

CompareFlow is a web app for small Singapore businesses (clinics, F&B outlets, small contractors) that buy supplies from several vendors. Instead of retyping quotes into a spreadsheet, a buyer clicks values in the quote itself. Each value stays linked to the spot it came from, the maths is checked (line totals, subtotals, 9% GST), and the approval is recorded in an audit log that can't be edited.

> **Status:** Phase 1 (Planning). No application code yet. See the [project plan](docs/planning/project-plan.md).

## How it works

1. **Request**: list the items you need.
2. **Collect quotes**: upload PDFs, scans or Excel files, or paste an email.
3. **Fill**: click values in the quote to fill the comparison table. Every cell links back to its source.
4. **Check**: line totals, subtotals and GST are recalculated and mismatches are flagged.
5. **Compare**: per item, with units and currencies converted to a total landed cost.
6. **Approve**: rules such as "3 quotes above S$1,000" and "a reason if not the cheapest", with an append-only audit log.

Suggested values (from OCR) are only ever suggestions. A person confirms each one.

## Project phases

The project runs through a full software development life cycle over 16 weeks.

| Phase | Weeks | Output |
| --- | --- | --- |
| 1. Planning | 1 | Problem statement, measurable goals, MoSCoW scope, risks, cost estimate |
| 2. Requirements | 2–3 | User interviews, personas, user stories, functional and non-functional requirements |
| 3. Design | 4–5 | Architecture, data model, OpenAPI spec, UI prototypes, threat model, test quotes |
| 4. Development | 6–11 | Three two-week sprints |
| 5. Testing | 6–13 | Unit, integration, end-to-end, load, security and usability testing |
| 6. Deployment | 14 | Terraform staging and production, gated release pipeline |
| 7. Maintenance | 15–16 | Monitoring, incident reviews, v1.1.0, retrospective |

## Repository layout

```
api/     Spring Boot REST API (Java)
web/     React + TypeScript single-page app
infra/   Terraform for AWS
docs/    Plans, requirements, design, ADRs and test reports
```

## Tech stack

- **Frontend:** React, TypeScript, PDF.js
- **Backend:** Java, Spring Boot, PostgreSQL, Tesseract OCR
- **Infrastructure:** Docker, Caddy, Oracle Cloud Always Free (VMs, Object Storage, Email Delivery, Vault), Terraform
- **CI/CD:** GitHub Actions, GitHub Container Registry

Hosting costs nothing: every service runs on a free tier. See [ADR-0002](docs/adr/0002-host-on-oracle-cloud-always-free.md).

## Data

All quotes in this repository are fake or redacted. No real company data is used.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branching, commit and review workflow.

## License

[MIT](LICENSE) © 2026 Ethan Yap
