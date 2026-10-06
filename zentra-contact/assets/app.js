/* app.js — logik kongsi ZENTRA CONTACT F0. Membaca window.ZC.CONTACTS (fixture SINTETIK).
   Satu sumber kebenaran: semua halaman mengira KPI dari senarai yang SAMA. */
(function () {
  var C = (window.ZC && window.ZC.CONTACTS) || [];
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var STATUS_ORDER = ['New', 'Contacted', 'Qualified', 'Viewing', 'Negotiation', 'Closed – Won', 'Closed – Lost', 'Nurture'];
  var STATUS_CLS = {
    'New': 'b-new', 'Contacted': 'b-contact', 'Qualified': 'b-qual', 'Viewing': 'b-view',
    'Negotiation': 'b-nego', 'Closed – Won': 'b-won', 'Closed – Lost': 'b-lost', 'Nurture': 'b-nurture'
  };

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function primaryPhone(c) {
    var p = (c.phones || []).filter(function (x) { return x.utama; })[0] || (c.phones || [])[0];
    return p ? p.nilai : '';
  }
  function primaryEmail(c) {
    var e = (c.emails || []).filter(function (x) { return x.utama; })[0] || (c.emails || [])[0];
    return e ? e.nilai : '';
  }
  function waLink(tel) { return 'https://wa.me/6' + String(tel).replace(/[^0-9]/g, ''); }
  function statusBadge(s) { return '<span class="badge ' + (STATUS_CLS[s] || 'b-nurture') + '">' + esc(s) + '</span>'; }
  function tagsHtml(t) { return (t || []).map(function (x) {
    return '<span class="tag' + (x === 'VIP' ? ' vip' : '') + '">' + esc(x) + '</span>'; }).join(''); }
  function initials(n) { return (n || '').split(/\s+/).slice(0, 2).map(function (w) { return w[0] || ''; }).join('').toUpperCase(); }
  function consentFlag(c) { return c.consent
    ? '<span class="flag ok">Consented</span>' : '<span class="flag no">No consent</span>'; }
  function dueFlag(c) { return c.nextFollowUpAt
    ? '<span class="flag due">' + esc(c.nextFollowUpAt) + '</span>' : '<span style="color:#7d8fa6">—</span>'; }

  /* ---- KPI (dikira dari satu senarai) ---- */
  function kpi() {
    var now = '2026-10-06';
    return {
      total: C.length,
      people: C.filter(function (c) { return c.kind === 'person'; }).length,
      orgs: C.filter(function (c) { return c.kind === 'organization'; }).length,
      newThisWeek: C.filter(function (c) { return c.createdAt >= '2026-09-29'; }).length,
      dueToday: C.filter(function (c) { return c.nextFollowUpAt && c.nextFollowUpAt <= '2026-10-06'; }).length,
      overdue: C.filter(function (c) { return c.nextFollowUpAt && c.nextFollowUpAt < now; }).length,
      noConsent: C.filter(function (c) { return !c.consent; }).length,
      active: C.filter(function (c) { return ['Negotiation', 'Viewing', 'Qualified'].indexOf(c.status) > -1; }).length,
      won: C.filter(function (c) { return c.status === 'Closed – Won'; }).length
    };
  }

  /* ---- Jadual: bina baris + tapis ---- */
  function tableRows(list) {
    return list.map(function (c) {
      var tel = primaryPhone(c), em = primaryEmail(c);
      return '<tr>' +
        '<td data-l="Name"><a href="contact.html?id=' + esc(c.id) + '">' + esc(c.fullName) + '</a>' +
          (c.kind === 'organization' ? ' <span class="tag">Org</span>' : '') + '</td>' +
        '<td data-l="Roles">' + esc((c.roles || []).join(', ')) + '</td>' +
        '<td data-l="Phone" class="tel">' + (tel ? '<a href="tel:' + esc(tel) + '">' + esc(tel) + '</a>' : '—') + '</td>' +
        '<td data-l="Email">' + esc(em) + '</td>' +
        '<td data-l="Area">' + esc((c.preferredArea || []).join(', ')) + '</td>' +
        '<td data-l="Status">' + statusBadge(c.status) + '</td>' +
        '<td data-l="Tags">' + tagsHtml(c.tags) + '</td>' +
        '<td data-l="Follow-up">' + dueFlag(c) + '</td>' +
        '<td data-l="Consent">' + consentFlag(c) + '</td>' +
        '<td data-l="Action"><a class="btn small ghost" href="contact.html?id=' + esc(c.id) + '">View</a></td>' +
        '</tr>';
    }).join('');
  }

  function initContactsPage() {
    var tb = $('#rows'); if (!tb) return;
    var q = '', role = 'All', status = 'All', tagf = 'All', consent = 'All';
    var roles = ['All'].concat(uniq(C.map(function (c) { return c.roles; })));
    var tags = ['All'].concat(uniq(C.map(function (c) { return c.tags; })));
    var selR = $('#fRole'), selS = $('#fStatus'), selT = $('#fTag'), selC = $('#fConsent');
    if (selR) selR.innerHTML = roles.map(opt).join('');
    if (selS) selS.innerHTML = ['All'].concat(STATUS_ORDER).map(opt).join('');
    if (selT) selT.innerHTML = tags.map(opt).join('');
    function opt(v) { return '<option value="' + esc(v) + '">' + esc(v) + '</option>'; }

    function apply() {
      var list = C.filter(function (c) {
        var hay = [c.fullName, c.nickname, c.company, primaryPhone(c), primaryEmail(c),
                   (c.roles || []).join(' '), (c.tags || []).join(' '), (c.preferredArea || []).join(' ')].join(' ').toLowerCase();
        if (q && hay.indexOf(q) === -1) return false;
        if (role !== 'All' && (c.roles || []).indexOf(role) === -1) return false;
        if (status !== 'All' && c.status !== status) return false;
        if (tagf !== 'All' && (c.tags || []).indexOf(tagf) === -1) return false;
        if (consent === 'No consent only' && c.consent) return false;
        if (consent === 'Consented only' && !c.consent) return false;
        return true;
      });
      tb.innerHTML = list.length ? tableRows(list) : '';
      var em = $('#empty'); if (em) em.style.display = list.length ? 'none' : 'block';
      var cnt = $('#count'); if (cnt) cnt.textContent = list.length + ' of ' + C.length + ' contacts';
    }
    var si = $('#q'); if (si) si.addEventListener('input', function () { q = this.value.trim().toLowerCase(); apply(); });
    if (selR) selR.addEventListener('change', function () { role = this.value; apply(); });
    if (selS) selS.addEventListener('change', function () { status = this.value; apply(); });
    if (selT) selT.addEventListener('change', function () { tagf = this.value; apply(); });
    if (selC) selC.addEventListener('change', function () { consent = this.value; apply(); });
    apply();
  }
  function uniq(arrs) {
    var s = {}; arrs.forEach(function (a) { (a || []).forEach(function (x) { s[x] = 1; }); });
    return Object.keys(s).sort();
  }

  /* ---- Kanban ---- */
  function initPipeline() {
    var host = $('#kanban'); if (!host) return;
    host.innerHTML = STATUS_ORDER.map(function (st) {
      var list = C.filter(function (c) { return c.status === st; });
      return '<div class="kcol"><h3>' + esc(st) + '<span>' + list.length + '</span></h3>' +
        list.map(function (c) {
          var budget = c.budgetMax ? 'RM ' + (c.budgetMax / 1000).toFixed(0) + 'k' : '';
          return '<div class="kcard"><div class="kn">' + esc(c.fullName) + '</div>' +
            '<div class="km">' + esc((c.roles || []).join(', ')) + '</div>' +
            (budget ? '<div class="kv">' + budget + '</div>' : '') +
            '<div class="km">' + esc(c.agent || '') + '</div></div>';
        }).join('') + '</div>';
    }).join('');
  }

  /* ---- Dashboard ---- */
  function initDashboard() {
    var k = kpi();
    $$('[data-kpi]').forEach(function (el) { var v = k[el.dataset.kpi]; if (v != null) el.textContent = v; });
    var recent = $('#recent'); if (recent) {
      recent.innerHTML = C.slice(0, 6).map(function (c) {
        return '<tr><td data-l="Name"><a href="contact.html?id=' + esc(c.id) + '">' + esc(c.fullName) + '</a></td>' +
          '<td data-l="Status">' + statusBadge(c.status) + '</td>' +
          '<td data-l="Agent">' + esc(c.agent) + '</td>' +
          '<td data-l="Created">' + esc(c.createdAt) + '</td></tr>';
      }).join('');
    }
    var due = $('#dueList'); if (due) {
      var d = C.filter(function (c) { return c.nextFollowUpAt; }).sort(function (a, b) {
        return a.nextFollowUpAt < b.nextFollowUpAt ? -1 : 1; }).slice(0, 6);
      due.innerHTML = d.map(function (c) {
        return '<tr><td data-l="Name"><a href="contact.html?id=' + esc(c.id) + '">' + esc(c.fullName) + '</a></td>' +
          '<td data-l="Due">' + dueFlag(c) + '</td>' +
          '<td data-l="Status">' + statusBadge(c.status) + '</td></tr>';
      }).join('');
    }
    var pipe = $('#pipeChart'); if (pipe) {
      pipe.innerHTML = STATUS_ORDER.map(function (st) {
        var n = C.filter(function (c) { return c.status === st; }).length;
        var pct = C.length ? Math.round(n / C.length * 100) : 0;
        return '<div style="display:flex;align-items:center;gap:10px;margin-bottom:7px">' +
          '<span style="width:112px;font-size:11.5px;color:#9fb0c4">' + esc(st) + '</span>' +
          '<span style="flex:1;height:9px;border-radius:5px;background:rgba(255,255,255,.07);overflow:hidden">' +
          '<span style="display:block;height:100%;width:' + pct + '%;background:linear-gradient(90deg,#c9a227,#e8ce86)"></span></span>' +
          '<span style="width:26px;text-align:right;font-size:11.5px;color:#e8ce86;font-weight:600">' + n + '</span></div>';
      }).join('');
    }
  }

  /* ---- Profil (contact.html?id=) ---- */
  function initProfile() {
    var host = $('#profile'); if (!host) return;
    var id = (location.search.match(/[?&]id=([^&]+)/) || [])[1];
    var c = C.filter(function (x) { return x.id === id; })[0] || C[0];
    var tel = primaryPhone(c), em = primaryEmail(c);
    $('#pName').textContent = c.fullName;
    $('#pMeta').innerHTML = esc((c.jobTitle || '') + (c.company ? ' · ' + c.company : '') + (c.roles ? ' · ' + c.roles.join(', ') : ''));
    $('#pAvatar').textContent = initials(c.fullName);
    $('#pTags').innerHTML = tagsHtml(c.tags) + ' ' + statusBadge(c.status);
    $('#pActions').innerHTML =
      (tel ? '<a class="btn small primary" href="' + waLink(tel) + '" target="_blank" rel="noopener">WhatsApp</a>' +
             '<a class="btn small" href="tel:' + esc(tel) + '">Call</a>' : '') +
      (em ? '<a class="btn small ghost" href="mailto:' + esc(em) + '">Email</a>' : '') +
      '<a class="btn small ghost" href="new-contact.html?id=' + esc(c.id) + '">Edit</a>' +
      '<button class="btn small danger">Archive</button>';
    $('#pKv').innerHTML = [
      ['ID', c.id], ['Kind', c.kind === 'organization' ? 'Organization' : 'Person'],
      ['IC no.', c.ic ? '<span class="flag ok">Encrypted at rest</span> ' + esc(c.ic.replace(/-\d{4}$/, '-••••')) : '—'],
      ['TIN', c.tin ? esc(c.tin.replace(/\d{4}$/, '••••')) : '—'],
      ['REN no.', c.renNumber || '—'],
      ['Phone', tel ? '<a href="tel:' + esc(tel) + '" style="color:#8fd4a8">' + esc(tel) + '</a>' : '—'],
      ['Email', esc(em)],
      ['Area of interest', esc((c.preferredArea || []).join(', '))],
      ['Budget', c.budgetMax ? 'RM ' + c.budgetMin.toLocaleString() + ' – ' + c.budgetMax.toLocaleString() : '—'],
      ['Source', esc(c.source)],
      ['Owner (agent)', esc(c.agent)],
      ['Created', esc(c.createdAt)],
      ['Last contact', esc(c.lastContactAt)],
      ['Next follow-up', dueFlag(c)],
      ['Consent', consentFlag(c) + (c.consentDate ? ' <span style="color:#7d8fa6;font-size:11px">' + esc(c.consentDate) + '</span>' : '')]
    ].map(function (r) { return '<dt>' + r[0] + '</dt><dd>' + r[1] + '</dd>'; }).join('');

    /* timeline interaksi (sintetik, terbit dari rekod) */
    $('#timeline').innerHTML = [
      { t: c.lastContactAt + ' · 10:20', b: 'Phone call — discussed requirements and budget.' },
      { t: c.lastContactAt + ' · 09:05', b: 'WhatsApp follow-up sent from the pipeline card.' },
      { t: c.createdAt + ' · 15:40', b: 'Record created from ' + c.source + ' and assigned to ' + c.agent + '.' }
    ].map(function (a) {
      return '<div class="act"><div class="at">' + esc(a.t) + '</div><div class="ab">' + esc(a.b) + '</div></div>';
    }).join('');

    $('#docs').innerHTML = [
      ['📄', 'NRIC copy', 'Uploaded ' + c.createdAt],
      ['📄', 'Consent form (signed)', c.consent ? 'Uploaded ' + (c.consentDate || c.createdAt) : 'Not on file'],
      ['📄', 'Booking form', 'Sample document — prototype']
    ].map(function (d) {
      return '<div class="doc-row"><span class="di">' + d[0] + '</span><span style="flex:1">' + esc(d[1]) +
        '</span><span style="color:#7d8fa6;font-size:11px">' + esc(d[2]) + '</span></div>';
    }).join('');

    $('#auditRows').innerHTML = [
      ['2026-10-06 09:12', 'Zahir (ZM)', 'Viewed profile (IC/TIN fields masked)'],
      ['2026-10-06 09:05', 'Zahir (ZM)', 'Added interaction — WhatsApp follow-up'],
      ['2026-09-29 15:40', 'System', 'Record created from ' + c.source]
    ].map(function (a) {
      return '<tr><td data-l="Time">' + esc(a[0]) + '</td><td data-l="Actor">' + esc(a[1]) + '</td><td data-l="Action">' + esc(a[2]) + '</td></tr>';
    }).join('');
  }

  /* ---- Duplicates ---- */
  function initDuplicates() {
    var host = $('#dups'); if (!host) return;
    var pair = [C[4], C[5]];
    host.innerHTML = '<div class="card"><h2>Probable duplicate (1 pair)</h2>' +
      '<div class="card-table"><table class="tbl responsive"><thead><tr><th>Field</th><th>Record A</th><th>Record B</th></tr></thead><tbody>' +
      [['ID', pair[0].id, pair[1].id], ['Name', pair[0].fullName, pair[1].fullName],
       ['Phone', primaryPhone(pair[0]), primaryPhone(pair[1])], ['Email', primaryEmail(pair[0]), primaryEmail(pair[1])]]
        .map(function (r) { return '<tr><td data-l="Field">' + esc(r[0]) + '</td><td data-l="Record A">' + esc(r[1]) + '</td><td data-l="Record B">' + esc(r[2]) + '</td></tr>'; }).join('') +
      '</tbody></table></div>' +
      '<div class="actions-row"><button class="btn primary">Merge — keep A</button>' +
      '<button class="btn">Merge — keep B</button>' +
      '<button class="btn ghost">Not a match</button></div>' +
      '<p style="font-size:11.5px;color:#9fb0c4;margin:12px 0 0">Matched on: exact phone number. ' +
      'The live system compares normalised phone, email, and IC — never name alone (names collide).</p></div>';
  }

  /* ---- Reminders ---- */
  function initReminders() {
    var host = $('#reminders'); if (!host) return;
    var d = C.filter(function (c) { return c.nextFollowUpAt; }).sort(function (a, b) {
      return a.nextFollowUpAt < b.nextFollowUpAt ? -1 : 1; });
    host.innerHTML = d.length ? d.map(function (c) {
      var late = c.nextFollowUpAt < '2026-10-06';
      return '<div class="card" style="padding:12px 15px;margin-bottom:10px">' +
        '<div style="display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;align-items:center">' +
        '<div><a href="contact.html?id=' + esc(c.id) + '" style="color:#f2e6c4;font-weight:600;text-decoration:none">' + esc(c.fullName) + '</a>' +
        '<div style="font-size:11.5px;color:#9fb0c4;margin-top:3px">' + esc((c.roles || []).join(', ')) + ' · ' + esc(c.agent) + '</div></div>' +
        '<div style="display:flex;gap:8px;align-items:center">' +
        (late ? '<span class="flag no">Overdue</span>' : '<span class="flag due">Due</span>') +
        '<span style="font-size:11.5px;color:#9fb0c4">' + esc(c.nextFollowUpAt) + '</span>' +
        '<button class="btn small primary">Mark done</button></div></div></div>';
    }).join('') : '<div class="empty">No follow-ups due.</div>';
  }

  /* ---- PDPA ---- */
  function initPdpa() {
    var k = kpi();
    $$('[data-pdpa]').forEach(function (el) { var v = k[el.dataset.pdpa]; if (v != null) el.textContent = v; });
    var host = $('#noConsentList'); if (host) {
      host.innerHTML = C.filter(function (c) { return !c.consent; }).map(function (c) {
        return '<tr><td data-l="Name"><a href="contact.html?id=' + esc(c.id) + '">' + esc(c.fullName) + '</a></td>' +
          '<td data-l="Source">' + esc(c.source) + '</td>' +
          '<td data-l="Created">' + esc(c.createdAt) + '</td>' +
          '<td data-l="Action"><button class="btn small">Record consent</button></td></tr>';
      }).join('');
    }
  }

  function boot() {
    initDashboard(); initContactsPage(); initPipeline(); initProfile();
    initDuplicates(); initReminders(); initPdpa();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
