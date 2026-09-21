/* ============================================================================
   ZENTRA HUB SWITCHER (JS) — v20260922
   Fail kongsi: dipasang pada setiap sistem Zentra yang LIVE supaya pengguna
   boleh melompat antara sistem tanpa menaip URL.

   Reka bentuk sengaja TIDAK menyentuh struktur HTML mana-mana sistem:
     - ia menyuntik satu "pil" terapung di penjuru bawah kiri
     - klik pil -> panel senarai sistem terbuka
     - sistem semasa ditanda "You are here"

   Sebab pil terapung (bukan pautan dalam header): kelima-lima sistem mempunyai
   header BERBEZA (topbar .zux-top, header.site, sidebar .side). Pil terapung
   tiada risiko susun atur, dan selamat pada skrin 415px.

   Nota penting: setiap kawalan di sini mesti ada `data-demo-ignore`
   supaya lapisan zentra-ui.js (toast "Demo action") tidak merampas klik.
   ========================================================================== */
(function () {
  'use strict';
  if (window.__zentraHubSwitcher) { return; }
  window.__zentraHubSwitcher = true;

  /* ---------- DESTINASI ---------------------------------------------------- */
  /* Hanya sistem yang BENAR-BENAR hidup disenaraikan. Tiada pautan ke salinan
     arkib mock-up — itu yang menyebabkan dashboard salah label sebelum ini. */
  var SISTEM = [
    { host: 'asset.zentrapropertygroup.com',  nama: 'Zentra Asset',
      nota: 'Managed portfolio operations', href: 'https://asset.zentrapropertygroup.com/' },
    { host: 'launch.zentrapropertygroup.com', nama: 'Zentra Launch',
      nota: 'New project sales',            href: 'https://launch.zentrapropertygroup.com/' },
    { host: 'push.zentrapropertygroup.com',   nama: 'Zentra Push',
      nota: 'Listing distribution',         href: 'https://push.zentrapropertygroup.com/' },
    { host: 'realty.zentrapropertygroup.com', nama: 'Zentra Realty',
      nota: 'Agency and agent operations',  href: 'https://realty.zentrapropertygroup.com/' },
    { host: 'legal.zentrapropertygroup.com',  nama: 'Zentra Legal',
      nota: 'Conveyancing and matters',     href: 'https://legal.zentrapropertygroup.com/' }
  ];

  /* ---------- GAYA (disuntik sendiri) ------------------------------------- */
  var CSS = ''
  + '.zhs-pil,.zhs-panel,.zhs-panel *{box-sizing:border-box}'
  + '.zhs-pil{position:fixed;left:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));'
  +   'z-index:80;display:inline-flex;align-items:center;gap:8px;padding:9px 14px 9px 11px;'
  +   'font:600 13px/1.1 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;letter-spacing:.02em;'
  +   'color:#e8ce86;background:#0b1b2e;border:1px solid rgba(201,162,39,.55);border-radius:999px;'
  +   'cursor:pointer;box-shadow:0 6px 22px rgba(7,17,32,.42);transition:transform .16s,box-shadow .16s}'
  + '.zhs-pil:hover{transform:translateY(-1px);box-shadow:0 10px 26px rgba(7,17,32,.5)}'
  + '.zhs-pil:focus-visible{outline:2px solid #c9a227;outline-offset:2px}'
  + '.zhs-pil .zhs-mark{width:20px;height:20px;flex:0 0 20px;border-radius:6px;'
  +   'background:linear-gradient(145deg,#e8ce86,#c9a227 55%,#9a7a2e);color:#0b1b2e;'
  +   'font:800 10px/20px system-ui,sans-serif;text-align:center}'
  + '.zhs-pil .zhs-caret{opacity:.8;font-size:10px;transition:transform .16s}'
  + '.zhs-pil[aria-expanded="true"] .zhs-caret{transform:rotate(180deg)}'

  + '.zhs-panel{position:fixed;left:16px;bottom:calc(62px + env(safe-area-inset-bottom,0px));z-index:81;'
  +   'width:min(330px,92vw);padding:14px;border-radius:16px;'
  +   'background:#0b1b2e;border:1px solid rgba(201,162,39,.4);'
  +   'box-shadow:0 18px 48px rgba(7,17,32,.55);color:#c7d1dc;'
  +   'font:400 13px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
  +   'opacity:0;visibility:hidden;transform:translateY(8px);'
  /* PENTING: 'visibility' mesti bertukar SERTA-MERTA (lengah 0s), bukan dianimasikan.
     Jika ia diletak dalam peralihan, ia kekal 'hidden' pada bingkai pembukaan dan
     pautan di dalam panel TIDAK boleh menerima fokus — pengguna papan kekunci
     tersangkut di luar panel. Jadi: buka = 0s, tutup = 0.16s (supaya pudar kelihatan). */
  +   'transition:opacity .16s,transform .16s,visibility 0s linear .16s}'
  + '.zhs-panel.on{opacity:1;visibility:visible;transform:translateY(0);'
  +   'transition:opacity .16s,transform .16s,visibility 0s linear 0s}'
  + '.zhs-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;margin:0 0 10px}'
  + '.zhs-head b{display:block;color:#fff;font-size:14px;line-height:1.2}'
  + '.zhs-head small{display:block;color:#8c9fb4;font-size:11.5px;margin-top:2px}'
  + '.zhs-x{flex:0 0 auto;width:26px;height:26px;border-radius:8px;cursor:pointer;'
  +   'background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);color:#c7d1dc;'
  +   'font:400 15px/1 system-ui,sans-serif}'
  + '.zhs-x:hover{background:rgba(255,255,255,.12);color:#fff}'
  + '.zhs-x:focus-visible{outline:2px solid #c9a227;outline-offset:2px}'
  + '.zhs-list{display:flex;flex-direction:column;gap:4px;margin:0;padding:0;list-style:none}'
  + '.zhs-list a{display:block;padding:9px 10px;border-radius:10px;text-decoration:none;'
  +   'color:#c7d1dc;border:1px solid transparent}'
  + '.zhs-list a:hover{background:rgba(201,162,39,.1);border-color:rgba(201,162,39,.35);color:#fff}'
  + '.zhs-list a:focus-visible{outline:2px solid #c9a227;outline-offset:2px}'
  + '.zhs-list a b{display:block;font-weight:600;font-size:13px;color:#fff}'
  + '.zhs-list a small{display:block;font-size:11.5px;color:#8c9fb4;margin-top:1px}'
  + '.zhs-now{display:inline-block;margin-left:6px;padding:1px 6px;border-radius:999px;'
  +   'background:rgba(201,162,39,.16);border:1px solid rgba(201,162,39,.5);'
  +   'color:#e8ce86;font-size:10px;font-weight:600;vertical-align:1px}'
  + '.zhs-foot{margin:10px 0 0;padding-top:9px;border-top:1px solid rgba(255,255,255,.1);'
  +   'color:#8c9fb4;font-size:11px}'

  /* tema cerah: ikut corak sistem (html[data-theme="light"]), plus fallback OS */
  + 'html[data-theme="light"] .zhs-pil{color:#8a6d20;background:#fff;border-color:#e2e8f0;'
  +   'box-shadow:0 6px 20px rgba(11,27,46,.14)}'
  + 'html[data-theme="light"] .zhs-pil .zhs-mark{color:#fff}'
  + 'html[data-theme="light"] .zhs-panel{background:#fff;border-color:#e2e8f0;color:#39506a;'
  +   'box-shadow:0 18px 44px rgba(11,27,46,.18)}'
  + 'html[data-theme="light"] .zhs-head b,html[data-theme="light"] .zhs-list a b{color:#0b1b2e}'
  + 'html[data-theme="light"] .zhs-head small,html[data-theme="light"] .zhs-list a small,'
  + 'html[data-theme="light"] .zhs-foot{color:#5f6b7a}'
  + 'html[data-theme="light"] .zhs-list a{color:#39506a}'
  + 'html[data-theme="light"] .zhs-list a:hover{background:rgba(11,27,46,.04);border-color:#e2e8f0;color:#0b1b2e}'
  + 'html[data-theme="light"] .zhs-x{background:#f5f7f9;border-color:#e2e8f0;color:#39506a}'
  + 'html[data-theme="light"] .zhs-foot{border-top-color:#e2e8f0}';

  function suntikGaya() {
    if (document.getElementById('zhsStyle')) { return; }
    var s = document.createElement('style');
    s.id = 'zhsStyle';
    s.appendChild(document.createTextNode(CSS));
    document.head.appendChild(s);
  }

  /* ---------- BINA WIDGET -------------------------------------------------- */
  var panel, pil;

  function hostSemasa() { return location.hostname.replace(/^www\./, ''); }

  function bina() {
    suntikGaya();
    var kini = hostSemasa();

    pil = document.createElement('button');
    pil.type = 'button';
    pil.className = 'zhs-pil';
    pil.setAttribute('data-demo-ignore', '');   /* elak toast lapisan demo */
    pil.setAttribute('aria-expanded', 'false');
    pil.setAttribute('aria-controls', 'zhsPanel');
    pil.setAttribute('aria-label', 'Switch between Zentra systems');
    pil.innerHTML = '<span class="zhs-mark">Z</span><span>Zentra systems</span>'
                  + '<span class="zhs-caret">&#9650;</span>';

    panel = document.createElement('div');
    panel.className = 'zhs-panel';
    panel.id = 'zhsPanel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Zentra systems');
    panel.setAttribute('data-demo-ignore', '');

    var senarai = SISTEM.map(function (s) {
      var sini = (s.host === kini);
      /* data-demo-ignore pada SETIAP pautan: lapisan zentra-ui.js menyemak atribut
         pada elemen yang DIKLIK, bukan pada ibu bapa — jadi atribut pada bekas
         panel tidak melindungi apa-apa. Setiap kawalan mesti menandanya sendiri. */
      return '<li><a data-demo-ignore href="' + s.href + '"' + (sini ? ' aria-current="true"' : '') + '>'
           + '<b>' + s.nama + (sini ? '<span class="zhs-now">You are here</span>' : '') + '</b>'
           + '<small>' + s.nota + '</small></a></li>';
    }).join('');

    panel.innerHTML = '<div class="zhs-head"><div><b>Zentra systems</b>'
      + '<small>' + SISTEM.length + ' live systems</small></div>'
      + '<button type="button" class="zhs-x" data-demo-ignore aria-label="Close">&times;</button></div>'
      + '<ul class="zhs-list">' + senarai + '</ul>'
      + '<p class="zhs-foot">Internal systems. Sample data only &mdash; no customer records.</p>';

    document.body.appendChild(pil);
    document.body.appendChild(panel);

    pil.addEventListener('click', function () { togol(panel.className.indexOf('on') < 0); });
    panel.querySelector('.zhs-x').addEventListener('click', function () { togol(false); });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.className.indexOf('on') >= 0) { togol(false); }
    });
    document.addEventListener('click', function (e) {
      if (panel.className.indexOf('on') < 0) { return; }
      if (e.target.closest && (e.target.closest('.zhs-panel') || e.target.closest('.zhs-pil'))) { return; }
      togol(false);
    });
  }

  function togol(buka) {
    panel.className = 'zhs-panel' + (buka ? ' on' : '');
    pil.setAttribute('aria-expanded', String(!!buka));
    if (buka) {
      /* Panel masih 'visibility:hidden' pada bingkai ini (peralihan CSS belum
         selesai), dan unsur tersembunyi TIDAK boleh menerima fokus. Jadi kita
         paksa reflow dahulu, barulah fokus — jika tidak, fokus kekal di BODY
         dan pengguna papan kekunci tersangkut di luar panel. */
      void panel.offsetHeight;
      var pindah = function () {
        var a = panel.querySelector('.zhs-list a[aria-current="true"]') || panel.querySelector('.zhs-list a');
        if (a) { a.focus({ preventScroll: true }); }
      };
      if (window.requestAnimationFrame) { window.requestAnimationFrame(pindah); } else { setTimeout(pindah, 0); }
    }
  }

  function boot() { try { bina(); } catch (e) { /* jangan sekali-kali pecahkan halaman hos */ } }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', boot); } else { boot(); }
})();
