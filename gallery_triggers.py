from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
out = []
start = 0
while True:
    i = text.find("mygallery", start)
    if i < 0:
        break
    out.append(text[max(0, i-200):i+100])
    start = i + 1
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\gallery_triggers.txt").write_text("\n---\n".join(out), encoding="utf-8")
