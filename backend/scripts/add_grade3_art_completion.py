#!/usr/bin/env python3
"""Depth pass, Grade 3 Art: fill in real, hand-checked data_table content
for the 18 Grade 3 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 3 Art to full 20/20 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade3_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade3.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g3-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Texture", "How a surface feels or looks like it feels"],
            ["Pattern", "A design that repeats"],
        ]),
    },
    "art-g3-l3": {
        "data_table": table(["Color Group", "Examples"], [
            ["Warm colors", "Red, orange, yellow"], ["Cool colors", "Blue, green, purple"],
        ]),
    },
    "art-g3-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Shading", "Using darker or lighter tones to show depth"],
        ]),
    },
    "art-g3-l5": {
        "data_table": table(["Line Type", "Example"], [
            ["Straight line", "A ruler's edge"], ["Curved line", "A wave shape"],
        ]),
    },
    "art-g3-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Shape", "A flat, 2D area (circle, square)"], ["Form", "A 3D object (sphere, cube)"],
        ]),
    },
    "art-g3-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g3-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g3-l9": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"],
            ["Coiling", "Stacking rolled clay ropes to build a form"],
        ]),
    },
    "art-g3-l10": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g3-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-portrait", "A drawing or painting of oneself"],
        ]),
    },
    "art-g3-l13": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g3-l14": {
        "data_table": table(["Art Style", "Region"], [
            ["Aboriginal dot painting", "Australia"], ["Origami", "Japan"],
        ]),
    },
    "art-g3-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Origami", "The Japanese art of paper folding"],
        ]),
    },
    "art-g3-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Perspective", "Making objects look closer or farther away"],
        ]),
    },
    "art-g3-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Mixed media", "Art made using more than one material or technique"],
        ]),
    },
    "art-g3-l18": {
        "data_table": table(["Inspiration Source", "Example Artwork"], [
            ["Leaves", "Leaf rubbing prints"], ["Flowers", "Painted flower still life"],
        ]),
    },
    "art-g3-l19": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows what a character says"],
        ]),
    },
    "art-g3-l20": {
        "data_table": table(["Recycled Material", "Possible Art Use"], [
            ["Cardboard", "Sculpture base"], ["Bottle caps", "Mosaic pieces"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade3.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 3 Art lessons (completing 20/20).")


if __name__ == "__main__":
    main()
