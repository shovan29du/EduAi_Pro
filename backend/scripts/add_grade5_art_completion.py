#!/usr/bin/env python3
"""Depth pass, Grade 5 Art: fill in real, hand-checked data_table content
for the 28 Grade 5 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 5 Art to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g5-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Perspective", "Making objects look closer or farther away"],
            ["Composition", "The arrangement of elements in an artwork"],
        ]),
    },
    "art-g5-l2": {
        "data_table": table(["Color Group", "Examples"], [
            ["Warm colors", "Red, orange, yellow"], ["Cool colors", "Blue, green, purple"],
        ]),
    },
    "art-g5-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Value", "The lightness or darkness of a color"],
        ]),
    },
    "art-g5-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Texture", "How a surface feels or looks like it feels"],
        ]),
    },
    "art-g5-l6": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D area"], ["Form", "A 3D object"],
        ]),
    },
    "art-g5-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Positive space", "The subject of the artwork"], ["Negative space", "The empty space around the subject"],
        ]),
    },
    "art-g5-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g5-l9": {
        "data_table": table(["Technique", "Description"], [
            ["Carving", "Removing material to reveal a form"], ["Modeling", "Building up material, like clay"],
        ]),
    },
    "art-g5-l10": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g5-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g5-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g5-l13": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g5-l14": {
        "data_table": table(["Proportion Guideline", "Detail"], [
            ["Eyes", "Roughly halfway down the head"],
        ]),
    },
    "art-g5-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Ancient Egyptian art convention", "Figures often shown in profile with frontal shoulders"],
        ]),
    },
    "art-g5-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"], ["Known for", "Visible brushstrokes, light effects"],
        ]),
    },
    "art-g5-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Abstract art", "Art that doesn't attempt to represent reality accurately"],
        ]),
    },
    "art-g5-l19": {
        "data_table": table(["Folk Art Style", "Region"], [
            ["Aboriginal dot painting", "Australia"], ["Molas", "Panama (Guna people)"],
        ]),
    },
    "art-g5-l20": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"], ["Wheel throwing", "Shaping clay on a spinning wheel"],
        ]),
    },
    "art-g5-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Mosaic", "Art made from small pieces of tile, glass, or stone"],
        ]),
    },
    "art-g5-l22": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows dialogue"],
        ]),
    },
    "art-g5-l23": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"], ["Layers", "Separate editable parts of an image"],
        ]),
    },
    "art-g5-l24": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g5-l25": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Dove", "Peace"], ["Heart", "Love"],
        ]),
    },
    "art-g5-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g5-l27": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ukiyo-e woodblock prints", "Japan"], ["Batik", "Indonesia"],
        ]),
    },
    "art-g5-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-portrait", "A drawing or painting of oneself"],
        ]),
    },
    "art-g5-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Perspective drawing", "Making a 2D drawing look 3D"],
        ]),
    },
    "art-g5-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Sketching", "Planning the composition before finishing"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 Art lessons (completing 30/30).")


if __name__ == "__main__":
    main()
