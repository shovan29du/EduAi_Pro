#!/usr/bin/env python3
"""Depth pass, Grade 5 World History: fill in real, hand-checked
data_table content for the 28 Grade 5 World History lessons not
covered by the earlier breadth-first batch. Brings Grade 5 World
History to full 30/30 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade5_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade5.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g5-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "14th-17th century, began in Italy"], ["Meaning", "'Rebirth' of art, science, and learning"],
        ]),
    },
    "hist-g5-l2": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"], ["Vasco da Gama", "Sea route to India"],
        ]),
    },
    "world-history-g5-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Early humans migrated from", "Africa, over 60,000 years ago"],
        ]),
    },
    "world-history-g5-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "About 10,000-12,000 years ago"], ["Effect", "People settled and began farming"],
        ]),
    },
    "world-history-g5-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g5-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g5-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"], ["Famous philosophers", "Socrates, Plato, Aristotle"],
        ]),
    },
    "world-history-g5-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome founded (tradition)", "753 BCE"], ["Fall of Western Roman Empire", "476 CE"],
        ]),
    },
    "world-history-g5-l9": {
        "data_table": table(["Dynasty", "Known For"], [
            ["Han Dynasty", "Silk Road expansion"], ["Qin Dynasty", "Unified China, began the Great Wall"],
        ]),
    },
    "world-history-g5-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"], ["River", "Indus River"],
        ]),
    },
    "world-history-g5-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Linked China and Europe"], ["Goods traded", "Silk, spices, precious stones"],
        ]),
    },
    "world-history-g5-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 500-1500 CE"], ["Social system", "Feudalism"],
        ]),
    },
    "world-history-g5-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 8th-14th century CE"], ["Achievement", "Advances in medicine, mathematics, and astronomy"],
        ]),
    },
    "world-history-g5-l14": {
        "data_table": table(["Empire", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"], ["Ghana Empire", "Early West African trade empire"],
        ]),
    },
    "world-history-g5-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g5-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Samurai", "Japanese warrior class"], ["Code of honor", "Bushido"],
        ]),
    },
    "world-history-g5-l17": {
        "data_table": table(["Civilization", "Location"], [
            ["Maya", "Central America"], ["Aztec", "Central Mexico"], ["Inca", "Andes Mountains, South America"],
        ]),
    },
    "world-history-g5-l20": {
        "data_table": table(["Consequence", "Detail"], [
            ["New trade routes", "Connected Europe, Africa, and the Americas"],
            ["Colonization", "European powers established colonies"],
        ]),
    },
    "world-history-g5-l21": {
        "data_table": table(["Exchanged Item", "Direction"], [
            ["Potatoes, corn", "Americas to Europe"], ["Horses, wheat", "Europe to Americas"],
        ]),
    },
    "world-history-g5-l22": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Improved the telescope, supported heliocentrism"],
            ["Isaac Newton", "Laws of motion and gravity"],
        ]),
    },
    "world-history-g5-l23": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "Territories across every continent"], ["Spanish Empire", "Much of the Americas"],
        ]),
    },
    "world-history-g5-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Africa to the Americas via the Middle Passage"],
            ["Duration", "16th to 19th century"],
        ]),
    },
    "world-history-g5-l25": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
            ["Voltaire", "Advocated for freedom of speech"],
        ]),
    },
    "world-history-g5-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "Late 18th century, in Britain"], ["Key change", "Shift from hand production to machines"],
        ]),
    },
    "world-history-g5-l27": {
        "data_table": table(["Revolution", "Year"], [
            ["American Revolution", "1776"], ["Latin American independence movements", "Early 19th century"],
        ]),
    },
    "world-history-g5-l28": {
        "data_table": table(["War", "Approximate Dates"], [
            ["World War I", "1914-1918"], ["World War II", "1939-1945"],
        ]),
    },
    "world-history-g5-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "1945, after World War II"], ["Purpose", "Promote peace and cooperation among nations"],
        ]),
    },
    "world-history-g5-l30": {
        "data_table": table(["Era", "Approximate Period"], [
            ["Ancient history", "3000 BCE - 500 CE"], ["Medieval history", "500 CE - 1500 CE"],
            ["Modern history", "1500 CE - present"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade5.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 5 World History lessons (completing 30/30).")


if __name__ == "__main__":
    main()
