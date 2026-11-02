"""Сторінки: Для ГО, Про нас, Портфоліо, Ціни, Контакти, Політика конфіденційності, 404."""
import os
from build import (ROOT, SITE, TG, IG, LI, EMAIL, LEGAL, BRAND, ORG_ID, SERVICES, page, register, write, crumbs_html,
                   faq_html, faq_schema, cta, btn, btn_back, link_arr, icon, marquee, e, ARR)
from scenes import scene, cover
from pages_services import svc_card

ARROW = '<svg aria-hidden="true"><use href="#arrow"/></svg>'

# ---------------- Для ГО ----------------
def ngo():
    path = "/ngo/"
    crumbs = [("Для громадських організацій", path)]
    faq = [("Ви працюєте з громадськими організаціями та благодійними фондами?", "Так, це один із двох наших основних напрямів. Робимо звіти, посібники, інфографіку, айдентику, матеріали інформаційних кампаній і заходів."),
           ("Чи знаєте ви вимоги донорів щодо видимості?", "Так. Перед стартом вивчаємо брендбук програми чи донора (visibility guidelines) і розміщуємо логотипи, дисклеймери, шрифти та кольори відповідно до них. Якщо вимоги суперечливі, допомагаємо узгодити з програмним офіцером."),
           ("Чи берете участь у тендерах і конкурсних відборах?", "Так, подаємо комерційні пропозиції на тендери й відбори підрядників, готуємо кошторис і портфоліо під вимоги закупівлі."),
           ("Які документи ви надаєте?", "Договір, рахунки та акти виконаних робіт від ФОП. За потреби – цінову пропозицію, кошторис у потрібній валюті й інші документи для звітності перед донором."),
           ("Як скласти бюджет на дизайн у грантовій заявці?", "Напишіть нам на етапі підготовки заявки: розпишемо перелік матеріалів і орієнтовну вартість кожної позиції, щоб бюджет був реалістичним."),
           ("Чи можна працювати англійською?", "Так, готуємо матеріали українською та англійською, комунікуємо з міжнародними партнерами англійською.")]
    inc = [("chart", "Звіти та інфографіка", "Річні звіти, звіти для донорів, факт-шити, дашборди з результатами."),
           ("book", "Посібники й методички", "Верстка багатосторінкових видань, навчальних матеріалів, збірників."),
           ("mega", "Інформаційні кампанії", "Концепція кампанії, соцмережі, банери, плакати, відео-обкладинки."),
           ("users", "Матеріали для заходів", "Бейджі, ролапи, банери, програми, презентації для форумів і тренінгів."),
           ("palette", "Айдентика ГО та проєкту", "Логотип і стиль організації чи окремого проєкту, сумісний з логотипами донорів."),
           ("slides", "Презентації для донорів", "Презентація організації, результатів і заявки, pitch для фандрейзингу.")]
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
      <h1 class="d1" data-split>Дизайн для <em>громадських</em> організацій і фондів</h1>
      <p class="lead">Звіти, посібники, інформаційні кампанії та айдентика для ГО, благодійних фондів і грантових проєктів – з урахуванням вимог донорів щодо видимості та звітності.</p>
      <div class="hero__facts"><span>Вимоги видимості донорів</span><span>Тендери й відбори підрядників</span><span>Договір, рахунки, акти</span></div>
      <div class="btns">{btn("Обговорити проєкт", TG, ext=True, lead="Дизайн для ГО")}{btn("Що ми робимо", "#what", "ghost")}</div>
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
<p>Також ми допомагаємо ще на етапі заявки: розписуємо бюджет на комунікаційні матеріали, щоб кошторис був реалістичним, і готуємо цінові пропозиції для відборів підрядників.</p>
</div></section>
<section class="sec"><div class="wrap"><div class="sec__head"><div><span class="eyebrow">FAQ</span><h2 class="d2">Питання від ГО</h2></div></div>{faq_html(faq)}</div></section>
{cta("Плануєте проєкт або звіт?", "Надішліть ТЗ чи опис проєкту – підготуємо кошторис під бюджет гранту і графік робіт під ваші дедлайни.", lead="Дизайн для ГО")}
'''
    svc = {"@type": "Service", "name": "Дизайн для громадських організацій і благодійних фондів", "serviceType": "Графічний дизайн для неприбуткових організацій",
           "provider": {"@id": ORG_ID}, "areaServed": "UA", "audience": {"@type": "Audience", "audienceType": "Громадські організації, благодійні фонди, міжнародні донорські програми"}}
    register(path, page(path, "Дизайн для ГО та благодійних фондів | Perseus",
                        "Дизайн звітів, посібників, інфографіки, інформаційних кампаній та айдентики для ГО і фондів з урахуванням вимог видимості донорів. Тендери, договір, акти.",
                        body, active="/ngo/", crumbs=crumbs, schema=[svc, faq_schema(faq)]), "0.9")

# ---------------- Про нас ----------------
def about():
    path = "/about/"
    crumbs = [("Про нас", path)]
    img = '''<picture><source type="image/webp" srcset="/assets/ihor-isychenko-720.webp 720w, /assets/ihor-isychenko-1122.webp 1122w" sizes="(max-width:860px) 92vw, 54vw">
