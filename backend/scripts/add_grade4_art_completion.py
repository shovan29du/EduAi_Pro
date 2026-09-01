#!/usr/bin/env python3
"""Depth pass, Grade 4 Art: fill in real, hand-checked data_table content
for the 28 Grade 4 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 4 Art to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g4-l1": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g4-l2": {
        "data_table": table(["Color Type", "Examples"], [
            ["Primary", "Red, blue, yellow"], ["Secondary", "Green, orange, purple"],
        ]),
    },
    "art-g4-l3": {
        "data_table": table(["Color Group", "Examples"], [
            ["Warm colors", "Red, orange, yellow"], ["Cool colors", "Blue, green, purple"],
        ]),
    },
    "art-g4-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g4-l5": {
        "data_table": table(["Element", "Example"], [
            ["Shape", "2D area like a circle or square"], ["Line", "Straight or curved marks"],
        ]),
    },
    "art-g4-l6": {
        "data_table": table(["Portrait Element", "Description"], [
            ["Proportions", "Relative size and placement of facial features"],
        ]),
    },
    "art-g4-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g4-l8": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"], ["Coiling", "Stacking rolled clay ropes"],
        ]),
    },
    "art-g4-l9": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g4-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g4-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Perspective", "Making objects look closer or farther away"],
        ]),
    },
    "art-g4-l14": {
        "data_table": table(["Textile Art Style", "Region"], [
            ["Batik", "Indonesia"], ["Ikat weaving", "Central and Southeast Asia"],
        ]),
    },
    "art-g4-l15": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows what a character says"],
        ]),
    },
    "art-g4-l16": {
        "data_table": table(["Technique", "Effect"], [
            ["Layering", "Blends colors for depth"], ["Burnishing", "Smooths and blends colored pencil"],
        ]),
    },
    "art-g4-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Origami", "The Japanese art of paper folding"],
        ]),
    },
    "art-g4-l18": {
        "data_table": table(["Recycled Material", "Possible Art Use"], [
            ["Cardboard", "Sculpture base"], ["Bottle caps", "Mosaic pieces"],
        ]),
    },
    "art-g4-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Mosaic", "Art made from small pieces of tile, glass, or stone"],
        ]),
    },
    "art-g4-l20": {
        "data_table": table(["Poster Element", "Purpose"], [
            ["Headline", "Grabs attention"], ["Image", "Illustrates the message"],
        ]),
    },
    "art-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Photography composition", "Using foreground and background"],
        ]),
    },
    "art-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Interior design", "Mixing primary colors to choose paint"],
        ]),
    },
    "art-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Fashion", "Choosing warm or cool color palettes"],
        ]),
    },
    "art-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Greeting cards", "Painting a watercolor scene"],
        ]),
    },
    "art-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Logo design", "Using simple shapes and lines"],
        ]),
    },
    "art-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Family portraits", "Drawing accurate facial proportions"],
        ]),
    },
    "art-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Advertising", "Arranging product photos like a still life"],
        ]),
    },
    "art-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Pottery making", "Shaping bowls and mugs from clay"],
        ]),
    },
    "art-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Fabric design", "Stamping repeated patterns onto cloth"],
        ]),
    },
    "art-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Scrapbooking", "Combining photos and materials into a collage"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 Art lessons (completing 30/30).")


if __name__ == "__main__":
    main()
