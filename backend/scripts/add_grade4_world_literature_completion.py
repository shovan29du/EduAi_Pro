#!/usr/bin/env python3
"""Depth pass, Grade 4 World Literature: fill in real, hand-checked
data_table content for the 28 Grade 4 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 4 World
Literature to full 30/30 coverage.

Content covers real folk/legend origins -- nothing fabricated or
presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade4_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade4.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g4-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Genre", "Stories written for young readers"], ["Purpose", "Entertainment and moral lessons"],
        ]),
    },
    "world-literature-g4-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short stories with animal characters and morals"],
        ]),
    },
    "world-literature-g4-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g4-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Collectors", "Jacob and Wilhelm Grimm"], ["Country", "Germany"],
        ]),
    },
    "world-literature-g4-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Country", "Denmark"],
        ]),
    },
    "world-literature-g4-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India"], ["Purpose", "Teaching wisdom through animal stories"],
        ]),
    },
    "world-literature-g4-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "West African oral tradition"], ["Character", "Anansi, a clever trickster spider"],
        ]),
    },
    "world-literature-g4-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "Japan"], ["Example", "Momotaro, the Peach Boy"],
        ]),
    },
    "world-literature-g4-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "China"], ["Example", "Journey to the West"],
        ]),
    },
    "world-literature-g4-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Indigenous peoples of North America"], ["Purpose", "Passing down cultural values orally"],
        ]),
    },
    "world-literature-g4-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Aboriginal Australian culture"], ["Theme", "Explains the creation of the world"],
        ]),
    },
    "world-literature-g4-l12": {
        "data_table": table(["Poet", "Country"], [
            ["Rumi", "Persia (modern-day Iran/Afghanistan)"], ["Hafez", "Persia"],
        ]),
    },
    "world-literature-g4-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "Korea"], ["Theme", "Often features clever animals and moral lessons"],
        ]),
    },
    "world-literature-g4-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Caribbean, rooted in West African Anansi tales"],
        ]),
    },
    "world-literature-g4-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Country", "Russia"], ["Example character", "Baba Yaga, a witch figure"],
        ]),
    },
    "world-literature-g4-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Region", "Latin America"], ["Example", "La Llorona legend"],
        ]),
    },
    "world-literature-g4-l19": {
        "data_table": table(["Version", "Origin"], [
            ["Cendrillon", "France"], ["Ye Xian", "China"],
        ]),
    },
    "world-literature-g4-l20": {
        "data_table": table(["Tradition", "Region"], [
            ["Griot storytelling", "West Africa"], ["Oral epic recitation", "Ancient Greece"],
        ]),
    },
    "world-literature-g4-l21": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Bedtime reading", "Sharing classic tales with younger siblings"],
        ]),
    },
    "world-literature-g4-l22": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Learning honesty", "Recognizing a fable's moral in real situations"],
        ]),
    },
    "world-literature-g4-l23": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Storytelling traditions", "Sharing adventure tales at gatherings"],
        ]),
    },
    "world-literature-g4-l24": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Cultural festivals", "Fairy tale themed events"],
        ]),
    },
    "world-literature-g4-l25": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Life lessons", "Andersen's tales often teach empathy"],
        ]),
    },
    "world-literature-g4-l26": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Teaching wisdom", "Using animal fables to discuss decisions"],
        ]),
    },
    "world-literature-g4-l27": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Cleverness in problem-solving", "Applying a trickster character's cunning"],
        ]),
    },
    "world-literature-g4-l28": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Cultural exchange", "Comparing folk tales across countries"],
        ]),
    },
    "world-literature-g4-l29": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Understanding history", "Legends reflect a culture's values"],
        ]),
    },
    "world-literature-g4-l30": {
        "data_table": table(["Real-Life Use", "Example"], [
            ["Community storytelling", "Sharing legends at family gatherings"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade4.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 4 World Literature lessons (completing 30/30).")


if __name__ == "__main__":
    main()
