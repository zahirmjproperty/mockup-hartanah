#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
POC "Tanya Ali" — backend AI assistant untuk web Zahir MJ Property & Mr Tanah.
Preview/POC sahaja: kunci API kekal di pelayan (TIDAK pernah dihantar ke pelayar).
Jalankan: python3 server.py   (lalai 127.0.0.1:8795)

Guardrail: AI hanya menjawab berdasarkan data listing sebenar (data/listings.js)
+ FAQ terkawal. Tiada angka rekaan. Tiada data peribadi pelanggan dihantar ke LLM.
"""
import json, os, re, time, hashlib, threading, subprocess, urllib.request, urllib.error
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HOME = os.path.expanduser("~")
ZMP_JS = "/home/ubuntu/zahir-web/data/listings.js"
MT_JS = "/home/ubuntu/mrtanah-site/data/listings.js"
IMG_DIR = "/home/ubuntu/mockup-hartanah/img"
LOG = "/home/ubuntu/mockup-hartanah/poc-ai/log.jsonl"
TEMUJANJI_LOG = "/home/ubuntu/mockup-hartanah/poc-ai/temujanji.jsonl"
RATES = os.path.join(HOME, ".hermes/ai_rates.json")

ENV = {}
for line in open(os.path.join(HOME, ".hermes/.env")):
    m = re.match(r"^([A-Z0-9_]+)=(.*)$", line.strip())
    if m:
        ENV[m.group(1)] = m.group(2).strip().strip('"')

API_KEY = ENV.get("DEEPSEEK_API_KEY", "")
BASE = ENV.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
MODEL = os.environ.get("ALI_MODEL", "deepseek-flash")
PORT = int(os.environ.get("ALI_PORT", "8795"))
ALLOWED_ORIGINS = ("https://zahirmjproperty.github.io", "https://mrtanah.com",
                   "https://zahirmjproperty.com", "https://www.mrtanah.com",
                   "https://www.zahirmjproperty.com",
                   "http://127.0.0.1:8099", "http://localhost:8099", "http://127.0.0.1:8000")

# ---------------------------------------------------------------- data listing
_cache = {"t": 0, "z": [], "m": []}


def _load(path):
    s = open(path).read()
    return json.loads(s[s.index("window.LISTINGS"):].split("=", 1)[1].rsplit(";", 1)[0])


def listings():
    if time.time() - _cache["t"] > 60:
        _cache["z"] = [x for x in _load(ZMP_JS) if x.get("active")]
        _cache["m"] = [x for x in _load(MT_JS) if x.get("active")]
        _cache["t"] = time.time()
    return _cache["z"], _cache["m"]


# ---------------------------------------------------------------- retrieval-lite
NEGERI = ["selangor", "kuala lumpur", "kl", "pahang", "putrajaya", "melaka", "negeri sembilan",
          "johor", "penang", "pulau pinang", "perak", "kedah", "kelantan", "terengganu",
          "sabah", "sarawak", "bangi", "kajang", "cyberjaya", "janda baik", "hulu langat",
          "port dickson", "sentul", "shah alam", "banting", "sepang", "ayer keroh",
          "sungai merab", "teluk kemang"]
KAT = {"pertanian": ["pertanian", "dusun", "kebun", "sawit", "getah", "durian", "ladang", "tanah"],
       "bangunan": ["bungalow", "banglo", "lot banglo"],
       "perumahan": ["rumah", "teres", "semi", "apartmen", "kondominium", "kondo", "flat"],
       "komersial": ["komersial", "kedai", "pejabat", "shoplot"],
       "perindustrian": ["industri", "kilang", "gudang"]}


def parse_q(q):
    ql = q.lower()
    want = set()
    for k, ws in KAT.items():
        if any(w in ql for w in ws):
            want.add(k)
    negeri = [n for n in NEGERI if n in ql]
    freehold = "freehold" in ql
    leasehold = "leasehold" in ql
    murah = any(w in ql for w in ["murah", "bawah", "below", "budget", "bajet"])
    ekars = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*(?:ekar|acre)", ql)]
    # harga: RM500k / 500k / 1.5j / 2 juta / 500000
    lim = None
    m1 = re.search(r"rm?\s?(\d+(?:\.\d+)?)\s*(k|ribu|j|juta|m)\b", ql, re.I)
    if m1:
        v = float(m1.group(1))
        lim = v * (1_000 if m1.group(2).lower() in ("k", "ribu") else 1_000_000)
    else:
        m2 = re.search(r"rm\s?([\d,]{5,})", ql)
        if m2:
            lim = float(m2.group(1).replace(",", ""))
    # jenis hartanah disebut pengguna
    jenis_kata = [w for w in ("teres", "semi-d", "semid", "banglo", "bungalow", "apartmen",
                              "apartment", "kondo", "kondominium", "flat", "kedai", "pejabat",
                              "shoplot", "dusun", "kebun", "sawit", "getah")
                  if w in ql]
    trak = re.findall(r"(mtcoa-\d+|mt-\d+|coa-\d+)", ql, re.I)
    return want, negeri, freehold, leasehold, murah, ekars, lim, [t.upper() for t in trak], jenis_kata


def skor(l, kw):
    want, negeri, fh, lh, murah, ekars, lim, trak, jenis_kata = kw
    s = 0
    if l["tracking"] in trak:
        s += 200
    hay = " ".join(str(l.get(k, "")) for k in
                   ("title", "location", "state", "type", "kategori", "zoning", "sekatan",
                    "description", "tenure", "project_name")).lower()
    for n in negeri:
        if n in hay:
            s += 25
    if jenis_kata and any(w in hay for w in jenis_kata):
        s += 22
    if want:
        kat = (l.get("kategori") or "").lower()
        jen = (l.get("type") or "").lower()
        if kat in want or any(w in hay for w in KAT.get(kat, [])):
            s += 18
        if any(w in jen for w in ["tanah", "bungalow", "banglo"]) and "bangunan" in want:
            s += 10
    if fh and (l.get("tenure") or "").lower() == "freehold":
        s += 12
    if lh and (l.get("tenure") or "").lower() == "leasehold":
        s += 12
    p = l.get("price") or 0
    if lim:
        s += 20 if p and p <= lim else -25
    if murah and p:
        s += 6
    if ekars:
        ar = (l.get("land_area") or "").lower()
        for e in ekars:
            if f"{e:g} ekar" in ar or f"{e:g} acre" in ar:
                s += 30
    return s


def ansuran(p):
    """Ansuran anggaran: 4.00% p.a., 35 tahun, 90% pembiayaan (dikira pelayan)."""
    if not p:
        return None
    loan, r, n = p * 0.90, 0.04 / 12, 35 * 12
    return round(loan * r / (1 - (1 + r) ** -n))


def konteks(z, m, kw, had=12):
    pool = [(skor(l, kw), l) for l in (m + z)]
    pool = [(s, l) for s, l in pool if s > 0]
    pool.sort(key=lambda t: (-t[0], -(t[1].get("price") or 0)))
    pilih = [l for _, l in pool[:had]]
    if not pilih:                                     # tiada padanan → saham terkini
        pilih = sorted(m, key=lambda x: x.get("date") or "", reverse=True)[:8]
    baris = []
    for l in pilih:
        b = (f'{l["tracking"]} | {l["title"]} | {l.get("location","")} | {l.get("price_label") or ""}'
             f' | {l.get("land_area") or ""} | {l.get("built_up") or ""}'
             f' | {l.get("tenure") or ""} | {l.get("kategori") or l.get("type") or ""}'
             f' | guna tanah: {l.get("zoning") or "-"} | sekatan: {l.get("sekatan") or "-"}'
             f' | psf: {l.get("psf") or "-"}')
        if l.get("bedrooms"):
            b += f' | {l["bedrooms"]} bilik, {l.get("bathrooms")} bilik air'
        if l.get("jenis"):
            j = l["jenis"]
            b += " | " + ("+".join(j) if isinstance(j, list) else str(j))
        a = ansuran(l.get("price"))
        if a:
            b += f" | ansuran anggaran RM{a:,}/bln (4.00%, 35 thn, 90%)"
        baris.append(b)
    return pilih, "\n".join(baris)


SISTEM = """Anda "Ali", pembantu hartanah Zahir MJ Property (zahirmjproperty.com) dan Mr Tanah (mrtanah.com).
Tugasan: bantu pelawat mencari hartanah dan faham data listing.

