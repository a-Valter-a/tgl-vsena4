from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
i = text.find("mygallery")
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\gallery_snip.txt").write_text(text[max(0,i-500):i+800], encoding="utf-8")
