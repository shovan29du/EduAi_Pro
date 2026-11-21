#!/usr/bin/env python3
"""Depth pass, Grade 8 World Literature: fill in real, hand-checked
data_table content for the 38 Grade 8 World Literature lessons not
covered by the earlier breadth-first batch. Brings Grade 8 World
Literature to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "wl-g8-l1": {
        "data_table": table(["Movement", "Approximate Period"], [
            ["Realism", "Mid to late 19th century"], ["Modernism", "Late 19th to early 20th century"],
        ]),
    },
    "world-literature-g8-l2": {
        "data_table": table(["Epic", "Hero"], [
            ["The Iliad", "Achilles"], ["The Odyssey", "Odysseus"],
        ]),
    },
    "world-literature-g8-l3": {
        "data_table": table(["God/Hero", "Known For"], [
            ["Zeus", "King of the gods"], ["Hercules", "Twelve legendary labors"],
        ]),
    },
    "world-literature-g8-l4": {
        "data_table": table(["Fact", "Detail"], [
            ["Credited to", "Aesop, ancient Greece"], ["Style", "Short animal stories with morals"],
        ]),
    },
    "world-literature-g8-l5": {
        "data_table": table(["Comedy", "Author"], [
            ["A Midsummer Night's Dream", "William Shakespeare"], ["Much Ado About Nothing", "William Shakespeare"],
        ]),
    },
    "world-literature-g8-l6": {
        "data_table": table(["Tragedy", "Author"], [
            ["Hamlet", "William Shakespeare"], ["Macbeth", "William Shakespeare"],
        ]),
    },
    "world-literature-g8-l7": {
        "data_table": table(["Poet", "Known For"], [
            ["William Wordsworth", "Romantic poetry celebrating nature"],
        ]),
    },
    "world-literature-g8-l8": {
        "data_table": table(["Author", "Famous Work"], [
            ["Charles Dickens", "Oliver Twist"],
        ]),
    },
    "world-literature-g8-l9": {
        "data_table": table(["Author", "Famous Work"], [
            ["Jane Austen", "Pride and Prejudice"],
        ]),
    },
    "world-literature-g8-l10": {
        "data_table": table(["Author", "Famous Work"], [
            ["Mark Twain", "The Adventures of Tom Sawyer"],
        ]),
    },
    "world-literature-g8-l12": {
        "data_table": table(["Author", "Famous Work"], [
            ["Edgar Allan Poe", "The Tell-Tale Heart"],
        ]),
    },
    "world-literature-g8-l13": {
        "data_table": table(["Author", "Famous Work"], [
            ["Charlotte Bronte", "Jane Eyre"], ["Emily Bronte", "Wuthering Heights"],
        ]),
    },
    "world-literature-g8-l14": {
        "data_table": table(["Author", "Famous Work"], [
            ["Leo Tolstoy", "War and Peace"],
        ]),
    },
    "world-literature-g8-l15": {
        "data_table": table(["Author", "Known For"], [
            ["Anton Chekhov", "Master of the short story form"],
        ]),
    },
    "world-literature-g8-l16": {
        "data_table": table(["Poet", "Fact"], [
            ["Rabindranath Tagore", "First non-European Nobel laureate in Literature, 1913"],
        ]),
    },
    "world-literature-g8-l17": {
        "data_table": table(["Fact", "Detail"], [
            ["Also known as", "One Thousand and One Nights"], ["Origin", "Middle Eastern and South Asian folklore"],
        ]),
    },
    "world-literature-g8-l19": {
        "data_table": table(["Author", "Region"], [
            ["Chinua Achebe", "Nigeria"],
        ]),
    },
    "world-literature-g8-l20": {
        "data_table": table(["Author", "Country"], [
            ["Gabriel Garcia Marquez", "Colombia, known for magical realism"],
        ]),
    },
    "world-literature-g8-l21": {
        "data_table": table(["Poet", "Country"], [
            ["Pablo Neruda", "Chile, Nobel laureate in Literature, 1971"],
        ]),
    },
    "world-literature-g8-l22": {
        "data_table": table(["Author", "Famous Work"], [
            ["Franz Kafka", "The Metamorphosis"],
        ]),
    },
    "world-literature-g8-l23": {
        "data_table": table(["Author", "Famous Work"], [
            ["George Orwell", "Animal Farm"],
        ]),
    },
    "world-literature-g8-l24": {
        "data_table": table(["Playwright", "Famous Work"], [
            ["Henrik Ibsen", "A Doll's House"],
        ]),
    },
    "world-literature-g8-l25": {
        "data_table": table(["Author", "Fact"], [
            ["Henry David Thoreau", "Author of Walden"], ["Ralph Waldo Emerson", "Leading transcendentalist essayist"],
        ]),
    },
    "world-literature-g8-l26": {
        "data_table": table(["Fact", "Detail"], [
            ["Harlem Renaissance", "African American cultural movement centered in Harlem, 1920s"],
        ]),
    },
    "world-literature-g8-l27": {
        "data_table": table(["Poet", "Known For"], [
            ["Langston Hughes", "A leading voice of the Harlem Renaissance"],
        ]),
    },
    "world-literature-g8-l28": {
        "data_table": table(["Author", "Famous Work"], [
            ["Toni Morrison", "Beloved, Nobel laureate in Literature, 1993"],
        ]),
    },
    "world-literature-g8-l29": {
        "data_table": table(["Folktale", "Origin"], [
            ["Cinderella variants", "Found across many cultures"],
        ]),
    },
    "world-literature-g8-l30": {
        "data_table": table(["Fact", "Detail"], [
            ["The Epic of Gilgamesh", "One of the earliest known works of literature, from ancient Mesopotamia"],
        ]),
    },
    "world-literature-g8-l31": {
        "data_table": table(["Fact", "Detail"], [
            ["Origin", "Ancient India"], ["Purpose", "Teaching wisdom through animal stories"],
        ]),
    },
    "world-literature-g8-l32": {
        "data_table": table(["Fact", "Detail"], [
            ["Journey to the West", "Classic Chinese novel"],
        ]),
    },
    "world-literature-g8-l33": {
        "data_table": table(["Poet", "Country"], [
            ["Matsuo Basho", "Japan, master of haiku"],
        ]),
    },
    "world-literature-g8-l34": {
        "data_table": table(["Fact", "Detail"], [
            ["Collectors", "Jacob and Wilhelm Grimm"], ["Country", "Germany"],
        ]),
    },
    "world-literature-g8-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Hans Christian Andersen"], ["Country", "Denmark"],
        ]),
    },
    "world-literature-g8-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Lewis Carroll"], ["Famous work", "Alice's Adventures in Wonderland"],
        ]),
    },
    "world-literature-g8-l37": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "J.R.R. Tolkien"], ["Famous work", "The Lord of the Rings"],
        ]),
    },
    "world-literature-g8-l38": {
        "data_table": table(["Author", "Famous Work"], [
            ["Jules Verne", "Twenty Thousand Leagues Under the Sea"],
        ]),
    },
    "world-literature-g8-l39": {
        "data_table": table(["Fact", "Detail"], [
            ["Author", "Anne Frank"], ["Historical context", "Written while hiding during the Holocaust, WWII"],
        ]),
    },
    "world-literature-g8-l40": {
        "data_table": table(["Archetype", "Example"], [
            ["The hero", "A protagonist who overcomes challenges"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 World Literature lessons (completing 40/40).")


if __name__ == "__main__":
    main()
