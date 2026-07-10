#!/usr/bin/env python3
"""Add a 1000-object "World Collections" gallery to the Virtual Museum.

Unlike the other 13 hand-curated galleries, this gallery is generated
programmatically (country x object-type combinations, like the existing
adult_learning_data.py fallback generator) so it can honestly cover 1000
entries without fabricating specific museum pieces. Each card links out to
real, live Wikipedia/Wikimedia Commons search results rather than a guessed
specific artifact page. No age/safety gating is applied -- this gallery is
available to every learner, school through adult.

Re-run after editing:
    python3 backend/scripts/generate_museum_expansion.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.adult_learning_data import PLACES, OBJECT_TYPES, _region_for_index, _period_for_index

MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"

TARGET_COUNT = 1000


def _wikipedia(topic: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(topic).replace("+", "_")


def _wikipedia_search(topic: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(topic)


def _commons_search(topic: str) -> str:
    return "https://commons.wikimedia.org/w/index.php?search=" + quote_plus(topic)


def _youtube_search(topic: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(topic)


def build_objects(count: int) -> list[dict]:
    objects = []
    n = 0
    for place_index, place in enumerate(PLACES, start=1):
        for type_index, object_type in enumerate(OBJECT_TYPES, start=1):
            if n >= count:
                return objects
            n += 1
            name = f"{place} {object_type}"
            period = _period_for_index(place_index + type_index)
            region = _region_for_index(place_index)
            objects.append({
                "id": f"wc_{n:04d}",
                "name": name,
                "origin": place,
                "region": region,
                "year": period,
                "material": object_type,
                "category": object_type.lower().replace(" ", "_"),
                "description": (
                    f"A study card for exploring {object_type.lower()} traditions connected with {place}, "
                    f"covering makers, materials, and historical context from the {period.lower()} period."
                ),
                "significance": f"Represents the {object_type.lower()} tradition of {place} within {region}.",
                "fun_fact": f"Museums and collections worldwide hold {object_type.lower()} pieces from {place} spanning many centuries.",
                "museum": "Various world collections",
                "image_hint": f"A representative {object_type.lower()} associated with {place}",
                "educational_importance": f"Connects world history and art with the material culture of {place}.",
                "related_lesson": "World History",
                "activity": f"Research one real {object_type.lower()} from {place} and note its maker, material, and period.",
                "quiz": {
                    "question": f"Which country/region is this {object_type.lower()} card associated with?",
                    "options": [place, "Antarctica", "International Waters", "Unknown"],
                    "answer": 0,
                },
                "related_subjects": ["World History", "Art", "Geography"],
                "links": {
                    "wikipedia_search": _wikipedia_search(name),
                    "image_search": _commons_search(name),
                    "video": _youtube_search(f"{name} history documentary"),
                    "museum_channel": _youtube_search(f"{object_type} {place} museum tour"),
                },
                # No specific real photo exists for a generated "Place + Type" card, so this
                # points WikiThumbnail at the country's own real Wikipedia page/photo instead
                # of showing nothing -- an honest, real (if generic) thumbnail rather than none.
                "wiki_title": place,
            })
    return objects


def main() -> None:
    with open(MUSEUM_PATH, encoding="utf-8") as f:
        data = json.load(f)

    objects = build_objects(TARGET_COUNT)
    data["galleries"]["world_collections"] = {
        "label": "World Collections",
        "emoji": "🌐",
        "description": (
            f"{len(objects)} unrestricted study cards spanning {len(PLACES)} countries and "
            f"{len(OBJECT_TYPES)} object types, open to every learner from school through adult."
        ),
        "objects": objects,
    }

    with open(MUSEUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total = sum(len(g.get("objects", [])) for g in data["galleries"].values())
    print(f"Added {len(objects)} objects. Museum now has {total} objects across {len(data['galleries'])} galleries.")


if __name__ == "__main__":
    main()
