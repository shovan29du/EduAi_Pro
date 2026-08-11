#!/usr/bin/env python3
"""Generates the desktop-shortcut icon files used by full_install.py, derived
from the app's existing PWA icon (frontend/public/pwa-512x512.png).

Produces:
    assets/icons/EduAi_Pro.ico   - Windows shortcut icon (multi-resolution)
    assets/icons/EduAi_Pro.icns  - macOS .app bundle icon
    assets/icons/EduAi_Pro.png   - Linux .desktop icon

Re-run after changing the source PWA icon:
    python3 scripts/generate_desktop_icons.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "frontend" / "public" / "pwa-512x512.png"
OUT_DIR = REPO_ROOT / "assets" / "icons"

ICO_SIZES = [16, 24, 32, 48, 64, 128, 256]
ICNS_SIZES = [16, 32, 64, 128, 256, 512]


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source icon not found: {SOURCE}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")

    ico_path = OUT_DIR / "EduAi_Pro.ico"
    source.save(ico_path, format="ICO", sizes=[(s, s) for s in ICO_SIZES])
    print(f"Wrote {ico_path}")

    icns_path = OUT_DIR / "EduAi_Pro.icns"
    source.save(icns_path, format="ICNS", sizes=[(s, s) for s in ICNS_SIZES])
    print(f"Wrote {icns_path}")

    png_path = OUT_DIR / "EduAi_Pro.png"
    source.resize((512, 512)).save(png_path, format="PNG")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
