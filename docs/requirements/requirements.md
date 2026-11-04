# Requirements

CompareFlow v0.2 has 15 user stories, 27 functional requirements and 13 non-functional requirements. They draw on the [market research](market-research.md) and the one interview from the 2026 pitch. No new user interviews were run, so anything about user behaviour is labelled as an assumption.

| Item | Detail |
| --- | --- |
| Version | 0.2 |
| Date | 4 November 2026 |
| Basis | Desk research plus one pitch interview |

## Stakeholders

| Stakeholder | Role | What they need |
| --- | --- | --- |
| Requester (procurement or ops staff) | Primary user | Fill the comparison fast and without retyping |
| Approver (owner or manager) | Primary user | See all options and the reason on one screen, then decide quickly |
| Admin (often the owner) | Sets up the company, users and rules | Simple rules that match how the company buys |
| Suppliers | Not users; their quotes are the input | None directly |

## Proto-personas

These are fictional and built from assumptions. They guide design, but they are not findings about real people.

**Mei, clinic operations executive (requester).** Orders medical supplies from 3-4 regular suppliers and gets quotes as PDFs and the odd scan. *Assumed pain:* retyping, and checking every number twice. *Goal:* see where each number came from so she doesn't have to recheck it.

**Mr Tan, F&B outlet owner (approver).** Runs two cafés and approves larger purchases from his phone. Sometimes he also places the order himself. *Assumed pain:* gets a screenshot with no alternatives. *Goal:* one link with the options, the recommendation and the reason.

**Raj, site supervisor at a small contractor (requester).** Buys cement, rebar and aggregates in bags, tons and kg. Some small suppliers don't charge GST. *Assumed pain:* can't tell the real unit price or which total is fair. *Goal:* everything on the same unit and the same GST basis.

## User stories

Twelve Must stories cover the MVP; three Should stories follow if time allows. Acceptance criteria become test cases in Phase 5.

| ID | As a... | I want to... | So that... | Acceptance criteria | Priority |
| --- | --- | --- | --- | --- | --- |
| US-01 | Admin | set up my company and invite users with roles | the right people can request and approve | Invite by email; role is requester, approver or admin; a user only ever sees their own company's data | Must |
| US-02 | Requester | create a purchase request listing items, quantities and units | every quote is compared against the same list | Add, edit, remove items; a request cannot be compared with fewer than 1 quote | Must |
| US-03 | Requester | upload quotes as PDF, image or Excel | I can use whatever the supplier sent | PDF, PNG, JPG, XLSX up to 10 MB; other types rejected with a clear message; file shown within 3 s | Must |
| US-04 | Requester | click a value in the quote to fill a table cell | I never retype numbers | Clicking text fills the selected cell; works on scanned files after OCR; typing by hand is still possible | Must |
| US-05 | Requester or approver | click any filled value and see where it came from | I can trust the number without rechecking | The source spot is highlighted on the quote; hand-typed values are marked "manual" | Must |
| US-06 | Requester | map each supplier's lines to my requested items | items with different names are compared fairly | Drag or pick a request item per line; unmapped lines are listed; one line can map to only one item | Must |
| US-07 | Requester | be warned when a quote's maths is wrong | I catch supplier and typing errors | Each quote is set to 9% added, 9% included, 0% zero-rated or no GST charged. Flags when qty x unit price differs from the line total by more than S$0.01, when lines do not add to the subtotal, or when GST matches neither the item-by-item nor the subtotal method. A total within S$0.05 that is rounded to the nearest 5 cents shows a note, not an error | Must |
| US-08 | Requester | see prices in the same unit and currency | I can tell the real unit price | Converts kg/g/tons and bags (with a set bag weight). Foreign currency uses a prefilled daily reference rate that can be overridden; the rate, date and source stay on the quote | Must |
| US-09 | Requester | see the total landed cost per supplier | the cheapest-looking quote doesn't fool me | Items, delivery and GST shown per supplier, per item and in total. A GST-registered company ranks on cost before GST; others rank on cost with GST; the basis is on screen; cheapest marked | Must |
| US-10 | Requester | send a recommendation for approval with a reason | my manager knows why | Cannot send if the company's rules are not met, with the failed rule named; a reason is required if not the cheapest | Must |
| US-11 | Approver | approve or reject from one screen, including on my phone | decisions are quick and recorded | Sees all quotes, the recommendation and the reason; approve or reject with a comment; works at 375 px width. Requesters cannot approve their own request unless an admin allows it, and each such approval is flagged in the audit log | Must |
| US-12 | Admin or auditor | view an audit log of every request | anyone can see who did what and why | Every create, edit, send, approve and reject is logged with user and time; entries cannot be edited or deleted; anonymising a user leaves the entries in place | Must |
| US-13 | Requester | get AI-suggested values that I confirm | filling is even faster | Suggestions shown in a different colour; none count until confirmed; each still links to its source | Should |
| US-14 | Approver | get an email when something needs my approval | I don't miss it | Email within 1 minute, with a link to the approval screen | Should |
| US-15 | Requester | record a quote I got by phone or in person | it still counts in the comparison | Supplier, values and a note can be entered with no file; every value is marked "manual"; the approver sees that it has no file | Should |

