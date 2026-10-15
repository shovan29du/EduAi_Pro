#!/usr/bin/env python3
"""Depth pass, C2 General Knowledge: fill in real, hand-checked
data_table content for the 69 C2 General Knowledge lessons not
covered by the earlier breadth-first batch. Brings C2 General
Knowledge to full 70/70 coverage.

l61-l70 are "Worked Analysis" companions to l1-l10. l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_general_knowledge_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "general-knowledge-c2-l1": {
        "data_table": table(["Institution", "Role"], [
            ["United Nations", "Coordinates international peace, security, and development efforts"],
        ]),
    },
    "general-knowledge-c2-l2": {
        "data_table": table(["Skill", "Purpose"], [
            ["Media literacy", "Evaluates the credibility and bias of information sources"],
        ]),
    },
    "general-knowledge-c2-l4": {
        "data_table": table(["Tradition", "Core Belief"], [
            ["Buddhism", "The end of suffering through following the Noble Eightfold Path"],
            ["Hinduism", "Diverse traditions centered on dharma, karma, and moksha"],
        ]),
    },
    "general-knowledge-c2-l5": {
        "data_table": table(["System", "Feature"], [
            ["Market economy", "Prices set primarily by supply and demand"],
            ["Mixed economy", "Combines market mechanisms with government intervention"],
        ]),
    },
    "general-knowledge-c2-l6": {
        "data_table": table(["Innovation", "Impact"], [
            ["Printing press", "Massively expanded the spread of written knowledge"],
        ]),
    },
    "general-knowledge-c2-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["World geography synthesis", "Connects physical features, climate, and human settlement patterns"],
        ]),
    },
    "general-knowledge-c2-l8": {
        "data_table": table(["Region", "Cultural Note"], [
            ["East Asia", "Confucian values historically shaped social and educational norms"],
        ]),
    },
    "general-knowledge-c2-l9": {
        "data_table": table(["Puzzle Type", "Skill Practiced"], [
            ["Logic grid puzzle", "Deductive reasoning from a set of constraints"],
        ]),
    },
    "general-knowledge-c2-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["General science literacy", "Understanding basic scientific method and core findings across fields"],
        ]),
    },
    "general-knowledge-c2-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Compound interest", "Interest calculated on both principal and previously accumulated interest"],
        ]),
    },
    "general-knowledge-c2-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Civic knowledge", "Understanding of government structure, rights, and civic responsibility"],
        ]),
    },
    "general-knowledge-c2-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Environmental literacy", "Understanding of ecosystems, sustainability, and human environmental impact"],
        ]),
    },
    "general-knowledge-c2-l14": {
        "data_table": table(["Concept", "Detail"], [
            ["Health literacy", "Ability to find, understand, and use health information effectively"],
        ]),
    },
    "general-knowledge-c2-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Technology literacy", "Functional understanding of how digital tools and systems work"],
        ]),
    },
    "general-knowledge-c2-l16": {
        "data_table": table(["Figure", "Field"], [
            ["Marie Curie", "Physics and chemistry — pioneering research on radioactivity"],
        ]),
    },
    "general-knowledge-c2-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Trivia question design", "Balances difficulty and clarity to test recall without ambiguity"],
        ]),
    },
    "general-knowledge-c2-l18": {
        "data_table": table(["Step", "Purpose"], [
            ["Source triangulation", "Confirms a claim across multiple independent, credible sources"],
        ]),
    },
    "general-knowledge-c2-l19": {
        "data_table": table(["Organization", "Focus"], [
            ["World Health Organization", "Coordinates international public health policy and response"],
        ]),
    },
    "general-knowledge-c2-l20": {
        "data_table": table(["Fallacy", "Description"], [
            ["Ad hominem", "Attacks the person rather than the argument"],
        ]),
    },
    "general-knowledge-c2-l21": {
        "data_table": table(["Structure", "Function"], [
            ["Security Council", "UN body responsible for maintaining international peace and security"],
        ]),
    },
    "general-knowledge-c2-l22": {
        "data_table": table(["System", "Feature"], [
            ["Parliamentary system", "Executive is drawn from and accountable to the legislature"],
            ["Presidential system", "Executive and legislature are elected and function separately"],
        ]),
    },
    "general-knowledge-c2-l23": {
        "data_table": table(["Practice", "Goal"], [
            ["Interfaith dialogue", "Builds mutual understanding across differing religious traditions"],
        ]),
    },
    "general-knowledge-c2-l24": {
        "data_table": table(["System", "Development"], [
            ["Bretton Woods system", "Established postwar fixed exchange rates and international financial institutions"],
        ]),
    },
    "general-knowledge-c2-l25": {
        "data_table": table(["Crisis", "Cause"], [
            ["Currency crisis", "Often triggered by loss of confidence and rapid capital flight"],
        ]),
    },
    "general-knowledge-c2-l26": {
        "data_table": table(["Concept", "Detail"], [
            ["Paradigm shift", "A fundamental change in the basic assumptions of a scientific field"],
        ]),
    },
    "general-knowledge-c2-l27": {
        "data_table": table(["Feature", "Geopolitical Effect"], [
            ["River border", "Can both unite trade and become a contested territorial line"],
        ]),
    },
    "general-knowledge-c2-l28": {
        "data_table": table(["Issue", "Detail"], [
            ["Nobel Prize omission", "Some major contributors have been controversially excluded from recognition"],
        ]),
    },
    "general-knowledge-c2-l29": {
        "data_table": table(["Policy", "Effect"], [
            ["Language policy", "National language choices can accelerate or slow minority language decline"],
        ]),
    },
    "general-knowledge-c2-l30": {
        "data_table": table(["Revolution", "Feature"], [
            ["Industrial Revolution", "Mechanized production reshaped economies and societies"],
            ["Digital Revolution", "Computing and networks reshaped information and communication"],
        ]),
    },
    "general-knowledge-c2-l31": {
        "data_table": table(["Event", "Detail"], [
            ["Sporting diplomacy", "International competitions have both eased and heightened political tensions"],
        ]),
    },
    "general-knowledge-c2-l32": {
        "data_table": table(["Symbol", "Function"], [
            ["National flag", "Communicates collective identity and historical narrative"],
        ]),
    },
    "general-knowledge-c2-l33": {
        "data_table": table(["Driver", "Effect"], [
            ["Desertification", "Land degradation can force displacement and climate-driven migration"],
        ]),
    },
    "general-knowledge-c2-l34": {
        "data_table": table(["Milestone", "Year"], [
            ["First human spaceflight", "1961"],
            ["First Moon landing", "1969"],
        ]),
    },
    "general-knowledge-c2-l35": {
        "data_table": table(["Practice", "Purpose"], [
            ["Cultural heritage preservation", "Protects sites and traditions from loss due to conflict or neglect"],
        ]),
    },
    "general-knowledge-c2-l36": {
        "data_table": table(["Body", "Role"], [
            ["ICANN", "Coordinates the global domain name and IP address system"],
        ]),
    },
    "general-knowledge-c2-l37": {
        "data_table": table(["Stage", "Feature"], [
            ["Demographic transition", "Populations shift from high to low birth and death rates over development"],
        ]),
    },
    "general-knowledge-c2-l38": {
        "data_table": table(["System", "Feature"], [
            ["Religious law system", "Governs personal and sometimes civil matters within a faith community"],
        ]),
    },
    "general-knowledge-c2-l39": {
        "data_table": table(["Trend", "Detail"], [
            ["Democratic backsliding", "Erosion of democratic norms and institutions over time"],
        ]),
    },
    "general-knowledge-c2-l40": {
        "data_table": table(["Project", "Impact"], [
            ["Megaproject", "Large-scale infrastructure often reshapes regional economies and ecosystems"],
        ]),
    },
    "general-knowledge-c2-l41": {
        "data_table": table(["Era", "Feature"], [
            ["Age of Exploration", "European voyages expanded global trade networks and colonial claims"],
        ]),
    },
    "general-knowledge-c2-l42": {
        "data_table": table(["Concern", "Response"], [
            ["Biodiversity loss", "Protected areas and international agreements aim to slow species decline"],
        ]),
    },
    "general-knowledge-c2-l43": {
        "data_table": table(["Symbol", "Conflict Role"], [
            ["National monument", "Can become a flashpoint for competing historical claims"],
        ]),
    },
    "general-knowledge-c2-l44": {
        "data_table": table(["Body", "Role"], [
            ["Global public health governance", "Coordinates disease surveillance and response across borders"],
        ]),
    },
    "general-knowledge-c2-l45": {
        "data_table": table(["Era", "Feature"], [
            ["Modern Olympic movement", "Revived in 1896, has grown into a major global sporting institution"],
        ]),
    },
    "general-knowledge-c2-l46": {
        "data_table": table(["Trend", "Detail"], [
            ["Food security", "Supply chain resilience and climate stability both shape global food access"],
        ]),
    },
    "general-knowledge-c2-l47": {
        "data_table": table(["Example", "Statement"], [
            ["Monumental architecture", "Can project state power or national identity"],
        ]),
    },
    "general-knowledge-c2-l48": {
        "data_table": table(["Issue", "Detail"], [
            ["Global education inequality", "Access and quality vary sharply by income and region"],
        ]),
    },
    "general-knowledge-c2-l49": {
        "data_table": table(["Mechanism", "Role"], [
            ["International Criminal Court", "Prosecutes individuals for war crimes and crimes against humanity"],
        ]),
    },
    "general-knowledge-c2-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Maritime law", "Governs use of the sea, including territorial waters and exclusive economic zones"],
        ]),
    },
    "general-knowledge-c2-l51": {
        "data_table": table(["Treaty", "Significance"], [
            ["Paris Agreement", "International accord targeting global climate change mitigation"],
        ]),
    },
    "general-knowledge-c2-l52": {
        "data_table": table(["Trend", "Detail"], [
            ["Trade route realignment", "Shifting geopolitics reroutes global shipping and supply chains"],
        ]),
    },
    "general-knowledge-c2-l53": {
        "data_table": table(["Trend", "Detail"], [
            ["Energy transition", "Shift from fossil fuels toward renewable energy sources"],
        ]),
    },
    "general-knowledge-c2-l54": {
        "data_table": table(["Process", "Purpose"], [
            ["World Heritage designation", "Recognizes and helps protect sites of outstanding universal value"],
        ]),
    },
    "general-knowledge-c2-l55": {
        "data_table": table(["Trend", "Detail"], [
            ["Megacity growth", "Rapid urban expansion strains housing, transit, and infrastructure"],
        ]),
    },
    "general-knowledge-c2-l56": {
        "data_table": table(["Standard", "Purpose"], [
            ["UTC/Coordinated Universal Time", "Provides a common global time reference"],
        ]),
    },
    "general-knowledge-c2-l57": {
        "data_table": table(["Issue", "Detail"], [
            ["Misinformation", "Spreads faster online and requires active verification habits to counter"],
        ]),
    },
    "general-knowledge-c2-l58": {
        "data_table": table(["Design Choice", "Effect"], [
            ["Federal constitution", "Divides power between national and regional governments"],
        ]),
    },
    "general-knowledge-c2-l59": {
        "data_table": table(["Pattern", "Driver"], [
            ["Global migration pattern", "Shaped by economic opportunity, conflict, and climate pressures"],
        ]),
    },
    "general-knowledge-c2-l60": {
        "data_table": table(["Task", "Focus"], [
            ["Current events synthesis", "Connects global news to underlying historical and structural patterns"],
        ]),
    },
}

# l3 was already completed by an earlier breadth-first batch.
_l3_source_table = table(["Intellectual Movement", "Approx. Period"], [
    ["The Renaissance", "14th-17th century"],
    ["The Enlightenment", "17th-18th century"],
])

# l61-l70 "Worked Analysis" lessons reuse the data_table of l1-l10.
WORKED_ANALYSIS_MAP = {61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10}
for worked_n, base_n in WORKED_ANALYSIS_MAP.items():
    base_key = f"general-knowledge-c2-l{base_n}"
    if base_key in CHARTS:
        CHARTS[f"general-knowledge-c2-l{worked_n}"] = {
            "data_table": CHARTS[base_key]["data_table"],
        }
    elif base_n == 3:
        CHARTS[f"general-knowledge-c2-l{worked_n}"] = {
            "data_table": _l3_source_table,
        }


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["General Knowledge"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json General Knowledge: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 General Knowledge lessons (completing 70/70).")


if __name__ == "__main__":
    main()
