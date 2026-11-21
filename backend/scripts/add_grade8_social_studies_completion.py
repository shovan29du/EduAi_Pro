#!/usr/bin/env python3
"""Depth pass, Grade 8 Social Studies: fill in real, hand-checked
data_table content for the 38 Grade 8 Social Studies lessons not
covered by the earlier breadth-first batch. Brings Grade 8 Social
Studies to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "ss-g8-l1": {
        "data_table": table(["System", "Description"], [
            ["Market economy", "Prices set by supply and demand"], ["Command economy", "Government controls production"],
        ]),
    },
    "social-studies-g8-l2": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "social-studies-g8-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "social-studies-g8-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"],
        ]),
    },
    "social-studies-g8-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome founded (tradition)", "753 BCE"], ["Fall of Western Roman Empire", "476 CE"],
        ]),
    },
    "social-studies-g8-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Silk Road", "Linked China and Europe, traded silk, spices"],
        ]),
    },
    "social-studies-g8-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Feudalism", "A social system based on land in exchange for service"],
        ]),
    },
    "social-studies-g8-l8": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"],
        ]),
    },
    "social-studies-g8-l9": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"],
        ]),
    },
    "social-studies-g8-l10": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Improved the telescope, supported heliocentrism"],
        ]),
    },
    "social-studies-g8-l11": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
        ]),
    },
    "social-studies-g8-l12": {
        "data_table": table(["Fact", "Detail"], [
            ["Declaration of Independence", "1776"],
        ]),
    },
    "social-studies-g8-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1789"], ["Key event", "Storming of the Bastille"],
        ]),
    },
    "social-studies-g8-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "Late 18th century, in Britain"],
        ]),
    },
    "social-studies-g8-l15": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "Territories across every continent"],
        ]),
    },
    "social-studies-g8-l18": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "1947-1991"], ["Main rivals", "United States and Soviet Union"],
        ]),
    },
    "social-studies-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Decolonization", "The process of colonies gaining independence"],
        ]),
    },
    "social-studies-g8-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "1945, after World War II"],
        ]),
    },
    "social-studies-g8-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "social-studies-g8-l22": {
        "data_table": table(["Branch", "Role"], [
            ["Legislative", "Makes laws"], ["Executive", "Enforces laws"], ["Judicial", "Interprets laws"],
        ]),
    },
    "social-studies-g8-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Constitution", "A document establishing a country's fundamental laws"],
        ]),
    },
    "social-studies-g8-l24": {
        "data_table": table(["Government Type", "Description"], [
            ["Democracy", "Citizens vote for leaders"], ["Monarchy", "Rule by a king or queen"],
        ]),
    },
    "social-studies-g8-l25": {
        "data_table": table(["Concept", "Example"], [
            ["Citizenship", "Legal membership in a country"], ["Civic responsibility", "Voting, following laws"],
        ]),
    },
    "social-studies-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Vote", "Choosing a leader or decision by ballot"],
        ]),
    },
    "social-studies-g8-l27": {
        "data_table": table(["Level", "Example Responsibility"], [
            ["Local", "City services like trash collection"], ["National", "Defense and foreign policy"],
        ]),
    },
    "social-studies-g8-l28": {
        "data_table": table(["Continent", "Ocean"], [
            ["Asia", "Pacific Ocean"], ["Africa", "Indian Ocean"],
        ]),
    },
    "social-studies-g8-l29": {
        "data_table": table(["Landform", "Description"], [
            ["Plateau", "A raised, flat area of land"],
        ]),
    },
    "social-studies-g8-l30": {
        "data_table": table(["Factor", "Example"], [
            ["Push factor", "War or lack of jobs at home"], ["Pull factor", "Better opportunities elsewhere"],
        ]),
    },
    "social-studies-g8-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural diffusion", "The spread of ideas and customs between cultures"],
        ]),
    },
    "social-studies-g8-l32": {
        "data_table": table(["Religion", "Approx. Founded"], [
            ["Hinduism", "Ancient, over 4,000 years ago"], ["Islam", "7th century CE"],
        ]),
    },
    "social-studies-g8-l33": {
        "data_table": table(["Tool", "Use"], [
            ["GPS", "Pinpoints exact location using satellites"],
        ]),
    },
    "social-studies-g8-l34": {
        "data_table": table(["Resource", "Use"], [
            ["Water", "Drinking, farming"], ["Coal", "Energy production"],
        ]),
    },
    "social-studies-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanisation", "Growth of cities as more people move there"],
        ]),
    },
    "social-studies-g8-l36": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
        ]),
    },
    "social-studies-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "social-studies-g8-l38": {
        "data_table": table(["Organization", "Purpose"], [
            ["NATO", "Military alliance among member countries"],
        ]),
    },
    "social-studies-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Media literacy", "The ability to evaluate and understand media messages"],
        ]),
    },
    "social-studies-g8-l40": {
        "data_table": table(["Ideology", "Core Idea"], [
            ["Liberalism", "Emphasizes individual rights and freedoms"], ["Conservatism", "Emphasizes tradition and gradual change"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Social Studies lessons (completing 40/40).")


if __name__ == "__main__":
    main()