<img src="/assets/ihor-isychenko.jpg" width="1122" height="1402" alt="Ігор Ісиченко, засновник і керівник Perseus Digital Studio, у кріслі під лампою" fetchpriority="high"></picture>'''
    values = [("chat", "Відповідаємо швидко", "До 2 годин у робочий час. Без «подивлюсь завтра»."),
              ("folder", "Файли належать вам", "Вихідники у Figma, PSD, AI та всі шаблони лишаються у вас."),
              ("target", "Дивимося на результат", "Оцінюємо дизайн за заявками, продажами й охопленнями. Лайки колег-дизайнерів тут не рахуються."),
              ("shield", "Прозорі умови", "Ціна й терміни фіксуються до старту. Договір, рахунки й акти.")]
    works = [("smm", "linear-gradient(140deg,#2b1748,#8A31EF)", "Соцмережі"), ("branding", "linear-gradient(140deg,#3a1a0c,#FF6016)", "Айдентика"),
             ("slides", "linear-gradient(140deg,#1A2729,#7D71F7)", "Презентації")]
    wk = "".join(f'<a class="work" href="/portfolio/" data-r="{i+1}">{cover(k, bg)}<div class="work__meta"><h3>{n}</h3><span>Дивитись →</span></div></a>' for i, (k, bg, n) in enumerate(works))
    body = f'''
