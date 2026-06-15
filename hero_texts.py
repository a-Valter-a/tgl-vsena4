import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
m = re.search(r"rec1352094341.*?</div>\s*</div>\s*<script>t_onReady", text, re.DOTALL)
body = m.group(0) if m else ""
for match in re.finditer(r"data-elem-type='text'[^>]*>.*?class='tn-atom'[^>]*>(.*?)</div>", body, re.DOTALL):
    t = re.sub(r"<[^>]+>", "", match.group(1)).strip()
    if t:
        print(t)
