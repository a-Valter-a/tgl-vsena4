import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
m = re.search(r"rec1352094551.*?</div>\s*</div>\s*</div>\s*<script", text, re.DOTALL)
if m:
    for field in ["t433__title", "t433__descr", "t433__text"]:
        for match in re.finditer(rf'class="[^"]*{field}[^"]*"[^>]*>(.*?)</div>', m.group(0), re.DOTALL):
            t = re.sub(r"<[^>]+>", " ", match.group(1))
            t = re.sub(r"\s+", " ", t).strip()
            if t:
                print(field, ":", t[:200])

m2 = re.search(r"rec1352094481.*?</form>", text, re.DOTALL)
if m2:
    opts = re.findall(r'<span>([^<]{1,120})</span></label>', m2.group(0))
    for o in opts:
        print("OPT:", o)
