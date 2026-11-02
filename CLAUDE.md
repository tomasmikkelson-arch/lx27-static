# Perseus Digital Studio – сайт perseus.company

## Публікація
- Власник сайту дозволив публікувати зміни **одразу в гілку `main`** (GitHub Pages публікує сайт з `main`). Після завершення роботи – коміт і `git push origin HEAD:main`, без окремого погодження.
- Перед пушем: `git pull --rebase origin main` (GitHub Action може додати власний коміт з автозбіркою).

## Як влаштовано
- `index.html` – головна, редагується вручну (GSAP + Lenis, власні стилі всередині файлу).
- Решта сторінок генерується: `python3 -B tools/build.py` (Python 3, без обовʼязкових залежностей; PyYAML – опціонально).
  - `tools/build.py` – шаблон сторінки: шапка, футер, SEO-мета, JSON-LD, sitemap.xml, robots.txt.
  - `tools/pages_services.py` – /services/ і 7 сторінок послуг (тексти, FAQ, ціни).
  - `tools/pages_main.py` – /ngo/, /about/, /portfolio/, /prices/ (калькулятор), /contacts/, /privacy/, 404.
  - `tools/pages_blog.py` – блог із `content/blog/*.md` (front matter + Markdown), RSS.
  - `tools/reviews.py` – розділ «Відгуки» з `content/reviews.json`, вставляється в `index.html` між маркерами `<!-- REVIEWS:START -->` / `<!-- REVIEWS:END -->`. Показуються лише відгуки з `allowed: true`; якщо таких немає, розділ прихований. Демо дизайну: `/reviews-preview/` (noindex).
  - `tools/scenes.py` – CSS-ілюстрації для перших екранів і превʼю портфоліо.
  - `tools/privacy_body.html` – текст політики конфіденційності.
  - `tools/patch_index.py` – одноразовий скрипт, уже застосований; повторно не запускати.
- Не редагуйте згенеровані `*/index.html` вручну – правте джерело в `tools/` і перезбирайте.
- Спільні стилі/скрипти: `assets/site.css`, `assets/site.js`; pop-up заявки: `assets/lead.css`, `assets/lead.js` (атрибут `data-lead="контекст"` на будь-якій кнопці); відгуки: `assets/reviews.css`; футер: `assets/footer.css` (копія стилів футера головної – футер внутрішніх сторінок береться з `index.html` автоматично, тож правте його лише на головній і перезбирайте).
- Адмінка: Pages CMS (`.pages.yml`), вхід на https://app.pagescms.org через GitHub – колекції «Блог» і «Відгуки». Workflow `.github/workflows/build-site.yml` перезбирає сайт при змінах у `content/` або `tools/` і щодня (для відкладених статей).
- Мова сайту – українська. Реквізити: ФОП Ісиченко Ігор Володимирович.
- Після зміни текстів статичних сторінок оновіть `SITE_UPDATED` у `tools/build.py` (дата для sitemap).

## Важливо
- Публікувати лише реальні відгуки, кейси й цифри, погоджені з клієнтами. Не додавати вигадані імена, чужі фото чи логотипи організацій без дозволу – це порушує політику Google Ads (Misrepresentation) і закон про недобросовісну рекламу.
