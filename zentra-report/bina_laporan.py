#!/usr/bin/env python3
"""
ZENTRA REPORT KIT — pembina laporan (HTML → PDF)

Guna:
  python3 bina_laporan.py --meta meta.json --kandungan badan.html --keluar keluar.pdf
  python3 bina_laporan.py ... --enjin chrome      # fallback (PDF bertag, tiada bookmark)
  python3 bina_laporan.py ... --pdfa              # tambah salinan PDF/A-2b (ghostscript)
  python3 bina_laporan.py ... --sahkan            # jalankan pemeriksaan susun atur

Struktur kandungan (badan.html):
  <h2>  = Bab (auto nombor, mula halaman baharu, masuk Kandungan)
  <h3>  = Sub-bab (masuk Kandungan)
  blok  : <p class="lead">, <p class="intro">, .kpi, table.data, .kotak, .petik,
          figure>img+figcaption, ul.semak, ol.langkah, span.fn (nota kaki)
"""
from __future__ import annotations
import argparse, html, json, re, shutil, subprocess, sys, unicodedata
from pathlib import Path

KIT = Path(__file__).resolve().parent
ASSETS = KIT / "assets"

# ---------------------------------------------------------------- kandungan --
def _slug(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE).strip().lower()
    return re.sub(r"[\s_-]+", "-", t) or "bahagian"

def pecah_bab(html_teks: str):
    """Bahagi fragmen kandungan kepada bab (h2) + kumpul sub-bab (h3)."""
    bahagian = re.split(r"(?=<h2\b)", html_teks)
    bab, n = [], 0
    for blok in bahagian:
        blok = blok.strip()
        if not blok:
            continue
        m = re.search(r"<h2[^>]*>(.*?)</h2>", blok, re.S)
        if not m:
            # kandungan sebelum h2 pertama → bab pengenalan
            n += 1
            bab.append({"id": f"bab-{n}", "no": f"{n:02d}", "tajuk": "Pendahuluan",
                        "intro": "", "isi": blok, "sub": []})
            continue
        judul = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        n += 1
        # buang h2 asal (templat yang bina kepala bab)
        sisa = (blok[:m.start()] + blok[m.end():]).strip()
        # intro = <p class="intro"> pertama
        mi = re.search(r'<p class="intro"[^>]*>(.*?)</p>', sisa, re.S)
        intro = html.unescape(re.sub(r"<[^>]+>", "", mi.group(1))).strip() if mi else ""
        if mi:
            sisa = (sisa[:mi.start()] + sisa[mi.end():]).strip()
        # id + kumpul h3
        subs = []
        def _h3(mm, bno=n):
            t2 = html.unescape(re.sub(r"<[^>]+>", "", mm.group(1))).strip()
            sid = f"bab-{bno}-{_slug(t2)}"
            subs.append({"id": sid, "tajuk": t2})
            return f'<h3 id="{sid}">{mm.group(1)}</h3>'
        sisa = re.sub(r"<h3[^>]*>(.*?)</h3>", _h3, sisa, flags=re.S)
        bab.append({"id": f"bab-{n}", "no": f"{n:02d}", "tajuk": judul,
                    "intro": intro, "isi": sisa, "sub": subs})
    return bab

# -------------------------------------------------------------------- enjin --
def hantar_weasy(html_path: Path, out: Path, varian: str | None = None) -> str:
    """WeasyPrint: bookmark, TOC auto-nombor, metadata, fon CID.
    varian: None | 'pdf/ua-1' (bertag) | 'pdf/a-2b' | 'pdf/a-3b' (arkib)."""
    import weasyprint  # venv ~/.venvs/pdf
    doc = weasyprint.HTML(filename=str(html_path), base_url=str(html_path.parent) + "/")
    kw = {"pdf_variant": varian} if varian else {}
    doc.write_pdf(str(out), **kw)
    return f"weasyprint {weasyprint.__version__}" + (f" [{varian}]" if varian else "")

