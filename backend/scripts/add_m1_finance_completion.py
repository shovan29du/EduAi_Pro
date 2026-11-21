#!/usr/bin/env python3
"""Depth pass, M1 Finance: fill in real, hand-checked data_table
content for the 119 M1 Finance lessons not covered by the earlier
breadth-first batch. Brings M1 Finance to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
valuation and M&A, behavioral finance, corporate finance theory,
fixed income and derivatives, risk management, personal and
institutional investing, and specialized/emerging finance topics;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Discounted cash flow", "Values an asset as the present value of its expected future cash flows"],
    ["Discount rate", "The rate used to convert future cash flows into today's value"],
])

CHARTS: dict[str, dict] = {
    "finance-m1-l1": {"data_table": table(["Method", "Approach"], [
        ["Valuation methods", "DCF, comparables, and precedent transactions estimate a company's worth from different angles"],
    ])},
    "finance-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral finance", "Studies how psychological biases cause investors to deviate from rational decision-making"],
    ])},
    "finance-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Comparable company analysis", "Values a company by benchmarking its multiples against similar public firms"],
    ])},
    "finance-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Precedent transaction analysis", "Values a company using multiples paid in comparable historical M&A deals"],
    ])},
    "finance-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Sum-of-the-parts valuation", "Values each business segment separately, then adds them together"],
    ])},
    "finance-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Private company valuation", "Adjusts standard valuation methods for illiquidity and lack of public market data"],
    ])},
    "finance-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["M&A valuation technique", "Combines standalone valuation with deal-specific factors like synergies and premiums"],
    ])},
    "finance-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Leveraged buyout", "Acquires a company primarily using borrowed money, repaid from its future cash flows"],
    ])},
    "finance-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Synergy valuation", "Estimates additional value created by combining two companies beyond their standalone worth"],
    ])},
    "finance-m1-l11": {"data_table": table(["Bias", "Effect"], [
        ["Overconfidence", "Overestimating one's own predictive accuracy"],
        ["Anchoring", "Relying too heavily on an initial reference point"],
    ])},
    "finance-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Loss aversion", "Losses are felt more painfully than equivalent gains are felt pleasurably"],
    ])},
    "finance-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Herding behavior", "Investors follow the crowd rather than independent analysis, amplifying market moves"],
    ])},
    "finance-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Market anomaly", "A persistent pattern in returns that standard efficient-market theory cannot fully explain"],
    ])},
    "finance-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Agency cost", "The cost arising when managers' interests diverge from shareholders' interests"],
    ])},
    "finance-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Exchange rate risk", "The risk that currency fluctuations affect the value of international investments"],
    ])},
    "finance-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Private equity / venture capital", "Invest in private companies at different stages, from startups to mature buyouts"],
    ])},
    "finance-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Fintech innovation", "Technology-driven changes reshaping how financial services are delivered"],
    ])},
    "finance-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["ESG investing", "Incorporates environmental, social, and governance criteria into investment decisions"],
    ])},
    "finance-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Capstone valuation project", "Integrates modeling, valuation, and analysis into one full financial project"],
    ])},
    "finance-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["CAPM", "Prices an asset's expected return based on its systematic risk (beta) relative to the market"],
    ])},
    "finance-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Fama-French model", "Extends CAPM with size and value factors (and later profitability/investment factors)"],
    ])},
    "finance-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Modigliani-Miller theorem", "In idealized markets, a firm's capital structure doesn't affect its total value"],
    ])},
    "finance-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Pecking order theory", "Firms prefer internal funds, then debt, then equity, in financing decisions"],
    ])},
    "finance-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["WACC", "Weighted Average Cost of Capital; blends the cost of debt and equity financing"],
    ])},
    "finance-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Dividend signaling", "A dividend change can signal management's private view of future prospects"],
    ])},
    "finance-m1-l27": {"data_table": table(["Approach", "Feature"], [
        ["Buybacks", "Flexible, tax-efficient in many jurisdictions"],
        ["Dividends", "Signal stable, reliable commitment to shareholders"],
    ])},
    "finance-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Cash conversion cycle", "Measures how long it takes a company to convert investments in inventory into cash"],
    ])},
    "finance-m1-l29": {"data_table": table(["Method", "Feature"], [
        ["NPV", "Sums discounted future cash flows minus initial investment"],
        ["IRR", "The discount rate at which a project's NPV equals zero"],
    ])},
    "finance-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Black-Scholes-Merton model", "Prices European options using volatility, time, and risk-free rate assumptions"],
    ])},
    "finance-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Binomial option pricing", "Values options using a discrete tree of possible up/down price movements"],
    ])},
    "finance-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Interest rate swap", "Exchanges fixed for floating interest payments between two parties"],
    ])},
    "finance-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Credit default swap", "A contract that transfers credit risk on a debt instrument to a third party"],
    ])},
    "finance-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Duration and convexity", "Measure a bond's price sensitivity to interest rate changes"],
    ])},
    "finance-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Yield curve", "Plots interest rates across different maturities, reflecting expectations about future rates"],
    ])},
    "finance-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Credit rating methodology", "Assesses a borrower's likelihood of default using financial and qualitative factors"],
    ])},
    "finance-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["CDO", "Collateralized Debt Obligation; pools debt into tranches with different risk/return profiles"],
    ])},
    "finance-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Securitization", "Pools loans (e.g. mortgages) into tradable securities backed by their cash flows"],
    ])},
    "finance-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Quality of earnings", "Assesses whether reported earnings reflect sustainable, cash-backed performance"],
    ])},
    "finance-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Forensic accounting", "Investigates financial records to detect fraud or misstatement"],
    ])},
    "finance-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Credit ratio analysis", "Uses financial ratios to assess a borrower's creditworthiness"],
    ])},
    "finance-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Altman Z-score", "Combines financial ratios into a single score predicting bankruptcy risk"],
    ])},
    "finance-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Three-statement model", "Links the income statement, balance sheet, and cash flow statement into one integrated model"],
    ])},
    "finance-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Sensitivity analysis", "Tests how a model's output changes as key assumptions are varied"],
    ])},
    "finance-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo simulation (finance)", "Runs many randomized scenarios to estimate the distribution of possible outcomes"],
    ])},
    "finance-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise risk management", "A framework for identifying and managing risk across an entire organization"],
    ])},
    "finance-m1-l47": {"data_table": table(["Metric", "Measures"], [
        ["Value at Risk", "The maximum expected loss at a given confidence level"],
        ["Expected shortfall", "The average loss in the worst-case tail beyond VaR"],
    ])},
    "finance-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Stress testing", "Evaluates how a financial institution would perform under severe hypothetical scenarios"],
    ])},
    "finance-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Basel III", "International regulatory standards setting bank capital adequacy requirements"],
    ])},
    "finance-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Asset-liability management", "Balances a bank's assets and liabilities to manage interest rate and liquidity risk"],
    ])},
    "finance-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Retirement income strategy", "Plans how to draw down savings to fund a sustainable income in retirement"],
    ])},
    "finance-m1-l52": {"data_table": table(["Type", "Purpose"], [
        ["Life insurance", "Provides income replacement for dependents after death"],
        ["Disability insurance", "Replaces income if the policyholder cannot work"],
    ])},
    "finance-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral retirement savings", "Studies why people under-save for retirement despite knowing they should save more"],
    ])},
    "finance-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Time value of money", "A dollar today is worth more than a dollar in the future due to its earning potential"],
    ])},
    "finance-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Education funding strategy", "Plans tax-advantaged savings vehicles to cover future education costs"],
    ])},
    "finance-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Mortgage refinancing", "Replaces an existing mortgage with a new one, often to secure a lower rate"],
    ])},
    "finance-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Credit score optimization", "Manages debt behavior to maximize a borrower's creditworthiness rating"],
    ])},
    "finance-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Modern portfolio theory", "Builds portfolios that maximize expected return for a given level of risk via diversification"],
    ])},
    "finance-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Life-cycle asset allocation", "Shifts a portfolio's risk level as an investor ages toward retirement"],
    ])},
    "finance-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Rebalancing strategy", "Periodically adjusts a portfolio back to its target asset allocation"],
    ])},
    "finance-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Tax-loss harvesting", "Sells losing investments to offset taxable gains elsewhere in a portfolio"],
    ])},
    "finance-m1-l62": {"data_table": table(["Factor", "Basis"], [
        ["Value / momentum / quality", "Systematic return premiums used to construct factor-based portfolios"],
    ])},
    "finance-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Index fund / ETF mechanics", "Track a benchmark's returns, ETFs trading intraday like a stock via creation/redemption"],
    ])},
    "finance-m1-l64": {"data_table": table(["Approach", "Claim"], [
        ["Active management", "Aims to beat the market via security selection"],
        ["Passive management", "Aims to match the market at lower cost"],
    ])},
    "finance-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Hedge fund strategy", "Uses varied approaches (long/short, macro, event-driven) seeking absolute returns"],
    ])},
    "finance-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Private debt / direct lending", "Non-bank lenders provide loans directly to companies outside public bond markets"],
    ])},
    "finance-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["REIT", "Real Estate Investment Trust; lets investors gain real estate exposure through publicly traded shares"],
    ])},
    "finance-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Commodities asset class", "Raw materials like oil and gold, often used for diversification and inflation hedging"],
    ])},
    "finance-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Currency hedging", "Reduces exposure to exchange rate movements in international portfolios"],
    ])},
    "finance-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Sovereign wealth fund", "A state-owned investment fund managing national savings, often from resource revenue"],
    ])},
    "finance-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Asset-liability matching (pensions)", "Aligns investment horizons with the timing of future pension obligations"],
    ])},
    "finance-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Actuarial methods", "Uses statistical models to estimate future pension liabilities and funding needs"],
    ])},
    "finance-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Distressed debt investing", "Buys debt of financially troubled companies, betting on recovery or restructuring value"],
    ])},
    "finance-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Spin-off / divestiture", "Separates a business unit into an independent company to unlock shareholder value"],
    ])},
    "finance-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["IPO process", "Underwriters help a private company sell shares to the public for the first time"],
    ])},
    "finance-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["SPAC", "Special Purpose Acquisition Company; a shell company that raises funds to merge with a private firm"],
    ])},
    "finance-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Dividend recapitalization", "A private equity portfolio company borrows to pay a special dividend to its owners"],
    ])},
    "finance-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Liquidation preference", "Determines the order and amount investors are paid before common shareholders in an exit"],
    ])},
    "finance-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Cap table", "Tracks a startup's ownership stakes across founders, employees, and investors"],
    ])},
    "finance-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Corporate treasury management", "Manages a company's cash, liquidity, and short-term financial risk"],
    ])},
    "finance-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Letter of credit", "A bank guarantee ensuring payment in international trade transactions"],
    ])},
    "finance-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain finance", "Lets suppliers get paid early using a buyer's stronger credit standing"],
    ])},
    "finance-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Cross-border M&A risk", "Currency, regulatory, and integration risks specific to international mergers"],
    ])},
    "finance-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Transfer pricing", "Sets prices for transactions between a multinational's own subsidiaries"],
    ])},
    "finance-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Corporate FX exposure management", "Hedges a company's revenue and cost exposure to currency fluctuations"],
    ])},
    "finance-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Sukuk / Islamic finance", "Structures returns as asset-backed profit-sharing to comply with a prohibition on interest"],
    ])},
    "finance-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral portfolio theory", "Models investors as holding mental layers of assets for different goals, not one optimal portfolio"],
    ])},
    "finance-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Robo-advisory", "Uses algorithms to automatically construct and rebalance client portfolios"],
    ])},
    "finance-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Dodd-Frank Act", "Post-2008 US financial reform expanding regulation of banks and derivatives markets"],
    ])},
    "finance-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Central bank digital currency", "A digital form of a country's official currency issued directly by its central bank"],
    ])},
    "finance-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Stablecoin", "A digital asset designed to maintain a stable value, often pegged to a fiat currency"],
    ])},
    "finance-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Family office governance", "Structures investment decision-making for a wealthy family's private capital"],
    ])},
    "finance-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Catastrophe bond", "Transfers insurance risk (e.g. hurricanes) to capital markets investors"],
    ])},
    "finance-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Convertible bond arbitrage", "Profits from mispricing between a convertible bond and its underlying stock"],
    ])},
    "finance-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Merger arbitrage", "Profits from the spread between a target's market price and the announced deal price"],
    ])},
    "finance-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Volatility risk premium", "Options tend to be priced with implied volatility exceeding realized volatility"],
    ])},
    "finance-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Repo / rehypothecation", "Short-term collateralized borrowing where the same collateral can be reused across transactions"],
    ])},
    "finance-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["CLO", "Collateralized Loan Obligation; pools corporate loans into risk-tranched securities"],
    ])},
    "finance-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Currency overlay", "Manages a portfolio's currency exposure separately from its underlying asset selection"],
    ])},
    "finance-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Advisor-client behavioral bias", "Studies how biases affect the advice financial advisors give and clients accept"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"finance-m1-l{base_n}"
    worked_key = f"finance-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Finance: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Finance lessons (completing 120/120).")


if __name__ == "__main__":
    main()
