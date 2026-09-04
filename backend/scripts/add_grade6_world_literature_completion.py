#!/usr/bin/env python3
"""Depth pass, Grade 6 World Literature: fill in real, hand-checked
data_table content for the 28 Grade 6 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 6 World
Literature to full 30/30 coverage.

Content covers real literary/folk origins -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade6_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade6.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g6-l1": {
        "data_table": table(["Author", "Known For"], [
            ["Anton Chekhov", "Master of the short story form"], ["Guy de Maupassant", "French short story writer"],
        ]),
    },
    "world-literature-g6-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short animal stories with morals"],
        ]),
    },
    "world-literature-g6-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g6-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Collectors", "Jacob and Wilhelm Grimm"], ["Country", "Germany"],
        ]),
    },
    "world-literature-g6-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Country", "Denmark"],
        ]),
    },
    "world-literature-g6-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Playwright", "William Shakespeare"], ["Country", "England"],
        ]),
    },
    "world-literature-g6-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Mark Twain"], ["Famous work", "The Adventures of Tom Sawyer"],
        ]),
    },
    "world-literature-g6-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Charles Dickens"], ["Famous work", "Oliver Twist"],
        ]),
    },
    "world-literature-g6-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Jules Verne"], ["Famous work", "Twenty Thousand Leagues Under the Sea"],
        ]),
    },
    "world-literature-g6-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Rudyard Kipling"], ["Famous work", "The Jungle Book"],
        ]),
    },
    "world-literature-g6-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Lewis Carroll"], ["Famous work", "Alice's Adventures in Wonderland"],
        ]),
    },
    "world-literature-g6-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "China"], ["Character", "Sun Wukong, the Monkey King"],
        ]),
    },
    "world-literature-g6-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "Japan"], ["Example", "Momotaro, the Peach Boy"],
        ]),
    },
    "world-literature-g6-l16": {
        "data_table": table(["Tradition", "Region"], [
            ["Griot storytelling", "West Africa"],
        ]),
    },
    "world-literature-g6-l17": {
        "data_table": table(["God/Hero", "Known For"], [
            ["Zeus", "King of the gods"], ["Hercules", "Twelve legendary labors"],
        ]),
    },
    "world-literature-g6-l18": {
        "data_table": table(["Figure", "Known For"], [
            ["Odin", "Chief god, associated with wisdom"], ["Thor", "God of thunder"],
        ]),
    },
    "world-literature-g6-l19": {
        "data_table": table(["Region", "Example"], [
            ["Latin America", "La Llorona legend"],
        ]),
    },
    "world-literature-g6-l20": {
        "data_table": table(["Poet", "Country"], [
            ["Rumi", "Persia"], ["Matsuo Basho", "Japan"],
        ]),
    },
    "world-literature-g6-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Novel", "A long fictional narrative"],
        ]),
    },
    "world-literature-g6-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Drama", "A story written to be performed"], ["Playwright", "A person who writes plays"],
        ]),
    },
    "world-literature-g6-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Coming-of-age story", "A story about a character growing from youth to maturity"],
        ]),
    },
    "world-literature-g6-l24": {
        "data_table": table(["Novel", "Author"], [
            ["Robinson Crusoe", "Daniel Defoe"], ["Treasure Island", "Robert Louis Stevenson"],
        ]),
    },
    "world-literature-g6-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["World-building", "Creating a fictional setting with its own rules"],
        ]),
    },
    "world-literature-g6-l26": {
        "data_table": table(["Genre", "Definition"], [
            ["Historical fiction", "Invented story set in a real historical period"],
        ]),
    },
    "world-literature-g6-l27": {
        "data_table": table(["Genre", "Definition"], [
            ["Biography", "A true account of someone else's life"],
            ["Memoir", "A personal account focused on specific experiences"],
        ]),
    },
    "world-literature-g6-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Translation", "Rendering a text into another language"],
        ]),
    },
    "world-literature-g6-l29": {
        "data_table": table(["Author", "Region"], [
            ["Jamaica Kincaid", "Antigua/Caribbean"],
        ]),
    },
    "world-literature-g6-l30": {
        "data_table": table(["Author", "Country"], [
            ["Katherine Rundell", "United Kingdom"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade6.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 6 World Literature lessons (completing 30/30).")


if __name__ == "__main__":
    main()
