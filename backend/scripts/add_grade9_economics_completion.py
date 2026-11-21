#!/usr/bin/env python3
"""Depth pass, Grade 9 Economics: fill in real, hand-checked data_table
content for the 48 Grade 9 Economics lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Economics to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "econ-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Price mechanism", "How supply and demand set prices in a market"],
        ]),
    },
    "economics-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Scarcity", "Limited resources relative to unlimited wants"],
        ]),
    },
    "economics-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Opportunity cost", "The value of the next best alternative given up"],
        ]),
    },
    "economics-g9-l4": {
        "data_table": table(["Factor", "Example"], [
            ["Land", "Natural resources"], ["Labor", "Human effort"], ["Capital", "Tools and machinery"],
        ]),
    },
    "economics-g9-l5": {
        "data_table": table(["System", "Key Feature"], [
            ["Capitalism", "Private ownership and free markets"], ["Socialism", "Collective or state ownership"],
        ]),
    },
    "economics-g9-l7": {
        "data_table": table(["Law of Demand", "Meaning"], [
            ["Price up", "Quantity demanded down, all else equal"],
        ]),
    },
    "economics-g9-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Equilibrium price", "Where quantity supplied equals quantity demanded"],
        ]),
    },
    "economics-g9-l9": {
        "data_table": table(["Elasticity", "Meaning"], [
            ["Elastic demand", "Quantity demanded changes a lot with price"], ["Inelastic demand", "Quantity demanded changes little with price"],
        ]),
    },
    "economics-g9-l10": {
        "data_table": table(["Structure", "Example"], [
            ["Perfect competition", "Many small firms, identical products"], ["Monopoly", "One firm dominates the market"],
        ]),
    },
    "economics-g9-l11": {
        "data_table": table(["Feature", "Detail"], [
            ["Perfect competition", "Many buyers/sellers, no single firm controls price"],
        ]),
    },
    "economics-g9-l12": {
        "data_table": table(["Feature", "Detail"], [
            ["Monopoly", "A single seller controls the entire market"],
        ]),
    },
    "economics-g9-l13": {
        "data_table": table(["Flow", "Description"], [
            ["Circular flow of income", "Money moves between households and firms"],
        ]),
    },
    "economics-g9-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic growth", "An increase in a country's output of goods and services over time"],
        ]),
    },
    "economics-g9-l16": {
        "data_table": table(["Cause", "Example"], [
            ["Demand-pull inflation", "Too much demand chasing too few goods"],
        ]),
    },
    "economics-g9-l17": {
        "data_table": table(["Type", "Meaning"], [
            ["Cyclical unemployment", "Caused by economic downturns"], ["Structural unemployment", "Caused by a mismatch of skills"],
        ]),
    },
    "economics-g9-l18": {
        "data_table": table(["Tool", "Effect"], [
            ["Government spending", "Increases economic activity"], ["Taxation", "Reduces disposable income"],
        ]),
    },
    "economics-g9-l19": {
        "data_table": table(["Tool", "Effect"], [
            ["Interest rates", "Central banks adjust to influence borrowing and spending"],
        ]),
    },
    "economics-g9-l20": {
        "data_table": table(["Role", "Example"], [
            ["Setting interest rates", "Influences inflation and growth"],
        ]),
    },
    "economics-g9-l21": {
        "data_table": table(["Tax Type", "Example"], [
            ["Income tax", "Tax on earnings"], ["Sales tax", "Tax on purchases"],
        ]),
    },
    "economics-g9-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Budget deficit", "Government spends more than it collects in revenue"],
        ]),
    },
    "economics-g9-l23": {
        "data_table": table(["Good Type", "Example"], [
            ["Public good", "National defense, non-excludable and non-rivalrous"], ["Private good", "A sandwich, excludable and rivalrous"],
        ]),
    },
    "economics-g9-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Externality", "A cost or benefit affecting a third party not involved in a transaction"],
        ]),
    },
    "economics-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Import", "Goods bought from abroad"], ["Export", "Goods sold abroad"],
        ]),
    },
    "economics-g9-l26": {
        "data_table": table(["Concept", "Meaning"], [
            ["Comparative advantage", "Producing a good at a lower opportunity cost than others"],
        ]),
    },
    "economics-g9-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Exchange rate", "The value of one currency in terms of another"],
        ]),
    },
    "economics-g9-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Balance of payments", "A record of a country's transactions with the rest of the world"],
        ]),
    },
    "economics-g9-l29": {
        "data_table": table(["Indicator", "Measures"], [
            ["Human Development Index", "Health, education, and income combined"],
        ]),
    },
    "economics-g9-l30": {
        "data_table": table(["Economy Type", "Feature"], [
            ["Developed economy", "High income, industrialized"], ["Developing economy", "Lower income, industrializing"],
        ]),
    },
    "economics-g9-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Income inequality", "Uneven distribution of income across a population"],
        ]),
    },
    "economics-g9-l32": {
        "data_table": table(["Factor", "Effect on Wages"], [
            ["Supply and demand for labor", "Determines wage levels"],
        ]),
    },
    "economics-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneur", "A person who starts and runs a new business, taking on risk"],
        ]),
    },
    "economics-g9-l34": {
        "data_table": table(["Cost Type", "Example"], [
            ["Fixed cost", "Rent, doesn't change with output"], ["Variable cost", "Raw materials, changes with output"],
        ]),
    },
    "economics-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Economies of scale", "Cost advantages gained from larger production"],
        ]),
    },
    "economics-g9-l36": {
        "data_table": table(["Phase", "Description"], [
            ["Expansion", "Economic growth"], ["Recession", "Economic decline"],
        ]),
    },
    "economics-g9-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Recession", "A significant decline in economic activity lasting months or more"],
        ]),
    },
    "economics-g9-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock market", "A place where shares of companies are bought and sold"],
        ]),
    },
    "economics-g9-l39": {
        "data_table": table(["Factor", "Effect"], [
            ["Price", "Influences how much consumers buy"],
        ]),
    },
    "economics-g9-l40": {
        "data_table": table(["Motive", "Meaning"], [
            ["Profit motive", "Drives producers to supply goods and services"],
        ]),
    },
    "economics-g9-l41": {
        "data_table": table(["Control", "Effect"], [
            ["Price ceiling", "Maximum legal price, can cause shortages"], ["Price floor", "Minimum legal price, can cause surpluses"],
        ]),
    },
    "economics-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Subsidy", "Government financial support to lower production costs"],
        ]),
    },
    "economics-g9-l43": {
        "data_table": table(["Barrier", "Effect"], [
            ["Tariff", "A tax on imports that raises their price"],
        ]),
    },
    "economics-g9-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing economic integration between countries"],
        ]),
    },
    "economics-g9-l45": {
        "data_table": table(["Indicator", "Measures"], [
            ["GDP", "Total value of goods and services produced"], ["CPI", "Average change in prices consumers pay"],
        ]),
    },
    "economics-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Sustainable development", "Growth that meets present needs without harming future generations"],
        ]),
    },
    "economics-g9-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental economics", "Studies the economic impact of environmental policies"],
        ]),
    },
    "economics-g9-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Behavioral economics", "Studies psychological factors in economic decisions"],
        ]),
    },
    "economics-g9-l49": {
        "data_table": table(["Economist", "Idea"], [
            ["Adam Smith", "Father of modern economics, the 'invisible hand'"],
        ]),
    },
    "economics-g9-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptocurrency", "A digital currency secured by cryptography, e.g. Bitcoin"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Economics lessons (completing 50/50).")


if __name__ == "__main__":
    main()
