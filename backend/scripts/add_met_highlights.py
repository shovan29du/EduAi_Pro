#!/usr/bin/env python3
"""Add the most famous public-domain objects of The Metropolitan Museum of Art
to the Virtual Museum, as real, individually named objects.

Source: the Met's Open Access data (CC0), MetObjects.csv, from
https://github.com/metmuseum/openaccess. "Famous" is judged from the Met's own
curation, not guessed:

  score = 4 if the curators flag it a Highlight
        + 2 if it has its own Wikidata item (it is notable enough to have one)
        + 1 if its maker has a Wikidata item
        + 1 if it is listed in a gallery
        + 1 if it is in the Met's Timeline of Art History

Only public-domain objects are kept (their pictures are free to use). Generic
titles ("Bowl", "Fragment", "Untitled"), repeated titles and objects already in
the Museum are skipped. The top N by score become galleries, one per Met
department. Pictures are not stored here: `met_id` lets the app (and
museum_download_pictures.py) fetch each one from the Met's open-access API.

    python3 backend/scripts/add_met_highlights.py [--csv MetObjects.csv] [--limit 6000]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import quote_plus

BASE = Path(__file__).resolve().parent.parent
MUSEUM = BASE / "data" / "virtual_museum" / "museum.json"
CSV_URL = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"
SOURCE = "The Metropolitan Museum of Art Open Access (CC0)"

DEPARTMENTS = {  # department: (emoji, related subjects)
    "Asian Art": ("🏯", ["Art History", "World History", "Geography"]),
    "Drawings and Prints": ("✏️", ["Art History", "Art"]),
    "European Sculpture and Decorative Arts": ("🗿", ["Art History", "World History"]),
    "European Paintings": ("🎨", ["Art History", "World History"]),
    "The American Wing": ("🗽", ["Art History", "World History", "Social Studies"]),
    "Greek and Roman Art": ("🏛️", ["Art History", "World History", "Mythology"]),
    "Islamic Art": ("🕌", ["Art History", "World History", "Islamic Studies"]),
    "Arts of Africa, Oceania, and the Americas": ("🌍", ["Art History", "World History", "Geography"]),
    "Egyptian Art": ("🏺", ["Art History", "World History", "Mythology"]),
    "Medieval Art": ("🏰", ["Art History", "World History"]),
    "Ancient West Asian Art": ("🐂", ["Art History", "World History", "Geography"]),
    "The Cloisters": ("⛪", ["Art History", "World History", "World Religions"]),
    "Musical Instruments": ("🎻", ["Music", "Art History", "Physics"]),
    "Arms and Armor": ("🛡️", ["World History", "Art History"]),
    "Photographs": ("📷", ["Art", "Art History", "World History"]),
    "The Libraries": ("📚", ["World Literature", "Art History"]),
    "Robert Lehman Collection": ("🖼️", ["Art History", "World History"]),
    "Costume Institute": ("👗", ["Art History", "Art"]),
    "Modern and Contemporary Art": ("🖌️", ["Art History", "Art"]),
}
CATEGORIES = [  # (regex on Classification, category)
    (r"Paintings", "painting"), (r"Sculpture|Stone|Bronzes", "sculpture"), (r"Ceramic|Pottery|Porcelain|Terracotta|Vases", "ceramic"),
    (r"Metalwork|Gold|Silver|Copper", "metalwork"), (r"Textile|Costume|Tapestr|Embroider|Lace", "textile"), (r"Armor", "armor"),
    (r"Arms|Swords|Firearms", "weapon"), (r"Jewelry", "jewelry"), (r"Photograph", "photograph"), (r"Coin|Medal", "coin"),
    (r"Manuscript|Book|Codices", "manuscript"), (r"Print|Drawing", "print"), (r"Musical|Chordophone|Aerophone|Idiophone|Membranophone", "instrument"),
    (r"Furniture", "furniture"), (r"Glass|Enamel|Ivor|Wood|Leather|Horn|Mosaic|Lacquer|Tools|Equestrian|Clocks|Watches|Scientific", "decorative art"),
]
GENERIC_TITLES = {
    "bowl", "plate", "vase", "cup", "dish", "jar", "figure", "figurine", "panel", "fragment", "relief", "untitled", "head", "mask", "box",
    "ring", "coin", "tile", "textile", "pendant", "bottle", "ewer", "flask", "stand", "sword", "dagger", "helmet", "armor", "page", "leaf",
    "portrait", "landscape", "study", "plaque", "amulet", "bead", "necklace", "bracelet", "earring", "brooch", "cameo", "vessel", "beaker",
    "lamp", "mirror", "chair", "table", "cabinet", "clock", "teapot", "pitcher", "tankard", "goblet", "spoon", "fork", "knife",
}


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def clean(text: str, limit: int = 0) -> str:
    text = re.sub(r"\s+", " ", (text or "").replace("|", ", ")).strip(" ,;")
    return text[:limit].rstrip() if limit else text


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def qid(url: str) -> str:
    m = re.search(r"(Q\d+)", url or "")
    return m.group(1) if m else ""


def category_for(classification: str) -> str:
    for pattern, category in CATEGORIES:
        if re.search(pattern, classification or "", re.I):
            return category
    return "museum object"


def score(row: dict) -> int:
    return (4 * (row["Is Highlight"] == "True") + 2 * bool(qid(row["Object Wikidata URL"])) + bool(qid(row["Artist Wikidata URL"]))
            + bool(row["Gallery Number"].strip()) + (row["Is Timeline Work"] == "True"))


def usable(row: dict) -> bool:
    if row["Is Public Domain"] != "True" or not (row["Is Highlight"] == "True" or row["Is Timeline Work"] == "True"):
        return False
    title = clean(row["Title"])
    if len(title) < 5 or norm(title) in GENERIC_TITLES or row["Department"] not in DEPARTMENTS:
        return False
    # an anonymous, one- or two-word title with no Wikidata item is not a famous object
    if not row["Artist Display Name"].strip() and len(title.split()) <= 2 and not qid(row["Object Wikidata URL"]) and row["Is Highlight"] != "True":
        return False
    return True


def select(rows, existing_names: set[str], limit: int) -> list[dict]:
    best: dict[str, dict] = {}
    for row in rows:
        if not usable(row):
            continue
        key = norm(row["Title"]) + "|" + norm(row["Artist Display Name"])
        if norm(row["Title"]) in existing_names:
            continue
        s = score(row)
        if key not in best or s > best[key]["_score"]:
            best[key] = {**row, "_score": s}
    # Equal scores are shuffled by a hash of the object ID so no department's catalogue order dominates the top ranks.
    ranked = sorted(best.values(), key=lambda r: (-r["_score"], hashlib.sha1(r["Object ID"].encode()).hexdigest()))
    return ranked[:limit]


def display_name(row: dict, title: str, origin: str, date: str) -> str:
    """Short titles ("Basket", "Shield") say little; add the maker or origin so each card names one object."""
    if len(title.split()) > 2 and len(title) >= 14:
        return title
    maker = re.sub(r"\s*\(.*?\)", "", clean(row["Artist Display Name"]).split(",")[0]).strip()
    if maker:
        return f"{title} by {maker}"[:160]
    detail = ", ".join(x for x in (origin if origin != "World" else "", date) if x)
    return f"{title} ({detail})"[:160] if detail else title


def build_object(row: dict, rank: int) -> dict:
    title, oid = clean(row["Title"], 160), row["Object ID"]
    artist = clean(row["Artist Display Name"], 120)
    bio = clean(row["Artist Display Bio"], 100)
    date = clean(row["Object Date"], 60)
    medium = clean(row["Medium"], 160)
    dims = clean(row["Dimensions"], 160)
    dept = row["Department"]
    origin = next((clean(row[k], 60) for k in ("Culture", "Country", "Artist Nationality", "Region", "Geography Type") if clean(row[k])), "World")
    category = category_for(row["Classification"])
    on_view = row["Gallery Number"].strip()
    flags = []
    if row["Is Highlight"] == "True":
        flags.append("Chosen by The Metropolitan Museum of Art as one of the highlights of its collection.")
    if row["Is Timeline Work"] == "True":
        flags.append("Featured in the Met's Timeline of Art History, a curated survey of world art.")
    description = f"{title}, {date}. " if date else f"{title}. "
    if artist:
        description += f"{artist}{' (' + bio + ')' if bio else ''}. "
    if medium:
        description += f"{medium}. "
    if dims and "unavailable" not in dims.lower():
        description += f"{dims}. "
    description += f"{clean(row['Credit Line'], 200)}. The Metropolitan Museum of Art, accession number {row['Object Number']}."
    depts = sorted(DEPARTMENTS)
    h = int(hashlib.sha1(oid.encode()).hexdigest(), 16)
    wrong = [d for d in depts if d != dept]
    options = [wrong[(h + i * 5) % len(wrong)] for i in range(3)]
    options = list(dict.fromkeys(options))
    while len(options) < 3:
        options.append(wrong[(h + len(options) * 7 + 1) % len(wrong)])
    pos = h % 4
    options.insert(pos, dept)
    q = quote_plus(" ".join(x for x in (title, artist, "Metropolitan Museum of Art") if x))
    links = {"museum_object": (row["Link Resource"] or f"https://www.metmuseum.org/art/collection/search/{oid}").replace("http://", "https://"),
             "wikipedia": f"https://en.wikipedia.org/w/index.php?search={q}", "image_search": f"https://commons.wikimedia.org/w/index.php?search={q}",
             "google_image_search": f"https://www.google.com/search?tbm=isch&q={q}", "video": f"https://www.youtube.com/results?search_query={q}+explained",
             "virtual_tour": "https://artsandculture.google.com/search?q=Metropolitan+Museum+of+Art"}
    if qid(row["Object Wikidata URL"]):
        links["wikidata"] = f"https://www.wikidata.org/wiki/{qid(row['Object Wikidata URL'])}"
    return {
        "id": f"met_{oid}", "name": display_name(row, title, origin, date), "artist": artist, "year": date, "origin": origin, "material": medium or row["Classification"],
        "category": category, "description": description, "significance": " ".join(flags),
        "fun_fact": f"Listed in Gallery {on_view} at The Met." if on_view else f"Accession number {row['Object Number']}; part of the Met's open-access collection.",
        "museum": "The Metropolitan Museum of Art, New York", "educational_importance": f"A famous example for studying {origin} art and material culture: compare its date, materials and purpose with other objects in this gallery.",
        "related_lesson": "Museum Studies and Visual Analysis", "related_subjects": DEPARTMENTS[dept][1] + ["Museum Studies"],
        "quiz": {"question": f"Which department of The Metropolitan Museum of Art looks after '{title}'?", "options": options, "answer": pos},
        "activity": f"Study '{title}'. Describe its material{' (' + medium + ')' if medium else ''}, its date{' (' + date + ')' if date else ''} and what it tells you about {origin}.",
        "links": links, "source": SOURCE, "source_id": f"met-{oid}", "source_rank": rank, "met_id": int(oid),
    }


def read_rows(path: Path):
    csv.field_size_limit(10 ** 9)
    with path.open(encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=Path("MetObjects.csv"))
    ap.add_argument("--limit", type=int, default=6000)
    args = ap.parse_args()
    if not args.csv.exists():
        print(f"downloading {CSV_URL} (about 340 MB)…")
        urllib.request.urlretrieve(CSV_URL, args.csv)
    data = json.loads(MUSEUM.read_text(encoding="utf-8"))
    for gid in [g for g in data["galleries"] if g.startswith("met_")]:  # idempotent
        del data["galleries"][gid]
    existing = {norm(o["name"]) for g in data["galleries"].values() for o in g["objects"]}
    picked = select(read_rows(args.csv), existing, args.limit)
    built = [build_object(row, rank) for rank, row in enumerate(picked, 1)]
    seen: dict[str, int] = {}
    for obj in built:  # two different works can share a title: tell them apart by date or accession number
        seen[obj["name"]] = seen.get(obj["name"], 0) + 1
    for obj, row in zip(built, picked):
        if seen[obj["name"]] > 1:
            obj["name"] = f"{obj['name'][:120]} ({clean(row['Object Date'], 30) or row['Object Number']})"
    seen = {}
    for obj in built:  # same title and same date: fall back to the accession number, which is unique
        seen[obj["name"]] = seen.get(obj["name"], 0) + 1
    for obj, row in zip(built, picked):
        if seen[obj["name"]] > 1:
            obj["name"] = f"{obj['name'][:120]} [{row['Object Number']}]"  # truncate the title first so the unique part survives
    by_dept: dict[str, list] = {}
    for obj, row in zip(built, picked):
        by_dept.setdefault(row["Department"], []).append(obj)
    for dept, objects in sorted(by_dept.items(), key=lambda kv: -len(kv[1])):
        data["galleries"]["met_" + slug(dept)] = {"label": f"Met: {dept}", "emoji": DEPARTMENTS[dept][0], "objects": objects}
    MUSEUM.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added {len(picked)} Met objects in {len(by_dept)} galleries:", {d: len(o) for d, o in by_dept.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
