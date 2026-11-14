#!/usr/bin/env python3
"""Second museum de-duplication pass (idempotent).

Removes three kinds of duplicate from backend/data/virtual_museum/museum.json
and backend/data/museum_objects.json:

1. Same real object listed in more than one gallery (matched by normalised
   name). Keeper: the specific category gallery copy over the curated
   "greatest hits" galleries (matches the policy in dedupe_museum_entries.py);
   between two category copies prefer a real image, then the richer entry.
2. Template clones: bulk-generated cards in `sculptures` / `architecture`
   that share an identical description and differ only by a trailing number
   ("Byzantine Sculpture 16", "Byzantine Sculpture 28", ...). One card per
   style is kept and its trailing number is dropped from the name.
3. Exact duplicate rows (same id / image / url) in museum_objects.json.

Different works that merely share a title are NOT merged (see KEEP_DISTINCT).

    python3 backend/scripts/dedupe_museum_round2.py          # dry run
    python3 backend/scripts/dedupe_museum_round2.py --apply  # write changes
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
OBJECTS_PATH = BASE_DIR / "data" / "museum_objects.json"
RESOURCE_DIR = BASE_DIR / "data" / "museum_resource"

CURATED_PRIORITY = ["famous_masterpieces", "world_heritage_treasures", "top_2000_additions"]
TEMPLATE_GALLERIES = ("sculptures", "architecture")

# Same title, genuinely different work (verified by artist/date).
KEEP_DISTINCT = {"wht_0107", "wht_0001"}
# Tests treat these as canonical copies.
PINNED_KEEPERS = {"fm_0002"}


def norm(s: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def richness(obj: dict) -> int:
    return len(obj) + len(obj.get("links", {}))


def has_real_image(obj: dict) -> bool:
    return str(obj.get("thumbnail_local", "")).startswith("http")


def pick_keeper(entries: list[tuple[str, dict]]) -> tuple[str, dict]:
    for gid, obj in entries:
        if obj["id"] in PINNED_KEEPERS:
            return gid, obj

    def rank(item: tuple[str, dict]):
        gid, obj = item
        curated = CURATED_PRIORITY.index(gid) if gid in CURATED_PRIORITY else -1
        is_curated = gid in CURATED_PRIORITY
        # category copies first; then real image; then richer; then curated order
        return (is_curated, not has_real_image(obj), -richness(obj), curated)

    return sorted(entries, key=rank)[0]


def dump_like_original(path: Path, payload) -> None:
    """Write JSON keeping the file's existing line endings / trailing newline,
    so the git diff only shows the rows that actually changed."""
    raw = path.read_bytes()
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if b"\r\n" in raw:
        text = text.replace("\n", "\r\n")
    if raw.endswith(b"\n"):
        text += "\r\n" if b"\r\n" in raw else "\n"
    path.write_bytes(text.encode("utf-8"))


def main(apply: bool) -> None:
    data = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    galleries = data["galleries"]
    before_total = sum(len(g["objects"]) for g in galleries.values())
    removed: set[tuple[str, str]] = set()

    # 1. same-name cross-gallery duplicates
    groups: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for gid, g in galleries.items():
        for obj in g["objects"]:
            if obj["id"] in KEEP_DISTINCT:
                continue
            groups[norm(obj["name"])].append((gid, obj))
    same_object = 0
    for name, entries in groups.items():
        if not name or len(entries) < 2:
            continue
        keep_gid, keep = pick_keeper(entries)
        for gid, obj in entries:
            if obj is keep:
                continue
            if not keep.get("wiki_title") and obj.get("wiki_title"):
                keep["wiki_title"] = obj["wiki_title"]
            if has_real_image(obj) and not has_real_image(keep):
                for k in ("thumbnail_local", "image_source", "image_source_url", "image_found_via_query"):
                    if obj.get(k):
                        keep[k] = obj[k]
            removed.add((gid, obj["id"]))
            same_object += 1
            print(f"  dup  {gid}/{obj['id']:22s} '{obj['name']}'  -> keep {keep_gid}/{keep['id']}")

    # 2. template clones
    clones = 0
    for gid in TEMPLATE_GALLERIES:
        seen: dict[tuple[str, str], dict] = {}
        for obj in galleries[gid]["objects"]:
            if (gid, obj["id"]) in removed:
                continue
            base = re.sub(r"\s+\d+$", "", obj["name"])
            if base == obj["name"] and not re.search(r"Example\s*\d*$", obj["name"]):
                continue
            base = re.sub(r"\s*Example$", " Example", base).strip()
            key = (base, obj.get("description", ""))
            if key in seen:
                removed.add((gid, obj["id"]))
                clones += 1
            else:
                seen[key] = obj
        for (base, _), obj in seen.items():
            obj["name"] = base.replace(" Example", "")

    for gid, g in galleries.items():
        g["objects"] = [o for o in g["objects"] if (gid, o["id"]) not in removed]
    after_total = sum(len(g["objects"]) for g in galleries.values())
    print(f"museum.json: {before_total} -> {after_total}  (same-object {same_object}, template clones {clones})")

    # 3. exact duplicate rows in museum_objects.json
    objs_data = json.loads(OBJECTS_PATH.read_text(encoding="utf-8"))
    seen_keys: set = set()
    kept_rows = []
    for row in objs_data["objects"]:
        keys = [("id", row.get("id")), ("image", row.get("image")), ("url", row.get("url"))]
        if any(k in seen_keys for k in keys if k[1]):
            continue
        seen_keys.update(k for k in keys if k[1])
        kept_rows.append(row)
    print(f"museum_objects.json: {len(objs_data['objects'])} -> {len(kept_rows)}")
    objs_data["objects"] = kept_rows

    removed_ids = {oid for _, oid in removed}
    orphans = []
    thumbs = RESOURCE_DIR / "thumbnails"
    for oid in removed_ids:
        p = thumbs / f"{oid}.svg"
        if p.exists():
            orphans.append(p)
    print(f"orphan placeholder thumbnails to delete: {len(orphans)}")

    if not apply:
        print("dry run - nothing written (use --apply)")
        return
    dump_like_original(MUSEUM_PATH, data)
    dump_like_original(OBJECTS_PATH, objs_data)
    for p in orphans:
        p.unlink()
    manifest = RESOURCE_DIR / "manifest.json"
    if manifest.exists():
        m = json.loads(manifest.read_text(encoding="utf-8"))
        for oid in removed_ids:
            m.pop(oid, None)
        dump_like_original(manifest, m)
    print("written")


if __name__ == "__main__":
    main("--apply" in sys.argv)
