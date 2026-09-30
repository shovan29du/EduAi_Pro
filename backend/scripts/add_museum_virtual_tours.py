#!/usr/bin/env python3
"""Add a "virtual_tour" link to every Virtual Museum object, pointing at a
Google Arts & Culture search for the object's housing museum.

Most institutions represented in the museum data (British Museum, Louvre,
Smithsonian, Art Institute of Chicago, and so on) are Google Arts & Culture
partners with real 360-degree virtual tours and exhibit stories published
there. Rather than guessing a specific deep link per museum (which would
risk a broken or simply wrong URL for 300+ different institutions), this
follows the same "search link" convention already used everywhere else in
this file (YouTube, Wikimedia Commons, Google Images search) -- a search
query that reliably surfaces the relevant tour/story when one exists.

Re-run after editing:
    python3 backend/scripts/add_museum_virtual_tours.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"


def virtual_tour_search(museum: str) -> str:
    return "https://artsandculture.google.com/search?q=" + quote_plus(museum)


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    skipped = 0
    for gallery in data["galleries"].values():
        for obj in gallery.get("objects", []):
            museum = obj.get("museum")
            if not museum:
                skipped += 1
                continue
            obj.setdefault("links", {})["virtual_tour"] = virtual_tour_search(museum)
            updated += 1

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"virtual_tour links: {updated} objects updated, {skipped} skipped (no museum field)")


if __name__ == "__main__":
    main()
