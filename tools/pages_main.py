"""Сторінки: Для ГО, Про нас, Портфоліо, Ціни, Контакти, Політика конфіденційності, 404."""
import os
import json
from build import (ROOT, SITE, TG, IG, LI, EMAIL, LEGAL, BRAND, ORG_ID, SERVICES, page, register, write, crumbs_html,
                   faq_html, faq_schema, cta, btn, btn_back, link_arr, icon, marquee, e, ARR,
                   PLANS, UNITS, UNIT, ONEOFF, MODE_DESIGN, MODE_SMM, money, plan_limits, plan_extra)
from scenes import scene, cover
from pages_services import svc_card

ARROW = '<svg aria-hidden="true"><use href="#arrow"/></svg>'

# ---------------- Для ГО ----------------
def ngo():
    path = "/ngo/"
    crumbs = [("Для громадських організацій", path)]
    faq = [("Ви працюєте з громадськими організаціями та благодійними фондами?", "Так, це один із двох наших основних напрямів. Робимо звіти, посібники, інфографіку, айдентику, матеріали інформаційних кампаній і заходів."),
           ("Чи знаєте ви вимоги донорів щодо видимості?", "Так. Перед стартом вивчаємо брендбук програми чи донора (visibility guidelines) і розміщуємо логотипи, дисклеймери, шрифти та кольори відповідно до них. Якщо вимоги суперечливі, допомагаємо узгодити з програмним офіцером."),
           ("Чи берете участь у тендерах і конкурсних відборах?", "Так, подаємо комерційні пропозиції на тендери й відбори підрядників. Якщо вам потрібна цінова пропозиція, надішліть ТЗ і дату подання. Підготуємо кошторис за вказаними позиціями."),
           ("Які документи ви надаєте?", "Договір, рахунки та акти виконаних робіт від ФОП. За потреби – цінову пропозицію, кошторис у потрібній валюті й інші документи для звітності перед донором."),
           ("Як скласти бюджет на дизайн у грантовій заявці?", "Напишіть нам на етапі підготовки заявки: розпишемо перелік матеріалів і орієнтовну вартість кожної позиції, щоб бюджет був реалістичним."),
           ("Чи можна працювати англійською?", "Так, готуємо матеріали українською та англійською, комунікуємо з міжнародними партнерами англійською.")]
    inc = [("chart", "Звіти та інфографіка", "Річні звіти, звіти для донорів, факт-шити, дашборди з результатами."),
           ("book", "Посібники й методички", "Верстка багатосторінкових видань, навчальних матеріалів, збірників."),
           ("mega", "Інформаційні кампанії", "Концепція кампанії, соцмережі, банери, плакати, обкладинки відео."),
           ("users", "Матеріали для заходів", "Бейджі, ролапи, банери, програми, презентації для форумів і тренінгів."),
           ("palette", "Айдентика ГО та проєкту", "Логотип і стиль організації чи окремого проєкту, сумісний з логотипами донорів."),
           ("slides", "Презентації для донорів", "Презентація організації, результатів і заявки для фандрейзингу."),
           ("web", "Сайти", "Сайт організації або окремого проєкту з новинами, звітами й формою звернення.")]
    rules = [("shield", "Вимоги видимості", "Логотипи партнерів, дисклеймери, шрифти й кольори – як прописано в брендбуку донора чи програми."),
             ("clock", "Терміни під проєкт", "Плануємо роботу під дедлайни звітів, заходів і запусків кампаній."),
             ("file", "Документи для звіту", "Договір, рахунки й акти, які приймуть бухгалтерія та донор."),
             ("globe", "Двомовність", "Українська та англійська версії матеріалів, коректура обох мов.")]
    who = ["Громадські організації та ініціативи", "Благодійні фонди", "Міжнародні організації та їхні партнери в Україні",
           "Органи місцевого самоврядування та громади", "Освітні та культурні проєкти", "Агенції, що реалізують грантові програми"]
    body = f'''
<section class="hero"><div class="wrap">
  {crumbs_html(crumbs)}
  <div class="hero__grid">
    <div class="hero__text">
      <span class="eyebrow">Громадський сектор</span>
      <h1 class="d1" data-split>Дизайн для <em>громадських</em> організацій, фондів і донорських програм</h1>
      <p class="lead">Розробляємо айдентику, шаблони для соцмереж, презентації та сайти. Оформлюємо видання й готуємо матеріали для подій та інформаційних кампаній. Якщо проєкт має вимоги до оформлення або погодження, врахуємо їх у роботі.</p>
      <div class="hero__facts"><span>Вимоги видимості донорів</span><span>Тендери й відбори підрядників</span><span>Договір, рахунки, акти</span></div>
      <div class="btns">{btn("Обговорити задачу", TG, ext=True, lead="Дизайн для ГО")}{btn("Переглянути послуги", "#what", "ghost")}</div>
    </div>
    {scene("ngo")}
  </div>
</div></section>
<section class="sec sec--night" id="what"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Послуги для ГО</span><h2 class="d2">Що ми робимо</h2></div><p class="muted">Можемо зробити один факт-шит, а можемо вести весь візуал програми протягом року.</p></div>
  <div class="grid g3">{"".join(f'<div class="card" data-r="{i%3+1}"><div class="ico">{icon(a)}</div><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(inc))}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Правила гранту</span><h2 class="d2">Працюємо за правилами донорів</h2></div></div>
  <div class="grid g4">{"".join(f'<div class="card" data-r="{i%4+1}"><div class="ico">{icon(a)}</div><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(rules))}</div>
</div></section>
<section class="sec sec--cream"><div class="wrap">
  <div class="grid g2" style="gap:clamp(30px,5vw,70px);align-items:start">
    <div data-r><span class="eyebrow">Для кого</span><h2 class="d2" style="margin-top:16px">З ким працюємо</h2>
      <p class="lead" style="margin-top:18px">Ми вже працювали з освітніми проєктами, медіа, громадськими ініціативами й організаціями, які отримують гранти від міжнародних донорів.</p></div>
    <div class="grid g2" data-r="2">{"".join(f'<div class="card"><p style="color:inherit;font-weight:600">{w}</p></div>' for w in who)}</div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Процес</span><h2 class="d2">Як ми працюємо з ГО</h2></div></div>
  <div class="steps">
    <div class="step" data-r><div><h3>Бриф і вимоги донора</h3><p>Отримуємо ТЗ, брендбук програми, логотипи партнерів, дедлайни звітності.</p></div><span class="when">1–2 дні</span></div>
    <div class="step" data-r><div><h3>Кошторис і договір</h3><p>Фіксуємо перелік матеріалів, ціну за позицію і терміни. Готуємо документи під вимоги закупівлі.</p></div><span class="when">1–3 дні</span></div>
    <div class="step" data-r><div><h3>Дизайн і погодження</h3><p>Показуємо макети, проходимо погодження з вами та, за потреби, з донором.</p></div><span class="when">за графіком</span></div>
    <div class="step" data-r><div><h3>Передача та звітність</h3><p>Файли для друку й онлайну, вихідники, акти виконаних робіт.</p></div><span class="when">у дедлайн</span></div>
  </div>
</div></section>
<section class="sec sec--tight"><div class="wrap prose article" data-r>
<h2>Дизайн для грантових проєктів: що важливо знати</h2>
<p>Більшість міжнародних донорів мають власні правила візуальної ідентифікації: як розміщувати логотип донора поряд з логотипом організації, який дисклеймер додавати до публікацій, які матеріали потребують попереднього погодження. Помилка у видимості може коштувати передрукованого тиражу або зауважень під час звіту.</p>
<p>Ми робимо для громадських організацій і фондів матеріали, які добре виглядають і проходять перевірку донора. Дизайн звітів, посібників, інфографіки, соцмереж і заходів беремо на себе, а ваша команда займається самим проєктом.</p>
<p>Також ми допомагаємо ще на етапі заявки: розписуємо бюджет на комунікаційні матеріали, щоб кошторис був реалістичним. Якщо вам потрібна цінова пропозиція, надішліть ТЗ і дату подання. Підготуємо кошторис за вказаними позиціями.</p>
</div></section>
<section class="sec"><div class="wrap"><div class="sec__head"><div><span class="eyebrow">FAQ</span><h2 class="d2">Питання від ГО</h2></div></div>{faq_html(faq)}</div></section>
{cta("Плануєте проєкт або звіт?", "Надішліть ТЗ чи опис проєкту – підготуємо кошторис під бюджет гранту і графік робіт під ваші дедлайни.", lead="Дизайн для ГО")}
'''
    svc = {"@type": "Service", "name": "Дизайн для громадських організацій і благодійних фондів", "serviceType": "Графічний дизайн для неприбуткових організацій",
           "provider": {"@id": ORG_ID}, "areaServed": "UA", "audience": {"@type": "Audience", "audienceType": "Громадські організації, благодійні фонди, міжнародні донорські програми"}}
    register(path, page(path, "Дизайн для громадських організацій і фондів | Perseus",
                        "Дизайн звітів, посібників, інфографіки, інформаційних кампаній та айдентики для ГО і фондів з урахуванням вимог видимості донорів. Тендери, договір, акти.",
                        body, active="/ngo/", crumbs=crumbs, schema=[svc, faq_schema(faq)]), "0.9")

