/* MOCK-UP Fasa 1 — interaksi kecil (preview sahaja, tiada backend) */
(function(){
  // Tab segmen carian
  document.querySelectorAll('.tabs').forEach(function(g){
    g.addEventListener('click',function(e){
      var b=e.target.closest('.tab'); if(!b) return;
      g.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
      b.classList.add('on');
      var seg=b.dataset.seg;
      document.querySelectorAll('[data-seg-only]').forEach(function(el){
        el.style.display = (seg==='all'||el.dataset.segOnly===seg)?'':'none';
      });
    });
  });

  // Simpan (kegemaran) — localStorage contoh
  try{
    var saved=JSON.parse(localStorage.getItem('mock_saved')||'[]');
    document.querySelectorAll('.save').forEach(function(b){
      var id=b.dataset.id;
      if(saved.indexOf(id)>-1){b.classList.add('on');b.textContent='♥';}
      b.addEventListener('click',function(){
        var i=saved.indexOf(id);
        if(i>-1){saved.splice(i,1);b.textContent='♡';b.classList.remove('on');}
        else{saved.push(id);b.textContent='♥';b.classList.add('on');}
        localStorage.setItem('mock_saved',JSON.stringify(saved));
      });
    });
  }catch(e){}

  // Lightbox galeri
  var lb=document.getElementById('lightbox');
  if(lb){
    var lbimg=lb.querySelector('img');
    document.querySelectorAll('[data-zoom]').forEach(function(im){
      im.addEventListener('click',function(){lbimg.src=im.dataset.zoom||im.src;lb.classList.add('on');});
    });
    lb.addEventListener('click',function(){lb.classList.remove('on');});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on');});
  }

  // Thumbnail galeri
  var main=document.getElementById('galMain');
  if(main){
    document.querySelectorAll('.thumbs img').forEach(function(t){
      t.addEventListener('click',function(){
        main.src=t.dataset.big||t.src;
        document.querySelectorAll('.thumbs img').forEach(function(x){x.classList.remove('on')});
        t.classList.add('on');
      });
    });
  }

  // Widget ansuran
  document.querySelectorAll('[data-calc]').forEach(function(w){
    var harga=w.querySelector('input[type=range]');
    var out=w.querySelector('.out b');
    var val=w.querySelector('.val');
    var RATE=0.0400, YEARS=35, MARGIN=0.90;
    function hitung(){
      var p=+harga.value;
      val.textContent='RM '+p.toLocaleString('en-MY');
      var loan=p*MARGIN, r=RATE/12, n=YEARS*12;
      var m=loan*r/(1-Math.pow(1+r,-n));
      out.textContent='RM '+Math.round(m).toLocaleString('en-MY');
    }
    if(harga){harga.addEventListener('input',hitung);hitung();}
  });

  // Bar bawah mudah alih muncul selepas skrol
  var mb=document.querySelector('.mbar');
  if(mb){
    function chk(){ mb.style.transform = (window.scrollY>380)?'translateY(0)':'translateY(120%)'; }
    mb.style.transition='transform .25s'; chk();
    window.addEventListener('scroll',chk,{passive:true});
  }

  // Menu mudah alih
  var tg=document.getElementById('navToggle'), nv=document.getElementById('nav');
  if(tg&&nv){tg.addEventListener('click',function(){
    nv.style.display = (nv.style.display==='flex')?'none':'flex';
    nv.style.position='absolute';nv.style.top='66px';nv.style.left='0';nv.style.right='0';
    nv.style.background='#fff';nv.style.flexDirection='column';nv.style.padding='12px';
    nv.style.boxShadow='0 12px 30px rgba(15,23,42,.14)';nv.style.zIndex='60';
  });}
})();
