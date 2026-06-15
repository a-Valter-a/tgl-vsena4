import re
import json
from pathlib import Path
from html import unescape

p = Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source")
html_file = [f for f in p.rglob("*.html") if f.stat().st_size > 100000][0]
text = html_file.read_text(encoding="utf-8")

def strip_html(s):
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = unescape(s)
    return re.sub(r"[ \t]+", " ", s).strip()

# Split by records
parts = re.split(r'(<div id="rec\d+"[^>]*>)', text)
records = []
for i in range(1, len(parts), 2):
    tag = parts[i]
    body = parts[i + 1] if i + 1 < len(parts) else ""
    rid = re.search(r'id="(rec\d+)"', tag).group(1)
    rtype = re.search(r'data-record-type="(\d+)"', tag)
    rtype = rtype.group(1) if rtype else "?"
    records.append((rid, rtype, body))

for rid, rtype, body in records:
    print(f"\n{'='*60}\n{rid} type={rtype}")
    
    # artboard style
    m = re.search(r"#" + rid + r" \.t396__artboard \{([^}]+)\}", body)
    if m:
        print("ARTBOARD:", m.group(1)[:200])
    
    # all tn-atom text
    atoms = re.findall(r"class='tn-atom'[^>]*>(.*?)</div>", body, re.DOTALL)
    atoms += re.findall(r'class="tn-atom"[^>]*>(.*?)</div>', body, re.DOTALL)
    for a in atoms:
        t = strip_html(a)
        if t and len(t) > 1:
            print("TEXT:", t[:200])
    
    # images in record
    for img in re.findall(r"data-original=['\"]([^'\"]+)['\"]|src=['\"]([^'\"]+\.(?:webp|png|jpg|svg))['\"]", body):
        url = img[0] or img[1]
        if "tildacdn" in url or ".webp" in url or ".png" in url:
            print("IMG:", url[:120])
    
    # buttons
    for btn in re.findall(r"data-field-buttonname-value=['\"]([^'\"]+)['\"]", body):
        print("BTN:", btn)
    
    # quiz questions
    for q in re.findall(r'id="field-title_\d+"[^>]*>([^<]+)', body):
        print("QUIZ Q:", q)
    for opt in re.findall(r'<span>([^<]{1,80})</span></label>', body):
        if opt not in ("Я согласен на ", "Я согласен на получение "):
            print("OPT:", opt)
    
    # reviews
    for rev in re.findall(r'class="t728__text[^"]*"[^>]*>(.*?)</div>', body, re.DOTALL):
        t = strip_html(rev)
        if len(t) > 20:
            print("REVIEW:", t[:150])
    for name in re.findall(r'class="t728__title[^"]*"[^>]*>(.*?)</div>', body, re.DOTALL):
        print("REVIEWER:", strip_html(name))
    
    # map section
    for addr in re.findall(r'field="text"[^>]*>(.*?)</div>', body, re.DOTALL):
        t = strip_html(addr)
        if len(t) > 10:
            print("ADDR:", t[:200])
