/* nav.js — satu sumber navigasi Zentra Push: ikon SVG, keadaan aktif, togol tema */
(function(){
  const I = {
    home:'<path d="M3 10.6 12 3l9 7.6V21H3z"/><path d="M9 21v-6h6v6"/>',
    layers:'<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    send:'<path d="M21 3 3 10.5l7 2.5 2.5 7z"/><path d="M21 3 10 14"/>',
    plug:'<path d="M9 3v5M15 3v5"/><path d="M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v4"/>',
    grid:'<circle cx="7.5" cy="7.5" r="2.2"/><circle cx="16.5" cy="7.5" r="2.2"/><circle cx="7.5" cy="16.5" r="2.2"/><circle cx="16.5" cy="16.5" r="2.2"/>',
    shield:'<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
    list:'<path d="M8 6h13M8 12h13M8 18h13"/><circle cx="4" cy="6" r="1.2"/><circle cx="4" cy="12" r="1.2"/><circle cx="4" cy="18" r="1.2"/>',
    clock:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.4 2"/>',
    users:'<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><path d="M16 5.5a3 3 0 0 1 0 5.8"/><path d="M17.5 20a6 6 0 0 0-2-4.5"/>',
    plus:'<path d="M12 5v14M5 12h14"/>',
    home2:'<path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10.5V20h13v-9.5"/><path d="M12 14.5v5.5M9.5 17h5"/>',
    map:'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    cog:'<circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v2.4M12 18.8v2.4M4.6 7.2l2 1.2M17.4 15.6l2 1.2M4.6 16.8l2-1.2M17.4 8.4l2-1.2"/>',
    sun:'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
  };
  const N = [
    {sec:'Distribution'},
    {h:'new.html',       t:'New listing',     i:'plus'},
    {h:'index.html',     t:'Overview',        i:'home'},
    {h:'push.html',      t:'Push console',    i:'send'},
    {h:'listings.html',  t:'Listing ledger',  i:'list'},
    {h:'channels.html',  t:'Channel matrix',  i:'plug'},
    {sec:'Governance'},
    {h:'compliance.html',t:'Compliance guard',i:'shield'},
    {h:'evidence.html',  t:'Evidence & audit',i:'clock'},
    {h:'agents.html',    t:'Agents & quota',  i:'users'},
    {sec:'Blueprint'},
    {h:'roadmap.html',   t:'Roadmap & phases',i:'layers'}
  ];
  const here=(location.pathname.split('/').pop()||'index.html');
  const host=document.getElementById('znav');
  if(!host) return;
  let html='<div class="brand"><div class="mark"><img src="assets/zp-mark.png" alt="Zentra Push" width="34" height="34"></div><div><b>Zentra Push</b><small>Zentra Property Group</small></div></div><nav class="nav">';
  N.forEach(n=>{
    if(n.sec){ html+='<div class="sec">'+n.sec+'</div>'; return; }
    const on = (n.h===here)||(here===''&&n.h==='index.html');
    html+='<a href="'+n.h+'"'+(on?' class="on"':'')+'><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'+I[n.i]+'</svg><span>'+n.t+'</span></a>';
  });
  html+='</nav>';
  html+='<div class="sideact"><button class="btn ghost small" id="themeBtn"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round">'+I.sun+'</svg><span id="themeTxt">Light</span></button></div>';
  html+='<div class="foot">Interactive mockup &middot; sample data only<br>Zentra Property Group &copy; 2026</div>';
  host.innerHTML=html;

  /* togol tema — :root.theme-light untuk kekhususan yang betul */
  const btn=document.getElementById('themeBtn'), txt=document.getElementById('themeTxt');
  function paint(){
    const light=document.documentElement.classList.contains('theme-light');
    if(txt) txt.textContent = light ? 'Dark' : 'Light';
  }
  if(btn) btn.onclick=function(){
    const light=document.documentElement.classList.toggle('theme-light');
    try{ localStorage.setItem('zp-theme', light?'light':'dark'); }catch(e){}
    paint();
  };
  paint();
})();