# ---------------- Про нас ----------------
def about():
    path = "/about/"
    crumbs = [("Про нас", path)]
    img = '''<picture><source type="image/webp" srcset="/assets/ihor-isychenko-720.webp 720w, /assets/ihor-isychenko-1122.webp 1122w" sizes="(max-width:860px) 92vw, 54vw">
<img src="/assets/ihor-isychenko.jpg" width="1122" height="1402" alt="Ігор Ісиченко, засновник і керівник Perseus Agency, у кріслі під лампою" fetchpriority="high"></picture>'''
    values = [("chat", "Відповідаємо швидко", "До 2 годин у робочий час, у Telegram або поштою."),
              ("folder", "Файли належать вам", "Вихідники у Figma, PSD, AI та всі шаблони лишаються у вас."),
              ("target", "Обсяг погоджено заздалегідь", "Ви знаєте, які матеріали отримаєте та в якому форматі."),
              ("shield", "Прозорі умови", "Ціна й терміни фіксуються до старту. Договір, рахунки й акти.")]
    works = [("smm", "linear-gradient(140deg,#2b1748,#8A31EF)", "Соцмережі"), ("branding", "linear-gradient(140deg,#3a1a0c,#FF6016)", "Айдентика"),
             ("slides", "linear-gradient(140deg,#1A2729,#7D71F7)", "Презентації")]
    wk = "".join(f'<a class="work" href="/portfolio/" data-r="{i+1}">{cover(k, bg)}<div class="work__meta"><h3>{n}</h3><span>Дивитись →</span></div></a>' for i, (k, bg, n) in enumerate(works))
    body = f'''
<section class="hero" style="padding-bottom:clamp(30px,4vw,50px)"><div class="wrap">
  {crumbs_html(crumbs)}
  <h1 class="giant" data-r>Perseus<br><em>agency</em></h1>
  <p class="lead" style="margin-top:22px;font-family:var(--f-display);font-weight:600;text-transform:uppercase;letter-spacing:.02em;color:var(--fg)">Агенція візуальної комунікації</p>
  <div class="intro">
    <div class="intro__card" data-r>
      <p class="intro__lead">Perseus об’єднує досвід у графічному дизайні, розробці сайтів і роботі із соцмережами. Співпрацюємо з громадськими організаціями, фондами та малим і середнім бізнесом. Беремо окремі проєкти й забезпечуємо щомісячний дизайн-супровід.</p>
    </div>
    <figure class="intro__photo" data-r="2" style="margin:0">{img}
      <figcaption><span>Ігор Ісиченко</span><span>Засновник і керівник агенції</span></figcaption></figure>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <span class="eyebrow">Засновник</span>
  <h2 class="d2" style="margin:16px 0 clamp(24px,3vw,40px)">Про засновника</h2>
  <div class="manifest" data-scrub-words>
    <p>Ігор Ісиченко заснував Perseus Agency, розпочавши професійний шлях із фрилансу. Працював із громадськими організаціями, донорськими та освітніми проєктами та бізнесом.</p>
    <p>За цей час займався оформленням досліджень і навчальних матеріалів, створював інфографіку, презентації та рекламні креативи, працював із соцмережами. Досвід роботи з різними темами й аудиторіями став основою Perseus.</p>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <h2 class="d2" style="margin-bottom:clamp(24px,3vw,40px)">Коротко про Perseus</h2>
  <div class="stats4">
    <div class="card stat-card" data-r="1"><div class="n">10<sup>+</sup></div><p>років роботи</p></div>
    <div class="card stat-card" data-r="2"><div class="n">180</div><p>реалізованих проєктів</p></div>
    <div class="card stat-card" data-r="3"><div class="n">7</div><p>напрямів роботи</p></div>
    <div class="card stat-card" data-r="4"><div class="n">2</div><p>формати співпраці: окремі проєкти й щомісячний супровід</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Напрями</span><h2 class="d2">Кому ми допомагаємо</h2></div></div>
  <div class="aud">
    <div class="aud__card aud__card--ngo" data-r="1"><h3>Громадським організаціям і фондам</h3>
      <p>Розробляємо айдентику проєктів і сайти, готуємо презентації та матеріали для соцмереж. Оформлюємо дослідження й видання, працюємо над інформаційними кампаніями. Якщо проєкт має вимоги до візуального оформлення, враховуємо їх у макетах.</p>
      {link_arr("Послуги для ГО", "/ngo/")}</div>
    <div class="aud__card aud__card--biz" data-r="2"><h3>Малому й середньому бізнесу</h3>
      <p>Створюємо фірмовий стиль, паковання та сайти. Оформлюємо презентації для клієнтів і партнерів, готуємо рекламні матеріали й ведемо соцмережі.</p>
      {link_arr("Переглянути послуги", "/services/")}</div>
  </div>
</div></section>

<section class="sec sec--night"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Принципи</span><h2 class="d2">Як ми працюємо</h2></div></div>
  <div class="grid g4">{"".join(f'<div class="card" data-r="{i+1}"><div class="ico">{icon(a)}</div><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(values))}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Роботи</span><h2 class="d2">Проєкти</h2></div>{link_arr("Усі роботи", "/portfolio/")}</div>
  <div class="works">{wk}</div>
</div></section>
{cta("Послуги та ціни", "Перегляньте вартість окремих робіт або порівняйте пакети щомісячного супроводу.", primary=("Переглянути ціни", "/prices/", False), secondary=None, lead=None)}
'''
    person = {"@type": "Person", "@id": SITE + "/about/#ihor", "name": "Ігор Ісиченко", "alternateName": "Ihor Isychenko",
              "givenName": "Ігор", "familyName": "Ісиченко", "jobTitle": "Засновник і керівник Perseus Agency",
              "image": SITE + "/assets/ihor-isychenko-1122.webp", "worksFor": {"@id": ORG_ID}, "url": SITE + "/about/",
              "knowsAbout": ["Графічний дизайн", "SMM", "Брендинг", "Дизайн презентацій", "Дизайн для громадських організацій"]}
    about_page = {"@type": "AboutPage", "url": SITE + path, "mainEntity": {"@id": ORG_ID}}
    register(path, page(path, "Про агенцію Perseus і засновника Ігоря Ісиченка | Perseus",
                        "Perseus Agency – агенція візуальної комунікації для малого й середнього бізнесу, ГО та освітніх проєктів. Засновник і керівник – Ігор Ісиченко. Історія та принципи.",
                        body, active="/about/", crumbs=crumbs, schema=[person, about_page],
                        image=None), "0.8")

