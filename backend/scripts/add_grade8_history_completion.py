#!/usr/bin/env python3
"""Depth pass, Grade 8 World History: fill in real, hand-checked
data_table content for the 38 Grade 8 World History lessons not
covered by the earlier breadth-first batch. Brings Grade 8 World
History to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalisation", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "world-history-g8-l3": {
        "data_table": table(["Civilization", "Location"], [
            ["Mesopotamia", "Between the Tigris and Euphrates rivers"], ["Ancient Egypt", "Along the Nile River"],
        ]),
    },
    "world-history-g8-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g8-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g8-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"],
        ]),
    },
    "world-history-g8-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome founded (tradition)", "753 BCE"], ["Fall of Western Roman Empire", "476 CE"],
        ]),
    },
    "world-history-g8-l8": {
        "data_table": table(["Dynasty", "Known For"], [
            ["Han Dynasty", "Silk Road expansion"],
        ]),
    },
    "world-history-g8-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Major cities", "Mohenjo-daro and Harappa"], ["Mauryan Empire founder", "Chandragupta Maurya"],
        ]),
    },
    "world-history-g8-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 8th-14th century CE"], ["Achievement", "Advances in medicine, mathematics, and astronomy"],
        ]),
    },
    "world-history-g8-l11": {
        "data_table": table(["Fact", "Detail"], [
            ["Capital", "Constantinople"], ["Fell in", "1453 CE"],
        ]),
    },
    "world-history-g8-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 500-1500 CE"], ["Social system", "Feudalism"],
        ]),
    },
    "world-history-g8-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1096-1291 CE"], ["Nature", "Religious military campaigns"],
        ]),
    },
    "world-history-g8-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g8-l15": {
        "data_table": table(["Empire", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"],
        ]),
    },
    "world-history-g8-l16": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "world-history-g8-l17": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
        ]),
    },
    "world-history-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Started by", "Martin Luther, 1517"],
        ]),
    },
    "world-history-g8-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Founder", "Babur"], ["Famous structure", "Taj Mahal, built under Shah Jahan"],
        ]),
    },
    "world-history-g8-l21": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Improved the telescope, supported heliocentrism"],
        ]),
    },
    "world-history-g8-l22": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "world-history-g8-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Route", "Africa to the Americas via the Middle Passage"], ["Duration", "16th to 19th century"],
        ]),
    },
    "world-history-g8-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Declaration of Independence", "1776"],
        ]),
    },
    "world-history-g8-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1789"], ["Key event", "Storming of the Bastille"],
        ]),
    },
    "world-history-g8-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "Late 18th century, in Britain"],
        ]),
    },
    "world-history-g8-l27": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "Territories across every continent"],
        ]),
    },
    "world-history-g8-l28": {
        "data_table": table(["Country", "Unification Completed"], [
            ["Italy", "1871"], ["Germany", "1871"],
        ]),
    },
    "world-history-g8-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"], ["Trigger", "Assassination of Archduke Franz Ferdinand"],
        ]),
    },
    "world-history-g8-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["Year", "1917"], ["Result", "End of Tsarist rule, rise of Soviet government"],
        ]),
    },
    "world-history-g8-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1929, with the US stock market crash"],
        ]),
    },
    "world-history-g8-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"],
        ]),
    },
    "world-history-g8-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["The Holocaust", "Systematic genocide of six million Jews by Nazi Germany, 1941-1945"],
        ]),
    },
    "world-history-g8-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1947-1991"], ["Main rivals", "United States and Soviet Union"],
        ]),
    },
    "world-history-g8-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "1945, after World War II"],
        ]),
    },
    "world-history-g8-l36": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
        ]),
    },
    "world-history-g8-l37": {
        "data_table": table(["Milestone", "Year"], [
            ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "world-history-g8-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Marshall Plan", "US aid program to rebuild Western Europe after WWII, 1948"],
        ]),
    },
    "world-history-g8-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Berlin Wall fell", "1989"],
        ]),
    },
    "world-history-g8-l40": {
        "data_table": table(["Concept", "Meaning"], [
            ["Peacebuilding", "Efforts to establish lasting peace after conflict"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 World History lessons (completing 40/40).")


if __name__ == "__main__":
    main()
