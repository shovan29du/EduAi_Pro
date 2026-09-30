#!/usr/bin/env python3
"""Depth pass, Grade 6 Art: fill in real, hand-checked data_table content
for the 28 Grade 6 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 6 Art to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g6-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Portrait", "An artwork depicting a person"], ["Expression", "The emotion shown on a face"],
        ]),
    },
    "art-g6-l2": {
        "data_table": table(["Element", "Meaning"], [
            ["Line", "A mark connecting two points"], ["Shape", "A 2D area"], ["Form", "A 3D object"],
        ]),
    },
    "art-g6-l3": {
        "data_table": table(["Principle", "Meaning"], [
            ["Balance", "Even distribution of visual weight"], ["Contrast", "Difference between elements to create interest"],
        ]),
    },
    "art-g6-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Shading", "Using darker or lighter tones to show depth"], ["Perspective", "Making objects look closer or farther away"],
        ]),
    },
    "art-g6-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Watercolor", "Paint made with pigment and water, often translucent"],
        ]),
    },
    "art-g6-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Acrylic paint", "Fast-drying, water-based paint"],
        ]),
    },
    "art-g6-l8": {
        "data_table": table(["Technique", "Description"], [
            ["Carving", "Removing material to reveal a form"], ["Modeling", "Building up material, like clay"],
        ]),
    },
    "art-g6-l9": {
        "data_table": table(["Technique", "Description"], [
            ["Stamping", "Pressing an inked object onto paper"],
        ]),
    },
    "art-g6-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Collage", "Art made by gluing different materials onto a surface"],
        ]),
    },
    "art-g6-l11": {
        "data_table": table(["Technique", "Description"], [
            ["Pinch pot", "Shaping clay by pinching with fingers"], ["Wheel throwing", "Shaping clay on a spinning wheel"],
        ]),
    },
    "art-g6-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Lascaux cave paintings", "Located in France, roughly 17,000 years old"],
        ]),
    },
    "art-g6-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Ancient Egyptian art convention", "Figures often shown in profile with frontal shoulders"],
        ]),
    },
    "art-g6-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Greek sculpture", "Known for idealized human forms"], ["Roman art", "Known for realistic portraiture"],
        ]),
    },
    "art-g6-l15": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "art-g6-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Impressionism began", "1870s, in France"], ["Known for", "Visible brushstrokes, light effects"],
        ]),
    },
    "art-g6-l17": {
        "data_table": table(["Movement", "Approximate Period"], [
            ["Cubism", "Early 20th century"], ["Surrealism", "1920s onward"],
        ]),
    },
    "art-g6-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Abstract art", "Art that doesn't attempt to represent reality accurately"],
        ]),
    },
    "art-g6-l19": {
        "data_table": table(["Artist", "Known For"], [
            ["Andy Warhol", "Pop art depicting everyday consumer items"],
        ]),
    },
    "art-g6-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["African masks", "Used in ceremonies, often representing spirits or ancestors"],
        ]),
    },
    "art-g6-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Ink painting", "A traditional East Asian painting style using ink and brush"],
        ]),
    },
    "art-g6-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous art of the Americas", "Includes totem poles, pottery, and weaving traditions"],
        ]),
    },
    "art-g6-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Photography", "Creating images by capturing light"],
        ]),
    },
    "art-g6-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Architecture", "The art and science of designing buildings"],
        ]),
    },
    "art-g6-l26": {
        "data_table": table(["Step", "Purpose"], [
            ["Describe", "State what you see"], ["Interpret", "Explain what it might mean"],
        ]),
    },
    "art-g6-l27": {
        "data_table": table(["Comic Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows dialogue"],
        ]),
    },
    "art-g6-l28": {
        "data_table": table(["Tool", "Use"], [
            ["Digital brush", "Simulates painting on a tablet or computer"], ["Layers", "Separate editable parts of an image"],
        ]),
    },
    "art-g6-l29": {
        "data_table": table(["Technique", "Description"], [
            ["Weaving", "Interlacing threads to create fabric"],
        ]),
    },
    "art-g6-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Mural", "A large painting applied directly to a wall"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 Art lessons (completing 30/30).")


if __name__ == "__main__":
    main()
