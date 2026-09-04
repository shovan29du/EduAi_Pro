#!/usr/bin/env python3
"""Depth pass, Grade 1 World History: fill in real, hand-checked
data_table content for the 17 Grade 1 World History lessons not covered
by the earlier breadth-first batch. Brings Grade 1 World History to full
20/20 coverage.

Every fact is real (Lascaux/Altamira cave paintings, real ancient Chinese
inventions, real explorers, real historical leaders) -- nothing
fabricated or presented as fact when it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade1_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g1-l1": {
        "data_table": table(["Family Term", "Meaning"], [
            ["Ancestor", "A family member who lived before you"],
            ["Generation", "A group of family members around the same age (e.g. grandparents, parents, children)"],
        ]),
    },
    "world-history-g1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["History", "The study of things that happened in the past"],
            ["Historian", "A person who studies history"],
        ]),
    },
    "world-history-g1-l3": {
        "data_table": table(["Then", "Now"], [
            ["Hunting and gathering food", "Buying food at a store"],
            ["Walking or riding animals", "Cars, buses, trains"],
        ]),
    },
    "world-history-g1-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Famous cave paintings found at", "Lascaux, France and Altamira, Spain"],
            ["Approximate age", "Tens of thousands of years old"],
        ]),
    },
    "world-history-g1-l6": {
        "data_table": table(["Invention", "Origin"], [
            ["Paper", "Ancient China, c. 2nd century BCE"],
            ["Compass", "Ancient China"], ["Silk", "Ancient China"],
        ]),
    },
    "world-history-g1-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Famous saying", "'All roads lead to Rome'"],
            ["Purpose of Roman roads", "Moving armies, trade, and messages quickly"],
        ]),
    },
    "world-history-g1-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["The Agricultural Revolution began", "About 10,000-12,000 years ago"],
            ["Effect", "People settled in one place instead of moving to find food"],
        ]),
    },
    "world-history-g1-l10": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
            ["Marco Polo", "Travels along the Silk Road to China"],
        ]),
    },
    "world-history-g1-l11": {
        "data_table": table(["Home Type", "Time Period"], [
            ["Cave", "Prehistoric times"], ["Mud brick house", "Ancient civilizations (e.g. Mesopotamia)"],
            ["Modern house", "Today"],
        ]),
    },
    "world-history-g1-l12": {
        "data_table": table(["Material", "Used In"], [
            ["Animal skins", "Prehistoric times"], ["Wool and linen", "Ancient civilizations"],
            ["Cotton and synthetic fabrics", "Today"],
        ]),
    },
    "world-history-g1-l13": {
        "data_table": table(["Toy", "Time Period"], [
            ["Hoop and stick", "Ancient Egypt and Greece"], ["Marbles", "Ancient Rome and beyond"],
            ["Video games", "Modern times"],
        ]),
    },
    "world-history-g1-l14": {
        "data_table": table(["Then", "Now"], [
            ["Walking or horse", "Car"], ["Sailing ship", "Airplane"],
        ]),
    },
    "world-history-g1-l15": {
        "data_table": table(["Then", "Now"], [
            ["Messenger on foot/horse", "Phone call"], ["Letters by mail", "Text messages and email"],
        ]),
    },
    "world-history-g1-l16": {
        "data_table": table(["Invention", "Impact"], [
            ["The wheel", "Made transportation and work easier"],
            ["The printing press", "Made books widely available"],
        ]),
    },
    "world-history-g1-l17": {
        "data_table": table(["Castle Feature", "Purpose"], [
            ["Moat", "A ditch of water for defense"],
            ["Drawbridge", "A bridge that could be raised to block entry"],
        ]),
    },
    "world-history-g1-l18": {
        "data_table": table(["Leader", "Known For"], [
            ["Nelson Mandela", "Promoting peace and equality in South Africa"],
            ["Mahatma Gandhi", "Leading peaceful protest in India"],
        ]),
    },
    "world-history-g1-l19": {
        "data_table": table(["Celebration", "Tradition"], [
            ["New Year", "Celebrating the start of a new year"],
            ["Harvest festivals", "Celebrating a successful harvest"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade1.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 1 World History lessons (completing 20/20).")


if __name__ == "__main__":
    main()
