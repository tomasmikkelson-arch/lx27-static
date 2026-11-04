/* Pop-up «Обговорити задачу».
   Будь-яке посилання/кнопка з атрибутом data-lead відкриває форму-бриф.
   data-lead="Назва послуги або пакета" – підставляється як контекст і попередньо обирає послугу.
   Без JS посилання веде у Telegram (href лишається робочим).
   data-lead-extra='{"Поле":"значення"}' – додаткові поля для листа (наприклад, розрахунок із калькулятора).
   Введене зберігається, поки сторінка відкрита (форма не очищується при закритті); очищується після успішного надсилання.
   Під Google Ads / Meta: при надсиланні пушиться подія lead_submit у dataLayer і fbq('track','Lead'), якщо їх підключено.
   Особисті дані (імʼя, контакт, текст задачі) в аналітику не передаються. */
(function(){
  var TG='https://t.me/perseus_agency';
  // Заявки надсилаються на пошту через FormSubmit (formsubmit.co). Першу заявку сервіс надішле як лист з кнопкою активації.
  var ENDPOINT='https://formsubmit.co/ajax/tomas.mikkelson@gmail.com';
  var SERVICES=['Дизайн-супровід','Логотип і фірмовий стиль','Дизайн дописів і сторіз','Ведення соцмереж','Презентація','Рекламні креативи','Поліграфія та верстка','Сайт під ключ','Поки хочу порадитися'];
  var MAP=[[/з веденням|ведення/i,'Ведення соцмереж'],[/пакет|starter|plus|premium|індивідуальн|супровід|design-support/i,'Дизайн-супровід'],[/логотип|айдентик|фірмов|бренд|branding/i,'Логотип і фірмовий стиль'],[/соцмереж|допис|пост|сторіз|instagram/i,'Дизайн дописів і сторіз'],[/презентац|pitch|слайд/i,'Презентація'],[/реклам|креатив|банер/i,'Рекламні креативи'],[/поліграф|верстк|друк|каталог|брошур|звіт|посібник/i,'Поліграфія та верстка'],[/сайт|лендінг|web/i,'Сайт під ключ']];
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
      '<aside class="lm__side"><span class="lm__eyebrow">Perseus Agency</span>'+
        '<h2 class="lm__title" id="lmTitle">Що потрібно зробити?</h2>'+
        '<p class="lm__intro">Оберіть послугу або опишіть задачу. Відповімо на контакт, який ви залишите.</p>'+
        '<span class="lm__ctx" id="lmCtxWrap" hidden><span id="lmCtx"></span><button type="button" class="lm__ctx-x" id="lmCtxX" aria-label="Прибрати вибір">×</button></span>'+
      '</aside>'+
      '<div class="lm__main">'+
        '<form class="lm__form" novalidate>'+
          '<div class="lm__order" id="lmOrder" hidden></div>'+
          '<fieldset><legend>Що вас цікавить?</legend><div class="lm__chips">'+chips('svc',SERVICES,'checkbox')+'</div></fieldset>'+
          '<div><label class="lm__lbl" for="lmTask">Коротко про задачу</label><textarea id="lmTask" name="task" placeholder="Що ви плануєте? Якщо вже відомі обсяг або бажана дата, їх теж можна вказати"></textarea></div>'+
          '<div><label class="lm__lbl" for="lmContact">Куди вам відповісти?</label><input type="text" id="lmContact" name="contact" autocomplete="email" placeholder="Email, Telegram або телефон"></div>'+
          '<details class="lm__more"><summary>Ще кілька деталей (необовʼязково)</summary>'+
            '<div><label class="lm__lbl" for="lmName">Імʼя</label><input type="text" id="lmName" name="name" autocomplete="name" placeholder="Як до вас звертатися"></div>'+
            '<fieldset><legend>Ви представляєте</legend><div class="lm__chips">'+chips('org',ORG,'radio')+'</div></fieldset>'+
            '<fieldset><legend>Орієнтовний бюджет</legend><div class="lm__chips">'+chips('bud',BUD,'radio')+'</div></fieldset>'+
          '</details>'+
          '<div class="lm__err" id="lmErr" role="alert"></div>'+
          '<input type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">'+
          '<div class="lm__actions"><button class="lm__btn lm__btn--send" type="submit">Надіслати</button></div>'+
          '<p class="lm__fine">Надсилаючи заявку, ви погоджуєтеся з <a href="/privacy/" target="_blank">Політикою конфіденційності</a>. Ми використаємо контакти лише для відповіді.</p>'+
        '</form>'+
        '<div class="lm__ok" role="status"><div class="big">'+ic.ok+'</div><h3 id="lmOkT">Повідомлення надіслано</h3><p id="lmOkP">Дякуємо, отримали ваше повідомлення. Відповімо за контактом, який ви залишили.</p>'+
          '<div class="lm__actions"><button class="lm__btn lm__btn--send" type="button" data-close>Закрити</button></div></div>'+
      '</div>'+
    '</div>';
    d.body.appendChild(root);
    root.addEventListener('click',function(e){if(e.target.closest('[data-close]'))close()});
    root.addEventListener('keydown',function(e){
      if(e.key==='Escape'){close();return}
      if(e.key==='Tab'){var f=root.querySelectorAll('button,a,input,textarea');f=Array.prototype.filter.call(f,function(x){return x.offsetParent!==null});if(!f.length)return;var a=f[0],z=f[f.length-1];
        if(e.shiftKey&&d.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&d.activeElement===z){e.preventDefault();a.focus()}}
    });
    var form=root.querySelector('form');
    form.addEventListener('submit',function(e){e.preventDefault();send()});
    root.querySelector('#lmCtxX').addEventListener('click',function(){setCtx('',null)});
  }
  function val(n){var f=root.querySelector('form');return Array.prototype.map.call(f.querySelectorAll('[name="'+n+'"]:checked'),function(x){return x.value})}
  function track(method){
    try{(window.dataLayer=window.dataLayer||[]).push({event:'lead_submit',lead_method:method,lead_context:root._ctx||''})}catch(e){}
    try{if(typeof window.fbq==='function')window.fbq('track','Lead',{content_name:root._ctx||'',method:method})}catch(e){}
    try{if(typeof window.gtag==='function')window.gtag('event','generate_lead',{method:method})}catch(e){}
  }
  function send(){
    var f=root.querySelector('form'),err=root.querySelector('#lmErr'),btn=f.querySelector('.lm__btn--send');
    if(!val('svc').length&&!f.task.value.trim()&&!root._ctx){err.textContent='Оберіть послугу або напишіть кілька слів про задачу.';return}
    if(!f.contact.value.trim()){err.textContent='Залиште email, номер телефону або Telegram, щоб ми могли відповісти.';f.contact.focus();return}
    if(f._honey.value)return; // бот
    err.textContent='';
    var data={
      _subject:'Заявка з сайту'+(root._ctx?' – '+root._ctx:''),
      _template:'table',
      _captcha:'false',
      'Звідки':root._ctx||'Головна кнопка',
      'Послуги':val('svc').join(', ')||'–',
      'Хто':val('org')[0]||'–',
      'Бюджет':val('bud')[0]||'–',
      'Задача':f.task.value.trim()||'–',
      "Ім'я":f.name.value.trim()||'–',
      'Контакт':f.contact.value.trim(),
      'Сторінка':location.href
    };
    if(root._extra)for(var k in root._extra)if(Object.prototype.hasOwnProperty.call(root._extra,k))data[k]=String(root._extra[k]);
    var c=f.contact.value.trim();if(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(c))data._replyto=c;
    btn.disabled=true;btn.textContent='Надсилаємо…';
    fetch(ENDPOINT,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json().catch(function(){return {}}).then(function(j){if(!r.ok||j.success===false||j.success==='false')throw new Error(j.message||r.status);return j})})
      .then(function(){track('form');root.classList.add('done');f.reset();setCtx('',null);var c=root.querySelector('.lm__ok [data-close]');c&&setTimeout(function(){c.focus()},50)})
      .catch(function(){err.textContent='Не вдалося надіслати повідомлення. Перевірте інтернет-зʼєднання й спробуйте ще раз.'})
      .then(function(){btn.disabled=false;btn.textContent='Надіслати'});
  }
  function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  // Підсумок вибору (пакет або розрахунок із калькулятора): показуємо в pop-up і передаємо в лист.
  function renderOrder(){
    var box=root.querySelector('#lmOrder'),x=root._extra;
    if(!x||!x['Підсумок']){box.hidden=true;box.innerHTML='';return}
    var rows='';
    if(x['Пакет']&&x['Пакет']!=='індивідуальна оцінка')rows+='<div><dt>Пакет</dt><dd>'+esc(x['Пакет'])+(x['Режим']&&String(x['Пакет']).indexOf(x['Режим'])<0?' · '+esc(x['Режим']):'')+'</dd></div>';
    else if(x['Режим'])rows+='<div><dt>Режим</dt><dd>'+esc(x['Режим'])+'</dd></div>';
    var items=x['Що входить']||x['Позиції'];
    if(items&&items!=='–')rows+='<div><dt>'+(x['Що входить']?'Що входить':'Матеріали')+'</dt><dd><ul>'+String(items).split(/;\s*/).map(function(i){return '<li>'+esc(i)+'</li>'}).join('')+'</ul></dd></div>';
    box.innerHTML='<p class="lm__order-t">Ваш вибір</p><dl>'+rows+'</dl><p class="lm__order-sum"><span>Разом</span><b>'+esc(x['Підсумок'])+'</b></p>';
    box.hidden=false;
  }
  function setCtx(ctx,extra){
    root._ctx=ctx||'';root._extra=extra||null;
    root.querySelector('#lmCtx').textContent=root._ctx;root.querySelector('#lmCtxWrap').hidden=!root._ctx;
    renderOrder();
  }
  // Попередній вибір доповнює вже введене: нічого не стирає, лише позначає послугу за контекстом.
  function preselect(ctx){
    var f=root.querySelector('form');root.classList.remove('done');root.querySelector('#lmErr').textContent='';
    if(!ctx)return;
    for(var i=0;i<MAP.length;i++){if(MAP[i][0].test(ctx)){var inp=f.querySelector('input[name="svc"][value="'+MAP[i][1]+'"]');if(inp)inp.checked=true;break}}
    if(/\bГО\b|громадськ|фонд|донор|грант/i.test(ctx)){var o=f.querySelector('input[name="org"][value^="Громадська"]');if(o)o.checked=true}
  }
  function open(ctx,extra){
    if(!root)build();
    lastFocus=d.activeElement;
    if(ctx||!root._ctx)setCtx(ctx,extra);
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
    e.preventDefault();e.stopPropagation();
    var ex=null,raw=t.getAttribute('data-lead-extra');if(raw){try{ex=JSON.parse(raw)}catch(_){ex=null}}
    open(t.getAttribute('data-lead'),ex);
  },true);
  d.addEventListener('keydown',function(e){if(e.key==='Escape'&&root&&root.classList.contains('open'))close()});
  window.PerseusLead={open:open,close:close};
  if(location.hash==='#brief')setTimeout(function(){open('')},300);
})();
