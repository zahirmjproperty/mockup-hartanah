/* nav.js — navigasi ZENTRA CONTACT (Pola A: sidebar). Ikon SVG + keadaan aktif + menu mudah alih.
   Fasa 0 mock-up. Tiada data sebenar — lihat assets/contact-data.js (SINTETIK). */
(function () {
  var I = {
    dash: '<path d="M3 10.6 12 3l9 7.6V21H3z"/><path d="M9 21v-6h6v6"/>',
    users: '<circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><path d="M16 5.5a3 3 0 0 1 0 5.8"/><path d="M17.5 20a6 6 0 0 0-2-4.5"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    board: '<path d="M3 4h18v12H3z"/><path d="M8 20h8M12 16v4"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.4 2"/>',
    copy: '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>',
    swap: '<path d="M4 8h13l-3.2-3.2M20 16H7l3.2 3.2"/>',
    cog: '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v2.4M12 18.8v2.4M4.6 7.2l2 1.2M17.4 15.6l2 1.2M4.6 16.8l2-1.2M17.4 8.4l2-1.2"/>',
    shield: '<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
    grid: '<circle cx="7.5" cy="7.5" r="2.2"/><circle cx="16.5" cy="7.5" r="2.2"/><circle cx="7.5" cy="16.5" r="2.2"/><circle cx="16.5" cy="16.5" r="2.2"/>'
  };
  var N = [
    { sec: 'Contacts' },
    { h: 'index.html', t: 'Dashboard', i: 'dash' },
    { h: 'contacts.html', t: 'All contacts', i: 'users' },
    { h: 'new-contact.html', t: 'Add contact', i: 'plus' },
    { sec: 'Pipeline' },
    { h: 'pipeline.html', t: 'Kanban pipeline', i: 'board' },
    { h: 'reminders.html', t: 'Reminders & tasks', i: 'clock' },
    { sec: 'Data quality' },
    { h: 'duplicates.html', t: 'Duplicate review', i: 'copy' },
    { h: 'import-export.html', t: 'Import / export', i: 'swap' },
    { sec: 'Governance' },
    { h: 'pdpa.html', t: 'PDPA & consent', i: 'shield' },
    { h: 'audit.html', t: 'Audit trail', i: 'grid' },
    { h: 'settings.html', t: 'Settings', i: 'cog' }
  ];
  var here = (location.pathname.split('/').pop() || 'index.html');
  var host = document.getElementById('znav');
  if (!host) return;
  var html = '<div class="brand"><div class="mark"><img src="assets/contact-mark.png" alt="ZENTRA Contact" width="32" height="32"></div>' +
    '<div><b>ZENTRA Contact</b><small>Zentra Property Group</small></div></div><nav class="nav">';
  N.forEach(function (n) {
    if (n.sec) { html += '<div class="sec">' + n.sec + '</div>'; return; }
    var on = (n.h === here) || (here === '' && n.h === 'index.html');
    html += '<a href="' + n.h + '"' + (on ? ' class="on"' : '') + '><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' +
      I[n.i] + '</svg><span>' + n.t + '</span></a>';
  });
  html += '</nav><div class="foot">Prototype &middot; sample data only<br>Zentra Property Group &copy; 2026</div>';
  host.innerHTML = html;

  /* menu mudah alih */
  var btn = document.createElement('button');
  btn.className = 'burger'; btn.setAttribute('aria-label', 'Menu');
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  document.body.appendChild(btn);
  var ov = document.createElement('div'); ov.className = 'overlay'; document.body.appendChild(ov);
  function close() { host.classList.remove('open'); ov.classList.remove('on'); }
  btn.onclick = function () { host.classList.toggle('open'); ov.classList.toggle('on'); };
  ov.onclick = close;
  host.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
})();

