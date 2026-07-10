#!/usr/bin/env python3
"""Add a real Google Images *search* link (not a guessed direct image URL)
to every object in backend/data/virtual_museum/museum.json, as a
supplementary thumbnail/image-lookup resource alongside the existing
Wikimedia Commons image_search link and the live WikiThumbnail component
(which fetches real thumbnails from Wikipedia's REST API client-side using
each object's wiki_title).

Consistent with this project's no-fabrication rule, we link to a Google
Images *search* for the object's name (+ museum, when known, for
disambiguation) rather than guessing a specific direct image URL.

Re-run after editing / whenever new museum objects are added:
    python3 backend/scripts/add_museum_google_image_links.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"


def google_image_search(query: str) -> str:
    return "https://www.google.com/search?tbm=isch&q=" + quote_plus(query)


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    total = 0
    for gallery in data["galleries"].values():
        for obj in gallery.get("objects", []):
            total += 1
            name = obj.get("name") or obj.get("wiki_title") or ""
            museum = obj.get("museum", "")
            query = f"{name} {museum}".strip() if museum else name
            links = obj.setdefault("links", {})
            if not links.get("google_image_search"):
                links["google_image_search"] = google_image_search(query)
                updated += 1

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added google_image_search link to {updated} of {total} museum objects.")


if __name__ == "__main__":
    main()
