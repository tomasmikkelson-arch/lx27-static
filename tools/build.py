#!/usr/bin/env python3
"""Генератор статичних сторінок Perseus.

Запуск з кореня репозиторію:  python3 tools/build.py
Створює <slug>/index.html для кожної сторінки, sitemap.xml і robots.txt.
Головна сторінка (index.html) редагується вручну.
"""
import html, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = "https://perseus.company"
BRAND = "Perseus Digital Studio"
EMAIL = "hello@perseus.studio"
TG = "https://t.me/perseus_agency"
IG = "https://www.instagram.com/perseus_agency"
LI = "https://www.linkedin.com/company/perseus-agency/"
LEGAL = "ФОП Ісиченко Ігор Володимирович"
TODAY = date.today().isoformat()
OG_IMG = SITE + "/assets/og-image.jpg"

_src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
WM = re.search(r'<symbol id="wm".*?</symbol>', _src, re.S).group(0)

def e(s):
    return html.escape(s, quote=True)

# ---------- іконки (стиль як на головній: контур 1.8) ----------
_I = {
 "pen": '<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16v4Z"/><path d="m13.5 6.5 4 4"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
 "slides": '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M12 17v4M8 21h8M7 13l3-3 2 2 4-4"/>',
 "cycle": '<path d="M21 12a9 9 0 1 1-3.2-6.9"/><path d="M21 4v5h-5"/><path d="M8 13.5l2.5 2.5L16 10"/>',
 "mega": '<path d="M3 11v2a1 1 0 0 0 1 1h3l6 4V6L7 10H4a1 1 0 0 0-1 1Z"/><path d="M17 9a4 4 0 0 1 0 6M19.5 6.5a8 8 0 0 1 0 11"/>',
 "print": '<path d="M7 8V3h10v5"/><rect x="3" y="8" width="18" height="9" rx="2"/><path d="M7 14h10v7H7z"/>',
 "star": '<path d="M12 3c.6 4.6 3.4 7.4 9 9-5.6 1.6-8.4 4.4-9 9-.6-4.6-3.4-7.4-9-9 5.6-1.6 8.4-4.4 9-9Z"/>',
 "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5Z"/><path d="M4 19a2 2 0 0 1 2-2h13M9 7h6"/>',
 "web": '<rect x="2.5" y="4" width="19" height="16" rx="2"/><path d="M2.5 9h19M6 6.5h.01M9 6.5h.01"/>',
 "heart": '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10Z"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 4.5a3 3 0 0 1 0 6M18 14c2 .8 3 2.8 3 6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6l-8-3Z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 "file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9l-6-6Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
 "palette": '<path d="M12 3a9 9 0 1 0 0 18c1.1 0 1.6-.8 1.6-1.6 0-1.2-1-1.6-1-2.6 0-.9.7-1.6 1.6-1.6H17a4 4 0 0 0 4-4C21 6.6 17 3 12 3Z"/><circle cx="7.5" cy="11" r="1.2"/><circle cx="10" cy="7" r="1.2"/><circle cx="15" cy="7.5" r="1.2"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.8 7L4 20l1.1-4.6A8 8 0 1 1 21 12Z"/>',
 "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9S14.5 18.4 12 21c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/>',
 "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>'

ARR = '<svg aria-hidden="true"><use href="#arrow"/></svg>'

def btn(text, href, kind="ember", ext=False, cls="", lead=None):
    t = ' target="_blank" rel="noopener"' if ext else ""
    if lead is not None:
        t += f' data-lead="{e(lead)}"'
    return (f'<a href="{e(href)}" class="btn btn--{kind} {cls}"{t}><span class="roll"><span>{text}</span>'
            f'<span aria-hidden="true">{text}</span></span><span class="arr">{ARR}</span></a>')

def btn_back(text, href):
    return (f'<a href="{e(href)}" class="btn btn--ghost btn--back"><span class="arr">{ARR}</span>'
            f'<span class="roll"><span>{text}</span><span aria-hidden="true">{text}</span></span></a>')

def link_arr(text, href):
    return f'<a class="link-arr" href="{e(href)}">{text}<i>{ARR}</i></a>'

# ---------- навігація ----------
NAV = [("Послуги", "/services/"), ("Для ГО", "/ngo/"), ("Портфоліо", "/portfolio/"),
       ("Ціни", "/prices/"), ("Про нас", "/about/"), ("Блог", "/blog/"), ("Контакти", "/contacts/")]

SERVICES = [  # slug, назва, коротко, іконка, ціна
 ("design-support", "Дизайн-супровід бренду", "Дизайнер на аутсорсі за щомісячною підпискою", "pen", "від 12 000 грн/міс"),
 ("branding", "Логотип і фірмовий стиль", "Айдентика, брендбук, ребрендинг", "palette", "після брифу"),
 ("smm", "SMM і дизайн для соцмереж", "Пости, сторіз, Reels-обкладинки, ведення акаунтів", "grid", "від 450 грн/пост"),
 ("presentations", "Презентації та pitch-деки", "Для продажів, інвесторів, донорів і конференцій", "slides", "від 600 грн/слайд"),
 ("ad-creatives", "Рекламні креативи", "Банери для Meta Ads і Google Ads", "mega", "від 900 грн/креатив"),
 ("print-layout", "Поліграфія та верстка", "Каталоги, брошури, звіти, книги, меню", "print", "від 1 500 грн"),
 ("web-design", "Дизайн сайтів і лендінгів", "Лендінги, корпоративні сайти, UI у Figma", "web", "після брифу"),
]

def header(active):
    nav = "".join(f'<a href="{u}"{" aria-current=\"page\"" if active == u else ""}>{n}</a>' for n, u in NAV)
    mm = "".join(f'<a href="{u}">{n}</a>' for n, u in NAV)
    return f'''<a class="skip" href="#main">Перейти до змісту</a>
<header class="header">
  <div class="header__bar">
    <a href="/" class="logo" aria-label="Perseus – на головну"><svg viewBox="0 0 1346 272" aria-hidden="true"><use href="#wm" fill="currentColor"/></svg></a>
    <nav class="nav" aria-label="Основна навігація">{nav}</nav>
    {btn("Обговорити проєкт", TG, ext=True, lead="")}
    <button class="burger" id="burger" aria-label="Відкрити меню" aria-expanded="false" aria-controls="mmenu"><span></span><span></span></button>
  </div>
</header>
<div class="mmenu" id="mmenu">
  <a href="/">Головна</a>{mm}
  <a href="{TG}" target="_blank" rel="noopener" data-lead=""><em>Обговорити проєкт</em></a>
  <small>Telegram @perseus_agency · Instagram @perseus_agency</small>
</div>'''

def footer():
    svc = "".join(f'<li><a href="/services/{s}/">{n}</a></li>' for s, n, *_ in SERVICES)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="fcard">
      <div class="fcard__top">
        <h2>Готові працювати <em>разом</em>?</h2>
        <div class="btns">{btn("Обговорити проєкт", TG, ext=True, lead="")}{btn("Усі контакти", "/contacts/", "ghost")}</div>
      </div>
      <div class="fcols">
        <div class="fabout">
          <a href="/" class="logo" aria-label="Perseus – на головну"><svg viewBox="0 0 1346 272" aria-hidden="true"><use href="#wm" fill="currentColor"/></svg></a>
          <p>Digital-студія графічного дизайну та SMM. Повноцінний дизайн-підрядник для малого й середнього бізнесу та громадських організацій.</p>
          <div class="socials">
            <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/></svg></a>
            <a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.5 3.6 2.9 10.8c-1.3.5-1.2 1.3-.2 1.6l4.8 1.5 1.8 5.6c.2.7.4.9.9.9s.7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.3-.5-1.9-1.6-1.4ZM9.4 13.6l9-5.7c.4-.3.8-.1.5.2l-7.4 6.7-.3 3.2-1.8-4.4Z"/></svg></a>
            <a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.5h4V21H3V9.5Zm6.5 0h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.3c0-1.3 0-2.9-1.8-2.9s-2.1 1.4-2.1 2.8V21h-4V9.5Z"/></svg></a>
          </div>
        </div>
        <div><h3>Послуги</h3><ul>{svc}</ul></div>
        <div><h3>Студія</h3><ul>
          <li><a href="/about/">Про нас</a></li><li><a href="/ngo/">Для громадських організацій</a></li>
          <li><a href="/portfolio/">Портфоліо</a></li><li><a href="/prices/">Ціни</a></li>
          <li><a href="/blog/">Блог</a></li><li><a href="/#faq">Часті питання</a></li></ul></div>
        <div><h3>Контакти</h3><ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{TG}" target="_blank" rel="noopener">Telegram: @perseus_agency</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram: @perseus_agency</a></li>
          <li><a href="/contacts/">Як почати співпрацю</a></li></ul></div>
      </div>
      <div class="giant-foot" aria-hidden="true"><svg viewBox="0 0 1346 272"><use href="#wm" fill="url(#gFoot)"/></svg></div>
    </div>
    <div class="legal"><span>© {date.today().year} {BRAND} · {LEGAL}</span><span><a href="/privacy/">Політика конфіденційності</a><a href="#" data-cookie-settings>Налаштування cookie</a></span></div>
  </div>
</footer>
<button class="totop" id="totop" aria-label="Нагору">{ARR}</button>'''

SPRITE = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
{WM}
<symbol id="arrow" viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<linearGradient id="gFoot" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="272"><stop offset="0" stop-color="#A45CFF"/><stop offset=".3" stop-color="#8A31EF"/><stop offset="1" stop-color="#5E1CB0"/></linearGradient>
</defs></svg>'''

ORG_ID = SITE + "/#org"
def org_schema():
    return {
        "@type": ["Organization", "ProfessionalService"], "@id": ORG_ID,
        "name": BRAND, "alternateName": ["Perseus", "Персей", "Perseus Agency", "Perseus Digital"],
        "legalName": LEGAL, "url": SITE + "/", "email": EMAIL,
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/icons/icon-512.png", "width": 512, "height": 512},
        "image": OG_IMG,
        "description": "Digital-студія графічного дизайну та SMM для малого й середнього бізнесу та громадських організацій: дизайн-супровід, айдентика, соцмережі, презентації, рекламні креативи, поліграфія, дизайн сайтів.",
        "founder": {"@id": SITE + "/about/#ihor"},
        "address": {"@type": "PostalAddress", "addressCountry": "UA"},
        "areaServed": [{"@type": "Country", "name": "Україна"}, {"@type": "Place", "name": "Європа"}],
        "knowsLanguage": ["uk", "en"], "priceRange": "₴₴", "currenciesAccepted": "UAH, EUR, USD",
        "sameAs": [IG, TG, LI],
        "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "email": EMAIL, "url": TG, "availableLanguage": ["Ukrainian", "English"]},
    }

def page(path, title, desc, body, active=None, crumbs=None, schema=None, og_type="website", noindex=False, image=None):
    url = SITE + path
    crumbs = crumbs or []
    graph = [org_schema(), {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND, "inLanguage": "uk-UA", "publisher": {"@id": ORG_ID}},
             {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "uk-UA",
              "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}, "dateModified": TODAY}]
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Головна", "item": SITE + "/"}]
        for i, (n, u) in enumerate(crumbs, 2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": SITE + u})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    graph += schema or []
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    img = image or OG_IMG
    return f'''<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="uk" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#131D1E">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="uk_UA">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400;500;600;700&family=Unbounded:wght@600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={TODAY}">
<link rel="stylesheet" href="/assets/lead.css?v={TODAY}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
{SPRITE}
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/site.js?v={TODAY}" defer></script>
<script src="/assets/lead.js?v={TODAY}" defer></script>
</body>
</html>
'''

def crumbs_html(crumbs):
    li = '<li><a href="/">Головна</a></li>'
    for i, (n, u) in enumerate(crumbs):
        li += f'<li><a href="{u}">{n}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{n}</li>'
    return f'<ol class="crumbs" aria-label="Хлібні крихти">{li}</ol>'

def faq_html(items):
    return '<div class="faq">' + "".join(
        f'<details data-r><summary>{q}</summary><div class="a"><p>{a}</p></div></details>' for q, a in items) + '</div>'

def faq_schema(items):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}

def cta(title, text, primary=("Обговорити проєкт", TG, True), secondary=("Подивитися ціни", "/prices/"), lead=""):
    return f'''<section class="sec sec--tight"><div class="wrap"><div class="cta" data-r>
  <div><h2 class="d2">{title}</h2><p>{text}</p></div>
  <div class="btns">{btn(primary[0], primary[1], ext=primary[2], lead=lead)}{btn(secondary[0], secondary[1], "ghost") if secondary else ""}</div>
</div></div></section>'''

def marquee(words):
    s = "".join(f"<span>{w}</span>" for w in words)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee__track">{s}{s}</div></div>'

def write(path, content):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/404.html" else os.path.join(ROOT, "404.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)

PAGES = []  # (path, priority) для sitemap

def register(path, html_text, priority="0.8", sitemap=True):
    write(path, html_text)
    if sitemap:
        PAGES.append((path, priority))

def finish():
    urls = [("/", "1.0")] + PAGES
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p, pr in urls:
        sm += f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n"
    sm += "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /content/\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"OK: {len(urls)} URL у sitemap")

if __name__ == "__main__":
    import pages_services, pages_main  # noqa: E402
    import build as B  # той самий модуль, у який реєструють сторінки
    pages_services.build()
    pages_main.build()
    B.finish()
