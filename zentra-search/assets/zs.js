/* ZENTRA Search — demo search console over window.ZS_DATA (synthetic).
   Live wire-up: replace ZS_DATA with `socmed_search.py <platform> "<q>" --json` output. */
(function () {
  var DATA = window.ZS_DATA || [];
  var form = document.getElementById('zs-form');
  var q = document.getElementById('zs-q');
  var chips = document.getElementById('zs-chips');
  var out = document.getElementById('zs-results');
  var meta = document.getElementById('zs-meta');
  var platform = 'all';

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) {
    return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  function match(p) {
    if (platform !== 'all' && p.platform !== platform) return false;
    var term = q.value.trim().toLowerCase();
    if (!term) return true;
    return (p.text + ' ' + p.author + ' ' + (p.tags || []).join(' ')).toLowerCase().indexOf(term) > -1;
  }

  function render() {
    var hits = DATA.filter(match);
    out.innerHTML = hits.length ? hits.map(function (p) {
      return '<article class="zs-card">' +
        '<div class="zs-card-top">' +
          '<span class="zs-src ' + esc(p.platform) + '">' + esc(p.platform) + '</span>' +
          '<span class="zs-author">' + esc(p.author) + '</span>' +
          '<span class="zs-when">' + esc(p.when) + '</span>' +
        '</div>' +
        '<p class="zs-text">' + esc(p.text) + '</p>' +
        '<p>' + (p.tags || []).map(function (t) { return '<span class="zs-tag">#' + esc(t) + '</span>'; }).join(' ') + '</p>' +
      '</article>';
    }).join('') : '<p class="zs-empty">No public posts matched. Widen the platform filter or try a shorter keyword.</p>';

    meta.textContent = 'Showing sample of ' + hits.length + ' public post' + (hits.length === 1 ? '' : 's') +
      ' (synthetic) · platform: ' + platform + (q.value.trim() ? ' · keyword: "' + q.value.trim() + '"' : '') +
      '. No login required.';
  }

  chips.addEventListener('click', function (e) {
    var b = e.target.closest('.zs-chip');
    if (!b) return;
    platform = b.dataset.p;
    [].forEach.call(chips.querySelectorAll('.zs-chip'), function (c) {
      c.setAttribute('aria-pressed', String(c === b));
    });
    render();
  });

  form.addEventListener('submit', function (e) { e.preventDefault(); render(); });
  q.addEventListener('input', render);
  render();
})();
