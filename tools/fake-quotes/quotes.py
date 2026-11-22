"""Data for the fake quote set.

Every company, address and number here is fictional. Values are written out
as the supplier "printed" them, including the deliberate mistakes (traps),
so nothing on a quote is calculated by the generator.
"""

FAKE_NOTE = "Fictional quote made for CompareFlow testing. Not a real company or offer."

BUYERS = {
    "a": {"name": "Bukit Fern Family Clinic", "gst_registered": False},
    "b": {"name": "Kopi Lantern Cafe", "gst_registered": True},
    "c": {"name": "Tembusu Build & Renovation Pte Ltd", "gst_registered": True},
}

# Each line: (description, quantity, unit, unit price, line total as printed)
QUOTES = [
    # ---------------- Scenario A: clinic supplies, 3 text PDFs ----------------
    {
        "id": "a1", "scenario": "a", "file": "scenario-a-clinic/a1-orchidpath.pdf",
        "format": "text_pdf", "layout": "classic",
        "supplier": {"name": "Orchidpath Medical Supplies Pte Ltd",
                     "address": "8 Sample Lane #02-01, Singapore 000001",
                     "contact": "sales@orchidpath.example | 000-0001",
                     "gst_reg": "FAKE-GST-0001"},
        "quote_no": "OP-Q-2611-041", "date": "18 Nov 2026", "valid_until": "18 Dec 2026",
        "currency": "SGD", "gst_label": "GST 9%",
        "lines": [
            ("Nitrile examination gloves, medium (box of 100)", "20", "box", "8.50", "170.00"),
            ("Surgical face masks, 3-ply (box of 50)", "20", "box", "4.20", "84.00"),
            ("Alcohol swabs (box of 100)", "10", "box", "2.10", "21.00"),
        ],
        "subtotal": "275.00", "delivery": None, "gst": "24.75", "rounding": None, "total": "299.75",
        "terms": {"payment": "30 days", "lead_time": "3 working days", "warranty": "-"},
        "notes": "Free delivery for orders above S$200.",
    },
    {
        "id": "a2", "scenario": "a", "file": "scenario-a-clinic/a2-tamarind.pdf",
        "format": "text_pdf", "layout": "minimal",
        "supplier": {"name": "Tamarind Healthcare Trading",
                     "address": "21 Example Road, Singapore 000002",
                     "contact": "quotes@tamarind.example | 000-0002",
                     "gst_reg": "FAKE-GST-0002"},
        "quote_no": "TH/26/1187", "date": "19 Nov 2026", "valid_until": "3 Dec 2026",
        "currency": "SGD", "gst_label": "GST @ 9%",
        "lines": [
            ("Nitrile gloves M", "2000", "pc", "0.082", "164.00"),
            ("3-ply surgical mask", "1000", "pc", "0.090", "90.00"),
            ("Alcohol prep pad", "1000", "pc", "0.020", "20.00"),
        ],
        "subtotal": "274.00", "delivery": "15.00", "gst": "26.01", "rounding": None, "total": "315.01",
        "terms": {"payment": "COD", "lead_time": "Next day", "warranty": "-"},
        "notes": "Prices per piece. Delivery charged per order.",
    },
    {
        "id": "a3", "scenario": "a", "file": "scenario-a-clinic/a3-bluewren.pdf",
        "format": "text_pdf", "layout": "modern",
        "supplier": {"name": "Bluewren Clinical Supply",
                     "address": "5 Placeholder Avenue, Singapore 000003",
                     "contact": "hello@bluewren.example | 000-0003",
                     "gst_reg": "FAKE-GST-0003"},
        "quote_no": "BW-7720", "date": "19 Nov 2026", "valid_until": "19 Dec 2026",
        "currency": "SGD", "gst_label": "Add 9% GST",
        "lines": [
            ("Gloves, nitrile, size M - 100/box", "20", "box", "8.20", "164.00"),
            ("Face mask 3-ply - 50/box", "20", "box", "4.50", "99.00"),  # trap: 20 x 4.50 = 90.00
            ("Alcohol swab - 100/box", "10", "box", "2.30", "23.00"),
        ],
        "subtotal": "286.00", "delivery": None, "gst": "25.74", "rounding": None, "total": "311.74",
        "terms": {"payment": "14 days", "lead_time": "5 working days", "warranty": "-"},
        "notes": "Thank you for your enquiry.",
    },
    # ---------------- Scenario B: cafe ingredients, PDF + photo + Excel ----------------
    {
        "id": "b1", "scenario": "b", "file": "scenario-b-cafe/b1-harbourline.pdf",
        "format": "text_pdf", "layout": "classic",
        "supplier": {"name": "Harbourline Food Supplies Pte Ltd",
                     "address": "40 Sample Industrial Park, Singapore 000004",
                     "contact": "orders@harbourline.example | 000-0004",
                     "gst_reg": "FAKE-GST-0004"},
        "quote_no": "HFS-11-0932", "date": "20 Nov 2026", "valid_until": "27 Nov 2026",
        "currency": "SGD", "gst_label": "GST 9%",
        "lines": [
            ("Arabica coffee beans, medium roast", "10", "kg", "28.00", "280.00"),
            ("Fresh milk 1L carton", "48", "carton", "2.95", "141.60"),
            ("Raw cane sugar", "5", "kg", "3.20", "16.00"),
        ],
        "subtotal": "437.60", "delivery": None, "gst": "39.38", "rounding": "-0.03", "total": "476.95",
        "terms": {"payment": "30 days", "lead_time": "2 days", "warranty": "-"},
        "notes": "Total rounded to the nearest 5 cents.",
    },
    {
        "id": "b2", "scenario": "b", "file": "scenario-b-cafe/b2-sunbird-photo.jpg",
        "format": "photo", "layout": "minimal",
        "supplier": {"name": "Sunbird Provisions",
                     "address": "Blk 9 Example Market #01-12, Singapore 000005",
                     "contact": "000-0005",
                     "gst_reg": None},
        "quote_no": "SP-0215", "date": "20 Nov 2026", "valid_until": "4 Dec 2026",
        "currency": "SGD", "gst_label": None,
        "lines": [
            ("Arabica beans", "10", "kg", "30.00", "300.00"),
            ("Fresh milk 1L", "48", "ctn", "2.80", "134.40"),
            ("Cane sugar", "5", "kg", "3.00", "15.00"),
        ],
        "subtotal": "449.40", "delivery": None, "gst": None, "rounding": None, "total": "449.40",
        "terms": {"payment": "Cash on delivery", "lead_time": "1 day", "warranty": "-"},
        "notes": "Not GST registered. No GST charged.",
    },
    {
        "id": "b3", "scenario": "b", "file": "scenario-b-cafe/b3-greenleaf.xlsx",
        "format": "xlsx", "layout": "sheet",
        "supplier": {"name": "Greenleaf Pantry Wholesale",
                     "address": "77 Placeholder Street, Singapore 000006",
                     "contact": "sales@greenleaf.example | 000-0006",
                     "gst_reg": "FAKE-GST-0006"},
        "quote_no": "GPW-Q-3381", "date": "21 Nov 2026", "valid_until": "5 Dec 2026",
        "currency": "SGD", "gst_label": "GST 9%",
        "lines": [
            ("Coffee beans - Arabica", "10", "kg", "27.50", "275.00"),
            ("Milk, fresh, 1 litre", "48", "carton", "2.90", "139.20"),
            ("Sugar, raw cane", "5", "kg", "3.10", "15.50"),
        ],
        "subtotal": "429.70", "delivery": "25.00", "gst": "40.92", "rounding": None, "total": "495.62",
        "terms": {"payment": "30 days", "lead_time": "3 days", "warranty": "-"},
        "notes": "Delivery fee applies to orders below S$500.",
    },
    # ---------------- Scenario C: construction materials, 2 PDFs + scan ----------------
    {
        "id": "c1", "scenario": "c", "file": "scenario-c-construction/c1-kranji-rock.pdf",
        "format": "text_pdf", "layout": "classic",
        "supplier": {"name": "Kranji Rock Building Supplies Pte Ltd",
                     "address": "3 Example Quarry Road, Singapore 000007",
                     "contact": "quote@kranjirock.example | 000-0007",
                     "gst_reg": "FAKE-GST-0007"},
        "quote_no": "KR-26-5510", "date": "20 Nov 2026", "valid_until": "20 Dec 2026",
        "currency": "SGD", "gst_label": "GST 9%",
        "lines": [
            ("Portland cement, 50 kg bag", "80", "bag", "7.20", "576.00"),
            ("Washed sand", "10", "ton", "38.00", "380.00"),
            ("Rebar T12", "1500", "kg", "1.15", "1725.00"),
        ],
        "subtotal": "2681.00", "delivery": "120.00", "gst": "252.09", "rounding": None, "total": "3053.09",
        "terms": {"payment": "30 days", "lead_time": "5 working days", "warranty": "-"},
        "notes": "Delivery to site within mainland Singapore.",
    },
    {
        "id": "c2", "scenario": "c", "file": "scenario-c-construction/c2-straits-cargo-usd.pdf",
        "format": "text_pdf", "layout": "modern",
        "supplier": {"name": "Straits Cargo Materials Pte Ltd",
                     "address": "60 Sample Harbour Drive, Singapore 000008",
                     "contact": "trade@straitscargo.example | 000-0008",
                     "gst_reg": "FAKE-GST-0008"},
        "quote_no": "SCM-USD-0419", "date": "21 Nov 2026", "valid_until": "5 Dec 2026",
        "currency": "USD", "gst_label": "GST 9%",
        "lines": [
            ("Cement OPC", "4", "ton", "110.00", "440.00"),
            ("Sand, washed", "10", "ton", "27.00", "270.00"),
            ("Steel rebar T12", "1.5", "ton", "820.00", "1230.00"),
        ],
        "subtotal": "1940.00", "delivery": "150.00", "gst": "188.10", "rounding": None, "total": "2278.10",
        "terms": {"payment": "50% deposit", "lead_time": "10 working days", "warranty": "-"},
        "notes": "All prices in US dollars.",
    },
    {
        "id": "c3", "scenario": "c", "file": "scenario-c-construction/c3-seletar-scan.pdf",
        "format": "scan_pdf", "layout": "minimal",
        "supplier": {"name": "Seletar Hardware & Aggregates",
                     "address": "14 Placeholder Crescent, Singapore 000009",
                     "contact": "000-0009",
                     "gst_reg": "FAKE-GST-0009"},
        "quote_no": "SHA 1046", "date": "21 Nov 2026", "valid_until": "21 Dec 2026",
        "currency": "SGD", "gst_label": "GST 9%",
        "lines": [
            ("Cement 50kg bag", "80", "bag", "6.90", "552.00"),
            ("Sand (washed)", "10000", "kg", "0.036", "360.00"),
            ("Rebar 12mm", "1.5", "ton", "1120.00", "1680.00"),
        ],
        # trap: GST worked out on the subtotal only, leaving out the delivery fee
        "subtotal": "2592.00", "delivery": "250.00", "gst": "233.28", "rounding": None, "total": "3075.28",
        "terms": {"payment": "7 days", "lead_time": "3 working days", "warranty": "-"},
        "notes": "Transport by lorry crane.",
    },
]

