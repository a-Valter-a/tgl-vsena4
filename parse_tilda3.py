import re
import json
from pathlib import Path
from html import unescape

p = Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source")
html_file = [f for f in p.rglob("*.html") if f.stat().st_size > 100000][0]
text = html_file.read_text(encoding="utf-8")
out = Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\content.json")

def strip_html(s):
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = unescape(s)
    return re.sub(r"\s+", " ", s).strip()

parts = re.split(r'(<div id="rec\d+"[^>]*>)', text)
records = []
for i in range(1, len(parts), 2):
    tag = parts[i]
    body = parts[i + 1] if i + 1 < len(parts) else ""
    rid = re.search(r'id="(rec\d+)"', tag).group(1)
    rtype = re.search(r'data-record-type="(\d+)"', tag)
    rtype = rtype.group(1) if rtype else "?"
    rec = {"id": rid, "type": rtype, "texts": [], "images": [], "buttons": [], "styles": []}
    m = re.search(r"#" + rid + r" \.t396__artboard \{([^}]+)\}", body)
    if m:
        rec["artboard"] = m.group(1)
    atoms = re.findall(r"class=['\"]tn-atom['\"][^>]*>(.*?)</div>", body, re.DOTALL)
    for a in atoms:
        t = strip_html(a)
        if t and len(t) > 1:
            rec["texts"].append(t)
    for img in re.findall(r"(?:data-original|src)=['\"]([^'\"]+)['\"]", body):
        if any(x in img for x in [".webp", ".png", ".jpg", ".svg", "tildacdn"]):
            if img not in rec["images"]:
                rec["images"].append(img)
    for btn in re.findall(r"data-field-buttonname-value=['\"]([^'\"]+)['\"]", body):
        rec["buttons"].append(btn)
    # popup
    pt = re.search(r'id="popuptitle_\d+">([^<]+)', body)
    if pt:
        rec["popup_title"] = pt.group(1)
    # quiz
    qs = re.findall(r'class="t-input-title[^"]*"[^>]*>([^<]+)', body)
    if qs:
        rec["quiz_questions"] = qs
    # reviews
    revs = []
    for block in re.findall(r'class="t728__wrapper"(.*?</div>\s*</div>\s*</div>)', body, re.DOTALL):
        txt = re.search(r'class="t728__text[^"]*"[^>]*>(.*?)</div>', block, re.DOTALL)
        name = re.search(r'class="t728__title[^"]*"[^>]*>(.*?)</div>', block, re.DOTALL)
        if txt:
            revs.append({"text": strip_html(txt.group(1)), "name": strip_html(name.group(1)) if name else ""})
    if revs:
        rec["reviews"] = revs
    # map coords
    mc = re.search(r'data-map-x="([^"]+)"[^>]*data-map-y="([^"]+)"', body)
    if mc:
        rec["map"] = {"lat": mc.group(1), "lng": mc.group(2)}
    records.append(rec)

out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print("written", out)
