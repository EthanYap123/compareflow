"""Generate the fake quote set into testdata/quotes.

Usage (from the repo root):
    python -m venv tools/fake-quotes/.venv
    tools/fake-quotes/.venv/Scripts/pip install -r tools/fake-quotes/requirements.txt
    tools/fake-quotes/.venv/Scripts/python tools/fake-quotes/generate.py

Output is deterministic: the same data and seed give the same files.
"""

import io
import random
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path

import pymupdf
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from PIL import Image, ImageEnhance, ImageFilter

from quotes import BUYERS, EDGE_CASES, EXTRA_CLINIC_LINES, FAKE_NOTE, QUOTES

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "testdata" / "quotes"
W, H = 595, 842  # A4 in points
SEED = 20261122


def money(value, currency):
    symbol = {"SGD": "S$", "USD": "US$", "CNY": "RMB "}[currency]
    whole, _, cents = value.partition(".")
    sign = "-" if whole.startswith("-") else ""
    whole = whole.lstrip("-")
    grouped = f"{int(whole):,}"
    return f"{sign}{symbol}{grouped}.{cents}" if cents else f"{sign}{symbol}{grouped}"


def num(value):
    if "." in value:
        whole, cents = value.split(".")
        return f"{int(whole):,}.{cents}"
    return f"{int(value):,}"


def text(page, x, y, s, size=9, bold=False, color=(0, 0, 0)):
    page.insert_text((x, y), s, fontsize=size, fontname="hebo" if bold else "helv", color=color)


def rtext(page, x_right, y, s, size=9, bold=False):
    font = pymupdf.Font("hebo" if bold else "helv")
    width = font.text_length(s, fontsize=size)
    text(page, x_right - width, y, s, size, bold)


def watermark(page):
    centre = pymupdf.Point(W / 2, H / 2)
    page.insert_text((120, H / 2 + 40), "SAMPLE - FICTIONAL", fontsize=54, fontname="hebo",
                     color=(0.92, 0.92, 0.92), morph=(centre, pymupdf.Matrix(1, 1).prerotate(-35)))


def footer(page):
    text(page, 40, H - 30, FAKE_NOTE, size=7, color=(0.45, 0.45, 0.45))


def totals_rows(q):
    cur = q["currency"]
    rows = [("Subtotal", money(q["subtotal"], cur))]
    if q["delivery"]:
        rows.append(("Delivery", money(q["delivery"], cur)))
    if q["gst"]:
        rows.append((q["gst_label"], money(q["gst"], cur)))
    if q["rounding"]:
        rows.append(("Rounding", money(q["rounding"], cur)))
    rows.append(("TOTAL", money(q["total"], cur)))
    return rows


def terms_rows(q):
    t = q["terms"]
    return [("Payment terms", t["payment"]), ("Lead time", t["lead_time"]), ("Valid until", q["valid_until"])]


# ---------------------------------------------------------------- PDF layouts

def layout_classic(page, q, lines):
    """Letterhead on the left, boxed table with grid lines."""
    s = q["supplier"]
    watermark(page)
    text(page, 40, 60, s["name"], 15, bold=True)
    text(page, 40, 76, s["address"])
    text(page, 40, 88, s["contact"])
    if s["gst_reg"]:
        text(page, 40, 100, f"GST Reg No: {s['gst_reg']}")
    text(page, 400, 60, "QUOTATION", 16, bold=True)
    text(page, 400, 80, f"Quote No: {q['quote_no']}")
    text(page, 400, 92, f"Date: {q['date']}")
    text(page, 40, 130, "To:", bold=True)
    text(page, 60, 130, BUYERS[q["scenario"]]["name"])
    text(page, 40, 144, f"All prices in {q['currency']}.")

    cols = [40, 70, 330, 380, 430, 490, 555]  # No | Description | Qty | Unit | Unit price | Amount
    heads = ["No", "Description", "Qty", "Unit", "Unit price", "Amount"]
    y = 165
    page.draw_rect(pymupdf.Rect(40, y, 555, y + 18), color=(0, 0, 0), fill=(0.85, 0.85, 0.85))
    for i, hd in enumerate(heads):
        text(page, cols[i] + 4, y + 12, hd, bold=True)
        page.draw_line((cols[i], y), (cols[i], y + 18), color=(0, 0, 0))
    y += 18
    for n, (desc, qty, unit, price, total) in enumerate(lines, 1):
        if y > H - 120:
            footer(page)
            page = page.parent.new_page(width=W, height=H)
            watermark(page)
            y = 60
        page.draw_rect(pymupdf.Rect(40, y, 555, y + 18), color=(0, 0, 0))
        for x in cols:
            page.draw_line((x, y), (x, y + 18), color=(0, 0, 0))
        text(page, cols[0] + 4, y + 12, str(n))
        text(page, cols[1] + 4, y + 12, desc)
        rtext(page, cols[3] - 4, y + 12, num(qty))
        text(page, cols[3] + 4, y + 12, unit)
        rtext(page, cols[5] - 4, y + 12, num(price))
        rtext(page, cols[6] - 4, y + 12, num(total))
        y += 18
    return page, y + 20


