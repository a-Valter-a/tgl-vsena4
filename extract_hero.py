import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
ids = ["1750420763552", "1750417885676", "1750861082363", "1750861082376", "1750861082384"]
out = []
for eid in ids:
    m = re.search(r"data-elem-id='" + eid + r"'[^>]*>.*?class='tn-atom'[^>]*>(.*?)</div>\s*</div>", text, re.DOTALL)
    if m:
        out.append(f"=== {eid} ===\n" + m.group(1))
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\hero_html.txt").write_text("\n\n".join(out), encoding="utf-8")
