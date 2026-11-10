# Market research

Public sources show a real gap between free ordering or spend tools and expensive procurement suites. Source-linked comparison on its own is no longer unique, though. CompareFlow's case is the combination of source links, Singapore GST checks, approval rules and an audit log in one small tool. The second round (findings 11-18) checked the gaps found in the requirements review: quote formats, Excel files, weighted scoring, decision records, rejected requests, audit logging and sign-off.

| Item | Detail |
| --- | --- |
| Version | 2 |
| Date | 4 November 2026 (round 1), 10 November 2026 (round 2) |
| Method | Desk research: government data, regulator pages, standards bodies, academic work, vendor pages and help centres |
| Primary user research | One interview with a clinic operations manager, held for the July 2026 pitch. No new interviews were run for this version |

## What this research can and can't show

It can show what the rules require, what products exist, what they cost and how they handle each feature. It can't show how often small businesses compare quotes, how long that takes them, or whether they would switch tools. Those points stay as assumptions in the [requirements](requirements.md). Most procurement-pain content online is vendor marketing. It was used only to show which features exist, never as evidence of user behaviour.

## Findings

### Round 1: market, rules and data (4 November 2026)

| # | Finding | Evidence | What it changes |
| --- | --- | --- | --- |
| 1 | Small firms are a large market, but no public data covers how they compare quotes | Singapore had 369,500 SMEs out of 371,000 enterprises in 2025 (99.6%), employing 2.49 million of 3.6 million workers (69%) ([SingStat via data.gov.sg](https://data.gov.sg/datasets/d_f9c93c1ffcefe660272c101cd733711c/view)) | Market size is context only; frequency and time lost stay unverified |
| 2 | Comparing quotes by GST-inclusive total can mislead | Only GST-registered businesses can charge GST, and they may claim back GST paid on business purchases, subject to conditions ([IRAS](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/basics-of-gst/goods-and-services-tax-(gst)-what-it-is-and-how-it-works)). Registration is compulsory only above S$1 million taxable turnover ([IRAS](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-registration-deregistration/do-i-need-to-register-for-gst)) | A quote with no GST is not always wrong, so FR-12 changes. The comparison depends on the buyer's GST status, so FR-15, FR-23 and FR-24 are added or changed |
| 3 | A correct invoice can differ by a few cents | GST may be worked out per item or on the subtotal, and a bill may be rounded to the nearest 5 cents ([IRAS](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/basics-of-gst/invoicing-price-display-and-record-keeping/invoicing-customers/index)) | A flat S$0.01 GST check would raise false alarms, so FR-12 accepts both methods and notes rounding |
| 4 | Quote rules vary, so they must be configurable | Singapore's government uses bands of S$6,000 and S$90,000, and allows verbal or written quotes for the smallest band ([MOF](https://www.mof.gov.sg/policies/government-procurement/procurement-processes/)). A [Utah district](https://www.utah.gov/pmn/files/920888.docx) requires three written quotes from US$30,000, and a [Canadian school board](https://www.dcdsb.ca/media/1obkr2tz/ap102-1-general-requirements-posted.pdf) from C$10,001 | FR-16 lets each company set the amount and quote count. S$1,000 and 3 become example values. FR-26 covers quotes with no file |
| 5 | Small teams can't always separate requester and approver | [Utah guidance](https://schools.Utah.gov/financialoperations/resources/bestpracticesandmodelpolicies/CashDisbursementPolicyProcedures.pdf) accepts compensating controls where staffing makes full separation impossible | FR-25 blocks self-approval by default, with a logged owner override |
| 6 | Spreadsheet errors are a documented risk, with dated evidence | A review of seven field audits found errors in 94% of 88 spreadsheets, with a 5.2% cell error rate ([Panko 1998, via Rittweger and Langan 2010](https://arxiv.org/pdf/1009.2775)). These were general operational spreadsheets from a small sample, not quote comparisons | Supports the maths checks; not used as a claim about quote sheets |
| 7 | Personal data can't simply be kept forever, and the audit log can't be edited | Organisations may stop retaining personal data by removing the means of linking it to a person ([PDPC guidelines](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/the-retention-limitation-obligation---ch-18-(270717).pdf)) | NFR-06 changes and FR-27 is added: anonymise the user record, keep the audit entries |
| 8 | Tax invoices must be kept for at least 5 years | [IRAS](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/basics-of-gst/invoicing-price-display-and-record-keeping/invoicing-customers/index). This covers invoices, not quotes | Relevant only if the Could-have invoice matching is built |
| 9 | Invoice data rules are arriving, but not soon enough to shape the MVP | InvoiceNow submission phases in from 2025, with existing registrants from 1 April 2028 to 1 April 2031 by turnover, and covers purchases as well as supplies ([IRAS](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-invoicenow-requirement)) | Invoice matching stays a Could-have |
| 10 | A free daily exchange rate is available without a key | The official [data.gov.sg USD series](https://data.gov.sg/datasets/d_046ff8d521a218d9178178cfbfc45c2c/view) stops in October 2015. [Frankfurter](https://api.frankfurter.dev/v1/latest?base=USD&symbols=SGD,CNY) returned USD to SGD and CNY for 3 November 2026 | FR-14 prefills this reference rate, allows an override and saves the rate used |

### Round 2: requirements review gaps (10 November 2026)

| # | Finding | Evidence | What it changes |
| --- | --- | --- | --- |
| 11 | Quotes typed into an email body are a normal format, not an edge case | A vendor guide to quote extraction lists five formats: ERP PDFs, Excel sheets, scanned handwritten forms, quotes typed in the email body, and Word files ([ImageToTable](https://imagetotable.ai/blog/complete-guide-vendor-quote-extraction)). Email-parsing tools such as [Parabola](https://parabola.io/use-cases/extract-email-body-attachment-data) read the message body as well as attachments. Figures on WhatsApp use by Singapore SMEs come only from vendor blogs, so they are not used | Pasting text as a quote gets its own story (US-16), with each value linked to its place in the pasted text |
| 12 | Excel quotes need their own handling | The same guide warns that column layouts, merged cells and missing headers vary between suppliers, and that units such as "EA" and "PCS" differ, so fields should be matched by meaning, not fixed cell position ([ImageToTable](https://imagetotable.ai/blog/complete-guide-vendor-quote-extraction)) | XLSX quotes are shown as a clickable grid, and a value's source is the file, sheet and cell (FR-28). No fixed template is assumed |
| 13 | The closest competitors already accept Excel and trace values to the quote | BidLevel supports PDFs and Excel files and lets users trace every number back to the original quote ([BidLevel](https://procurepro.co/bidlevel)). Umbiko reads PDF, Excel and Word quotes and ranks them by the user's own criteria ([Product Hunt](https://www.producthunt.com/products/umbiko)) | Excel support stays a Must; without it, CompareFlow falls behind tools that already exist |
| 14 | Weighted scoring is common, but price-based ranking is the norm for small purchases | A free quote-comparison template scores price, lead time, warranty and payment terms with user-set weights, beside landed cost ([Lapasar](https://lapasar.com/templates/quotation-comparison)). MOF says evaluation criteria "will generally include both quality and price", but for small purchases it asks only that prices be "assessed to be reasonable" ([MOF](https://www.mof.gov.sg/policies/government-procurement/procurement-processes/)) | Weighted score stays a Should (US-17) and is off by default. Landed cost stays the main ranking |
| 15 | A shareable record of the decision is not a given in procurement tools | Procurify says there is no option to create a PDF of an order request; users print the page from the browser ([Procurify](https://success.procurify.com/en/articles/9002121-can-i-download-my-order-request-as-a-pdf-formatted-document)). MOF asks agencies to "ensure proper documentation of key considerations and decisions" ([MOF](https://www.mof.gov.sg/policies/government-procurement/procurement-processes/)) | A PDF decision summary with the quotes, recommendation, reason and approval trail becomes a Should (US-18) |
| 16 | A rejected request needs a defined way back | Ramp separates "request changes", which pauses a step without rejecting the request, from rejection ([Ramp](https://support.ramp.com/request-changes-to-procurement-requests)). In Dynamics 365, resubmitting a rejected requisition starts the review over ([Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-requisitions-overview)) | The approver can send a request back for changes or reject it outright. A resubmitted request starts a new approval round, and every round stays in the audit log (FR-29) |
| 17 | Admin actions belong in the audit log, and the log must show tampering | OWASP lists user administration, privilege changes, admin actions and configuration changes as events to log, each with when, where, who and what. It also says to "build in tamper detection" ([OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)) | FR-19 also logs approval-rule changes, role changes, the self-approval setting and anonymisation. FR-20 adds tamper detection |
| 18 | Requirements are signed off as a fixed baseline, with changes controlled after that | ISO/IEC/IEEE 29148 covers eliciting, specifying and managing requirements, and change control applies once a baseline exists ([IEEE](https://technav.ieee.org/topic/requirements-management/)). The IEEE definition quoted by [Modern Analyst](https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/2930/The-Line-in-the-Sand-Requirements-Baseline.aspx) says a baseline is "formally reviewed and agreed on" and "can be changed only through formal change control procedures" | Requirements are baselined as v1.0 with a dated sign-off. Later changes need a change-log entry with a reason |

## Competing products

Prices and features come from each vendor's or publisher's public page on 4 or 10 November 2026.

| Product | Who it serves | Cost shown | Quote formats | Compares quotes | Links values to source | Approval rules and audit log |
| --- | --- | --- | --- | --- | --- | --- |
| [Precoro](https://precoro.com/pricing) | Procurement teams | From US$499 a month, billed annually | Not shown | Not confirmed on entry plan | Not shown | Automated approvals included |
| [Procurify](https://success.procurify.com/en/articles/9002121-can-i-download-my-order-request-as-a-pdf-formatted-document) | Mid-size finance and procurement teams | Not checked | Not shown | Not shown | Not shown | Approval routing; no PDF of a request |
| [Zeemart](https://apps.xero.com/sg/app/zeemart) | Singapore and regional F&B operators | Free for operators | Not shown | Not shown; tracks prices and orders | Not shown | Not shown |
| [BidLevel](https://procurepro.co/bidlevel) | Construction contractors | Free to try; paid price not shown | PDF, Excel | Yes; exports an Excel comparison | Yes | Not shown |
| [Umbiko](https://www.producthunt.com/products/umbiko) | Procurement and project teams | Free options; paid price not shown | PDF, Excel, Word | Yes, ranked by the user's criteria | Not shown | Not mentioned |
| [Lapasar template](https://lapasar.com/templates/quotation-comparison) | Anyone with Excel | Free download | Typed in by hand | Up to 5 quotes, weighted score, landed cost | No | No |
| Excel + WhatsApp | Anyone | Usually already available | Any, retyped | By hand | No | No |
| **CompareFlow** | Small Singapore businesses | Portfolio project | PDF, scan, Excel, pasted text | Yes | Yes | Yes |

"Not shown" means the public page did not say, not that the feature is missing. BidLevel already does source-linked comparison well in construction, so CompareFlow should not claim that feature is unique.

## What this means for scope

- **Keep:** click-to-fill, source links, maths checks, approvals and the audit log. A person confirms every value, which BidLevel's own guidance also expects.
- **Changed in round 1:** GST handling, rule settings, self-approval, exchange rates and personal data, as listed in the [v0.2 changes](requirements.md#changes-from-v01).
- **Added as a Should in round 1:** recording a verbal or no-file quote.
- **Round 2:** Excel quotes get a clickable grid with cell-level sources, which keeps them a Must. Pasted text, weighted scoring and the PDF decision summary become Should stories. The approval flow gains "send back for changes". The audit log covers admin actions and shows tampering.
- **Leave as is:** invoice matching stays a Could-have, and supplier logins stay out of scope.