def layout_minimal(page, q, lines):
    """Plain text, no grid, centred heading."""
    s = q["supplier"]
    watermark(page)
    head = s["name"].upper()
    font = pymupdf.Font("hebo")
    text(page, (W - font.text_length(head, fontsize=14)) / 2, 60, head, 14, bold=True)
    sub = s["address"] + "  Tel " + s["contact"]
    text(page, (W - pymupdf.Font("helv").text_length(sub, fontsize=8)) / 2, 74, sub, 8)
    text(page, 40, 110, f"QUOTE {q['quote_no']}", 11, bold=True)
    rtext(page, 555, 110, q["date"])
    text(page, 40, 126, f"Attn: {BUYERS[q['scenario']]['name']}")
    y = 160
    text(page, 40, y, "Item", bold=True)
    rtext(page, 360, y, "Qty", bold=True)
    text(page, 370, y, "Unit", bold=True)
    rtext(page, 480, y, "Price", bold=True)
    rtext(page, 555, y, "Total", bold=True)
    page.draw_line((40, y + 5), (555, y + 5), color=(0, 0, 0))
    y += 20
    for desc, qty, unit, price, total in lines:
        text(page, 40, y, desc)
        rtext(page, 360, y, num(qty))
        text(page, 370, y, unit)
        rtext(page, 480, y, num(price))
        rtext(page, 555, y, num(total))
        y += 16
    page.draw_line((40, y - 8), (555, y - 8), color=(0, 0, 0))
    return page, y + 10


def layout_modern(page, q, lines):
    """Coloured header band, shaded rows, details in two columns."""
    s = q["supplier"]
    page.draw_rect(pymupdf.Rect(0, 0, W, 90), color=None, fill=(0.16, 0.32, 0.45))
    watermark(page)
    page.insert_text((40, 45), s["name"], fontsize=16, fontname="hebo", color=(1, 1, 1))
    page.insert_text((40, 62), s["address"], fontsize=8, fontname="helv", color=(1, 1, 1))
    page.insert_text((40, 74), s["contact"] + (f"  |  GST Reg {s['gst_reg']}" if s["gst_reg"] else ""),
                     fontsize=8, fontname="helv", color=(1, 1, 1))
    text(page, 40, 120, "Quotation for", bold=True)
    text(page, 40, 133, BUYERS[q["scenario"]]["name"])
    text(page, 330, 120, "Reference", bold=True)
    text(page, 420, 120, q["quote_no"])
    text(page, 330, 133, "Issued", bold=True)
    text(page, 420, 133, q["date"])
    text(page, 330, 146, "Currency", bold=True)
    text(page, 420, 146, q["currency"])
    y = 175
    page.draw_rect(pymupdf.Rect(40, y - 13, 555, y + 5), color=None, fill=(0.16, 0.32, 0.45))
    for x, hd, right in [(44, "Description", False), (370, "Quantity", True), (380, "Unit", False),
                         (480, "Rate", True), (551, "Line total", True)]:
        if right:
            font = pymupdf.Font("hebo")
            page.insert_text((x - font.text_length(hd, fontsize=9), y), hd, fontsize=9, fontname="hebo", color=(1, 1, 1))
        else:
            page.insert_text((x, y), hd, fontsize=9, fontname="hebo", color=(1, 1, 1))
    y += 20
    for i, (desc, qty, unit, price, total) in enumerate(lines):
        if i % 2 == 0:
            page.draw_rect(pymupdf.Rect(40, y - 12, 555, y + 5), color=None, fill=(0.93, 0.95, 0.97))
        text(page, 44, y, desc)
        rtext(page, 370, y, num(qty))
        text(page, 380, y, unit)
        rtext(page, 480, y, num(price))
        rtext(page, 551, y, num(total))
        y += 18
    return page, y + 12


LAYOUTS = {"classic": layout_classic, "minimal": layout_minimal, "modern": layout_modern}


def build_pdf(q, lines=None):
    doc = pymupdf.open()
    page = doc.new_page(width=W, height=H)
    page, y = LAYOUTS[q["layout"]](page, q, lines or q["lines"])
    for label, value in totals_rows(q):
        bold = label == "TOTAL"
        rtext(page, 470, y, label, 10 if bold else 9, bold)
        rtext(page, 555, y, value, 10 if bold else 9, bold)
        y += 15
    y += 15
    for label, value in terms_rows(q):
        text(page, 40, y, f"{label}:", bold=True)
        text(page, 140, y, value)
        y += 13
    if q.get("notes"):
        text(page, 40, y + 8, q["notes"], 8, color=(0.3, 0.3, 0.3))
    footer(page)
    return doc


