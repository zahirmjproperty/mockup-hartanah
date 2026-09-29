/* nav.js — Fasa 1 preview navigation (Zentra Realty x Zentra Project).
   Compact sibling of zentra-realty/assets/nav.js: same sidebar pattern, same theme key. */
(function(){
  const I = {
    home:'<path d="M3 10.6 12 3l9 7.6V21H3z"/><path d="M9 21v-6h6v6"/>',
    users:'<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><path d="M16 5.5a3 3 0 0 1 0 5.8"/><path d="M17.5 20a6 6 0 0 0-2-4.5"/>',
    mail:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
    file:'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    sig:'<path d="M3 17c3-6 5-9 6.5-9 2 0-1.5 6.5.5 6.5S14 6 15.5 6c1.2 0 .5 3.5 2 3.5.9 0 1.6-.9 2.5-2"/><path d="M3 21h18"/>',
    rows:'<rect x="3" y="4.5" width="18" height="5" rx="1.5"/><rect x="3" y="14.5" width="18" height="5" rx="1.5"/>',
    sum:'<path d="M5 5h14l-8 7 8 7H5"/>',
    chart:'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    board:'<path d="M3 4h18v12H3z"/><path d="M8 20h8M12 16v4"/>'
  };
  const N = [
    {sec:'Preview'},
    {h:'index.html',       t:'F1 overview',        i:'home'},
    {sec:'Zentra Realty · agent side'},
    {h:'lead-inbox.html',  t:'Lead inbox',         i:'rows'},
    {h:'campaigns.html',   t:'Campaigns',          i:'chart'},
    {sec:'Zentra Project · developer side'},
    {h:'booking-new.html',   t:'New booking (E-Form)', i:'file'},
    {h:'booking-status.html',t:'Booking pipeline',     i:'board'},
    {h:'calculators.html',   t:'Calculator suite',     i:'sum'}
  ];
  const here = (location.pathname.split('/').pop() || 'index.html');
  const host = document.getElementById('znav');
  if(!host) return;

  let html = '<div class="brand"><div class="mark"><img src="assets/zr-mark.png" alt="Zentra" width="34" height="34"></div>'
    + '<div><b>Zentra F1 preview</b><small>Realty &times; Project &middot; sample data</small></div></div><nav class="nav">';
  N.forEach(n => {
    if(n.sec){ html += '<div class="sec">' + n.sec + '</div>'; return; }
    const on = (n.h === here) || (here === '' && n.h === 'index.html');
    html += '<a href="' + n.h + '"' + (on ? ' class="on"' : '') + '><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' + I[n.i] + '</svg><span>' + n.t + '</span></a>';
  });
  html += '</nav><div class="foot">PREVIEW &middot; prototype, sample data only<br>Not for production use<br>Zentra Property Group &copy; 2026</div>';
  html += '<button class="theme-toggle" id="themeBtn" type="button">Light / dark</button>';
  host.innerHTML = html;

  const btn = document.createElement('button');
  btn.className = 'burger'; btn.setAttribute('aria-label', 'Menu');
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  document.body.appendChild(btn);
  const ov = document.createElement('div'); ov.className = 'overlay'; document.body.appendChild(ov);
  const close = () => { host.classList.remove('open'); ov.classList.remove('on'); };
  btn.onclick = () => { host.classList.toggle('open'); ov.classList.toggle('on'); };
  ov.onclick = close;
  host.addEventListener('click', e => { if(e.target.closest('a')) close(); });

  const tb = document.getElementById('themeBtn');
  if(tb) tb.onclick = () => {
    const light = document.documentElement.classList.toggle('theme-light');
    try { localStorage.setItem('zr-theme', light ? 'light' : 'dark'); } catch(e){}
  };
})();
(function(){
  try {
    const q = new URLSearchParams(location.search).get('theme');
    const t = q || localStorage.getItem('zr-theme') || 'dark';
    if(t === 'light') document.documentElement.classList.add('theme-light');
  } catch(e){}
})();