PERATURAN KERAS (jangan langgar):
1. Jawab HANYA menggunakan DATA LISTING / INFO yang diberi di bawah. Jangan sekali-kali mengarang
   angka (keluasan, harga, tahun, bilangan bilik, ciri rumah) yang tiada dalam data.
2. Jika jawapan tiada dalam data, kata dengan jujur: "Saya tak pasti" dan tawarkan butang WhatsApp
   untuk bercakap dengan pasukan. JANGAN teka.
3. JANGAN dedahkan nama pemilik, kos, komisen, atau hal dalaman. JANGAN mengaku anda manusia.
4. JANGAN beri nasihat undang-undang, cukai, atau jaminan pinjaman sebagai fakta muktamad.
   Untuk kelayakan pinjaman, rujuk kalkulator/semak kelayakan. Untuk geran/pelan sebenar,
   arahkan kepada pasukan (dokumen hanya diberi kepada pembeli serius).
5. Isu harga/rundingan/dokumen/tawaran rasmi = di luar bidang anda → tawarkan WhatsApp.

GAYA: Bahasa Melayu Malaysia, ringkas (maksimum 110 patah), mesra, profesional.
Jika menyenaraikan hartanah: MAKSIMUM 3 listing, satu baris setiap satu dalam format
'KOD — lokasi — harga — keluasan — hakmilik'. Gunakan TAJUK/lokasi tepat seperti dalam data.
Jangan guna jadual markdown. Mesti habiskan ayat terakhir (jangan berhenti separuh jalan).
Anggaran ansuran SUDAH dikira dalam data (setiap baris ada "ansuran anggaran RM…/bln").
JANGAN kira sendiri — guna angka itu sahaja, dan nyatakan ia anggaran.
NOMBOR WHATSAPP: guna nombor laman ini SAHAJA (lihat "nombor WhatsApp laman ini" di bawah).
Jangan sebut nombor laman yang satu lagi.
"""

FAQ = """INFO TETAP:
- WhatsApp: Zahir MJ Property 012-2310119 (laman ZMP) · Mr Tanah 016-3119076 (laman MT).
  Sebut nombor MENGIKUT laman pelawat sahaja (MT → 016-3119076; ZMP → 012-2310119).
- Semua hartanah melalui semakan status pemilikan. Pelan & geran penuh diberi kepada pembeli serius.
- Ejen berdaftar: PEA 2684. Pejabat: DNA Workspace, Seksyen 9, Bandar Baru Bangi.
- Ada kalkulator pinjaman dan semak kelayakan (DSR) di laman Zahir MJ Property.
- Lawatan tapak boleh diatur melalui BORANG temujanji (butang disediakan oleh sistem).

