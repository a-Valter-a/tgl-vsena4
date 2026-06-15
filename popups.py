import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
hooks = sorted(set(re.findall(r"#popup:[^\"']+", text)))
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\popups.txt").write_text("\n".join(hooks), encoding="utf-8")
