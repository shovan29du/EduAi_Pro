#!/usr/bin/env python3
"""Depth pass, Grade 1 World Literature: fill in real, hand-checked
data_table content for the 17 Grade 1 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 1 World
Literature to full 20/20 coverage.

Every fact is real (real folktale origins, real publication dates for
Andersen's tales, the real Panchatantra compilation period, real author
attributions) -- nothing fabricated or presented as fact when it's
actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g1-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Genre", "Traditional stories passed down orally across many cultures"],
            ["Purpose", "Teaching lessons and passing on cultural values"],
        ]),
    },
    "world-literature-g1-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aesop's Fables, Ancient Greece"], ["Moral", "Slow and steady wins the race"],
        ]),
    },
    "world-literature-g1-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aesop's Fables, Ancient Greece"],
            ["Moral", "Lying makes people stop believing you"],
        ]),
    },
    "world-literature-g1-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "West African (Ashanti) folklore"],
            ["Character", "Anansi, a clever trickster spider"],
        ]),
    },
    "world-literature-g1-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "European folktale, best known from Charles Perrault (1697) and the Brothers Grimm (1812)"],
            ["Moral", "Be cautious of strangers"],
        ]),
    },
    "world-literature-g1-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "English folktale"], ["Moral", "Hard work and good planning pay off"],
        ]),
    },
    "world-literature-g1-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "English folktale, popularized by Robert Southey (1837)"],
            ["Moral", "Respect other people's belongings"],
        ]),
    },
    "world-literature-g1-l9": {
        "data_table": table(["Version", "Origin"], [
            ["Rhodopis", "Ancient Egypt/Greece (oldest known recorded version)"],
            ["Ye Xian", "China (Tang dynasty, 9th century)"],
            ["Cendrillon", "France (Charles Perrault, 1697)"],
        ]),
    },
    "world-literature-g1-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Published", "1843"],
            ["Moral", "True beauty and worth take time to be recognized"],
        ]),
    },
    "world-literature-g1-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Published", "1837"],
            ["Moral", "Speaking the truth even when others don't"],
        ]),
    },
    "world-literature-g1-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India, compiled c. 200 BCE-300 CE"],
            ["Content", "Animal fables teaching wisdom"],
        ]),
    },
    "world-literature-g1-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Japanese folktale"],
            ["Character", "Momotaro, 'Peach Boy', born from a giant peach"],
        ]),
    },
    "world-literature-g1-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "African American folklore, rooted in West African trickster tales"],
            ["Character", "Br'er Rabbit, a clever trickster"],
        ]),
    },
    "world-literature-g1-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "German folktale, Brothers Grimm (1812)"], ["Moral", "Keeping promises matters"],
        ]),
    },
    "world-literature-g1-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Various Native American traditions"],
            ["Character", "Coyote, a common trickster figure"],
        ]),
    },
    "world-literature-g1-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Published", "1837"],
        ]),
    },
    "world-literature-g1-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Published", "1843"], ["Setting", "Imperial China"],
        ]),
    },
    "world-literature-g1-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Chinese novel, published 16th century"],
            ["Attributed author", "Wu Cheng'en"], ["Main character", "Sun Wukong, the Monkey King"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 World Literature lessons (completing 20/20).")


if __name__ == "__main__":
    main()
