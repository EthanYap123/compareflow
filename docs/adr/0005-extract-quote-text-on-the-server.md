# 5. Extract quote text on the server into one word map

- **Status:** Accepted
- **Date:** 2026-11-14

## Context

Quotes arrive as text PDFs, scanned PDFs, images, Excel files and pasted text (FR-05, FR-28, FR-30). For each one, the requester must be able to click a value to fill a cell (US-04), and anyone must be able to see where a value came from (US-05). Goals set in Phase 1 need every value traceable and OCR accuracy measured. Both are easier to prove if one piece of code reads all quotes.

The browser could read text PDFs itself with PDF.js and only send scans to the server, but then two code paths would produce source locations, and only one of them could be tested on the server.

## Decision

The API reads every quote document and saves the result as a **word map**: each piece of text with its location (page and box, sheet and cell, or character range).

- Text PDFs: PDFBox reads the text layer with word positions. A PDF with no text layer goes to OCR.
- Scans and images: PDF pages are rendered to images, then Tesseract (through Tess4J) reads them, keeping each word's box and confidence.
- Excel: Apache POI reads each sheet's cells, keeping the shown value and the cell reference.
- Pasted text: split into words, keeping character positions.

The browser shows the original (PDF.js for PDFs, an image, a cell grid or the text) and draws the word map over it as click targets. It sends the clicked location to the API, which saves the value and its source.

## Alternatives considered

| Option | Why not |
| --- | --- |
| Text PDFs in the browser (PDF.js), scans on the server | Two code paths for source locations; browser-side extraction is harder to test in CI |
| OCR in the browser (Tesseract.js) | Slow on phones, results depend on the device, and the server cannot check the confidence figures |
| A paid cloud OCR or document AI service | Costs money and sends quote content to a third party; breaks the US$0 budget ([ADR-0002](0002-host-on-oracle-cloud-always-free.md)) |

## Consequences

- One tested path produces every source location, so the "100% traceable" and OCR accuracy goals are measured on server code.
- Uploads are no longer instant for scans: OCR runs in the background and the browser waits for the document to be `ready`.
- PDFBox and PDF.js must agree on coordinates. The Week 4 spike checks that boxes line up at different zoom levels.
- Tesseract adds native libraries and some memory to the API image, measured in the Week 4 spike.
