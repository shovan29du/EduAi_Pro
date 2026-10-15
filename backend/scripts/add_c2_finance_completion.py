#!/usr/bin/env python3
"""Depth pass, C2 Finance: fill in real, hand-checked data_table/formulae
content for the 69 C2 Finance lessons not covered by the earlier
breadth-first batch. Brings C2 Finance to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "finance-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Time value of money", "A dollar today is worth more than a dollar in the future"],
        ]),
        "formulae": ["FV = PV * (1 + r) ** n"],
    },
    "finance-c2-l2": {
        "data_table": table(["Principle", "Meaning"], [
            ["Risk-return tradeoff", "Higher potential returns generally require accepting higher risk"],
        ]),
    },
    "finance-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Annuity", "A series of equal payments at regular intervals"], ["Perpetuity", "An annuity that continues indefinitely"],
        ]),
        "formulae": ["PV_perpetuity = PMT / r"],
    },
    "finance-c2-l5": {
        "data_table": table(["Component", "Detail"], [
            ["Amortization schedule", "Breaks each payment into principal and interest portions"],
        ]),
    },
    "finance-c2-l6": {
        "data_table": table(["Term", "Formula"], [
            ["NPV", "Sum of discounted cash flows minus initial investment"],
        ]),
        "formulae": ["NPV = sum(CF_t / (1 + r) ** t for t in years) - initial_investment"],
    },
    "finance-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["IRR", "The discount rate that makes NPV equal to zero"],
        ]),
        "formulae": ["NPV(IRR) = 0"],
    },
    "finance-c2-l8": {
        "data_table": table(["Step", "Purpose"], [
            ["Discounting future cash flows", "Converts future money into today's equivalent value"],
        ]),
    },
    "finance-c2-l9": {
        "data_table": table(["Measure", "Meaning"], [
            ["Standard deviation", "Measures the dispersion of returns around the mean"],
        ]),
    },
    "finance-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Risk premium", "Extra return demanded for taking on additional risk above the risk-free rate"],
        ]),
        "formulae": ["risk_premium = expected_return - risk_free_rate"],
    },
    "finance-c2-l11": {
        "data_table": table(["Type", "Meaning"], [
            ["Diversifiable risk", "Company-specific risk that can be reduced through diversification"], ["Non-diversifiable risk", "Market-wide risk that cannot be eliminated"],
        ]),
    },
    "finance-c2-l12": {
        "data_table": table(["Term", "Formula"], [
            ["CAPM", "Expected return = Rf + β(Rm - Rf)"],
        ]),
        "formulae": ["expected_return = risk_free_rate + beta * (market_return - risk_free_rate)"],
    },
    "finance-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Beta", "Measures an asset's volatility relative to the overall market"],
        ]),
    },
    "finance-c2-l14": {
        "data_table": table(["Term", "Formula"], [
            ["Expected return", "Sum of each outcome's probability times its return"],
        ]),
        "formulae": ["E_R = sum(p_i * r_i for p_i, r_i in outcomes)"],
    },
    "finance-c2-l15": {
        "data_table": table(["Rate Type", "Meaning"], [
            ["Nominal rate", "The stated interest rate, not adjusted for inflation"], ["Real rate", "The rate adjusted for inflation's effect on purchasing power"],
        ]),
    },
    "finance-c2-l16": {
        "data_table": table(["Frequency", "Effect"], [
            ["Monthly compounding", "Produces a higher effective rate than annual compounding at the same stated rate"],
        ]),
        "formulae": ["FV = PV * (1 + r/n) ** (n * t)"],
    },
    "finance-c2-l17": {
        "data_table": table(["Term", "Formula"], [
            ["Bond price", "Sum of discounted coupon payments plus discounted face value"],
        ]),
        "formulae": ["Price = sum(C / (1+r)**t for t in periods) + F / (1+r)**n"],
    },
    "finance-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Risk aversion", "A preference for lower-risk options even at the cost of lower expected return"],
        ]),
    },
    "finance-c2-l19": {
        "data_table": table(["Application", "Example"], [
            ["Retirement planning", "Using future value calculations to project savings growth over decades"],
        ]),
    },
    "finance-c2-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Sensitivity analysis", "Tests how a decision's outcome changes with different input assumptions"],
        ]),
    },
    "finance-c2-l21": {
        "data_table": table(["Rule", "Decision"], [
            ["NPV rule", "Accept a project if NPV > 0"], ["IRR rule", "Accept a project if IRR exceeds the required return"],
        ]),
    },
    "finance-c2-l22": {
        "data_table": table(["Term", "Formula"], [
            ["WACC", "Weighted average of the cost of equity and after-tax cost of debt"],
        ]),
        "formulae": ["WACC = (E/V) * Re + (D/V) * Rd * (1 - Tc)"],
    },
    "finance-c2-l23": {
        "data_table": table(["Proposition", "Statement"], [
            ["Modigliani-Miller I", "In a frictionless market, capital structure doesn't affect firm value"],
        ]),
    },
    "finance-c2-l24": {
        "data_table": table(["Theory", "Meaning"], [
            ["Signaling theory", "Dividend changes signal management's view of future prospects"],
        ]),
    },
    "finance-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["DCF modeling", "Values an asset based on the present value of its projected future cash flows"],
        ]),
    },
    "finance-c2-l26": {
        "data_table": table(["Method", "Meaning"], [
            ["Comparable company analysis", "Values a company by comparing valuation multiples of similar firms"],
        ]),
    },
    "finance-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Efficient frontier", "The set of portfolios offering the highest expected return for a given risk level"],
        ]),
    },
    "finance-c2-l28": {
        "data_table": table(["Application", "Example"], [
            ["Using CAPM", "Estimating a stock's required return based on its beta"],
        ]),
    },
    "finance-c2-l29": {
        "data_table": table(["Model", "Use"], [
            ["Black-Scholes model", "Prices European-style options based on volatility and time"],
        ]),
    },
    "finance-c2-l30": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Futures hedge", "Locks in a future price to reduce exposure to price volatility"],
        ]),
    },
    "finance-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Bond duration", "Measures a bond's price sensitivity to interest rate changes"], ["Convexity", "Measures the curvature of the price-yield relationship"],
        ]),
    },
    "finance-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Yield curve", "Plots bond yields against their maturities"],
        ]),
    },
    "finance-c2-l33": {
        "data_table": table(["Structure", "Feature"], [
            ["Stock deal", "Acquirer pays with its own shares"], ["Cash deal", "Acquirer pays with cash"],
        ]),
    },
    "finance-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Corporate restructuring", "Reorganizing a company's structure, operations, or finances"],
        ]),
    },
    "finance-c2-l35": {
        "data_table": table(["Term", "Formula"], [
            ["Cash conversion cycle", "Days inventory + days receivable - days payable"],
        ]),
        "formulae": ["CCC = DIO + DSO - DPO"],
    },
    "finance-c2-l36": {
        "data_table": table(["Component", "Formula"], [
            ["DuPont analysis", "ROE = Net margin × Asset turnover × Equity multiplier"],
        ]),
        "formulae": ["ROE = net_margin * asset_turnover * equity_multiplier"],
    },
    "finance-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Value at Risk", "Estimates the maximum expected loss over a time period at a confidence level"],
        ]),
    },
    "finance-c2-l38": {
        "data_table": table(["Term", "Example"], [
            ["Market bubble", "Asset prices rise well beyond fundamental value before collapsing"],
        ]),
    },
    "finance-c2-l39": {
        "data_table": table(["Strategy", "Purpose"], [
            ["Currency hedging", "Reduces exposure to exchange rate fluctuations"],
        ]),
    },
    "finance-c2-l40": {
        "data_table": table(["Theory", "Statement"], [
            ["Interest rate parity", "Interest rate differences between countries equal the expected exchange rate change"],
        ]),
    },
    "finance-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Leveraged buyout", "Acquiring a company primarily using borrowed funds"],
        ]),
    },
    "finance-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Term sheet", "Outlines the key terms of a venture capital investment before final agreement"],
        ]),
    },
    "finance-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Mortgage-backed security", "A bond backed by a pool of mortgage loans"],
        ]),
    },
    "finance-c2-l44": {
        "data_table": table(["Metric", "Formula"], [
            ["Cap rate", "Net operating income / property value"],
        ]),
        "formulae": ["cap_rate = NOI / property_value"],
    },
    "finance-c2-l45": {
        "data_table": table(["Consideration", "Detail"], [
            ["Social Security claiming age", "Affects the size of monthly retirement benefits"],
        ]),
    },
    "finance-c2-l46": {
        "data_table": table(["Tool", "Purpose"], [
            ["Trust", "Transfers assets while potentially reducing estate tax exposure"],
        ]),
    },
    "finance-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Credit risk model", "Estimates the probability a borrower will default on a debt"],
        ]),
    },
    "finance-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Basel Accords", "International banking regulations setting minimum capital requirements"],
        ]),
    },
    "finance-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Securities law", "Regulates the issuance and trading of financial securities"],
        ]),
    },
    "finance-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Monte Carlo simulation", "Models a range of outcomes using repeated random sampling"],
        ]),
    },
    "finance-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Decentralized finance", "Financial services built on blockchain without centralized intermediaries"],
        ]),
    },
    "finance-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["ESG investing", "Considers environmental, social, and governance factors in investment decisions"],
        ]),
    },
    "finance-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Agency theory", "Studies conflicts of interest between managers and shareholders"],
        ]),
    },
    "finance-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Pro forma statement", "A projected financial statement based on assumptions about the future"],
        ]),
    },
    "finance-c2-l55": {
        "data_table": table(["Strategy", "Example"], [
            ["Tax-loss harvesting", "Selling losing investments to offset capital gains taxes"],
        ]),
    },
    "finance-c2-l56": {
        "data_table": table(["Metric", "Meaning"], [
            ["Sharpe ratio", "Measures risk-adjusted return relative to a risk-free rate"],
        ]),
        "formulae": ["Sharpe = (portfolio_return - risk_free_rate) / portfolio_std_dev"],
    },
    "finance-c2-l57": {
        "data_table": table(["Crisis", "Cause"], [
            ["2008 financial crisis", "Subprime mortgage collapse and excessive leverage"],
        ]),
    },
    "finance-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Securitization", "Pooling financial assets and issuing new securities backed by them"],
        ]),
    },
    "finance-c2-l59": {
        "data_table": table(["Skill", "Application"], [
            ["Financial modeling in spreadsheets", "Building projections for valuation and decision-making"],
        ]),
    },
    "finance-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Building a portfolio plan", "Balances risk tolerance, time horizon, and diversification"],
        ]),
    },
    "finance-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Computing future value", "Projecting an investment's growth over 10 years at a fixed rate"],
        ]),
        "formulae": ["FV = PV * (1 + r) ** n"],
    },
    "finance-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Comparing two investments", "Weighing higher expected return against higher volatility"],
        ]),
    },
    "finance-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Solving for present value", "Finding today's value of a future lump sum payment"],
        ]),
        "formulae": ["PV = FV / (1 + r) ** n"],
    },
    "finance-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Valuing an annuity", "Calculating the present value of fixed monthly payments"],
        ]),
    },
    "finance-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Building an amortization table", "Tracking principal and interest across a loan's life"],
        ]),
    },
    "finance-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a project with NPV", "Deciding whether an investment adds value"],
        ]),
    },
    "finance-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing IRR across projects", "Ranking investment opportunities by return"],
        ]),
    },
    "finance-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Discounting a cash flow stream", "Valuing an uneven series of future payments"],
        ]),
    },
    "finance-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Measuring portfolio risk", "Calculating standard deviation of historical returns"],
        ]),
    },
    "finance-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Estimating a risk premium", "Comparing an asset's expected return against the risk-free rate"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Finance lessons (completing 70/70).")


if __name__ == "__main__":
    main()
