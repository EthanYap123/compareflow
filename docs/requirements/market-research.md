# Market research

Public sources show a real gap between free ordering or spend tools and expensive procurement suites, but source-linked comparison alone is no longer unique. CompareFlow's case is the combination: source links, Singapore GST checks, approval rules and an audit log, in one small tool.

| Item | Detail |
| --- | --- |
| Date | 4 November 2026 |
| Method | Desk research: government data, regulator pages, academic work and vendor pages |
| Primary user research | One interview with a clinic operations manager, held for the July 2026 pitch. No new interviews were run for this version |

## What this research can and can't show

It can show what the rules require, what products exist and what they cost. It can't show how often small businesses compare quotes, how long it takes them, or whether they would change tools. Those points stay as assumptions in the [requirements](requirements.md). Most procurement-pain content online is vendor marketing, so it was not used as evidence.

## Findings

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

## Competing products

Prices and features come from each vendor's or marketplace's public page on 4 November 2026.

| Product | Who it serves | Cost shown | Compares quotes | Links values to source | Approval rules and audit log |
| --- | --- | --- | --- | --- | --- |
| [Precoro](https://precoro.com/pricing) | Procurement teams | From US$499 a month, billed annually | Not confirmed on entry plan | Not shown | Automated approvals included |
| [Zeemart](https://apps.xero.com/sg/app/zeemart) | Singapore and regional F&B operators | Free for operators | Not shown; tracks prices and orders | Not shown | Not shown |
| [BidLevel](https://procurepro.co/bidlevel) | Construction contractors | Free to try; paid price not shown | Yes | Yes | Not shown |
| [Umbiko](https://www.producthunt.com/products/umbiko) | Procurement and project teams | Free options; paid price not shown | Yes, ranked | Not shown | Not mentioned |
| Excel + WhatsApp | Anyone | Usually already available | By hand | No | No |
| **CompareFlow** | Small Singapore businesses | Portfolio project | Yes | Yes | Yes |

"Not shown" means the public page did not say, not that the feature is missing. Tools like BidLevel already do source-linked comparison well in construction, so CompareFlow should not claim that feature is unique.

## What this means for scope

- **Keep:** click-to-fill, source links, maths checks, approvals and the audit log. A person confirms every value, which BidLevel's own guidance also expects.
- **Change:** GST handling, rule settings, self-approval, exchange rates and personal data, as listed in the [v0.2 changes](requirements.md#changes-from-v01).
- **Add as a Should-have:** recording a verbal or no-file quote.
- **Leave as is:** invoice matching stays a Could-have, and supplier logins stay out of scope.
