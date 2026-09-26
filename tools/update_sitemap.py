#!/usr/bin/env python3
"""Regenera sitemap.xml de exowise.ai a partir de los .html de la carpeta.
Uso: python3 tools/update_sitemap.py   (desde ~/Documents/Exowise-web)
Correr SIEMPRE despues de cualquier cambio en la web, y subir sitemap.xml junto con los archivos cambiados."""
import os, datetime, pathlib

BASE = "https://exowise.ai"
ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {"tools", "wp-content", ".git"}

def lastmod(p):
    return datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()

urls = []
home = ROOT / "index.html"
urls.append((BASE + "/", lastmod(home), "weekly", "1.0", True))
for p in sorted(ROOT.rglob("*.html")):
    rel = p.relative_to(ROOT)
    if rel.parts[0] in SKIP_DIRS or rel.name == "index.html" and len(rel.parts) == 1:
        continue
    loc = BASE + "/" + "/".join(rel.parts)
    urls.append((loc, lastmod(p), "monthly", "0.8", False))

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for loc, lm, cf, pr, alt in urls:
    x = f"<url><loc>{loc}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority>"
    if alt:
        x += (f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}/"/>'
              f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}/?lang=es"/>'
              f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>')
    out.append(x + "</url>")
out.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"sitemap.xml actualizado: {len(urls)} URLs")
