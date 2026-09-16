#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uji_konsistensi.py — pagar konsistensi Zentra Hub (Fasa 0, diperluas).

Memeriksa:
  A. levels.js: tangga level, jumlah (comm+bonus=total), siling override, GL berasingan,
     versi kadar, peraturan keras — serta invarian total + siling leader <= 100%.
  B. Setiap halaman HTML: label level/tier/peratus padan levels.js, jawatan pada peratus betul,
     contoh pengiraan berjumlah 100% dan jumlah RM tepat, tiada frasa terlarang
     ("one account code" / "referrer chain the override engine"), nota wajib hadir.
  C. Enjin komisen (assets/agency.js): had 40%, dan nota rekonsiliasi sen.
Gagal (exit 1) jika ada percanggahan.
"""
import os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
masalah, lulus = [], 0


def baca(f):
    return open(os.path.join(D, f), encoding="utf-8").read()


def semak(ok, butir):
    global lulus
    if ok:
        lulus += 1
    else:
        masalah.append(butir)


# ---------------------------------------------------------------- A. levels.js
lv = baca("assets/levels.js")
LAD = {}
for m in re.finditer(r"\{id:'(L\d)', tier:'([^']+)',\s*comm:(\d+), bonus:(\d+), total:(\d+), ovrCap:(\d+)", lv):
    LAD[m.group(1)] = {"tier": m.group(2), "comm": int(m.group(3)), "bonus": int(m.group(4)),
                       "total": int(m.group(5)), "cap": int(m.group(6))}
semak(len(LAD) == 6, "levels.js: jangka 6 level, jumpa %d" % len(LAD))

for lid, r in sorted(LAD.items()):
    semak(r["comm"] == 40, "%s: declared commission mesti 40%% (jumpa %d%%)" % (lid, r["comm"]))
    semak(r["comm"] + r["bonus"] == r["total"],
          "%s: comm %d + bonus %d != total %d" % (lid, r["comm"], r["bonus"], r["total"]))
    semak(r["cap"] in (0, 10, 15), "%s: siling override luar jangka (%d%%)" % (lid, r["cap"]))

kunci = sorted(LAD)
for i, lid in enumerate(kunci[:-1]):
    naik = LAD[kunci[i + 1]]["cap"]           # siling override level di atas
    semak(LAD[lid]["total"] + naik <= 100,
          "%s: total %d%% + siling leader %d%% melebihi 100%%" % (lid, LAD[lid]["total"], naik))

semak(re.search(r"window\.ZTH_GL\s*=", lv) is not None, "levels.js: ZTH_GL (kod akaun) tiada")
gl = dict(re.findall(r"(\w+):'(602-\d+)'", lv))
semak(len(set(gl.values())) == len(gl) and len(gl) >= 4,
      "levels.js: kod GL tidak berasingan/unik: %r" % gl)
semak(re.search(r"window\.ZTH_RATE_VERSION\s*=", lv) is not None, "levels.js: versi kadar tiada")
semak(re.search(r"window\.ZTH_RULES\s*=", lv) is not None, "levels.js: peraturan keras tiada")

# ---------------------------------------------------------------- B. halaman
JADUAL_JAWATAN = {"Team Leader": 85, "Group Leader": 90, "Senior negotiator": 75}
TERLARANG = [
    (r"one account code", "frasa terlarang: 'one account code' (kod GL mesti berasingan)"),
    (r"same account code", "frasa terlarang: 'same account code' (kod GL mesti berasingan)"),
    (r"referrer chain the (override|reward) engine", "frasa terlarang: rantai referrer untuk enjin override"),
    (r"Referral chain \(upline", "frasa terlarang: 'Referral chain (upline...' — guna 'Management upline'"),
    (r"RM152\.79", "angka tidak konsisten: RM152.79 (mesti RM152.78 supaya berjumlah tepat)"),
]
WAJIB = {
    "hierarchy.html": "Rate versioning",
    "team.html": "Referrer ≠ leader",
    "tree.html": "Referral record",
    "payouts.html": "clawback ledger",
    "commission.html": "roundNote",
    "claims.html": "602-150",
    "index.html": "Reconciles to the professional fee",
}

fail = sorted(f for f in os.listdir(D) if f.endswith(".html"))
for f in fail:
    s = baca(f)
    # struktur asas
    semak(s.count("<script") == s.count("</script>"),
          "%s: tag <script> tidak seimbang" % f)
    # 1) label level "L# · ..." padan levels.js (abaikan senarai level seperti 'L1 · L2')
    for m in re.finditer(r"(L\d) · ([^·<'\"]{2,30}?)(?: · (\d+)%)?(?=['\"<]|$)", s):
        lid, tier, pct = m.group(1), m.group(2).strip().rstrip(")"), m.group(3)
        if lid not in LAD:
            masalah.append("%s: kod level tidak dikenali: %s" % (f, m.group(0))); continue
        if re.fullmatch(r"L\d", tier):          # senarai level (L1 · L2 ...) — bukan rujukan tier
            lulus += 1; continue
        if tier.rstrip("%").isdigit():
            semak(int(tier.rstrip("%")) == LAD[lid]["total"],
                  "%s: %s peratus %s%% != %d%%" % (f, lid, tier, LAD[lid]["total"])); continue
        semak(tier == LAD[lid]["tier"] or tier == LAD[lid]["tier"] + " cap 10%",
              "%s: %s tier '%s' != '%s'" % (f, lid, tier, LAD[lid]["tier"]))
        if pct:
            semak(int(pct) == LAD[lid]["total"],
                  "%s: %s peratus %s%% != %d%%" % (f, lid, pct, LAD[lid]["total"]))
    # 2) jawatan pada peratus betul
    for m in re.finditer(r"(Team Leader|Group Leader|Senior negotiator)[^<]{0,40}?(\d{2})%", s):
        jt, pct = m.group(1), int(m.group(2))
        if pct != JADUAL_JAWATAN[jt]:
            masalah.append("%s: %s · %d%% (jangka %d%%)" % (f, jt, pct, JADUAL_JAWATAN[jt]))
    # 3) frasa terlarang
    for pat, msg in TERLARANG:
        if re.search(pat, s):
            masalah.append("%s: %s" % (f, msg))
    # 4) nota wajib
    if f in WAJIB:
        semak(WAJIB[f] in s, "%s: nota wajib hilang ('%s')" % (f, WAJIB[f]))
    # 5) contoh pengiraan mesti berjumlah 100%
    if "Worked example" in s:
        bahagian = s.split("Worked example", 1)[1].split("</table>", 1)[0]
        baris_contoh = [b for b in re.findall(r"<tr[^>]*>(.*?)</tr>", bahagian, re.S) if "Total" not in b and "Reconciles" not in b]
        pcts = [int(x) for b in baris_contoh for x in re.findall(r'class="num">(?:<b>)?(\d+)%', b)]
        rms = [float(x.replace(",", "")) for x in re.findall(r'class="num">(?:<b>)?([\d,]+)</td>', bahagian)]
        semak(sum(pcts) == 100 if pcts else False,
              "%s: contoh pengiraan tidak berjumlah 100%% (%s)" % (f, pcts or "tiada peratus"))
    # 6) RK (rekonsiliasi) — jumlah dalam contoh RM10,000 mesti padan baris akhir
    if "Worked example" in s:
        bahagian = s.split("Worked example", 1)[1].split("</table>", 1)[0]
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", bahagian, re.S)
        jum = 0.0
        for r_ in rows:
            sel = re.findall(r">([\d,]+\.?\d*)<", r_)
            if len(sel) >= 2 and re.search(r"\d+%", r_) and "Total" not in r_:
                try:
                    jum += float(sel[-1].replace(",", ""))
                except ValueError:
                    pass
        semak(abs(jum - 10000) < 0.01 or jum == 0, "%s: contoh RM berjumlah %s (jangka 10000)" % (f, jum))

# ---------------------------------------------------------------- khusus index.html
ix = baca("index.html")
fee = float(re.search(r"professional fee <b>RM([\d,\.]+)</b>", ix).group(1).replace(",", ""))
legend = ix.split('class="legend"', 1)[1].split("</div>", 1)[0]
amts = [float(x.replace(",", "")) for x in re.findall(r"RM([\d,]+\.\d{2})", legend)]
semak(len(amts) == 3, "index.html: jangka 3 angka dalam legend, jumpa %d" % len(amts))
semak(abs(sum(amts) - fee) < 0.005,
      "index.html: split %s berjumlah %.2f != fee %.2f" % (amts, sum(amts), fee))

# ---------------------------------------------------------------- C. enjin
js = baca("assets/agency.js")
semak("CAP_COMMISSION = 40" in js, "agency.js: had komisen 40% tiada")
semak("roundNote" in js, "agency.js: nota rekonsiliasi sen (roundNote) tiada")
semak("Math.min(o.commPct, CAP_COMMISSION)" in js, "agency.js: enjin tidak mengunci komisen pada 40%")

# ---------------------------------------------------------------- hasil
print("levels.js : %s" % ", ".join("%s=%d%% (cap %d%%)" % (k, v["total"], v["cap"]) for k, v in sorted(LAD.items())))
print("kod GL    : %s" % ", ".join("%s=%s" % (k, v) for k, v in sorted(gl.items())))
print("halaman   : %d diperiksa" % len(fail))
print("pemeriksaan lulus: %d" % lulus)
if masalah:
    print("\n❌ %d percanggahan:" % len(masalah))
    for x in masalah:
        print("  - %s" % x)
    sys.exit(1)
print("\n✅ LULUS — semua halaman, levels.js dan enjin komisen konsisten.")
