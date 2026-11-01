"""Одноразові правки головної сторінки (SEO, pop-up, посилання на нові сторінки)."""
import re, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

p = os.path.join(B.ROOT, "index.html")
s = open(p, encoding="utf-8").read()

def rep(a, b, count=1):
    global s
    n = s.count(a)
    assert n == count, (n, a[:80])
    s = s.replace(a, b)

# ---------- HEAD ----------
title = "Perseus – digital-студія графічного дизайну та SMM для бізнесу і ГО"
desc = "Дизайн-супровід бренду, логотип і фірмовий стиль, дизайн для соцмереж і SMM, презентації, рекламні креативи, поліграфія. Для малого й середнього бізнесу та громадських організацій. Від 9 900 грн/міс."
faq = re.findall(r'<div class="qa[^"]*"><button[^>]*>(.*?)<span class="pm"></span></button><div class="a"><div><p>(.*?)</p>', s, re.S)
graph = [B.org_schema(),
         {"@type": "WebSite", "@id": B.SITE + "/#website", "url": B.SITE + "/", "name": B.BRAND, "inLanguage": "uk-UA", "publisher": {"@id": B.ORG_ID}},
         {"@type": "WebPage", "@id": B.SITE + "/#webpage", "url": B.SITE + "/", "name": title, "description": desc, "inLanguage": "uk-UA", "isPartOf": {"@id": B.SITE + "/#website"}, "about": {"@id": B.ORG_ID}},
         {"@type": "OfferCatalog", "name": "Послуги Perseus", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": f"{B.SITE}/services/{sl}/", "provider": {"@id": B.ORG_ID}}} for sl, n, *_ in B.SERVICES]},
         B.faq_schema(faq)]
ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
head_new = f'''<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{B.SITE}/">
<link rel="alternate" hreflang="uk" href="{B.SITE}/">
<link rel="alternate" hreflang="x-default" href="{B.SITE}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="uk_UA">
<meta property="og:site_name" content="{B.BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{B.SITE}/">
<meta property="og:image" content="{B.OG_IMG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/lead.css">
<script type="application/ld+json">{ld}</script>'''
s = re.sub(r'<title>.*?</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="description" content="[^"]*">', lambda m: head_new, s, count=1)
assert "og:image" in s

# ---------- навігація ----------
rep('''      <a href="#about">Студія</a>
      <a href="#services">Послуги</a>
      <a href="#works">Формати</a>
      <a href="#process">Процес</a>
      <a href="#pricing">Тарифи</a>
      <a href="#faq">Питання</a>''',
'''      <a href="#services">Послуги</a>
      <a href="/ngo/">Для ГО</a>
      <a href="/portfolio/">Портфоліо</a>
      <a href="#pricing">Тарифи</a>
      <a href="/about/">Про нас</a>
      <a href="/blog/">Блог</a>''')
rep('''  <a class="mm" href="#about">Студія</a>
  <a class="mm" href="#services">Послуги</a>
  <a class="mm" href="#works">Формати</a>
  <a class="mm" href="#process">Процес</a>
  <a class="mm" href="#pricing">Тарифи</a>
  <a class="mm" href="#contact"><em>Контакти</em></a>''',
'''  <a class="mm" href="/services/">Послуги</a>
  <a class="mm" href="/ngo/">Для ГО</a>
  <a class="mm" href="/portfolio/">Портфоліо</a>
  <a class="mm" href="/prices/">Ціни</a>
  <a class="mm" href="/about/">Про нас</a>
  <a class="mm" href="/blog/">Блог</a>
  <a class="mm" href="/contacts/">Контакти</a>
  <a class="mm" href="https://t.me/perseus_agency" data-lead=""><em>Обговорити проєкт</em></a>''')

# ---------- кнопки → pop-up ----------
rep('<a href="#contact" class="btn btn--ember" data-magnetic><span class="roll"><span>Обговорити проєкт</span>',
    '<a href="https://t.me/perseus_agency" class="btn btn--ember" data-magnetic data-lead=""><span class="roll"><span>Обговорити проєкт</span>', 2)
rep('<a href="#contact" class="btn btn--ember" data-magnetic><span class="roll"><span>Записатися на дзвінок</span>',
    '<a href="https://t.me/perseus_agency" class="btn btn--ember" data-magnetic data-lead="Дзвінок-знайомство"><span class="roll"><span>Записатися на дзвінок</span>')
for n in ["Старт", "Ріст", "Партнер"]:
    s = re.sub(r'<a href="#contact" class="(btn btn--(?:dark|ember))"><span class="roll"><span>Обрати ' + n + '</span>',
               lambda m: f'<a href="https://t.me/perseus_agency" class="{m.group(1)}" data-lead="Пакет «{n}» (Тільки дизайн)" data-plan="{n}"><span class="roll"><span>Обрати {n}</span>', s, count=1)
assert s.count('data-plan=') == 3
rep('class="cta-big" data-magnetic data-cursor="Пишіть">', 'class="cta-big" data-magnetic data-cursor="Пишіть" data-lead="">')

# індивідуальний пакет
rep('<p class="pricing__note">Вартість без бюджету на рекламу. Разові проєкти без підписки рахуємо окремо після брифу.</p>',
'''<div class="plan-ind">
      <div><h3>Індивідуальний пакет</h3><p>Жоден пакет не підходить? Зберемо обсяг під ваші канали й бюджет – у <a href="/prices/#calc">калькуляторі</a> або разом з менеджером.</p></div>
      <a href="https://t.me/perseus_agency" class="btn btn--ember" data-lead="Індивідуальний пакет"><span class="roll"><span>Обговорити індивідуально</span><span>Обговорити індивідуально</span></span><span class="arr"><svg width="14" height="14"><use href="#arrow"/></svg></span></a>
    </div>
    <p class="pricing__note">Вартість без бюджету на рекламу. Разові проєкти без підписки рахуємо окремо після брифу. <a href="/prices/" style="text-decoration:underline">Усі ціни та калькулятор</a></p>''')
rep('.pricing__note{margin:22px 0 0;font-size:14px;opacity:.6}',
    '.pricing__note{margin:22px 0 0;font-size:14px;opacity:.6}\n.plan-ind{margin-top:16px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px;padding:26px 30px;border-radius:var(--r-lg);border:1.5px dashed rgba(19,29,30,.3);color:var(--on-light)}\n.plan-ind h3{font-family:var(--f-display);font-size:22px;margin:0 0 6px}\n.plan-ind p{margin:0;max-width:640px;opacity:.75}\n.plan-ind a:not(.btn){text-decoration:underline}')

# посилання з послуг на сторінки
links = ["design-support", "smm", "presentations", "smm", "ad-creatives", "print-layout"]
parts = s.split('<div class="svc__body"><div><div class="svc__inner">')
assert len(parts) == 7
for i, sl in enumerate(links):
    seg = parts[i + 1]
    j = seg.index("</div>\n        </div></div></div>")
    seg = seg[:j] + f'<a class="svc__more" href="/services/{sl}/">Детальніше про послугу →</a></div>\n        </div></div></div>' + seg[j + len("</div>\n        </div></div></div>"):]
    parts[i + 1] = seg
s = '<div class="svc__body"><div><div class="svc__inner">'.join(parts)
rep('.svc__chips{display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start}',
    '.svc__chips{display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start}\n.svc__more{grid-column:1/-1;justify-self:start;font-weight:700;font-size:15px;border-bottom:1.5px solid currentColor;padding-bottom:2px}')

# футер
rep('<ul><li><a href="#about">Студія</a></li><li><a href="#services">Послуги</a></li><li><a href="#works">Формати</a></li><li><a href="#process">Процес</a></li><li><a href="#pricing">Тарифи</a></li></ul>',
    '<ul><li><a href="/services/">Послуги</a></li><li><a href="/ngo/">Для ГО</a></li><li><a href="/portfolio/">Портфоліо</a></li><li><a href="/prices/">Ціни</a></li><li><a href="/about/">Про нас</a></li><li><a href="/blog/">Блог</a></li><li><a href="/contacts/">Контакти</a></li></ul>')
rep('<div class="legal"><span>© 2026 Perseus Digital Studio</span><span><a href="/privacy/">Політика конфіденційності</a></span></div>',
    '<div class="legal"><span>© 2026 Perseus Digital Studio · ФОП Ісиченко Ігор Володимирович</span><span><a href="/privacy/">Політика конфіденційності</a> · <a href="#" data-cookie-settings>Налаштування cookie</a></span></div>')

# lenis доступний для pop-up
rep("    lenis = new Lenis({", "    lenis = window.lenis = new Lenis({")

# скрипт pop-up + перемикач тарифів оновлює контекст
rep("</body>", '''<script>
document.querySelectorAll('#switch button').forEach(function(b){b.addEventListener('click',function(){var m=b.getAttribute('data-mode')==='smm'?'Дизайн + SMM':'Тільки дизайн';
document.querySelectorAll('[data-plan]').forEach(function(a){a.setAttribute('data-lead','Пакет «'+a.getAttribute('data-plan')+'» ('+m+')')})})});
document.addEventListener('click',function(e){var c=e.target.closest('[data-cookie-settings]');if(!c)return;e.preventDefault();
if(typeof window.openCookieSettings==='function'){window.openCookieSettings();return}location.href='/privacy/#consent'});
</script>
<script src="/assets/lead.js" defer></script>
</body>''')

open(p, "w", encoding="utf-8").write(s)
print("index.html оновлено")
