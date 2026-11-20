#!/usr/bin/env python3
"""Download real pictures for the Virtual Museum's objects.

Run this on a computer with Internet access. It saves each picture to
backend/data/museum_resource/images/ and records its credit and licence in
backend/data/museum_resource/pictures.json; the app then shows the local copy
(works offline, loads fast, credit shown). It is resumable: run it again and it
carries on, retrying only what failed.

Picture sources, most precise first:
  * Met objects          -> the Met's open-access API (public domain, CC0)
  * Cleveland objects    -> Cleveland Museum of Art open-access images (CC0)
  * objects with an article, or found by name -> Wikipedia / Wikimedia Commons
    (free-licence images only, with author and licence recorded)

    python backend/scripts/museum_download_pictures.py                 # everything
    python backend/scripts/museum_download_pictures.py --gallery met_egyptian_art --limit 50
    python backend/scripts/museum_download_pictures.py --dry-run       # just count
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import museum_pictures  # noqa: E402

MUSEUM = Path(__file__).resolve().parent.parent / "data" / "virtual_museum" / "museum.json"


def iter_objects(gallery: str = ""):
    data = json.loads(MUSEUM.read_text(encoding="utf-8"))
    for gid, g in data["galleries"].items():
        if gallery and gid != gallery:
            continue
        yield from g["objects"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gallery", default="", help="only this gallery id")
    ap.add_argument("--limit", type=int, default=0, help="stop after trying this many objects")
    ap.add_argument("--sleep", type=float, default=0.25, help="seconds to wait between downloads (be polite to the servers)")
    ap.add_argument("--dry-run", action="store_true", help="only count what is left to download")
    args = ap.parse_args()
    objects = list(iter_objects(args.gallery))
    have = museum_pictures.manifest()
    todo = [o for o in objects if not (o["id"] in have and (museum_pictures.IMAGES_DIR / have[o["id"]]["file"]).exists())]
    print(f"{len(objects)} objects, {len(objects) - len(todo)} already have a picture, {len(todo)} to go")
    if args.dry_run or not todo:
        return 0
    from app.main import museum_thumbnail  # reuses its Wikipedia/Commons lookup and cache

    def wiki_lookup(wiki_title: str, q: str):
        return museum_thumbnail(wiki_title=wiki_title, q=q).get("thumbnail_url")

    stats = museum_pictures.download_pictures(todo, wiki_lookup, limit=args.limit, sleep=args.sleep)
    print("finished:", stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
