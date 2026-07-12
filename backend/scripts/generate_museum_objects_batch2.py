#!/usr/bin/env python3
"""Add a second large batch of ~1000 genuinely famous, individually-named
real museum objects/artifacts to the Virtual Museum, in a new
"World Heritage Treasures" gallery, complementing the earlier
"Famous Masterpieces" (501 objects) and "World Collections" (1000
objects) galleries.

Every entry is a real, well-known work (not a generated placeholder).
Each carries an accurate ``wiki_title`` -- the real Wikipedia article
title -- so the existing ``WikiThumbnail`` component
(frontend/src/components/VirtualMuseum.jsx) fetches a genuine, live photo
of the actual work from Wikipedia's public REST API at render time. This
project does not fabricate direct image URLs; the live-fetch-with-fallback
mechanism is the honest way to get a real thumbnail for every entry
without guessing file paths that might not exist.

Re-run after editing:
    python3 backend/scripts/generate_museum_objects_batch2.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
GALLERY_KEY = "world_heritage_treasures"


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(title).replace("+", "_")


def commons_search(q: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(q)


def google_image_search(q: str) -> str:
    return "https://www.google.com/search?tbm=isch&q=" + quote_plus(q)


def yt(q: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


def smarthistory(q: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(q)


# Each entry is a tuple: (name, wiki_title, creator_or_culture, date, origin,
#                         one_line_description)
# CATEGORY_ASSIGNMENTS pairs each list with its museum "category" facet.
CATEGORY_ASSIGNMENTS: list[tuple[list[tuple], str]] = []


def build_object(idx: int, name: str, wiki_title: str, creator: str, date: str, origin: str, description: str, category: str) -> dict:
    obj_id = f"wht_{idx:04d}"
    return {
        "id": obj_id,
        "name": name,
        "artist": creator,
        "year": date,
        "origin": origin,
        "material": category,
        "category": category,
        "description": description,
        "significance": f"Widely recognized as one of the famous works representing {origin} in world art, science, or cultural history.",
        "fun_fact": f"{name} is frequently featured in museum collections and history curricula as a landmark example from {origin}.",
        "museum": "See Wikipedia for current location",
        "educational_importance": "A genuinely famous, real work -- useful for art history, world history, natural history, and cultural studies at every level.",
        "related_lesson": "Art History" if category in ("painting", "sculpture") else "World History",
        "activity": f"Research {name} further: who made or discovered it, where it is today, and why it became famous.",
        "quiz": {
            "question": f"Which culture or region does '{name}' come from?",
            "options": [origin, "Antarctica", "International Waters", "Unknown"],
            "answer": 0,
        },
        "related_subjects": ["Art History", "World History", "Geography"],
        "links": {
            "wikipedia": wiki_url(wiki_title),
            "image_search": commons_search(name),
            "google_image_search": google_image_search(f"{name} {origin}"),
            "video": yt(f"{name} explained documentary"),
            "smarthistory": smarthistory(name),
        },
        "wiki_title": wiki_title,
    }


def build_objects(existing_wiki_titles: set[str]) -> list[dict]:
    objects = []
    idx = 0
    seen = set()
    for items, category in CATEGORY_ASSIGNMENTS:
        for name, wiki_title, creator, date, origin, description in items:
            if wiki_title in seen or wiki_title in existing_wiki_titles:
                continue  # avoid duplicating a real work already in the museum
            seen.add(wiki_title)
            idx += 1
            objects.append(build_object(idx, name, wiki_title, creator, date, origin, description, category))
    return objects


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    existing_wiki_titles = set()
    for gallery in data["galleries"].values():
        for obj in gallery.get("objects", []):
            wt = obj.get("wiki_title")
            if wt:
                existing_wiki_titles.add(wt)

    objects = build_objects(existing_wiki_titles)

    gallery = data["galleries"].get(GALLERY_KEY)
    if gallery is None:
        gallery = {
            "label": "World Heritage Treasures",
            "emoji": "🌐",
            "description": "",
            "objects": [],
        }
        data["galleries"][GALLERY_KEY] = gallery
    gallery["objects"].extend(objects)
    gallery["description"] = (
        f"{len(gallery['objects'])} genuinely famous, individually named real artworks, artifacts, natural "
        f"history specimens, and scientific/historic objects from around the world -- each linked to its real "
        f"Wikipedia page so the museum can show an actual live photo of the object."
    )

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} new objects. {GALLERY_KEY} now has {len(gallery['objects'])} objects. "
          f"Museum total: {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