<section class="hero" style="padding-bottom:clamp(30px,4vw,50px)"><div class="wrap">
  {crumbs_html(crumbs)}
  <h1 class="giant" data-r>Perseus<br><em>studio</em></h1>
  <p class="lead" style="margin-top:22px;font-family:var(--f-display);font-weight:600;text-transform:uppercase;letter-spacing:.02em;color:var(--fg)">Digital-студія, яка стає вашим відділом дизайну</p>
  <div class="intro">
    <div class="intro__card" data-r>
      <p>Perseus – digital-студія графічного дизайну та SMM. Робимо дизайн для малого й середнього бізнесу та громадських організацій: логотипи, соцмережі, звіти для донорів, презентації для інвесторів.</p>
      <ul class="checks">
        <li><span><strong>Малий і середній бізнес</strong> – соцмережі, реклама, презентації, друк</span></li>
        <li><span><strong>Громадські організації</strong> – звіти, посібники, кампанії за правилами донорів</span></li>
        <li><span><strong>Аутсорс-підрядник</strong> – беремо дизайн-частину проєктів і тендерів</span></li>
        <li><span><strong>Договір, рахунки, акти</strong> – прозоро для бухгалтерії та донорів</span></li>
      </ul>
      {btn("Познайомитися", TG, ext=True, lead="Сторінка «Про нас»")}
    </div>
    <figure class="intro__photo" data-r="2" style="margin:0">{img}
      <figcaption><span>Ігор Ісиченко</span><span>Засновник і керівник студії</span></figcaption></figure>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <div class="split2">
    <h2 class="d2" data-r>Про засновника</h2>
    <div class="prose" data-r="2">
      <p><strong>Ігор Ісиченко</strong> – засновник і керівник Perseus Digital Studio. Понад 10 років у графічному дизайні та соцмережах: починав як дизайнер на фрилансі, працював з ресторанами, освітніми проєктами, меблевими брендами, IT-компаніями й громадськими організаціями.</p>
      <p>Майже кожен клієнт Ігоря стикався з тим самим: дизайн потрібен постійно, а надійного виконавця немає. Фрилансер може зникнути посеред задачі, агенція для малого бізнесу задорога й надто довго погоджує, а один штатний дизайнер рідко вміє і сторіз, і верстку річного звіту. Тому Ігор зібрав команду, яка працює як внутрішній відділ дизайну клієнта, тільки без найму в штат.</p>
      <p>Зараз студія бере разові проєкти й щомісяця веде клієнтів на супроводі. Працюємо переважно з <strong>малим і середнім бізнесом</strong> та <strong>громадськими організаціями</strong>: першим треба продавати, другим – звітувати перед донорами й пояснювати людям, чим вони займаються.</p>
      <blockquote class="quote">Я перевіряю дизайн двома питаннями: чи зрозуміла людина з першого погляду, хто ви, і чи захотіла вам написати.</blockquote>
      <div class="sign"><img src="/assets/ihor-face-160.webp" srcset="/assets/ihor-face-160.webp 1x, /assets/ihor-face-320.webp 2x" alt="Ігор Ісиченко" width="88" height="88" loading="lazy"><span><b>Ігор Ісиченко</b>Засновник і керівник Perseus Digital Studio</span></div>
    </div>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <div class="grid g4">
    <div class="card stat-card" data-r="1"><div class="n">10<sup>+</sup></div><p>років у графічному дизайні та соцмережах</p></div>
    <div class="card stat-card" data-r="2"><div class="n">340</div><p>завершених проєктів: презентації, креативи, запуски акаунтів</p></div>
    <div class="card stat-card" data-r="3"><div class="n">13</div><p>клієнтів на щомісячному дизайн- та SMM-супроводі</p></div>
    <div class="card stat-card" data-r="4"><div class="n">1200</div><p>макетів на місяць: пости, сторіз, банери, слайди</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Напрями</span><h2 class="d2">Кому ми допомагаємо</h2></div></div>
  <div class="roles">
    <a class="role" href="/services/" data-r>Малий і середній бізнес<small>Візуал, який допомагає продавати: соцмережі, реклама, презентації, друк</small></a>
    <a class="role" href="/ngo/" data-r>Громадські організації<small>Звіти, посібники й кампанії за правилами донорів</small></a>
    <a class="role" href="/services/design-support/" data-r>Аутсорс-підрядник<small>Беремо дизайн-частину проєктів агенцій і тендерів</small></a>
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

<section class="sec sec--tight"><div class="wrap">
  <div class="split2">
    <h2 class="d2" data-r>Реквізити</h2>
    <div class="prose" data-r="2"><p>{LEGAL}, бренд {BRAND}. Працюємо за договором, оплата за рахунком у гривнях або іноземній валюті. Email: <a href="mailto:{EMAIL}">{EMAIL}</a>, Telegram: <a href="{TG}" target="_blank" rel="noopener">@perseus_agency</a>.</p></div>
  </div>
