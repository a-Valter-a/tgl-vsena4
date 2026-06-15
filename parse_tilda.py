import re
from pathlib import Path

p = Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source")
html_files = [
    f for f in p.rglob("*.html")
    if "saved_resource" not in f.name and f.stat().st_size > 100000
]
html_file = html_files[0]
text = html_file.read_text(encoding="utf-8")

recs = re.findall(r'<div id="(rec\d+)"[^>]*data-record-type="(\d+)"', text)
print("RECORDS:", len(recs))
for rid, rtype in recs:
    print(f"  {rid} type={rtype}")

# inline artboard styles
styles = re.findall(r"<style>(#rec\d+[^<]+)</style>", text)
print("\nINLINE STYLES:", len(styles))
for s in styles[:15]:
    print(" ", s[:120])

# popup title
popups = re.findall(r'id="popuptitle_\d+">([^<]+)', text)
print("\nPOPUPS:", popups)

# section titles
for m in re.finditer(r't-section__title[^>]*>.*?field="btitle"[^>]*>(.*?)</div>\s*</div>', text, re.DOTALL):
    clean = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    if clean:
        print("TITLE:", clean[:100])

# t396 text elements
texts = re.findall(r"data-elem-type='text'[^>]*>.*?<div class='tn-atom'[^>]*>(.*?)</div>", text, re.DOTALL)
print("\nT396 TEXTS:", len(texts))
for t in texts[:25]:
    clean = re.sub(r"<[^>]+>", " ", t)
    clean = re.sub(r"\s+", " ", clean).strip()
    if clean and len(clean) > 3:
        print(" ", clean[:120])

# images
imgs = sorted(set(re.findall(r'src="\./([^"]+)"', text)))
print("\nLOCAL IMAGES:", len(imgs))
for img in imgs:
    print(" ", img)
