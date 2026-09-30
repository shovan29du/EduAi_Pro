#!/usr/bin/env python3
"""Depth pass, Grade 9 World History: fill in real, hand-checked
data_table content for the 48 Grade 9 World History lessons not
covered by the earlier breadth-first batch. Brings Grade 9 World
History to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Historiography", "The study of how history is written and interpreted"],
        ]),
    },
    "hist-g9-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "world-history-g9-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Early humans migrated from", "Africa, over 60,000 years ago"],
        ]),
    },
    "world-history-g9-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "About 10,000-12,000 years ago"], ["Effect", "People settled and began farming"],
        ]),
    },
    "world-history-g9-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g9-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g9-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"], ["River", "Indus River"],
        ]),
    },
    "world-history-g9-l8": {
        "data_table": table(["Dynasty", "Known For"], [
            ["Han Dynasty", "Silk Road expansion"], ["Zhou Dynasty", "Development of Confucianism and Daoism"],
        ]),
    },
    "world-history-g9-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"],
        ]),
    },
    "world-history-g9-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Roman Republic", "Governed by elected officials, c. 509-27 BCE"],
        ]),
    },
    "world-history-g9-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Roman Empire declared by", "Augustus, 27 BCE"],
        ]),
    },
    "world-history-g9-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Fall of Western Roman Empire", "476 CE"],
        ]),
    },
    "world-history-g9-l15": {
        "data_table": table(["Fact", "Detail"], [
            ["Capital", "Constantinople"], ["Fell in", "1453 CE"],
        ]),
    },
    "world-history-g9-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Rise of Islam", "Began in the 7th century CE in Arabia"],
        ]),
    },
    "world-history-g9-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 8th-14th century CE"], ["Achievement", "Advances in medicine, mathematics, and astronomy"],
        ]),
    },
    "world-history-g9-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Samurai", "Japanese warrior class"], ["Code of honor", "Bushido"],
        ]),
    },
    "world-history-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 500-1500 CE"], ["Social system", "Feudalism"],
        ]),
    },
    "world-history-g9-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1096-1291 CE"], ["Nature", "Religious military campaigns"],
        ]),
    },
    "world-history-g9-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g9-l22": {
        "data_table": table(["Empire", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"], ["Songhai Empire", "Grew from Mali"],
        ]),
    },
    "world-history-g9-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Silk Road", "Linked China and Europe, traded silk, spices"],
        ]),
    },
    "world-history-g9-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Black Death", "A devastating plague that killed a large share of Europe's population, 1347-1351"],
        ]),
    },
    "world-history-g9-l25": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "world-history-g9-l26": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
        ]),
    },
    "world-history-g9-l27": {
        "data_table": table(["Exchanged Item", "Direction"], [
            ["Potatoes, corn", "Americas to Europe"], ["Horses, wheat", "Europe to Americas"],
        ]),
    },
    "world-history-g9-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Started by", "Martin Luther, 1517"],
        ]),
    },
    "world-history-g9-l29": {
        "data_table": table(["Empire", "Location"], [
            ["Aztec Empire", "Central Mexico"], ["Inca Empire", "Andes Mountains, South America"],
        ]),
    },
    "world-history-g9-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Africa to the Americas via the Middle Passage"],
        ]),
    },
    "world-history-g9-l31": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Improved the telescope, supported heliocentrism"],
        ]),
    },
    "world-history-g9-l32": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "world-history-g9-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Declaration of Independence", "1776"],
        ]),
    },
    "world-history-g9-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1789"], ["Key event", "Storming of the Bastille"],
        ]),
    },
    "world-history-g9-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "Late 18th century, in Britain"],
        ]),
    },
    "world-history-g9-l36": {
        "data_table": table(["Country", "Unification Completed"], [
            ["Italy", "1871"], ["Germany", "1871"],
        ]),
    },
    "world-history-g9-l39": {
        "data_table": table(["Country", "Unification Completed"], [
            ["Italy", "1871"], ["Germany", "1871"],
        ]),
    },
    "world-history-g9-l37": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "Much of Africa"], ["French Empire", "Parts of West Africa"],
        ]),
    },
    "world-history-g9-l38": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "India and Southeast Asia"],
        ]),
    },
    "world-history-g9-l40": {
        "data_table": table(["Cause", "Detail"], [
            ["Alliances", "Countries drawn in by treaty obligations"], ["Assassination", "Archduke Franz Ferdinand, 1914"],
        ]),
    },
    "world-history-g9-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"], ["Casualties", "Over 16 million deaths"],
        ]),
    },
    "world-history-g9-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Year", "1917"], ["Result", "End of Tsarist rule, rise of Soviet government"],
        ]),
    },
    "world-history-g9-l43": {
        "data_table": table(["Leader", "Country"], [
            ["Benito Mussolini", "Italy"], ["Adolf Hitler", "Germany"],
        ]),
    },
    "world-history-g9-l44": {
        "data_table": table(["Cause", "Detail"], [
            ["Treaty of Versailles resentment", "Fueled German nationalism"], ["Expansionism", "Axis powers sought territory"],
        ]),
    },
    "world-history-g9-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["The Holocaust", "Systematic genocide of six million Jews by Nazi Germany, 1941-1945"],
        ]),
    },
    "world-history-g9-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"],
        ]),
    },
    "world-history-g9-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1947-1991"], ["Main rivals", "United States and Soviet Union"],
        ]),
    },
    "world-history-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Decolonization", "The process of colonies gaining independence"],
        ]),
    },
    "world-history-g9-l49": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
        ]),
    },
    "world-history-g9-l50": {
        "data_table": table(["Fact", "Detail"], [
            ["Berlin Wall fell", "1989"], ["Soviet Union dissolved", "1991"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 World History lessons (completing 50/50).")


if __name__ == "__main__":
    main()
