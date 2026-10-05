#!/usr/bin/env python3
"""Copies site/ to preview/ for the Artifact tool: inlines fonts as data URIs and strips the
document wrapper that the Artifact tool adds itself."""
import base64, re, shutil
from pathlib import Path
root = Path(__file__).resolve().parent.parent
site, prev = root, root / "_preview"
shutil.rmtree(prev, ignore_errors=True); prev.mkdir()
for f in site.iterdir():
    if f.is_file() and f.name not in ("404.html", "robots.txt", "sitemap.xml"):
        shutil.copy(f, prev / f.name)
shutil.copytree(site / "images", prev / "images")
css = (site / "style.css").read_text()
def inline(m):
    data = base64.b64encode((site / m.group(1)).read_bytes()).decode()
    return f'url("data:font/woff2;base64,{data}")'
css = re.sub(r'url\("(fonts/[^"]+\.woff2)"\)', inline, css)
(prev / "style.css").write_text(css)
s = (prev / "index.html").read_text()
head = re.search(r"<head>(.*)</head>", s, re.S).group(1)
head = re.sub(r'<meta charset[^>]*>\s*<meta name="viewport"[^>]*>', "", head)
head = re.sub(r'<link rel="preload"[^>]*>\n', "", head)
body = re.search(r"<body>(.*)</body>", s, re.S).group(1)
(prev / "index.html").write_text(head + body)
print("preview ready", sum(f.stat().st_size for f in prev.iterdir()) // 1024, "KB")
