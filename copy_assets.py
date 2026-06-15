import shutil
from pathlib import Path

src = None
for d in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*_files"):
    if d.is_dir() and not any(p.name.endswith("_files") for p in d.parents if p != d):
        # innermost _files with images
        if list(d.glob("*.webp")):
            src = d
            break

if not src:
    for d in Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\tilda-source").rglob("*_files"):
        if d.is_dir() and list(d.glob("*.webp")):
            src = d

dest = Path(r"C:\Users\nikar\OneDrive\Desktop\Lands\assets\images")
dest.mkdir(parents=True, exist_ok=True)

mapping = {
    "__.png.webp": "logo-header.webp",
    "photo.png": "logo-clinic.png",
    "white_january_realis.png.webp": "hero-bg.webp",
    "photo_2025-07-11_16-.png.webp": "hero-badge.webp",
    "555.png.webp": "icon-shield.webp",
    "embraced-senior-coup.png.webp": "hero-couple.webp",
    "portrait-senior-coup.png.webp": "hero-portrait.webp",
    "17bu_18.svg": "icon-gift.svg",
    "__2.png.webp": "license.webp",
    "__(1).png.webp": "logo-footer.webp",
    "1.png.webp": "footer-icon-1.webp",
    "2.png.webp": "footer-icon-2.webp",
}

for old, new in mapping.items():
    f = src / old
    if f.exists():
        shutil.copy2(f, dest / new)
        print("copied", new)

# review images from tildacdn URLs - use local if we have them, else keep CDN in HTML
print("src:", src)
print("files:", [p.name for p in dest.iterdir()])
