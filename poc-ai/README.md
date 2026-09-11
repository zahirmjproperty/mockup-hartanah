# POC "Tanya Ali" — AI Assistant laman web (preview)

**Tujuan:** buktikan konsep AI assistant yang menjawab **hanya** berdasarkan data listing sebenar,
dengan penyerahan (handover) kepada WhatsApp. **BUKAN production** — repo mock-up sahaja.

---

## Seni bina

```
GitHub Pages (mock-up, statik)
  assets/ali-chat.js  ──POST JSON──▶  Cloudflare quick tunnel
                                        │
                                  poc-ai/server.py  (kunci API di sini sahaja)
                                    1. parse_q()      → kekangan (negeri/jenis/harga/ekar/hakmilik)
                                    2. konteks()      → tapis listing ("retrieval-lite", ~12 listing)
                                    3. _panggil()     → DeepSeek V4.1-Flash (temperature 0)
                                    4. betulkan()     → nombor WhatsApp/jenama ikut laman
                                    5. log.jsonl      → audit (soalan, kod, token, kos)
                                        │
                                  jawapan + kad listing + pautan WhatsApp
```

## Fail

| Fail | Fungsi |
|---|---|
| `server.py` | Pelayan AI (stdlib sahaja). Baca data dari `zahir-web/data/listings.js` + `mrtanah-site/data/listings.js` |
| `start_poc.sh` | Mula pelayan + terowong, kunci URL ke `assets/ali-chat.js` |
| `jaga_poc.sh` | Watchdog: pastikan hidup; jika URL berubah → kemas kini + push (cron `01de9cc6fe02`, tiap 20 min) |
| `tangkap_skrin.py` | Tangkap skrin headless (guna venv hermes: `websocket-client`) |
| `log.jsonl` | Log audit pertanyaan + kos (30 hari) |
| `../assets/ali-chat.js` | Widget chat (butang + panel + kad listing + handover) |

## Guardrail (dikuatkuasa dalam prompt sistem)

1. Jawab **hanya** dari data listing + FAQ yang diberikan. Tiada angka rekaan.
2. Jika tiada dalam data → mengaku "tak pasti" + tawar WhatsApp (**jangan teka**).
3. Larang: nama pemilik, kos, komisen, nasihat undang-undang/cukai, mengaku manusia.
4. Ansuran **dikira pelayan** (`ansuran()`), bukan oleh model — elak salah kira.
5. Nombor WhatsApp & jenama dibetulkan secara deterministik ikut laman (MT: 016-3119076 · ZMP: 012-2310119).
6. Had kadar: 40/jam & 200/hari setiap IP; had sesi widget 20 mesej.
7. Log: soalan + kod listing + token + kos. **Tiada data peribadi** dihantar ke LLM.

## Jalankan semula (jika terowong mati)

```bash
bash ~/mockup-hartanah/poc-ai/start_poc.sh      # dapat URL baharu + kemas kini widget
cd ~/mockup-hartanah && git add -A && git commit -m "POC: URL baharu" && git push
```
Atau tunggu cron watchdog (≤20 minit) — ia berbuat sendiri.

## Kos (ukuran sebenar)

- Purata **RM0.00091 per pertanyaan** (off-peak, DeepSeek V4.1-Flash, konteks ~1.6k token, cache hit).
- 3,000 pertanyaan/bulan ≈ **RM2.7** + hosting RM0 (cloudflared percuma / Cloudflare Workers 100k req/hari).
- 33 pertanyaan ujian = RM0.03.

## Quirk yang diketahui

- **V4.1-Flash ialah model reasoning**; `thinking: {type: disabled}` mematikan proses berfikir
  (jimat token). Sesekali jawapan terpotong → `_terpotong()` mengesan dan cuba semula dengan
  thinking aktif. Perlu dipantau jika model ditukar.
- Terowong `trycloudflare.com` **sementara** (URL berubah bila mula semula) — untuk produksi guna
  Cloudflare Worker bernama atau letak endpoint pada domain sendiri.

## Fasa seterusnya (bila Zahir lulus)

1. Pindahkan endpoint ke Cloudflare Worker (URL tetap, RM0) + had kadar KV.
2. Pasang widget pada laman sebenar (selepas Fasa 1 reka bentuk diterbitkan) + GA4 event `ali_chat`.
3. Kuiz padanan hartanah & gate "Minta Pelan & Geran" (lihat `cadangan-ai-portal-2026-09-12.md`).
4. Notis privasi dikemas kini (pemprosesan AI + pemindahan rentas sempadan) — PDPA.
