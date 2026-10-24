#!/usr/bin/env python3
"""Depth pass, Grade 10 Economics: fill in real, hand-checked
data_table content for the Grade 10 Economics lessons not covered by
the earlier breadth-first batch. Brings Grade 10 Economics to full
50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "econ-g10-l1": {
        "data_table": table(["Indicator", "Measures"], [
            ["GDP", "Total value of goods and services produced"], ["Inflation", "Rate of price increase over time"], ["Unemployment", "Share of the labor force without work"],
        ]),
    },
    "economics-g10-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Scarcity", "Limited resources relative to unlimited wants"],
        ]),
    },
    "economics-g10-l3": {
        "data_table": table(["Category", "Example"], [
            ["Need", "Housing, food"], ["Want", "Entertainment"],
        ]),
    },
    "economics-g10-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Opportunity cost", "The value of the next best alternative given up"],
        ]),
    },
    "economics-g10-l5": {
        "data_table": table(["Factor", "Example"], [
            ["Land", "Natural resources"], ["Labor", "Human effort"], ["Capital", "Tools and machinery"],
        ]),
    },
    "economics-g10-l6": {
        "data_table": table(["Law of Demand", "Meaning"], [
            ["Price up", "Quantity demanded down, all else equal"],
        ]),
    },
    "economics-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Equilibrium price", "Where quantity supplied equals quantity demanded"],
        ]),
    },
    "economics-g10-l8": {
        "data_table": table(["System", "Key Feature"], [
            ["Capitalism", "Private ownership and free markets"], ["Socialism", "Collective or state ownership"],
        ]),
    },
    "economics-g10-l9": {
        "data_table": table(["Concept", "Meaning"], [
            ["Consumer choice", "How individuals allocate limited income across goods"],
        ]),
    },
    "economics-g10-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Production", "The process of combining inputs to create goods and services"],
        ]),
    },
    "economics-g10-l11": {
        "data_table": table(["Elasticity", "Meaning"], [
            ["Elastic demand", "Quantity demanded changes a lot with price"], ["Inelastic demand", "Quantity demanded changes little with price"],
        ]),
    },
    "economics-g10-l12": {
        "data_table": table(["Elasticity", "Meaning"], [
            ["Elastic supply", "Quantity supplied responds strongly to price changes"],
        ]),
    },
    "economics-g10-l13": {
        "data_table": table(["Feature", "Detail"], [
            ["Perfect competition", "Many buyers/sellers, no single firm controls price"],
        ]),
    },
    "economics-g10-l15": {
        "data_table": table(["Structure", "Feature"], [
            ["Oligopoly", "A market dominated by a few large firms"],
        ]),
    },
    "economics-g10-l16": {
        "data_table": table(["Role", "Example"], [
            ["Regulation", "Government sets rules to correct market failures"],
        ]),
    },
    "economics-g10-l17": {
        "data_table": table(["Tax Type", "Example"], [
            ["Income tax", "Tax on earnings"], ["Sales tax", "Tax on purchases"],
        ]),
    },
    "economics-g10-l18": {
        "data_table": table(["Good Type", "Example"], [
            ["Public good", "National defense, non-excludable and non-rivalrous"], ["Externality", "A cost/benefit affecting a third party"],
        ]),
    },
    "economics-g10-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Market failure", "When markets fail to allocate resources efficiently"],
        ]),
    },
    "economics-g10-l21": {
        "data_table": table(["Barrier", "Effect"], [
            ["Tariff", "A tax on imports that raises their price"], ["Quota", "A limit on the quantity that can be imported"],
        ]),
    },
    "economics-g10-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Exchange rate", "The value of one currency in terms of another"],
        ]),
    },
    "economics-g10-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Balance of payments", "A record of a country's transactions with the rest of the world"],
        ]),
    },
    "economics-g10-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic growth", "An increase in a country's output over time"],
        ]),
    },
    "economics-g10-l25": {
        "data_table": table(["Indicator", "Measures"], [
            ["HDI", "Health, education, and income combined"],
        ]),
    },
    "economics-g10-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Income inequality", "Uneven distribution of income across a population"],
        ]),
    },
    "economics-g10-l27": {
        "data_table": table(["Phase", "Description"], [
            ["Expansion", "Economic growth"], ["Recession", "Economic decline"],
        ]),
    },
    "economics-g10-l28": {
        "data_table": table(["Tool", "Effect"], [
            ["Government spending", "Increases economic activity"], ["Taxation", "Reduces disposable income"],
        ]),
    },
    "economics-g10-l29": {
        "data_table": table(["Role", "Example"], [
            ["Setting interest rates", "Central banks influence inflation and growth"],
        ]),
    },
    "economics-g10-l30": {
        "data_table": table(["Effect", "Direction"], [
            ["Interest rates up", "Borrowing costs rise, spending tends to fall"],
        ]),
    },
    "economics-g10-l31": {
        "data_table": table(["Cause", "Example"], [
            ["Demand-pull inflation", "Too much demand chasing too few goods"],
        ]),
    },
    "economics-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Deflation", "A sustained decrease in the general price level"],
        ]),
    },
    "economics-g10-l33": {
        "data_table": table(["Type", "Meaning"], [
            ["Cyclical unemployment", "Caused by economic downturns"], ["Structural unemployment", "Caused by a mismatch of skills"],
        ]),
    },
    "economics-g10-l34": {
        "data_table": table(["Factor", "Effect on Wages"], [
            ["Supply and demand for labor", "Determines wage levels"],
        ]),
    },
    "economics-g10-l35": {
        "data_table": table(["Role", "Function"], [
            ["Commercial banks", "Accept deposits and lend money"],
        ]),
    },
    "economics-g10-l36": {
        "data_table": table(["Function of Money", "Example"], [
            ["Medium of exchange", "Used to buy and sell goods"], ["Store of value", "Holds value over time"],
        ]),
    },
    "economics-g10-l37": {
        "data_table": table(["Indicator", "Measures"], [
            ["GDP", "Total economic output"], ["CPI", "Average change in consumer prices"],
        ]),
    },
    "economics-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing economic integration between countries"],
        ]),
    },
    "economics-g10-l39": {
        "data_table": table(["Economy Type", "Feature"], [
            ["Developed economy", "High income, industrialized"], ["Developing economy", "Lower income, industrializing"],
        ]),
    },
    "economics-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Sustainable development", "Growth that meets present needs without harming future generations"],
        ]),
    },
    "economics-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental economics", "Studies the economic impact of environmental policies"],
        ]),
    },
    "economics-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Behavioural economics", "Studies psychological factors in economic decisions"],
        ]),
    },
    "economics-g10-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneurship", "Starting and running a business, taking on risk for potential profit"],
        ]),
    },
    "economics-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The network moving goods from producer to consumer"],
        ]),
    },
    "economics-g10-l45": {
        "data_table": table(["Sector", "Example"], [
            ["Primary", "Farming"], ["Secondary", "Manufacturing"], ["Tertiary", "Services"],
        ]),
    },
    "economics-g10-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Cooperative", "A business owned and run jointly by its members"],
        ]),
    },
    "economics-g10-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock market", "A place where shares of companies are bought and sold"],
        ]),
    },
    "economics-g10-l48": {
        "data_table": table(["Right", "Example"], [
            ["Right to a refund", "Consumer protection against faulty goods"],
        ]),
    },
    "economics-g10-l49": {
        "data_table": table(["Flow", "Description"], [
            ["Circular flow of income", "Money moves between households and firms"],
        ]),
    },
    "economics-g10-l50": {
        "data_table": table(["System", "Example Country"], [
            ["Mixed economy", "Combines market and government intervention, e.g. most modern economies"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Economics lessons (completing 50/50).")


if __name__ == "__main__":
    main()