</div></section>
{cta("Давайте знайомитися", "Розкажіть про ваш бізнес чи організацію – запропонуємо, з чого почати, і порахуємо бюджет.", lead="Сторінка «Про нас»")}
'''
    person = {"@type": "Person", "@id": SITE + "/about/#ihor", "name": "Ігор Ісиченко", "alternateName": "Ihor Isychenko",
              "givenName": "Ігор", "familyName": "Ісиченко", "jobTitle": "Засновник і керівник Perseus Digital Studio",
              "image": SITE + "/assets/ihor-isychenko-1122.webp", "worksFor": {"@id": ORG_ID}, "url": SITE + "/about/",
              "knowsAbout": ["Графічний дизайн", "SMM", "Брендинг", "Дизайн презентацій", "Дизайн для громадських організацій"]}
    about_page = {"@type": "AboutPage", "url": SITE + path, "mainEntity": {"@id": ORG_ID}}
    register(path, page(path, "Про студію Perseus і засновника Ігоря Ісиченка",
                        "Perseus – студія графічного дизайну та SMM для малого й середнього бізнесу та ГО. Засновник і керівник – Ігор Ісиченко. Історія та принципи.",
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
  <h1 class="d1" data-split style="margin-top:18px">Роботи <em>студії</em></h1>
  <p class="lead" style="margin-top:22px">Айдентика, соцмережі, презентації, креативи, поліграфія та матеріали для громадських організацій. Ми оновлюємо розділ: частина кейсів під NDA, тому повні добірки надсилаємо за запитом під вашу задачу.</p>
  <div class="btns" style="margin-top:26px">{btn("Отримати добірку робіт", TG, ext=True, lead="Добірка робіт під мою задачу")}</div>
</div></section>
<section class="sec sec--tight"><div class="wrap">
  <div class="filters" role="group" aria-label="Фільтр робіт">{f}</div>
  <div class="works">{w}</div>
</div></section>
{cta("Хочете приклади під вашу нішу?", "Надішлемо добірку релевантних робіт і розповімо, як вирішували схожі задачі.", lead="Добірка робіт під мою задачу")}
'''
    register(path, page(path, "Портфоліо Perseus: айдентика, соцмережі, презентації, поліграфія",
                        "Роботи digital-студії Perseus: логотипи та фірмові стилі, дизайн соцмереж, презентації, рекламні креативи, каталоги та звіти для громадських організацій.",
                        body, active="/portfolio/", crumbs=crumbs, schema=[{"@type": "CollectionPage", "url": SITE + path, "about": {"@id": ORG_ID}}]), "0.7")

