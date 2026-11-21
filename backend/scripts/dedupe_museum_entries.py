#!/usr/bin/env python3
"""Remove duplicate entries from the Virtual Museum
(backend/data/virtual_museum/museum.json).

Two distinct kinds of duplicate were found:

1. ID collisions: a handful of objects share the same `id` within the SAME
   gallery, because two separate content-generation passes independently
   added the same real-world topic (e.g. two "galileo_telescope" entries
   in science_technology, one richer than the other). Since
   GET /api/museum/{gallery}/{object_id} does `obj["id"] == object_id` and
   returns the first match, the second entry of each pair is unreachable by
   direct lookup and also creates a duplicate React key in list views.
   Fix: keep the richer entry (more fields/links), drop the leaner one.

2. Cross-gallery duplicates: the same real object (by name + origin)
   appears in both a specific category gallery (paintings, sculptures,
   architecture, ancient_world, ...) and one of the large curated
   "greatest hits" galleries (famous_masterpieces, world_heritage_treasures,
   top_2000_additions). This is mostly intentional overlap by design, but
   per an explicit decision, duplicates are removed from the curated
   galleries, keeping the copy in the specific category gallery. Where a
   duplicate group exists entirely within curated galleries (no category
   copy), the entry in famous_masterpieces is kept (it is the smaller,
   earlier, more tightly curated list) and the rest are dropped.

Groups that span only non-curated category galleries (e.g. "Terracotta
Warriors" in both ancient_world and sculptures) are left untouched --
they're a different, smaller edge case not covered by this decision, and
removing either copy would be a judgment call nobody asked for.

Re-run after editing:
    python3 backend/scripts/dedupe_museum_entries.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"

CURATED_GALLERIES_PRIORITY = ["famous_masterpieces", "world_heritage_treasures", "top_2000_additions"]

# (gallery, id) of the leaner entry to drop in each same-gallery ID collision.
# Decided by comparing field richness (museum/category/fun_fact/related_subjects
# and fuller `links`) -- keep the richer entry in each pair.
ID_COLLISION_DROPS = [
    ("ancient_world", "dead_sea_scrolls", "Dead Sea Scrolls Fragment"),
    ("science_technology", "galileo_telescope", "Galileo's Telescopes"),
    ("science_technology", "crick_watson_dna", "Crick & Watson's DNA Model"),
    ("science_technology", "printing_press", "Gutenberg's Printing Press"),
]


def main() -> None:
    data = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    galleries = data["galleries"]

    # --- Step 1: fix the 4 same-gallery ID collisions ---------------------
    collision_removed = 0
    for gid, oid, name in ID_COLLISION_DROPS:
        objs = galleries[gid]["objects"]
        before = len(objs)
        galleries[gid]["objects"] = [
            o for o in objs if not (o["id"] == oid and o.get("name") == name)
        ]
        removed = before - len(galleries[gid]["objects"])
        if removed != 1:
            raise SystemExit(f"Expected to remove exactly 1 entry for {gid}/{oid} ({name!r}), removed {removed}")
        collision_removed += removed

    # --- Step 2: cross-gallery duplicate removal ---------------------------
    name_locations: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for gid, g in galleries.items():
        for obj in g.get("objects", []):
            key = ((obj.get("name") or "").strip().lower(), (obj.get("origin") or "").strip().lower())
            name_locations.setdefault(key, []).append((gid, obj["id"]))

    to_remove: set[tuple[str, str]] = set()  # (gallery, id)
    left_as_is: list[tuple] = []

    for key, locations in name_locations.items():
        if len(locations) < 2:
            continue
        curated = [loc for loc in locations if loc[0] in CURATED_GALLERIES_PRIORITY]
        non_curated = [loc for loc in locations if loc[0] not in CURATED_GALLERIES_PRIORITY]

        if non_curated and curated:
            # Keep all non-curated copies, drop every curated copy.
            for loc in curated:
                to_remove.add(loc)
        elif curated and not non_curated:
            # All copies are in curated galleries: keep the highest-priority
            # one, drop the rest.
            curated_sorted = sorted(curated, key=lambda loc: CURATED_GALLERIES_PRIORITY.index(loc[0]))
            for loc in curated_sorted[1:]:
                to_remove.add(loc)
        else:
            # Entirely within non-curated category galleries -- not covered
            # by this decision; leave untouched.
            left_as_is.append((key, locations))

    cross_gallery_removed = 0
    for gid, g in galleries.items():
        objs = g.get("objects", [])
        before = len(objs)
        g["objects"] = [o for o in objs if (gid, o["id"]) not in to_remove]
        cross_gallery_removed += before - len(g["objects"])

    MUSEUM_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Fixed {collision_removed} same-gallery ID collisions (kept the richer entry each time).")
    print(f"Removed {cross_gallery_removed} duplicate entries from curated galleries.")
    print(f"Left {len(left_as_is)} category-vs-category overlap group(s) untouched (not covered by this decision):")
    for key, locations in left_as_is:
        print(f"  {key[0]!r} ({key[1]}) -> {locations}")

    total = sum(len(g.get("objects", [])) for g in galleries.values())
    print(f"Total objects now: {total}")


if __name__ == "__main__":
    main()
