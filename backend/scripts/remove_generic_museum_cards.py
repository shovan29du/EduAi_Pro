#!/usr/bin/env python3
"""Remove the generic "Country + type" study cards from the Virtual Museum.

The seven `world_*` galleries held 1,000 placeholder cards such as
"Afghanistan Painting" (museum: "Various world collections"): they described a
tradition, not a real object, so no genuine picture exists for them. A gallery
is removed only when *every* object in it is such a card. Idempotent.

    python3 backend/scripts/remove_generic_museum_cards.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MUSEUM = BASE / "data" / "virtual_museum" / "museum.json"
RESOURCE = BASE / "data" / "museum_resource"
GENERIC_MUSEUM = "Various world collections"


def is_generic(obj: dict) -> bool:
    return obj.get("museum") == GENERIC_MUSEUM and not obj.get("wiki_title") and not obj.get("source_id")


def main() -> None:
    data = json.loads(MUSEUM.read_text(encoding="utf-8"))
    removed_ids: list[str] = []
    for gid in [g for g, gallery in data["galleries"].items()
                if gallery.get("objects") and all(is_generic(o) for o in gallery["objects"])]:
        removed_ids += [o["id"] for o in data["galleries"][gid]["objects"]]
        del data["galleries"][gid]
    MUSEUM.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Drop their placeholder thumbnails and manifest entries too.
    manifest_path = RESOURCE / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for oid in removed_ids:
            manifest.pop(oid, None)
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for oid in removed_ids:
        for path in (RESOURCE / "thumbnails").glob(f"{oid}.*"):
            path.unlink()
    print(f"removed {len(removed_ids)} generic cards")


if __name__ == "__main__":
    main()