# ---------------- Портфоліо ----------------
def portfolio():
    path = "/portfolio/"
    crumbs = [("Портфоліо", path)]
    cats = [("all", "Усі"), ("smm", "Соцмережі"), ("branding", "Айдентика"), ("slides", "Презентації"), ("ads", "Реклама"),
            ("print", "Поліграфія"), ("web", "Сайти"), ("ngo", "Для ГО")]
    items = [("smm", "wide", "linear-gradient(130deg,#2b1748,#8A31EF 70%,#A45CFF)", "Візуальна концепція стрічки Instagram", "Соцмережі"),
             ("branding", "", "linear-gradient(140deg,#3a1a0c,#FF6016)", "Логотип і фірмовий стиль", "Айдентика"),
             ("slides", "", "linear-gradient(140deg,#1A2729,#7D71F7)", "Pitch deck для інвесторів", "Презентації"),
             ("ngo", "", "linear-gradient(140deg,#F3E6D8,#CDB0FF)", "Річний звіт для донора", "Для ГО"),
             ("ads", "", "linear-gradient(140deg,#131D1E,#2b1748)", "Пакет креативів для Meta Ads", "Реклама"),
             ("print", "wide", "linear-gradient(130deg,#FFC94A,#FF6016)", "Каталог продукції, 48 сторінок", "Поліграфія"),
             ("web", "", "linear-gradient(140deg,#1F1233,#8A31EF)", "Лендінг під рекламну кампанію", "Сайти"),
             ("ngo smm", "", "linear-gradient(140deg,#1A2729,#FF6016)", "Інформаційна кампанія ГО", "Для ГО"),
             ("slides ngo", "", "linear-gradient(140deg,#2b1748,#FFC94A)", "Презентація проєкту для донора", "Презентації")]
    kmap = {"smm": "smm", "branding": "branding", "slides": "slides", "ngo": "ngo", "ads": "ads", "print": "print", "web": "web", "ngo smm": "smm", "slides ngo": "slides"}
    w = "".join(f'''<article class="work {wide}" data-cat="{c}" data-r>{cover(kmap[c], bg)[:-6]}<span class="soon">Кейс готується</span></div>
<div class="work__meta"><h3>{t}</h3><span>{lab}</span></div></article>''' for c, wide, bg, t, lab in items)
    f = "".join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k=="all" else "false"}">{n}</button>' for k, n in cats)
    body = f'''
<section class="hero" style="padding-bottom:30px"><div class="wrap">
  {crumbs_html(crumbs)}
  <span class="eyebrow">Портфоліо</span>
  <h1 class="d1" data-split style="margin-top:18px">Роботи <em>агенції</em></h1>
  <p class="lead" style="margin-top:22px">Айдентика, соцмережі, презентації, креативи, поліграфія та матеріали для громадських організацій. Ми оновлюємо розділ: частина кейсів під NDA, тому повні добірки надсилаємо за запитом під вашу задачу.</p>
  <div class="btns" style="margin-top:26px">{btn("Отримати добірку робіт", TG, ext=True, lead="Добірка робіт під мою задачу")}</div>
</div></section>
<section class="sec sec--tight"><div class="wrap">
  <div class="filters" role="group" aria-label="Фільтр робіт">{f}</div>
  <div class="works">{w}</div>
</div></section>
{cta("Хочете приклади під вашу нішу?", "Надішлемо добірку релевантних робіт і розповімо, як вирішували схожі задачі.", lead="Добірка робіт під мою задачу")}
'''
    register(path, page(path, "Портфоліо Perseus, айдентика, соцмережі й презентації",
                        "Роботи агенції Perseus: логотипи та фірмові стилі, дизайн соцмереж, презентації, рекламні креативи, каталоги та звіти для громадських організацій.",
                        body, active="/portfolio/", crumbs=crumbs, schema=[{"@type": "CollectionPage", "url": SITE + path, "about": {"@id": ORG_ID}}]), "0.7")

