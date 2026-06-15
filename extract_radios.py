import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
m = re.search(r"rec1352094481.*?</form>", text, re.DOTALL)
radios = re.findall(r'<input type="radio"[^>]*value="([^"]+)"[^>]*>\s*<div class="t-radio__indicator"[^>]*></div>\s*<span>([^<]*)</span>', m.group(0))
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\quiz_radios.txt").write_text("\n".join(f"{v} | {s}" for v,s in radios), encoding="utf-8")
