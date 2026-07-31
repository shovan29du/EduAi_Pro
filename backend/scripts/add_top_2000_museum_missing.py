#!/usr/bin/env python3
"""Add 2,000 missing objects from the bundled CMA open-access source list.

The top 2,000 records are exhausted first. Because that range contains fewer
than 2,000 titles absent from the existing museum, selection then continues
in source order. The output is deterministic and idempotent.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_PATH = BASE_DIR / "data" / "museum_objects.json"
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
GALLERY_KEY = "top_2000_additions"
SOURCE_LIMIT = 5_000
TARGET_COUNT = 2_000


def normalize(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def first_text(value, fallback="Unknown") -> str:
    if isinstance(value, list):
        return next((str(item).strip() for item in value if str(item).strip()), fallback)
    return str(value).strip() if value else fallback


def category_for(object_type: str | None) -> str:
    value = (object_type or "").lower()
    mappings = (
        ("paint", "painting"), ("draw", "painting"), ("print", "painting"),
        ("sculpt", "sculpture"), ("ceramic", "ceramic"), ("porcelain", "ceramic"),
        ("manuscript", "manuscript"), ("volume", "manuscript"),
        ("textile", "textile"), ("tapestry", "textile"),
        ("jewel", "jewelry"), ("silver", "metalwork"), ("metal", "metalwork"),
        ("armor", "weapon"), ("weapon", "weapon"),
        ("furniture", "decorative art"), ("glass", "decorative art"),
        ("mask", "ritual object"),
    )
    return next((category for needle, category in mappings if needle in value), "museum object")


def search_url(base: str, query: str) -> str:
    return base + quote_plus(query)


def build_object(source: dict, rank: int) -> dict:
    title = str(source.get("title") or "Untitled object").strip()
    origin = first_text(source.get("country") or source.get("culture"))
    object_type = str(source.get("type") or "Museum object")
    category = category_for(object_type)
    creator = str(source.get("creator") or "Unknown maker")
    source_url = source.get("url")
    query = f"{title} {creator} Cleveland Museum of Art"
    return {
        "id": f"top2k_{source['id']}",
        "name": title,
        "artist": creator,
        "year": str(source.get("date") or "Date unknown"),
        "origin": origin,
        "material": object_type,
        "category": category,
        "description": str(source.get("description") or f"{title}, held by the Cleveland Museum of Art."),
        "significance": (
            f"Ranked #{rank} in the bundled top-2000 Cleveland Museum of Art "
            "open-access source list and not previously present in EduAI_Pro's Virtual Museum."
        ),
        "fun_fact": (
            "The Cleveland Museum of Art publishes this object's record and image "
            "through its open-access collection."
        ),
        "museum": "Cleveland Museum of Art",
        "educational_importance": (
            f"A primary museum record useful for studying {category}, material culture, "
            "art history, provenance, and visual analysis."
        ),
        "related_lesson": "Museum Studies and Visual Analysis",
        "activity": (
            f"Study {title}. Identify its materials, intended use, visual features, "
            "historical context, and the evidence recorded by the museum."
        ),
        "quiz": {
            "question": f"Which museum provides the open-access record for '{title}'?",
            "options": [
                "Cleveland Museum of Art",
                "A fictional private collection",
                "No museum source is recorded",
                "An unidentified auction listing",
            ],
            "answer": 0,
        },
        "related_subjects": ["Art History", "World History", "Museum Studies"],
        "links": {
            "museum_object": source_url,
            "wikipedia": search_url("https://en.wikipedia.org/w/index.php?search=", query),
            "image_search": search_url(
                "https://commons.wikimedia.org/w/index.php?search=", query
            ),
            "google_image_search": search_url(
                "https://www.google.com/search?tbm=isch&q=", query
            ),
            "video": search_url(
                "https://www.youtube.com/results?search_query=", f"{query} explained"
            ),
            "smarthistory": search_url("https://smarthistory.org/?s=", title),
        },
        "thumbnail_local": source.get("image"),
        "source": "Cleveland Museum of Art Open Access",
        "source_rank": rank,
        "source_id": source["id"],
    }


def main() -> None:
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    source_objects = source.get("objects", source)[:SOURCE_LIMIT]
    museum = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    existing_names = {
        normalize(obj.get("name"))
        for gallery_id, gallery in museum["galleries"].items()
        if gallery_id != GALLERY_KEY
        for obj in gallery.get("objects", [])
    }

    selected = []
    seen = set(existing_names)
    for rank, item in enumerate(source_objects, start=1):
        title_key = normalize(item.get("title"))
        if not title_key or title_key in seen:
            continue
        selected.append(build_object(item, rank))
        seen.add(title_key)
        if len(selected) == TARGET_COUNT:
            break
    if len(selected) != TARGET_COUNT:
        raise RuntimeError(
            f"Only {len(selected)} eligible missing objects found; expected {TARGET_COUNT}"
        )

    museum["galleries"][GALLERY_KEY] = {
        "label": "Top Collection Additions",
        "emoji": "🏛️",
        "description": (
            "Two thousand open-access Cleveland Museum of Art objects selected in source "
            "order after removing titles already represented in the Virtual Museum. The "
            "top-2000 source range is exhausted first, then selection continues only as "
            "far as needed to complete the unique collection."
        ),
        "objects": selected,
    }
    MUSEUM_PATH.write_text(json.dumps(museum, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Added {len(selected)} objects to {GALLERY_KEY}; "
        f"source ranks {selected[0]['source_rank']}–{selected[-1]['source_rank']}."
    )


if __name__ == "__main__":
    main()
