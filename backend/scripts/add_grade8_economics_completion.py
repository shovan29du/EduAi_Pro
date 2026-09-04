#!/usr/bin/env python3
"""Depth pass, Grade 8 Economics: fill in real, hand-checked data_table
content for the 38 Grade 8 Economics lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Economics to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "econ-g8-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Economics", "The study of how people use limited resources"],
        ]),
    },
    "economics-g8-l2": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "economics-g8-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Scarcity", "Limited resources relative to unlimited wants"], ["Choice", "Deciding how to use scarce resources"],
        ]),
    },
    "economics-g8-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Opportunity cost", "The value of the next best alternative given up"],
        ]),
    },
    "economics-g8-l5": {
        "data_table": table(["Factor of Production", "Example"], [
            ["Land", "Natural resources"], ["Labor", "Human work"], ["Capital", "Tools and machinery"],
        ]),
    },
    "economics-g8-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Market equilibrium", "The price where supply equals demand"],
        ]),
    },
    "economics-g8-l8": {
        "data_table": table(["System", "Description"], [
            ["Market economy", "Prices set by supply and demand"], ["Command economy", "Government controls production"],
        ]),
    },
    "economics-g8-l9": {
        "data_table": table(["Role", "Example"], [
            ["Regulation", "Setting rules for fair business"], ["Public goods", "Providing roads and defense"],
        ]),
    },
    "economics-g8-l10": {
        "data_table": table(["Flow", "Direction"], [
            ["Money", "Households to businesses for goods/services"],
            ["Resources", "Households to businesses as labor and capital"],
        ]),
    },
    "economics-g8-l11": {
        "data_table": table(["Market Type", "Description"], [
            ["Perfect competition", "Many sellers, similar products"], ["Monopoly", "A single seller controls the market"],
        ]),
    },
    "economics-g8-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Price elasticity", "How much quantity demanded changes when price changes"],
        ]),
    },
    "economics-g8-l13": {
        "data_table": table(["Role", "Example"], [
            ["Producer", "A farmer growing crops"], ["Consumer", "A shopper buying groceries"],
        ]),
    },
    "economics-g8-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Specialization", "Focusing on producing one thing efficiently"],
            ["Division of labor", "Splitting a task among different workers"],
        ]),
    },
    "economics-g8-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Comparative advantage", "Producing something at a lower opportunity cost than others"],
        ]),
    },
    "economics-g8-l16": {
        "data_table": table(["Function of Money", "Example"], [
            ["Medium of exchange", "Buying goods"], ["Store of value", "Saving for later"],
        ]),
    },
    "economics-g8-l17": {
        "data_table": table(["System", "Description"], [
            ["Barter", "Trading goods directly without money"], ["Money economy", "Trading using a medium of exchange"],
        ]),
    },
    "economics-g8-l18": {
        "data_table": table(["Institution", "Role"], [
            ["Central bank", "Manages a country's money supply"], ["Commercial bank", "Holds deposits, gives loans"],
        ]),
    },
    "economics-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Interest rate", "The cost of borrowing money, or return on savings"],
        ]),
    },
    "economics-g8-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["GDP", "The total value of goods and services produced in a country"],
        ]),
    },
    "economics-g8-l22": {
        "data_table": table(["Unemployment Type", "Cause"], [
            ["Cyclical", "Economic downturns"], ["Structural", "Skills mismatch"],
        ]),
    },
    "economics-g8-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic growth", "An increase in a country's production of goods and services over time"],
        ]),
    },
    "economics-g8-l24": {
        "data_table": table(["Phase", "Description"], [
            ["Expansion", "Economic growth"], ["Recession", "Economic decline"],
        ]),
    },
    "economics-g8-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax", "Money collected by government to fund public services"],
        ]),
    },
    "economics-g8-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Public good", "A good available to everyone, like a road"],
            ["Externality", "A side effect of an economic activity affecting others"],
        ]),
    },
    "economics-g8-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneurship", "Starting and running a new business"],
        ]),
    },
    "economics-g8-l28": {
        "data_table": table(["Business Type", "Description"], [
            ["Sole proprietorship", "Owned by one person"], ["Corporation", "Owned by shareholders"],
        ]),
    },
    "economics-g8-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Wage", "Payment for labor"], ["Labor market", "Where workers and employers meet"],
        ]),
    },
    "economics-g8-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Tariff", "A tax on imported goods"],
        ]),
    },
    "economics-g8-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Exchange rate", "The value of one currency in terms of another"],
        ]),
    },
    "economics-g8-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Globalization", "Increasing connection between countries through trade and communication"],
        ]),
    },
    "economics-g8-l33": {
        "data_table": table(["Indicator", "Measures"], [
            ["GDP", "Total economic output"], ["Unemployment rate", "Percentage without jobs seeking work"],
        ]),
    },
    "economics-g8-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Income inequality", "Uneven distribution of income across a population"],
        ]),
    },
    "economics-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Economic development", "Improvement in a country's economic well-being over time"],
        ]),
    },
    "economics-g8-l36": {
        "data_table": table(["Resource Type", "Example"], [
            ["Renewable", "Solar, wind"], ["Nonrenewable", "Coal, oil"],
        ]),
    },
    "economics-g8-l37": {
        "data_table": table(["Right", "Example"], [
            ["Right to a refund", "For a defective product"], ["Right to accurate information", "Truthful advertising"],
        ]),
    },
    "economics-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply chain", "The steps from raw materials to finished product to consumer"],
        ]),
    },
    "economics-g8-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock", "A share of ownership in a company"],
        ]),
    },
    "economics-g8-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Behavioral economics", "The study of how psychology affects economic decisions"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Economics lessons (completing 40/40).")


if __name__ == "__main__":
    main()
