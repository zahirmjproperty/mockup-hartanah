/* nav.js — satu sumber navigasi Zentra Hub: ikon SVG, keadaan aktif, menu mudah alih */
(function(){
  const I = {  /* ikon stroke 24px */
    home:'<path d="M3 10.6 12 3l9 7.6V21H3z"/><path d="M9 21v-6h6v6"/>',
    map:'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    file:'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    cog:'<circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v2.4M12 18.8v2.4M4.6 7.2l2 1.2M17.4 15.6l2 1.2M4.6 16.8l2-1.2M17.4 8.4l2-1.2"/>',
    mail:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
    users:'<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><path d="M16 5.5a3 3 0 0 1 0 5.8"/><path d="M17.5 20a6 6 0 0 0-2-4.5"/>',
    user:'<circle cx="12" cy="8" r="3.4"/><path d="M5 20a7 7 0 0 1 14 0"/>',
    list:'<path d="M8 6h13M8 12h13M8 18h13"/><circle cx="4" cy="6" r="1.2"/><circle cx="4" cy="12" r="1.2"/><circle cx="4" cy="18" r="1.2"/>',
    sum:'<path d="M5 5h14l-8 7 8 7H5"/>',
    check:'<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.6 2.6L16.5 9"/>',
    swap:'<path d="M4 8h13l-3.2-3.2M20 16H7l3.2 3.2"/>',
    board:'<path d="M3 4h18v12H3z"/><path d="M8 20h8M12 16v4"/>',
    shield:'<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
    grid:'<circle cx="7.5" cy="7.5" r="2.2"/><circle cx="16.5" cy="7.5" r="2.2"/><circle cx="7.5" cy="16.5" r="2.2"/><circle cx="16.5" cy="16.5" r="2.2"/>',
    sitemap:'<rect x="9" y="3" width="6" height="4" rx="1"/><rect x="3" y="14" width="6" height="4" rx="1"/><rect x="15" y="14" width="6" height="4" rx="1"/><path d="M12 7v4M12 11H6v3M12 11h6v3"/>',
    search:'<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>',
    bell:'<path d="M18 8a6 6 0 1 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
    sig:'<path d="M3 17c3-6 5-9 6.5-9 2 0-1.5 6.5.5 6.5S14 6 15.5 6c1.2 0 .5 3.5 2 3.5.9 0 1.6-.9 2.5-2"/><path d="M3 21h18"/>'
  };
  const N = [
    {sec:'Operations'},
    {h:'index.html', t:'Overview', i:'home'},
    {h:'platform.html', t:'Platform map', i:'map'},
    {h:'documents.html', t:'Documents & e-sign', i:'file'},
    {h:'search.html', t:'Deals & documents', i:'search'},
    {h:'f1.html', t:'F1 document generator', i:'cog', d:1},
    {h:'f2.html', t:'F2 send & track', i:'mail', d:1},
    {h:'sign.html', t:'F2 client signing view', i:'sig', d:1},
    {h:'team.html', t:'Team & referrers', i:'users'},
    {h:'tree.html', t:'Team tree', i:'sitemap'},
    {h:'agents.html', t:'Agent registry', i:'user'},
    {h:'onboard.html', t:'Agent onboarding', i:'list'},
    {h:'hierarchy.html', t:'Levels & hierarchy', i:'list'},
    {sec:'Money'},
    {h:'f3.html', t:'F3 reward engine', i:'sum', d:1},
    {h:'commission.html', t:'Commission engine', i:'sum'},
    {h:'claims.html', t:'Claims & vouchers', i:'check'},
    {h:'payouts.html', t:'Payout runs', i:'swap'},
    {sec:'Governance'},
    {h:'f4.html', t:'F4 monitoring board', i:'board', d:1},
    {h:'compliance.html', t:'Compliance guard', i:'shield'},
    {h:'notifications.html', t:'Notification centre', i:'bell', d:1},
    {h:'modules.html', t:'Module map', i:'grid'}
  ];
  const here=(location.pathname.split('/').pop()||'index.html');
  const host=document.getElementById('znav');
  if(!host) return;
  let html='<div class="brand"><div class="mark">ZH</div><div><b>Zentra Hub</b><small>Zentra Property Group</small></div></div><nav class="nav">';
  N.forEach(n=>{
    if(n.sec){ html+='<div class="sec">'+n.sec+'</div>'; return; }
    const on = (n.h===here)||(here===''&&n.h==='index.html');
    html+='<a href="'+n.h+'"'+(on?' class="on"':'')+'><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'+I[n.i]+'</svg><span>'+n.t+'</span>'+(n.d?'<span class="pill-live">demo</span>':'')+'</a>';
  });
  html+='</nav><div class="foot">Prototype &middot; sample data only<br>Zentra Property Group &copy; 2026</div>';
  host.innerHTML=html;
  /* bar konteks berterusan (Claude #6) */

  /* ---------- pusat notifikasi (Pakej B) ---------- */
  function bell(){
    if(!document.querySelector('.bellwrap')){
      const w=document.createElement('div'); w.className='bellwrap';
      w.innerHTML='<button class="bell" id="bellBtn" aria-label="Notifications"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg><span class="dot" id="bellDot"></span></button>';
      document.body.appendChild(w);
      const d=document.createElement('div'); d.className='drawer'; d.id='notifDrawer';
      d.innerHTML='<div class="dhead"><b>Notifications</b><button class="btn ghost small" id="ndAll">Mark all read</button></div><div id="ndList"></div><a class="dfoot" href="notifications.html">Open the notification centre &rarr;</a>';
      document.body.appendChild(d);
      document.getElementById('bellBtn').onclick=()=>{ paint(); d.classList.toggle('open'); };
      document.getElementById('ndAll').onclick=()=>{ ZTH.markAllRead(); paint(); };
    }
    paint();
  }
  function paint(){
    const cn=ZTH.unread().length;
    const dot=document.getElementById('bellDot'); if(dot) dot.style.display = cn? 'block':'none';
    const list=document.getElementById('ndList'); if(!list) return;
    const read=ZTH.loadRead();
    list.innerHTML = ZTH.notif.slice().sort((a,b)=>(b.pri||0)-(a.pri||0)).map(x=>`
      <a class="nitem ${read.includes(x.id)?'read':''}" href="${x.href}" data-id="${x.id}">
        <span class="nbar ${x.t}"></span>
        <span class="nbody"><span class="ntop"><b>${x.ti}</b></span>
        <span class="nmeta">${x.mt}</span>
        <span class="nrow"><span class="pill ${x.t}">${x.s}</span><span class="nw">${x.w}</span></span></span>
      </a>`).join('');
    list.querySelectorAll('.nitem').forEach(a=>a.onclick=()=>{ ZTH.markRead(a.dataset.id); });
  }
  if(window.ZTH && ZTH.notif){ bell(); }
  if(here!=='index.html'){
    const main=document.querySelector('main.main');
    if(main && !document.querySelector('.ctxbar')){
      const cb=document.createElement('div'); cb.className='ctxbar';
      cb.innerHTML='<b>Zentra Hub</b> &middot; negotiator commission declared within the ceiling &middot; level and leader rewards are paid by the agency from its own share on completed transactions';
      main.insertBefore(cb, main.firstChild);
    }
  }
  /* menu mudah alih */
  const btn=document.createElement('button');
  btn.className='burger'; btn.setAttribute('aria-label','Menu');
  btn.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  document.body.appendChild(btn);
  const ov=document.createElement('div'); ov.className='overlay'; document.body.appendChild(ov);
  const close=()=>{ host.classList.remove('open'); ov.classList.remove('on'); };
  btn.onclick=()=>{ host.classList.toggle('open'); ov.classList.toggle('on'); };
  ov.onclick=close;
  host.addEventListener('click',e=>{ if(e.target.closest('a')) close(); });
})();