def hantar_chrome(html_path: Path, out: Path) -> str:
    """Chrome headless: PDF bertag (a11y) tetapi tiada bookmark/TOC-nombor."""
    exe = shutil.which("google-chrome") or shutil.which("chromium")
    if not exe:
        raise RuntimeError("google-chrome tiada")
    cmd = [exe, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--no-pdf-header-footer", "--virtual-time-budget=15000",
           f"--print-to-pdf={out}", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if not out.exists():
        raise RuntimeError(f"chrome gagal: {r.stderr[-400:]}")
    return "chrome-headless"

# ------------------------------------------------------------ pasca-proses --
def pasca(out: Path, meta: dict) -> None:
    """Isi metadata PDF + lapor status struktur (bukti, bukan andaian)."""
    import pymupdf
    d = pymupdf.open(str(out))
    d.set_metadata({
        "title": meta["tajuk"],
        "author": meta["disediakan_oleh"],
        "subject": f'{meta["jenis_dokumen"]} — {meta.get("skop","")}',
        "keywords": meta.get("kata_kunci", f'{meta["entiti"]}, laporan, zentra'),
        "creator": "Zentra Report Kit",
        "producer": "Zentra Report Kit",
    })
    d.save(str(out), incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    d.close()

def varian_pdf(html_path: Path, out: Path, varian: str, tanda: str) -> Path:
    """Keluaran PDF/A atau PDF/UA melalui varian asli WeasyPrint.

    Nota (diuji 19 Sep 2026): varian asli WeasyPrint MENGEKALKAN pautan + bookmark.
    Laluan ghostscript (`gs -dPDFA=2`) juga menghasilkan PDF/A yang sah tetapi
    MEMBUANG semua pautan hiperteks — sebab itu varian WeasyPrint diutamakan.
    Metadata tutorial diambil daripada tag <meta> HTML, jadi TIADA pasca-proses
    pymupdf (menulis semula fail PDF/A boleh membatalkan pematuhan/struktur tag).
    """
    target = out.with_name(f"{out.stem}-{tanda}.pdf")
    hantar_weasy(html_path, target, varian=varian)
    return target

# ------------------------------------------------------------- pemeriksaan --
def sahkan(pdf: Path, meta: dict) -> dict:
    import pymupdf
    d = pymupdf.open(str(pdf))
    MM = 72 / 25.4
    lapor = {"halaman": d.page_count, "saiz_kb": round(pdf.stat().st_size / 1024, 1),
             "bookmark": len(d.get_toc()), "isyarat": []}
    # 0) tanda struktur & pematuhan
    lapor["bertag_pdf_ua"] = d.xref_get_key(d.pdf_catalog(), "StructTreeRoot")[0] != "null"
    oi = d.xref_get_key(d.pdf_catalog(), "OutputIntents")
    lapor["output_intent"] = "ada (PDF/A)" if oi[0] != "null" else None
    lapor["pautan"] = sum(1 for p in d for l in p.get_links())
    # 1) saiz halaman
    saiz = {(round(p.rect.width), round(p.rect.height)) for p in d}
    lapor["saiz_halaman"] = sorted(saiz)
    if saiz != {(595, 842)}:
        lapor["isyarat"].append(f"saiz halaman bukan A4 seragam: {saiz}")
    # 2) limpahan margin (halaman isi: margin 18/24/22/18 mm → tolerans 2mm)
    for i, p in enumerate(d):
        bl = [b for b in p.get_text("blocks") if b[4].strip()]
        if not bl:
            continue
        x0 = min(b[0] for b in bl); x1 = max(b[2] for b in bl)
        y0 = min(b[1] for b in bl); y1 = max(b[3] for b in bl)
        if i == 0:
            continue  # kulit = penuh (bleed)
        if x0 < (18 - 2) * MM or x1 > p.rect.width - (18 - 2) * MM:
            lapor["isyarat"].append(f"P{i+1}: teks hampir/keluar margin sisi (x {x0/MM:.1f}–{x1/MM:.1f}mm)")
        if y0 < 6 * MM or y1 > p.rect.height - 6 * MM:
            lapor["isyarat"].append(f"P{i+1}: teks hampir tepi atas/bawah (y {y0/MM:.1f}–{y1/MM:.1f}mm)")
    # 3) teks bertindih (kotak bertindan > 60%)
    for i, p in enumerate(d):
        bx = [b for b in p.get_text("blocks") if b[4].strip()]
        for a in range(len(bx)):
            for b in range(a + 1, len(bx)):
                A = pymupdf.Rect(bx[a][:4]); B = pymupdf.Rect(bx[b][:4])
                u = A & B
                if not u.is_empty and (u.get_area() / min(A.get_area(), B.get_area())) > 0.6:
                    lapor["isyarat"].append(f"P{i+1}: teks bertindih {bx[a][4][:22]!r}/{bx[b][4][:22]!r}")
    # 4) markdown tersisa
    teks = "\n".join(p.get_text() for p in d)
    for pola, nama in [(r"\*\*", "sisa '**tebal**'"), (r"^\s*\|.*\|", "jadual paip mentah"),
                       (r"target-counter\s*\(", "target-counter tidak selesai"),
                       (r"attr\(href", "attr(href) tidak selesai")]:
        if re.search(pola, teks, re.M):
            lapor["isyarat"].append(nama)
    # 5) metadata
    md = d.metadata or {}
    lapor["metadata"] = {k: md.get(k) for k in ("title", "author", "subject", "keywords")}
    if not md.get("author") or not md.get("subject"):
        lapor["isyarat"].append("metadata author/subject kosong")
    if meta.get("tajuk") not in (md.get("title") or ""):
        lapor["isyarat"].append("tajuk PDF tidak sepadan meta")
    # 6) fon
    fon = set()
    for p in d:
        for f in p.get_fonts(full=True):
            fon.add((f[3], f[2]))
    lapor["fon"] = sorted(fon)
    for nama, jenis in fon:
        if "Type3" in jenis or jenis == "Type3":
            lapor["isyarat"].append(f"fon Type 3 (kualiti cetak rendah): {nama}")
    return lapor

# ------------------------------------------------------------------- utama --
def utama() -> int:
    ap = argparse.ArgumentParser(description="Zentra Report Kit — bina laporan PDF")
    ap.add_argument("--meta", required=True)
    ap.add_argument("--kandungan", required=True)
    ap.add_argument("--keluar", required=True)
    ap.add_argument("--enjin", default="weasy", choices=["weasy", "chrome"])
    ap.add_argument("--lampiran", default=None, help="fail HTML lampiran (pilihan)")
    ap.add_argument("--ua", action="store_true", help="salinan PDF/UA-1 (bertag, aksesibiliti)")
    ap.add_argument("--pdfa", action="store_true", help="salinan PDF/A-2b (arkib, OutputIntent sRGB)")
    ap.add_argument("--sahkan", action="store_true")
    ap.add_argument("--html-sahaja", action="store_true", help="simpan HTML tanpa jana PDF")
    a = ap.parse_args()

    from jinja2 import Template
    meta = json.loads(Path(a.meta).read_text(encoding="utf-8"))
    isi = Path(a.kandungan).read_text(encoding="utf-8")
    lamp = Path(a.lampiran).read_text(encoding="utf-8") if a.lampiran else ""

    bab = pecah_bab(isi)
    out = Path(a.keluar).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    import os
    css_href = os.path.relpath(ASSETS / "zentra-report.css", out.parent)
    html_teks = Template((KIT / "templates/laporan.html.j2").read_text(encoding="utf-8")).render(
        meta=meta, bab=bab, lampiran=lamp, bahasa=meta.get("bahasa", "ms"), css_href=css_href)
    html_path = out.with_suffix(".html")
    html_path.write_text(html_teks, encoding="utf-8")
    print(f"HTML : {html_path} ({len(html_teks)} bait) · bab={len(bab)} · sub={sum(len(b['sub']) for b in bab)}")
    if a.html_sahaja:
        return 0

    enjin = hantar_weasy(html_path, out) if a.enjin == "weasy" else hantar_chrome(html_path, out)
    pasca(out, meta)
    print(f"PDF  : {out} · {out.stat().st_size/1024:.1f} KB · enjin={enjin}")
    if a.ua:
        pu = varian_pdf(html_path, out, "pdf/ua-1", "ua")
        print(f"PDF/UA: {pu} · {pu.stat().st_size/1024:.1f} KB")
    if a.pdfa:
        pa = varian_pdf(html_path, out, "pdf/a-2b", "pdfa")
        print(f"PDF/A: {pa} · {pa.stat().st_size/1024:.1f} KB")
    if a.sahkan:
        lapor = sahkan(out, meta)
        print("SAHKAN:", json.dumps(lapor, ensure_ascii=False, indent=2))
        if lapor["isyarat"]:
            print("!! ISYARAT:", len(lapor["isyarat"]), file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(utama())
