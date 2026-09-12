// Tapis kad projek baharu (halaman /projek-baharu.html)
(function(){
  var btns=document.querySelectorAll('#pjFilters button'), cards=document.querySelectorAll('.pjc');
  if(!btns.length) return;
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(x){x.classList.remove('on');}); b.classList.add('on');
    var f=b.getAttribute('data-f');
    cards.forEach(function(c){
      var ok=(f==='semua')||c.getAttribute('data-negeri')===f||c.getAttribute('data-status').indexOf(f)===0;
      c.style.display=ok?'':'none';
    });
  });});
})();
