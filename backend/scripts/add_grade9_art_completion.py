#!/usr/bin/env python3
"""Depth pass, Grade 9 Art: fill in real, hand-checked data_table content
for the 48 Grade 9 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 9 Art to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Typography", "The art of arranging text"],
        ]),
    },
    "art-g9-l2": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D area"], ["Form", "A 3D object"],
        ]),
    },
    "art-g9-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Balance", "Even distribution of visual weight"], ["Contrast", "Difference between elements to create interest"],
        ]),
    },
    "art-g9-l5": {
        "data_table": table(["Color Type", "Examples"], [
            ["Primary", "Red, blue, yellow"], ["Secondary", "Green, orange, purple"],
        ]),
    },
    "art-g9-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Contour", "The outline of a form"],
        ]),
    },
    "art-g9-l7": {
        "data_table": table(["Technique", "Description"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Hatching", "Parallel lines to create shading"],
        ]),
    },
    "art-g9-l9": {
        "data_table": table(["Perspective Type", "Description"], [
            ["Two-point perspective", "Uses two vanishing points"],
        ]),
    },
    "art-g9-l10": {
        "data_table": table(["Proportion Guideline", "Detail"], [
            ["Figure height", "Often measured in 'head' units"],
        ]),
    },
    "art-g9-l11": {
        "data_table": table(["Proportion Guideline", "Detail"], [
            ["Eyes", "Roughly halfway down the head"],
        ]),
    },
    "art-g9-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g9-l13": {
        "data_table": table(["Element", "Example"], [
            ["Foreground", "What's closest, drawn largest"], ["Background", "What's farthest, drawn smallest"],
        ]),
    },
    "art-g9-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g9-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Acrylic paint", "Fast-drying, water-based paint"],
        ]),
    },
    "art-g9-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Oil paint", "Slow-drying paint using pigment bound in oil"],
        ]),
    },
    "art-g9-l17": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g9-l18": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"],
        ]),
    },
    "art-g9-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Assemblage", "Sculpture made from found objects"],
        ]),
    },
    "art-g9-l20": {
        "data_table": table(["Technique", "Description"], [
            ["Wheel throwing", "Shaping clay on a spinning wheel"],
        ]),
    },
    "art-g9-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g9-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Art history", "The study of visual art through different periods and cultures"],
        ]),
    },
    "art-g9-l23": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Egypt", "Figures shown in profile with frontal shoulders"], ["Mesopotamia", "Relief carvings and ziggurats"],
        ]),
    },
    "art-g9-l24": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Greece", "Idealized human forms in sculpture"], ["Ancient Rome", "Realistic portraiture"],
        ]),
    },
    "art-g9-l25": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "art-g9-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Baroque art", "17th century, known for drama and rich detail"],
        ]),
    },
    "art-g9-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"],
        ]),
    },
    "art-g9-l28": {
        "data_table": table(["Artist", "Movement"], [
            ["Vincent van Gogh", "Post-Impressionism"],
        ]),
    },
    "art-g9-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Cubism founders", "Pablo Picasso and Georges Braque"],
        ]),
    },
    "art-g9-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Surrealism", "Movement exploring dreams and the subconscious"],
        ]),
    },
    "art-g9-l31": {
        "data_table": table(["Artist", "Known For"], [
            ["Andy Warhol", "Pop art depicting everyday consumer items"],
        ]),
    },
    "art-g9-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Abstract Expressionism", "Post-WWII American movement emphasizing spontaneous gesture"],
        ]),
    },
    "art-g9-l33": {
        "data_table": table(["Element", "Purpose"], [
            ["Rule of thirds", "Guides balanced photo composition"],
        ]),
    },
    "art-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Exposure", "The amount of light captured in a photograph"],
        ]),
    },
    "art-g9-l35": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"],
        ]),
    },
    "art-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Graphic design", "Visual communication using images and text"],
        ]),
    },
    "art-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Animation", "Creating the illusion of motion from a sequence of images"],
        ]),
    },
    "art-g9-l38": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g9-l39": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Dove", "Peace"], ["Heart", "Love"],
        ]),
    },
    "art-g9-l40": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ukiyo-e woodblock prints", "Japan"],
        ]),
    },
    "art-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Mural", "A large painting applied directly to a wall"],
        ]),
    },
    "art-g9-l42": {
        "data_table": table(["Technique", "Description"], [
            ["Weaving", "Interlacing threads to create fabric"],
        ]),
    },
    "art-g9-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g9-l44": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Islamic geometric art", "Repeating shapes based on mathematical principles"],
        ]),
    },
    "art-g9-l45": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ink painting", "China and Japan"],
        ]),
    },
    "art-g9-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["African masks", "Used in ceremonies, often representing spirits or ancestors"],
        ]),
    },
    "art-g9-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous art of the Americas", "Includes totem poles, pottery, and weaving traditions"],
        ]),
    },
    "art-g9-l48": {
        "data_table": table(["Curation Step", "Purpose"], [
            ["Selecting works", "Chooses pieces that fit a theme"], ["Arranging", "Guides how viewers experience the exhibition"],
        ]),
    },
    "art-g9-l49": {
        "data_table": table(["Portfolio Element", "Purpose"], [
            ["Best work samples", "Showcases skill and range"], ["Artist statement", "Explains the artist's intent"],
        ]),
    },
    "art-g9-l50": {
        "data_table": table(["Career", "Focus"], [
            ["Illustrator", "Creates images for books, media, or products"], ["Art teacher", "Teaches art skills"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Art lessons (completing 50/50).")


if __name__ == "__main__":
    main()
