# POC Portal MT — Sistem Pengurusan Hartanah (Pratonton)

**Tarikh:** 12 Sep 2026 · **Oleh:** Ali (Hermes) · **Untuk:** Zahir MJ (Mr Tanah)
**Kajian sokongan:** `~/zmp-docs/kajian/kajian-pelan-upgrade-sistem-pengurusan-hartanah-2026-09-12.md`
**Repositori:** `zahirmjproperty/mockup-hartanah` → folder `portal-poc/` (**repo pratonton**; production `mrtanah-site`/`mrtanah` **TIDAK disentuh**)

---

## 1. Apa ini

POC (proof of concept) boleh klik untuk **3 jurang sebenar** sistem MT — dipilih Zahir 12/9/2026:

| # | Halaman | Apa yang diuji |
|---|---|---|
| 1 | `penyewa.html` | **Portal Penyewa** — baki sewa, tarikh akhir, resit, status aduan masa nyata, kontrak &amp; inventori, papan notis |
| 2 | `kanban.html` | **Papan Kanban + SLA** — 9 lajur kerja, warna SLA (hijau/kuning/merah), sebut harga, work order, jadual bayaran 30/40/30, tapisan |
| 3 | `bayar.html` | **Bayar Sewa** — ringkasan invois, DuitNow QR / FPX / pindahan, rujukan `BS-####`, simulasi resit |
| 4 | `ladang.html` | **Rangka** modul ladang (Fasa 2) — lejar tuaian per blok, tan/ha, harga rujukan BTS MPOB, kos, lesen e-LesenPK |

Plus `index.html` — hub POC (peta: apa BAHARU vs apa yang sudah LIVE).

## 2. Apa yang TIDAK dibina semula (kerana sudah live)

Sistem kerosakan MT sudah **hidup** (`ZMPKerja.gs v18`): halaman `aduan-pemilik.html` (timeline + bukti + kelulusan sebut harga), `aduan-kontraktor.html` (tugasan bertoken + rating), `aduan-mt.html` (papan dalaman), `aduan-ejen.html` (peranan ejen). POC ini **menambah paparan**, bukan menggantikan.

## 3. Data

- Struktur data meniru sistem sebenar: `MT-K-2026-####` (tiket), `MT-CK-####` (kontraktor), `INV-2026-08-####` (invois), sewa **RM420/bulan**, tempoh **2026-08**, due **17/09**, deposit 2 bulan, passthrough TNB/Air.
- **Nama &amp; alamat peribadi ditopengkan**, kes penilaian menggunakan set demo yang sama seperti pratonton `aduan2` (diluluskan Zahir 11/9).
- Semua halaman `noindex` + repo pratonton ada `robots.txt Disallow: /`.

## 4. Apa yang SIMULASI (tidak sebenar)

- QR bayaran = **QR contoh** (bukan akaun sebenar) — sengaja.
- Butang bayaran/FPX/resit = simulasi (tiada transaksi).
- Billplz untuk **invois sewa** masih belum diaktifkan (koleksi PROD sedia ada = invois perkhidmatan ZMJ `BAYARZMJ`).
- Harga BTS MPOB &amp; angka blok ladang = contoh.

## 5. Ujian untuk Zahir / Fadilah / kontraktor

1. **Portal Penyewa** — tekan "Bayar Sekarang" → pilih kaedah → "Simulasi pembayaran berjaya" → lihat resit. Kemudian lihat tiket `MT-K-2026-0014` (paip bocor): patut nampak timeline 6 langkah + status "DALAM KERJA".
2. **Kanban** — tekan tapisan "SLA — Lewat" (patut tinggal kes P1 siling bocor). Klik kad `MT-K-2026-0014` → patut nampak perbandingan 3 sebut harga + WO + jadual bayaran 30/40/30.
3. **Bayar** — semak rujukan `BS-2026-08-0002` jelas dan sebab ia penting (padanan automatik).
4. **Ladang** — sahkan bentuk lejar (blok/tan/ha/harga MPOB/kos/lesen) sebelum dibina pada Fasa 2.
5. **Maklum balas** — apa perlu ditambah/dibuang sebelum sambung ke sistem sebenar?

## 6. Cara jalankan (tempatan)

```bash
cd ~/mockup-hartanah && python3 -m http.server 8099
# buka http://localhost:8099/portal-poc/index.html
```

## 7. Fail

```
portal-poc/
  index.html         hub POC
  penyewa.html       portal penyewa
  kanban.html        papan kanban + SLA (+ modal butiran)
  bayar.html         bayar sewa
  ladang.html        rangka modul ladang
  poc.css            gaya kongsi (navy #0F172A + hijau #0C7A4B)
  data/poc.js        data contoh berstruktur
  data/qr-contoh.svg QR contoh (bukan QR sebenar)
  _read_nyata.py     pembaca data sebenar (Sheets) → data/nyata.json (tidak dihantar ke web)
```

## 8. Langkah selepas LULUS

1. Sambung `penyewa.html` ke webhook sebenar: token per unit → baca tab `Invois` + `Tickets` (Apps Script) → guna semula siri emel/WA sedia ada.
2. Kanban: paparan atas tab `Tickets/Sebutharga/Work Order/Jadual Bayaran` + medan SLA baru (2 lajur) + status kerja konsisten.
3. Bayar Sewa: keputusan Zahir — aktifkan Billplz untuk sewa **atau** kekal DuitNow QR + pengesahan manual; jana rujukan `BS-####` dalam tab `Invois`.
4. Fasa 2: lejar ladang (tab baru) + suapan harga MPOB BEPI + OCR resit → auto-lejer kos.
