# Answer key

The expected result for each scenario, worked out step by step. The Phase 5 scenario tests compare the app's output with these numbers (also in [answer-key.json](answer-key.json)). Every step must be checked by hand against the quote files before the key is used.

| Item | Detail |
| --- | --- |
| Version | 1.0 |
| Date | 22 November 2026 |
| Checked against the files | 22 November 2026: every value re-read from the quote files (text layer, sheet cells, email text, and the photo and scan by eye) and every check, conversion, landed cost and ranking recomputed. No differences found |
| Checked by hand | _not yet_ |

## Rules used

- **Comparison basis.** A GST-registered buyer ranks on landed cost before GST, because it can claim the GST back. A buyer that is not registered ranks on landed cost including GST (US-09, FR-15, FR-24).
- **Landed cost** = items + delivery (+ GST when the buyer is not registered). Values are taken as printed on the quote, even when a check flags them; a flag asks a person to look, it does not change the supplier's price.
- **Line check:** quantity × unit price must equal the line total within S$0.01. **GST check:** 9% of (subtotal + delivery), by the item-by-item or subtotal method. **Rounding:** a total within S$0.05 of the exact figure and rounded to the nearest 5 cents is a note, not an error (FR-12).
- **Units** are converted to the request's unit: pieces for scenario A, kg for scenario C. A box of 100 is 100 pieces, a 50 kg bag is 50 kg, 1 ton is 1,000 kg.
- **Exchange rates** are fixed for testing, using the override in FR-14: **1 USD = 1.3500 SGD** and **1 CNY = 0.1900 SGD**. Live reference rates change daily, so the tests never use them.
- Amounts are rounded half-up to 2 decimal places only at the end.

## Scenario A: clinic supplies

Buyer: Bukit Fern Family Clinic, **not GST-registered**, so quotes rank on cost **including GST**.

Request: nitrile gloves (medium) 2,000 pieces; 3-ply surgical masks 1,000 pieces; alcohol swabs 1,000 pieces.

**Unit price per piece**

| Item | A1 Orchidpath | A2 Tamarind | A3 Bluewren |
| --- | --- | --- | --- |
| Gloves | 8.50 / 100 = 0.0850 | 0.0820 | 8.20 / 100 = 0.0820 |
| Masks | 4.20 / 50 = 0.0840 | 0.0900 | 4.50 / 50 = 0.0900 |
| Swabs | 2.10 / 100 = 0.0210 | 0.0200 | 2.30 / 100 = 0.0230 |

**Checks**

| Quote | Check | Expected | Printed | Result |
| --- | --- | --- | --- | --- |
| A1 | All lines, subtotal 170.00 + 84.00 + 21.00 = 275.00, GST 9% × 275.00 = 24.75, total 299.75 | | | Pass |
| A2 | Lines, subtotal 274.00, GST 9% × (274.00 + 15.00) = 26.01, total 315.01 | | | Pass |
| A3 | Line 2: 20 × 4.50 | 90.00 | 99.00 | **Flag** (off by 9.00) |
| A3 | Subtotal 164.00 + 99.00 + 23.00 (printed lines) | 286.00 | 286.00 | Pass |
| A3 | GST 9% × 286.00 | 25.74 | 25.74 | Pass |

**Landed cost (including GST)**

| Quote | Items | Delivery | GST | Landed | Rank |
| --- | --- | --- | --- | --- | --- |
| A1 | 275.00 | 0.00 | 24.75 | **299.75** | **1** |
| A3 | 286.00 | 0.00 | 25.74 | 311.74 | 2 |
| A2 | 274.00 | 15.00 | 26.01 | 315.01 | 3 |

**Answer: A1 Orchidpath is cheapest at S$299.75.** If A3's mask line were corrected to 90.00, A3 would be 301.93 and still second.

## Scenario B: cafe ingredients

Buyer: Kopi Lantern Cafe, **GST-registered**, so quotes rank on cost **before GST**.

Request: Arabica coffee beans 10 kg; fresh milk 1 L, 48 cartons; raw cane sugar 5 kg. All quotes already use these units.

**Checks**

| Quote | Check | Expected | Printed | Result |
| --- | --- | --- | --- | --- |
| B1 | Lines and subtotal 280.00 + 141.60 + 16.00 = 437.60 | 437.60 | 437.60 | Pass |
| B1 | GST 9% × 437.60 = 39.384 | 39.38 | 39.38 | Pass |
| B1 | Total 437.60 + 39.38 = 476.98, rounded to nearest 5 cents | 476.95 | 476.95 | **Note** (rounding -0.03) |
| B2 | Lines and subtotal 300.00 + 134.40 + 15.00 | 449.40 | 449.40 | Pass |
| B2 | GST treatment "no GST charged" (supplier not registered) | none | none | Pass, no flag |
| B3 | Lines and subtotal 275.00 + 139.20 + 15.50 | 429.70 | 429.70 | Pass |
| B3 | GST 9% × (429.70 + 25.00) = 40.923 | 40.92 | 40.92 | Pass |
| B3 | Total 454.70 + 40.92 | 495.62 | 495.62 | Pass |

**Landed cost (before GST)**

| Quote | Items | Delivery (from the bottom of the sheet for B3) | Landed before GST | Printed total | Rank |
| --- | --- | --- | --- | --- | --- |
| B1 | 437.60 | 0.00 | **437.60** | 476.95 | **1** |
| B2 | 449.40 | 0.00 | 449.40 | 449.40 | 2 |
| B3 | 429.70 | 25.00 | 454.70 | 495.62 | 3 |