# ---------------- Ціни ----------------
CALC_JS = r'''
(function(){
  var D=__DATA__;
  var fmt=function(n){return (+n).toLocaleString('uk-UA')};
  var sw=document.querySelector('#plans .switch2'),grid=document.getElementById('plansGrid');
  sw.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var m=b.getAttribute('data-mode');
    sw.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    grid.classList.toggle('mode-smm',m==='smm');
    grid.querySelectorAll('[data-design]').forEach(function(s){s.textContent=fmt(s.getAttribute('data-'+m))});
    grid.querySelectorAll('[data-plan]').forEach(function(a){a.setAttribute('data-lead','Пакет «'+a.getAttribute('data-plan')+'» ('+D.modes[m]+')');a.setAttribute('data-lead-extra',a.getAttribute('data-extra-'+m))});
  });
  var mode='design',ms=document.getElementById('calcMode'),rows=document.querySelectorAll('.qty'),
      tot=document.getElementById('calcTotal'),totW=document.getElementById('calcTotalWrap'),line=document.getElementById('calcLine'),list=document.getElementById('calcList'),
      hint=document.getElementById('calcHint'),hintT=document.getElementById('calcHintText'),hintS=document.getElementById('calcHintSave'),pb=document.getElementById('calcPlanBtn'),cb=document.getElementById('calcBtn');
  // лише цілі невід'ємні кількості
  function qty(inp){var v=String(inp.value).trim();if(!/^\d+$/.test(v))return 0;var n=parseInt(v,10);return isFinite(n)&&n>=0?n:0}
  function setTxt(t){pb.querySelectorAll('.roll span').forEach(function(s){s.textContent=t})}
  function calc(){
    var q={},d=0,parts=[];
    rows.forEach(function(r){var n=qty(r.querySelector('input'));q[r.dataset.k]=n;
      if(n>0){d+=n*(+r.dataset.p);parts.push(r.parentNode.querySelector('b').textContent+' × '+n)}});
    var extra={'Режим':D.modes[mode],'Позиції':parts.join('; ')||'–','Сума дизайну':fmt(d)+' грн','Пакет':'індивідуальна оцінка',
      'Підсумок':mode==='smm'?fmt(d)+' грн за дизайн, ведення – оцінка окремо':fmt(d)+' грн'};
    hint.hidden=true;hintS.hidden=true;pb.setAttribute('data-lead','');pb.removeAttribute('data-lead-extra');
    cb.setAttribute('data-lead-extra',JSON.stringify(extra));
    if(!d){totW.hidden=true;line.textContent='Оберіть матеріали для розрахунку';list.textContent='';
      cb.setAttribute('data-lead','Індивідуальний розрахунок');return}
    totW.hidden=false;list.textContent=parts.join(', ');
    cb.setAttribute('data-lead','Індивідуальний розрахунок ('+D.modes[mode]+')');
    // пакет охоплює обсяг, лише якщо покрито всі три ліміти й немає банерів, обкладинок чи слайдів
    var outside=q.banner+q.cover+q.slide_tpl+q.slide_custom>0,best=null;
    if(!outside)D.plans.forEach(function(p){
      if(q.post<=p.posts&&q.story<=p.stories&&q.creative<=p.creatives){var pr=mode==='smm'?p.smm:p.design;if(!best||pr<best.pr)best={p:p,pr:pr}}});
    var offer=null;
    if(mode==='design'){
      tot.textContent=fmt(d);line.textContent='Вибрані матеріали – '+fmt(d)+' грн';
      if(best&&best.pr<d){offer=best;hintT.textContent='Пакет «'+best.p.name+'» за '+fmt(best.pr)+'\u00a0грн охоплює вибраний обсяг';hintS.hidden=false;hintS.textContent='Економія '+fmt(d-best.pr)+'\u00a0грн'}
    }else if(best){
      tot.textContent=fmt(best.pr);line.textContent='Дизайн і ведення за пакетом «'+best.p.name+'» – '+fmt(best.pr)+' грн/міс';offer=best;
      hintT.textContent='Готовий пакет передається за повною фіксованою ціною.';
    }else{
      tot.textContent=fmt(d);line.textContent='Дизайн – '+fmt(d)+' грн. Вартість ведення погодимо окремо';
    }
    if(offer){
      hint.hidden=false;setTxt('Обрати «'+offer.p.name+'»');
      var ex=Object.assign({},extra,{'Пакет':offer.p.name+' ('+D.modes[mode]+')','Підсумок':fmt(offer.pr)+' грн/міс'});
      pb.setAttribute('data-lead','Пакет «'+offer.p.name+'» ('+D.modes[mode]+')');pb.setAttribute('data-lead-extra',JSON.stringify(ex));
    }
  }
  ms.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;mode=b.getAttribute('data-mode');
    ms.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});calc()});
  rows.forEach(function(r){var inp=r.querySelector('input'),b=r.querySelectorAll('button');
    b[0].addEventListener('click',function(){inp.value=Math.max(0,qty(inp)-1);calc()});
    b[1].addEventListener('click',function(){inp.value=qty(inp)+1;calc()});
    inp.addEventListener('input',calc);inp.addEventListener('change',function(){inp.value=qty(inp);calc()});});
  calc();
})();
'''

