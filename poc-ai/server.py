#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
POC "Tanya Ali" — backend AI assistant untuk web Zahir MJ Property & Mr Tanah.
Preview/POC sahaja: kunci API kekal di pelayan (TIDAK pernah dihantar ke pelayar).
Jalankan: python3 server.py   (lalai 127.0.0.1:8795)

Guardrail: AI hanya menjawab berdasarkan data listing sebenar (data/listings.js)
+ FAQ terkawal. Tiada angka rekaan. Tiada data peribadi pelanggan dihantar ke LLM.
"""
import json, os, re, time, hashlib, threading, urllib.request, urllib.error
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HOME = os.path.expanduser("~")
ZMP_JS = "/home/ubuntu/zahir-web/data/listings.js"
MT_JS = "/home/ubuntu/mrtanah-site/data/listings.js"
IMG_DIR = "/home/ubuntu/mockup-hartanah/img"
LOG = "/home/ubuntu/mockup-hartanah/poc-ai/log.jsonl"
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
                   "https://zahirmjproperty.com", "http://127.0.0.1:8099", "http://localhost:8099")

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
Sebut anggaran ansuran hanya jika ditanya atau jika harga disebut (kadar 4.00% p.a., 35 tahun,
90% pembiayaan) dan nyatakan ia anggaran.
"""

FAQ = """INFO TETAP:
- WhatsApp: Zahir MJ Property 012-2310119 (laman ZMP) · Mr Tanah 016-3119076 (laman MT).
  Sebut nombor MENGIKUT laman pelawat sahaja (MT → 016-3119076; ZMP → 012-2310119).
- Semua hartanah melalui semakan status pemilikan. Pelan & geran penuh diberi kepada pembeli serius.
- Ejen berdaftar: PEA 2684. Pejabat: DNA Workspace, Seksyen 9, Bandar Baru Bangi.
- Ada kalkulator pinjaman dan semak kelayakan (DSR) di laman Zahir MJ Property.
- Lawatan tapak boleh diatur (borang temujanji / WhatsApp).
"""


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


def tanya(soalan, sejarah, laman, listing_hint=None):
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
    msgs = [{"role": "system", "content": SISTEM + "\n" + FAQ +
             "\nDATA LISTING (sumber tunggal kebenaran):\n" + ctx +
             ("\nKekangan yang dikesan daripada soalan: " + "; ".join(kekangan) if kekangan else "") +
             ("\nKonteks halaman: pelawat sedang melihat " + listing_hint if listing_hint else
              "\nKonteks halaman: laman " + ("Mr Tanah (tanah/pertanian/lot banglo)" if laman == "mt"
                                             else "Zahir MJ Property (rumah/komersial)"))}]
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


def imej(tracking):
    p = os.path.join(IMG_DIR, tracking.lower() + "-card.webp")
    return f"img/{tracking.lower()}-card.webp" if os.path.exists(p) else None


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
        else:
            self._json({"ok": False, "ralat": "not found"}, 404)

    def do_POST(self):
        if not self.path.startswith("/chat"):
            return self._json({"ok": False, "ralat": "not found"}, 404)
        ip = self.headers.get("CF-Connecting-IP") or self.headers.get("X-Forwarded-For") or self.client_address[0]
        ip = ip.split(",")[0].strip()
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
            ans, pilih, u, lat = tanya(soalan, d.get("sejarah"), laman, hint)
            wa = "60163119076" if laman == "mt" else "60122310119"
            kod = [l["tracking"] for l in pilih[:3]]
            ringkas = f"Salam, saya dari laman web ({laman.upper()}). Saya tanya Ali: \"{soalan[:120]}\""
            if kod:
                ringkas += f" — berminat dengan {', '.join(kod)}."
            from urllib.parse import quote
            out = {"ok": True, "jawapan": ans,
                   "listing": [{"kod": l["tracking"], "tajuk": l["title"], "lokasi": l.get("location", ""),
                                "harga": l.get("price_label") or "", "imej": imej(l["tracking"])}
                               for l in pilih[:3]],
                   "wa": f"https://wa.me/{wa}?text={quote(ringkas)}",
                   "kos_myr": kos(u)[0], "waktu": kos(u)[1], "latency_s": lat,
                   "model": MODEL}
            try:
                with open(LOG, "a") as f:
                    f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"),
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
    z, m = listings()
    print(f"[ali-poc] sedia · model={MODEL} · ZMP={len(z)} MT={len(m)} · port={PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
