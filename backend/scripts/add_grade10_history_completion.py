#!/usr/bin/env python3
"""Depth pass, Grade 10 World History: fill in real, hand-checked
data_table content for the Grade 10 World History lessons not covered
by the earlier breadth-first batch. Brings Grade 10 World History to
full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "hist-g10-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Soviet Union dissolved", "1991"], ["Post-1991 era", "Marked by globalization and US-led unipolarity"],
        ]),
    },
    "world-history-g10-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g10-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Notable achievement", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g10-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"], ["Notable philosophers", "Socrates, Plato, Aristotle"],
        ]),
    },
    "world-history-g10-l6": {
        "data_table": table(["Period", "Approximate Dates"], [
            ["Roman Republic", "509-27 BCE"], ["Roman Empire", "27 BCE-476 CE (west)"],
        ]),
    },
    "world-history-g10-l7": {
        "data_table": table(["Dynasty", "Known For"], [
            ["Han Dynasty", "Silk Road expansion"], ["Zhou Dynasty", "Confucianism and Daoism"],
        ]),
    },
    "world-history-g10-l8": {
        "data_table": table(["Empire", "Notable Ruler"], [
            ["Mauryan Empire", "Ashoka the Great"], ["Gupta Empire", "Golden age of Indian culture and science"],
        ]),
    },
    "world-history-g10-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Rise of Islam", "7th century CE, Arabia"], ["Rightly Guided Caliphs", "First four successors to Prophet Muhammad"],
        ]),
    },
    "world-history-g10-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Capital", "Constantinople"], ["Fell in", "1453 CE, to the Ottomans"],
        ]),
    },
    "world-history-g10-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Feudalism", "A hierarchical system of land and loyalty exchange"],
        ]),
    },
    "world-history-g10-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Crusades", "Religious military campaigns, 1096-1291 CE"],
        ]),
    },
    "world-history-g10-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g10-l14": {
        "data_table": table(["Empire", "Notable Ruler"], [
            ["Mali Empire", "Mansa Musa, known for immense wealth"],
        ]),
    },
    "world-history-g10-l15": {
        "data_table": table(["Route", "Goods Traded"], [
            ["Silk Road", "Silk, spices, and ideas between China and Europe"], ["Trans-Saharan trade", "Gold and salt across the Sahara"],
        ]),
    },
    "world-history-g10-l16": {
        "data_table": table(["Civilization", "Region"], [
            ["Maya", "Mesoamerica"], ["Inca", "Andes Mountains"],
        ]),
    },
    "world-history-g10-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Renaissance began", "14th century, Italy"], ["Notable figures", "Leonardo da Vinci, Michelangelo"],
        ]),
    },
    "world-history-g10-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Started by", "Martin Luther, 1517"],
        ]),
    },
    "world-history-g10-l19": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"], ["Vasco da Gama", "Sea route to India"],
        ]),
    },
    "world-history-g10-l21": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Supported heliocentrism"], ["Isaac Newton", "Laws of motion and gravity"],
        ]),
    },
    "world-history-g10-l22": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights"], ["Voltaire", "Freedom of speech and religious tolerance"],
        ]),
    },
    "world-history-g10-l23": {
        "data_table": table(["Fact", "Detail"], [
            ["Ottoman Empire", "1299-1922, centered in Anatolia"],
        ]),
    },
    "world-history-g10-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Mughal Empire", "Ruled much of the Indian subcontinent, 1526-1857"],
        ]),
    },
    "world-history-g10-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["English Civil War", "1642-1651, between Parliament and the monarchy"],
        ]),
    },
    "world-history-g10-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Declaration of Independence", "1776"],
        ]),
    },
    "world-history-g10-l27": {
        "data_table": table(["Fact", "Detail"], [
            ["French Revolution began", "1789"], ["Key event", "Storming of the Bastille"],
        ]),
    },
    "world-history-g10-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Napoleon Bonaparte", "French emperor, defeated at Waterloo in 1815"],
        ]),
    },
    "world-history-g10-l29": {
        "data_table": table(["Fact", "Detail"], [
            ["Industrial Revolution began", "Late 18th century, in Britain"],
        ]),
    },
    "world-history-g10-l30": {
        "data_table": table(["Country", "Unification Completed"], [
            ["Italy", "1871"], ["Germany", "1871"],
        ]),
    },
    "world-history-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Scramble for Africa", "European colonization of most of Africa in the late 19th century"],
        ]),
    },
    "world-history-g10-l32": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "India and Southeast Asia"],
        ]),
    },
    "world-history-g10-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Meiji Restoration", "1868, rapid modernization of Japan"],
        ]),
    },
    "world-history-g10-l34": {
        "data_table": table(["Cause", "Detail"], [
            ["Alliances", "Drew countries into the conflict"], ["Assassination", "Archduke Franz Ferdinand, 1914"],
        ]),
    },
    "world-history-g10-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"], ["Casualties", "Over 16 million deaths"],
        ]),
    },
    "world-history-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Year", "1917"], ["Result", "End of Tsarist rule, rise of the Soviet government"],
        ]),
    },
    "world-history-g10-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1929, with the Wall Street Crash"],
        ]),
    },
    "world-history-g10-l38": {
        "data_table": table(["Leader", "Country"], [
            ["Benito Mussolini", "Italy"], ["Adolf Hitler", "Germany"],
        ]),
    },
    "world-history-g10-l39": {
        "data_table": table(["Cause", "Detail"], [
            ["Treaty of Versailles resentment", "Fueled German nationalism"], ["Expansionism", "Axis powers sought territory"],
        ]),
    },
    "world-history-g10-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["The Holocaust", "Systematic genocide of six million Jews by Nazi Germany, 1941-1945"],
        ]),
    },
    "world-history-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1939-1945"], ["Ended", "1945"],
        ]),
    },
    "world-history-g10-l42": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1947-1991"], ["Main rivals", "United States and Soviet Union"],
        ]),
    },
    "world-history-g10-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["Decolonization", "Most African and Asian colonies gained independence in the mid-20th century"],
        ]),
    },
    "world-history-g10-l44": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
        ]),
    },
    "world-history-g10-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Cuban Missile Crisis", "1962, near-nuclear confrontation between the US and USSR"],
        ]),
    },
    "world-history-g10-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Vietnam War", "1955-1975, conflict between North and South Vietnam"],
        ]),
    },
    "world-history-g10-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["Berlin Wall fell", "1989"], ["Soviet Union dissolved", "1991"],
        ]),
    },
    "world-history-g10-l48": {
        "data_table": table(["Fact", "Detail"], [
            ["People's Republic of China founded", "1949, led by Mao Zedong"],
        ]),
    },
    "world-history-g10-l49": {
        "data_table": table(["Fact", "Detail"], [
            ["Apartheid ended", "1994, with Nelson Mandela's election"],
        ]),
    },
    "world-history-g10-l50": {
        "data_table": table(["Fact", "Detail"], [
            ["Partition of India", "1947, creating India and Pakistan"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 World History lessons (completing 50/50).")


if __name__ == "__main__":
    main()
