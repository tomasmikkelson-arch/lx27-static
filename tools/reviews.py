"""Розділ «Відгуки».

Відгуки зберігаються в content/reviews.json (редагуються через Pages CMS).
На головній розділ зʼявляється автоматично між маркерами
<!-- REVIEWS:START --> і <!-- REVIEWS:END -->, щойно є хоча б один відгук
з allowed=true (клієнт погодився на публікацію).
Демо-сторінка /reviews-preview/ показує дизайн на явно позначених прикладах (noindex).
"""
import json, os, re
from build import ROOT, TG, e, page, write

DATA = os.path.join(ROOT, "content", "reviews.json")

DEMO = [
    ("Ім'я Прізвище", "Власниця кав'ярні", "Бізнес", "Соцмережі", "Приклад відгуку: стрічка нарешті виглядає як один бренд, а шаблони дозволяють нам самим робити швидкі анонси."),
    ("Ім'я Прізвище", "Керівниця громадської організації", "ГО", "Звіт для донора", "Приклад відгуку: команда врахувала всі вимоги видимості донора, звіт погодили з першого разу."),
    ("Ім'я Прізвище", "Маркетолог, виробнича компанія", "Бізнес", "Каталог", "Приклад відгуку: каталог на 48 сторінок зверстали за два тижні, друкарня прийняла файли без жодного зауваження."),
    ("Ім'я Прізвище", "Засновник стартапу", "Бізнес", "Pitch deck", "Приклад відгуку: презентація стала зрозумілою за п'ять хвилин читання – саме те, що потрібно інвесторам."),
    ("Ім'я Прізвище", "Комунікаційниця благодійного фонду", "ГО", "Інформаційна кампанія", "Приклад відгуку: візуал кампанії зібрали в одну систему, а шаблони команда використовує досі."),
    ("Ім'я Прізвище", "Власник інтернет-магазину", "Бізнес", "Рекламні креативи", "Приклад відгуку: нові креативи щотижня – і таргетологу є що тестувати."),
    ("Ім'я Прізвище", "Менеджерка проєкту ГО", "ГО", "Посібник", "Приклад відгуку: посібник верстали в дедлайн, з українською та англійською версіями."),
    ("Ім'я Прізвище", "Директорка ресторану", "Бізнес", "Меню і POS", "Приклад відгуку: меню, флаєри та сторіз тепер в одному стилі."),
]

def load():
    try:
        data = json.load(open(DATA, encoding="utf-8"))
    except (OSError, ValueError):
        return []
    out = []
    for r in data.get("reviews", []):
        if not r.get("allowed") or not str(r.get("text", "")).strip() or not str(r.get("name", "")).strip():
            continue
        out.append(r)
    return out

def initials(name):
    parts = [p for p in re.split(r"\s+", name.strip()) if p]
    return "".join(p[0] for p in parts[:2]).upper() or "•"

def card(r, demo=False):
    name = str(r.get("name", ""))
    who = ", ".join(x for x in [str(r.get("role", "")), str(r.get("org", ""))] if x.strip())
    photo = r.get("photo")
    ava = (f'<img class="rv-card__ava" src="{e(photo)}" alt="{e(name)}" width="52" height="52" loading="lazy">' if photo
           else f'<span class="rv-card__ava" aria-hidden="true">{e(initials(name))}</span>')
    tag = "ГО" if r.get("org_type") == "ГО" else "Бізнес"
    rating = int(r.get("rating") or 5)
    svc = f'<span class="rv-card__svc">{e(str(r["service"]))}</span>' if r.get("service") else ""
    badge = '<span class="rv-demo-badge">Демо</span>' if demo else ""
    return f'''<figure class="rv-card">{badge}<div class="rv-card__top"><span class="rv-card__q" aria-hidden="true">“</span><span class="rv-card__tag">{tag}</span></div>
<blockquote class="rv-card__text">{e(str(r["text"]))}</blockquote>
<figcaption class="rv-card__who">{ava}<span><b>{e(name)}</b><small>{e(who)}</small>{svc}<span class="rv__stars" aria-label="Оцінка {rating} з 5">{"★" * rating}</span></span></figcaption></figure>'''

def section(reviews, demo=False):
    n = len(reviews)
    if n == 0:
        return ""
    cards = [card(r, demo) for r in reviews]
    static = n < 4
    if static:
        rows = f'<div class="rv__row"><div class="rv__track">{"".join(cards)}</div></div>'
    else:
        half = (n + 1) // 2
        a, b = cards[:half], cards[half:] or cards[:half]
        # дублюємо, щоб стрічка йшла безшовно
        rows = (f'<div class="rv__row"><div class="rv__track" style="--rv-dur:{max(40, len(a) * 12)}s">{"".join(a * 2)}</div></div>'
                f'<div class="rv__row rv__row--rev"><div class="rv__track" style="--rv-dur:{max(40, len(b) * 12)}s">{"".join(b * 2)}</div></div>')
    avg = sum(int(r.get("rating") or 5) for r in reviews) / n
    return f'''<link rel="stylesheet" href="/assets/reviews.css">
<section class="rv{' rv--static' if static else ''}" id="reviews" aria-labelledby="rvTitle">
  <div class="wrap">
    <div class="rv__head">
      <div><span class="eyebrow">Відгуки</span><h2 class="rv__title" id="rvTitle">Що кажуть <em>клієнти</em></h2></div>
      <div class="rv__sum"><b>{avg:.1f}</b><div><span class="rv__stars" aria-hidden="true">★★★★★</span><small>{n} {"відгук" if n % 10 == 1 and n % 100 != 11 else ("відгуки" if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else "відгуків")} від бізнесу та ГО</small></div></div>
    </div>
  </div>
  <div class="rv__rows">{rows}</div>
  <div class="wrap"><p class="rv__foot">Працювали з нами? Будемо вдячні за ваш відгук – <a href="{TG}" target="_blank" rel="noopener" style="text-decoration:underline">напишіть у Telegram</a>.</p></div>
</section>'''

def inject_index():
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    m = re.search(r"<!-- REVIEWS:START -->.*?<!-- REVIEWS:END -->", s, re.S)
    if not m:
        return
    html = section(load())
    new = f"<!-- REVIEWS:START -->\n{html}\n<!-- REVIEWS:END -->" if html else "<!-- REVIEWS:START --><!-- REVIEWS:END -->"
    if new != m.group(0):
        s = s[:m.start()] + new + s[m.end():]
        open(p, "w", encoding="utf-8").write(s)

def preview():
    demo = [dict(name=n, role=r, org="", org_type=t, service=sv, text=x, rating=5) for n, r, t, sv, x in DEMO]
    body = f'''<section class="hero" style="padding-bottom:0"><div class="wrap">
<span class="eyebrow">Службова сторінка</span>
<h1 class="d1" style="margin-top:16px;font-size:clamp(28px,4vw,52px)">Демо розділу «Відгуки»</h1>
<p class="lead" style="margin-top:18px">Це приклад дизайну з вигаданими текстами – він не показується відвідувачам і не індексується. На головній розділ зʼявиться автоматично, щойно в адмінці буде додано реальний відгук з позначкою «Клієнт погодився на публікацію».</p>
</div></section>
{section(demo, demo=True)}'''
    write("/reviews-preview/", page("/reviews-preview/", "Демо: відгуки – Perseus", "Службова сторінка.", body, noindex=True))

def build():
    inject_index()
    preview()
