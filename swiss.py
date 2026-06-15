from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
i = text.find("швейцар")
Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\snip_swiss.txt").write_text(text[i-50:i+500] if i>=0 else "no", encoding="utf-8")
