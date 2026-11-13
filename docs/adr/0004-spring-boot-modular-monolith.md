# 4. Build the API as a Spring Boot modular monolith

- **Status:** Accepted
- **Date:** 2026-11-14

## Context

The API holds every business rule: company isolation, text extraction and OCR, maths and GST checks, comparison, approvals and the audit log. One developer builds it part-time in three sprints, and it runs on a single VM with 1 OCPU and 6 GB of memory per environment ([ADR-0002](0002-host-on-oracle-cloud-always-free.md)). The stack was set in Phase 1: Java and Spring Boot, chosen as a learning goal and because it is common in banks and government in Singapore.

## Decision

Build one Spring Boot application, split into modules by feature (identity, requests, quotes, extraction, checks, comparison, approvals, audit, notifications, reports). Each module is a Java package that owns its tables and exposes a service interface; other modules call that interface, never its repositories. The `checks` and `comparison` modules are plain Java with no Spring or database code. The [architecture](../design/architecture.md) lists the modules.

## Alternatives considered

| Option | Why not |
| --- | --- |
| Microservices (for example a separate OCR service) | More containers, network calls and deployments on a VM with little memory, for one developer and no scaling need |
| Node.js (Express or NestJS) | Would also work, but misses the Spring Boot learning goal and the Java libraries used here (PDFBox, Tesseract via Tess4J, Apache POI) |
| One package per layer (controllers, services, repositories) | Spreads each feature across the codebase and lets any service reach any table, which makes company isolation harder to review |

## Consequences

- One image to build, test, scan and deploy per environment.
- Module boundaries are a convention, so they can erode. A test (for example with ArchUnit) can fail the build if one module uses another's repository.
- OCR shares memory with the rest of the API. It runs in a small, bounded worker pool, and the Week 4 spike measures memory use. If it does not fit, OCR can move to its own container later without changing the rest.
