#!/usr/bin/env python3
"""Depth pass, C1 Finance: fill in real, hand-checked data_table
content for the 69 C1 Finance lessons not covered by the earlier
breadth-first batch. Brings C1 Finance to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "finance-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Personal finance", "Managing your own money: budgeting, saving, and investing"],
        ]),
    },
    "finance-c1-l2": {
        "data_table": table(["Statement", "Purpose"], [
            ["Balance sheet", "Shows assets, liabilities, and net worth"], ["Income statement", "Shows revenue and expenses over a period"],
        ]),
    },
    "finance-c1-l4": {
        "data_table": table(["Guideline", "Detail"], [
            ["Emergency fund", "Often recommended to cover 3-6 months of expenses"],
        ]),
    },
    "finance-c1-l5": {
        "data_table": table(["Factor", "Effect on Credit Score"], [
            ["Payment history", "Largest factor, on-time payments help"], ["Credit utilization", "Lower usage of available credit helps"],
        ]),
    },
    "finance-c1-l6": {
        "data_table": table(["Account Type", "Purpose"], [
            ["Checking account", "Everyday transactions"], ["Savings account", "Earning interest on deposits"],
        ]),
    },
    "finance-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Income tax", "A tax on earnings, used to fund public services"],
        ]),
    },
    "finance-c1-l8": {
        "data_table": table(["Type", "Formula"], [
            ["Simple interest", "I = P * r * t"], ["Compound interest", "A = P(1+r/n)^(nt)"],
        ]),
        "formulae": ["I = P * r * t", "A = P(1 + r/n)^(n*t)"],
    },
    "finance-c1-l9": {
        "data_table": table(["Insurance Type", "Covers"], [
            ["Health insurance", "Medical expenses"], ["Auto insurance", "Vehicle damage or liability"],
        ]),
    },
    "finance-c1-l10": {
        "data_table": table(["Account Type", "Feature"], [
            ["401(k)", "Employer-sponsored retirement account, often with matching"], ["IRA", "Individual retirement account"],
        ]),
    },
    "finance-c1-l11": {
        "data_table": table(["Component", "Meaning"], [
            ["Assets", "What a company owns"], ["Liabilities", "What a company owes"],
        ]),
    },
    "finance-c1-l12": {
        "data_table": table(["Component", "Meaning"], [
            ["Revenue", "Total income from sales"], ["Net income", "Profit after all expenses"],
        ]),
    },
    "finance-c1-l13": {
        "data_table": table(["Category", "Meaning"], [
            ["Operating activities", "Cash from core business operations"], ["Investing activities", "Cash from buying/selling assets"],
        ]),
    },
    "finance-c1-l14": {
        "data_table": table(["Ratio", "Formula"], [
            ["Current ratio", "Current assets / current liabilities"],
        ]),
        "formulae": ["Current ratio = Current assets / Current liabilities"],
    },
    "finance-c1-l15": {
        "data_table": table(["Strategy", "Benefit"], [
            ["Debt snowball", "Pays smallest debts first for psychological wins"], ["Debt avalanche", "Pays highest-interest debts first to save money"],
        ]),
    },
    "finance-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Inflation", "The general increase in prices over time, which reduces purchasing power"],
        ]),
    },
    "finance-c1-l17": {
        "data_table": table(["Goal Type", "Example"], [
            ["Short-term goal", "Saving for a vacation"], ["Long-term goal", "Saving for retirement"],
        ]),
    },
    "finance-c1-l18": {
        "data_table": table(["Warning Sign", "Reason"], [
            ["Pressure to act immediately", "Common tactic of financial scammers"],
        ]),
    },
    "finance-c1-l19": {
        "data_table": table(["Loan Type", "Feature"], [
            ["Mortgage", "Secured by real estate property"], ["Auto loan", "Secured by the vehicle"],
        ]),
    },
    "finance-c1-l20": {
        "data_table": table(["Tool", "Purpose"], [
            ["Budgeting app", "Tracks income and spending automatically"],
        ]),
    },
    "finance-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Corporate finance", "Managing a company's funding, capital structure, and investment decisions"],
        ]),
    },
    "finance-c1-l22": {
        "data_table": table(["Market Type", "Example"], [
            ["Primary market", "Where new securities are issued"], ["Secondary market", "Where existing securities are traded"],
        ]),
    },
    "finance-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Stock", "A share of ownership in a company"],
        ]),
    },
    "finance-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Bond", "A loan to a government or company that pays interest"],
        ]),
    },
    "finance-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Mutual fund", "A pooled investment managed by professionals"], ["ETF", "A fund that trades like a stock on an exchange"],
        ]),
    },
    "finance-c1-l26": {
        "data_table": table(["Principle", "Meaning"], [
            ["Diversification", "Spreading investments to reduce risk"],
        ]),
    },
    "finance-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Asset allocation", "Dividing investments among asset classes like stocks, bonds, and cash"],
        ]),
    },
    "finance-c1-l28": {
        "data_table": table(["Principle", "Meaning"], [
            ["Time value of money", "A dollar today is worth more than a dollar in the future"],
        ]),
        "formulae": ["PV = FV / (1 + r)^n"],
    },
    "finance-c1-l29": {
        "data_table": table(["Step", "Purpose"], [
            ["Set goals", "Provides direction for a financial plan"],
        ]),
    },
    "finance-c1-l30": {
        "data_table": table(["Method", "Description"], [
            ["Discounted cash flow", "Values a business based on projected future cash flows"],
        ]),
    },
    "finance-c1-l31": {
        "data_table": table(["Term", "Formula"], [
            ["Working capital", "Current assets - current liabilities"],
        ]),
        "formulae": ["Working capital = Current assets - Current liabilities"],
    },
    "finance-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Capital budgeting", "Evaluating long-term investment decisions for a company"],
        ]),
    },
    "finance-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Cost of capital", "The return required to justify a capital investment"],
        ]),
    },
    "finance-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Dividend", "A portion of company profits paid to shareholders"],
        ]),
    },
    "finance-c1-l35": {
        "data_table": table(["Type", "Description"], [
            ["Merger", "Two companies combine into one"], ["Acquisition", "One company buys another"],
        ]),
    },
    "finance-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["IPO", "Initial Public Offering, when a private company first sells shares to the public"],
        ]),
    },
    "finance-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Foreign exchange market", "The global marketplace for trading currencies"],
        ]),
    },
    "finance-c1-l38": {
        "data_table": table(["Instrument", "Description"], [
            ["Option", "The right, not obligation, to buy/sell at a set price"], ["Futures contract", "An obligation to buy/sell at a set future price"],
        ]),
    },
    "finance-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["REIT", "Real Estate Investment Trust, allows investing in property without direct ownership"],
        ]),
    },
    "finance-c1-l40": {
        "data_table": table(["Example", "Type"], [
            ["Gold, oil", "Commodities traded on exchanges"],
        ]),
    },
    "finance-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Behavioral finance", "Studies psychological factors influencing financial decisions"],
        ]),
    },
    "finance-c1-l42": {
        "data_table": table(["Factor", "Purpose"], [
            ["Credit analysis", "Assesses a borrower's ability to repay debt"],
        ]),
    },
    "finance-c1-l43": {
        "data_table": table(["Account Type", "Feature"], [
            ["Brokerage account", "Used to buy and sell securities"],
        ]),
    },
    "finance-c1-l44": {
        "data_table": table(["Statement", "Use"], [
            ["Income statement", "Assesses profitability over time"],
        ]),
    },
    "finance-c1-l45": {
        "data_table": table(["Ratio", "Use"], [
            ["Price-to-earnings ratio", "Compares stock price to earnings per share"],
        ]),
    },
    "finance-c1-l46": {
        "data_table": table(["Principle", "Meaning"], [
            ["Risk management", "Identifying and mitigating potential financial losses"],
        ]),
    },
    "finance-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Insurance", "A contract that provides financial protection against loss"],
        ]),
    },
    "finance-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Estate planning", "Preparing for the transfer of assets after death"],
        ]),
    },
    "finance-c1-l49": {
        "data_table": table(["Concept", "Reason"], [
            ["Start early", "More time for compound growth before retirement"],
        ]),
    },
    "finance-c1-l50": {
        "data_table": table(["Option", "Detail"], [
            ["Scholarships", "Do not need to be repaid"], ["Student loans", "Must be repaid, usually with interest"],
        ]),
    },
    "finance-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Small business financing", "Funding options like loans, grants, and investors for a new business"],
        ]),
    },
    "finance-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Venture capital", "Investment in early-stage, high-growth startups"], ["Private equity", "Investment in established private companies"],
        ]),
    },
    "finance-c1-l53": {
        "data_table": table(["Body", "Role"], [
            ["SEC", "Regulates US securities markets"],
        ]),
    },
    "finance-c1-l54": {
        "data_table": table(["Role", "Example"], [
            ["Central bank", "Sets interest rate policy to influence the economy"],
        ]),
    },
    "finance-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Revolving debt", "Debt like credit cards where you can carry a balance and pay interest"],
        ]),
    },
    "finance-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Student loan", "Borrowed money used to pay for education, repaid later"],
        ]),
    },
    "finance-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Fintech", "Technology-driven innovation in financial services"],
        ]),
    },
    "finance-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["ESG investing", "Investing based on Environmental, Social, and Governance criteria"],
        ]),
    },
    "finance-c1-l59": {
        "data_table": table(["Warning Sign", "Reason"], [
            ["Inconsistent numbers", "Common indicator of financial statement fraud"],
        ]),
    },
    "finance-c1-l60": {
        "data_table": table(["Formula", "Meaning"], [
            ["Net worth = Assets - Liabilities", "Measures overall financial position"],
        ]),
        "formulae": ["Net worth = Assets - Liabilities"],
    },
    "finance-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Building a starter budget", "Allocating income across needs, wants, and savings"],
        ]),
    },
    "finance-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Reading a company's balance sheet", "Identifying whether a business has more assets than liabilities"],
        ]),
    },
    "finance-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Building a monthly budget", "Tracking income against fixed and variable expenses"],
        ]),
    },
    "finance-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Sizing an emergency fund", "Calculating 3-6 months of expenses for a sample household"],
        ]),
    },
    "finance-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Reading a credit report", "Identifying factors that could be improved to raise a score"],
        ]),
    },
    "finance-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a bank account", "Comparing fees and interest rates across account types"],
        ]),
    },
    "finance-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Estimating a tax bill", "Applying a simplified tax bracket to sample income"],
        ]),
    },
    "finance-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing loan offers", "Calculating total interest paid at different rates"],
        ]),
    },
    "finance-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Comparing insurance policies", "Weighing premium cost against coverage level"],
        ]),
    },
    "finance-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Projecting retirement savings", "Estimating account growth from regular 401(k) contributions"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Finance lessons (completing 70/70).")


if __name__ == "__main__":
    main()