BORANG YANG ADA (jangan cetak URL — sistem akan tunjuk butang boleh klik):
- Borang temujanji lawatan tapak (nama, WhatsApp, tarikh) — untuk atur lawatan apa-apa hartanah.
- Semak kelayakan pinjaman & DSR (percuma) — laman Zahir MJ Property.
- Kalkulator ansuran bulanan — laman Zahir MJ Property.
- Serah listing (pemilik ejen nak jual/sewa/develop hartanah).
- Serah dokumen urus niaga · Mohon sewa · Aduan kerosakan (portal).
Apabila pelanggan menyebut lawatan tapak / temujanji / nak jumpa / nak isi borang, sebut bahawa
anda akan sediakan BUTANG BORANG di bawah jawapan (jangan cetak pautan mentah).
"""

# ---------------------------------------------------------------- borang boleh klik
BASE_TEMUJANJI = os.environ.get("ALI_BASE_TEMUJANJI",
                                "https://zahirmjproperty.github.io/mockup-hartanah/temujanji.html")
BORANG = {
    "temujanji": {"label": "📅 Isi borang lawatan tapak", "jenis": "borang",
                  "kata": ["lawatan", "tapak", "temujanji", "viewing", "tengok", "lihat rumah",
                           "lihat tanah", "jumpa", "visit", "tur"]},
    "kelayakan": {"label": "✅ Semak kelayakan & DSR (percuma)", "jenis": "borang",
                  "url": "https://zahirmjproperty.com/semak-kelayakan.html",
                  "kata": ["kelayakan", "dsr", "layak", "pinjaman", "loan", "bank", "gaji",
                           "komitmen", "lulus"]},
    "kalkulator": {"label": "🧮 Kira ansuran (kalkulator)", "jenis": "borang",
                   "url": "https://zahirmjproperty.com/kalkulator.html",
                   "kata": ["kalkulator", "ansuran", "bulanan", "installment", "faedah", "interest"]},
    "serah_listing": {"label": "📤 Serah listing (nak jual/sewa)", "jenis": "borang",
                      "kata": ["nak jual", "hendak jual", "nak sewa", "hendak sewa", "serah listing",
                               "senaraikan", "list kan", "develop", "pasarkan", "jual rumah saya",
                               "jual tanah saya"]},
    "serah_dokumen": {"label": "📁 Serah dokumen urus niaga", "jenis": "borang",
                      "kata": ["serah dokumen", "hantar dokumen", "ic", "salinan", "geran asal"]},
}
BORANG_MT = {
    "serah_listing": {"label": "📤 Serah listing tanah (nak jual)", "jenis": "borang",
                      "url": "https://mrtanah.com/jual-sewa-develop.html",
                      "kata": ["nak jual", "hendak jual", "nak sewa", "hendak sewa", "serah listing",
                               "senaraikan", "list kan", "jual tanah saya", "jual tanah", "nak develop",
                               "pasarkan tanah", "ada tanah nak jual", "ada lot nak jual"]},
    "serah_dokumen": {"label": "📁 Serah dokumen urus niaga", "jenis": "borang",
                      "url": "https://mrtanah.com/serah-dokumen.html",
                      "kata": ["serah dokumen", "hantar dokumen", "salinan ic", "geran asal"]},
    "aduan": {"label": "🛠 Aduan kerosakan (penyewa/pemilik)", "jenis": "borang",
              "url": "https://mrtanah.com/portal/lapor-kerosakan.html",
              "kata": ["aduan", "kerosakan", "rosak", "bocor", "baiki", "maintenance", "repair"]},
    "ladang": {"label": "🌴 Portal ladang (SAT)", "jenis": "borang",
               "url": "https://mrtanah.com/portal/ladang/index.html",
               "kata": ["ladang", "kebun", "sawit", "pertanian", "tanam"]},
    "kelayakan": {"label": "✅ Semak kelayakan & DSR (percuma)", "jenis": "borang",
                  "url": "https://zahirmjproperty.com/semak-kelayakan.html",
                  "kata": ["kelayakan", "dsr", "pinjaman", "loan", "bank", "gaji", "layak"]},
    "kalkulator": {"label": "🧮 Kira ansuran (kalkulator)", "jenis": "borang",
                   "url": "https://zahirmjproperty.com/kalkulator.html",
                   "kata": ["kalkulator", "ansuran", "bulanan", "faedah", "interest"]},
}


def cta_untuk(soalan, laman, kod=None, tajuk=None):
    """Pulangkan senarai butang (maks 2) ikut niat soalan."""
    ql = (soalan or "").lower()
    reg = dict(BORANG)
    if laman == "mt":
        reg.update(BORANG_MT)
    pilih = []
    for nama, b in reg.items():
        if any(k in ql for k in b.get("kata", [])):
            pilih.append(nama)
    # temujanji diberi keutamaan bila disebut
    if "temujanji" in pilih:
        pilih.remove("temujanji")
        pilih.insert(0, "temujanji")
    butang = []
    for nama in pilih[:2]:
        b = reg[nama]
        if nama == "temujanji":
            from urllib.parse import quote
            url = (f"{BASE_TEMUJANJI}?laman={laman}"
                   + (f"&kod={quote(kod)}&tajuk={quote((tajuk or '')[:80])}" if kod else ""))
        else:
            url = b["url"]
        butang.append({"label": b["label"], "url": url, "jenis": b["jenis"]})
    return butang



def _panggil(msgs, thinking_off=True, max_tokens=700):
    muatan = {"model": MODEL, "messages": msgs, "temperature": 0, "max_tokens": max_tokens,
              "stream": False}
    if thinking_off:
        # V4.1-Flash ialah model "reasoning": matikan supaya jawapan tidak dipotong
        muatan["thinking"] = {"type": "disabled"}
    body = json.dumps(muatan).encode()
    req = urllib.request.Request(BASE.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + API_KEY})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.loads(r.read())
    return (d["choices"][0]["message"].get("content") or "").strip(), d.get("usage", {}), round(time.time() - t0, 2)


def _terpotong(a):
    """Kesan jawapan yang terhenti separuh jalan (quirk model V4.1-Flash)."""
    a = (a or "").strip()
    return len(a) < 160 and not re.search(r"[.!?)\]]\s*$", a)


def tanya(soalan, sejarah, laman, listing_hint=None, nama=None, bil=1):
    z, m = listings()
    kw = parse_q(soalan + " " + (listing_hint or ""))
    pilih, ctx = konteks(z, m, kw)
    kekangan = []
    if kw[6]:
        kekangan.append(f"harga maksimum RM{int(kw[6]):,}")
    if kw[1]:
        kekangan.append("kawasan/negeri: " + ", ".join(kw[1]))
    if kw[8]:
        kekangan.append("jenis: " + ", ".join(kw[8]))
    if kw[2]:
        kekangan.append("mesti freehold")
    if kw[3]:
        kekangan.append("mesti leasehold")
    if kw[5]:
        kekangan.append("keluasan: " + ", ".join(f"{e:g} ekar" for e in kw[5]))
    arahan_nama = ""
    if nama:
        arahan_nama = ("\nPelawat ini sudah memperkenalkan diri sebagai " + nama +
                       ". Panggil dengan hormat (Encik/Puan " + nama + ") sekali-sekala sahaja.")
    elif bil >= 2:
        arahan_nama = ("\nSapaan: tanya nama pelawat dengan sopan SATU kali sahaja dalam jawapan ini "
                       "(cth: \"Boleh saya tahu nama encik/puan?\"), lepas itu jangan tanya lagi.")
    msgs = [{"role": "system", "content": SISTEM + "\n" + FAQ +
             "\nDATA LISTING (sumber tunggal kebenaran):\n" + ctx +
             ("\nKekangan yang dikesan daripada soalan: " + "; ".join(kekangan) if kekangan else "") +
             ("\nKonteks halaman: pelawat sedang melihat " + listing_hint if listing_hint else
              "\nKonteks halaman: laman " + ("Mr Tanah (tanah/pertanian/lot banglo)" if laman == "mt"
                                             else "Zahir MJ Property (rumah/komersial)")) +
             arahan_nama}]
    for t in (sejarah or [])[-6:]:
        if t.get("role") in ("user", "assistant") and t.get("content"):
            msgs.append({"role": t["role"], "content": str(t["content"])[:600]})
    msgs.append({"role": "user", "content": soalan[:600]})

    ans, u, lat = _panggil(msgs, thinking_off=True)
    if _terpotong(ans):                      # cuba semula tanpa mematikan "thinking"
        try:
            ans2, u2, lat2 = _panggil(msgs, thinking_off=False, max_tokens=2000)
            if len(ans2) > len(ans):
                ans, u, lat = ans2, u2, lat + lat2
        except Exception:
            pass
    return ans, pilih, u, lat


def betulkan(ans, laman):
    """Pembetulan deterministik: nombor WhatsApp & jenama mesti ikut laman pelawat."""
    if laman == "mt":
        for a, b in (("012-2310119", "016-3119076"), ("012 2310 119", "016-3119076"),
                     ("+60122310119", "+60163119076"), ("Zahir MJ Property", "Mr Tanah")):
            ans = ans.replace(a, b)
    else:
        for a, b in (("016-3119076", "012-2310119"), ("016 3119 076", "012-2310119"),
                     ("+60163119076", "+60122310119"), ("Mr Tanah", "Zahir MJ Property")):
            ans = ans.replace(a, b)
    return ans


def kos(u):
    try:
        reg = json.load(open(RATES))
        ok = reg["providers"]["deepseek"]["models"]["deepseek-flash"]
        h = time.localtime()
        peak = h.tm_wday < 5 and ((9 <= h.tm_hour < 12) or (14 <= h.tm_hour < 18))
        t = ok["peak" if peak else "offpeak"]
        myr = reg.get("usd_to_myr", 4.03)
        i = u.get("prompt_tokens", 0)
        hid = u.get("prompt_cache_hit_tokens", 0)
        out = u.get("completion_tokens", 0)
        usd = ((i - hid) * t["input_miss"] + hid * t["cache_hit"] + out * t["output"]) / 1e6
        return round(usd * myr, 5), ("peak" if peak else "off-peak")
    except Exception:
        return None, None


def imej(l):
    """Gambar kecil untuk kad dalam chat — guna URL gambar listing SEBENAR (=w200)."""
    try:
        u = (l.get("images") or [None])[0]
        if not u:
            return None
        if "googleusercontent.com" in u:                 # Drive/lh3 → minta saiz kecil
            return re.sub(r"=w\d+$", "=w200", u) if re.search(r"=w\d+$", u) else u + "=w200"
        return u
    except Exception:
        return None


# =========================================================== v2: rekod + analitik
# Ditambah 2026-09-12 (kelulusan Zahir): rekod perbualan penuh, identiti (nama/WA),
# geo percuma, halaman analitik ber-token. Semua kos RM0 (tiada API berbayar).
import urllib.parse
import html as _html
import mimetypes

LOG_DIR = os.environ.get("ALI_LOG_DIR", os.path.join(HOME, "ali-logs"))
GEO_CACHE = os.path.join(LOG_DIR, "geo-cache.json")
SESI_STORE = os.path.join(LOG_DIR, "sesi.json")
TOKEN_FILE = os.path.join(HOME, ".hermes/state/ali_analitik_token.txt")
# Mod pratonton (POC): hidangkan salinan laman sebenar dari folder ini.
# Kosongkan pada produksi supaya tiada fail tempatan terdedah.
PREVIEW_DIR = os.environ.get("ALI_PREVIEW_DIR", "")
_geo_lock = threading.Lock()
_sesi_lock = threading.Lock()
SETEMPAT = ("127.", "10.", "192.168.", "172.16.", "172.17.", "172.18.", "172.19.",
            "::1", "localhost")


def analitik_token():
    """Token akses halaman analitik (fail tempatan, 24 aksara)."""
    try:
        t = open(TOKEN_FILE).read().strip()
        if t:
            return t
    except Exception:
        pass
    t = hashlib.sha256(os.urandom(32)).hexdigest()[:24]
    os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
    with open(TOKEN_FILE, "w") as f:
        f.write(t + "\n")
    return t


def sesi_id(ip, ua):
    """Kumpulkan mesej dalam satu perbualan tanpa simpan IP berulang."""
    return hashlib.sha256((ip + "|" + ua + "|" + time.strftime("%Y-%m-%d")).encode()).hexdigest()[:10]


def _baca(path, lalai):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return lalai


def _tulis(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, ensure_ascii=False)
    os.replace(tmp, path)


def _geo(ip):
    """Geo percuma ip-api.com (45 req/min) + cache fail. Miss → cari di latar (tak lewatkan chat)."""
    if not ip or ip.startswith(SETEMPAT):
        return {"negara": "Setempat", "bandar": "-", "isp": "-", "asn": ""}
    c = _baca(GEO_CACHE, {})
    if ip in c:
        return c[ip]
    threading.Thread(target=_geo_cari, args=(ip,), daemon=True).start()
    return {}


def _geo_cari(ip):
    try:
        u = "http://ip-api.com/json/" + urllib.parse.quote(ip) + \
            "?fields=status,country,countryCode,city,isp,as"
        with urllib.request.urlopen(u, timeout=4) as r:
            d = json.loads(r.read())
        if d.get("status") == "success":
            g = {"negara": d.get("country") or "-", "kod": d.get("countryCode") or "",
                 "bandar": d.get("city") or "-", "isp": d.get("isp") or "", "asn": d.get("as") or ""}
            with _geo_lock:
                c = _baca(GEO_CACHE, {})
                c[ip] = g
                _tulis(GEO_CACHE, c)
            return g
    except Exception:
        pass
    return {}


def semua_sesi():
    return _baca(SESI_STORE, {})


def sesi(sid):
    return semua_sesi().get(sid) or {}


def sesi_kemas(sid, tambah):
    """Kemas kini indeks ringkas satu sesi (untuk halaman analitik + Sheet)."""
    with _sesi_lock:
        s = _baca(SESI_STORE, {})
        v = s.get(sid) or {"mula": tambah.get("t")}
        v.update({k: x for k, x in tambah.items() if x is not None})
        v["ts"] = time.time()
        v["kod"] = sorted(set((v.get("kod") or []) + (tambah.get("kod") or [])))
        s[sid] = v
        had = time.time() - 400 * 86400
        s = {k: x for k, x in s.items() if x.get("ts", 0) >= had}
        _tulis(SESI_STORE, s)
    return v


def rekod_chat(rec):
    """Tulis rekod penuh (soalan + jawapan) ke fail harian JSONL."""
    os.makedirs(LOG_DIR, exist_ok=True)
    p = os.path.join(LOG_DIR, (rec.get("t") or time.strftime("%Y-%m-%dT%H:%M:%S"))[:10] + ".jsonl")
    with open(p, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def data_analitik(hari=7):
    hari = max(1, min(int(hari or 7), 90))
    had = time.time() - hari * 86400
    senarai = [dict(v, sesi=k) for k, v in semua_sesi().items() if v.get("ts", 0) >= had]
    senarai.sort(key=lambda v: v.get("ts", 0), reverse=True)
    ids = {v["sesi"] for v in senarai}
    skrip = {}
    if os.path.isdir(LOG_DIR):
        for fn in sorted(os.listdir(LOG_DIR)):
            if not fn.endswith(".jsonl"):
                continue
            try:
                if time.mktime(time.strptime(fn[:-6], "%Y-%m-%d")) < had - 86400:
                    continue
            except Exception:
                continue
            for line in open(os.path.join(LOG_DIR, fn)):
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("sesi") in ids:
                    skrip.setdefault(r["sesi"], []).append(r)
    for k in skrip:
        skrip[k].sort(key=lambda r: r.get("t", ""))
    stat = {"sesi": len(senarai), "mesej": 0, "pelawat": 0, "lead": 0, "negara": {}, "kos": 0.0,
            "handover": 0, "soalan": 0}
    ip_set = set()
    for v in senarai:
        stat["mesej"] += v.get("bil", 0)
        if v.get("ip"):
            ip_set.add(v["ip"])
        if v.get("wa"):
            stat["lead"] += 1
        if v.get("handover"):
            stat["handover"] += 1
        n = v.get("negara") or "-"
        stat["negara"][n] = stat["negara"].get(n, 0) + 1
    stat["pelawat"] = len(ip_set)
    for rows in skrip.values():
        for r in rows:
            stat["kos"] += (r.get("kos_myr") or 0)
            stat["soalan"] += 1
    return {"hari": hari, "stat": stat, "sesi": senarai, "skrip": skrip,
            "masa": time.strftime("%Y-%m-%d %H:%M:%S")}


def halaman_analitik(hari=7, k="", uji=False):
    d = data_analitik(hari)
    s = d["stat"]
    def e(x):
        return _html.escape(str(x if x is not None else "-"))
    kad = "".join(
        f'<div class="kad"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in
        ((s["sesi"], "Sesi perbualan"), (s["soalan"], "Mesej dikirim"), (s["pelawat"], "Pelawat unik"),
         (s["lead"], "Ada nombor WA"), (f"RM{s['kos']:.3f}", "Kos AI (anggaran)")))
    negara = " · ".join(f"{e(n)} ({v})" for n, v in sorted(s["negara"].items(), key=lambda x: -x[1]))

    baris = []
    for v in d["sesi"]:
        sid = v["sesi"]
        rows = d["skrip"].get(sid, [])
        qa = "".join(
            f'<div class="q">👤 {e(r.get("soalan"))}</div><div class="a">🤖 {e(r.get("jawapan"))}</div>'
            for r in rows) or '<div class="a">(tiada transkrip lagi)</div>'
        tanda = []
        if v.get("ujian"):
            tanda.append('<span class="tag uji">UJIAN</span>')
        if v.get("handover"):
            tanda.append('<span class="tag ho">Minta manusia</span>')
        if v.get("wa"):
            tanda.append('<span class="tag lead">Ada WA</span>')
        baris.append(
            f'<tr><td>{e((v.get("mula") or "").replace("T"," "))}</td>'
            f'<td><b>{e(v.get("nama") or "(tiada nama)")}</b>{"".join(tanda)}'
            f'<br><small>{e(v.get("wa") or "")}</small></td>'
            f'<td>{e(v.get("bandar"))}, {e(v.get("negara"))}<br><small>{e(v.get("isp"))}</small></td>'
            f'<td><code>{e(v.get("ip"))}</code></td>'
            f'<td>{e((v.get("laman") or "").upper())}</td>'
            f'<td style="text-align:center">{e(v.get("bil"))}</td>'
            f'<td>{e(", ".join(v.get("kod") or []) or "-")}</td>'
            f'<td><details><summary>Lihat</summary><div class="trans">{qa}</div></details></td></tr>')

    uji_box = ""
    if uji:
        uji_box = """
  <div class="kotak">
    <b>Ujian chat di sini</b> (rekod ditanda UJIAN)
    <div style="display:flex;gap:8px;margin-top:8px;flex-wrap:wrap">
      <input id="un" placeholder="Nama anda" style="flex:1;min-width:130px;padding:9px;border:1px solid #CBD5E1;border-radius:9px">
      <input id="uq" placeholder="Soalan… cth: rumah teres bawah RM600k di Bangi" style="flex:3;min-width:220px;padding:9px;border:1px solid #CBD5E1;border-radius:9px">
      <button onclick="ujiHantar()" style="background:#0C7A4B;color:#fff;border:0;border-radius:9px;padding:9px 16px;cursor:pointer">Hantar</button>
    </div>
    <pre id="uj" style="white-space:pre-wrap;margin-top:10px;font-size:12.5px;color:#334155"></pre>
  </div>
  <script>
  async function ujiHantar(){
    var n=document.getElementById('un').value, q=document.getElementById('uq').value;
    if(!q) return;
    document.getElementById('uj').textContent='Menunggu jawapan Ali…';
    try{
      var r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json','X-Ujian':'1'},
        body:JSON.stringify({soalan:q,nama:n,laman:document.body.dataset.laman||'zmp',halaman:'analitik'})});
      var j=await r.json();
      document.getElementById('uj').textContent=j.ok?('Ali: '+j.jawapan):('Ralat: '+(j.ralat||''));
    }catch(e){document.getElementById('uj').textContent='Ralat rangkaian';}
  }
  </script>"""

    return f"""<!doctype html><html lang="ms"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Rekod Perbualan Tanya Ali</title>
