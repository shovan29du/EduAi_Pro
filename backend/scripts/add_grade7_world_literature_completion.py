#!/usr/bin/env python3
"""Depth pass, Grade 7 World Literature: fill in real, hand-checked
data_table content for the 38 Grade 7 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 7 World
Literature to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g7-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Novel", "A long fictional narrative"], ["Theme", "The underlying message of a story"],
        ]),
    },
    "world-literature-g7-l2": {
        "data_table": table(["Author", "Known For"], [
            ["Anton Chekhov", "Master of the short story form"],
        ]),
    },
    "world-literature-g7-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short animal stories with morals"],
        ]),
    },
    "world-literature-g7-l4": {
        "data_table": table(["God/Hero", "Known For"], [
            ["Zeus", "King of the gods"], ["Hercules", "Twelve legendary labors"],
        ]),
    },
    "world-literature-g7-l5": {
        "data_table": table(["Figure", "Known For"], [
            ["Odin", "Chief god, associated with wisdom"], ["Thor", "God of thunder"],
        ]),
    },
    "world-literature-g7-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Playwright", "William Shakespeare"], ["Country", "England"],
        ]),
    },
    "world-literature-g7-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Collectors", "Jacob and Wilhelm Grimm"], ["Country", "Germany"],
        ]),
    },
    "world-literature-g7-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Fantasy", "Fiction featuring magical or supernatural elements"],
        ]),
    },
    "world-literature-g7-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Science fiction", "Fiction based on imagined science or technology"],
        ]),
    },
    "world-literature-g7-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Mystery", "A story centered on solving a puzzle or crime"],
        ]),
    },
    "world-literature-g7-l12": {
        "data_table": table(["Genre", "Definition"], [
            ["Historical fiction", "Invented story set in a real historical period"],
        ]),
    },
    "world-literature-g7-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Coming-of-age story", "A story about a character growing from youth to maturity"],
        ]),
    },
    "world-literature-g7-l14": {
        "data_table": table(["Element", "Purpose"], [
            ["Panel", "One frame of the story"], ["Speech bubble", "Shows dialogue"],
        ]),
    },
    "world-literature-g7-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Drama", "A story written to be performed"], ["Playwright", "A person who writes plays"],
        ]),
    },
    "world-literature-g7-l17": {
        "data_table": table(["Tradition", "Region"], [
            ["Griot storytelling", "West Africa"],
        ]),
    },
    "world-literature-g7-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Translation", "Rendering a text into another language"],
        ]),
    },
    "world-literature-g7-l19": {
        "data_table": table(["Author", "Region"], [
            ["Chinua Achebe", "Nigeria"], ["Wole Soyinka", "Nigeria, Nobel laureate in Literature"],
        ]),
    },
    "world-literature-g7-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Journey to the West", "Classic Chinese novel"], ["The Tale of Genji", "Classic Japanese novel"],
        ]),
    },
    "world-literature-g7-l21": {
        "data_table": table(["Author", "Country"], [
            ["Gabriel Garcia Marquez", "Colombia, known for magical realism"],
        ]),
    },
    "world-literature-g7-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["One Thousand and One Nights", "Collection of Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g7-l23": {
        "data_table": table(["Author", "Country"], [
            ["Victor Hugo", "France"], ["Leo Tolstoy", "Russia"],
        ]),
    },
    "world-literature-g7-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Dystopia", "An imagined society that is undesirable or frightening"],
        ]),
    },
    "world-literature-g7-l25": {
        "data_table": table(["Novel", "Author"], [
            ["Robinson Crusoe", "Daniel Defoe"], ["Treasure Island", "Robert Louis Stevenson"],
        ]),
    },
    "world-literature-g7-l26": {
        "data_table": table(["Genre", "Definition"], [
            ["Memoir", "A personal account focused on specific experiences"],
        ]),
    },
    "world-literature-g7-l27": {
        "data_table": table(["Award", "Field"], [
            ["Nobel Prize in Literature", "Awarded for outstanding literary contributions"],
            ["Newbery Medal", "Awarded for children's literature (US)"],
        ]),
    },
    "world-literature-g7-l28": {
        "data_table": table(["Book", "Author"], [
            ["Alice's Adventures in Wonderland", "Lewis Carroll"], ["The Jungle Book", "Rudyard Kipling"],
        ]),
    },
    "world-literature-g7-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Allegory", "A story with a hidden symbolic meaning"],
        ]),
    },
    "world-literature-g7-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Satire", "Using humor or irony to criticize behavior or ideas"],
        ]),
    },
    "world-literature-g7-l31": {
        "data_table": table(["Movement", "Approximate Period"], [
            ["Romanticism", "Late 18th to mid-19th century"],
        ]),
    },
    "world-literature-g7-l32": {
        "data_table": table(["Movement", "Approximate Period"], [
            ["Realism", "Mid to late 19th century"],
        ]),
    },
    "world-literature-g7-l33": {
        "data_table": table(["Format", "Strength"], [
            ["Book", "Rich internal detail and description"], ["Film", "Visual and audio storytelling"],
        ]),
    },
    "world-literature-g7-l34": {
        "data_table": table(["Archetype", "Example"], [
            ["The hero", "A protagonist who overcomes challenges"], ["The mentor", "A wise guide figure"],
        ]),
    },
    "world-literature-g7-l35": {
        "data_table": table(["Point of View", "Pronoun Used"], [
            ["First person", "I, we"], ["Third person", "he, she, they"],
        ]),
    },
    "world-literature-g7-l36": {
        "data_table": table(["Story", "Theme of Courage"], [
            ["The Odyssey", "Odysseus's perseverance through trials"],
        ]),
    },
    "world-literature-g7-l37": {
        "data_table": table(["Story", "Theme of Friendship"], [
            ["The Lion and the Mouse", "Small acts of kindness are never wasted"],
        ]),
    },
    "world-literature-g7-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["The hero's journey", "A common narrative pattern of a hero's adventure and return"],
        ]),
    },
    "world-literature-g7-l39": {
        "data_table": table(["Proverb", "Meaning"], [
            ["'A stitch in time saves nine'", "Fixing a problem early prevents it from getting worse"],
        ]),
    },
    "world-literature-g7-l40": {
        "data_table": table(["Concept", "Meaning"], [
            ["Representation", "Seeing diverse characters and experiences reflected in literature"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 World Literature lessons (completing 40/40).")


if __name__ == "__main__":
    main()
