#!/usr/bin/env python3
"""Depth pass, C2 Economics: fill in real, hand-checked data_table
content for the 69 C2 Economics lessons not covered by the earlier
breadth-first batch. Brings C2 Economics to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "economics-c2-l1": {
        "data_table": table(["Term", "Formula"], [
            ["Price elasticity of demand", "%ΔQuantity / %ΔPrice"],
        ]),
        "formulae": ["PED = pct_change_quantity / pct_change_price"],
    },
    "economics-c2-l2": {
        "data_table": table(["Structure", "Feature"], [
            ["Perfect competition", "Many small firms, identical products"], ["Monopoly", "A single seller dominates the market"],
        ]),
    },
    "economics-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Marginal cost", "The cost of producing one additional unit"],
        ]),
    },
    "economics-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Marginal revenue product", "The additional revenue from hiring one more worker"],
        ]),
    },
    "economics-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Externality", "A cost or benefit affecting a party who didn't choose to incur it"],
        ]),
    },
    "economics-c2-l7": {
        "data_table": table(["Curve", "Shows"], [
            ["Aggregate demand", "Total spending in the economy at each price level"], ["Aggregate supply", "Total output producers offer at each price level"],
        ]),
    },
    "economics-c2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Financial system", "Channels savings into productive investment"],
        ]),
    },
    "economics-c2-l9": {
        "data_table": table(["Metric", "Meaning"], [
            ["Gini coefficient", "Measures income inequality on a scale from 0 to 1"],
        ]),
    },
    "economics-c2-l10": {
        "data_table": table(["Era", "Feature"], [
            ["Industrialization", "Shift from agrarian to manufacturing-based economies"], ["Globalization", "Increasing economic interconnection across nations"],
        ]),
    },
    "economics-c2-l11": {
        "data_table": table(["Term", "Formula"], [
            ["Price elasticity of demand", "%ΔQd / %ΔP"],
        ]),
        "formulae": ["PED = (pct_change_Qd) / (pct_change_P)"],
    },
    "economics-c2-l12": {
        "data_table": table(["Elasticity Type", "Meaning"], [
            ["Cross-price elasticity", "Measures how demand for one good responds to another good's price"], ["Income elasticity", "Measures how demand responds to income changes"],
        ]),
    },
    "economics-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Utility maximization", "Consumers choose the combination of goods maximizing satisfaction given a budget"],
        ]),
    },
    "economics-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["General equilibrium", "A state where supply equals demand simultaneously across all markets"],
        ]),
    },
    "economics-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Pareto efficiency", "An allocation where no one can be made better off without making someone worse off"],
        ]),
    },
    "economics-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Nash equilibrium", "A state where no player benefits from changing strategy unilaterally"],
        ]),
    },
    "economics-c2-l17": {
        "data_table": table(["Concept", "Meaning"], [
            ["Prisoner's dilemma", "Illustrates why rational individual choices can lead to worse collective outcomes"],
        ]),
    },
    "economics-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Price discrimination", "Charging different prices to different customers for the same good"],
        ]),
    },
    "economics-c2-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Natural monopoly", "A market where one firm can supply the whole market more efficiently than multiple firms"],
        ]),
    },
    "economics-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Cartel", "A group of firms colluding to restrict output and raise prices"],
        ]),
    },
    "economics-c2-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Contestable market", "A market with low entry/exit barriers that disciplines pricing even with few firms"],
        ]),
    },
    "economics-c2-l22": {
        "data_table": table(["Term", "Formula"], [
            ["Spending multiplier", "1 / (1 - MPC)"],
        ]),
        "formulae": ["multiplier = 1 / (1 - MPC)"],
    },
    "economics-c2-l23": {
        "data_table": table(["Curve", "Represents"], [
            ["IS curve", "Combinations of interest rate and output where goods market is in equilibrium"], ["LM curve", "Combinations where money market is in equilibrium"],
        ]),
    },
    "economics-c2-l24": {
        "data_table": table(["Curve", "Shows"], [
            ["Phillips curve", "The inverse relationship between inflation and unemployment"],
        ]),
    },
    "economics-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Rational expectations", "Economic agents use all available information to form unbiased predictions"],
        ]),
    },
    "economics-c2-l26": {
        "data_table": table(["School", "Focus"], [
            ["Monetarism", "Emphasizes controlling the money supply to manage the economy"], ["Keynesianism", "Emphasizes active fiscal policy to manage demand"],
        ]),
    },
    "economics-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Quantitative easing", "A central bank purchases assets to inject money into the economy"],
        ]),
    },
    "economics-c2-l28": {
        "data_table": table(["Regime", "Feature"], [
            ["Fixed exchange rate", "Currency value pegged to another currency or asset"], ["Floating exchange rate", "Currency value determined by market forces"],
        ]),
    },
    "economics-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Purchasing power parity", "Exchange rates should adjust so identical goods cost the same across countries"],
        ]),
    },
    "economics-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Mundell-Fleming model", "Extends IS-LM to an open economy with capital mobility"],
        ]),
    },
    "economics-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Heckscher-Ohlin model", "Countries export goods that intensively use their abundant factors of production"],
        ]),
    },
    "economics-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Strategic trade theory", "Government intervention can shift competitive advantage to domestic firms"],
        ]),
    },
    "economics-c2-l33": {
        "data_table": table(["Term", "Example"], [
            ["Trade bloc", "European Union"], ["Common market", "Allows free movement of goods, services, capital, and labor"],
        ]),
    },
    "economics-c2-l34": {
        "data_table": table(["Term", "Formula"], [
            ["Solow growth model", "Output growth driven by capital, labor, and technology"],
        ]),
    },
    "economics-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Endogenous growth theory", "Technological progress is driven by internal economic factors like R&D"],
        ]),
    },
    "economics-c2-l36": {
        "data_table": table(["Factor", "Effect"], [
            ["Strong property rights", "Encourages investment and long-term economic development"],
        ]),
    },
    "economics-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Human capital", "The skills, education, and experience that make workers more productive"],
        ]),
    },
    "economics-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Efficiency wage", "Paying above-market wages to boost worker productivity and retention"],
        ]),
    },
    "economics-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Optimal taxation", "Balances revenue generation against minimizing economic distortion"],
        ]),
    },
    "economics-c2-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Comparing costs and benefits", "Determines whether a public policy is worth pursuing"],
        ]),
    },
    "economics-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Cap-and-trade", "Sets an emissions limit and allows trading of permits within that cap"],
        ]),
    },
    "economics-c2-l42": {
        "data_table": table(["Theorem", "Statement"], [
            ["Coase theorem", "With clear property rights and low transaction costs, parties can resolve externalities through bargaining"],
        ]),
    },
    "economics-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Prospect theory", "People value gains and losses differently, weighting losses more heavily"],
        ]),
    },
    "economics-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Nudge", "A subtle design choice that influences behavior without restricting choice"],
        ]),
    },
    "economics-c2-l45": {
        "data_table": table(["Term", "Example"], [
            ["Adverse selection", "Buyers of insurance who need it most are most likely to purchase it"], ["Moral hazard", "Insured parties take on more risk once protected from consequences"],
        ]),
    },
    "economics-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Signaling", "Sending a costly, credible signal to convey hidden information"],
        ]),
    },
    "economics-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Regression analysis", "Estimates the relationship between economic variables using data"],
        ]),
    },
    "economics-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Time series analysis", "Studies economic data points collected over successive time intervals"],
        ]),
    },
    "economics-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Poverty trap", "A self-reinforcing mechanism keeping households in persistent poverty"],
        ]),
    },
    "economics-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Microfinance", "Small loans to entrepreneurs lacking access to traditional banking"],
        ]),
    },
    "economics-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Efficient market hypothesis", "Asset prices fully reflect all available information"],
        ]),
    },
    "economics-c2-l52": {
        "data_table": table(["Term", "Example"], [
            ["Market anomaly", "A pattern that contradicts the efficient market hypothesis"],
        ]),
    },
    "economics-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Fractional reserve banking", "Banks hold only a fraction of deposits, lending out the rest"],
        ]),
        "formulae": ["money_multiplier = 1 / reserve_ratio"],
    },
    "economics-c2-l54": {
        "data_table": table(["Crisis", "Cause"], [
            ["2008 financial crisis", "Subprime mortgage defaults triggered a broader credit crisis"],
        ]),
    },
    "economics-c2-l55": {
        "data_table": table(["Era", "Feature"], [
            ["The Great Depression", "1930s global economic collapse marked by mass unemployment"],
        ]),
    },
    "economics-c2-l56": {
        "data_table": table(["Event", "Cause"], [
            ["2008 financial crisis", "Housing bubble collapse and overleveraged financial institutions"],
        ]),
    },
    "economics-c2-l57": {
        "data_table": table(["System", "Feature"], [
            ["Capitalism", "Private ownership and market-driven pricing"], ["Socialism", "Collective or state ownership of production"],
        ]),
    },
    "economics-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Lorenz curve", "Graphically shows the distribution of income across a population"],
        ]),
    },
    "economics-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Rent-seeking", "Seeking wealth through manipulating the economic environment rather than production"],
        ]),
    },
    "economics-c2-l60": {
        "data_table": table(["Step", "Purpose"], [
            ["Applying a macro model to policy", "Evaluating a real fiscal or monetary proposal's likely effects"],
        ]),
    },
    "economics-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Applying endogenous growth theory", "Assessing how R&D investment drives long-run growth"],
        ]),
    },
    "economics-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Calculating elasticity", "Determining if a good is elastic or inelastic from price and quantity data"],
        ]),
    },
    "economics-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Comparing market structures", "Contrasting pricing behavior in monopoly versus competition"],
        ]),
    },
    "economics-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Graphing consumer choice", "Finding the optimal bundle where budget line meets indifference curve"],
        ]),
    },
    "economics-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a cost curve", "Identifying the output level minimizing average total cost"],
        ]),
    },
    "economics-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing wage determination", "Explaining a wage change using supply and demand for labor"],
        ]),
    },
    "economics-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Applying Coase theorem logic", "Analyzing a pollution dispute resolved through bargaining"],
        ]),
    },
    "economics-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Shifting AD/AS curves", "Predicting price and output effects of an economic shock"],
        ]),
    },
    "economics-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing savings and investment", "Tracing how interest rates affect loanable funds"],
        ]),
    },
    "economics-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting inequality data", "Reading a Gini coefficient in context"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Economics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
