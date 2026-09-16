/* law.js — Zentra Law F0 interactions (vanilla JS, no build step).
   Semua kadar di sini adalah salinan daripada _f0_common.py untuk tujuan tunjuk cara sahaja. */
(function () {
  'use strict';

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function rm(x, dp) { dp = (dp === undefined) ? 2 : dp;
    var s = Math.round(x * Math.pow(10, dp)) / Math.pow(10, dp);
    return s.toFixed(dp).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

  /* ---- 1. chip groups behave like radio buttons ------------------------ */
  $$('.chips').forEach(function (g) {
    g.addEventListener('click', function (e) {
      var c = e.target.closest ? e.target.closest('.chip') : null;
      if (!c || c.classList.contains('chip-doc')) { return; }
      $$('.chip', g).forEach(function (x) { x.classList.remove('on'); });
      c.classList.add('on');
      if (g.id === 'mFilter') { filterMatters(c.getAttribute('data-k') || 'all'); }
    });
  });

  /* ---- 2. matter filter + search --------------------------------------- */
  function filterMatters(kind) {
    var rows = $$('#mTable tr[data-k]');
    var q = ($('#mSearch') && $('#mSearch').value || '').toLowerCase();
    rows.forEach(function (r) {
      var okKind = (kind === 'all') || (r.getAttribute('data-k') === kind);
      var okText = !q || r.textContent.toLowerCase().indexOf(q) >= 0;
      r.style.display = (okKind && okText) ? '' : 'none';
    });
  }
  var ms = $('#mSearch');
  if (ms) {
    ms.addEventListener('keyup', function () {
      var on = $('#mFilter .chip.on');
      filterMatters(on ? (on.getAttribute('data-k') || 'all') : 'all');
    });
  }

  /* ---- 3. signing guard ------------------------------------------------- */
  var RULES = {
    esign: ['ok', '<b>Sent.</b> This document may be signed electronically under the Electronic Commerce Act 2006. The envelope will carry the signing certificate, the document hash and the access log &mdash; the three things that answer a dispute about a signature.'],
    wet: ['warn', '<b>Blocked, and routed instead.</b> This document is produced for wet-ink execution with attesting witnesses. The prototype records the intended signatories and opens a signing-session request rather than sending an electronic envelope.'],
    block: ['bad', '<b>Refused.</b> Instruments of transfer and charge are executed in wet ink: the land office and the stamping counter will not accept an electronic signature. The system will not pretend otherwise &mdash; it logs the attempt, who tried, and when.']
  };
  var sel = $('#docSel'), btn = $('#sendBtn'), box = $('#guardBox');
  if (sel && btn && box) {
    btn.addEventListener('click', function () {
      var r = RULES[sel.value] || RULES.esign;
      box.className = 'note' + (r[0] === 'ok' ? '' : ' ' + r[0]);
      box.innerHTML = r[1];
    });
  }

  /* ---- 4. fee engine ---------------------------------------------------- */
  function scale(v) {
    if (v <= 0) { return 0; }
    var f = Math.min(v, 500000) * 0.0125;
    if (v > 500000) { f += (Math.min(v, 7500000) - 500000) * 0.01; }
    return Math.max(f, 500);
  }
  function dutyMot(v) {
    var d = Math.min(v, 100000) * 0.01;
    if (v > 100000) { d += (Math.min(v, 500000) - 100000) * 0.02; }
    if (v > 500000) { d += (Math.min(v, 1000000) - 500000) * 0.03; }
    if (v > 1000000) { d += (v - 1000000) * 0.04; }
    return d;
  }
  function fees() {
    var price = parseFloat(($('#fPrice') || {}).value || 0) || 0;
    var loan = parseFloat(($('#fLoan') || {}).value || 0) || 0;
    var discPct = parseFloat(($('#fDisc') || {}).value || 0) || 0;
    var out = $('#fOut'), note = $('#discNote');
    if (!out) { return; }
    var gross = scale(price), loanFee = scale(loan);
    var disc = gross * Math.min(discPct, 25) / 100;
    var sst = (gross - disc + loanFee) * 0.08;
    var rows = [
      ['Professional fee &mdash; sale and purchase', 'Scale 1.25% / 1%, minimum RM500', gross, 0],
      ['Discount granted', 'Ceiling 25% of the scale fee', -disc, -1],
      ['Professional fee &mdash; financing documents', 'Third Schedule scale', loanFee, 0],
      ['SST', '8% on professional fees after discount', sst, 0],
      ['Stamp duty &mdash; MOT', '1% / 2% / 3% / 4% bands', dutyMot(price), 0],
      ['Stamp duty &mdash; loan agreement', '0.5% of amount secured', loan * 0.005, 0]
    ];
    var html = '<tr><th>Line</th><th>Basis</th><th class="num">Amount (RM)</th></tr>';
    var total = 0;
    rows.forEach(function (r) {
      total += r[2];
      html += '<tr><td>' + r[0] + '</td><td class="small muted">' + r[1] + '</td><td class="num">' +
              (r[2] < 0 ? '-' : '') + rm(Math.abs(r[2])) + '</td></tr>';
    });
    html += '<tr class="total"><td>Professional fees, tax and duty</td><td>&mdash;</td><td class="num">' + rm(total) + '</td></tr>';
    out.innerHTML = html;
    if (note) {
      if (discPct > 25) {
        note.className = 'note warn';
        note.innerHTML = '<b>Refused at ' + discPct + '%.</b> The order caps a discount at 25% of the scale fee for sale and transfer work. The engine applies 25% and logs the request as refused &mdash; it does not quietly round the number down.';
      } else if (discPct == 25) {
        note.className = 'note';
        note.innerHTML = '<b>At the ceiling.</b> A 25% discount is the most the order allows here. Anything beyond it has to be a genuine waiver of fees recorded in the client\'s favour, with a reason and an approver.';
      } else {
        note.className = 'note';
        note.innerHTML = '<b>Within the ceiling.</b> ' + discPct + '% granted. There is room to ' + (25 - discPct) + ' percentage points before the cap.';
      }
    }
  }
  ['#fPrice', '#fLoan', '#fDisc'].forEach(function (s) {
    var el = $(s);
    if (el) { el.addEventListener('input', fees); el.addEventListener('change', fees); }
  });
  if ($('#fOut')) { fees(); }
})();