def prices():
    path = "/prices/"
    crumbs = [("Ціни", path)]
    pl = ""
    for p in PLANS:
        n, hot = p["name"], p["hot"]
        li = "".join(f"<li>{x}</li>" for x in plan_limits(p) + p["extra"]) + "".join(f'<li class="smm-only">{x}</li>' for x in p["smm_extra"])
        style = "" if hot else "color:var(--on-light);border-color:rgba(19,29,30,.25)"
        pl += (f'<div class="plan{" plan--hot" if hot else ""}" data-r>{"<span class=\"badge\">Найчастіше обирають</span>" if hot else ""}<h3>{n}</h3>\n'
               f'<div class="sum"><span data-design="{p["design"]}" data-smm="{p["smm"]}">{money(p["design"])}</span> <small>грн / міс</small></div><p>{p["desc"]}</p><ul>{li}</ul>\n'
               f'<a href="{TG}" target="_blank" rel="noopener" class="btn btn--{"ember" if hot else "ghost"}" data-lead="Пакет «{n}» ({MODE_DESIGN})" data-plan="{n}" data-lead-extra="{e(plan_extra(p))}" data-extra-design="{e(plan_extra(p))}" data-extra-smm="{e(plan_extra(p, 'smm'))}" style="{style}">'
               f'<span class="roll"><span>Обрати пакет</span><span aria-hidden="true">Обрати пакет</span></span><span class="arr">{ARROW}</span></a></div>')
    rows = "".join(
        f'<div class="calc__row"><div><b>{n}</b><small>{s + " · " if s else ""}{money(pr)} грн</small></div>\n'
        f'<div class="qty" data-k="{k}" data-p="{pr}"><button type="button" aria-label="Менше: {n}">−</button>'
        f'<input type="text" value="0" inputmode="numeric" pattern="[0-9]*" autocomplete="off" aria-label="Кількість: {n}">'
        f'<button type="button" aria-label="Більше: {n}">+</button></div></div>' for k, n, s, pr in UNITS)
    single = [("Макет допису або картка каруселі", f"{money(UNIT['post'])} грн"), ("Статична сторіз", f"{money(UNIT['story'])} грн"),
              ("Рекламний креатив у форматах 1:1, 4:5 і 9:16", f"від {money(UNIT['creative'])} грн"), ("Банер для сайту чи розсилки", f"{money(UNIT['banner'])} грн"),
              ("Обкладинка відео", f"{money(UNIT['cover'])} грн"), ("Слайд за готовим шаблоном", f"{money(UNIT['slide_tpl'])} грн"),
              ("Слайд з індивідуальним компонуванням", f"{money(UNIT['slide_custom'])} грн"), ("Дизайн листівки або флаєра", f"від {money(ONEOFF['flyer'])} грн"),
              ("Відмальовка готового логотипа у вектор", f"від {money(ONEOFF['logo_redraw'])} грн"), ("Логотип", f"від {money(ONEOFF['logo'])} грн"),
              ("Логотип і фірмовий стиль", f"від {money(ONEOFF['logo_style'])} грн"), ("Верстка каталогу, звіту чи посібника", "після брифу"),
              ("Сайт під ключ", "після брифу"), ("Матеріали для ГО за грантом", "за кошторисом проєкту")]
    srows = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td></tr>" for a, b in single)
    faq = [("Що, якщо мені не підходить жоден пакет?", "Порахуйте потрібні матеріали в калькуляторі або опишіть задачу у формі. Оцінимо обсяг і запропонуємо ціну."),
           ("Чи входить бюджет на рекламу у вартість?", "Ні, ціни вказано за дизайн і ведення. Рекламний бюджет ви оплачуєте напряму в Meta чи Google."),
           ("Як рахуються слайди презентації?", f"Слайд за вашим готовим шаблоном коштує {money(UNIT['slide_tpl'])} грн, слайд з індивідуальним компонуванням – {money(UNIT['slide_custom'])} грн. В одній презентації можна поєднувати обидва види. Розробку шаблону, тексти й складну інфографіку оцінюємо окремо."),
           ("Чи можна змінити пакет?", "Так, пакет можна збільшити або зменшити з наступного місяця."),
           ("Які умови оплати?", "Передоплата за місяць для пакетів; для разових проєктів – 50% на старті та 50% після здачі. Оплата за рахунком від ФОП."),
           ("Чи є знижки для громадських організацій?", "Для ГО ми готуємо кошторис під бюджет гранту та формат закупівлі. Надішліть ТЗ, і ми підберемо обсяг, який вкладеться в грант.")]
    data = json.dumps({"plans": [{k: p[k] for k in ("name", "design", "smm", "posts", "stories", "creatives")} for p in PLANS],
                       "modes": {"design": MODE_DESIGN, "smm": MODE_SMM}}, ensure_ascii=False)
    sw = (f'<button type="button" aria-pressed="true" data-mode="design">{MODE_DESIGN}</button>'
          f'<button type="button" aria-pressed="false" data-mode="smm">{MODE_SMM}</button>')
    body = f'''
<section class="hero" style="padding-bottom:40px"><div class="wrap">
  {crumbs_html(crumbs)}
  <span class="eyebrow">Ціни</span>
  <h1 class="d1" data-split style="margin-top:18px">Скільки коштує <em>дизайн</em></h1>
  <p class="lead" style="margin-top:22px">Тут можна порахувати окремі матеріали або вибрати пакет на місяць. Якщо вашої задачі немає у списку, напишіть нам – оцінимо її окремо.</p>
</div></section>
<section class="sec sec--cream" id="plans"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Пакети на місяць</span><h2 class="d2">Щомісячний супровід</h2></div>
    <div class="switch2" role="group" aria-label="Тип пакета">{sw}</div></div>
  <p class="mode-note">{MODE_DESIGN} – ви надаєте тексти й публікуєте матеріали. {MODE_SMM} – ми складаємо контент-план, пишемо тексти й публікуємо погоджені матеріали в межах пакета.</p>
  <div class="plans" id="plansGrid">{pl}</div>
  <p class="muted" style="margin-top:20px;font-size:15px">Усі суми пакетів у гривнях за місяць. Одна картка каруселі рахується як один макет. Рекламний бюджет оплачується окремо.</p>
  <div class="plan plan--ind" data-r style="margin-top:16px;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between">
    <div style="max-width:640px"><h3>Індивідуальний обсяг</h3><p style="margin-top:8px">Потрібно 6 дописів і презентацію? Або 40 креативів на місяць без соцмереж? Порахуйте матеріали в калькуляторі нижче або опишіть задачу.</p></div>
    <div class="btns"><a href="{TG}" class="btn btn--ember" target="_blank" rel="noopener" data-lead="Індивідуальний обсяг"><span class="roll"><span>Обговорити задачу</span><span aria-hidden="true">Обговорити задачу</span></span><span class="arr">{ARROW}</span></a></div>
  </div>
</div></section>

<section class="sec" id="calc"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Калькулятор</span><h2 class="d2">Порахуйте свій обсяг</h2></div><p class="muted">Вкажіть, скільки матеріалів потрібно на місяць. Покажемо суму й підкажемо, чи охоплює цей обсяг готовий пакет.</p></div>
  <div class="switch2 switch2--dark" role="group" aria-label="Режим розрахунку" id="calcMode">{sw}</div>
  <div class="calc">
    <div class="calc__items">
      {rows}
      <p class="muted" style="font-size:14px;margin:6px 4px 0">Логотип, верстку видань і нестандартні роботи рахуємо окремо, ціни в таблиці нижче.</p>
    </div>
    <aside class="calc__sum" aria-live="polite">
      <span class="eyebrow" style="color:#fff">Розрахунок на місяць</span>
      <div class="total" id="calcTotalWrap" hidden><span id="calcTotal">0</span> грн</div>
      <p id="calcLine" style="font-weight:600;color:#fff">Оберіть матеріали для розрахунку</p>
      <p id="calcList" style="font-size:14px"></p>
      <div class="hint" id="calcHint" hidden><p class="hint__t" id="calcHintText"></p><p class="hint__save" id="calcHintSave" hidden></p>
        <a href="{TG}" target="_blank" rel="noopener" class="btn btn--ghost calc__plan" id="calcPlanBtn" data-lead=""><span class="roll"><span>Обрати пакет</span><span aria-hidden="true">Обрати пакет</span></span></a></div>
      <a href="{TG}" target="_blank" rel="noopener" class="btn btn--ember" id="calcBtn" data-lead="Індивідуальний розрахунок"><span class="roll"><span>Обговорити цей пакет</span><span aria-hidden="true">Обговорити цей пакет</span></span><span class="arr">{ARROW}</span></a>
      <p style="font-size:13px;opacity:.75">Розрахунок орієнтовний. Фінальну ціну фіксуємо до початку роботи.</p>
    </aside>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Поштучно й разово</span><h2 class="d2">Окремі роботи</h2></div>{link_arr("Усі послуги", "/services/")}</div>
  <div class="table-wrap" data-r><table class="ptable"><thead><tr><th>Робота</th><th>Ціна</th></tr></thead><tbody>{srows}</tbody></table></div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec__head"><div><span class="eyebrow">FAQ</span><h2 class="d2">Питання про ціни</h2></div></div>{faq_html(faq)}</div></section>
{cta("Порахуємо вашу задачу", "Опишіть, що потрібно зробити. Надішлемо кошторис з фіксованою ціною та строками.", lead="Розрахунок вартості", secondary=("Послуги", "/services/"))}
<script>{CALC_JS.replace("__DATA__", data)}</script>
'''
    offers = [{"@type": "Offer", "name": f"Пакет «{p['name']}» ({MODE_DESIGN.lower()})", "price": p["design"], "priceCurrency": "UAH", "url": SITE + path + "#plans"} for p in PLANS]
    offers += [{"@type": "Offer", "name": f"Пакет «{p['name']}» ({MODE_SMM.lower()})", "price": p["smm"], "priceCurrency": "UAH", "url": SITE + path + "#plans"} for p in PLANS]
    register(path, page(path, "Скільки коштує дизайн, пакети та калькулятор | Perseus",
                        "Ціни на дизайн дописів, сторіз, рекламних креативів, презентацій і логотипа. Пакети Starter, Plus і Premium від 4 900 грн/міс, калькулятор вартості.",
                        body, active="/prices/", crumbs=crumbs,
                        schema=[{"@type": "OfferCatalog", "name": "Пакети дизайну та ведення соцмереж", "itemListElement": offers}, faq_schema(faq)]), "0.9")

