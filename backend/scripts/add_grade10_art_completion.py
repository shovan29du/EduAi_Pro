#!/usr/bin/env python3
"""Depth pass, Grade 10 Art: fill in real, hand-checked data_table
content for the Grade 10 Art lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Art to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g10-l1": {
        "data_table": table(["Skill", "Purpose"], [
            ["Formal analysis", "Examines composition, color, and technique"],
        ]),
    },
    "art-g10-l2": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D enclosed area"],
        ]),
    },
    "art-g10-l4": {
        "data_table": table(["Principle", "Meaning"], [
            ["Balance", "Even distribution of visual weight"], ["Contrast", "Difference between elements to create interest"],
        ]),
    },
    "art-g10-l5": {
        "data_table": table(["Principle", "Meaning"], [
            ["Rhythm", "Repeated elements creating visual movement"],
        ]),
    },
    "art-g10-l6": {
        "data_table": table(["Perspective Type", "Description"], [
            ["One-point perspective", "Uses a single vanishing point"], ["Two-point perspective", "Uses two vanishing points"],
        ]),
    },
    "art-g10-l7": {
        "data_table": table(["Technique", "Description"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Hatching", "Parallel lines to create shading"],
        ]),
    },
    "art-g10-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g10-l9": {
        "data_table": table(["Medium", "Property"], [
            ["Acrylic", "Fast-drying, water-based"], ["Oil paint", "Slow-drying, pigment bound in oil"],
        ]),
    },
    "art-g10-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Sculpture", "Three-dimensional art made by carving, modeling, or assembling"],
        ]),
    },
    "art-g10-l11": {
        "data_table": table(["Technique", "Description"], [
            ["Woodblock printing", "Carving an image into wood to make repeated prints"],
        ]),
    },
    "art-g10-l12": {
        "data_table": table(["Technique", "Description"], [
            ["Wheel throwing", "Shaping clay on a spinning wheel"],
        ]),
    },
    "art-g10-l13": {
        "data_table": table(["Element", "Purpose"], [
            ["Rule of thirds", "Guides balanced photo composition"],
        ]),
    },
    "art-g10-l14": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"],
        ]),
    },
    "art-g10-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Graphic design", "Visual communication using images and text"],
        ]),
    },
    "art-g10-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Typography", "The art of arranging text"],
        ]),
    },
    "art-g10-l17": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Egypt", "Figures shown in profile with frontal shoulders"],
        ]),
    },
    "art-g10-l18": {
        "data_table": table(["Civilization", "Art Style"], [
            ["Ancient Greece", "Idealized human forms in sculpture"], ["Ancient Rome", "Realistic portraiture"],
        ]),
    },
    "art-g10-l19": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "art-g10-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"],
        ]),
    },
    "art-g10-l22": {
        "data_table": table(["Artist", "Movement"], [
            ["Vincent van Gogh", "Post-Impressionism"],
        ]),
    },
    "art-g10-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Cubism founders", "Pablo Picasso and Georges Braque"],
        ]),
    },
    "art-g10-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Surrealism", "Movement exploring dreams and the subconscious"],
        ]),
    },
    "art-g10-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Abstract Expressionism", "Post-WWII American movement emphasizing spontaneous gesture"],
        ]),
    },
    "art-g10-l26": {
        "data_table": table(["Artist", "Known For"], [
            ["Andy Warhol", "Pop art depicting everyday consumer items"],
        ]),
    },
    "art-g10-l27": {
        "data_table": table(["Art Form", "Characteristic"], [
            ["Islamic geometric art", "Repeating shapes based on mathematical principles"],
        ]),
    },
    "art-g10-l28": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ink painting", "China"],
        ]),
    },
    "art-g10-l29": {
        "data_table": table(["Art Tradition", "Region"], [
            ["Ukiyo-e woodblock prints", "Japan"],
        ]),
    },
    "art-g10-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["African masks", "Used in ceremonies, often representing spirits or ancestors"],
        ]),
    },
    "art-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous art of the Americas", "Includes totem poles, pottery, and weaving traditions"],
        ]),
    },
    "art-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Street art", "Visual art created in public locations"],
        ]),
    },
    "art-g10-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Portraiture", "The art of depicting a person's likeness"],
        ]),
    },
    "art-g10-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Landscape art", "Depicts natural scenery as the primary subject"],
        ]),
    },
    "art-g10-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Still life", "Art depicting inanimate objects, like fruit or flowers"],
        ]),
    },
    "art-g10-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g10-l37": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g10-l38": {
        "data_table": table(["Curation Step", "Purpose"], [
            ["Selecting works", "Chooses pieces that fit a theme"],
        ]),
    },
    "art-g10-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Mural", "A large painting applied directly to a wall"],
        ]),
    },
    "art-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Fashion design", "The art of creating clothing and accessories"],
        ]),
    },
    "art-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Illustration", "Visual art created to accompany or explain a text"],
        ]),
    },
    "art-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Animation", "Creating the illusion of motion from a sequence of images"],
        ]),
    },
    "art-g10-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["Art as social commentary", "Used to critique political or social issues"],
        ]),
    },
    "art-g10-l45": {
        "data_table": table(["Portfolio Element", "Purpose"], [
            ["Best work samples", "Showcases skill and range"], ["Artist statement", "Explains the artist's intent"],
        ]),
    },
    "art-g10-l46": {
        "data_table": table(["Principle", "Meaning"], [
            ["Composition", "The arrangement of visual elements in a work"],
        ]),
    },
    "art-g10-l47": {
        "data_table": table(["Symbol", "Common Meaning"], [
            ["Dove", "Peace"], ["Heart", "Love"],
        ]),
    },
    "art-g10-l48": {
        "data_table": table(["Movement", "Feature"], [
            ["Contemporary art", "Art produced from the late 20th century to today"],
        ]),
    },
    "art-g10-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Art conservation", "Preserving and restoring artworks for future generations"],
        ]),
    },
    "art-g10-l50": {
        "data_table": table(["Term", "Role"], [
            ["Gallery", "Sells and exhibits art"], ["Art market", "The buying and selling of artworks"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Art lessons (completing 50/50).")


if __name__ == "__main__":
    main()