## Functional requirements

Each requirement gets at least one automated or manual test in Phase 5.

| ID | The system shall... | Story |
| --- | --- | --- |
| FR-01 | Let users sign up, log in and log out with email and password | US-01 |
| FR-02 | Let an admin invite users and assign one role: requester, approver or admin | US-01 |
| FR-03 | Restrict every read and write to the user's own company | US-01 |
| FR-04 | Create, edit and close purchase requests with item lines (name, quantity, unit) | US-02 |
| FR-05 | Accept PDF, PNG, JPG and XLSX uploads up to 10 MB and reject other types | US-03 |
| FR-06 | Store uploaded files privately and serve them only through short-lived links | US-03 |
| FR-07 | Extract the text layer from text PDFs and run OCR on scans and images | US-03, US-04 |
| FR-08 | Fill the selected table cell with the clicked text, parsing numbers and currency symbols | US-04 |
| FR-09 | Save the source (file, page, position) of every filled value, or mark it as manual | US-05 |
| FR-10 | Highlight a value's source on the quote when the value is selected | US-05 |
| FR-11 | Let users map each quote line to one request item and list unmapped lines | US-06 |
| FR-12 | Check line totals and subtotals to S$0.01, and check GST against the quote's treatment using both the item-by-item and subtotal methods; note 5-cent rounding of the total instead of flagging it | US-07 |
| FR-13 | Convert between kg, g and tons, and from bags using a set weight per bag | US-08 |
| FR-14 | Convert foreign currency to SGD using a prefilled daily reference rate that a user can override, saving the rate, date and source with the quote | US-08 |
| FR-15 | Show per-item unit prices and total landed cost (items + delivery + GST) for each supplier, ranked on the company's GST basis | US-09 |
| FR-16 | Let an admin set approval rules: the minimum number of quotes above an amount they choose, and a reason required if not cheapest | US-10 |
| FR-17 | Block sending for approval until the rules are met, and say which rule failed | US-10 |
| FR-18 | Let an approver approve or reject with a comment, locking the request afterwards | US-11 |
| FR-19 | Record every create, edit, send, approve and reject event with user and time | US-12 |
| FR-20 | Never allow audit entries to be changed or deleted, including by admins | US-12 |
| FR-21 | Show AI-suggested values as unconfirmed until a user confirms each one | US-13 |
| FR-22 | Email approvers when a request is sent to them | US-14 |
| FR-23 | Record each quote's GST treatment: 9% added, 9% included, 0% zero-rated or no GST charged | US-07 |
| FR-24 | Let an admin record whether the company is GST-registered, which sets the comparison basis | US-09 |
| FR-25 | Block users from approving their own request unless an admin allows it, and flag each such approval in the audit log | US-11 |
| FR-26 | Let a requester record a quote with no file, with every value marked manual and the missing file shown to the approver | US-15 |
| FR-27 | Let an admin anonymise a user's name and email while keeping that user's audit entries | US-12 |

## Non-functional requirements

Every quality target has a number and a way to test it.

