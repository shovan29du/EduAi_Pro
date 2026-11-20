#!/usr/bin/env python3
"""Remove duplicate and generic objects from the Virtual Museum.

Duplicates: the same real thing listed more than once, found by (a) the same
normalised title or (b) the same Wikipedia article (`wiki_title`). Of each
group the best entry is kept: the one whose title is the article's title, then
the one with a picture, a quiz and the fullest description, then the first
gallery in the museum's own order. Different works that merely share a Wikidata
item (a print and its woodblock) are not duplicates.

Generic: an object named only by what kind of thing it is ("Teapot", "Untitled",
"Standing Buddha", "Tea Table") says nothing about which object it is and has no
picture to find. Only objects drawn from the Cleveland and Met open-access lists
are tested; hand-curated famous objects always carry a specific name and article.

    python3 backend/scripts/remove_duplicate_and_generic_museum_objects.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

MUSEUM = Path(__file__).resolve().parent.parent / "data" / "virtual_museum" / "museum.json"

GENERIC_NOUNS = set("""bowl plate vase cup dish jar figure figurine panel fragment relief untitled head mask box ring coin tile textile
pendant bottle ewer stand sword dagger helmet armor armour page leaf portrait landscape study plaque amulet bead necklace bracelet earring
brooch cameo vessel beaker lamp mirror chair table cabinet clock teapot pitcher tankard goblet spoon fork knife sideboard mantle mantel
fountain sculpture painting drawing print photograph book manuscript medal beaker candlestick chest desk bed bench stool tray basket
bag shield saddle spear axe arrow bow coffeepot tureen platter saucer jug flagon urn casket reliquary crucifix cross chalice censer
box buckle button comb fan glove hat shoe sandal robe dress coat cloak cap belt scarf shawl rug carpet blanket quilt curtain tapestry
statue statuette bust torso hand foot horse lion dog cat""".split())
GENERIC_MODIFIERS = set("""the a an of with and in on for from to by tea standing seated kneeling reclining covered small large pair two three four
one set miniature ceremonial decorative ancient old new young little big grand great round square oval double single folding sitting
walking dancing sleeping holy sacred royal imperial votive funerary drinking serving writing hanging""".split())


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def is_generic(obj: dict) -> bool:
    """Named only by kind: every word is an object type or a plain modifier, and at least one is a type."""
    if obj.get("wiki_title"):
        return False
    if not str(obj.get("id", "")).startswith(("top2k_", "met_")):
        return False
    words = norm(obj.get("name", "")).split()
    if not words:
        return True
    return all(w in GENERIC_NOUNS or w in GENERIC_MODIFIERS for w in words) and any(w in GENERIC_NOUNS for w in words)


def quality(obj: dict, wiki_title_norm: str = "") -> tuple:
    name_is_article = bool(wiki_title_norm) and norm(obj.get("name")) == wiki_title_norm
    has_picture = bool(obj.get("thumbnail_local") and not str(obj["thumbnail_local"]).endswith(".svg"))
    return (name_is_article, bool(obj.get("quiz")), has_picture, len(obj.get("description", "")),
            -obj.get("source_rank", 0) if obj.get("source_rank") else 0)


def find_duplicates(entries: list[tuple[str, dict]]) -> list[tuple[str, dict, tuple[str, dict]]]:
    """[(gallery, removed object, kept (gallery, object))] for every duplicate group."""
    order = {id(o): i for i, (_, o) in enumerate(entries)}
    parent = list(range(len(entries)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        parent[find(a)] = find(b)

    for key_fn in (lambda o: norm(o.get("name")), lambda o: norm(o.get("wiki_title"))):
        seen: dict[str, int] = {}
        for i, (_, o) in enumerate(entries):
            key = key_fn(o)
            if not key:
                continue
            if key in seen:
                union(i, seen[key])
            else:
                seen[key] = i
    groups = defaultdict(list)
    for i in range(len(entries)):
        groups[find(i)].append(i)
    removed = []
    for members in groups.values():
        if len(members) < 2:
            continue
        titles = {norm(entries[i][1].get("wiki_title")) for i in members} - {""}
        title = next(iter(titles), "")
        best = max(members, key=lambda i: (quality(entries[i][1], title), -order[id(entries[i][1])]))
        removed += [(entries[i][0], entries[i][1], entries[best]) for i in members if i != best]
    return removed


def clean(data: dict) -> dict:
    """Remove generic objects, then duplicates. Returns {'generic': [...], 'duplicates': [...]}."""
    report = {"generic": [], "duplicates": []}
    for gid, gallery in data["galleries"].items():
        keep = []
        for obj in gallery["objects"]:
            (report["generic"].append((gid, obj["id"], obj["name"])) if is_generic(obj) else keep.append(obj))
        gallery["objects"] = keep
    entries = [(gid, o) for gid, g in data["galleries"].items() for o in g["objects"]]
    drop = {id(o) for _, o, _ in find_duplicates(entries)}
    for gid, obj, (kgid, kept) in find_duplicates(entries):
        report["duplicates"].append((gid, obj["id"], obj["name"], kgid, kept["id"], kept["name"]))
    for gallery in data["galleries"].values():
        gallery["objects"] = [o for o in gallery["objects"] if id(o) not in drop]
    for gid in [g for g, v in data["galleries"].items() if not v["objects"]]:
        del data["galleries"][gid]
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    data = json.loads(MUSEUM.read_text(encoding="utf-8"))
    before = sum(len(g["objects"]) for g in data["galleries"].values())
    report = clean(data)
    after = sum(len(g["objects"]) for g in data["galleries"].values())
    for gid, oid, name in report["generic"]:
        print(f"generic    {gid}/{oid}: {name}")
    for gid, oid, name, kgid, koid, kname in report["duplicates"]:
        print(f"duplicate  {gid}/{oid}: {name}  ->  kept {kgid}/{koid}: {kname}")
    print(f"{len(report['generic'])} generic + {len(report['duplicates'])} duplicate objects; {before} -> {after}")
    if not args.dry_run:
        MUSEUM.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
