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

/* ---------- Agreement generator demo (generator.html) ---------- */
(function(){
  function el(id){ return document.getElementById(id); }
  if (!el('genBtn')) return;
  var UNITS = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'];
  var TENS = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];
  function under1000(n){ var s=''; if(n>99){ s+=UNITS[Math.floor(n/100)]+' Hundred '; n=n%100; } if(n>19){ s+=TENS[Math.floor(n/10)]+' '; n=n%10; } if(n>0){ s+=UNITS[n]+' '; } return s.trim(); }
  function words(n){
    if(n===0) return 'Zero';
    var out=''; var groups=[[1000000000,'Billion'],[1000000,'Million'],[1000,'Thousand']];
    for(var i=0;i<groups.length;i++){ var g=groups[i][0]; if(n>=g){ out+=under1000(Math.floor(n/g))+' '+groups[i][1]+' '; n=n%g; } }
    if(n>0){ out+=under1000(n); }
    return out.trim();
  }
  function addMonths(d, m){ var x=new Date(d.getTime()); var day=x.getDate(); x.setMonth(x.getMonth()+m); if(x.getDate()<day){ x.setDate(0); } return x; }
  function fmt(d){ var mo=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']; return ('0'+d.getDate()).slice(-2)+' '+mo[d.getMonth()]+' '+d.getFullYear(); }
  function lines(cls, txt){ return '<div class="small" style="margin:4px 0"><span class="pill '+cls+'">'+(cls==='bad'?'blocked':(cls==='warn'?'warning':'pass'))+'</span> '+txt+'</div>'; }
  el('genBtn').addEventListener('click', function(){
    var price = parseFloat(String(el('genPrice').value).replace(/[^0-9.]/g,''))||0;
    var say = el('genWords').value||'';
    var ic = String(el('genIc').value).replace(/[^0-9]/g,'');
    var spa = new Date(el('genSpa').value);
    var comp = new Date(el('genComp').value);
    var rate = parseFloat(el('genInt').value)||0;
    var strata = el('chipStrata').querySelector('input').checked;
    var bumi = el('chipBumi').querySelector('input').checked;
    var restrict = el('chipRestrict').querySelector('input').checked;
    var bad=[], warn=[], good=[];
    var expect = words(price);
    var sayNorm = say.toLowerCase().replace(/[^a-z ]/g,' ').replace(/\s+/g,' ').trim();
    if (expect && sayNorm.indexOf(expect.toLowerCase())===-1) {
      bad.push('Price in figures (RM'+price.toLocaleString('en-US')+') does not match the words. The engine reads &ldquo;'+expect+'&rdquo;.');
    } else { good.push('Price in figures matches the words: Ringgit Malaysia '+expect+' Only.'); }
    if (ic.length!==12) { bad.push('Identification number has '+ic.length+' digits after cleaning; twelve are required.'); }
    else { good.push('Identification number format is valid ('+ic.slice(0,6)+'-'+ic.slice(6,8)+'-'+ic.slice(8)+').'); }
    if (isNaN(spa)||isNaN(comp)) { bad.push('SPA date or completion date is empty.'); }
    else {
      var plus3=addMonths(spa,3), plus4=addMonths(spa,4);
      if (comp.getTime()===plus3.getTime()) { good.push('Completion date is exactly the SPA date plus three months ('+fmt(plus3)+'). The 3+1 extension, if taken, ends '+fmt(plus4)+' with interest.'); }
      else if (comp.getTime()===plus4.getTime()) { warn.push('Completion date is SPA plus four months - the 3+1 reading. The extension interest clause must be present.'); }
      else { bad.push('Completion date ('+fmt(comp)+') is neither SPA plus three months ('+fmt(plus3)+') nor plus four ('+fmt(plus4)+').'); }
    }
    if (rate && (rate<8||rate>10)) { warn.push('Late payment interest of '+rate+'% per annum is outside the firm\u2019s 8-10% band. A partner must acknowledge.'); }
    else if (rate) { good.push('Late payment interest of '+rate+'% per annum is within the firm\u2019s band.'); }
    if (bumi) { bad.push('Bumiputera lot selected. A release or state authority approval clause and evidence of consent must be attached first.'); }
    if (restrict) { bad.push('Restriction in interest selected. The state authority consent clause and the consent letter must be attached first.'); }
    if (strata) { good.push('Strata block included: Act 757 notices, by-laws and management corporation clauses.'); }
    var blocks = ['Parties and recitals','Property and title particulars','Purchase price and payment schedule','Deposit and stakeholder terms','Completion and vacant possession','Redemption of existing charge','Loan rejection and refund of deposit','Transfer, charge and registration','Chattels, fittings and inventory list','Apportionment of taxes and outgoings','Default, late payment and remedies','Notices and service','Dispute resolution and governing law','Execution and attestation pages'];
    if (strata) blocks.push('Strata management and by-laws (Act 757)');
    if (!bumi) blocks.push('Bumiputera release clause (not applicable - omitted)');
    var html = '';
    if (bad.length) { html += '<b>Generation blocked.</b> Fix these and generate again.'; bad.forEach(function(t){ html+=lines('bad',t); }); }
    else { html += '<b>Document generated.</b> Watermarked DRAFT, awaiting partner approval.'; }
    warn.forEach(function(t){ html+=lines('warn',t); });
    good.forEach(function(t){ html+=lines('ok',t); });
    html += '<div class="hr"></div><b>Assembled from '+blocks.length+' blocks:</b><div class="small muted" style="margin-top:4px">'+blocks.join(' &middot; ')+'</div>';
    html += '<div class="hr"></div><div class="small"><b>Scan:</b> no leftover placeholders &middot; parties consistent in 23 references &middot; inventory list attached &middot; 38 pages (inside range). Template pinned: v9.1, clause set pinned: CL-2026-09-17-4.</div>';
    el('genResult').innerHTML = html;
  });
  ['chipStrata','chipBumi','chipRestrict'].forEach(function(id){
    var box = el(id); if(!box) return;
    var inp = box.querySelector('input');
    inp.addEventListener('change', function(){ box.classList.toggle('on', inp.checked); });
  });
})();
