#!/usr/bin/env python3
"""Download real pictures for the Virtual Museum's objects.

Run this on a computer with Internet access. It saves each picture, with its
credit and licence, in the app's database (the museum_pictures table); the app
then shows the stored copy (works offline, loads fast, credit shown). Each
object page also has Download / Upload / Delete buttons that do the same one
object at a time. It is resumable: run it again and it carries on, retrying
only what failed.

Objects with no picture at all are done first. For each object the links it already
has are tried first, then a search by name:
  1. a direct image link it carries
  2. its museum page: Met -> the Met open-access API (CC0); Cleveland -> its open-access
     image (CC0); any other museum site -> the page's own og:image (licence unknown, so the
     credit says "check its terms before reuse")
  3. its Wikipedia article link -> the article's picture (Wikimedia Commons, with author and licence)
  4. its Wikidata item -> the item's image (property P18)
  5. a Wikipedia / Commons search by name

    python backend/scripts/museum_download_pictures.py                  # everything, no-picture objects first
    python backend/scripts/museum_download_pictures.py --only-missing   # only objects that show no picture now
    python backend/scripts/museum_download_pictures.py --gallery met_egyptian_art --limit 50
    python backend/scripts/museum_download_pictures.py --check-links    # test the links instead of downloading
    python backend/scripts/museum_download_pictures.py --dry-run        # just count

Afterwards pictures_missing.json lists what is still without a picture and what was tried;
--check-links writes link_report.json listing broken links.
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
    """Every object (skipping ones the owner deleted), each tagged with its gallery id."""
    from app import museum_store
    from app.database import create_schema
    create_schema()
    deleted = museum_store.deleted_objects()
    data = json.loads(MUSEUM.read_text(encoding="utf-8"))
    for gid, g in data["galleries"].items():
        if gallery and gid != gallery:
            continue
        for obj in g["objects"]:
            if (gid, obj["id"]) not in deleted:
                yield {**obj, "gallery": gid}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gallery", default="", help="only this gallery id")
    ap.add_argument("--limit", type=int, default=0, help="stop after trying this many objects")
    ap.add_argument("--sleep", type=float, default=0.25, help="seconds to wait between downloads (be polite to the servers)")
    ap.add_argument("--dry-run", action="store_true", help="only count what is left to download")
    ap.add_argument("--only-missing", action="store_true", help="skip objects that already show a picture from a web link")
    ap.add_argument("--check-links", action="store_true", help="check each object's own links (museum page, Wikipedia, Wikidata) and report broken ones")
    args = ap.parse_args()
    objects = list(iter_objects(args.gallery))
    if args.check_links:
        todo = museum_pictures.prioritise(objects)[: args.limit or None]
        report = museum_pictures.check_links(todo, sleep=args.sleep)
        broken = [(oid, key, r["url"]) for oid, links in report.items() for key, r in links.items() if not r["ok"]]
        print(f"checked {sum(len(v) for v in report.values())} links on {len(todo)} objects: {len(broken)} broken (see link_report.json)")
        return 0
    from app import museum_store
    from app.database import create_schema
    create_schema()
    have = set(museum_store.stored_pictures())
    todo = [o for o in objects if o["id"] not in have]
    none_at_all = [o for o in todo if not museum_pictures.has_picture(o) and not o.get("met_id")]
    print(f"{len(objects)} objects, {len(objects) - len(todo)} already downloaded, {len(todo)} to go "
          f"({len(none_at_all)} with no picture at all, done first)")
    if args.dry_run or not todo:
        return 0
    from app.main import museum_thumbnail  # reuses its Wikipedia/Commons lookup and cache

    def wiki_lookup(wiki_title: str, q: str):
        return museum_thumbnail(wiki_title=wiki_title, q=q).get("thumbnail_url")

    stats = museum_pictures.download_pictures(todo, wiki_lookup, limit=args.limit, sleep=args.sleep, only_missing=args.only_missing)
    print("finished:", stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
