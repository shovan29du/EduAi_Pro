#!/usr/bin/env python3
"""Depth pass, Grade 7 World History: fill in real, hand-checked
data_table content for the 38 Grade 7 World History lessons not
covered by the earlier breadth-first batch. Brings Grade 7 World
History to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade7_history_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade7.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-history-g7-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Location", "Between the Tigris and Euphrates rivers"], ["Writing system", "Cuneiform"],
        ]),
    },
    "world-history-g7-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["River", "The Nile"], ["Famous structure", "The Great Pyramid of Giza"],
        ]),
    },
    "world-history-g7-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Democracy began in", "Athens, c. 508 BCE"], ["Famous philosophers", "Socrates, Plato, Aristotle"],
        ]),
    },
    "world-history-g7-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Rome founded (tradition)", "753 BCE"], ["Fall of Western Roman Empire", "476 CE"],
        ]),
    },
    "world-history-g7-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Capital", "Constantinople"], ["Fell in", "1453 CE"],
        ]),
    },
    "world-history-g7-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 8th-14th century CE"], ["Achievement", "Advances in medicine, mathematics, and astronomy"],
        ]),
    },
    "world-history-g7-l9": {
        "data_table": table(["Fact", "Detail"], [
            ["Period", "c. 500-1500 CE"], ["Social system", "Feudalism"],
        ]),
    },
    "world-history-g7-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded by", "Genghis Khan"], ["Extent", "Largest contiguous land empire in history"],
        ]),
    },
    "world-history-g7-l11": {
        "data_table": table(["Empire", "Known For"], [
            ["Mali Empire", "Ruler Mansa Musa, wealth from gold"], ["Songhai Empire", "Grew from Mali, controlled Timbuktu"],
        ]),
    },
    "world-history-g7-l12": {
        "data_table": table(["Dynasty", "Known For"], [
            ["Han Dynasty", "Silk Road expansion"], ["Ming Dynasty", "Building much of the Great Wall"],
        ]),
    },
    "world-history-g7-l13": {
        "data_table": table(["Fact", "Detail"], [
            ["Founder", "Babur"], ["Famous structure", "Taj Mahal, built under Shah Jahan"],
        ]),
    },
    "world-history-g7-l14": {
        "data_table": table(["Artist", "Famous Work"], [
            ["Leonardo da Vinci", "Mona Lisa"], ["Michelangelo", "Sistine Chapel ceiling"],
        ]),
    },
    "world-history-g7-l15": {
        "data_table": table(["Explorer", "Known For"], [
            ["Christopher Columbus", "Voyages to the Americas, 1492"], ["Vasco da Gama", "Sea route to India"],
        ]),
    },
    "world-history-g7-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Started by", "Martin Luther, 1517"], ["Effect", "Split within Western Christianity"],
        ]),
    },
    "world-history-g7-l17": {
        "data_table": table(["Scientist", "Contribution"], [
            ["Galileo Galilei", "Improved the telescope, supported heliocentrism"],
            ["Isaac Newton", "Laws of motion and gravity"],
        ]),
    },
    "world-history-g7-l18": {
        "data_table": table(["Thinker", "Idea"], [
            ["John Locke", "Natural rights to life, liberty, and property"],
            ["Voltaire", "Advocated for freedom of speech"],
        ]),
    },
    "world-history-g7-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["Declaration of Independence", "1776"], ["Founding document", "US Constitution, 1787"],
        ]),
    },
    "world-history-g7-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "1789"], ["Key event", "Storming of the Bastille"],
        ]),
    },
    "world-history-g7-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Began", "Late 18th century, in Britain"], ["Key change", "Shift from hand production to machines"],
        ]),
    },
    "world-history-g7-l22": {
        "data_table": table(["Empire", "Region Controlled"], [
            ["British Empire", "Territories across every continent"], ["Spanish Empire", "Much of the Americas"],
        ]),
    },
    "world-history-g7-l23": {
        "data_table": table(["Country", "Unification Completed"], [
            ["Italy", "1871"], ["Germany", "1871"],
        ]),
    },
    "world-history-g7-l24": {
        "data_table": table(["Fact", "Detail"], [
            ["Dates", "1914-1918"], ["Trigger", "Assassination of Archduke Franz Ferdinand"],
        ]),
    },
    "world-history-g7-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Year", "1917"], ["Result", "End of Tsarist rule, rise of Soviet government"],
        ]),
    },
    "world-history-g7-l26": {
        "data_table": table(["Leader", "Country"], [
            ["Benito Mussolini", "Italy"], ["Adolf Hitler", "Germany"],
        ]),
    },
    "world-history-g7-l27": {
        "data_table": table(["Country", "Independence Achieved"], [
            ["Mexico", "1821"], ["Brazil", "1822"],
        ]),
    },
    "world-history-g7-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Founded", "1945, after World War II"], ["Purpose", "Promote peace and cooperation among nations"],
        ]),
    },
    "world-history-g7-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Decolonization", "The process of colonies gaining independence"],
        ]),
    },
    "world-history-g7-l30": {
        "data_table": table(["Figure", "Known For"], [
            ["Martin Luther King Jr.", "Leader in the American civil rights movement"],
            ["Rosa Parks", "Sparked the Montgomery bus boycott"],
        ]),
    },
    "world-history-g7-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Apartheid", "A system of racial segregation in South Africa, 1948-1994"],
            ["Ended by", "Nelson Mandela's leadership and negotiated reform"],
        ]),
    },
    "world-history-g7-l32": {
        "data_table": table(["Milestone", "Year"], [
            ["First human in space (Yuri Gagarin)", "1961"], ["First Moon landing (Apollo 11)", "1969"],
        ]),
    },
    "world-history-g7-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Berlin Wall fell", "1989"], ["Significance", "Symbolized the end of the Cold War divide"],
        ]),
    },
    "world-history-g7-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Soviet Union dissolved", "1991"], ["Result", "Formation of independent states, including Russia"],
        ]),
    },
    "world-history-g7-l35": {
        "data_table": table(["Country", "Postwar Development"], [
            ["Japan", "Rapid economic recovery and growth"], ["Germany", "Rebuilt and later reunified in 1990"],
        ]),
    },
    "world-history-g7-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Universal Declaration of Human Rights", "Adopted by the UN in 1948"],
        ]),
    },
    "world-history-g7-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "world-history-g7-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Non-Aligned Movement", "Countries choosing not to formally align with either major Cold War bloc"],
        ]),
    },
    "world-history-g7-l39": {
        "data_table": table(["Invention", "Impact"], [
            ["The telephone", "Enabled instant long-distance communication"], ["The internet", "Connected the world digitally"],
        ]),
    },
    "world-history-g7-l40": {
        "data_table": table(["Turning Point", "Approximate Year"], [
            ["End of World War II", "1945"], ["Fall of the Berlin Wall", "1989"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World History"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade7.json World History: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 7 World History lessons (completing 40/40).")


if __name__ == "__main__":
    main()
