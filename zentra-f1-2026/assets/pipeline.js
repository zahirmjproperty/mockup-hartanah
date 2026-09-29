/* pipeline.js — Fasa 1 booking pipeline board, role views and stage timeline. Preview only. */
(function(){
  const B = F1.BOOKINGS, ST = F1.STAGES, P = F1.PROJECTS, U = F1.UNITS, A = F1.AGENTS, L = F1.LEADS;
  const $ = id => document.getElementById(id);
  const money = n => 'RM' + Number(n).toLocaleString('en-MY');
  const proj = id => (P.find(p => p.id === id) || {}).name || id;
  const agent = id => (A.find(a => a.id === id) || {}).name || id;
  const pill = k => k >= 7 ? 'ok' : (k >= 5 ? 'blue' : (k >= 3 ? 'gold' : 'warn'));

  let sel = new URLSearchParams(location.search).get('id') || B[0].id;
  let stageFilter = 0;
  let role = 'Agent';

  /* ---------- KPIs ---------- */
  const inPipe = B.filter(x => x.stage < 7);
  const value = inPipe.reduce((s,x) => s + x.price, 0);
  $('kpis').innerHTML = [
    {lab:'Bookings in pipeline', val:inPipe.length, sub:B.length + ' records in total', c:''},
    {lab:'Value in pipeline', val:money(value), sub:'selling price of open bookings', c:'blue'},
    {lab:'Waiting on the bank', val:B.filter(x => x.stage === 3).length, sub:'valuation or offer letter', c:'warn'},
    {lab:'At the lawyer', val:B.filter(x => x.stage === 5).length, sub:'SPA or deed of assignment', c:'warn'}
  ].map(k => '<div class="kpi ' + k.c + '"><div class="lab">' + k.lab + '</div><div class="val">' + k.val +
    '</div><div class="sub">' + k.sub + '</div></div>').join('');

  /* ---------- board ---------- */
  function board(){
    $('board').innerHTML = ST.map(s => {
      const rows = B.filter(x => x.stage === s.k);
      const v = rows.reduce((a,x) => a + x.price, 0);
      return '<div class="stg ' + (stageFilter === s.k ? 'on' : '') + '" data-k="' + s.k + '">' +
        '<div class="k">STAGE ' + s.k + '</div><div class="t">' + s.label + '</div>' +
        '<div class="v">' + rows.length + '</div><div class="k">' + (v ? money(v) : '—') + '</div></div>';
    }).join('');
    $('board').querySelectorAll('.stg').forEach(el => el.onclick = () => {
      stageFilter = (stageFilter === Number(el.dataset.k)) ? 0 : Number(el.dataset.k);
      board(); table();
    });
  }

  /* ---------- table ---------- */
  function table(){
    const rows = B.filter(x => !stageFilter || x.stage === stageFilter);
    $('tbl').querySelector('tbody').innerHTML = rows.map(x => {
      const w = Math.round(x.stage / 7 * 100);
      return '<tr class="lrow" data-id="' + x.id + '">' +
        '<td><b>' + x.id + '</b><div class="lsub">' + (x.lead || '') + '</div></td>' +
        '<td>' + proj(x.project) + '<div class="lsub">' + x.unit + '</div></td>' +
        '<td>' + x.buyer + '</td><td>' + agent(x.agent) + '</td>' +
        '<td class="num money">' + money(x.price) + '</td>' +
        '<td><span class="pill ' + pill(x.stage) + '">' + x.stage + ' &middot; ' + ST[x.stage-1].label + '</span>' +
        '<div class="bar" style="margin-top:6px"><i style="width:' + w + '%"></i></div></td>' +
        '<td>' + x.updated + '</td></tr>';
    }).join('');
    $('tbl').querySelectorAll('tbody tr').forEach(tr => tr.onclick = () => { sel = tr.dataset.id; detail(); });
  }

  /* ---------- role view ---------- */
  const ROLE = {
    Agent:    {sees:['Own bookings only — never another agent&rsquo;s buyer','Buyer contact, agreed rebate, unit held','Commission estimate for the deal'],
               does:['Upload the booking form and the buyer&rsquo;s documents','See exactly what is blocking the file','Chase the bank and the lawyer'],
               not:'Bank&rsquo;s internal notes, the developer&rsquo;s payment ledger, other agents&rsquo; buyers'},
    Developer:{sees:['Every booking in the developer&rsquo;s own project','Unit hold, price, rebate request and approval','Payment position per file'],
               does:['Confirm or release the unit hold','Approve or reject the rebate','Mark progress billing and handover'],
               not:'The agent&rsquo;s commission split, the leader override, other developers&rsquo; projects'},
    Bank:     {sees:['Only buyers who signed the booking and consented to loan processing','Valuation, income documents, offer letter status'],
               does:['Issue the offer letter','Record the valuation and any condition','Return the file if documents are incomplete'],
               not:'The rebate negotiation, the agency commission, the developer&rsquo;s internal ledger'},
    Lawyer:   {sees:['SPA preparation data — unit, price, buyer identity, developer entity','Signed LO and the booking form','Stamping and registration dates'],
               does:['Prepare and issue the SPA or deed of assignment','Record execution and stamping','Flag any title or consent issue'],
               not:'The agency&rsquo;s commission or the rebate internal notes'}
  };
  function roles(){
    $('roles').innerHTML = Object.keys(ROLE).map(r =>
      '<button class="btn ghost ' + (r === role ? 'on' : '') + '" data-r="' + r + '">' + r + ' view</button>').join('');
    $('roles').querySelectorAll('.btn').forEach(b => b.onclick = () => { role = b.dataset.r; roles(); detail(); });
  }

  /* ---------- detail: role view + timeline ---------- */
  function detail(){
    const x = B.find(b => b.id === sel) || B[0];
    const s = ST[x.stage - 1];
    const R = ROLE[role];
    $('roleview').innerHTML =
      '<h3 style="margin-top:0">' + role + ' &middot; ' + x.id + ' at stage ' + x.stage + ' (' + s.label + ')</h3>' +
      '<p class="small muted" style="margin-top:0">' + s.desc + '</p>' +
      '<div class="grid g3">' +
      '<div><div class="lab small muted">Sees</div><ul class="small" style="margin:6px 0 0;padding-left:18px">' + R.sees.map(t => '<li>' + t + '</li>').join('') + '</ul></div>' +
      '<div><div class="lab small muted">Can do</div><ul class="small" style="margin:6px 0 0;padding-left:18px">' + R.does.map(t => '<li>' + t + '</li>').join('') + '</ul></div>' +
      '<div><div class="lab small muted">Never sees</div><p class="small" style="margin:6px 0 0">' + R.not + '</p></div>' +
      '</div>';

    $('who2').textContent = '· ' + x.id + ' · ' + proj(x.project) + ' · ' + x.buyer;
    $('tl').innerHTML = ST.map(st => {
      const cls = st.k < x.stage ? 'done' : (st.k === x.stage ? 'now' : '');
      const when = st.k === 1 ? x.booked : (st.k === 4 && x.signed_lo ? x.signed_lo : (st.k === x.stage ? x.updated : '—'));
      return '<li class="' + cls + '"><div class="t">STAGE ' + st.k + ' &middot; ' + when + '</div>' +
        '<div class="w">' + st.label + '</div><div class="who">' + st.who.join(' &middot; ') + ' — ' + st.desc + '</div></li>';
    }).join('');
  }

  roles(); board(); table(); detail();
})();
