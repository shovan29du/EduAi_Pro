#!/usr/bin/env python3
"""Depth pass, Grade 10 World Literature: fill in real, hand-checked
data_table content for the Grade 10 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 10 World
Literature to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g10-l1": {
        "data_table": table(["Fact", "Detail"], [
            ["Nobel Prize in Literature", "Awarded annually since 1901"],
        ]),
    },
    "world-literature-g10-l2": {
        "data_table": table(["Epic", "Subject"], [
            ["The Iliad", "The Trojan War"], ["The Odyssey", "Odysseus's journey home"],
        ]),
    },
    "world-literature-g10-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Structure", "A frame narrative told by Scheherazade"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g10-l5": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Dante Alighieri"], ["Structure", "Inferno, Purgatorio, Paradiso"],
        ]),
    },
    "world-literature-g10-l6": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Miguel de Cervantes"], ["Country", "Spain"],
        ]),
    },
    "world-literature-g10-l7": {
        "data_table": table(["Genre", "Example"], [
            ["Comedy", "Much Ado About Nothing"], ["History play", "Henry V"],
        ]),
    },
    "world-literature-g10-l8": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Jane Austen"], ["Notable work", "Pride and Prejudice"],
        ]),
    },
    "world-literature-g10-l9": {
        "data_table": table(["Author", "Famous Work"], [
            ["Leo Tolstoy", "War and Peace, Anna Karenina"],
        ]),
    },
    "world-literature-g10-l10": {
        "data_table": table(["Author", "Famous Work"], [
            ["Fyodor Dostoevsky", "Crime and Punishment"],
        ]),
    },
    "world-literature-g10-l12": {
        "data_table": table(["Author", "Style"], [
            ["Gabriel Garcia Marquez", "Magical realism, One Hundred Years of Solitude"],
        ]),
    },
    "world-literature-g10-l13": {
        "data_table": table(["Author", "Famous Work"], [
            ["Chinua Achebe", "Things Fall Apart"],
        ]),
    },
    "world-literature-g10-l14": {
        "data_table": table(["Fact", "Detail"], [
            ["Rabindranath Tagore", "First non-European Nobel laureate in Literature, 1913"],
        ]),
    },
    "world-literature-g10-l15": {
        "data_table": table(["Poet", "Country"], [
            ["Matsuo Basho", "Japan, master of haiku"],
        ]),
    },
    "world-literature-g10-l16": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Murasaki Shikibu"], ["Significance", "Often considered the world's first novel"],
        ]),
    },
    "world-literature-g10-l17": {
        "data_table": table(["Author", "Famous Work"], [
            ["Franz Kafka", "The Metamorphosis"],
        ]),
    },
    "world-literature-g10-l18": {
        "data_table": table(["Author", "Famous Work"], [
            ["Albert Camus", "The Stranger"],
        ]),
    },
    "world-literature-g10-l19": {
        "data_table": table(["Author", "Famous Work"], [
            ["Toni Morrison", "Beloved, Nobel laureate in Literature, 1993"],
        ]),
    },
    "world-literature-g10-l20": {
        "data_table": table(["Fact", "Detail"], [
            ["Tang Dynasty poetry", "618-907 CE, a golden age of Chinese poetry"],
        ]),
    },
    "world-literature-g10-l21": {
        "data_table": table(["Fact", "Detail"], [
            ["Journey to the West", "Classic Chinese novel"],
        ]),
    },
    "world-literature-g10-l22": {
        "data_table": table(["Poet", "Region"], [
            ["Rumi", "Persia, 13th-century Sufi poet"], ["Hafez", "Persia, 14th-century poet"],
        ]),
    },
    "world-literature-g10-l23": {
        "data_table": table(["Author", "Country"], [
            ["Isabel Allende", "Chile"],
        ]),
    },
    "world-literature-g10-l24": {
        "data_table": table(["Author", "Country"], [
            ["Henrik Ibsen", "Norway, playwright known for A Doll's House"],
        ]),
    },
    "world-literature-g10-l25": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Johann Wolfgang von Goethe"], ["Work", "Faust"],
        ]),
    },
    "world-literature-g10-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Voltaire", "French Enlightenment writer known for the satirical novel Candide"],
        ]),
    },
    "world-literature-g10-l27": {
        "data_table": table(["Author", "Known For"], [
            ["Anton Chekhov", "Master of the short story and drama"],
        ]),
    },
    "world-literature-g10-l28": {
        "data_table": table(["Author", "Famous Work"], [
            ["Virginia Woolf", "Mrs Dalloway"],
        ]),
    },
    "world-literature-g10-l29": {
        "data_table": table(["Author", "Famous Work"], [
            ["James Joyce", "Ulysses"],
        ]),
    },
    "world-literature-g10-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["The Ramayana", "Ancient Indian epic about Prince Rama"],
        ]),
    },
    "world-literature-g10-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["The Mahabharata", "One of the longest epic poems in world literature"],
        ]),
    },
    "world-literature-g10-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Naguib Mahfouz", "Egyptian novelist, Nobel laureate in Literature, 1988"],
        ]),
    },
    "world-literature-g10-l33": {
        "data_table": table(["Fact", "Detail"], [
            ["Wole Soyinka", "Nigerian playwright, first African Nobel laureate in Literature, 1986"],
        ]),
    },
    "world-literature-g10-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Pablo Neruda", "Chilean poet, Nobel laureate in Literature, 1971"],
        ]),
    },
    "world-literature-g10-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Jorge Luis Borges", "Argentine writer known for metafiction and labyrinthine narratives"],
        ]),
    },
    "world-literature-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Milan Kundera", "Czech-French novelist, author of The Unbearable Lightness of Being"],
        ]),
    },
    "world-literature-g10-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Orhan Pamuk", "Turkish novelist, Nobel laureate in Literature, 2006"],
        ]),
    },
    "world-literature-g10-l38": {
        "data_table": table(["Fact", "Detail"], [
            ["Derek Walcott", "Saint Lucian poet, Nobel laureate in Literature, 1992"],
        ]),
    },
    "world-literature-g10-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["South Asian diaspora literature", "Explores identity and migration across cultures"],
        ]),
    },
    "world-literature-g10-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Oral tradition", "Stories passed down verbally across generations"],
        ]),
    },
    "world-literature-g10-l41": {
        "data_table": table(["Fact", "Detail"], [
            ["Brothers Grimm", "German collectors of fairy tales, early 19th century"],
        ]),
    },
    "world-literature-g10-l42": {
        "data_table": table(["Tradition", "Origin"], [
            ["Aesop's Fables", "Ancient Greece"], ["Panchatantra", "Ancient India"],
        ]),
    },
    "world-literature-g10-l43": {
        "data_table": table(["Fact", "Detail"], [
            ["Epic of Gilgamesh", "Ancient Mesopotamian epic, among the oldest known literature"],
        ]),
    },
    "world-literature-g10-l44": {
        "data_table": table(["Fact", "Detail"], [
            ["Beowulf", "Old English epic poem about a hero who battles monsters"],
        ]),
    },
    "world-literature-g10-l45": {
        "data_table": table(["Fact", "Detail"], [
            ["Canterbury Tales", "Author Geoffrey Chaucer, late 14th century"],
        ]),
    },
    "world-literature-g10-l46": {
        "data_table": table(["Fact", "Detail"], [
            ["Moliere", "17th-century French playwright known for comedies"],
        ]),
    },
    "world-literature-g10-l47": {
        "data_table": table(["Fact", "Detail"], [
            ["Anne Frank's Diary", "Written while hiding during the Holocaust, WWII"],
        ]),
    },
    "world-literature-g10-l48": {
        "data_table": table(["Fact", "Detail"], [
            ["Elie Wiesel", "Author of Night, Nobel Peace Prize laureate, 1986"],
        ]),
    },
    "world-literature-g10-l49": {
        "data_table": table(["Fact", "Detail"], [
            ["Contemporary world poetry", "Reflects diverse global voices and themes"],
        ]),
    },
    "world-literature-g10-l50": {
        "data_table": table(["Myth Theme", "Cross-Cultural Example"], [
            ["Great flood", "Found in Mesopotamian, biblical, and other traditions"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 World Literature lessons (completing 50/50).")


if __name__ == "__main__":
    main()