/* ---- Tema (dark lalai, pilihan light) ---- */
(function () {
  var KEY = 'zc-theme', html = document.documentElement;
  var SUN = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>';
  var MOON = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>';
  function apply(mode) {
    if (mode === 'light') { html.classList.add('theme-light'); } else { html.classList.remove('theme-light'); }
    var b = document.getElementById('zcThemeBtn');
    if (b) { b.setAttribute('aria-label', mode === 'light' ? 'Switch to dark theme' : 'Switch to light theme'); b.innerHTML = mode === 'light' ? SUN : MOON; }
  }
  var mode = localStorage.getItem(KEY) || 'dark';
  if (location.search.indexOf('theme=light') > -1) mode = 'light';
  apply(mode);
  function build() {
    var b = document.createElement('button');
    b.id = 'zcThemeBtn'; b.className = 'zc-theme-btn'; b.type = 'button';
    b.onclick = function () {
      mode = html.classList.contains('theme-light') ? 'dark' : 'light';
      localStorage.setItem(KEY, mode); apply(mode);
    };
    var host = document.querySelector('#sidebar .foot') || document.querySelector('#sidebar') || document.body;
    host.appendChild(b);
    var st = document.createElement('style');
    st.textContent = '.zc-theme-btn{margin-top:10px;display:inline-flex;align-items:center;gap:7px;padding:7px 11px;border-radius:10px;cursor:pointer;font:inherit;font-size:12px;font-weight:600;background:rgba(201,162,39,.10);color:#e8ce86;border:1px solid rgba(201,162,39,.24)}' +
      '.zc-theme-btn:hover{background:rgba(201,162,39,.18)}';
    document.head.appendChild(st);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();

/* ---- Lapisan tindakan demo: setiap kawalan memberi maklum balas JUJUR (toast).
   Tiada tindakan sebenar dilakukan — ini prototaip. ---- */
(function () {
  var PETA = [
    [/^(save|update|create)/i, 'Would save this record and write an entry to the audit trail.', null],
    [/^(export|download)/i, 'Would download a CSV of the current view.', null],
    [/^(import|upload)/i, 'Opens the file picker. (Prototype: no file is stored.)', null],
    [/^(merge)/i, 'Would merge the two records, keeping the primary and archiving the duplicate.', 'contacts.html'],
    [/^(dismiss|ignore)/i, 'Would mark this duplicate pair as not-a-match and remember the decision.', null],
    [/^(send|remind|email|whatsapp|call)/i, 'Would open the channel and log the interaction on the timeline.', null],
    [/^(delete|archive)/i, 'Would soft-delete the record. Nothing is removed in the prototype.', null],
    [/^(add|new)/i, 'Would open the add form.', 'new-contact.html'],
    [/^(run|scan|check)/i, 'Would run the check against the live database and report the result.', null],
    [/^(view|open|detail)/i, 'Opens the related record.', null]
  ];
  function toast(teks, label, href) {
    var t = document.getElementById('demoToast');
    if (!t) {
      t = document.createElement('div'); t.id = 'demoToast'; t.className = 'dtoast';
      t.setAttribute('role', 'status'); document.body.appendChild(t);
    }
    t.innerHTML = '<b>Demo action</b><span>' + (label ? '&ldquo;' + label + '&rdquo; &mdash; ' : '') + teks + '</span>' +
      (href ? '<a href="' + href + '">Open the related page &rarr;</a>' : '') +
      '<i>Prototype only &middot; sample data &middot; no real change is made.</i>';
    t.classList.add('on');
    clearTimeout(window.__dtoast);
    window.__dtoast = setTimeout(function () { t.classList.remove('on'); }, 5000);
  }
  document.addEventListener('click', function (e) {
    var el = e.target.closest('button, a.btn, .btn, .filter-btn, .kcard');
    if (!el) { return; }
    if (el.closest('#demoToast')) { return; }
    if (el.id === 'zcThemeBtn' || el.closest('#sidebar') || el.closest('.foot')) { return; }
    if (el.classList.contains('tab')) { return; }
    if (el.classList.contains('filter-btn')) { return; }
    if (el.tagName === 'A' && el.getAttribute('href')) { return; }
    if (el.hasAttribute('onclick') || el.hasAttribute('data-demo-ignore')) { return; }
    var label = (el.textContent || '').replace(/\s+/g, ' ').trim();
    if (!label || label.length > 46) { return; }
    var mesej = 'This is a prototype control &mdash; the live system runs the real action here.', href = null;
    for (var i = 0; i < PETA.length; i++) {
      if (PETA[i][0].test(label)) { mesej = PETA[i][1]; href = PETA[i][2]; break; }
    }
    toast(mesej, label, href);
  }, true);
})();