| ID | Category | Requirement | How it is tested |
| --- | --- | --- | --- |
| NFR-01 | Performance | API responses under 300 ms at the 95th percentile with 50 concurrent users | k6 load test on staging |
| NFR-02 | Performance | A 5-page text PDF is ready to click within 3 s; OCR of one scanned page within 10 s | Timed end-to-end test |
| NFR-03 | Security | Zero cases of one company reading another's data | Automated tests that try cross-company access on every endpoint |
| NFR-04 | Security | Passwords hashed with bcrypt; HTTPS only; login rate-limited | Config review + ZAP scan |
| NFR-05 | Security | No high or critical findings open at release | CodeQL, OWASP ZAP, Trivy and gitleaks in CI |
| NFR-06 | Privacy (PDPA) | Collect only name, email and company for users; anonymise a user's name and email within 30 days of a valid request or once no longer needed, while keeping audit entries | Data review + anonymisation test |
| NFR-07 | Reliability | Database backed up daily; restore tested once before release | Restore drill on staging |
| NFR-08 | Availability | Production up 99% during the 4-week testing and demo period | Uptime monitor report |
| NFR-09 | Usability | A new tester completes a 3-quote comparison without help in under 10 minutes; SUS score of 70+ | Phase 5 usability test |
| NFR-10 | Accessibility | No serious or critical axe issues; usable by keyboard | axe in CI + manual keyboard check |
| NFR-11 | Compatibility | Works on current Chrome, Edge and Safari; approval screen works at 375 px width | Playwright on three browsers + phone viewport |
| NFR-12 | Maintainability | All merges through pull requests with CI passing; core logic 80%+ line coverage | GitHub branch rules + coverage report |
| NFR-13 | Cost | US$0 hosting: free tiers only, with a budget alert at US$1 | OCI budget alert |

## Assumptions

| Assumption | Status | Basis |
| --- | --- | --- |
| Quotes arrive in mixed formats (PDF, scans, Excel, email) | Partly supported | Competing tools accept these formats; the mix in small Singapore firms is unknown |
| People want to check extracted values against the source | Partly supported | The pitch interview, and BidLevel still expects human review |
| Small businesses in clinics, F&B and construction compare quotes at least a few times a month | Unverified | No public data found |
| Comparing quotes takes enough time to be worth a new tool | Unverified | No reliable data found |
| Approvers will use a web app instead of WhatsApp if it takes under a minute | Unverified | No data found |
| Some small firms use a "minimum quotes above an amount" rule | Partly supported | Seen in public-sector policies, not small Singapore firms; FR-16 makes it configurable |

## Constraints

- One developer, part-time during the semester (about 10-12 hours a week).
- No money for hosting: free tiers only.
- Only fake or redacted quotes are used for development, demos and testing; no real company data is stored.
- Stack: React + TypeScript, Java Spring Boot, PostgreSQL, Docker, Terraform and GitHub Actions.

## Decisions from open questions

| Question | Decision | Why |
| --- | --- | --- |
| How many approver levels? | One for the MVP | Target firms are small, and one level keeps the rules simple |
| Which exchange-rate source? | Prefill from a free reference rate, allow an override, save what was used | The official USD series ended in 2015, and a saved rate keeps past decisions from changing |
| Is S$1,000 and 3 quotes a fixed rule? | No, both are company settings | Thresholds vary widely between organisations |

## Open questions

- [ ] Are the original pitch teammates okay with a solo version, and how do they want to be credited?
- [ ] Is OCR good enough on poor scans? (Week 4 spike)
- [ ] Who tests the prototype in Phase 3 and the app in Phase 5, now that no interview group exists? NFR-09 and the speed and trust goals depend on real testers and can't be claimed without them.

## Changes from v0.1

| Item | Change | Reason |
| --- | --- | --- |
| Interview plan | Replaced with desk research | Interviews are not being run for this version |
| Personas | Relabelled as proto-personas | They are not based on new interviews |
| US-07, FR-12, FR-23 | GST treatment per quote; accepted rounding methods | Findings 2 and 3 |
| US-09, FR-15, FR-24 | Comparison follows the buyer's GST status | Finding 2 |
| US-10, FR-16 | Quote amount and count are settings | Finding 4 |
| US-11, FR-25 | Self-approval blocked by default, with a logged override | Finding 5 |
| US-15, FR-26 | New Should-have for quotes with no file | Finding 4 |
| US-12, NFR-06, FR-27 | Anonymise instead of delete | Finding 7 |
| US-08, FR-14 | Prefilled, overridable, saved exchange rate | Finding 10 |
