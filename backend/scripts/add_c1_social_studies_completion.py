#!/usr/bin/env python3
"""Depth pass, C1 Social Studies: fill in real, hand-checked data_table
content for the 69 C1 Social Studies lessons not covered by the earlier
breadth-first batch. Brings C1 Social Studies to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_social_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "social-studies-c1-l1": {
        "data_table": table(["Institution", "Function"], [
            ["Family", "Primary unit of socialization"], ["Government", "Creates and enforces laws"],
        ]),
    },
    "social-studies-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Culture", "Shared beliefs, customs, and practices of a group"],
        ]),
    },
    "social-studies-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Cultural anthropology", "The study of human cultures and their social practices"],
        ]),
    },
    "social-studies-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Social stratification", "The hierarchical arrangement of individuals into social classes"],
        ]),
    },
    "social-studies-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethnicity", "Shared cultural heritage, language, or ancestry"], ["Race", "A social construct often based on physical characteristics"],
        ]),
    },
    "social-studies-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Gender", "Socially constructed roles and identities associated with being male, female, or other"],
        ]),
    },
    "social-studies-c1-l8": {
        "data_table": table(["Concept", "Meaning"], [
            ["Conformity", "Adjusting behavior to match group norms"],
        ]),
    },
    "social-studies-c1-l9": {
        "data_table": table(["Example", "Goal"], [
            ["Civil rights movement", "Ending racial segregation and discrimination"],
        ]),
    },
    "social-studies-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Urban sociology", "The study of social life and structure in cities"],
        ]),
    },
    "social-studies-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Kinship", "Social relationships based on blood, marriage, or adoption"],
        ]),
    },
    "social-studies-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Deviance", "Behavior that violates a society's norms"],
        ]),
    },
    "social-studies-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "The growing interconnection of economies, cultures, and societies worldwide"],
        ]),
    },
    "social-studies-c1-l14": {
        "data_table": table(["Method", "Type"], [
            ["Survey", "Quantitative data collection"], ["Interview", "Qualitative data collection"],
        ]),
    },
    "social-studies-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Demography", "The statistical study of population size, structure, and change"],
        ]),
    },
    "social-studies-c1-l16": {
        "data_table": table(["Effect", "Detail"], [
            ["Agenda-setting", "Media influences which issues the public considers important"],
        ]),
    },
    "social-studies-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Hidden curriculum", "Unspoken social norms and values taught alongside formal lessons"],
        ]),
    },
    "social-studies-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Division of labor", "The distribution of specialized tasks across a workforce"],
        ]),
    },
    "social-studies-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Secularization", "The declining influence of religion in public life"],
        ]),
    },
    "social-studies-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Social policy", "Government actions addressing social welfare and public needs"],
        ]),
    },
    "social-studies-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Political science", "The study of government systems, power, and political behavior"],
        ]),
    },
    "social-studies-c1-l22": {
        "data_table": table(["System", "Feature"], [
            ["Federal system", "Power divided between national and regional governments"], ["Unitary system", "Power concentrated in a central government"],
        ]),
    },
    "social-studies-c1-l23": {
        "data_table": table(["Type", "Feature"], [
            ["Direct democracy", "Citizens vote directly on policy"], ["Representative democracy", "Citizens elect officials to make decisions"],
        ]),
    },
    "social-studies-c1-l24": {
        "data_table": table(["Ideology", "Core Value"], [
            ["Liberalism", "Individual rights and limited government intervention"], ["Socialism", "Collective ownership and economic equality"],
        ]),
    },
    "social-studies-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Political party", "An organization that seeks to gain and exercise governmental power"],
        ]),
    },
    "social-studies-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Sampling error", "The gap between a poll's result and the true population value"],
        ]),
    },
    "social-studies-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["International relations", "The study of interactions between nations, including diplomacy and conflict"],
        ]),
    },
    "social-studies-c1-l28": {
        "data_table": table(["Body", "Role"], [
            ["UN Security Council", "Maintains international peace and security"],
        ]),
    },
    "social-studies-c1-l29": {
        "data_table": table(["Document", "Significance"], [
            ["Universal Declaration of Human Rights", "1948, establishes fundamental rights for all people"],
        ]),
    },
    "social-studies-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Microeconomics", "Studies individual and firm-level economic decisions"],
        ]),
    },
    "social-studies-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Macroeconomics", "Studies economy-wide phenomena like inflation and unemployment"],
        ]),
    },
    "social-studies-c1-l32": {
        "data_table": table(["Concept", "Effect"], [
            ["Increased demand", "Tends to raise price if supply stays constant"],
        ]),
    },
    "social-studies-c1-l33": {
        "data_table": table(["Structure", "Feature"], [
            ["Monopoly", "A single seller dominates the market"], ["Perfect competition", "Many sellers, no single one sets the price"],
        ]),
    },
    "social-studies-c1-l34": {
        "data_table": table(["System", "Feature"], [
            ["Mixed economy", "Combines market and government intervention"],
        ]),
    },
    "social-studies-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Human geography", "Studies how people interact with and shape their environment"],
        ]),
    },
    "social-studies-c1-l36": {
        "data_table": table(["Type", "Meaning"], [
            ["Push factor", "A reason people leave a location"], ["Pull factor", "A reason people are drawn to a new location"],
        ]),
    },
    "social-studies-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Urbanization", "The growing proportion of a population living in cities"],
        ]),
    },
    "social-studies-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Criminology", "The scientific study of crime and criminal behavior"],
        ]),
    },
    "social-studies-c1-l39": {
        "data_table": table(["Theory", "Core Idea"], [
            ["Strain theory", "Crime results from a gap between goals and legitimate means to achieve them"],
        ]),
    },
    "social-studies-c1-l40": {
        "data_table": table(["Component", "Role"], [
            ["Police", "Investigate crimes and enforce laws"], ["Courts", "Determine guilt and impose sentences"],
        ]),
    },
    "social-studies-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Social welfare", "Government programs supporting citizens' basic needs"],
        ]),
    },
    "social-studies-c1-l42": {
        "data_table": table(["Action", "Example"], [
            ["Voting", "The most common form of civic participation"],
        ]),
    },
    "social-studies-c1-l43": {
        "data_table": table(["System", "Feature"], [
            ["Finland's education system", "Emphasizes equity and minimal standardized testing"],
        ]),
    },
    "social-studies-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental sociology", "Studies the relationship between society and the natural environment"],
        ]),
    },
    "social-studies-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Political economy", "Studies the interplay between political and economic systems"],
        ]),
    },
    "social-studies-c1-l46": {
        "data_table": table(["Institution", "Example"], [
            ["Education", "Schools and universities"], ["Religion", "Churches, mosques, temples"],
        ]),
    },
    "social-studies-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethnography", "Immersive research studying a culture from within"],
        ]),
    },
    "social-studies-c1-l48": {
        "data_table": table(["Class", "Feature"], [
            ["Working class", "Typically earns wages through manual or service labor"],
        ]),
    },
    "social-studies-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Nationalism", "A strong identification with and loyalty to one's nation"],
        ]),
    },
    "social-studies-c1-l50": {
        "data_table": table(["Stage", "Focus"], [
            ["Adolescence", "Identity formation and increasing independence"],
        ]),
    },
    "social-studies-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Ageism", "Discrimination or prejudice based on a person's age"],
        ]),
    },
    "social-studies-c1-l52": {
        "data_table": table(["Model", "Focus"], [
            ["Social model of disability", "Views disability as created by societal barriers, not just impairment"],
        ]),
    },
    "social-studies-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Immigration", "The movement of people into a country to settle"],
        ]),
    },
    "social-studies-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Consumer culture", "A society organized significantly around the purchase of goods and services"],
        ]),
    },
    "social-studies-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Popular culture", "Widely shared cultural practices, media, and trends"],
        ]),
    },
    "social-studies-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Social network", "The web of relationships connecting individuals within a society"],
        ]),
    },
    "social-studies-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["NGO", "Non-Governmental Organization, operates independently of government to address social issues"],
        ]),
    },
    "social-studies-c1-l58": {
        "data_table": table(["Concept", "Meaning"], [
            ["Social determinants of health", "Non-medical factors like income and education that influence health outcomes"],
        ]),
    },
    "social-studies-c1-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Peace and conflict studies", "Examines the causes of conflict and pathways to resolution"],
        ]),
    },
    "social-studies-c1-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Indigenous studies", "Explores the histories, rights, and cultures of indigenous peoples"],
        ]),
    },
    "social-studies-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Comparing government structures", "Contrasting federal and unitary systems"],
        ]),
    },
    "social-studies-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an institution", "Explaining how schools transmit social norms"],
        ]),
    },
    "social-studies-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing cultural practices", "Comparing customs across two cultural groups"],
        ]),
    },
    "social-studies-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Applying a sociological lens", "Explaining a social trend using a sociological theory"],
        ]),
    },
    "social-studies-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Conducting fieldwork", "Observing a community's daily practices firsthand"],
        ]),
    },
    "social-studies-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing inequality", "Mapping income distribution across a social hierarchy"],
        ]),
    },
    "social-studies-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Examining identity", "Analyzing how ethnicity shapes community belonging"],
        ]),
    },
    "social-studies-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing gender roles", "Comparing expectations across two cultural contexts"],
        ]),
    },
    "social-studies-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Applying conformity concepts", "Explaining peer pressure using a social psychology model"],
        ]),
    },
    "social-studies-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a social movement", "Assessing the strategies behind a historical protest campaign"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Social Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Social Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Social Studies lessons (completing 70/70).")


if __name__ == "__main__":
    main()