# ---------------------------------------------------------------- images

def render(doc, page_no=0, dpi=150):
    pix = doc[page_no].get_pixmap(dpi=dpi)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def add_grain(img, rng, amount):
    """Blend in seeded random grain; a higher amount gives stronger grain."""
    w, h = img.size
    noise = Image.frombytes("L", (w, h), rng.randbytes(w * h)).convert("RGB")
    return Image.blend(img, noise, 0.08 * amount / 40)


def save_pdf(doc, path):
    """Save without timestamps or random IDs so the same data gives the same bytes."""
    doc.set_metadata({"producer": "", "creator": "", "creationDate": "", "modDate": ""})
    doc.save(path, garbage=4, deflate=True, no_new_id=True)


def fix_zip_times(path):
    """Give every entry in an .xlsx a fixed timestamp."""
    with zipfile.ZipFile(path) as src:
        entries = [(info, src.read(info.filename)) for info in src.infolist()]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as dst:
        for info, data in entries:
            if info.filename == "docProps/core.xml":  # openpyxl stamps the save time here
                data = re.sub(rb"(<dcterms:modified[^>]*>)[^<]*", rb"\g<1>2026-11-21T00:00:00Z", data)
            fixed = zipfile.ZipInfo(info.filename, date_time=(2026, 11, 22, 0, 0, 0))
            fixed.compress_type = zipfile.ZIP_DEFLATED
            dst.writestr(fixed, data)


def scanned(img, rng, angle, blur, quality):
    img = img.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
    img = add_grain(img, rng, 40)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    if blur:
        img = img.filter(ImageFilter.GaussianBlur(blur))
    buf = io.BytesIO()
    img.convert("L").save(buf, "JPEG", quality=quality)
    return buf.getvalue()


def phone_photo(img, rng):
    """Printed page photographed at a slight angle on a desk, with uneven light."""
    w, h = img.size
    canvas = Image.new("RGB", (int(w * 1.12), int(h * 1.08)), (120, 105, 90))
    canvas.paste(img, (int(w * 0.06), int(h * 0.04)))
    cw, ch = canvas.size
    # perspective: top edge slightly narrower than the bottom
    inset = int(cw * 0.035)
    quad = (inset, 0, 0, ch, cw, ch, cw - inset, 0)
    img = canvas.transform((cw, ch), Image.QUAD, quad, resample=Image.BICUBIC)
    shade = Image.linear_gradient("L").resize((cw, ch)).rotate(25, expand=False)
    shade = ImageEnhance.Brightness(shade.convert("RGB")).enhance(0.35)
    img = Image.blend(img, shade, 0.18)
    img = img.rotate(-2.0, resample=Image.BICUBIC, expand=True, fillcolor=(120, 105, 90))
    img = add_grain(img, rng, 30).filter(ImageFilter.GaussianBlur(0.6))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=78)
    return buf.getvalue()


def image_pdf(jpeg_pages):
    doc = pymupdf.open()
    for jpeg in jpeg_pages:
        page = doc.new_page(width=W, height=H)
        page.insert_image(pymupdf.Rect(0, 0, W, H), stream=jpeg, keep_proportion=True)
    return doc


# ---------------------------------------------------------------- other formats

