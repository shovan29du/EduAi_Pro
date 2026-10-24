#!/usr/bin/env python3
"""Depth pass, Grade 8 Finance: fill in real, hand-checked data_table
content for the 38 Grade 8 Finance lessons not covered by the earlier
breadth-first batch. Brings Grade 8 Finance to full 40/40 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade8_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade8.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "finance-g8-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Income", "Money earned"], ["Wages", "Payment for hourly or salaried work"],
        ]),
    },
    "finance-g8-l3": {
        "data_table": table(["Budget Category", "Example Allocation"], [
            ["Needs", "50% of income"], ["Wants", "30% of income"], ["Savings", "20% of income"],
        ]),
    },
    "finance-g8-l4": {
        "data_table": table(["Savings Goal", "Example"], [
            ["Short-term", "Save for a bike in 3 months"], ["Long-term", "Save for college"],
        ]),
    },
    "finance-g8-l5": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term", "Save $50 this month"], ["Long-term", "Save $2000 for a car"],
        ]),
    },
    "finance-g8-l6": {
        "data_table": table(["Account Type", "Purpose"], [
            ["Checking account", "Everyday spending"], ["Savings account", "Earning interest over time"],
        ]),
    },
    "finance-g8-l7": {
        "data_table": table(["Interest Type", "Formula"], [
            ["Simple interest", "I = P x R x T"], ["Compound interest", "A = P(1 + r)^t"],
        ]),
    },
    "finance-g8-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Credit", "Borrowing money with a promise to repay"],
        ]),
    },
    "finance-g8-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Debt", "Money owed to another party"], ["Borrowing", "Taking a loan to be repaid later"],
        ]),
    },
    "finance-g8-l11": {
        "data_table": table(["Card Type", "How It Works"], [
            ["Debit card", "Draws directly from your bank balance"], ["Credit card", "Borrows money to repay later"],
        ]),
    },
    "finance-g8-l12": {
        "data_table": table(["Loan Term", "Meaning"], [
            ["Principal", "The original amount borrowed"], ["Repayment", "Paying back the loan over time"],
        ]),
    },
    "finance-g8-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Interest rate on a loan", "The cost of borrowing, expressed as a percentage"],
        ]),
    },
    "finance-g8-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Investing", "Putting money into assets with the goal of growth"],
        ]),
    },
    "finance-g8-l15": {
        "data_table": table(["Investment", "Description"], [
            ["Stock", "A share of ownership in a company"], ["Bond", "A loan to a company or government"],
        ]),
    },
    "finance-g8-l16": {
        "data_table": table(["Concept", "Meaning"], [
            ["Risk", "The chance of losing value"], ["Return", "The gain or loss on an investment"],
        ]),
    },
    "finance-g8-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Diversification", "Spreading investments to reduce risk"],
        ]),
    },
    "finance-g8-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Retirement savings", "Money set aside for use after working years"],
        ]),
    },
    "finance-g8-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Income tax", "Tax collected on money earned"],
        ]),
    },
    "finance-g8-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Sales tax", "Tax added to the price of goods and services"],
        ]),
    },
    "finance-g8-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Insurance", "Payment to protect against future financial loss"],
        ]),
    },
    "finance-g8-l22": {
        "data_table": table(["Insurance Type", "Covers"], [
            ["Health insurance", "Medical costs"], ["Auto insurance", "Vehicle damage or accidents"],
        ]),
    },
    "finance-g8-l23": {
        "data_table": table(["Warning Sign", "Example"], [
            ["Unsolicited requests for personal info", "A common scam tactic"],
        ]),
    },
    "finance-g8-l24": {
        "data_table": table(["Payment Method", "Description"], [
            ["Online banking", "Managing accounts via the internet"], ["Digital wallet", "Stores payment info on a device"],
        ]),
    },
    "finance-g8-l25": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Comparing prices", "Finds the best value"],
        ]),
    },
    "finance-g8-l26": {
        "data_table": table(["Term", "Example"], [
            ["Need", "Food, water, shelter"], ["Want", "A toy, video game"],
        ]),
    },
    "finance-g8-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Emergency fund", "Money set aside for unexpected expenses"],
        ]),
    },
    "finance-g8-l28": {
        "data_table": table(["Paycheck Item", "Meaning"], [
            ["Gross pay", "Total earnings before deductions"], ["Net pay", "Take-home pay after deductions"],
        ]),
    },
    "finance-g8-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Entrepreneurship", "Starting and running a business to earn money"],
        ]),
    },
    "finance-g8-l30": {
        "data_table": table(["Cost Type", "Example"], [
            ["Tuition", "Direct cost of education"], ["Scholarship", "Reduces the cost of education"],
        ]),
    },
    "finance-g8-l31": {
        "data_table": table(["Loan Type", "Example Use"], [
            ["Auto loan", "Buying a car"], ["Mortgage", "Buying a home"],
        ]),
    },
    "finance-g8-l32": {
        "data_table": table(["Option", "Trade-off"], [
            ["Renting", "Lower upfront cost, no ownership"], ["Buying", "Builds equity, higher upfront cost"],
        ]),
    },
    "finance-g8-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Inflation", "A general rise in prices over time, reducing purchasing power"],
        ]),
    },
    "finance-g8-l34": {
        "data_table": table(["Record", "Purpose"], [
            ["Receipts", "Proof of purchase"], ["Bank statements", "Track account activity"],
        ]),
    },
    "finance-g8-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Charitable giving", "Donating money or resources to causes"],
        ]),
    },
    "finance-g8-l36": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Waiting 24 hours before buying", "Reduces impulse purchases"],
        ]),
    },
    "finance-g8-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Contract", "A legally binding agreement between parties"],
        ]),
    },
    "finance-g8-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer-to-peer payment", "Sending money directly between individuals digitally"],
        ]),
    },
    "finance-g8-l39": {
        "data_table": table(["Habit", "Benefit"], [
            ["Tracking spending", "Builds awareness of money habits"],
        ]),
    },
    "finance-g8-l40": {
        "data_table": table(["Trade-off", "Example"], [
            ["Spend now vs save later", "Buying a game today vs saving for something bigger"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade8.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 8 Finance lessons (completing 40/40).")


if __name__ == "__main__":
    main()
