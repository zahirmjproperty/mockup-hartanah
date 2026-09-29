/* booking.js — Fasa 1 booking E-Form wizard (preview only, nothing is sent anywhere). */
(function(){
  const P = F1.PROJECTS, U = F1.UNITS, A = F1.AGENTS, L = F1.LEADS, ST = F1.STAGES;
  const $ = id => document.getElementById(id);
  const money = n => 'RM' + Number(n).toLocaleString('en-MY');
  const lead = new URLSearchParams(location.search).get('lead');
  const src = lead ? (L.find(x => x.id === lead) || null) : null;

  const S = {
    step:1, proj: src ? src.project : P[0].id, unit:null, agent: src && src.owner ? src.owner : A[0].id,
    buyer:{name: src ? src.name : '', phone: src ? src.phone : '', email: src ? src.email : '', ic:'' },
    scheme:{price:0, rebate:3, fee:1000, bank:'Maybank'},
    consent:{c1:false,c2:false,c3:false}, signed:false, id:null
  };
  if(src && src.unit_interest){ /* keep the interest text visible in the unit filter */ }

  /* ---------- selects ---------- */
  P.forEach(p => $('proj').insertAdjacentHTML('beforeend', '<option value="' + p.id + '">' + p.name + ' &middot; ' + p.location + '</option>'));
  A.forEach(a => $('ag').insertAdjacentHTML('beforeend', '<option value="' + a.id + '">' + a.name + ' (' + a.level + ')</option>'));
  $('proj').value = S.proj; $('ag').value = S.agent;

  /* ---------- step chrome ---------- */
  const TITLES = ['Project and unit','Buyer','Scheme','Consent','Signature','Review','Done'];
  function steps(){
    $('steps').innerHTML = TITLES.map((t,i) =>
      '<div class="step ' + (i+1 === S.step ? 'on' : (i+1 < S.step ? 'done' : '')) + '">' + (i+1) + '. ' + t + '</div>').join('');
    for(let i=1;i<=7;i++) $('p'+i).classList.toggle('on', i === S.step);
    $('back').style.visibility = (S.step === 1 || S.step >= 6) ? 'hidden' : 'visible';
    $('next').style.visibility = S.step >= 6 ? 'hidden' : 'visible';
  }

  /* ---------- units ---------- */
  let availOnly = false;
  const STATUS_PILL = {available:'ok', reserved:'warn', booked:'blue', sold:''};
  function units(){
    const rows = U.filter(u => u.project === S.proj).filter(u => !availOnly || u.status === 'available');
    $('ucount').textContent = rows.length + ' unit(s) in this project' + (availOnly ? ' (available only)' : '');
    $('utbl').querySelector('tbody').innerHTML = rows.map(u =>
      '<tr class="lrow" data-u="' + u.id + '"' + (S.unit === u.id ? ' style="background:var(--gold-soft)"' : '') + '>' +
      '<td><b>' + u.id + '</b><div class="lsub">Block ' + u.block + ' &middot; level ' + (u.level || 'G') + '</div></td>' +
      '<td>' + u.type + '</td><td class="num">' + u.built_up + ' sqft</td><td class="num">' + money(u.price) + '</td>' +
      '<td><span class="pill ' + STATUS_PILL[u.status] + '">' + u.status + '</span></td>' +
      '<td>' + (u.status === 'available' ? (S.unit === u.id ? '<b>Selected</b>' : 'Select') : '<span class="small muted">not available</span>') + '</td></tr>').join('');
    $('utbl').querySelectorAll('tbody tr').forEach(tr => tr.onclick = () => {
      const u = U.find(x => x.id === tr.dataset.u);
      if(u.status !== 'available'){ $('msg').textContent = 'That unit is ' + u.status + ' and cannot be booked.'; return; }
      S.unit = u.id; S.scheme.price = u.price; $('msg').textContent = ''; $('pr').value = u.price;
      units(); calc();
    });
  }
  document.querySelector('[data-avail]').onclick = e => { availOnly = !availOnly; units(); };
  $('proj').onchange = () => { S.proj = $('proj').value; S.unit = null; S.scheme.price = 0; units(); };
  $('ag').onchange = () => { S.agent = $('ag').value; };

  /* ---------- buyer + scheme ---------- */
  ['bn','bp','be','bi'].forEach((id,i) => {
    const key = ['name','phone','email','ic'][i];
    $(id).value = S.buyer[key] || '';
    $(id).oninput = () => { S.buyer[key] = $(id).value.trim(); };
  });
  function calc(){
    const p = Number($('pr').value || 0);
    const reb = Number($('rb').value || 0);
    const net = Math.round(p * (1 - reb/100));
    const loan = Math.round(net * 0.9);
    const inst = Math.round(loan * (0.042/12) / (1 - Math.pow(1 + 0.042/12, -420)));
    $('calc').innerHTML = 'Net price after rebate: <b>' + money(net) + '</b> &middot; estimated loan at 90%: <b>' + money(loan) +
      '</b> &middot; indicative monthly instalment (4.2%, 35 years): <b>' + money(inst) + '</b>. Indicative only &mdash; the bank decides.';
    S.scheme.net = net; S.scheme.loan = loan; S.scheme.inst = inst;
  }
  $('pr').oninput = calc; $('rb').onchange = () => { S.scheme.rebate = Number($('rb').value); calc(); };
  $('bf').onchange = () => { S.scheme.fee = Number($('bf').value); };
  $('bk').onchange = () => { S.scheme.bank = $('bk').value; };

  /* ---------- consent ---------- */
  ['c1','c2','c3'].forEach(id => $(id).onchange = () => { S.consent[id] = $(id).checked; });

  /* ---------- signature ---------- */
  const cv = $('pad'); const ctx = cv.getContext('2d');
  let drawing = false, signed = false;
  function fit(){ const r = cv.getBoundingClientRect(); cv.width = r.width; cv.height = 150; ctx.lineWidth = 2; ctx.strokeStyle = '#e8ce86'; }
  setTimeout(fit, 60); window.addEventListener('resize', fit);
  const pos = e => { const r = cv.getBoundingClientRect(); const t = e.touches ? e.touches[0] : e; return {x:t.clientX - r.left, y:t.clientY - r.top}; };
  const start = e => { drawing = true; const p = pos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); e.preventDefault(); };
  const move = e => { if(!drawing) return; const p = pos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); e.preventDefault(); };
  const end = () => { if(!drawing) return; drawing = false; S.signed = signed = true; $('sigstate').textContent = 'Signed just now'; };
  cv.addEventListener('mousedown', start); cv.addEventListener('mousemove', move); window.addEventListener('mouseup', end);
  cv.addEventListener('touchstart', start, {passive:false}); cv.addEventListener('touchmove', move, {passive:false}); cv.addEventListener('touchend', end);
  $('clear').onclick = () => { ctx.clearRect(0,0,cv.width,cv.height); S.signed = signed = false; $('sigstate').textContent = 'Not signed yet'; };

  /* ---------- review ---------- */
  function sum(){
    const u = U.find(x => x.id === S.unit) || {};
    const p = P.find(x => x.id === S.proj) || {};
    const a = A.find(x => x.id === S.agent) || {};
    return [['Project', p.name + ' (' + p.apdl + ')'], ['Unit', u.id + ' &middot; ' + u.type + ' &middot; ' + u.built_up + ' sqft'],
      ['Buyer', S.buyer.name + ' &middot; ' + S.buyer.phone], ['Agent', a.name + ' (' + S.agent + ')'],
      ['Price', money(S.scheme.price)], ['Rebate', $('rb').value + '% &middot; net ' + money(S.scheme.net || 0)],
      ['Booking fee', money($('bf').value)], ['Bank', $('bk').value],
      ['Consent', ['PDPA','Marketing','Accuracy'].filter((t,i) => S.consent['c'+(i+1)]).join(', ') || 'none recorded'],
      ['Signature', S.signed ? 'signed in this session' : 'NOT signed']];
  }
  function paintSum(){
    $('sum').innerHTML = sum().map(r => '<dt>' + r[0] + '</dt><dd>' + r[1] + '</dd>').join('');
  }

  /* ---------- validation + navigation ---------- */
  function check(){
    if(S.step === 1 && !S.unit) return 'Pick an available unit first.';
    if(S.step === 2){
      if(!S.buyer.name) return 'Buyer name is required (as per IC).';
      if(!/^0\d{2}-\d{4} \d{4}$/.test(S.buyer.phone)) return 'Use the demo phone format 011-0000 ####.';
      if(!/^[^@]+@example\.com$/.test(S.buyer.email)) return 'Use an @example.com address in this preview.';
    }
    if(S.step === 3 && !(S.scheme.price > 0)) return 'Price must be greater than zero.';
    if(S.step === 4 && !(S.consent.c1 && S.consent.c2 && S.consent.c3)) return 'All three consent boxes must be ticked — this is the gate that protects the agency.';
    if(S.step === 5 && !S.signed) return 'The buyer must sign before the booking can be submitted.';
    return '';
  }
  $('next').onclick = () => {
    const m = check();
    if(m){ $('msg').textContent = m; return; }
    $('msg').textContent = '';
    S.step = Math.min(6, S.step + 1);
    if(S.step === 6) paintSum();
    steps();
  };
  $('back').onclick = () => { $('msg').textContent = ''; S.step = Math.max(1, S.step - 1); steps(); };
  function validateAll(){
    for(let s = 1; s <= 5; s++){
      const keep = S.step; S.step = s;
      const m = check(); S.step = keep;
      if(m) return {step:s, msg:m};
    }
    return null;
  }
  $('submit').onclick = () => {
    const bad = validateAll();
    if(bad){
      S.step = bad.step; steps();
      $('msg').textContent = 'Cannot submit yet — step ' + bad.step + ': ' + bad.msg;
      return;
    }
    $('msg').textContent = '';
    const u = U.find(x => x.id === S.unit);
    if(!u){ $('msg').textContent = 'The selected unit no longer exists — pick it again.'; return; }
    S.id = 'BK-2609-' + String(18 + Math.floor(Math.random() * 9)).padStart(3,'0');
    u.status = 'booked';
    const p = P.find(x => x.id === S.proj) || {};
    F1.BOOKINGS.push({id:S.id, project:S.proj, unit:S.unit, lead:lead || 'walk-in', buyer:S.buyer.name,
      agent:S.agent, price:S.scheme.price, rebate:$('rb').value + '%', stage:1, booked:'2026-09-29',
      bank:'not submitted', lawyer:'not appointed', signed_lo:null, updated:'2026-09-29 10:00', sumber:'SINTETIK'});
    $('okid').innerHTML = S.id + ' &middot; ' + p.name + ' &middot; unit ' + S.unit;
    $('sum2').innerHTML = sum().concat([['Stage', ST[0].k + ' of 7 &middot; ' + ST[0].label],
      ['Sees it now', ST[0].who.join(', ')], ['Next', ST[0].desc]]).map(r => '<dt>' + r[0] + '</dt><dd>' + r[1] + '</dd>').join('');
    $('toPipe').href = 'booking-status.html?id=' + S.id;
    S.step = 7; steps();
  };
  $('again').onclick = () => location.href = 'booking-new.html';

  if(src){ $('msg').textContent = 'Prefilled from lead ' + src.id + ' — ' + src.name; }
  units(); calc(); steps();
})();
