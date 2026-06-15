from pathlib import Path
text = [f for f in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*.html") if f.stat().st_size > 100000][0].read_text(encoding="utf-8")
for key in ["Акция до", "Восстановите все", "Все зубы за"]:
    i = text.find(key)
    if i >= 0:
        Path(rf"C:\Users\nikar\OneDrive\Desktop\Lands\snip_{key[:10]}.txt").write_text(text[i-100:i+400], encoding="utf-8")
