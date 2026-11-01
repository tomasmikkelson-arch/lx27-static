/* Perseus – спільні скрипти внутрішніх сторінок (без залежностей) */
(function(){
  var d=document,root=d.documentElement;
  root.classList.add('js');

  // мобільне меню
  var burger=d.getElementById('burger'),menu=d.getElementById('mmenu');
  if(burger&&menu){
    var toggle=function(open){
      burger.setAttribute('aria-expanded',open?'true':'false');
      burger.setAttribute('aria-label',open?'Закрити меню':'Відкрити меню');
      menu.classList.toggle('open',open);d.body.classList.toggle('menu-open',open);
    };
    burger.addEventListener('click',function(){toggle(burger.getAttribute('aria-expanded')!=='true')});
    menu.addEventListener('click',function(e){if(e.target.closest('a'))toggle(false)});
    d.addEventListener('keydown',function(e){if(e.key==='Escape')toggle(false)});
  }

  // розбиття заголовка на слова для анімації
  d.querySelectorAll('.d1[data-split]').forEach(function(h){
    var walk=function(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(n){
        if(n.nodeType===3){
          var parts=n.textContent.split(/(\s+)/),frag=d.createDocumentFragment();
          parts.forEach(function(p){
            if(!p)return;
            if(/^\s+$/.test(p)){frag.appendChild(d.createTextNode(p));return}
            var w=d.createElement('span');w.className='w';var i=d.createElement('span');i.textContent=p;w.appendChild(i);frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag,n);
        }else if(n.nodeType===1&&n.tagName!=='BR'){walk(n)}
      });
    };
    walk(h);
    h.querySelectorAll('.w>span').forEach(function(s,i){s.style.transitionDelay=(i*0.06)+'s'});
  });

  // поява при скролі
  var els=d.querySelectorAll('[data-r],.d1[data-split]');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.08});
    els.forEach(function(el){io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('in')})}

  // кнопка нагору
  var tt=d.getElementById('totop');
  if(tt){
    var on=false;
    window.addEventListener('scroll',function(){var s=window.scrollY>700;if(s!==on){on=s;tt.classList.toggle('show',s)}},{passive:true});
    tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});
  }

  // фільтр портфоліо
  var filters=d.querySelector('.filters');
  if(filters){
    filters.addEventListener('click',function(e){
      var b=e.target.closest('button');if(!b)return;
      filters.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
      var f=b.getAttribute('data-f');
      d.querySelectorAll('.work').forEach(function(w){w.hidden=!(f==='all'||(' '+w.getAttribute('data-cat')+' ').indexOf(' '+f+' ')>-1)});
    });
  }

  // копіювання email
  d.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click',function(){
      var t=b.getAttribute('data-copy'),old=b.textContent;
      var done=function(){b.textContent='Скопійовано';setTimeout(function(){b.textContent=old},1600)};
      if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,function(){})}
    });
  });

  // кнопка «Налаштування cookie» (під майбутній банер)
  d.querySelectorAll('[data-cookie-settings]').forEach(function(btn){
    btn.addEventListener('click',function(){
      try{
        if(typeof window.openCookieSettings==='function'){window.openCookieSettings();return}
        if(window.Cookiebot&&typeof window.Cookiebot.renew==='function'){window.Cookiebot.renew();return}
        if(typeof window.revisitCkyConsent==='function'){window.revisitCkyConsent();return}
        if(window.klaro&&typeof window.klaro.show==='function'){window.klaro.show();return}
      }catch(e){}
      alert('Наразі на сайті не встановлюються аналітичні та рекламні cookie. Щойно їх буде підключено, тут з’являться налаштування згоди. Ви також можете очистити cookie в налаштуваннях браузера.');
    });
  });
})();