def build_xlsx(q, path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Quotation"
    s = q["supplier"]
    bold = Font(bold=True)
    ws["A1"] = s["name"]
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = s["address"]
    ws["A3"] = s["contact"]
    ws["A4"] = f"GST Reg No: {s['gst_reg']}"
    ws["E1"] = "QUOTATION"
    ws["E1"].font = Font(bold=True, size=14)
    ws["E2"], ws["F2"] = "Quote No", q["quote_no"]
    ws["E3"], ws["F3"] = "Date", q["date"]
    ws["A6"], ws["B6"] = "Customer", BUYERS[q["scenario"]]["name"]
    ws["A6"].font = bold
    heads = ["Item", "Description", "Qty", "UOM", "Unit Price (SGD)", "Amount (SGD)"]
    for col, hd in enumerate(heads, 1):
        cell = ws.cell(row=8, column=col, value=hd)
        cell.font = bold
        cell.fill = PatternFill("solid", fgColor="DDEBD9")
    row = 9
    for n, (desc, qty, unit, price, total) in enumerate(q["lines"], 1):
        ws.cell(row=row, column=1, value=n)
        ws.cell(row=row, column=2, value=desc)
        ws.cell(row=row, column=3, value=float(qty))
        ws.cell(row=row, column=4, value=unit)
        ws.cell(row=row, column=5, value=float(price)).number_format = "#,##0.00"
        ws.cell(row=row, column=6, value=float(total)).number_format = "#,##0.00"
        row += 1
    row += 1
    ws.cell(row=row, column=5, value="Subtotal").font = bold
    ws.cell(row=row, column=6, value=float(q["subtotal"])).number_format = "#,##0.00"
    row += 2  # gap, then the extra charges further down the sheet
    ws.cell(row=row, column=2, value=q["notes"])
    row += 1
    ws.cell(row=row, column=5, value="Delivery fee").font = bold
    ws.cell(row=row, column=6, value=float(q["delivery"])).number_format = "#,##0.00"
    row += 1
    ws.cell(row=row, column=5, value=q["gst_label"]).font = bold
    ws.cell(row=row, column=6, value=float(q["gst"])).number_format = "#,##0.00"
    row += 1
    ws.cell(row=row, column=5, value="Grand Total").font = bold
    ws.cell(row=row, column=6, value=float(q["total"])).number_format = "#,##0.00"
    row += 2
    for label, value in terms_rows(q):
        ws.cell(row=row, column=1, value=label).font = bold
        ws.cell(row=row, column=2, value=value)
        row += 1
    ws.cell(row=row + 1, column=1, value=FAKE_NOTE).font = Font(italic=True, color="777777")
    for col, width in zip("ABCDEF", [16, 30, 8, 10, 18, 16]):
        ws.column_dimensions[col].width = width
    for r in ws.iter_rows(min_row=9, max_row=row, min_col=3, max_col=6):
        for c in r:
            c.alignment = Alignment(horizontal="right")
    wb.properties.creator = "Greenleaf Pantry Wholesale (fictional)"
    wb.properties.created = wb.properties.modified = datetime(2026, 11, 21)
    wb.save(path)
    fix_zip_times(path)


def build_email(q):
    cur = q["currency"]
    body = [
        f"Subject: Re: Quote request - coffee, milk, sugar",
        f"From: {q['supplier']['name']}",
        "",
        "Hi, thanks for asking. Price for your order as below:",
        "",
    ]
    for desc, qty, unit, price, total in q["lines"]:
        body.append(f"- {desc} {qty}{unit} x ${price} = ${total}")
    body += [
        "",
        f"Total ${q['total']}. We are not GST registered so no GST.",
        f"Delivery free. Can deliver {q['terms']['lead_time'].lower()} after confirm. Payment {q['terms']['payment'].lower()}.",
        f"Price valid until {q['valid_until']}.",
        "",
        "Thanks,",
        "Auntie Lim",
        q["supplier"]["name"],
        "",
        f"-- {FAKE_NOTE}",
    ]
    return "\n".join(body) + "\n"


# ---------------------------------------------------------------- main

def main():
    rng = random.Random(SEED)
    OUT.mkdir(parents=True, exist_ok=True)
    by_id = {q["id"]: q for q in QUOTES}

    for q in QUOTES:
        path = OUT / q["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        if q["format"] == "text_pdf":
            save_pdf(build_pdf(q), path)
        elif q["format"] == "scan_pdf":
            img = render(build_pdf(q), dpi=200)
            save_pdf(image_pdf([scanned(img, rng, angle=0.8, blur=0.4, quality=80)]), path)
        elif q["format"] == "photo":
            path.write_bytes(phone_photo(render(build_pdf(q), dpi=150), rng))
        elif q["format"] == "xlsx":
            build_xlsx(q, path)
        print("wrote", path.relative_to(ROOT))

    for e in EDGE_CASES:
        path = OUT / e["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        if e["format"] == "poor_scan":
            img = render(build_pdf(by_id[e["source"]]), dpi=110)
            save_pdf(image_pdf([scanned(img, rng, angle=2.5, blur=1.3, quality=45)]), path)
        elif e["format"] == "pasted_text":
            path.write_text(build_email(by_id[e["source"]]), encoding="utf-8", newline="\n")
        elif e["format"] == "long_pdf":
            base = by_id[e["source"]]
            extra = []
            for i in range(5):  # 75 extra catalogue lines push the quote onto 3 pages
                for desc, unit, price in EXTRA_CLINIC_LINES:
                    extra.append((f"{desc}" + ("" if i == 0 else f" - option {i + 1}"), "0", unit, price, "0.00"))
            lines = base["lines"][:2] + extra + base["lines"][2:]
            save_pdf(build_pdf(base, lines), path)
        elif e["format"] == "text_pdf":
            save_pdf(build_pdf(e), path)
        print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    sys.exit(main())