# Extra edge cases, outside the 3 scored scenarios.
EDGE_CASES = [
    {"id": "e1", "source": "c3", "file": "edge-cases/e1-seletar-blurry-scan.pdf", "format": "poor_scan"},
    {"id": "e2", "source": "b2", "file": "edge-cases/e2-sunbird-email.txt", "format": "pasted_text"},
    {"id": "e3", "source": "a1", "file": "edge-cases/e3-orchidpath-3-pages.pdf", "format": "long_pdf"},
    {
        "id": "e4", "scenario": "c", "file": "edge-cases/e4-jade-dragon-cny.pdf",
        "format": "text_pdf", "layout": "classic",
        "supplier": {"name": "Jade Dragon Building Materials Co., Ltd.",
                     "address": "88 Example Industrial Zone, Foshan, China",
                     "contact": "export@jadedragon.example",
                     "gst_reg": None},
        "quote_no": "JD-EX-2611-07", "date": "21 Nov 2026", "valid_until": "21 Dec 2026",
        "currency": "CNY", "gst_label": None,
        "lines": [
            ("Portland cement 42.5", "4", "ton", "560.00", "2240.00"),
            ("Deformed steel bar 12mm", "1.5", "ton", "4100.00", "6150.00"),
        ],
        "subtotal": "8390.00", "delivery": "1800.00", "gst": None, "rounding": None, "total": "10190.00",
        "terms": {"payment": "T/T in advance", "lead_time": "25 days by sea", "warranty": "-"},
        "notes": "FOB price plus freight to Singapore. Import GST is not included.",
    },
]

# Extra catalogue lines for the 3-page edge case (not in the request, so they stay unmapped).
EXTRA_CLINIC_LINES = [
    ("Gauze swab 10x10cm (pack of 100)", "pack", "3.80"),
    ("Cotton wool balls 500g", "pack", "4.60"),
    ("Disposable syringe 3ml (box of 100)", "box", "9.90"),
    ("Hypodermic needle 23G (box of 100)", "box", "6.50"),
    ("Adhesive plaster strips (box of 100)", "box", "3.20"),
    ("Tongue depressor, wooden (box of 100)", "box", "2.40"),
    ("Specimen container 60ml", "pc", "0.18"),
    ("Thermometer probe cover (box of 100)", "box", "5.70"),
    ("Hand sanitiser 500ml", "bottle", "3.90"),
    ("Disinfectant wipes (tub of 100)", "tub", "6.80"),
    ("Isolation gown, disposable", "pc", "1.25"),
    ("Bed sheet roll, paper", "roll", "7.40"),
    ("Sharps container 1L", "pc", "2.95"),
    ("Elastic bandage 7.5cm", "roll", "1.10"),
    ("Micropore tape 2.5cm", "roll", "0.95"),
]
