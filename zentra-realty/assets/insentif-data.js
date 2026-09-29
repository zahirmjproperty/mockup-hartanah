/* ============================================================================
   assets/insentif-data.js — SSOT (satu sumber kebenaran) untuk modul insentif,
   kempen sasaran dan pengiktirafan ZENTRA Realty.
   Digunakan oleh: insentif.html · agents.html (badge) · my.html · f3.html
   Data: SAMPEL/SINTETIK sahaja (mock-up). Angka direka untuk demonstrasi corak.
   Corak: kempen berasaskan SASARAN WANG + KIRAAN + SYARAT, sama seperti
   kempen insentif IQI (Incentive Trip, Dream Car, Home Bonus, World Club).
   ========================================================================== */
window.INS = (function () {

  /* ---------------- 1. Kempen aktif ---------------- */
  /* jenis: 'wang'  = sasaran nilai jualan (RM) yang mesti dicapai
     jenis: 'kiraan' = sasaran bilangan unit/tempahan
     jenis: 'pematuhan' = syarat tanpa angka (cth. hadir latihan)              */
  const KEMPEN = [
    {
      id: 'KMP-2026-01', nama: 'Convention Trip 2027 — Kuala Lumpur', jenis: 'wang',
      sasaran: 6000000, tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Pakej trip 2 orang + penginapan 3 malam',
      jenis_jualan: 'semua', nota: 'Jualan projek + subsale + sewa semuanya dikira.',
      warna: 'gold'
    },
    {
      id: 'KMP-2026-02', nama: 'Convention Trip 2027 — Wilayah Lain', jenis: 'wang',
      sasaran: 6000000, tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Pakej trip 2 orang (wilayah pilihan)',
      jenis_jualan: 'semua', nota: 'Sasaran sama seperti KL; peserta memilih satu wilayah.',
      warna: 'gold'
    },
    {
      id: 'KMP-2026-03', nama: 'Dream Car 2026', jenis: 'wang',
      sasaran: 6000000, tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Elak bayaran pendahuluan kereta terpilih',
      jenis_jualan: 'projek', nota: 'Hanya jualan projek pembangunan baharu dikira.',
      warna: 'blue'
    },
    {
      id: 'KMP-2026-04', nama: 'Home Bonus 2026 (Peribadi)', jenis: 'wang',
      sasaran: 12000000, tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Bonus tunai berperingkat',
      jenis_jualan: 'semua', nota: 'Sasaran tertinggi; dikira atas nama peribadi sahaja.',
      warna: 'green'
    },
    {
      id: 'KMP-2026-05', nama: 'World Club 2026 (Peribadi)', jenis: 'wang',
      sasaran: 12000000, tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Keahlian kelab antarabangsa',
      jenis_jualan: 'semua', nota: 'Jemputan ke majlis antarabangsa + pengiktirafan.',
      warna: 'violet'
    },
    {
      id: 'KMP-2026-06', nama: 'Projek Baru Champion', jenis: 'kiraan',
      sasaran: 10, unit: 'unit', tempoh: '1 Jan – 31 Dis 2026', hadiah: 'Bonus RM 5,000 + plak',
      jenis_jualan: 'projek', nota: 'Kiraan unit yang Berjaya Ditukar (converted), bukan tempahan.',
      warna: 'amber'
    }
  ];

  /* ---------------- 2. Syarat pematuhan (mesti lulus semua) ---------------- */
  const SYARAT = [
    { id: 'S1', nama: 'Lesen REN/REA sah sepanjang tempoh', wajib: true },
    { id: 'S2', nama: 'Tiada kes tatatertib terbuka', wajib: true },
    { id: 'S3', nama: 'Latihan pematuhan AMLA diselesaikan', wajib: true },
    { id: 'S4', nama: 'Minimum 6 bulan perkhidmatan aktif', wajib: false }
  ];

  /* ---------------- 3. Kemajuan peserta (angka SAMPEL) ---------------- */
  /* Nama ejen diselaraskan dengan nama yang sudah digunakan dalam mock-up
     (agency.js / realty-listings.js) supaya kad pengiktirafan tidak
     menunjukkan dua identiti berbeza bagi orang yang sama. */
  const EJEN = {
    'ZR-001': 'Zahiruddin M.J.',
    'ZR-002': 'Fadilah Yusof',
    'ZR-003': 'Hafiz Rahman',
    'ZR-004': 'Nurul Izzah binti Kamal',
    'ZR-005': 'New agent seat',
    'ZR-006': 'Aina Zulkifli'
  };
  function namaEjen(id) { return EJEN[id] || id; }
  /* agent_id merujuk kepada rekod dalam assets/agency.js (satu sumber ejen). */
  const KEMAJUAN = [
    { kempen: 'KMP-2026-01', agent: 'ZR-001', nilai: 4780000, kiraan: 0 },
    { kempen: 'KMP-2026-02', agent: 'ZR-001', nilai: 4780000, kiraan: 0 },
    { kempen: 'KMP-2026-03', agent: 'ZR-001', nilai: 3120000, kiraan: 0 },
    { kempen: 'KMP-2026-04', agent: 'ZR-001', nilai: 4780000, kiraan: 0 },
    { kempen: 'KMP-2026-05', agent: 'ZR-001', nilai: 4780000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-001', nilai: 0, kiraan: 7 },

    { kempen: 'KMP-2026-01', agent: 'ZR-002', nilai: 6210000, kiraan: 0 },
    { kempen: 'KMP-2026-03', agent: 'ZR-002', nilai: 4880000, kiraan: 0 },
    { kempen: 'KMP-2026-04', agent: 'ZR-002', nilai: 6210000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-002', nilai: 0, kiraan: 12 },

    { kempen: 'KMP-2026-01', agent: 'ZR-003', nilai: 1980000, kiraan: 0 },
    { kempen: 'KMP-2026-02', agent: 'ZR-003', nilai: 1980000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-003', nilai: 0, kiraan: 3 },

    { kempen: 'KMP-2026-01', agent: 'ZR-004', nilai: 7450000, kiraan: 0 },
    { kempen: 'KMP-2026-02', agent: 'ZR-004', nilai: 7450000, kiraan: 0 },
    { kempen: 'KMP-2026-03', agent: 'ZR-004', nilai: 7450000, kiraan: 0 },
    { kempen: 'KMP-2026-04', agent: 'ZR-004', nilai: 7450000, kiraan: 0 },
    { kempen: 'KMP-2026-05', agent: 'ZR-004', nilai: 7450000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-004', nilai: 0, kiraan: 15 },

    { kempen: 'KMP-2026-01', agent: 'ZR-005', nilai: 890000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-005', nilai: 0, kiraan: 1 },

    { kempen: 'KMP-2026-01', agent: 'ZR-006', nilai: 3350000, kiraan: 0 },
    { kempen: 'KMP-2026-02', agent: 'ZR-006', nilai: 3350000, kiraan: 0 },
    { kempen: 'KMP-2026-03', agent: 'ZR-006', nilai: 2200000, kiraan: 0 },
    { kempen: 'KMP-2026-06', agent: 'ZR-006', nilai: 0, kiraan: 6 }
  ];

  /* ---------------- 4. Pematuhan setiap peserta ---------------- */
  const PATUH = [
    { agent: 'ZR-001', lulus: ['S1', 'S2', 'S3', 'S4'], gagal: [] },
    { agent: 'ZR-002', lulus: ['S1', 'S2', 'S3'], gagal: ['S4'] },
    { agent: 'ZR-003', lulus: ['S1', 'S3'], gagal: ['S2'] },
    { agent: 'ZR-004', lulus: ['S1', 'S2', 'S3', 'S4'], gagal: [] },
    { agent: 'ZR-005', lulus: ['S1', 'S4'], gagal: ['S2', 'S3'] },
    { agent: 'ZR-006', lulus: ['S1', 'S2', 'S3', 'S4'], gagal: [] }
  ];

  /* ---------------- 5. Papan pengiktirafan ---------------- */
  const PENGIKTIRaan = [
    { gelaran: 'Top Project Closer — September', agent: 'ZR-004', nilai: '15 unit ditukar', nota: 'Mendahului dengan margin jelas' },
    { gelaran: 'Highest Subsale Value — Q3', agent: 'ZR-002', nilai: 'RM 6.21 juta', nota: 'Konsisten 3 bulan berturut' },
    { gelaran: 'Rising Agent — September', agent: 'ZR-006', nilai: '+128% vs Ogos', nota: 'Peningkatan terpantas' },
    { gelaran: 'Compliance Star — Q3', agent: 'ZR-001', nilai: '4/4 syarat lulus', nota: 'Tiada pengecualian sepanjang suku' }
  ];

  /* ---------------- 6. Pengiraan ---------------- */
  function kempunyai(id) { return KEMPEN.find(function (k) { return k.id === id; }); }
  function peserta(agent) { return KEMAJUAN.filter(function (p) { return p.agent === agent; }); }
  function patuhAgent(agent) {
    var p = PATUH.find(function (x) { return x.agent === agent; });
    return p || { agent: agent, lulus: [], gagal: SYARAT.map(function (s) { return s.id; }) };
  }
  /* Kemajuan satu peserta dalam satu kempen: 0-100 + status */
  function maju(agent, id) {
    var k = kempunyai(id);
    var p = KEMAJUAN.find(function (x) { return x.agent === agent && x.kempen === id; });
    if (!k) return null;
    var kini = k.jenis === 'kiraan' ? (p ? p.kiraan : 0) : (p ? p.nilai : 0);
    var pct = k.sasaran > 0 ? Math.min(100, Math.round(kini / k.sasaran * 1000) / 10) : 0;
    var pa = patuhAgent(agent);
    var gagalWajib = pa.gagal.filter(function (g) {
      var s = SYARAT.find(function (x) { return x.id === g; });
      return s && s.wajib;
    });
    var status = pct >= 100 ? (gagalWajib.length ? 'tertahan' : 'layak')
      : pct >= 60 ? 'hampir' : 'jauh';
    return { kempunyai: k, kini: kini, pct: pct, status: status, gagal: pa.gagal };
  }
  /* Kemajuan semua peserta dalam satu kempen, disusun menurun */
  function papanKempen(id) {
    var ids = [];
    KEMAJUAN.forEach(function (p) { if (p.kempen === id && ids.indexOf(p.agent) < 0) ids.push(p.agent); });
    return ids.map(function (a) {
      var m = maju(a, id);
      return { agent: a, kini: m.kini, pct: m.pct, status: m.status, gagal: m.gagal };
    }).sort(function (x, y) { return y.pct - x.pct; });
  }
  function ringkas() {
    var layak = 0, hampir = 0, tertahan = 0, jauh = 0;
    var agent = [];
    KEMAJUAN.forEach(function (p) { if (agent.indexOf(p.agent) < 0) agent.push(p.agent); });
    agent.forEach(function (a) {
      var m = maju(a, 'KMP-2026-01');
      if (m.status === 'layak') layak++;
      else if (m.status === 'tertahan') tertahan++;
      else if (m.status === 'hampir') hampir++;
      else jauh++;
    });
    return { kempen: KEMPEN.length, peserta: agent.length, layak: layak, hampir: hampir, tertahan: tertahan, jauh: jauh };
  }

  function rupiah(n) {
    return 'RM ' + Number(n).toLocaleString('en-MY');
  }
  function juta(n) {
    return 'RM ' + (n / 1000000).toFixed(2) + ' juta';
  }

  return {
    KEMPEN: KEMPEN, SYARAT: SYARAT, KEMAJUAN: KEMAJUAN, PATUH: PATUH,
    PENGIKTIRAN: PENGIKTIRaan, EJEN: EJEN,
    namaEjen: namaEjen,
    kempunyai: kempunyai, peserta: peserta, patuhAgent: patuhAgent,
    maju: maju, papanKempen: papanKempen, ringkas: ringkas,
    rupiah: rupiah, juta: juta
  };
})();
