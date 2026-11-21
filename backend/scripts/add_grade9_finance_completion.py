#!/usr/bin/env python3
"""Depth pass, Grade 9 Finance: fill in real, hand-checked data_table
content for the 48 Grade 9 Finance lessons not covered by the earlier
breadth-first batch. Brings Grade 9 Finance to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade9_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade9.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fin-g9-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Savings account", "A bank account that earns interest on deposits"],
        ]),
    },
    "finance-g9-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Budget", "A plan for how to spend and save money"],
        ]),
    },
    "finance-g9-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Income", "Money received, e.g. from a job"], ["Expenses", "Money spent"],
        ]),
    },
    "finance-g9-l4": {
        "data_table": table(["Category", "Example"], [
            ["Need", "Housing, food"], ["Want", "Video games, entertainment"],
        ]),
    },
    "finance-g9-l5": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term goal", "Saving for a phone"], ["Long-term goal", "Saving for college"],
        ]),
    },
    "finance-g9-l6": {
        "data_table": table(["Account Type", "Purpose"], [
            ["Checking account", "Everyday transactions"], ["Savings account", "Earning interest on deposits"],
        ]),
    },
    "finance-g9-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Interest rate", "The cost of borrowing money or the return on savings, as a percentage"],
        ]),
    },
    "finance-g9-l9": {
        "data_table": table(["Card Type", "How It Works"], [
            ["Debit card", "Spends money directly from your account"], ["Credit card", "Borrows money to be repaid later"],
        ]),
    },
    "finance-g9-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Loan", "Money borrowed that must be repaid, usually with interest"],
        ]),
    },
    "finance-g9-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Debt", "Money owed to another party"],
        ]),
    },
    "finance-g9-l13": {
        "data_table": table(["Strategy", "Reason"], [
            ["Pay more than the minimum", "Reduces debt faster and saves on interest"],
        ]),
    },
    "finance-g9-l14": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Pay yourself first", "Prioritizes savings before spending"],
        ]),
    },
    "finance-g9-l15": {
        "data_table": table(["Guideline", "Detail"], [
            ["Emergency fund", "Often recommended to cover 3-6 months of expenses"],
        ]),
    },
    "finance-g9-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Investing", "Putting money into assets expecting a return over time"],
        ]),
    },
    "finance-g9-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock", "A share of ownership in a company"],
        ]),
    },
    "finance-g9-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Bond", "A loan to a government or company that pays interest"],
        ]),
    },
    "finance-g9-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Mutual fund", "A pooled investment managed by professionals"],
        ]),
    },
    "finance-g9-l20": {
        "data_table": table(["Principle", "Meaning"], [
            ["Risk-return tradeoff", "Higher potential returns usually come with higher risk"],
        ]),
    },
    "finance-g9-l21": {
        "data_table": table(["Principle", "Meaning"], [
            ["Diversification", "Spreading investments to reduce risk"],
        ]),
    },
    "finance-g9-l22": {
        "data_table": table(["Concept", "Reason"], [
            ["Start early", "More time for compound growth before retirement"],
        ]),
    },
    "finance-g9-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Insurance", "A contract that provides financial protection against loss"],
        ]),
    },
    "finance-g9-l24": {
        "data_table": table(["Insurance Type", "Covers"], [
            ["Health insurance", "Medical expenses"], ["Auto insurance", "Vehicle damage or liability"],
        ]),
    },
    "finance-g9-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Income tax", "A tax on earnings, used to fund public services"],
        ]),
    },
    "finance-g9-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Gross pay", "Earnings before deductions"], ["Net pay", "Earnings after deductions"],
        ]),
    },
    "finance-g9-l27": {
        "data_table": table(["Warning Sign", "Reason"], [
            ["Pressure to act immediately", "Common tactic of scammers"],
        ]),
    },
    "finance-g9-l28": {
        "data_table": table(["Practice", "Reason"], [
            ["Monitor account statements", "Helps catch identity theft early"],
        ]),
    },
    "finance-g9-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["E-wallet", "A digital app that stores payment information"],
        ]),
    },
    "finance-g9-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptocurrency", "A digital asset secured by cryptography"],
        ]),
    },
    "finance-g9-l31": {
        "data_table": table(["Practice", "Reason"], [
            ["Save before buying", "Avoids interest costs of financing"],
        ]),
    },
    "finance-g9-l32": {
        "data_table": table(["Option", "Tradeoff"], [
            ["Renting", "More flexibility, no equity built"], ["Buying", "Builds equity, less flexibility"],
        ]),
    },
    "finance-g9-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Student loan", "Borrowed money used to pay for education, repaid later"],
        ]),
    },
    "finance-g9-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Cost of living", "The amount of money needed to cover basic expenses in an area"],
        ]),
    },
    "finance-g9-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Inflation", "The general increase in prices over time, which reduces purchasing power"],
        ]),
    },
    "finance-g9-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Currency exchange", "Converting one country's money into another's"],
        ]),
    },
    "finance-g9-l37": {
        "data_table": table(["Practice", "Reason"], [
            ["Keeping receipts and records", "Helps with budgeting and tax filing"],
        ]),
    },
    "finance-g9-l38": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comparison shopping", "Finds the best price before purchasing"],
        ]),
    },
    "finance-g9-l39": {
        "data_table": table(["Practice", "Reason"], [
            ["Read the fine print", "Avoids unexpected fees or terms"],
        ]),
    },
    "finance-g9-l40": {
        "data_table": table(["Fact", "Detail"], [
            ["Credit card interest", "Charged on unpaid balances, can compound quickly"],
        ]),
    },
    "finance-g9-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Financial independence", "Having enough resources to live without relying on a paycheck"],
        ]),
    },
    "finance-g9-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Philanthropy", "Voluntary giving to help others, e.g. through donations"],
        ]),
    },
    "finance-g9-l43": {
        "data_table": table(["Practice", "Reason"], [
            ["Separate business and personal finances", "Keeps accurate records"],
        ]),
    },
    "finance-g9-l44": {
        "data_table": table(["Deduction", "Purpose"], [
            ["Tax withholding", "Prepays income tax owed"],
        ]),
    },
    "finance-g9-l45": {
        "data_table": table(["Step", "Purpose"], [
            ["Compare options", "Leads to better financial decisions"],
        ]),
    },
    "finance-g9-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Opportunity cost", "What you give up by choosing one option over another"],
        ]),
    },
    "finance-g9-l47": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Researching fair prices", "Strengthens your negotiating position"],
        ]),
    },
    "finance-g9-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Document the incident", "Supports an insurance claim"],
        ]),
    },
    "finance-g9-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer-to-peer payment app", "Software for sending money directly between individuals"],
        ]),
    },
    "finance-g9-l50": {
        "data_table": table(["Strategy", "Reason"], [
            ["Wait 24 hours before buying", "Reduces impulsive, unplanned purchases"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade9.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 9 Finance lessons (completing 50/50).")


if __name__ == "__main__":
    main()