# ---------------- Контакти ----------------
def contacts():
    path = "/contacts/"
    crumbs = [("Контакти", path)]
    body = f'''
<section class="hero" style="padding-bottom:40px"><div class="wrap">
  {crumbs_html(crumbs)}
  <div class="hero__grid">
    <div class="hero__text">
      <span class="eyebrow">Контакти</span>
      <h1 class="d1" data-split>Контакти <em>агенції</em></h1>
      <p class="lead">Напишіть нам про вашу задачу. Якщо у вас уже є технічне завдання чи приклади матеріалів, їх можна надіслати електронною поштою.</p>
      <div class="btns">{btn("Обговорити задачу", TG, ext=True, lead="Сторінка контактів")}{btn("Написати в Telegram", TG, "ghost", ext=True)}</div>
    </div>
    <div class="grid" style="gap:12px">
      <a class="card" href="{TG}" target="_blank" rel="noopener" data-r="1" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">Найшвидше</span><h3 style="margin-top:10px">Telegram · @perseus_agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
      <div class="card" data-r="2" style="display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap"><div><span class="eyebrow">Email</span><h3 style="margin-top:10px"><a href="mailto:{EMAIL}">{EMAIL}</a></h3></div><button type="button" class="btn btn--ghost" style="height:44px;padding:0 18px" data-copy="{EMAIL}">Копіювати</button></div>
      <a class="card" href="{IG}" target="_blank" rel="noopener" data-r="3" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">Instagram</span><h3 style="margin-top:10px">@perseus_agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
      <a class="card" href="{LI}" target="_blank" rel="noopener" data-r="4" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">LinkedIn</span><h3 style="margin-top:10px">Perseus Agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
      <p class="muted" data-r="4" style="margin:6px 4px 0;font-size:15px">Зручно листуватися поштою? Надішліть опис задачі, посилання або готове ТЗ на <a href="mailto:{EMAIL}" style="text-decoration:underline">{EMAIL}</a>.</p>
    </div>
  </div>
</div></section>
<section class="sec sec--night"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Як почати</span><h2 class="d2">Від повідомлення до першого макета</h2></div></div>
  <div class="steps">
    <div class="step" data-r><div><h3>Ви пишете нам</h3><p>У Telegram, на email або через форму – коротко про задачу. Обсяг і дату можна додати, якщо вони вже відомі.</p></div><span class="when">5 хвилин</span></div>
    <div class="step" data-r><div><h3>Відповідь і, за потреби, дзвінок</h3><p>Уточнюємо деталі в листуванні. Якщо задачу простіше обговорити голосом, пропонуємо дзвінок на 30 хвилин. Безкоштовно.</p></div><span class="when">1 день</span></div>
    <div class="step" data-r><div><h3>Пропозиція і договір</h3><p>Фіксуємо обсяг, ціну, терміни. Підписуємо договір, ви отримуєте рахунок.</p></div><span class="when">1–2 дні</span></div>
    <div class="step" data-r><div><h3>Старт роботи</h3><p>Для разового проєкту строк називаємо в пропозиції. Старт місячного дизайн-супроводу – за 5–7 робочих днів: погоджуємо стиль і готуємо шаблони.</p></div><span class="when">за домовленістю</span></div>
  </div>
</div></section>
<section class="sec sec--tight"><div class="wrap">
  <div class="split2"><h2 class="d2" data-r>Реквізити</h2>
  <div class="prose" data-r="2"><p><strong>{LEGAL}</strong><br>Бренд: {BRAND}<br>Працюємо онлайн з клієнтами з усієї України та з-за кордону.<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Оплата за рахунком у гривнях або в іноземній валюті. Договір, рахунки й акти виконаних робіт.</p></div></div>
</div></section>
{cta("Маєте задачу або хочете порадитися щодо формату?", "Оберіть послугу або опишіть задачу своїми словами. Залиште контакт, і ми відповімо.", lead="Сторінка контактів", secondary=("Ціни", "/prices/"))}
'''
    cp = {"@type": "ContactPage", "url": SITE + path, "mainEntity": {"@id": ORG_ID}}
    register(path, page(path, "Контакти Perseus Agency, Telegram, email та Instagram",
                        "Зв'яжіться з Perseus: Telegram @perseus_agency, email hello@perseus.studio. Відповідаємо протягом 2 годин у робочий час. Безкоштовна консультація та оцінка проєкту.",
                        body, active="/contacts/", crumbs=crumbs, schema=[cp]), "0.7")

