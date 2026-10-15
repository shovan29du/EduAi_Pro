#!/usr/bin/env python3
"""Depth pass, Grade 1 Art: fill in real, hand-checked data_table content
for the 17 Grade 1 Art lessons not covered by the earlier breadth-first
batch. Brings Grade 1 Art to full 20/20 coverage.

Content covers real, verifiable art technique facts (shape/side counts,
watercolor technique names, real cultural art form origins) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_art_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "art-g1-l1": {
        "data_table": table(["Shape", "Number of Sides"], [
            ["Circle", "0"], ["Triangle", "3"], ["Square", "4"],
        ]),
    },
    "art-g1-l3": {
        "data_table": table(["Technique", "Effect"], [
            ["Wet-on-wet", "Colors blend softly"], ["Wet-on-dry", "Creates sharper edges"],
        ]),
    },
    "art-g1-l4": {
        "data_table": table(["Shape", "Everyday Object"], [
            ["Circle", "A ball"], ["Square", "A window"], ["Triangle", "A slice of pizza"],
        ]),
    },
    "art-g1-l5": {
        "data_table": table(["Material", "Example"], [
            ["Paper", "Colored construction paper"], ["Fabric", "Cloth scraps"],
            ["Natural items", "Leaves, dried flowers"],
        ]),
    },
    "art-g1-l6": {
        "data_table": table(["Technique", "Description"], [
            ["Pinching", "Shaping clay with fingers"], ["Rolling", "Making coils or flat sheets"],
        ]),
    },
    "art-g1-l7": {
        "data_table": table(["Object Used", "Print Pattern"], [
            ["Potato stamp", "Simple carved shapes"], ["Sponge", "Textured dabs"],
        ]),
    },
    "art-g1-l8": {
        "data_table": table(["Line Type", "Example"], [
            ["Straight", "A ruler's edge"], ["Zigzag", "A lightning bolt shape"], ["Curved", "A wave"],
        ]),
    },
    "art-g1-l9": {
        "data_table": table(["Texture", "Example"], [
            ["Rough", "Tree bark, sandpaper"], ["Smooth", "Glass, polished stone"],
        ]),
    },
    "art-g1-l10": {
        "data_table": table(["Face Feature", "Typical Position"], [
            ["Eyes", "Middle of the head"], ["Nose", "Below the eyes"], ["Mouth", "Below the nose"],
        ]),
    },
    "art-g1-l11": {
        "data_table": table(["Natural Material", "Use in Art"], [
            ["Leaves", "Leaf rubbings and prints"], ["Flowers", "Pressed flower art"],
        ]),
    },
    "art-g1-l12": {
        "data_table": table(["Origami Shape", "Fold Complexity"], [
            ["Paper boat", "A few simple folds"], ["Paper crane", "More folds, more advanced"],
        ]),
    },
    "art-g1-l13": {
        "data_table": table(["Primary Colours Mixed", "Secondary Colour Made"], [
            ["Red + Yellow", "Orange"], ["Yellow + Blue", "Green"], ["Blue + Red", "Purple"],
        ]),
    },
    "art-g1-l15": {
        "data_table": table(["Art Form", "Culture"], [
            ["Origami", "Japan"], ["Mandala", "India"], ["Aboriginal dot painting", "Australia"],
        ]),
    },
    "art-g1-l16": {
        "data_table": table(["Animal", "Simple Shapes Used"], [
            ["Cat", "Circles and triangles (ears)"], ["Fish", "Oval and triangle (tail)"],
        ]),
    },
    "art-g1-l17": {
        "data_table": table(["Material", "Effect"], [
            ["Chalk", "Soft, dusty texture"], ["Pastel", "Rich, blendable color"],
        ]),
    },
    "art-g1-l18": {
        "data_table": table(["Puppet Type", "How It's Made"], [
            ["Sock puppet", "A sock with attached eyes"], ["Paper bag puppet", "A folded paper bag"],
        ]),
    },
    "art-g1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Symmetry", "When one half of an image mirrors the other"], ["Example", "A butterfly's wings"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Art"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json Art: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 Art lessons (completing 20/20).")


if __name__ == "__main__":
    main()
