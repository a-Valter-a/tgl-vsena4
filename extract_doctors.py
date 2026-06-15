import re
from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
for name in ["Телятников", "Мананников", "Посмотреть"]:
    i = text.find(name)
    if i >= 0:
        print("===", name, "===\n", text[i-200:i+300], "\n")