# ---------------- Політика конфіденційності ----------------
def privacy():
    path = "/privacy/"
    crumbs = [("Політика конфіденційності", path)]
    art = open(os.path.join(ROOT, "tools", "privacy_body.html"), encoding="utf-8").read()
    body = f'''
<section class="hero" style="padding-bottom:40px"><div class="wrap">
  {crumbs_html(crumbs)}
  <span class="eyebrow">Правова інформація</span>
  <h1 class="d1" style="margin-top:18px">Політика конфіденційності</h1>
  <p class="lead" style="margin-top:22px">Ця Політика пояснює, які персональні дані збирає сайт <strong>perseus.company</strong>, навіщо ми їх використовуємо, з ким ділимося, як застосовуємо файли cookie та рекламні технології Google і Meta, а також які права ви маєте.</p>
  <div class="hero__facts" style="margin-top:22px"><span>Редакція від 1 листопада 2026 р.</span><span>Набирає чинності з дати публікації</span></div>
  <div class="btns" style="margin-top:26px">{btn_back("На головну", "/")}</div>
</div></section>
<div class="wrap legal-layout">{art}</div>
'''
    register(path, page(path, "Політика конфіденційності – Perseus Agency",
                        "Політика конфіденційності та cookie сайту perseus.company: які дані ми збираємо, навіщо, як довго зберігаємо та які у вас права.",
                        body, crumbs=crumbs), "0.3")

# ---------------- 404 ----------------
def not_found():
    body = f'''
<section class="hero" style="min-height:70vh;display:grid;align-items:center"><div class="wrap">
  <span class="eyebrow">Помилка 404</span>
  <h1 class="giant" style="margin-top:18px">404</h1>
  <p class="lead" style="margin-top:22px">Такої сторінки немає – можливо, її перенесли. Почніть з головної або оберіть послугу.</p>
  <div class="btns" style="margin-top:26px">{btn_back("На головну", "/")}{btn("Послуги", "/services/", "ghost")}{btn("Обговорити задачу", TG, ext=True, lead="")}</div>
</div></section>'''
    write("/404.html", page("/404.html", "Сторінку не знайдено – Perseus", "Сторінку не знайдено.", body, noindex=True))

def build():
    ngo(); about(); portfolio(); prices(); contacts(); privacy(); not_found()
    import pages_blog
    pages_blog.build()
