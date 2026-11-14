#!/usr/bin/env python3
"""Depth pass, Grade 7 Art: fill in real, hand-checked data_table content
for the 38 Grade 7 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 7 Art to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g7-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Abstract art", "Art that doesn't attempt to represent reality accurately"],
        ]),
    },
    "art-g7-l2": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D area"], ["Form", "A 3D object"],
        ]),
    },
    "art-g7-l3": {
        "data_table": table(["Element", "Meaning"], [
            ["Color", "Hue, the visual property of light"], ["Value", "Lightness or darkness of a color"], ["Texture", "Surface quality"],
        ]),
    },
    "art-g7-l4": {
        "data_table": table(["Principle", "Meaning"], [
            ["Balance", "Even distribution of visual weight"], ["Contrast", "Difference between elements to create interest"],
        ]),
    },
    "art-g7-l5": {
        "data_table": table(["Principle", "Meaning"], [
            ["Emphasis", "Drawing attention to a focal point"], ["Movement", "Guiding the eye through the artwork"],
        ]),
    },
    "art-g7-l6": {
        "data_table": table(["Principle", "Meaning"], [
            ["Pattern", "A repeated design element"], ["Rhythm", "Visual beat created by repetition"],
        ]),
    },
    "art-g7-l8": {
        "data_table": table(["Technique", "Description"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Hatching", "Parallel lines to create shading"],
        ]),
    },
    "art-g7-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g7-l11": {
        "data_table": table(["Proportion Guideline", "Detail"], [
            ["Eyes", "Roughly halfway down the head"],
        ]),
    },
    "art-g7-l12": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g7-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g7-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Acrylic paint", "Fast-drying, water-based paint"],
        ]),
    },
    "art-g7-l15": {
        "data_table": table(["Technique", "Description"], [
            ["Carving", "Removing material to reveal a form"], ["Modeling", "Building up material, like clay"],
        ]),
    },
    "art-g7-l16": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g7-l17": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"], ["Wheel throwing", "Shaping clay on a spinning wheel"],
        ]),
    },
    "art-g7-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g7-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Photography", "Creating images by capturing light"],
        ]),
    },
    "art-g7-l20": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"], ["Layers", "Separate editable parts of an image"],
        ]),
    },
    "art-g7-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Graphic design", "Visual communication using images and text"],
        ]),
    },
    "art-g7-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Typography", "The art of arranging text"],
        ]),
    },
    "art-g7-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Animation", "Creating the illusion of motion from a sequence of images"],
        ]),
    },
    "art-g7-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Mural", "A large painting applied directly to a wall"],
        ]),
    },
    "art-g7-l25": {
        "data_table": table(["Technique", "Description"], [
            ["Weaving", "Interlacing threads to create fabric"],
        ]),
    },
    "art-g7-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g7-l27": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows dialogue"],
        ]),
    },
    "art-g7-l28": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "art-g7-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"], ["Known for", "Visible brushstrokes, light effects"],
        ]),
    },
    "art-g7-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Cubism", "Early 20th century movement showing multiple perspectives at once"],
            ["Founders", "Pablo Picasso and Georges Braque"],
        ]),
    },
    "art-g7-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Surrealism", "Movement exploring dreams and the subconscious"],
            ["Notable artist", "Salvador Dali"],
        ]),
    },
    "art-g7-l32": {
        "data_table": table(["Artist", "Known For"], [
            ["Andy Warhol", "Pop art depicting everyday consumer items"],
        ]),
    },
    "art-g7-l33": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Egypt", "Figures shown in profile with frontal shoulders"],
            ["Ancient Greece", "Idealized human forms in sculpture"],
        ]),
    },
    "art-g7-l34": {
        "data_table": table(["Folk Art Style", "Region"], [
            ["Aboriginal dot painting", "Australia"], ["Molas", "Panama (Guna people)"],
        ]),
    },
    "art-g7-l35": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Dove", "Peace"], ["Heart", "Love"],
        ]),
    },
    "art-g7-l36": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g7-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-portrait", "A drawing or painting of oneself"],
        ]),
    },
    "art-g7-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Land art", "Art created directly in the natural landscape"],
        ]),
    },
    "art-g7-l39": {
        "data_table": table(["Career", "Focus"], [
            ["Illustrator", "Creates images for books, media, or products"], ["Art teacher", "Teaches art skills to students"],
        ]),
    },
    "art-g7-l40": {
        "data_table": table(["Portfolio Element", "Purpose"], [
            ["Best work samples", "Showcases skill and range"], ["Artist statement", "Explains the artist's intent"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 Art lessons (completing 40/40).")


if __name__ == "__main__":
    main()
