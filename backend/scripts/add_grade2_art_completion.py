#!/usr/bin/env python3
"""Depth pass, Grade 2 Art: fill in real, hand-checked data_table content
for the 18 Grade 2 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 2 Art to full 20/20 coverage.

Content covers real, verifiable art technique facts -- nothing fabricated
or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g2-l1": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g2-l3": {
        "data_table": table(["Colour Type", "Colours"], [
            ["Warm", "Red, Orange, Yellow"], ["Cool", "Blue, Green, Purple"],
        ]),
    },
    "art-g2-l4": {
        "data_table": table(["Line Type", "Example"], [
            ["Straight", "A ruler's edge"], ["Zigzag", "A lightning bolt shape"], ["Curved", "A wave"],
        ]),
    },
    "art-g2-l5": {
        "data_table": table(["Texture", "Example"], [
            ["Rough", "Tree bark, sandpaper"], ["Smooth", "Glass, polished stone"],
        ]),
    },
    "art-g2-l6": {
        "data_table": table(["Technique", "Effect"], [
            ["Wet-on-wet", "Colors blend softly"], ["Wet-on-dry", "Creates sharper edges"],
        ]),
    },
    "art-g2-l7": {
        "data_table": table(["Material", "Example"], [
            ["Paper", "Colored construction paper"], ["Fabric", "Cloth scraps"],
            ["Natural items", "Leaves, dried flowers"],
        ]),
    },
    "art-g2-l8": {
        "data_table": table(["Technique", "Description"], [
            ["Pinching", "Shaping clay with fingers"], ["Rolling", "Making coils or flat sheets"],
        ]),
    },
    "art-g2-l9": {
        "data_table": table(["Object Used", "Print Pattern"], [
            ["Potato stamp", "Simple carved shapes"], ["Sponge", "Textured dabs"],
        ]),
    },
    "art-g2-l10": {
        "data_table": table(["Face Feature", "Typical Position"], [
            ["Eyes", "Middle of the head"], ["Nose", "Below the eyes"], ["Mouth", "Below the nose"],
        ]),
    },
    "art-g2-l11": {
        "data_table": table(["Animal", "Simple Shapes Used"], [
            ["Cat", "Circles and triangles (ears)"], ["Fish", "Oval and triangle (tail)"],
        ]),
    },
    "art-g2-l12": {
        "data_table": table(["Landscape Element", "How to Draw It"], [
            ["Trees", "Circles or triangles on a trunk"],
            ["Mountains", "Zigzag or triangular shapes"], ["Sky", "Horizontal lines or soft shading"],
        ]),
    },
    "art-g2-l13": {
        "data_table": table(["Artist", "Known For"], [
            ["Vincent van Gogh", "The Starry Night"], ["Pablo Picasso", "Co-founding Cubism"],
            ["Leonardo da Vinci", "The Mona Lisa"],
        ]),
    },
    "art-g2-l14": {
        "data_table": table(["Pattern Type", "Example"], [
            ["Repeating pattern", "Same shape repeated in a row"],
            ["Symmetrical pattern", "Mirror image on both sides"],
        ]),
    },
    "art-g2-l15": {
        "data_table": table(["Origami Shape", "Fold Complexity"], [
            ["Paper boat", "A few simple folds"], ["Paper crane", "More folds, more advanced"],
        ]),
    },
    "art-g2-l17": {
        "data_table": table(["Shading Term", "Meaning"], [
            ["Highlight", "The lightest area, where light hits directly"],
            ["Shadow", "The darkest area, away from the light source"],
        ]),
    },
    "art-g2-l18": {
        "data_table": table(["Recycled Material", "Art Use"], [
            ["Cardboard", "Sculptures, collages"], ["Bottle caps", "Mosaic art"],
        ]),
    },
    "art-g2-l19": {
        "data_table": table(["Sculpture Type", "Description"], [
            ["Freestanding", "Can be viewed from all sides"],
            ["Relief", "Attached to a background, viewed from the front"],
        ]),
    },
    "art-g2-l20": {
        "data_table": table(["Art Form", "Culture"], [
            ["Origami", "Japan"], ["Mandala", "India"], ["Aboriginal dot painting", "Australia"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 Art lessons (completing 20/20).")


if __name__ == "__main__":
    main()
