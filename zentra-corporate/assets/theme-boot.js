// Theme boot - prevent white flash
(function() {
  var t = window.location.search.indexOf('theme=light') > -1
    ? 'light' : localStorage.getItem('za-theme') || 'dark';
  if (t === 'light') document.documentElement.classList.add('theme-light');
})();