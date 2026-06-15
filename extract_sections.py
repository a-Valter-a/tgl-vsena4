import re, json
from pathlib import Path
from html import unescape

html_file = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0]
text = html_file.read_text(encoding="utf-8")

for rid in ["rec1352094341", "rec1352094461", "rec1352094551", "rec1352094481", "rec1352094521", "rec1352096161"]:
    m = re.search(r'<div id="' + rid + r'"[^>]*>(.*?)(?=<div id="rec|<footer|</body>)', text, re.DOTALL)
    if not m:
        continue
    body = m.group(1)
    styles = re.findall(r"<style>([^<]+)</style>", body)
    Path(rf"C:\Users\nikar\OneDrive\Desktop\Lands\section_{rid}.txt").write_text(
        "STYLES:\n" + "\n---\n".join(styles[:8]) + "\n\nBODY SNIP:\n" + body[:8000],
        encoding="utf-8"
    )

# quiz options
m = re.search(r'rec1352094481.*', text, re.DOTALL)
if m:
    opts = re.findall(r'<span>([^<]{1,100})</span></label>', m.group(0)[:50000])
    Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\quiz_opts.txt").write_text("\n".join(opts), encoding="utf-8")
