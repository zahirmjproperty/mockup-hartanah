/* law-nav.js — Zentra Law sidebar (tema sama Zentra Hub). Vanilla, tiada kebergantungan. */
(function () {
  var NAV = [
    ["Practice", [["index", "Overview", "\u25a3"], ["matters", "Matters", "\u2630"],
                  ["checklist", "Document checklist", "\u2611"], ["documents", "Documents and signing", "\u270e"],
                  ["drafting", "Drafting and vetting", "\u2699"],
                  ["signing", "Signing room", "\u2712"], ["deadlines", "Statutory clock", "\u23f1"]]],
    ["Money", [["fees", "Fee engine", "\u2211"], ["billing", "Billing", "\u0024"],
               ["client-account", "Client account", "\u2696"]]],
    ["Firm", [["portal", "Client portal", "\u25c9"], ["admin", "Firm admin", "\u2699"],
              ["compliance", "Compliance guard", "\u26e8"], ["audit", "Audit trail", "\u29d6"]]],
    ["Plan", [["roadmap", "Roadmap", "\u2691"], ["guide", "Review guide", "\u2691"]]]
  ];
  var page = document.body.getAttribute("data-page") || "index";
  var html = '';
  html += '<div class="brand"><div class="mark">ZL</div><div><b>Zentra Law</b>' +
          '<small>Practice management</small></div></div>';
  html += '<nav class="nav">';
  NAV.forEach(function (group) {
    html += '<div class="sec">' + group[0] + '</div>';
    group[1].forEach(function (item) {
      var on = (item[0] === page) ? ' class="on"' : '';
      html += '<a href="' + item[0] + '.html"' + on + '><span class="ic">' + item[2] + '</span>' + item[1] + '</a>';
    });
  });
  html += '</nav>';
  html += '<div class="foot">Prototype of the Zentra Law practice management system.<br>' +
          'English (US) &middot; sample data only &middot; no database behind these screens.<br><br>' +
          '<a href="../agency-system/index.html">Zentra Hub &rarr;</a></div>';
  var host = document.getElementById('znav');
  if (host) { host.innerHTML = html; }
})();