# ---------------- Ціни ----------------
def prices():
    path = "/prices/"
    crumbs = [("Ціни", path)]
    plans = [("Старт", "9900", "19900", "Для невеликого бізнесу, якому потрібна охайна стрічка без зайвих витрат.",
              ["12 постів і 20 сторіз", "Шаблони в стилі бренду", "2 кола правок на макет"], ["Контент-план і тексти", "Публікації за графіком"], False),
             ("Ріст", "16900", "29900", "Коли соцмережі та реклама вже приносять заявки і контенту треба більше.",
              ["20 постів і 40 сторіз", "8 рекламних креативів з ресайзами", "Банери для сайту й розсилок", "Закріплений дизайнер"], ["Стратегія, тексти, модерація", "Звіт і розбір цифр щомісяця"], True),
             ("Партнер", "27900", "44900", "Зовнішній відділ дизайну для команди, яка веде кілька каналів одночасно.",
              ["До 60 дизайн-задач на місяць", "Презентації та друк у пакеті", "Анімовані креативи", "Пріоритетна черга"], ["До 3 соцмереж на супроводі", "Зйомки та робота з блогерами"], False)]
    def fmt(n): return f"{int(n):,}".replace(",", " ")
    pl = ""
    for n, dz, sm, desc, inc, smm, hot in plans:
        li = "".join(f"<li>{x}</li>" for x in inc) + "".join(f'<li class="smm-only">{x}</li>' for x in smm)
        pl += f'''<div class="plan{' plan--hot' if hot else ''}" data-r>{'<span class="badge">Найчастіше обирають</span>' if hot else ''}<h3>{n}</h3>
<div class="sum"><span data-design="{dz}" data-smm="{sm}">{fmt(dz)}</span> <small>грн / міс</small></div><p>{desc}</p><ul>{li}</ul>
<a href="{TG}" target="_blank" rel="noopener" class="btn btn--{'ember' if hot else 'ghost'}" data-lead="Пакет «{n}»" data-plan="{n}" style="{'' if hot else 'color:var(--on-light);border-color:rgba(19,29,30,.25)'}"><span class="roll"><span>Обрати {n}</span><span aria-hidden="true">Обрати {n}</span></span><span class="arr">{ARROW}</span></a></div>'''
    units = [("post", "Пост або слайд каруселі", "за шаблоном бренду", 450, 12), ("story", "Сторіз", "статичні, серіями", 250, 20),
             ("creative", "Рекламний креатив", "з ресайзами 1:1, 4:5, 9:16", 900, 0), ("banner", "Банер для сайту чи розсилки", "", 700, 0),
             ("reels", "Обкладинка Reels / YouTube", "", 300, 0), ("slide", "Слайд презентації", "за вашим текстом", 600, 0)]
    rows = "".join(f'''<div class="calc__row"><div><b>{n}</b><small>{s + " · " if s else ""}{fmt(p)} грн</small></div>
<div class="qty" data-k="{k}" data-p="{p}"><button type="button" aria-label="Менше: {n}">−</button><output aria-live="polite">{q}</output><button type="button" aria-label="Більше: {n}">+</button></div></div>''' for k, n, s, p, q in units)
    single = [("Дизайн поста", "від 450 грн"), ("Рекламний креатив з ресайзами", "від 900 грн"), ("Слайд презентації", "від 600 грн"),
              ("Флаєр, листівка, меню", "від 1 500 грн"), ("Логотип і фірмовий стиль", "після брифу"), ("Верстка каталогу, брошури, звіту", "після брифу"),
              ("Дизайн лендінгу чи сайту", "після брифу"), ("Матеріали для ГО за грантом", "за кошторисом проєкту")]
    srows = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td></tr>" for a, b in single)
    faq = [("Що, якщо мені не підходить жоден пакет?", "Зберемо індивідуальний пакет під ваш обсяг: скористайтеся калькулятором вище або опишіть задачу в формі – запропонуємо формат і ціну."),
           ("Чи входить бюджет на рекламу у вартість?", "Ні, ціни вказано за дизайн і SMM-роботу. Рекламний бюджет ви оплачуєте напряму в Meta чи Google."),
           ("Чи можна змінити пакет?", "Так, пакет можна збільшити або зменшити з наступного місяця."),
           ("Які умови оплати?", "Передоплата за місяць для пакетів; для разових проєктів – 50% на старті та 50% після здачі. Оплата за рахунком від ФОП."),
           ("Чи є знижки для громадських організацій?", "Для ГО ми готуємо кошторис під бюджет гранту та формат закупівлі. Напишіть нам – підберемо обсяг, який вкладеться в грант.")]
    body = f'''
<section class="hero" style="padding-bottom:40px"><div class="wrap">
  {crumbs_html(crumbs)}
  <span class="eyebrow">Ціни</span>
  <h1 class="d1" data-split style="margin-top:18px">Ціни на дизайн і <em>SMM</em></h1>
  <p class="lead" style="margin-top:22px">Готові пакети на місяць, конструктор власного пакета і ціни на разові задачі. Точну вартість фіксуємо після брифу – до початку роботи.</p>
</div></section>
<section class="sec sec--cream" id="plans"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Пакети на місяць</span><h2 class="d2">Щомісячний супровід</h2></div>
    <div class="switch2" role="group" aria-label="Тип пакета"><button type="button" aria-pressed="true" data-mode="design">Тільки дизайн</button><button type="button" aria-pressed="false" data-mode="smm">Дизайн + SMM</button></div></div>
  <div class="plans" id="plansGrid">{pl}</div>
  <div class="plan plan--ind" data-r style="margin-top:16px;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between">
    <div style="max-width:640px"><h3>Індивідуальний пакет</h3><p style="margin-top:8px">Потрібно 6 постів і презентацію? Або 40 креативів на місяць без соцмереж? Зберемо пакет під ваш обсяг, канали й бюджет – зберіть його в калькуляторі нижче або опишіть задачу.</p></div>
    <div class="btns"><a href="{TG}" class="btn btn--ember" target="_blank" rel="noopener" data-lead="Індивідуальний пакет"><span class="roll"><span>Обговорити індивідуально</span><span aria-hidden="true">Обговорити індивідуально</span></span><span class="arr">{ARROW}</span></a></div>
  </div>
  <p class="muted" style="margin-top:20px;font-size:15px">Вартість без бюджету на рекламу. Разові проєкти без підписки рахуємо окремо після брифу.</p>
</div></section>

<section class="sec" id="calc"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Конструктор</span><h2 class="d2">Зберіть свій пакет</h2></div><p class="muted">Вкажіть, скільки контенту потрібно на місяць, – покажемо орієнтовну вартість і підкажемо, чи вигідніше готовий пакет.</p></div>
  <div class="calc">
    <div class="calc__items">{rows}
      <label class="calc__row" style="cursor:pointer"><div><b>Додати SMM-ведення</b><small>контент-план, тексти, публікації, модерація · +10 000 грн</small></div><input type="checkbox" id="calcSmm" style="width:22px;height:22px;accent-color:#8A31EF"></label>
    </div>
    <aside class="calc__sum" aria-live="polite">
      <span class="eyebrow" style="color:#fff">Орієнтовно на місяць</span>
      <div class="total"><span id="calcTotal">0</span> грн</div>
      <p id="calcList">Оберіть позиції ліворуч.</p>
      <div class="hint" id="calcHint" hidden></div>
      <a href="{TG}" target="_blank" rel="noopener" class="btn btn--ember" id="calcBtn" data-lead="Індивідуальний пакет"><span class="roll"><span>Обговорити цей пакет</span><span aria-hidden="true">Обговорити цей пакет</span></span><span class="arr">{ARROW}</span></a>
      <p style="font-size:13px;opacity:.75">Розрахунок орієнтовний. Фінальну ціну фіксуємо після брифу.</p>
    </aside>
  </div>
</div></section>

<section class="sec sec--tight"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Разово</span><h2 class="d2">Разові задачі</h2></div>{link_arr("Усі послуги", "/services/")}</div>
  <div class="table-wrap" data-r><table class="ptable"><thead><tr><th>Послуга</th><th>Ціна</th></tr></thead><tbody>{srows}</tbody></table></div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec__head"><div><span class="eyebrow">FAQ</span><h2 class="d2">Питання про ціни</h2></div></div>{faq_html(faq)}</div></section>
{cta("Порахуємо ваш проєкт", "Опишіть задачу – надішлемо кошторис з фіксованою ціною та термінами.", lead="Розрахунок вартості", secondary=("Послуги", "/services/"))}
<script>
(function(){{
  var sw=document.querySelector('.switch2'),grid=document.getElementById('plansGrid');
  sw.addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;var m=b.getAttribute('data-mode');
    sw.querySelectorAll('button').forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}});
    grid.classList.toggle('mode-smm',m==='smm');
    grid.querySelectorAll('[data-design]').forEach(function(s){{s.textContent=(+s.getAttribute('data-'+m)).toLocaleString('uk-UA')}});
    grid.querySelectorAll('[data-plan]').forEach(function(a){{a.setAttribute('data-lead','Пакет «'+a.getAttribute('data-plan')+'» ('+(m==='smm'?'Дизайн + SMM':'Тільки дизайн')+')')}});
  }});
  var rows=document.querySelectorAll('.qty'),smm=document.getElementById('calcSmm'),tot=document.getElementById('calcTotal'),list=document.getElementById('calcList'),hint=document.getElementById('calcHint'),cb=document.getElementById('calcBtn');
  function calc(){{var s=0,parts=[],q={{}};
    rows.forEach(function(r){{var n=+r.querySelector('output').value||+r.querySelector('output').textContent;q[r.dataset.k]=n;if(n>0){{s+=n*(+r.dataset.p);parts.push(r.parentNode.querySelector('b').textContent+' × '+n)}}}});
    if(smm.checked&&s>0){{s+=10000;parts.push('SMM-ведення')}}
    tot.textContent=s.toLocaleString('uk-UA');list.textContent=parts.length?parts.join(', '):'Оберіть позиції ліворуч.';
    var h='';var base=smm.checked?[19900,29900]:[9900,16900];
    if(q.post>=12&&q.story>=20&&s>base[0]&&q.post<=20)h='Пакет «Старт» за '+base[0].toLocaleString('uk-UA')+' грн може бути вигіднішим.';
    if(q.post>=20&&q.story>=40&&s>base[1])h='Пакет «Ріст» за '+base[1].toLocaleString('uk-UA')+' грн включає ще й 8 креативів – вигідніше.';
    if(s>27900&&!smm.checked)h='Схоже, вам підійде «Партнер» за 27 900 грн: до 60 задач на місяць.';
    hint.hidden=!h;hint.textContent=h;
    cb.setAttribute('data-lead','Індивідуальний пакет: '+(parts.join(', ')||'обсяг уточнимо')+(s?' ≈ '+s.toLocaleString('uk-UA')+' грн/міс':''));
  }}
  rows.forEach(function(r){{var o=r.querySelector('output'),b=r.querySelectorAll('button');
    b[0].addEventListener('click',function(){{o.textContent=Math.max(0,(+o.textContent)-1);o.value=o.textContent;calc()}});
    b[1].addEventListener('click',function(){{o.textContent=(+o.textContent)+1;o.value=o.textContent;calc()}});}});
  smm.addEventListener('change',calc);calc();
}})();
</script>
'''
    offers = [{"@type": "Offer", "name": f"Пакет «{n}» (дизайн)", "price": dz, "priceCurrency": "UAH", "url": SITE + path + "#plans"} for n, dz, *_ in plans]
    offers += [{"@type": "Offer", "name": f"Пакет «{n}» (дизайн + SMM)", "price": sm, "priceCurrency": "UAH", "url": SITE + path + "#plans"} for n, dz, sm, *_ in plans]
    register(path, page(path, "Ціни на дизайн і SMM: пакети та калькулятор | Perseus",
                        "Скільки коштує дизайн-супровід, ведення соцмереж, логотип, презентація, креативи. Пакети від 9 900 грн/міс, калькулятор індивідуального пакета, ціни на разові задачі.",
                        body, active="/prices/", crumbs=crumbs,
                        schema=[{"@type": "OfferCatalog", "name": "Пакети дизайну та SMM", "itemListElement": offers}, faq_schema(faq)]), "0.9")

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
      <h1 class="d1" data-split>Напишіть <em>нам</em></h1>
      <p class="lead">Відповідаємо протягом 2 годин у робочий час. Перший дзвінок і оцінка проєкту – безкоштовно.</p>
      <div class="btns">{btn("Заповнити бриф", TG, ext=True, lead="Сторінка контактів")}{btn("Telegram", TG, "ghost", ext=True)}</div>
    </div>
    <div class="grid" style="gap:12px">
      <a class="card" href="{TG}" target="_blank" rel="noopener" data-r="1" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">Найшвидше</span><h3 style="margin-top:10px">Telegram · @perseus_agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
      <div class="card" data-r="2" style="display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap"><div><span class="eyebrow">Email</span><h3 style="margin-top:10px"><a href="mailto:{EMAIL}">{EMAIL}</a></h3></div><button type="button" class="btn btn--ghost" style="height:44px;padding:0 18px" data-copy="{EMAIL}">Копіювати</button></div>
      <a class="card" href="{IG}" target="_blank" rel="noopener" data-r="3" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">Instagram</span><h3 style="margin-top:10px">@perseus_agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
      <a class="card" href="{LI}" target="_blank" rel="noopener" data-r="4" style="display:flex;justify-content:space-between;align-items:center;gap:16px"><div><span class="eyebrow">LinkedIn</span><h3 style="margin-top:10px">Perseus Agency</h3></div><span class="link-arr"><i>{ARROW}</i></span></a>
    </div>
  </div>
