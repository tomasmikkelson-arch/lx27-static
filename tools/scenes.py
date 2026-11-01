"""CSS-ілюстрації (сцени) для перших екранів і превʼю портфоліо."""

def _tiles(colors):
    return "".join(f'<b style="background:{c}"></b>' for c in colors)

PAL = ["#8A31EF", "#F3E6D8", "#FF6016", "#FFC94A", "#A45CFF", "#1F1233", "#CDB0FF", "#FF6016", "#8A31EF",
       "#F3E6D8", "#FFC94A", "#7D71F7", "#FF6016", "#A45CFF", "#F3E6D8"]

def phone(style="", cls="fl", tiles=None):
    return f'''<div class="ph sc-abs {cls}" style="{style}"><div class="ph__top"><i></i>your.brand</div>
<div class="ph__grid">{_tiles(tiles or PAL)}</div></div>'''

def slide(title="Виручка зросла втричі", style="", cls="fl2"):
    return f'''<div class="slide sc-abs {cls}" style="{style}"><div><h4>{title}</h4><div class="ln" style="width:90%"></div><div class="ln" style="width:70%"></div><div class="ln" style="width:80%"></div></div>
<div class="bars"><i style="height:35%"></i><i style="height:55%"></i><i style="height:48%"></i><i style="height:90%"></i></div></div>'''

def ads(style="", cls="fl3"):
    return f'''<div class="ads sc-abs {cls}" style="{style}">
<div class="ad" style="width:90px;aspect-ratio:1;background:linear-gradient(140deg,#8A31EF,#A45CFF)"><em>1:1</em>-20%<span>Купити</span></div>
<div class="ad" style="width:96px;aspect-ratio:4/5;background:linear-gradient(140deg,#FF6016,#FFC94A)"><em>4:5</em>Новий сезон<span>Дивитись</span></div>
<div class="ad" style="width:84px;aspect-ratio:9/16;background:linear-gradient(160deg,#1F1233,#8A31EF)"><em>9:16</em>Заявки з реклами<span>Детальніше</span></div></div>'''

def spread(style="", cls="fl"):
    return f'''<div class="spread sc-abs {cls}" style="{style}"><div><h4>Каталог 2026</h4><div class="img" style="background:linear-gradient(140deg,#A45CFF,#1F1233)"></div></div>
<div><h4>Колекція</h4><div class="img"></div><div class="ln"></div><div class="ln" style="width:70%"></div></div></div>'''

def brand_board(style="", cls="fl"):
    p = ('<svg viewBox="140 40 245 290" aria-hidden="true"><path fill="#fff" fill-rule="evenodd" d="M241.286 132.325V280.925L194.104 322.532V132.325H241.286Z"/>'
         '<path fill="#fff" fill-rule="evenodd" d="M153.808 52.1067L152.352 50.6297L154.411 50.6094H302.387C342.662 50.6094 375.303 83.271 375.303 123.547C375.303 163.801 342.662 196.462 302.387 196.462H195.165V153.108H303.094C319.424 153.108 332.655 139.877 332.655 123.547C332.655 107.216 319.424 93.9635 303.094 93.9635H195.664L153.808 52.1067Z"/></svg>')
    return f'''<div class="bb sc-abs {cls}" style="{style}"><div class="big">{p}</div>
<div style="background:#FF6016">Aa</div><div style="background:#F3E6D8;color:#131D1E">#F3</div>
<div style="background:#FFC94A;color:#131D1E">✦</div><div style="background:#1F1233">Ag</div><div style="background:#A45CFF">●</div></div>'''

def browser(style="", cls="fl"):
    return f'''<div class="browser sc-abs {cls}" style="{style}"><div class="browser__bar"><i></i><i></i><i></i></div>
<div class="browser__body"><div class="browser__hero">Ваш бренд онлайн</div><div class="ln" style="width:60%"></div><div class="ln" style="width:40%"></div>
<div class="browser__cols"><b></b><b style="background:#CDB0FF"></b><b style="background:#FFC94A"></b></div></div></div>'''

def report(style="", cls="fl", title="Річний звіт 2025"):
    return f'''<div class="report sc-abs {cls}" style="{style}"><h4>{title}</h4><div class="ln" style="width:80%"></div><div class="ln" style="width:60%"></div>
<div class="donut" style="margin:6px auto"></div><div class="ln"></div><div class="ln" style="width:75%"></div>
<div class="logos-row"><i></i><i></i><i></i><i></i></div></div>'''

def scene(kind):
    """Повна сцена для першого екрана."""
    inner = {
        "support": phone("left:8%;top:12%;width:40%") + slide(style="right:5%;top:16%;width:52%") + ads("right:8%;bottom:9%"),
        "branding": brand_board("left:8%;top:8%"),
        "smm": phone("left:27%;top:7%;width:46%") + f'<div class="sc-abs fl3" style="right:6%;top:18%;background:#fff;color:#131D1E;border-radius:14px;padding:10px 14px;font-weight:700;font-size:13px;box-shadow:0 20px 40px rgba(0,0,0,.35)">♥ 1 248</div><div class="sc-abs fl2" style="left:6%;bottom:16%;background:#FF6016;color:#fff;border-radius:14px;padding:10px 14px;font-weight:700;font-size:13px;box-shadow:0 20px 40px rgba(0,0,0,.35)">+34% охоплення</div>',
        "slides": slide("Pitch deck", "left:6%;top:10%;width:70%", "fl3") + slide("Ринок і клієнти", "left:16%;top:30%;width:70%", "fl2") + slide("Виручка зросла втричі", "left:24%;top:52%;width:70%", "fl"),
        "ads": ads("left:50%;top:50%;transform:translate(-50%,-50%) scale(1.5)", ""),
        "print": spread("left:9%;top:22%;width:82%"),
        "web": browser("left:7%;top:14%") + phone("right:6%;bottom:6%;width:28%", "fl3"),
        "ngo": report("left:8%;top:10%") + slide("Результати проєкту", "right:5%;bottom:10%;width:52%", "fl3"),
        "about": phone("left:8%;top:12%;width:40%") + brand_board("right:4%;top:10%;width:46%", "fl3"),
    }[kind]
    return f'<div class="scene" data-r aria-hidden="true">{inner}</div>'

def cover(kind, bg):
    """Превʼю для портфоліо (заглушка до реальних робіт)."""
    inner = {
        "smm": phone("position:relative;width:38%", "fl"),
        "branding": brand_board("position:relative;width:46%", ""),
        "slides": slide("Pitch deck", "position:relative;width:72%", ""),
        "ads": ads("position:relative", ""),
        "print": spread("position:relative;width:70%", ""),
        "web": browser("position:relative;width:76%", ""),
        "ngo": report("position:relative;width:40%", "", "Звіт для донора"),
    }[kind]
    return f'<div class="work__cover" style="background:{bg}">{inner}</div>'
