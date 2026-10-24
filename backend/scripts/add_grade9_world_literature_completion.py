#!/usr/bin/env python3
"""Depth pass, Grade 9 World Literature: fill in real, hand-checked
data_table content for the 48 Grade 9 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 9 World
Literature to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Post-colonial literature", "Literature responding to the experience of colonialism and its aftermath"],
        ]),
    },
    "world-literature-g9-l2": {
        "data_table": table(["God/Hero", "Known For"], [
            ["Zeus", "King of the gods"], ["Odysseus", "Hero of The Odyssey"],
        ]),
    },
    "world-literature-g9-l3": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Attributed to Homer"], ["Theme", "Odysseus's journey home after the Trojan War"],
        ]),
    },
    "world-literature-g9-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Structure", "A frame narrative, told by Scheherazade"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g9-l7": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Miguel de Cervantes"], ["Country", "Spain"],
        ]),
    },
    "world-literature-g9-l8": {
        "data_table": table(["Author", "Famous Work"], [
            ["Leo Tolstoy", "War and Peace, Anna Karenina"],
        ]),
    },
    "world-literature-g9-l9": {
        "data_table": table(["Author", "Famous Work"], [
            ["Fyodor Dostoevsky", "Crime and Punishment"],
        ]),
    },
    "world-literature-g9-l10": {
        "data_table": table(["Author", "Famous Work"], [
            ["Franz Kafka", "The Metamorphosis"],
        ]),
    },
    "world-literature-g9-l11": {
        "data_table": table(["Author", "Country"], [
            ["Gabriel Garcia Marquez", "Colombia, known for magical realism"],
        ]),
    },
    "world-literature-g9-l12": {
        "data_table": table(["Author", "Country"], [
            ["Jorge Luis Borges", "Argentina"], ["Isabel Allende", "Chile"],
        ]),
    },
    "world-literature-g9-l13": {
        "data_table": table(["Author", "Region"], [
            ["Chinua Achebe", "Nigeria"],
        ]),
    },
    "world-literature-g9-l14": {
        "data_table": table(["Tradition", "Region"], [
            ["Griot storytelling", "West Africa"],
        ]),
    },
    "world-literature-g9-l15": {
        "data_table": table(["Poet", "Country"], [
            ["Matsuo Basho", "Japan, master of haiku"],
        ]),
    },
    "world-literature-g9-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Murasaki Shikibu"], ["Significance", "Often considered the world's first novel"],
        ]),
    },
    "world-literature-g9-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Journey to the West", "Classic Chinese novel"],
        ]),
    },
    "world-literature-g9-l18": {
        "data_table": table(["Poet", "Fact"], [
            ["Rabindranath Tagore", "First non-European Nobel laureate in Literature, 1913"],
        ]),
    },
    "world-literature-g9-l19": {
        "data_table": table(["Fact", "Detail"], [
            ["The Ramayana", "Ancient Indian epic about Prince Rama"],
        ]),
    },
    "world-literature-g9-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["The Mahabharata", "One of the longest epic poems in world literature"],
        ]),
    },
    "world-literature-g9-l21": {
        "data_table": table(["Author", "Famous Work"], [
            ["Toni Morrison", "Beloved, Nobel laureate in Literature, 1993"],
        ]),
    },
    "world-literature-g9-l22": {
        "data_table": table(["Fact", "Detail"], [
            ["Harlem Renaissance", "African American cultural movement centered in Harlem, 1920s"],
        ]),
    },
    "world-literature-g9-l23": {
        "data_table": table(["Author", "Famous Work"], [
            ["Maya Angelou", "I Know Why the Caged Bird Sings"],
        ]),
    },
    "world-literature-g9-l24": {
        "data_table": table(["Author", "Famous Work"], [
            ["George Orwell", "Animal Farm, 1984"],
        ]),
    },
    "world-literature-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Dystopia", "An imagined society that is undesirable or frightening"],
        ]),
    },
    "world-literature-g9-l26": {
        "data_table": table(["Author", "Famous Work"], [
            ["Virginia Woolf", "Mrs Dalloway"],
        ]),
    },
    "world-literature-g9-l27": {
        "data_table": table(["Author", "Famous Work"], [
            ["James Joyce", "Ulysses"],
        ]),
    },
    "world-literature-g9-l28": {
        "data_table": table(["Author", "Famous Work"], [
            ["Fyodor Dostoevsky", "Crime and Punishment"],
        ]),
    },
    "world-literature-g9-l29": {
        "data_table": table(["Author", "Famous Work"], [
            ["Victor Hugo", "Les Miserables"],
        ]),
    },
    "world-literature-g9-l30": {
        "data_table": table(["Author", "Famous Work"], [
            ["Albert Camus", "The Stranger"],
        ]),
    },
    "world-literature-g9-l31": {
        "data_table": table(["Thinker", "Idea"], [
            ["Jean-Paul Sartre", "Existence precedes essence"],
        ]),
    },
    "world-literature-g9-l32": {
        "data_table": table(["Author", "Known For"], [
            ["Anton Chekhov", "Master of the short story form"],
        ]),
    },
    "world-literature-g9-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Nordic folklore", "Includes trolls, sagas, and Norse mythology"],
        ]),
    },
    "world-literature-g9-l34": {
        "data_table": table(["Author", "Country"], [
            ["Isabel Allende", "Chile"],
        ]),
    },
    "world-literature-g9-l35": {
        "data_table": table(["Author", "Country"], [
            ["Chimamanda Ngozi Adichie", "Nigeria"],
        ]),
    },
    "world-literature-g9-l36": {
        "data_table": table(["Author", "Famous Work"], [
            ["Khaled Hosseini", "The Kite Runner"],
        ]),
    },
    "world-literature-g9-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Holocaust literature", "Written accounts bearing witness to the Holocaust"],
        ]),
    },
    "world-literature-g9-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Anne Frank"], ["Historical context", "Written while hiding during the Holocaust, WWII"],
        ]),
    },
    "world-literature-g9-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["War literature", "Often based on firsthand soldier accounts"],
        ]),
    },
    "world-literature-g9-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short animal stories with morals"],
        ]),
    },
    "world-literature-g9-l41": {
        "data_table": table(["Myth Theme", "Cross-Cultural Example"], [
            ["Great flood", "Found in Mesopotamian, biblical, and other traditions"],
        ]),
    },
    "world-literature-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Graphic novel", "A book-length narrative told through illustrated panels"],
        ]),
    },
    "world-literature-g9-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Translation", "Rendering a text into another language"],
        ]),
    },
    "world-literature-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Diaspora literature", "Writing by authors living outside their ancestral homeland"],
        ]),
    },
    "world-literature-g9-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Indigenous literature", "Includes oral storytelling traditions passed across generations"],
        ]),
    },
    "world-literature-g9-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Middle Eastern literature", "Includes classical poetry and modern novels"],
        ]),
    },
    "world-literature-g9-l47": {
        "data_table": table(["Author", "Region"], [
            ["Derek Walcott", "Saint Lucia, Nobel laureate in Literature, 1992"],
        ]),
    },
    "world-literature-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Protest literature", "Writing that critiques social or political injustice"],
        ]),
    },
    "world-literature-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Global novel", "Fiction that engages with transnational themes and audiences"],
        ]),
    },
    "world-literature-g9-l50": {
        "data_table": table(["Comparison Type", "Example"], [
            ["Hero archetype", "Comparing heroes across different cultures' epics"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 World Literature lessons (completing 50/50).")


if __name__ == "__main__":
    main()
