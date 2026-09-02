#!/usr/bin/env python3
"""Depth pass, Grade 10 Finance: fill in real, hand-checked data_table
content for the Grade 10 Finance lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Finance to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "fin-g10-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Investing", "Putting money into assets expecting a return over time"],
        ]),
    },
    "finance-g10-l2": {
        "data_table": table(["Function of Money", "Example"], [
            ["Medium of exchange", "Used to buy and sell goods"], ["Store of value", "Holds value over time"],
        ]),
    },
    "finance-g10-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Budget", "A plan for how to spend and save money"],
        ]),
    },
    "finance-g10-l4": {
        "data_table": table(["Category", "% of Income (common guideline)"], [
            ["Needs", "50%"], ["Wants", "30%"], ["Savings", "20%"],
        ]),
    },
    "finance-g10-l5": {
        "data_table": table(["Category", "Example"], [
            ["Need", "Housing, food"], ["Want", "Entertainment"],
        ]),
    },
    "finance-g10-l6": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Pay yourself first", "Prioritizes savings before spending"],
        ]),
    },
    "finance-g10-l7": {
        "data_table": table(["Account Type", "Purpose"], [
            ["Checking account", "Everyday transactions"], ["Savings account", "Earning interest on deposits"],
        ]),
    },
    "finance-g10-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Credit card", "Borrows money to be repaid later, often with interest if unpaid"],
        ]),
    },
    "finance-g10-l11": {
        "data_table": table(["Debt Type", "Example"], [
            ["Good debt", "A mortgage or student loan that builds value"], ["Bad debt", "High-interest credit card debt on depreciating purchases"],
        ]),
    },
    "finance-g10-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Loan", "Money borrowed that must be repaid, usually with interest"],
        ]),
    },
    "finance-g10-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Mortgage", "A loan used to purchase property, secured by the property itself"],
        ]),
    },
    "finance-g10-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Insurance", "A contract that provides financial protection against loss"],
        ]),
    },
    "finance-g10-l15": {
        "data_table": table(["Insurance Type", "Covers"], [
            ["Health insurance", "Medical expenses"], ["Auto insurance", "Vehicle damage or liability"], ["Life insurance", "Payout to beneficiaries upon death"],
        ]),
    },
    "finance-g10-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Payroll deduction", "An amount withheld from a paycheck, e.g. for tax"],
        ]),
    },
    "finance-g10-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Tax form", "A document used to report income and calculate tax owed"],
        ]),
    },
    "finance-g10-l18": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term goal", "Saving for a phone"], ["Long-term goal", "Saving for college"],
        ]),
    },
    "finance-g10-l19": {
        "data_table": table(["Guideline", "Detail"], [
            ["Emergency fund", "Often recommended to cover 3-6 months of expenses"],
        ]),
    },
    "finance-g10-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Inflation", "The general increase in prices over time, which reduces purchasing power"],
        ]),
    },
    "finance-g10-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock market", "A place where shares of companies are bought and sold"],
        ]),
    },
    "finance-g10-l22": {
        "data_table": table(["Type", "Meaning"], [
            ["Stock", "A share of ownership in a company"], ["Bond", "A loan to a government or company that pays interest"],
        ]),
    },
    "finance-g10-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Index fund", "A fund that tracks a market index, offering broad diversification"],
        ]),
    },
    "finance-g10-l24": {
        "data_table": table(["Principle", "Meaning"], [
            ["Risk-return tradeoff", "Higher potential returns usually come with higher risk"],
        ]),
    },
    "finance-g10-l25": {
        "data_table": table(["Principle", "Meaning"], [
            ["Diversification", "Spreading investments to reduce risk"],
        ]),
    },
    "finance-g10-l26": {
        "data_table": table(["Account Type", "Purpose"], [
            ["Retirement account", "Tax-advantaged savings for retirement"],
        ]),
    },
    "finance-g10-l27": {
        "data_table": table(["Formula", "Use"], [
            ["A = P(1+r/n)^(nt)", "Compound interest"],
        ]),
        "formulae": ["A = P(1 + r/n)^(n*t)"],
    },
    "finance-g10-l28": {
        "data_table": table(["Statement", "Purpose"], [
            ["Balance sheet", "Shows assets, liabilities, and net worth at a point in time"],
        ]),
    },
    "finance-g10-l29": {
        "data_table": table(["Practice", "Reason"], [
            ["Monitor account statements", "Helps catch identity theft early"],
        ]),
    },
    "finance-g10-l30": {
        "data_table": table(["Warning Sign", "Reason"], [
            ["Promises of guaranteed high returns", "A common sign of a Ponzi scheme"],
        ]),
    },
    "finance-g10-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Mobile banking", "Managing bank accounts through a smartphone app"],
        ]),
    },
    "finance-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Cryptocurrency", "A digital asset secured by cryptography, e.g. Bitcoin"],
        ]),
    },
    "finance-g10-l33": {
        "data_table": table(["Practice", "Reason"], [
            ["Read the fine print", "Avoids unexpected fees or terms in contracts"],
        ]),
    },
    "finance-g10-l34": {
        "data_table": table(["Right", "Example"], [
            ["Right to a refund", "Consumer protection against faulty goods or services"],
        ]),
    },
    "finance-g10-l35": {
        "data_table": table(["Practice", "Benefit"], [
            ["Comparison shopping", "Finds the best price before purchasing"],
        ]),
    },
    "finance-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Buying on credit", "Total cost often exceeds the sticker price due to interest"],
        ]),
    },
    "finance-g10-l37": {
        "data_table": table(["Step", "Purpose"], [
            ["Save before buying", "Avoids interest costs of financing a large purchase"],
        ]),
    },
    "finance-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Net income", "Take-home pay after taxes and deductions"],
        ]),
    },
    "finance-g10-l39": {
        "data_table": table(["Step", "Purpose"], [
            ["Set goals", "Provides direction for a personal financial plan"],
        ]),
    },
    "finance-g10-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Charitable giving", "Voluntarily donating money or resources to help others"],
        ]),
    },
    "finance-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Startup capital", "Initial funds needed to launch a business"],
        ]),
    },
    "finance-g10-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Business loan", "Borrowed capital used to fund business operations or growth"],
        ]),
    },
    "finance-g10-l43": {
        "data_table": table(["Practice", "Reason"], [
            ["Compare exchange rates", "Gets better value when converting currency abroad"],
        ]),
    },
    "finance-g10-l44": {
        "data_table": table(["Institution", "Feature"], [
            ["Bank", "For-profit financial institution"], ["Credit union", "Member-owned, not-for-profit"],
        ]),
    },
    "finance-g10-l45": {
        "data_table": table(["Role", "Example"], [
            ["Setting interest rates", "A central bank tool that affects loans and savings"],
        ]),
    },
    "finance-g10-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Lifestyle inflation", "Spending more as income rises, rather than saving the difference"],
        ]),
    },
    "finance-g10-l47": {
        "data_table": table(["Formula", "Meaning"], [
            ["Net worth = Assets - Liabilities", "Measures overall financial position"],
        ]),
        "formulae": ["Net worth = Assets - Liabilities"],
    },
    "finance-g10-l48": {
        "data_table": table(["Option", "Detail"], [
            ["Scholarships", "Do not need to be repaid"], ["Student loans", "Must be repaid, usually with interest"],
        ]),
    },
    "finance-g10-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Peer-to-peer lending", "Individuals lend directly to borrowers through an online platform"],
        ]),
    },
    "finance-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Ethical investing", "Choosing investments based on social or environmental values"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Finance lessons (completing 50/50).")


if __name__ == "__main__":
    main()
