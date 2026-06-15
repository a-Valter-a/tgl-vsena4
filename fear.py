from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
idx = text.find("страх лечения")
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\fear_snip.txt").write_text(text[idx:idx+2500] if idx>=0 else "not found", encoding="utf-8")
