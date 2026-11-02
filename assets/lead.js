/* Pop-up «Обговорити проєкт».
   Будь-яке посилання/кнопка з атрибутом data-lead відкриває форму-бриф.
   data-lead="Назва послуги або пакета" – підставляється як контекст і попередньо обирає послугу.
   Без JS посилання веде у Telegram (href лишається робочим).
   Під Google Ads / Meta: при надсиланні пушиться подія lead_submit у dataLayer і fbq('track','Lead'), якщо їх підключено. */
(function(){
  var TG='https://t.me/perseus_agency', TG_USER='perseus_agency', MAIL='hello@perseus.studio';
  var SERVICES=['Дизайн-супровід','Логотип і айдентика','Дизайн для соцмереж','SMM-ведення','Презентація','Рекламні креативи','Поліграфія / верстка','Дизайн сайту','Ще не знаю'];
  var MAP=[[/супровід|design-support|підписк/i,'Дизайн-супровід'],[/логотип|айдентик|фірмов|бренд|branding/i,'Логотип і айдентика'],[/smm-|ведення|дизайн \+ smm/i,'SMM-ведення'],[/соцмереж|пост|сторіз|instagram/i,'Дизайн для соцмереж'],[/презентац|pitch|деки/i,'Презентація'],[/реклам|креатив|банер/i,'Рекламні креативи'],[/поліграф|верстк|друк|каталог|брошур|звіт/i,'Поліграфія / верстка'],[/сайт|лендінг|web/i,'Дизайн сайту'],[/пакет|старт|ріст|партнер/i,'Дизайн-супровід']];
  var ORG=['Бізнес','Громадська організація / фонд','Приватна особа','Інше'];
  var BUD=['до 5 000 грн','5–10 тис. грн','10–20 тис. грн','20 тис.+','Поки не знаю'];
  var d=document,root,lastFocus;
  var ic={tg:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.5 3.6 2.9 10.8c-1.3.5-1.2 1.3-.2 1.6l4.8 1.5 1.8 5.6c.2.7.4.9.9.9s.7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.3-.5-1.9-1.6-1.4Z"/></svg>',
          mail:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
          x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
          ok:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'};
  function chips(name,list,type){return list.map(function(v){return '<label><input type="'+type+'" name="'+name+'" value="'+v+'"><span>'+v+'</span></label>'}).join('')}
  function build(){
    root=d.createElement('div');root.className='lm';root.setAttribute('aria-hidden','true');root.setAttribute('data-lenis-prevent','');
    root.innerHTML='<div class="lm__bg" data-close></div>'+
    '<div class="lm__box" role="dialog" aria-modal="true" aria-labelledby="lmTitle" data-lenis-prevent>'+
      '<button class="lm__close" type="button" data-close aria-label="Закрити">'+ic.x+'</button>'+
      '<aside class="lm__side"><span class="lm__eyebrow">Perseus Digital Studio</span>'+
        '<h2 class="lm__title" id="lmTitle">Обговорімо ваш проєкт</h2><span class="lm__ctx" id="lmCtx"></span>'+
        '<ul class="lm__pts"><li>Відповідаємо протягом 2 годин у робочий час</li><li>Перший дзвінок і оцінка – безкоштовно</li><li>Фіксуємо обсяг і ціну до старту</li><li>Працюємо за договором з ФОП, є акти для бухгалтерії та донорів</li></ul>'+
        '<div class="lm__direct"><a href="'+TG+'" target="_blank" rel="noopener" data-direct="telegram">Telegram <span>@perseus_agency</span></a><a href="mailto:'+MAIL+'" data-direct="email">Email <span>'+MAIL+'</span></a></div>'+
      '</aside>'+
      '<div class="lm__main">'+
        '<form class="lm__form" novalidate>'+
          '<fieldset><legend>Що потрібно?</legend><div class="lm__chips">'+chips('svc',SERVICES,'checkbox')+'</div></fieldset>'+
          '<fieldset><legend>Ви представляєте</legend><div class="lm__chips">'+chips('org',ORG,'radio')+'</div></fieldset>'+
          '<fieldset><legend>Орієнтовний бюджет</legend><div class="lm__chips">'+chips('bud',BUD,'radio')+'</div></fieldset>'+
          '<div><label class="lm__lbl" for="lmTask">Коротко про задачу</label><textarea id="lmTask" name="task" placeholder="Наприклад: потрібен дизайн-супровід Instagram для кав’ярні, 12 постів на місяць"></textarea></div>'+
          '<div class="lm__row"><div><label class="lm__lbl" for="lmName">Ім’я</label><input type="text" id="lmName" name="name" autocomplete="name" placeholder="Як до вас звертатися"></div>'+
          '<div><label class="lm__lbl" for="lmContact">Телефон, Telegram або email</label><input type="text" id="lmContact" name="contact" autocomplete="tel" placeholder="+380… або @нік"></div></div>'+
          '<div class="lm__err" id="lmErr" role="alert"></div>'+
          '<div class="lm__actions"><button class="lm__btn lm__btn--tg" type="submit" data-via="telegram">'+ic.tg+'Надіслати в Telegram</button><button class="lm__btn lm__btn--mail" type="submit" data-via="email">'+ic.mail+'Надіслати на email</button></div>'+
          '<p class="lm__fine">Надсилаючи заявку, ви погоджуєтеся з <a href="/privacy/" target="_blank">Політикою конфіденційності</a>. Ми використаємо контакти лише для відповіді.</p>'+
        '</form>'+
        '<div class="lm__ok" role="status"><div class="big">'+ic.ok+'</div><h3 id="lmOkT">Майже готово!</h3><p id="lmOkP"></p>'+
          '<div class="lm__actions"><a class="lm__btn lm__btn--tg" href="'+TG+'" target="_blank" rel="noopener">'+ic.tg+'Відкрити Telegram</a><button class="lm__btn lm__btn--mail" type="button" data-copy-again>Скопіювати ще раз</button></div></div>'+
      '</div>'+
    '</div>';
    d.body.appendChild(root);
    root.addEventListener('click',function(e){if(e.target.closest('[data-close]'))close()});
    root.addEventListener('keydown',function(e){
      if(e.key==='Escape'){close();return}
      if(e.key==='Tab'){var f=root.querySelectorAll('button,a,input,textarea');f=Array.prototype.filter.call(f,function(x){return x.offsetParent!==null});if(!f.length)return;var a=f[0],z=f[f.length-1];
        if(e.shiftKey&&d.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&d.activeElement===z){e.preventDefault();a.focus()}}
    });
    var form=root.querySelector('form'),via='telegram';
    form.querySelectorAll('[data-via]').forEach(function(b){b.addEventListener('click',function(){via=b.getAttribute('data-via')})});
    form.addEventListener('submit',function(e){e.preventDefault();send(via)});
    root.querySelector('[data-copy-again]').addEventListener('click',function(){copy(root._msg||'')});
    root.querySelectorAll('[data-direct]').forEach(function(a){a.addEventListener('click',function(){track(a.getAttribute('data-direct')+'_direct')})});
  }
  function val(n){var f=root.querySelector('form');return Array.prototype.map.call(f.querySelectorAll('[name="'+n+'"]:checked'),function(x){return x.value})}
  function compose(){
    var f=root.querySelector('form'),L=[];
    L.push('Вітаю! Хочу обговорити проєкт.');
    if(root._ctx)L.push('Звідки: '+root._ctx);
    var s=val('svc');if(s.length)L.push('Послуги: '+s.join(', '));
    var o=val('org');if(o.length)L.push('Хто: '+o[0]);
    var b=val('bud');if(b.length)L.push('Бюджет: '+b[0]);
    if(f.task.value.trim())L.push('Задача: '+f.task.value.trim());
    if(f.name.value.trim())L.push('Ім’я: '+f.name.value.trim());
    if(f.contact.value.trim())L.push('Контакт: '+f.contact.value.trim());
    return L.join('\n');
  }
  function copy(t){try{if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t);return true}}catch(e){}
    try{var ta=d.createElement('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';d.body.appendChild(ta);ta.select();d.execCommand('copy');ta.remove();return true}catch(e){return false}}
  function track(method){
    try{(window.dataLayer=window.dataLayer||[]).push({event:'lead_submit',lead_method:method,lead_context:root._ctx||''})}catch(e){}
    try{if(typeof window.fbq==='function')window.fbq('track','Lead',{content_name:root._ctx||'',method:method})}catch(e){}
    try{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{method:method})}catch(e){}
  }
  function send(via){
    var f=root.querySelector('form'),err=root.querySelector('#lmErr');
    if(!val('svc').length&&!f.task.value.trim()){err.textContent='Оберіть послугу або коротко опишіть задачу.';return}
    err.textContent='';
    var msg=compose();root._msg=msg;track(via);
    if(via==='email'){
      location.href='mailto:'+MAIL+'?subject='+encodeURIComponent('Заявка з сайту'+(root._ctx?' – '+root._ctx:''))+'&body='+encodeURIComponent(msg);
      root.querySelector('#lmOkT').textContent='Лист відкрито у вашій пошті';
      root.querySelector('#lmOkP').textContent='Перевірте текст і натисніть «Надіслати». Якщо поштова програма не відкрилася, напишіть нам у Telegram – текст заявки ми вже скопіювали.';
      copy(msg);
    }else{
      var ok=copy(msg);
      window.open('https://t.me/'+TG_USER+'?text='+encodeURIComponent(msg),'_blank','noopener');
      root.querySelector('#lmOkT').textContent='Відкриваємо Telegram';
      root.querySelector('#lmOkP').textContent=ok?'Текст заявки вже скопійовано. Якщо він не з’явився в чаті автоматично, просто вставте його (Ctrl+V або довге натискання → «Вставити») і надішліть.':'Напишіть нам у чат @perseus_agency – відповімо протягом 2 годин у робочий час.';
    }
    root.classList.add('done');
  }
  function preselect(ctx){
    var f=root.querySelector('form');f.reset();root.classList.remove('done');
    if(!ctx)return;
    for(var i=0;i<MAP.length;i++){if(MAP[i][0].test(ctx)){var inp=f.querySelector('input[name="svc"][value="'+MAP[i][1]+'"]');if(inp)inp.checked=true;break}}
    if(/\bГО\b|громадськ|фонд|донор|грант/i.test(ctx)){var o=f.querySelector('input[name="org"][value^="Громадська"]');if(o)o.checked=true}
  }
  function open(ctx){
    if(!root)build();
    lastFocus=d.activeElement;root._ctx=ctx||'';
    root.querySelector('#lmCtx').textContent=ctx||'';
    preselect(ctx);
    root.classList.add('open');root.setAttribute('aria-hidden','false');d.documentElement.classList.add('lm-lock');
    if(window.lenis&&window.lenis.stop)try{window.lenis.stop()}catch(e){}
    setTimeout(function(){var c=root.querySelector('.lm__close');c&&c.focus()},60);
    try{(window.dataLayer=window.dataLayer||[]).push({event:'lead_form_open',lead_context:ctx||''})}catch(e){}
  }
  function close(){
    if(!root)return;root.classList.remove('open');root.setAttribute('aria-hidden','true');d.documentElement.classList.remove('lm-lock');
    if(window.lenis&&window.lenis.start)try{window.lenis.start()}catch(e){}
    if(lastFocus&&lastFocus.focus)lastFocus.focus();
  }
  d.addEventListener('click',function(e){
    var t=e.target.closest('[data-lead]');if(!t)return;
    e.preventDefault();e.stopPropagation();open(t.getAttribute('data-lead'));
  },true);
  window.PerseusLead={open:open,close:close};
  if(location.hash==='#brief')setTimeout(function(){open('')},300);
})();
