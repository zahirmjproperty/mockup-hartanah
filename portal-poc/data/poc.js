/* POC Portal MT — data contoh berstruktur SEBENAR (nama/alamat bertopeng). Noindex. */
window.POC = {
  meta: {
    versi: "POC v1 · 12 Sep 2026",
    notis: "POC penilaian. Struktur data meniru sistem sebenar (ref MT-K-/MT-CK-/INV-). Nama & alamat ditopengkan. Production TIDAK disentuh."
  },
  penyewa: {
    nama: "Pn. Rosnah bte Ahmad", unit: "U-0002 · Lot 102B, Kg Bt 14 Kuantan",
    unit_pendek: "Lot 102B", sewa: 420, elektrik: 41.20, air: 6.80, lain: 0,
    deposit: 840, tempoh_mula: "2026-03-01", tempoh_tamat: "2027-02-28",
    baki: "Belum Bayar"
  },
  invois: [
    { id:"INV-0002", unit:"U-0002", tempoh:"2026-08", sewa:420, elektrik:41.20, air:6.80, lain:0,
      jana:"2026-09-07", due:"2026-09-17", status:"Belum Bayar", pdf:"#", billplz:"", resit:"" },
    { id:"INV-0003", unit:"U-0002", tempoh:"2026-07", sewa:420, elektrik:38.50, air:5.90, lain:0,
      jana:"2026-08-07", due:"2026-08-17", status:"Dibayar", tarikh_bayar:"2026-08-14", pdf:"#", resit:"#" },
    { id:"INV-0004", unit:"U-0002", tempoh:"2026-06", sewa:420, elektrik:44.10, air:7.20, lain:0,
      jana:"2026-07-07", due:"2026-07-17", status:"Dibayar", tarikh_bayar:"2026-07-15", pdf:"#", resit:"#" },
    { id:"INV-0005", unit:"U-0002", tempoh:"2026-05", sewa:420, elektrik:36.90, air:5.40, lain:0,
      jana:"2026-06-07", due:"2026-06-17", status:"Dibayar", tarikh_bayar:"2026-06-12", pdf:"#", resit:"#" }
  ],
  tiket_penyewa: [
    { ref:"MT-K-2026-0014", tajuk:"Paip sinki bocor + air meresap ke dinding", unit:"U-0002 · Lot 102B",
      dilapor:"2026-09-09 08:15", kategori:"Plumbing", keutamaan:"P2 — Urgent", status:"DALAM KERJA",
      kontraktor:"Sinar Aircond & Plumbing (Kontraktor B)", sla:"24 jam", sla_baki:"8 jam baki",
      timeline:[
        {t:"09/09 08:15", a:"Laporan diterima", d:"Gambar dihantar (3 keping)", s:"done"},
        {t:"09/09 09:05", a:"Triage selesai — P2 Urgent", d:"Tanggungjawab: pemilik (haus & lusuh)", s:"done"},
        {t:"09/09 11:40", a:"3 sebut harga dipanggil (RFQ)", d:"Sebut harga diterima 1 hari", s:"done"},
        {t:"10/09 10:20", a:"Pemilik lulus sebut harga", d:"RM480 + waranti 3 bulan", s:"done"},
        {t:"11/09 09:00", a:"Kerja bermula", d:"Teknikan dijadualkan hari ini 2:00 ptg", s:"now"},
        {t:"—", a:"Bukti siap + pengesahan anda", d:"Anda akan diminta sahkan bila siap", s:""}
      ] }
  ],
  dokumen: [
    { nama:"Perjanjian Sewa (TA) 2026/27 — ditandatangan & disetem", nota:"Duti setem RM2 · e-Stamping MyTax", link:"#" },
    { nama:"Inventori Serahan Masuk (01/03/2026)", nota:"24 gambar · bacaan meter: TNB 443 kWh · Air 12 m³", link:"#" },
    { nama:"Resit Deposit RM840 (2 bulan)", nota:"Diterima 28/02/2026 · dipegang pemilik", link:"#" },
    { nama:"Buku Panduan Rumah (house rules)", nota:"Semakan 03/2026", link:"#" }
  ],
  notis: [
    { tarikh:"10/09/2026", teks:"Pemotongan air SYABAS dijalankan 14/09 (9:00 pg–1:00 tgh). Sila simpan air secukupnya." },
    { tarikh:"01/09/2026", teks:"Bil sewa September (INV-0002) telah dijana — bayar sebelum 17/09 untuk elak caj lewat." }
  ],
  kontraktor: [
    { id:"MT-CK-0001", nama:"Rizal Plumbing & Renovation", kategori:"Plumbing", rating:4.6, kerja:8, kualiti:92, telefon:"013-6XX 8844" },
    { id:"MT-CK-0002", nama:"Maju Jaya Renovation", kategori:"Renovasi umum", rating:4.0, kerja:5, kualiti:80, telefon:"012-3XX 6777" },
    { id:"MT-CK-0003", nama:"Sinar Aircond & Plumbing", kategori:"Aircond & paip", rating:3.7, kerja:4, kualiti:75, telefon:"019-7XX 3110" }
  ],
  kanban: [
    { ref:"MT-K-2026-0013", unit:"Lot 101A, Kg Bt 14", kategori:"Elektrik — lampu luar", keutamaan:"P3 — Rutin",
      lajur:"Triage", pemilik:"En. Rahman", kontraktor:"—", kos:0, sla_target:72, sla_berlalu:3, dilapor:"12/09 07:40" },
    { ref:"MT-K-2026-0014", unit:"Lot 102B, Kg Bt 14", kategori:"Plumbing — paip bocor", keutamaan:"P2 — Urgent",
      lajur:"Sedang Dibaiki", pemilik:"Pn. Rosnah", kontraktor:"Sinar Aircond (B)", kos:480, sla_target:24, sla_berlalu:20, dilapor:"09/09 08:15" },
    { ref:"MT-K-2026-0012", unit:"Lot 103C, Kg Bt 14", kategori:"Renovasi dapur (waranti 12 bln)", keutamaan:"P2 — Urgent",
      lajur:"Menunggu Pengesahan", pemilik:"En. Wan", kontraktor:"Rizal Plumbing (A)", kos:14250, sla_target:120, sla_berlalu:96, dilapor:"05/09 09:10" },
    { ref:"MT-K-2026-0011", unit:"Rumah Nenek Minah", kategori:"Aircond tidak sejuk", keutamaan:"P3 — Rutin",
      lajur:"QC", pemilik:"Pn. Zubaidah", kontraktor:"Sinar Aircond (B)", kos:395, sla_target:72, sla_berlalu:70, dilapor:"08/09 14:20" },
    { ref:"MT-K-2026-0010", unit:"Lot 104D, Kg Bt 14", kategori:"Siling bocor (bumbung)", keutamaan:"P1 — Kecemasan",
      lajur:"SLA — Lewat", pemilik:"En. Kumar", kontraktor:"—", kos:0, sla_target:4, sla_berlalu:9, dilapor:"12/09 05:30" },
    { ref:"MT-K-2026-0009", unit:"Lot 105E, Kg Bt 14", kategori:"Pintu bilik air rosak", keutamaan:"P4 — Kosmetik",
      lajur:"Selesai", pemilik:"Pn. Ana", kontraktor:"Maju Jaya (C)", kos:186, sla_target:120, sla_berlalu:60, dilapor:"02/09 11:00",
      selesai:"09/09 16:40", qc:"LULUS — dinilai 4.0/5" },
    { ref:"MT-K-2026-0008", unit:"Rumah Mak Andak Salmah", kategori:"Cat semula luar", keutamaan:"P4 — Kosmetik",
      lajur:"Selesai", pemilik:"Pn. Salmah", kontraktor:"Maju Jaya (C)", kos:248, sla_target:168, sla_berlalu:150, dilapor:"28/08 08:00",
      selesai:"06/09 17:10", qc:"LULUS — dinilai 5.0/5" }
  ],
  kolum: ["Baru","Triage","Sebut Harga","Menunggu Kelulusan","Sedang Dibaiki","QC","Menunggu Pengesahan","Selesai","SLA — Lewat"],
  detail: {
    "MT-K-2026-0014": {
      unit:"Lot 102B, Kg Bt 14 Kuantan · Rumah sewa", pelapor:"Pn. Rosnah (penyewa) · 019-7XX 5021",
      pemilik:"Pn. Rosnah juga pemilik", kategori:"Plumbing · Paip sinki bocor + air meresap ke dinding",
      keutamaan:"P2 — Urgent (SLA 24 jam)", tanggungjawab:"Pemilik (haus & lusuh)",
      nilai:"RM480 (diluluskan pemilik)", siap:"15/09/2026",
      sebutharga:[
        {k:"Rizal Plumbing & Renovation", a:520, t:"2 hari", w:"3 bulan", st:"Ditolak"},
        {k:"Sinar Aircond & Plumbing", a:480, t:"2 hari", w:"6 bulan", st:"DIPILIH", pilih:true},
        {k:"Maju Jaya Renovation", a:545, t:"3 hari", w:"3 bulan", st:"Ditolak"}
      ],
      wo:{ no:"MT-WO-2026-0007", mula:"11/09/2026", siap_sasaran:"15/09/2026", status:"DALAM KERJA" },
      bayaran:[
        {tahap:"Deposit / mula 30%", amaun:144, status:"DIBAYAR", tarikh:"11/09"},
        {tahap:"Kemajuan selesai 40%", amaun:192, status:"MENUNGGU", tarikh:"selepas QC MT"},
        {tahap:"Siap sepenuhnya 30%", amaun:144, status:"BELUM", tarikh:"selepas terimaan pemilik"}
      ]
    }
  }
};
