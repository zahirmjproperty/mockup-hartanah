/* Halaman Butiran Projek v2 — galeri + lightbox + pelan unit + video facade */
(function () {
  /* ---------- galeri: tapis kategori ---------- */
  var tabs = document.querySelectorAll('.p2-tabs button');
  var figs = document.querySelectorAll('.p2-gal figure');
  tabs.forEach(function (b) {
    b.addEventListener('click', function () {
      tabs.forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      var c = b.getAttribute('data-cat');
      figs.forEach(function (f) {
        f.style.display = (c === 'semua' || f.getAttribute('data-cat') === c) ? '' : 'none';
      });
    });
  });

  /* ---------- lightbox ---------- */
  var lb = document.getElementById('p2lb');
  if (lb) {
    var img = lb.querySelector('img'), cap = lb.querySelector('.cap');
    var list = [], idx = 0;
    function refill() {
      list = Array.prototype.slice.call(document.querySelectorAll('.p2-gal figure'))
        .filter(function (f) { return f.style.display !== 'none'; });
    }
    function show(i) {
      if (!list.length) return;
      idx = (i + list.length) % list.length;
      var f = list[idx], im = f.querySelector('img');
      img.src = im.getAttribute('data-full') || im.src;
      img.alt = im.alt || '';
      cap.textContent = (f.getAttribute('data-cap') || '') + '  ·  ' + (idx + 1) + '/' + list.length;
    }
    document.querySelectorAll('.p2-gal figure').forEach(function (f) {
      f.addEventListener('click', function () { refill(); show(list.indexOf(f)); lb.classList.add('on'); });
    });
    lb.querySelector('.x').onclick = function () { lb.classList.remove('on'); lb.classList.remove('zoom'); };
    lb.querySelector('.prev').onclick = function (e) { e.stopPropagation(); show(idx - 1); };
    lb.querySelector('.next').onclick = function (e) { e.stopPropagation(); show(idx + 1); };
    lb.querySelector('.zin').onclick = function (e) { e.stopPropagation(); lb.classList.add('zoom'); };
    lb.querySelector('.zout').onclick = function (e) { e.stopPropagation(); lb.classList.remove('zoom'); };
    img.onclick = function (e) { e.stopPropagation(); lb.classList.toggle('zoom'); };
    lb.onclick = function () { lb.classList.remove('on'); lb.classList.remove('zoom'); };
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('on')) return;
      if (e.key === 'Escape') { lb.classList.remove('on'); lb.classList.remove('zoom'); }
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
      if (e.key === '+') lb.classList.add('zoom');
      if (e.key === '-') lb.classList.remove('zoom');
    });
  }

  /* ---------- pelan unit explorer ---------- */
  var plan = document.getElementById('p2plan');
  if (plan) {
    var stage = plan.querySelector('.stage img'), meta = plan.querySelector('.meta');
    var data = JSON.parse(plan.getAttribute('data-plan') || '[]');
    var cur = 0, scale = 1;
    function render() {
      var d = data[cur] || {};
      stage.src = d.img; stage.alt = d.judul || '';
      stage.style.transform = 'scale(' + scale + ')';
      meta.innerHTML = '<b>' + (d.judul || '') + '</b>' + (d.info ? ' · ' + d.info : '');
      plan.querySelectorAll('.list button').forEach(function (b, i) { b.classList.toggle('on', i === cur); });
      var dl = plan.querySelector('.dl'); if (dl) dl.href = d.img;
    }
    plan.querySelectorAll('.list button').forEach(function (b, i) {
      b.addEventListener('click', function () { cur = i; scale = 1; render(); });
    });
    plan.querySelector('.zin').onclick = function () { scale = Math.min(4, scale + 0.4); render(); };
    plan.querySelector('.zout').onclick = function () { scale = Math.max(1, scale - 0.4); render(); };
    plan.querySelector('.reset').onclick = function () { scale = 1; render(); };
    render();
  }

  /* ---------- video facade (lazy YouTube) ---------- */
  document.querySelectorAll('.p2-vid .frame').forEach(function (f) {
    f.addEventListener('click', function () {
      var id = f.getAttribute('data-yt');
      var w = document.createElement('iframe');
      w.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      w.setAttribute('title', f.getAttribute('data-tajuk') || 'Video projek');
      w.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
      w.setAttribute('allowfullscreen', '');
      w.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border:0';
      f.innerHTML = '';
      f.appendChild(w);
    }, { once: true });
  });

  /* ---------- masterplan pin tooltip (klik pada telefon) ---------- */
  document.querySelectorAll('.mp .pin').forEach(function (p) {
    p.addEventListener('click', function (e) { e.stopPropagation(); p.classList.toggle('on'); });
  });
})();
