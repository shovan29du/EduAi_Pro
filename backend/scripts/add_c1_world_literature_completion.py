#!/usr/bin/env python3
"""Depth pass, C1 World Literature: fill in real, hand-checked data_table
content for the 69 C1 World Literature lessons not covered by the earlier
breadth-first batch. Brings C1 World Literature to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_world_literature_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "world-literature-c1-l1": {
        "data_table": table(["Work", "Origin"], [
            ["The Odyssey", "Ancient Greece"], ["The Ramayana", "Ancient India"],
        ]),
    },
    "world-literature-c1-l2": {
        "data_table": table(["Period", "Feature"], [
            ["Modern literature", "Emphasizes individual perspective and formal experimentation"],
        ]),
    },
    "world-literature-c1-l4": {
        "data_table": table(["Work", "Focus"], [
            ["The Iliad", "The Trojan War and the wrath of Achilles"], ["The Odyssey", "Odysseus's long journey home"],
        ]),
    },
    "world-literature-c1-l5": {
        "data_table": table(["Playwright", "Notable Work"], [
            ["Sophocles", "Oedipus Rex"], ["Euripides", "Medea"],
        ]),
    },
    "world-literature-c1-l6": {
        "data_table": table(["Feature", "Detail"], [
            ["Early novel", "Extended prose fiction focused on character and plot development"],
        ]),
    },
    "world-literature-c1-l7": {
        "data_table": table(["Feature", "Detail"], [
            ["Modernism", "A literary movement rejecting traditional narrative structure and realism"],
        ]),
    },
    "world-literature-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Postcolonial literature", "Writing that engages with the legacy and aftermath of colonialism"],
        ]),
    },
    "world-literature-c1-l9": {
        "data_table": table(["Theme", "Focus"], [
            ["African diaspora literature", "Explores identity, displacement, and heritage across the Black diaspora"],
        ]),
    },
    "world-literature-c1-l10": {
        "data_table": table(["Movement", "Feature"], [
            ["Magical realism", "Blends realistic narrative with fantastical elements"],
        ]),
    },
    "world-literature-c1-l11": {
        "data_table": table(["Challenge", "Detail"], [
            ["Translation", "Requires balancing literal meaning with tone, rhythm, and cultural nuance"],
        ]),
    },
    "world-literature-c1-l12": {
        "data_table": table(["Writer", "Notable Work"], [
            ["Virginia Woolf", "Mrs Dalloway"], ["Toni Morrison", "Beloved"],
        ]),
    },
    "world-literature-c1-l13": {
        "data_table": table(["Function", "Example"], [
            ["Literature as resistance", "Uses narrative to critique oppression and inspire change"],
        ]),
    },
    "world-literature-c1-l14": {
        "data_table": table(["Theme", "Focus"], [
            ["Exile literature", "Explores displacement, loss of homeland, and dual identity"],
        ]),
    },
    "world-literature-c1-l15": {
        "data_table": table(["Feature", "Detail"], [
            ["Short story", "A concise narrative form focused on a single effect or moment"],
        ]),
    },
    "world-literature-c1-l16": {
        "data_table": table(["Tradition", "Feature"], [
            ["Haiku", "Japanese three-line poem capturing a fleeting moment"], ["Ghazal", "Persian/Urdu poetic form of rhyming couplets"],
        ]),
    },
    "world-literature-c1-l17": {
        "data_table": table(["Type", "Example"], [
            ["Film adaptation", "A novel reimagined for the screen"],
        ]),
    },
    "world-literature-c1-l18": {
        "data_table": table(["Effect", "Detail"], [
            ["Globalization", "Expands access to literature from diverse cultures worldwide"],
        ]),
    },
    "world-literature-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Literary censorship", "The suppression or banning of texts by authorities"],
        ]),
    },
    "world-literature-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Identifying a shared theme", "Anchors the comparison between two texts"],
        ]),
    },
    "world-literature-c1-l21": {
        "data_table": table(["Feature", "Detail"], [
            ["Epic of Gilgamesh", "A Mesopotamian epic considered among the oldest surviving works of literature"],
        ]),
    },
    "world-literature-c1-l22": {
        "data_table": table(["Feature", "Detail"], [
            ["Bhagavad Gita", "A Sanskrit dialogue on duty and righteousness within the Mahabharata"],
        ]),
    },
    "world-literature-c1-l23": {
        "data_table": table(["Part", "Focus"], [
            ["Inferno", "Journey through Hell"], ["Paradiso", "Journey through Heaven"],
        ]),
    },
    "world-literature-c1-l24": {
        "data_table": table(["Feature", "Detail"], [
            ["Don Quixote", "Often considered the first modern novel, satirizing chivalric romance"],
        ]),
    },
    "world-literature-c1-l25": {
        "data_table": table(["Influence", "Detail"], [
            ["Shakespeare", "His plays have been translated and adapted across nearly every world literary tradition"],
        ]),
    },
    "world-literature-c1-l26": {
        "data_table": table(["Poet", "Dynasty"], [
            ["Li Bai", "Tang Dynasty"], ["Du Fu", "Tang Dynasty"],
        ]),
    },
    "world-literature-c1-l27": {
        "data_table": table(["Feature", "Detail"], [
            ["The Tale of Genji", "Often considered the world's first novel, written by Murasaki Shikibu"],
        ]),
    },
    "world-literature-c1-l28": {
        "data_table": table(["Feature", "Detail"], [
            ["Frame narrative", "A story containing embedded stories, as told by Scheherazade"],
        ]),
    },
    "world-literature-c1-l29": {
        "data_table": table(["Author", "Notable Work"], [
            ["Leo Tolstoy", "Anna Karenina"], ["Fyodor Dostoevsky", "Crime and Punishment"],
        ]),
    },
    "world-literature-c1-l30": {
        "data_table": table(["Poet", "Notable Work"], [
            ["Charles Baudelaire", "Les Fleurs du mal"],
        ]),
    },
    "world-literature-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Bildungsroman", "A novel focused on the protagonist's psychological and moral growth"],
        ]),
    },
    "world-literature-c1-l32": {
        "data_table": table(["Feature", "Detail"], [
            ["Gothic literature", "Combines horror, romance, and supernatural elements in atmospheric settings"],
        ]),
    },
    "world-literature-c1-l33": {
        "data_table": table(["Feature", "Detail"], [
            ["Romanticism", "Emphasized emotion, nature, and individualism over reason"],
        ]),
    },
    "world-literature-c1-l34": {
        "data_table": table(["Author", "Notable Work"], [
            ["Charles Dickens", "Great Expectations"],
        ]),
    },
    "world-literature-c1-l35": {
        "data_table": table(["Feature", "Detail"], [
            ["Naturalism", "Depicts characters shaped by heredity and environment, often deterministically"],
        ]),
    },
    "world-literature-c1-l36": {
        "data_table": table(["Feature", "Detail"], [
            ["Kafka's work", "Explores bureaucratic absurdity and existential isolation"],
        ]),
    },
    "world-literature-c1-l37": {
        "data_table": table(["Author", "Notable Work"], [
            ["Albert Camus", "The Stranger"], ["Jean-Paul Sartre", "Nausea"],
        ]),
    },
    "world-literature-c1-l38": {
        "data_table": table(["Feature", "Detail"], [
            ["Absurdist drama", "Depicts meaningless or illogical situations to reflect life's absurdity"],
        ]),
    },
    "world-literature-c1-l39": {
        "data_table": table(["Feature", "Detail"], [
            ["Tagore's work", "First non-European to win the Nobel Prize in Literature (1913)"],
        ]),
    },
    "world-literature-c1-l40": {
        "data_table": table(["Author", "Notable Work"], [
            ["Derek Walcott", "Omeros"],
        ]),
    },
    "world-literature-c1-l41": {
        "data_table": table(["Feature", "Detail"], [
            ["One Hundred Years of Solitude", "Landmark magical realist novel by García Márquez"],
        ]),
    },
    "world-literature-c1-l42": {
        "data_table": table(["Feature", "Detail"], [
            ["Pablo Neruda", "Chilean poet, Nobel laureate known for love poetry and political verse"],
        ]),
    },
    "world-literature-c1-l43": {
        "data_table": table(["Author", "Notable Work"], [
            ["Salman Rushdie", "Midnight's Children"],
        ]),
    },
    "world-literature-c1-l44": {
        "data_table": table(["Author", "Notable Work"], [
            ["Chimamanda Ngozi Adichie", "Half of a Yellow Sun"],
        ]),
    },
    "world-literature-c1-l45": {
        "data_table": table(["Author", "Notable Work"], [
            ["Elie Wiesel", "Night"],
        ]),
    },
    "world-literature-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Testimonial literature", "First-person accounts bearing witness to injustice or historical trauma"],
        ]),
    },
    "world-literature-c1-l47": {
        "data_table": table(["Tradition", "Feature"], [
            ["Indigenous literature", "Centers oral tradition, land, and community identity"],
        ]),
    },
    "world-literature-c1-l48": {
        "data_table": table(["Author", "Notable Work"], [
            ["James Baldwin", "Giovanni's Room"],
        ]),
    },
    "world-literature-c1-l49": {
        "data_table": table(["Tradition", "Example"], [
            ["Folk tales", "Passed down orally across generations in many cultures"],
        ]),
    },
    "world-literature-c1-l50": {
        "data_table": table(["Author", "Notable Work"], [
            ["Liu Cixin", "The Three-Body Problem"],
        ]),
    },
    "world-literature-c1-l51": {
        "data_table": table(["Author", "Notable Work"], [
            ["Arthur Conan Doyle", "The Adventures of Sherlock Holmes"],
        ]),
    },
    "world-literature-c1-l52": {
        "data_table": table(["Author", "Notable Work"], [
            ["Erich Maria Remarque", "All Quiet on the Western Front"],
        ]),
    },
    "world-literature-c1-l53": {
        "data_table": table(["Feature", "Detail"], [
            ["Memoir", "A first-person account focused on the author's personal experience"],
        ]),
    },
    "world-literature-c1-l54": {
        "data_table": table(["Feature", "Detail"], [
            ["Literary realism", "Depicts everyday life and characters with accuracy and detail"],
        ]),
    },
    "world-literature-c1-l55": {
        "data_table": table(["Author", "Notable Work"], [
            ["Art Spiegelman", "Maus"],
        ]),
    },
    "world-literature-c1-l56": {
        "data_table": table(["Tradition", "Feature"], [
            ["Griot tradition", "West African oral historians and storytellers"],
        ]),
    },
    "world-literature-c1-l57": {
        "data_table": table(["Technique", "Meaning"], [
            ["Stream of consciousness", "Narrates a character's continuous flow of thoughts and impressions"],
        ]),
    },
    "world-literature-c1-l58": {
        "data_table": table(["Feature", "Detail"], [
            ["Postmodern literature", "Employs fragmentation, metafiction, and skepticism of grand narratives"],
        ]),
    },
    "world-literature-c1-l59": {
        "data_table": table(["Trend", "Detail"], [
            ["Growth in translated fiction", "More non-English works reaching global English-language readers"],
        ]),
    },
    "world-literature-c1-l60": {
        "data_table": table(["Prize", "Scope"], [
            ["Nobel Prize in Literature", "Honors a writer's complete body of work"], ["Booker Prize", "Honors a single novel published in English"],
        ]),
    },
    "world-literature-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing narrative structure", "Examining how Genji unfolds through interconnected episodes"],
        ]),
    },
    "world-literature-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing alienation", "Tracing bureaucratic dread in a Kafka short story"],
        ]),
    },
    "world-literature-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing cultural identity", "Examining themes of nationalism in Tagore's poetry"],
        ]),
    },
    "world-literature-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing imagery", "Interpreting natural imagery in a Neruda love poem"],
        ]),
    },
    "world-literature-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Comparing classic texts", "Identifying shared heroic archetypes across two epics"],
        ]),
    },
    "world-literature-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Tracing modern themes", "Comparing alienation across two 20th-century novels"],
        ]),
    },
    "world-literature-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Defining world literature", "Distinguishing it from national literary traditions"],
        ]),
    },
    "world-literature-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an epic hero", "Comparing Odysseus's cunning to another epic hero's traits"],
        ]),
    },
    "world-literature-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing tragic structure", "Identifying the tragic flaw in a Greek tragedy's protagonist"],
        ]),
    },
    "world-literature-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Tracing the novel's evolution", "Comparing an early novel's structure to a contemporary one"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["World Literature"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json World Literature: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 World Literature lessons (completing 70/70).")


if __name__ == "__main__":
    main()
