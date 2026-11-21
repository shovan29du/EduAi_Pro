#!/usr/bin/env python3
"""Depth pass, Grade 8 Art: fill in real, hand-checked data_table content
for the 38 Grade 8 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 8 Art to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g8-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Modernism", "Art movement rejecting traditional styles, late 19th-20th century"],
        ]),
    },
    "art-g8-l2": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D area"],
        ]),
    },
    "art-g8-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Balance", "Even distribution of visual weight"], ["Contrast", "Difference between elements to create interest"],
        ]),
    },
    "art-g8-l5": {
        "data_table": table(["Technique", "Description"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Perspective", "Making objects look closer or farther away"],
        ]),
    },
    "art-g8-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g8-l7": {
        "data_table": table(["Proportion Guideline", "Detail"], [
            ["Eyes", "Roughly halfway down the head"],
        ]),
    },
    "art-g8-l8": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g8-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g8-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Acrylic paint", "Fast-drying, water-based paint"],
        ]),
    },
    "art-g8-l11": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g8-l12": {
        "data_table": table(["Technique", "Description"], [
            ["Carving", "Removing material to reveal a form"], ["Modeling", "Building up material, like clay"],
        ]),
    },
    "art-g8-l13": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"],
        ]),
    },
    "art-g8-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g8-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Photography", "Creating images by capturing light"],
        ]),
    },
    "art-g8-l16": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"],
        ]),
    },
    "art-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Lascaux cave paintings", "Located in France, roughly 17,000 years old"],
        ]),
    },
    "art-g8-l18": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Greece", "Idealized human forms in sculpture"], ["Ancient Rome", "Realistic portraiture"],
        ]),
    },
    "art-g8-l19": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "art-g8-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"],
        ]),
    },
    "art-g8-l22": {
        "data_table": table(["Artist", "Movement"], [
            ["Vincent van Gogh", "Post-Impressionism"],
        ]),
    },
    "art-g8-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Cubism founders", "Pablo Picasso and Georges Braque"],
        ]),
    },
    "art-g8-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Surrealism", "Movement exploring dreams and the subconscious"],
        ]),
    },
    "art-g8-l25": {
        "data_table": table(["Artist", "Known For"], [
            ["Andy Warhol", "Pop art depicting everyday consumer items"],
        ]),
    },
    "art-g8-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Abstract Expressionism", "Post-WWII American movement emphasizing spontaneous gesture"],
        ]),
    },
    "art-g8-l27": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Islamic geometric art", "Repeating shapes based on mathematical principles"],
        ]),
    },
    "art-g8-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["African masks", "Used in ceremonies, often representing spirits or ancestors"],
        ]),
    },
    "art-g8-l29": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ukiyo-e woodblock prints", "Japan"],
        ]),
    },
    "art-g8-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous art of the Americas", "Includes totem poles, pottery, and weaving traditions"],
        ]),
    },
    "art-g8-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Graphic design", "Visual communication using images and text"],
        ]),
    },
    "art-g8-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Typography", "The art of arranging text"],
        ]),
    },
    "art-g8-l33": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"],
        ]),
    },
    "art-g8-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g8-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g8-l36": {
        "data_table": table(["Principle", "Meaning"], [
            ["Composition", "The arrangement of elements in an artwork"],
        ]),
    },
    "art-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Perspective drawing", "Making a 2D drawing look 3D"],
        ]),
    },
    "art-g8-l38": {
        "data_table": table(["Technique", "Description"], [
            ["Weaving", "Interlacing threads to create fabric"],
        ]),
    },
    "art-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Mural", "A large painting applied directly to a wall"],
        ]),
    },
    "art-g8-l40": {
        "data_table": table(["Career", "Focus"], [
            ["Illustrator", "Creates images for books, media, or products"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Art lessons (completing 40/40).")


if __name__ == "__main__":
    main()
