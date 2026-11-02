"""Блог: статті з content/blog/*.md → /blog/<slug>/ + /blog/.

Формат файлу (front matter):
---
title: Заголовок
slug: latin-url
description: Опис для Google (до 160 символів)
date: 2026-11-01
updated: 2026-11-05        # необов'язково
cover: /assets/blog/img.webp  # необов'язково
cover_alt: Опис зображення
category: Дизайн
tags: [SMM, Instagram]
draft: false
---
Текст у Markdown.
Статті з draft: true або з датою в майбутньому не публікуються.
"""
import os, re, html, math
from datetime import date
from build import ROOT, SITE, TG, ORG_ID, page, register, crumbs_html, cta, btn, link_arr, e, ARR

BLOG_DIR = os.path.join(ROOT, "content", "blog")

# ---------- front matter ----------
def _val(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        return [_val(x) for x in v[1:-1].split(",") if x.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v

def parse(text):
    meta, body = {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if m:
        try:
            import yaml
            meta = yaml.safe_load(m.group(1)) or {}
        except Exception:
            key = None
            for line in m.group(1).splitlines():
                if re.match(r"^\s+-\s+", line) and key:
                    meta.setdefault(key, [])
                    if not isinstance(meta[key], list):
                        meta[key] = []
                    meta[key].append(_val(re.sub(r"^\s+-\s+", "", line)))
                elif ":" in line and not line.startswith(" "):
                    key, v = line.split(":", 1)
                    key = key.strip()
                    meta[key] = _val(v) if v.strip() else []
        body = m.group(2)
    return meta, body

# ---------- мінімальний Markdown ----------
def _inline(s):
    if re.search(r"<[a-zA-Z/][^>]*>", s):  # вже HTML
        pass
    else:
        s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)", lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}"' + ('' if m.group(2).startswith(("/", "#")) or "perseus.company" in m.group(2) else ' target="_blank" rel="noopener"') + f'>{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
    return s

def slugify(s):
    tr = dict(zip("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя", ["a","b","v","h","g","d","e","ie","zh","z","y","i","i","i","k","l","m","n","o","p","r","s","t","u","f","kh","ts","ch","sh","shch","","iu","ia"]))
    s = "".join(tr.get(c, c) for c in s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70]

def md(text):
    out, para, lst, toc = [], [], None, []
    lines = text.replace("\r\n", "\n").split("\n")
    def flush():
        nonlocal para, lst
        if para:
            out.append("<p>" + _inline(" ".join(para)) + "</p>"); para = []
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{_inline(i)}</li>" for i in items) + f"</{tag}>"); lst = None
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush(); i += 1; continue
        h = re.match(r"^(#{2,4})\s+(.*)$", ln)
        if h:
            flush(); lvl = len(h.group(1)); t = h.group(2).strip()
            hid = slugify(t) or f"s{len(toc)}"
            if lvl == 2: toc.append((hid, re.sub(r"<[^>]+>", "", _inline(t))))
            out.append(f'<h{lvl} id="{hid}">{_inline(t)}</h{lvl}>'); i += 1; continue
        if re.match(r"^(-{3,}|\*{3,})$", ln.strip()):
            flush(); out.append("<hr>"); i += 1; continue
        if ln.startswith(">"):
            flush(); q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i].lstrip("> ").rstrip()); i += 1
            out.append("<blockquote>" + _inline(" ".join(q)) + "</blockquote>"); continue
        m_ul = re.match(r"^\s*[-*+]\s+(.*)$", ln); m_ol = re.match(r"^\s*\d+[.)]\s+(.*)$", ln)
        if m_ul or m_ol:
            if para: out.append("<p>" + _inline(" ".join(para)) + "</p>"); para = []
            tag = "ul" if m_ul else "ol"
            if not lst or lst[0] != tag:
                if lst: flush()
                lst = (tag, [])
            lst[1].append((m_ul or m_ol).group(1)); i += 1; continue
        if ln.lstrip().startswith("<") and not para:
            flush(); out.append(ln); i += 1; continue
        if lst:
            flush()
        para.append(ln.strip()); i += 1
    flush()
    return "\n".join(out), toc

def _date(v):
    if isinstance(v, date): return v
    try: return date.fromisoformat(str(v)[:10])
    except Exception: return date.today()

MONTHS = ["січня","лютого","березня","квітня","травня","червня","липня","серпня","вересня","жовтня","листопада","грудня"]
def human(d): return f"{d.day} {MONTHS[d.month-1]} {d.year}"

def load():
    posts = []
    if not os.path.isdir(BLOG_DIR): return posts
    for fn in sorted(os.listdir(BLOG_DIR)):
        if not fn.endswith(".md"): continue
        meta, body = parse(open(os.path.join(BLOG_DIR, fn), encoding="utf-8").read())
        if meta.get("draft") is True: continue
        d = _date(meta.get("date"))
        if d > date.today(): continue
        slug = meta.get("slug") or slugify(meta.get("title", "")) or slugify(fn[:-3])
        html_body, toc = md(body)
        words = len(re.sub(r"<[^>]+>", " ", html_body).split())
        tags = meta.get("tags") or []
        if isinstance(tags, str): tags = [t.strip() for t in tags.split(",") if t.strip()]
        posts.append(dict(meta=meta, slug=slugify(str(slug)) or "post", date=d, updated=_date(meta.get("updated") or d), html=html_body, toc=toc,
                          minutes=max(1, math.ceil(words / 180)), tags=tags, title=str(meta.get("title", "Без назви")),
                          desc=str(meta.get("description", ""))[:300], category=str(meta.get("category", "Блог"))))
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts

def card(p, i=0):
    return f'''<a class="card post-card" href="/blog/{p["slug"]}/" data-r="{i % 3 + 1}"><span class="eyebrow">{e(p["category"])}</span>
<h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><time datetime="{p["date"].isoformat()}">{human(p["date"])} · {p["minutes"]} хв</time>
<span class="more link-arr">Читати<i><svg aria-hidden="true"><use href="#arrow"/></svg></i></span></a>'''

def post_page(p, posts):
    path = f'/blog/{p["slug"]}/'
    crumbs = [("Блог", "/blog/"), (p["title"], path)]
    toc = ""
    if len(p["toc"]) >= 3:
        toc = '<nav class="toc-mini" aria-label="Зміст статті"><strong>Зміст</strong><ol>' + "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in p["toc"]) + "</ol></nav>"
    cover = p["meta"].get("cover")
    cover_html = f'<img src="{e(cover)}" alt="{e(str(p["meta"].get("cover_alt", p["title"])))}" style="border-radius:var(--r-md);margin:10px 0 24px;width:100%">' if cover else ""
    more = [x for x in posts if x is not p][:3]
    more_html = "".join(card(x, i) for i, x in enumerate(more))
    tags = "".join(f"<span>{e(t)}</span>" for t in p["tags"])
    body = f'''
<section class="hero" style="padding-bottom:20px"><div class="wrap article">
  {crumbs_html(crumbs)}
  <span class="eyebrow">{e(p["category"])}</span>
  <h1 class="d1" style="margin-top:18px;font-size:clamp(28px,4.6vw,58px)">{e(p["title"])}</h1>
  <p class="lead" style="margin-top:20px">{e(p["desc"])}</p>
  <div class="hero__facts" style="margin-top:20px"><span>{human(p["date"])}</span><span>{p["minutes"]} хв читання</span><span>Автор: Ігор Ісиченко</span></div>
</div></section>
<article class="sec sec--tight" style="padding-top:10px"><div class="wrap article prose">
  {cover_html}{toc}
  {p["html"]}
  <div class="chips" style="margin-top:30px">{tags}</div>
  <div class="cta" style="margin-top:40px;grid-template-columns:1fr"><div><h2 class="d2" style="font-size:clamp(22px,3vw,34px)">Потрібна допомога з дизайном?</h2><p>Розкажіть про задачу – відповімо протягом 2 годин у робочий час.</p></div>
  <div class="btns">{btn("Обговорити проєкт", TG, ext=True, lead="Блог: " + p["title"])}</div></div>
</div></article>
{f'<section class="sec sec--tight"><div class="wrap"><div class="sec__head"><div><span class="eyebrow">Блог</span><h2 class="d2">Читайте також</h2></div>{link_arr("Усі статті", "/blog/")}</div><div class="grid g3">{more_html}</div></div></section>' if more else ""}
'''
    img = SITE + cover if cover and str(cover).startswith("/") else (cover or SITE + "/assets/og-image.jpg")
    art = {"@type": "BlogPosting", "@id": SITE + path + "#article", "headline": p["title"][:110], "description": p["desc"],
           "datePublished": p["date"].isoformat(), "dateModified": p["updated"].isoformat(), "inLanguage": "uk-UA",
           "mainEntityOfPage": SITE + path, "image": img, "keywords": ", ".join(p["tags"]),
           "author": {"@type": "Person", "@id": SITE + "/about/#ihor", "name": "Ігор Ісиченко", "url": SITE + "/about/"},
           "publisher": {"@id": ORG_ID}, "wordCount": len(re.sub(r"<[^>]+>", " ", p["html"]).split())}
    register(path, page(path, (f'{p["title"]} | Perseus' if len(p["title"]) <= 52 else p["title"]), p["desc"], body, active="/blog/", crumbs=crumbs,
                        schema=[art], og_type="article", image=img, lastmod=p["updated"].isoformat()), "0.6", lastmod=p["updated"].isoformat())

def index(posts):
    from build import SITE_UPDATED
    newest = max([p["updated"].isoformat() for p in posts] + [SITE_UPDATED])
    path = "/blog/"
    crumbs = [("Блог", path)]
    cards = "".join(card(p, i) for i, p in enumerate(posts)) or '<p class="muted">Статті скоро з\'являться.</p>'
    body = f'''
<section class="hero" style="padding-bottom:30px"><div class="wrap">
  {crumbs_html(crumbs)}
  <span class="eyebrow">Блог</span>
  <h1 class="d1" data-split style="margin-top:18px">Блог про дизайн і <em>SMM</em></h1>
  <p class="lead" style="margin-top:22px">Практичні поради для малого бізнесу та громадських організацій: скільки коштує дизайн, як працювати з підрядником, як оформити матеріали за вимогами донорів.</p>
</div></section>
<section class="sec sec--tight"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
{cta("Маєте питання по дизайну?", "Напишіть нам – відповімо і, можливо, напишемо про це статтю.", lead="Блог")}
'''
    lst = {"@type": "Blog", "@id": SITE + path + "#blog", "url": SITE + path, "name": "Блог Perseus", "publisher": {"@id": ORG_ID},
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f'{SITE}/blog/{p["slug"]}/', "datePublished": p["date"].isoformat()} for p in posts]}
    register(path, page(path, "Блог Perseus: графічний дизайн, SMM і брендинг для бізнесу та ГО",
                        "Статті про графічний дизайн, SMM, брендинг і рекламу для малого й середнього бізнесу та громадських організацій. Ціни, поради, чек-листи.",
                        body, active="/blog/", crumbs=crumbs, schema=[lst], lastmod=newest), "0.7", lastmod=newest)

def build():
    posts = load()
    for p in posts:
        post_page(p, posts)
    index(posts)
    # RSS
    items = "".join(f'''<item><title>{e(p["title"])}</title><link>{SITE}/blog/{p["slug"]}/</link><guid>{SITE}/blog/{p["slug"]}/</guid>
<pubDate>{p["date"].strftime("%a, %d %b %Y")} 09:00:00 +0200</pubDate><description>{e(p["desc"])}</description></item>''' for p in posts)
    rss = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>Блог Perseus</title><link>{SITE}/blog/</link><description>Графічний дизайн і SMM для бізнесу та ГО</description><language>uk</language>{items}</channel></rss>
'''
    open(os.path.join(ROOT, "blog", "rss.xml"), "w", encoding="utf-8").write(rss)