**Answer: B1 Harbourline is cheapest at S$437.60 before GST.** B2 has the lowest printed total and B3 the lowest item prices, but neither is cheapest for a GST-registered buyer.

## Scenario C: construction materials

Buyer: Tembusu Build & Renovation Pte Ltd, **GST-registered**, so quotes rank on cost **before GST**.

Request: Portland cement 4,000 kg; washed sand 10,000 kg; rebar T12 1,500 kg.

**Quantities converted to kg**

| Item | C1 Kranji Rock | C2 Straits Cargo | C3 Seletar |
| --- | --- | --- | --- |
| Cement | 80 bags × 50 kg = 4,000 | 4 ton = 4,000 | 80 bags × 50 kg = 4,000 |
| Sand | 10 ton = 10,000 | 10 ton = 10,000 | 10,000 kg |
| Rebar | 1,500 kg | 1.5 ton = 1,500 | 1.5 ton = 1,500 |

**Unit price per kg, in SGD** (C2 converted at 1.3500)

| Item | C1 | C2 | C3 |
| --- | --- | --- | --- |
| Cement | 7.20 / 50 = 0.1440 | 110.00 × 1.35 / 1,000 = 0.1485 | 6.90 / 50 = 0.1380 |
| Sand | 38.00 / 1,000 = 0.0380 | 27.00 × 1.35 / 1,000 = 0.03645 | 0.0360 |
| Rebar | 1.1500 | 820.00 × 1.35 / 1,000 = 1.1070 | 1,120.00 / 1,000 = 1.1200 |

**Checks**

| Quote | Check | Expected | Printed | Result |
| --- | --- | --- | --- | --- |
| C1 | Lines and subtotal 576.00 + 380.00 + 1,725.00 | 2,681.00 | 2,681.00 | Pass |
| C1 | GST 9% × (2,681.00 + 120.00) = 252.09 | 252.09 | 252.09 | Pass |
| C2 | Lines and subtotal (USD) 440.00 + 270.00 + 1,230.00 | 1,940.00 | 1,940.00 | Pass |
| C2 | GST 9% × (1,940.00 + 150.00) (USD) | 188.10 | 188.10 | Pass |
| C3 | Lines and subtotal 552.00 + 360.00 + 1,680.00 | 2,592.00 | 2,592.00 | Pass |
| C3 | GST 9% × (2,592.00 + 250.00) = 255.78 | 255.78 | 233.28 | **Flag** (GST left out the delivery fee) |

**Landed cost (before GST, SGD)**

| Quote | Items | Delivery | Landed before GST | Printed total | Rank |
| --- | --- | --- | --- | --- | --- |
| C1 | 2,681.00 | 120.00 | **2,801.00** | S$3,053.09 | **1** |
| C2 | USD 1,940.00 | USD 150.00 | USD 2,090.00 × 1.35 = 2,821.50 | US$2,278.10 | 2 |
| C3 | 2,592.00 | 250.00 | 2,842.00 | S$3,075.28 | 3 |

**Answer: C1 Kranji Rock is cheapest at S$2,801.00 before GST.** C2's printed total looks lowest only because it is in US dollars, and C3 has the lowest item subtotal but the highest delivery fee.

## Seeded traps

Every trap must be caught. "Caught" means the app gives the expected result below, not that it raises an error for each one.

| # | Quote | Trap | Expected result |
| --- | --- | --- | --- |
| T1 | A1 | Gloves and swabs priced per box of 100, masks per box of 50 | Converted to a price per piece |
| T2 | A2 | Priced per piece, so unit prices look about 100 times lower | Compared per piece; not ranked cheapest |
| T3 | A3 | Mask line total 99.00, should be 90.00 | Line check flags it |
| T4 | B1 | Total rounded to the nearest 5 cents (-0.03) | Shown as a note, not an error |
| T5 | B2 | Supplier not GST-registered, no GST charged | Accepted with "no GST charged"; no GST flag |
| T6 | B2 | Lowest printed total | Ranked 2nd on the buyer's before-GST basis |
| T7 | B3 | Delivery fee printed below the subtotal, near the bottom of the sheet | Included in landed cost; B3 ranked 3rd |
| T8 | C1, C3 | Cement priced per 50 kg bag | Converted to a price per kg |
| T9 | C2 | Prices in USD and per ton | Converted to SGD at the set rate and to a price per kg |
| T10 | C2 | Lowest printed total because it is in USD | Ranked 2nd after conversion |
| T11 | C3 | GST worked out on the subtotal only, leaving out the delivery fee | GST check flags it |
| T12 | C3 | Lowest item subtotal, highest delivery fee | Ranked 3rd on landed cost |
| T13 | C3 | Sand priced per kg while the others price it per ton | Converted to the same unit |

## Edge cases

These are not scored in the three scenarios. They test extraction and odd inputs.

| # | File | What it tests | Expected result |
| --- | --- | --- | --- |
| E1 | Blurry, tilted, low-resolution copy of C3 | OCR on a poor scan | Same values as C3 where OCR reads them; accuracy reported separately from clean scans |
| E2 | B2's quote as email text | Pasted text quote (US-16) | Same values and result as B2, each value linked to its place in the text |
| E3 | A1 with 75 extra catalogue lines (quantity 0) over 3 pages | Long quotes, unmapped lines | The 3 requested lines map as in A1; the 75 others stay unmapped; totals as A1 |
| E4 | Construction quote from abroad in CNY, no sand line, import GST not included | Another currency, a missing item | Converted at 0.1900: (8,390.00 + 1,800.00) × 0.19 = S$1,936.10; sand shown as not quoted, so E4 is not a complete offer |
