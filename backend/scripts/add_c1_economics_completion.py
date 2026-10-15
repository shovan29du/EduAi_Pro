#!/usr/bin/env python3
"""Depth pass, C1 Economics: fill in real, hand-checked data_table
content for the 69 C1 Economics lessons not covered by the earlier
breadth-first batch. Brings C1 Economics to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "economics-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Economics", "The study of how people allocate scarce resources"],
        ]),
    },
    "economics-c1-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic model", "A simplified representation used to analyze behavior"],
        ]),
    },
    "economics-c1-l4": {
        "data_table": table(["Concept", "Meaning"], [
            ["Comparative advantage", "Producing a good at a lower opportunity cost than others"],
        ]),
    },
    "economics-c1-l5": {
        "data_table": table(["Concept", "Meaning"], [
            ["Prices as signals", "Prices communicate information about scarcity and value"],
        ]),
    },
    "economics-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Consumer surplus", "Difference between what buyers are willing to pay and what they pay"], ["Producer surplus", "Difference between price received and minimum sellers would accept"],
        ]),
    },
    "economics-c1-l7": {
        "data_table": table(["Cost Type", "Example"], [
            ["Fixed cost", "Rent, doesn't change with output"], ["Variable cost", "Raw materials, changes with output"],
        ]),
    },
    "economics-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Money supply", "The total amount of currency and liquid assets in an economy"],
        ]),
    },
    "economics-c1-l9": {
        "data_table": table(["Indicator", "Measures"], [
            ["CPI", "Average change in prices consumers pay over time"],
        ]),
    },
    "economics-c1-l10": {
        "data_table": table(["Concept", "Meaning"], [
            ["Opportunity cost", "The value of the next best alternative given up"],
        ]),
    },
    "economics-c1-l11": {
        "data_table": table(["Type", "Meaning"], [
            ["Positive economics", "Describes what is, based on facts"], ["Normative economics", "Prescribes what should be, based on values"],
        ]),
    },
    "economics-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Production possibilities frontier", "Shows the maximum combinations of two goods an economy can produce"],
        ]),
    },
    "economics-c1-l13": {
        "data_table": table(["Flow", "Description"], [
            ["Circular flow of income", "Money moves between households and firms"],
        ]),
    },
    "economics-c1-l14": {
        "data_table": table(["System", "Key Feature"], [
            ["Market economy", "Prices and production driven by supply and demand"], ["Command economy", "Government controls production"],
        ]),
    },
    "economics-c1-l15": {
        "data_table": table(["Determinant", "Effect on Demand"], [
            ["Income", "Higher income can increase demand for normal goods"], ["Consumer preferences", "Shifts demand up or down"],
        ]),
    },
    "economics-c1-l16": {
        "data_table": table(["Determinant", "Effect on Supply"], [
            ["Input costs", "Higher costs reduce supply"], ["Technology", "Better technology increases supply"],
        ]),
    },
    "economics-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Equilibrium price", "Where quantity supplied equals quantity demanded"], ["Shortage", "Quantity demanded exceeds quantity supplied"],
        ]),
    },
    "economics-c1-l18": {
        "data_table": table(["Control", "Effect"], [
            ["Price ceiling (rent control)", "Maximum legal price, can cause housing shortages"],
        ]),
    },
    "economics-c1-l19": {
        "data_table": table(["Control", "Effect"], [
            ["Price floor (minimum wage)", "Minimum legal price, can cause labor surplus (unemployment)"],
        ]),
    },
    "economics-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Market failure", "When markets fail to allocate resources efficiently"],
        ]),
    },
    "economics-c1-l21": {
        "data_table": table(["Type", "Example"], [
            ["Negative externality", "Pollution from a factory affecting nearby residents"], ["Positive externality", "Vaccination benefiting public health"],
        ]),
    },
    "economics-c1-l22": {
        "data_table": table(["Good Type", "Example"], [
            ["Public good", "National defense, non-excludable and non-rivalrous"],
        ]),
    },
    "economics-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax incidence", "Who actually bears the economic burden of a tax"],
        ]),
    },
    "economics-c1-l24": {
        "data_table": table(["Tool", "Effect"], [
            ["Government spending", "Increases economic activity"], ["Taxation", "Reduces disposable income"],
        ]),
    },
    "economics-c1-l25": {
        "data_table": table(["Tool", "Effect"], [
            ["Interest rates", "Central banks adjust to influence borrowing and spending"],
        ]),
    },
    "economics-c1-l26": {
        "data_table": table(["Role", "Example"], [
            ["Setting interest rates", "Central banks influence inflation and growth"],
        ]),
    },
    "economics-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["GDP", "Total value of goods and services produced in a country"],
        ]),
    },
    "economics-c1-l28": {
        "data_table": table(["Type", "Meaning"], [
            ["Nominal GDP", "Measured at current prices"], ["Real GDP", "Adjusted for inflation"],
        ]),
    },
    "economics-c1-l29": {
        "data_table": table(["Type", "Meaning"], [
            ["Cyclical unemployment", "Caused by economic downturns"], ["Structural unemployment", "Caused by a mismatch of skills"],
        ]),
    },
    "economics-c1-l30": {
        "data_table": table(["Cause", "Example"], [
            ["Demand-pull inflation", "Too much demand chasing too few goods"],
        ]),
    },
    "economics-c1-l31": {
        "data_table": table(["Phase", "Description"], [
            ["Expansion", "Economic growth"], ["Recession", "Economic decline"],
        ]),
    },
    "economics-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Import", "Goods bought from abroad"], ["Export", "Goods sold abroad"],
        ]),
    },
    "economics-c1-l33": {
        "data_table": table(["Barrier", "Effect"], [
            ["Tariff", "A tax on imports that raises their price"], ["Quota", "A limit on the quantity that can be imported"],
        ]),
    },
    "economics-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Exchange rate", "The value of one currency in terms of another"],
        ]),
    },
    "economics-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Balance of payments", "A record of a country's transactions with the rest of the world"],
        ]),
    },
    "economics-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic growth", "An increase in a country's output over time"],
        ]),
    },
    "economics-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Human capital", "The skills, education, and knowledge of a workforce"],
        ]),
    },
    "economics-c1-l38": {
        "data_table": table(["Measure", "Meaning"], [
            ["Poverty line", "The minimum income needed to meet basic needs"],
        ]),
    },
    "economics-c1-l39": {
        "data_table": table(["Feature", "Detail"], [
            ["Perfect competition", "Many buyers/sellers, no single firm controls price"],
        ]),
    },
    "economics-c1-l40": {
        "data_table": table(["Feature", "Detail"], [
            ["Monopoly", "A single seller controls the entire market"],
        ]),
    },
    "economics-c1-l41": {
        "data_table": table(["Structure", "Feature"], [
            ["Oligopoly", "A market dominated by a few large firms"],
        ]),
    },
    "economics-c1-l42": {
        "data_table": table(["Structure", "Feature"], [
            ["Monopolistic competition", "Many firms selling differentiated products"],
        ]),
    },
    "economics-c1-l43": {
        "data_table": table(["Factor", "Effect on Wages"], [
            ["Supply and demand for labor", "Determines wage levels"],
        ]),
    },
    "economics-c1-l44": {
        "data_table": table(["Position", "Argument"], [
            ["For minimum wage", "Raises income for low-wage workers"], ["Against", "May reduce employment for entry-level jobs"],
        ]),
    },
    "economics-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Behavioral economics", "Studies psychological factors in economic decisions"],
        ]),
    },
    "economics-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Game theory", "Studies strategic decision-making between interacting agents"],
        ]),
    },
    "economics-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Asymmetric information", "One party in a transaction has more information than the other"],
        ]),
    },
    "economics-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Environmental economics", "Studies the economic impact of environmental policies"],
        ]),
    },
    "economics-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Development economics", "Studies economic growth and quality of life in developing countries"],
        ]),
    },
    "economics-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Public choice theory", "Applies economic analysis to political decision-making"],
        ]),
    },
    "economics-c1-l51": {
        "data_table": table(["Role", "Function"], [
            ["Commercial banks", "Accept deposits and lend money"],
        ]),
    },
    "economics-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock market", "A place where shares of companies are bought and sold"],
        ]),
    },
    "economics-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Bond", "A loan to a government or company that pays interest"],
        ]),
    },
    "economics-c1-l54": {
        "data_table": table(["Fact", "Detail"], [
            ["Federal Reserve", "The central bank of the United States, founded 1913"],
        ]),
    },
    "economics-c1-l55": {
        "data_table": table(["Indicator", "Measures"], [
            ["GDP", "Total economic output"], ["Unemployment rate", "Share of labor force without work"],
        ]),
    },
    "economics-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["National income accounting", "The system of measuring a nation's total economic output"],
        ]),
    },
    "economics-c1-l57": {
        "data_table": table(["Era", "Feature"], [
            ["Mercantilism", "16th-18th century, favored trade surpluses"], ["Capitalism", "Private ownership and free markets"],
        ]),
    },
    "economics-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptocurrency", "A digital currency secured by cryptography, e.g. Bitcoin"],
        ]),
    },
    "economics-c1-l59": {
        "data_table": table(["Method", "Use"], [
            ["Economic forecasting", "Predicting future economic conditions using models and data"],
        ]),
    },
    "economics-c1-l60": {
        "data_table": table(["Bias", "Effect"], [
            ["Anchoring bias", "Over-relying on the first piece of price information seen"],
        ]),
    },
    "economics-c1-l61": {
        "data_table": table(["Good Type", "Example"], [
            ["Public good", "Streetlights, non-excludable and non-rivalrous"],
        ]),
    },
    "economics-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing scarcity", "Comparing how a country allocates limited healthcare resources"],
        ]),
    },
    "economics-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Plotting supply and demand", "Finding the equilibrium price for a product from a data table"],
        ]),
    },
    "economics-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Applying an economic model", "Using the PPF to show a trade-off between two goods"],
        ]),
    },
    "economics-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Finding comparative advantage", "Determining which of two countries should specialize in which good"],
        ]),
    },
    "economics-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a price change", "Predicting how a price increase changes buyer and seller behavior"],
        ]),
    },
    "economics-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Calculating surplus", "Finding consumer and producer surplus from a supply-demand graph"],
        ]),
    },
    "economics-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing production costs", "Distinguishing fixed and variable costs for a small business"],
        ]),
    },
    "economics-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Tracing money supply effects", "Analyzing how a central bank's actions affect lending"],
        ]),
    },
    "economics-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Comparing cost of living", "Using CPI data to compare purchasing power across years"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Economics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