</div></section>
<section class="sec sec--night"><div class="wrap">
  <div class="sec__head"><div><span class="eyebrow">Як почати</span><h2 class="d2">Від повідомлення до першого макета</h2></div></div>
  <div class="steps">
    <div class="step" data-r><div><h3>Ви пишете нам</h3><p>У Telegram, на email або через форму-бриф – коротко про задачу, терміни й бюджет.</p></div><span class="when">5 хвилин</span></div>
    <div class="step" data-r><div><h3>Дзвінок-знайомство</h3><p>30 хвилин: цілі, аудиторія, що вже є. Безкоштовно.</p></div><span class="when">1 день</span></div>
    <div class="step" data-r><div><h3>Пропозиція і договір</h3><p>Фіксуємо обсяг, ціну, терміни. Підписуємо договір, ви отримуєте рахунок.</p></div><span class="when">1–2 дні</span></div>
    <div class="step" data-r><div><h3>Перші макети</h3><p>Погоджуємо стиль і запускаємо роботу.</p></div><span class="when">5–7 днів</span></div>
  </div>
</div></section>
<section class="sec sec--tight"><div class="wrap">
  <div class="split2"><h2 class="d2" data-r>Реквізити</h2>
  <div class="prose" data-r="2"><p><strong>{LEGAL}</strong><br>Бренд: {BRAND}<br>Працюємо онлайн з клієнтами з усієї України та з-за кордону.<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Оплата за рахунком у гривнях або в іноземній валюті. Договір, рахунки й акти виконаних робіт.</p></div></div>
