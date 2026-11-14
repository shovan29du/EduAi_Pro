#!/usr/bin/env python3
"""Attach a real picture to every Virtual Museum object that currently has
NONE (backend/data/virtual_museum/museum.json).

Context: of the museum's ~8,200 objects, most already have a way to show a
real photo -- either a direct image URL already stored in
`thumbnail_local` (mostly the Cleveland Museum of Art open-access objects),
or a `wiki_title` the frontend uses to fetch a live thumbnail from
Wikipedia's page-summary API at view time (GET /api/museum/thumbnail in
backend/app/main.py). But ~1,000 objects -- concentrated in the
world_visual_arts, world_sculpture_ritual, world_texts_maps,
world_decorative_arts, world_textiles_dress, world_innovation, and
world_archaeology_design galleries -- have NEITHER, so they permanently
show a generated placeholder icon instead of a real picture.

This script closes that gap using sources *other than* the live Wikipedia
lookup the app already relies on for other objects:
  1. Wikidata (wbsearchentities + wbgetentities): look up the object by
     name, read its P18 ("image") claim, which names a Wikimedia Commons
     file directly -- this is often populated even when the topic has no
     full Wikipedia article.
  2. Wikimedia Commons search (as a fallback): search Commons directly for
     a file matching the object's name.
In both cases the resulting image is referenced via Commons's stable
`Special:FilePath/<filename>` redirect, so no file-metadata parsing is
needed to get a direct, hotlinkable image URL.

Matching is deliberately conservative: a candidate is only accepted if the
matched title/filename shares a meaningful word overlap with the object's
own name. If nothing matches confidently, the object is left untouched
(same placeholder as before) rather than attaching a guessed, possibly
wrong, image -- consistent with this project's no-fabrication rule: a
mismatched picture on a real artifact is worse than no picture at all.

*** This cannot be run inside the current Claude Code cloud session: its
*** egress policy blocks wikidata.org and wikimedia.org (confirmed via
*** curl + the agent-proxy status endpoint). Run it from a machine/session
*** with normal internet access instead.

Usage:
    python3 backend/scripts/add_museum_images_from_alternate_sources.py --dry-run --limit 20
    python3 backend/scripts/add_museum_images_from_alternate_sources.py

Writes:
    backend/data/virtual_museum/museum.json (adds `thumbnail_local`,
    `image_source`, and `image_source_url` to objects that had neither a
    real thumbnail nor a wiki_title before)

Re-run any time: it only touches objects still missing both.
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MUSEUM_PATH = BASE_DIR / "data" / "virtual_museum" / "museum.json"
CACHE_PATH = Path("/tmp/museum_image_lookup_cache.json")

HEADERS = {"User-Agent": "EduAI-MuseumImages/1.0 (educational; contact@eduai.app)"}
REQUEST_TIMEOUT = 10
REQUEST_DELAY_SECONDS = 0.3  # politeness delay between external API calls

STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "in", "on", "at", "to", "for",
    "from", "with", "early", "late", "ancient", "traditional", "ceremonial",
}


def significant_words(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 2}


def confident_match(object_name: str, candidate_title: str) -> bool:
    """Require at least half of the object name's significant words (and at
    least one) to appear in the candidate title, to avoid attaching an
    unrelated image under a loose/coincidental text match."""
    obj_words = significant_words(object_name)
    if not obj_words:
        return False
    cand_words = significant_words(candidate_title)
    overlap = obj_words & cand_words
    return len(overlap) >= max(1, len(obj_words) // 2)


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(json.dumps(cache), encoding="utf-8")


def http_get_json(url: str) -> dict | None:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"    request failed: {e}")
        return None


def commons_file_path_url(filename: str) -> str:
    filename = filename.replace(" ", "_")
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(filename)


def lookup_via_wikidata(name: str) -> tuple[str, str] | None:
    """Returns (image_url, wikidata_item_url) or None."""
    search_url = (
        "https://www.wikidata.org/w/api.php?action=wbsearchentities"
        f"&search={urllib.parse.quote(name)}&language=en&format=json&limit=3"
    )
    data = http_get_json(search_url)
    if not data or not data.get("search"):
        return None
    for result in data["search"]:
        label = result.get("label", "")
        if not confident_match(name, label):
            continue
        qid = result["id"]
        entity_url = (
            f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={qid}"
            "&props=claims&format=json"
        )
        entity_data = http_get_json(entity_url)
        if not entity_data:
            continue
        claims = entity_data.get("entities", {}).get(qid, {}).get("claims", {})
        p18 = claims.get("P18")
        if not p18:
            continue
        try:
            filename = p18[0]["mainsnak"]["datavalue"]["value"]
        except (KeyError, IndexError, TypeError):
            continue
        return commons_file_path_url(filename), f"https://www.wikidata.org/wiki/{qid}"
    return None


def lookup_via_commons_search(name: str) -> tuple[str, str] | None:
    """Returns (image_url, commons_file_page_url) or None."""
    search_url = (
        "https://commons.wikimedia.org/w/api.php?action=query&list=search"
        f"&srsearch={urllib.parse.quote(name)}&srnamespace=6&format=json&srlimit=3"
    )
    data = http_get_json(search_url)
    if not data:
        return None
    for result in data.get("query", {}).get("search", []):
        title = result.get("title", "")  # e.g. "File:Example.jpg"
        if not title.lower().endswith((".jpg", ".jpeg", ".png", ".tif", ".tiff")):
            continue
        filename = title.split(":", 1)[-1]
        if not confident_match(name, filename):
            continue
        return commons_file_path_url(filename), f"https://commons.wikimedia.org/wiki/{title.replace(' ', '_')}"
    return None


def find_targets(data: dict) -> list[tuple[str, dict]]:
    """Objects with neither a real thumbnail_local URL nor a wiki_title."""
    targets = []
    for gid, g in data["galleries"].items():
        for obj in g.get("objects", []):
            tl = obj.get("thumbnail_local") or ""
            has_real_url = tl.startswith("http://") or tl.startswith("https://")
            if not has_real_url and not obj.get("wiki_title"):
                targets.append((gid, obj))
    return targets


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Look up and print matches without writing the file")
    parser.add_argument("--limit", type=int, default=0, help="Max objects to process (0 = all)")
    args = parser.parse_args()

    data = json.loads(MUSEUM_PATH.read_text(encoding="utf-8"))
    targets = find_targets(data)
    if args.limit:
        targets = targets[: args.limit]

    print(f"{len(targets)} object(s) have no real image mechanism yet.")

    cache = load_cache()
    found = skipped = 0

    for i, (gid, obj) in enumerate(targets, 1):
        name = obj.get("name", "")
        cache_key = f"{gid}:{obj['id']}"
        print(f"[{i}/{len(targets)}] {gid}/{obj['id']}: {name}")

        if cache_key in cache:
            result = cache[cache_key]
        else:
            result = lookup_via_wikidata(name)
            time.sleep(REQUEST_DELAY_SECONDS)
            if not result:
                result = lookup_via_commons_search(name)
                time.sleep(REQUEST_DELAY_SECONDS)
            cache[cache_key] = result
            save_cache(cache)

        if result:
            image_url, source_url = result
            print(f"    -> matched: {image_url}")
            found += 1
            if not args.dry_run:
                obj["thumbnail_local"] = image_url
                obj["image_source"] = "wikidata" if "wikidata.org" in source_url else "wikimedia_commons"
                obj["image_source_url"] = source_url
        else:
            print("    -> no confident match, left as placeholder")
            skipped += 1

    print(f"\nMatched: {found}  No confident match: {skipped}")
    if not args.dry_run:
        MUSEUM_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {MUSEUM_PATH}")
    else:
        print("Dry run -- museum.json was not modified.")


if __name__ == "__main__":
    main()