<style>
 body{{margin:0;font:14px/1.5 -apple-system,'Segoe UI',Inter,system-ui,sans-serif;background:#F1F5F9;color:#0F172A}}
 header{{background:#0F172A;color:#fff;padding:16px 20px}}
 header h1{{margin:0;font-size:18px}} header small{{color:#93A9C0;font-size:12.5px}}
 .wrap{{padding:16px 20px 40px;max-width:1400px;margin:0 auto}}
 .kad{{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:12px 14px;min-width:130px;flex:1}}
 .kad b{{display:block;font-size:20px}} .kad span{{font-size:12px;color:#64748B}}
 .kads{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px}}
 .kotak{{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:14px;margin-bottom:14px}}
 table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E2E8F0;border-radius:12px;overflow:hidden}}
 th,td{{padding:9px 10px;border-bottom:1px solid #EEF2F6;text-align:left;vertical-align:top;font-size:13px}}
 th{{background:#F8FAFC;font-size:12px;color:#475569;text-transform:uppercase;letter-spacing:.03em}}
 tr:last-child td{{border-bottom:0}}
 code{{font-size:12px;background:#F1F5F9;padding:2px 5px;border-radius:5px}}
 .tag{{display:inline-block;font-size:10.5px;padding:2px 6px;border-radius:999px;margin-left:5px;vertical-align:middle}}
 .tag.uji{{background:#FEF3C7;color:#92400E}} .tag.lead{{background:#DCFCE7;color:#166534}}
 .tag.ho{{background:#FFE4E6;color:#9F1239}}
 .trans{{max-width:640px;max-height:420px;overflow:auto;background:#F8FAFC;border-radius:9px;padding:9px;margin-top:6px}}
 .q{{color:#0F172A;font-weight:600;margin-top:6px}} .a{{color:#334155;white-space:pre-wrap;margin-bottom:8px}}
 summary{{cursor:pointer;color:#0C7A4B;font-weight:600}}
</style></head><body data-laman="zmp">
<header><h1>Rekod Perbualan “Tanya Ali”</h1>
<small>Tempoh: {d['hari']} hari terakhir · dikemas kini {e(d['masa'])} (MYT) · negara: {negara or '-'}</small></header>
<div class="wrap">
 <div class="kads">{kad}</div>
 {uji_box}
 <table><thead><tr><th>Mula (MYT)</th><th>Nama / WhatsApp</th><th>Lokasi · ISP</th><th>IP</th>
 <th>Laman</th><th>Msg</th><th>Minat</th><th>Transkrip</th></tr></thead>
 <tbody>{''.join(baris) or '<tr><td colspan="8">Tiada rekod dalam tempoh ini.</td></tr>'}</tbody></table>
 <p style="color:#64748B;font-size:12px">Fail mentah: <code>{e(LOG_DIR)}/YYYY-MM-DD.jsonl</code> ·
 Senarai: {e(SESI_STORE)} · Tanpa token: 403</p>
</div></body></html>"""


# ---------------------------------------------------------------- had kadar
_hits = {}
_lock = threading.Lock()
HAD_JAM, HAD_HARI = 40, 200


def benarkan(ip):
    now = time.time()
    with _lock:
        h = [t for t in _hits.get(ip, []) if now - t < 86400]
        jam = [t for t in h if now - t < 3600]
        if len(jam) >= HAD_JAM or len(h) >= HAD_HARI:
            _hits[ip] = h
            return False
        h.append(now)
        _hits[ip] = h
        return True


class H(BaseHTTPRequestHandler):
    server_version = "AliPOC/1.0"

    def log_message(self, *a):
        pass

    def _cors(self):
        o = self.headers.get("Origin", "")
        if o in ALLOWED_ORIGINS or o.startswith("http://127.0.0.1") or o.startswith("http://localhost"):
            self.send_header("Access-Control-Allow-Origin", o)
        else:
            self.send_header("Access-Control-Allow-Origin", ALLOWED_ORIGINS[0])
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self._cors()
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/health"):
            z, m = listings()
            self._json({"ok": True, "model": MODEL, "zmp": len(z), "mt": len(m),
                        "masa": time.strftime("%Y-%m-%d %H:%M:%S")})
        elif self.path.startswith("/analitik.json"):
            return self.analitik(True)
        elif self.path.startswith("/analitik"):
            return self.analitik(False)
        elif self.path.startswith("/temujanji-kira"):
            n = sum(1 for _ in open(TEMUJANJI_LOG)) if os.path.exists(TEMUJANJI_LOG) else 0
            self._json({"ok": True, "jumlah_permohonan": n})
        elif not (PREVIEW_DIR and self.serve_preview()):
            self._json({"ok": False, "ralat": "not found"}, 404)

    def serve_preview(self):
        """Hidangkan pratonton (POC) — halang path traversal."""
        p = urllib.parse.urlparse(self.path).path or "/"
        if p.endswith("/"):
            p += "index.html"
        akar = os.path.normpath(PREVIEW_DIR)
        f = os.path.normpath(os.path.join(akar, p.lstrip("/")))
        if not (f == akar or f.startswith(akar + os.sep)) or not os.path.isfile(f):
            return False
        try:
            with open(f, "rb") as fh:
                b = fh.read()
        except Exception:
            return False
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(f)[0] or "application/octet-stream")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
        return True

    def temujanji(self):
        """Borang lawatan tapak — simpan + beritahu Zahir (Baha)."""
        ip = self.ip_pelawat()
        if not benarkan(ip):
            return self._json({"ok": False, "ralat": "Terlalu banyak permohonan. Cuba sebentar."}, 429)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            d = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return self._json({"ok": False, "ralat": "Data tidak sah."}, 400)

        nama = str(d.get("nama") or "").strip()[:80]
        wa = re.sub(r"[^\d+]", "", str(d.get("wa") or ""))[:20]
        tarikh = str(d.get("tarikh") or "").strip()[:40]
        masa = str(d.get("masa") or "").strip()[:20]
        kod = str(d.get("kod") or "").strip()[:20]
        tajuk = str(d.get("tajuk") or "").strip()[:120]
        nota = str(d.get("nota") or "").strip()[:400]
        setuju = bool(d.get("setuju"))
        if len(nama) < 2 or len(wa) < 9:
            return self._json({"ok": False, "ralat": "Sila isi nama dan nombor WhatsApp yang sah."}, 400)
        if not setuju:
            return self._json({"ok": False, "ralat": "Sila tanda persetujuan penggunaan maklumat."}, 400)

        rekod = {"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "nama": nama, "wa": wa, "tarikh": tarikh,
                 "masa": masa, "kod": kod, "tajuk": tajuk, "nota": nota,
                 "laman": d.get("laman") or "zmp",
                 "ip_hash": hashlib.sha256(ip.encode()).hexdigest()[:12]}
        try:
            with open(TEMUJANJI_LOG, "a") as f:
                f.write(json.dumps(rekod, ensure_ascii=False) + "\n")
        except Exception as e:
            return self._json({"ok": False, "ralat": f"Gagal simpan: {e}"}, 500)

        # beritahu Zahir (Baha) — tidak menggagalkan permohonan jika notifikasi gagal
        try:
            tg = os.path.expanduser("~/.hermes/scripts/tg_baha_send.py")
            if os.path.exists(tg):
                teks = ("📅 PERMOHONAN LAWATAN TAPAK (POC web)\n"
                        f"Nama: {nama}\nWhatsApp: {wa}\n"
                        f"Hartana: {kod or '-'} {('· ' + tajuk) if tajuk else ''}\n"
                        f"Cadangan: {tarikh or '-'} {masa or ''}\n"
                        f"Nota: {nota or '-'}\nLaman: {rekod['laman']}")
                subprocess.Popen(["python3", tg, teks], stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
        except Exception:
            pass
        return self._json({"ok": True,
                           "mesej": "Terima kasih! Permohonan diterima. Kami akan WhatsApp anda untuk konfirmasi tarikh.",
                           "kod": kod})

    def ip_pelawat(self):
        """IP dipercayai: Caddy (produksi) menetapkan X-Real-IP & membuang header klien.
        Laluan terowong cloudflared setempat (127.0.0.1) → guna CF-Connecting-IP."""
        xr = self.headers.get("X-Real-IP")
        if xr:
            return xr.split(",")[0].strip()
        if self.client_address[0] in ("127.0.0.1", "::1"):
            cf = self.headers.get("CF-Connecting-IP")
            if cf:
                return cf.split(",")[0].strip()
        return self.client_address[0]

    def analitik(self, json_aja=False):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if (q.get("k") or [""])[0] != analitik_token():
            return self._json({"ok": False, "ralat": "token tidak sah"}, 403)
        try:
            hari = int((q.get("hari") or ["7"])[0])
        except Exception:
            hari = 7
        if json_aja:
            return self._json(data_analitik(hari))
        uji = (q.get("uji") or [""])[0] == "1"
        b = halaman_analitik(hari, (q.get("k") or [""])[0], uji=uji).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Robots-Tag", "noindex, nofollow")
        self._cors()
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_POST(self):
        if self.path.startswith("/temujanji"):
            return self.temujanji()
        if not self.path.startswith("/chat"):
            return self._json({"ok": False, "ralat": "not found"}, 404)
        ip = self.ip_pelawat()
        if not benarkan(ip):
            return self._json({"ok": False, "ralat": "Had kadar dicapai. Cuba sebentar atau WhatsApp kami."}, 429)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            d = json.loads(self.rfile.read(n) or b"{}")
            soalan = (d.get("soalan") or "").strip()
            if not soalan:
                return self._json({"ok": False, "ralat": "Soalan kosong."}, 400)
            laman = d.get("laman") or "zmp"
            hint = d.get("listing") or None
            ua = (self.headers.get("User-Agent") or "")[:200]
            ujian = self.headers.get("X-Ujian") == "1"
            sid = sesi_id(ip, ua)
            s0 = sesi(sid)
            nama = str(d.get("nama") or "").strip()[:60] or (s0.get("nama") or "")
            bil = int(s0.get("bil") or 0) + 1
            _geo(ip)            # cari geo di latar (selari dgn panggilan model)
            ans, pilih, u, lat = tanya(soalan, d.get("sejarah"), laman, hint, nama, bil)
            ans = betulkan(ans, laman)
            wa = "60163119076" if laman == "mt" else "60122310119"
            kod = [l["tracking"] for l in pilih[:3]]
            ringkas = f"Salam, saya dari laman web ({laman.upper()}). Saya tanya Ali: \"{soalan[:120]}\""
            if kod:
                ringkas += f" — berminat dengan {', '.join(kod)}."
            from urllib.parse import quote
            out = {"ok": True, "jawapan": ans,
                   "listing": [{"kod": l["tracking"], "tajuk": l["title"], "lokasi": l.get("location", ""),
                                "harga": l.get("price_label") or "", "imej": imej(l)}
                               for l in pilih[:3]],
                   "wa": f"https://wa.me/{wa}?text={quote(ringkas)}",
                   "cta": cta_untuk(soalan, laman, kod[0] if kod else None,
                                    pilih[0]["title"] if pilih else None),
                   "kos_myr": kos(u)[0], "waktu": kos(u)[1], "latency_s": lat,
                   "model": MODEL}
            g = _geo(ip) or {}          # geo biasanya sedia selepas panggilan model
            handover = bool(re.search(r"whatsapp|hubungi pasukan|012-2310119|016-3119076", ans, re.I))
            rekod = {"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "sesi": sid, "msj": bil,
                     "nama": nama, "wa": re.sub(r"[^0-9+]", "", str(d.get("wa") or ""))[:20],
                     "ip": ip, "negara": g.get("negara", "-"), "bandar": g.get("bandar", "-"),
                     "isp": g.get("isp", ""), "asn": g.get("asn", ""),
                     "laman": laman, "halaman": str(d.get("halaman") or "")[:300], "ua": ua,
                     "soalan": soalan[:1500], "jawapan": ans[:6000], "kod": kod,
                     "handover": handover, "ujian": ujian,
                     "kos_myr": out["kos_myr"], "latency_s": lat, "model": MODEL}
            try:
                rekod_chat(rekod)
            except Exception:
                pass
            try:
                sesi_kemas(sid, {"t": rekod["t"], "mula": s0.get("mula") or rekod["t"], "bil": bil,
                                 "nama": nama, "wa": rekod["wa"], "ip": ip,
                                 "negara": rekod["negara"], "bandar": rekod["bandar"],
                                 "isp": rekod["isp"], "laman": laman, "kod": kod,
                                 "handover": handover, "ujian": ujian,
                                 "soalan_pertama": s0.get("soalan_pertama") or soalan[:200]})
            except Exception:
                pass
            try:            # keserasian: log lama (skrip sedia ada membacanya)
                with open(LOG, "a") as f:
                    f.write(json.dumps({"t": rekod["t"],
                                        "ip_hash": hashlib.sha256(ip.encode()).hexdigest()[:12],
                                        "laman": laman, "soalan": soalan[:300],
                                        "kod": kod, "usage": u, "latency": lat,
                                        "kos_myr": out["kos_myr"]}, ensure_ascii=False) + "\n")
            except Exception:
                pass
            return self._json(out)
        except urllib.error.HTTPError as e:
            return self._json({"ok": False, "ralat": f"Ralat model ({e.code})."}, 502)
        except Exception as e:
            return self._json({"ok": False, "ralat": f"Ralat: {type(e).__name__}"}, 500)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    print(f"[ali-v2] analitik: token={analitik_token()[:6]}…  log={LOG_DIR}")
    z, m = listings()
    print(f"[ali-poc] sedia · model={MODEL} · ZMP={len(z)} MT={len(m)} · port={PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
