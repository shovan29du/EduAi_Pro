#!/usr/bin/env python3
"""Depth pass, Grade 2 World History: fill in real, hand-checked
data_table content for the 18 Grade 2 World History lessons not covered
by the earlier breadth-first batch. Brings Grade 2 World History to full
20/20 coverage.

Every fact is real (Indus Valley cities, real writing system origins,
Mansa Musa, Machu Picchu) -- nothing fabricated or presented as fact when
it's actually invented.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade2_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g2-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Civilization", "An organized society with cities, government, and writing"],
            ["Examples", "Ancient Egypt, Mesopotamia, China, Indus Valley"],
        ]),
    },
    "hist-g2-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Silk Road", "An ancient network of trade routes linking China and Europe"],
            ["Goods traded", "Silk, spices, precious stones"],
        ]),
    },
    "world-history-g2-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Great Pyramid of Giza built for", "Pharaoh Khufu"],
            ["Approximate build date", "c. 2560 BCE"], ["Location", "Giza, Egypt"],
        ]),
    },
    "world-history-g2-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"],
            ["Known as", "The 'Cradle of Civilization'"],
        ]),
    },
    "world-history-g2-l5": {
        "data_table": table(["Invention", "Origin"], [
            ["Paper", "Ancient China, c. 2nd century BCE"], ["Compass", "Ancient China"], ["Silk", "Ancient China"],
        ]),
    },
    "world-history-g2-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["First recorded Olympic Games", "776 BCE"], ["Location", "Olympia, Greece"],
            ["Held in honor of", "The god Zeus"],
        ]),
    },
    "world-history-g2-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome traditionally founded", "753 BCE"],
            ["Roman Empire declared by", "Augustus, 27 BCE"],
            ["Fall of the Western Roman Empire", "476 CE"],
        ]),
    },
    "world-history-g2-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"],
            ["Location", "Along the Indus River, in modern Pakistan/India"],
        ]),
    },
    "world-history-g2-l9": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
            ["Marco Polo", "Travels along the Silk Road to China"],
        ]),
    },
    "world-history-g2-l10": {
        "data_table": table(["Stone Age Period", "Key Feature"], [
            ["Old Stone Age (Paleolithic)", "Hunting and gathering, stone tools"],
            ["New Stone Age (Neolithic)", "Farming and permanent settlements"],
        ]),
    },
    "world-history-g2-l11": {
        "data_table": table(["Writing System", "Origin"], [
            ["Cuneiform", "Ancient Sumer (Mesopotamia)"], ["Hieroglyphics", "Ancient Egypt"],
        ]),
    },
    "world-history-g2-l12": {
        "data_table": table(["Trade Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices, precious stones"], ["Trans-Saharan trade", "Gold, salt"],
        ]),
    },
    "world-history-g2-l13": {
        "data_table": table(["Leader", "Known For"], [
            ["Julius Caesar", "Roman general and statesman"],
            ["Cleopatra", "Last active pharaoh of Egypt"],
        ]),
    },
    "world-history-g2-l14": {
        "data_table": table(["Castle Feature", "Purpose"], [
            ["Moat", "A ditch of water for defense"],
            ["Drawbridge", "A bridge that could be raised to block entry"],
        ]),
    },
    "world-history-g2-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Central America (Mexico, Guatemala, Belize)"],
            ["Known for", "Pyramids, a complex calendar, and writing system"],
        ]),
    },
    "world-history-g2-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "South America (Andes Mountains, Peru)"], ["Famous site", "Machu Picchu"],
        ]),
    },
    "world-history-g2-l17": {
        "data_table": table(["Timekeeping Tool", "How It Works"], [
            ["Sundial", "Uses the sun's shadow"], ["Hourglass", "Sand falling between two chambers"],
        ]),
    },
    "world-history-g2-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["The Agricultural Revolution began", "About 10,000-12,000 years ago"],
            ["Effect", "People settled in one place instead of moving to find food"],
        ]),
    },
    "world-history-g2-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Famous ruler", "Mansa Musa"], ["Known for", "Wealth from gold and salt trade"],
        ]),
    },
    "world-history-g2-l20": {
        "data_table": table(["Evidence Type", "Example"], [
            ["Artifact", "A tool or pottery made by people"], ["Fossil", "Preserved remains of ancient life"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade2.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 2 World History lessons (completing 20/20).")


if __name__ == "__main__":
    main()
