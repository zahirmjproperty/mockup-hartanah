/* tema dimuatkan awal supaya tiada kelipan putih */
(function(){
  try{
    var t = location.search.indexOf('theme=light') > -1 ? 'light'
          : (localStorage.getItem('zp-theme') || 'dark');
    if(t === 'light') document.documentElement.classList.add('theme-light');
  }catch(e){}
})();