</div></section>
{cta("Не любите писати?", "Заповніть короткий бриф з кількох кліків – ми самі уточнимо деталі.", lead="Сторінка контактів", secondary=("Ціни", "/prices/"))}
'''
    cp = {"@type": "ContactPage", "url": SITE + path, "mainEntity": {"@id": ORG_ID}}
    register(path, page(path, "Контакти Perseus Digital Studio: Telegram, email, Instagram",
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
    register(path, page(path, "Політика конфіденційності – Perseus Digital Studio",
                        "Політика конфіденційності та cookie сайту perseus.company: які дані ми збираємо, навіщо, як довго зберігаємо та які у вас права.",
                        body, crumbs=crumbs), "0.3")

# ---------------- 404 ----------------
def not_found():
    body = f'''
<section class="hero" style="min-height:70vh;display:grid;align-items:center"><div class="wrap">
  <span class="eyebrow">Помилка 404</span>
  <h1 class="giant" style="margin-top:18px">404</h1>
  <p class="lead" style="margin-top:22px">Такої сторінки немає – можливо, її перенесли. Почніть з головної або оберіть послугу.</p>
  <div class="btns" style="margin-top:26px">{btn_back("На головну", "/")}{btn("Послуги", "/services/", "ghost")}{btn("Обговорити проєкт", TG, ext=True, lead="")}</div>
</div></section>'''
    write("/404.html", page("/404.html", "Сторінку не знайдено – Perseus", "Сторінку не знайдено.", body, noindex=True))

def build():
    ngo(); about(); portfolio(); prices(); contacts(); privacy(); not_found()
    import pages_blog
    pages_blog.build()
