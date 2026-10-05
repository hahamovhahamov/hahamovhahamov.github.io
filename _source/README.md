# Site source

`build.py` regenerates every HTML page, 404.html, favicon.svg, robots.txt and sitemap.xml
in the repo root. Run `python3 _source/build.py` (needs Pillow). `style.css` is hand-edited
and not generated. `make_preview.py` builds a self-contained preview for review.

Do not delete `google*.html` (Search Console verification), `Hahamovitch-CV.pdf`,
`headshot.jpg`, `images/` or `fonts/`.
If a custom domain is added, change `SITE_URL` in build.py.
