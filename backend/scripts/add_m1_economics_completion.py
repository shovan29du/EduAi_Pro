#!/usr/bin/env python3
"""Depth pass, M1 Economics: fill in real, hand-checked data_table
content for the 119 M1 Economics lessons not covered by the earlier
breadth-first batch. Brings M1 Economics to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
microeconomic and macroeconomic theory, econometrics, economic
historiography, law and economics, economic geography, and history
of economic crises and thought; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["General equilibrium", "A state where supply equals demand simultaneously across all markets"],
    ["Consumer choice theory", "Models how consumers allocate limited income to maximize utility"],
])

CHARTS: dict[str, dict] = {
    "economics-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Development economics", "Studies the economic conditions and policies that drive growth in poorer countries"],
    ])},
    "economics-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Econometrics", "Applies statistical methods to test economic theories against real-world data"],
    ])},
    "economics-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic optimization (growth theory)", "Models how agents choose consumption and investment over time to maximize welfare"],
    ])},
    "economics-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["GMM", "Generalized Method of Moments; an estimator using theoretical moment conditions rather than a full likelihood"],
    ])},
    "economics-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Contract theory", "Studies how parties design agreements under asymmetric information and incentive conflicts"],
    ])},
    "economics-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Repeated games / bargaining", "Studies how cooperation and negotiated outcomes emerge from ongoing strategic interaction"],
    ])},
    "economics-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Search and matching", "Models how workers and jobs find each other in a labor market with frictions"],
    ])},
    "economics-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Optimal taxation", "Studies how to design taxes that raise revenue while minimizing economic distortion"],
    ])},
    "economics-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Structural econometrics", "Estimates parameters of an explicit economic model, including discrete-choice behavior"],
    ])},
    "economics-m1-l11": {"data_table": table(["Economist", "Contribution"], [
        ["Ronald Coase", "Showed transaction costs explain why firms exist instead of pure market contracting"],
    ])},
    "economics-m1-l12": {"data_table": table(["Economist", "Contribution"], [
        ["Elinor Ostrom", "Showed communities can sustainably self-govern shared resources without privatization or state control"],
    ])},
    "economics-m1-l13": {"data_table": table(["Economist", "Contribution"], [
        ["Friedrich Hayek", "Argued dispersed knowledge makes centralized economic planning fundamentally limited"],
    ])},
    "economics-m1-l14": {"data_table": table(["Economist", "Contribution"], [
        ["Joseph Schumpeter", "Described innovation as a process of creative destruction that drives economic change"],
    ])},
    "economics-m1-l15": {"data_table": table(["Economist", "Contribution"], [
        ["Thorstein Veblen", "Coined conspicuous consumption to describe status-driven spending"],
    ])},
    "economics-m1-l16": {"data_table": table(["Economist", "Contribution"], [
        ["Milton Friedman", "Argued consumption depends on expected long-run (permanent) income, not just current income"],
    ])},
    "economics-m1-l17": {"data_table": table(["Economist", "Contribution"], [
        ["Franco Modigliani", "Modeled saving as smoothing consumption across a person's life cycle"],
    ])},
    "economics-m1-l18": {"data_table": table(["Economist", "Contribution"], [
        ["Paul Samuelson", "Showed consumer preferences can be inferred from observed choices alone"],
    ])},
    "economics-m1-l19": {"data_table": table(["Economist", "Contribution"], [
        ["Kenneth Arrow", "Proved no voting system can perfectly aggregate individual preferences into a group ranking"],
    ])},
    "economics-m1-l20": {"data_table": table(["Economist", "Contribution"], [
        ["John Nash", "Defined a fair bargaining solution based on the product of players' gains over disagreement"],
    ])},
    "economics-m1-l21": {"data_table": table(["Economist", "Contribution"], [
        ["Gary Becker", "Applied economic analysis to family decisions like marriage and fertility"],
    ])},
    "economics-m1-l22": {"data_table": table(["Economist", "Contribution"], [
        ["Douglass North", "Showed institutions shape long-run economic performance across history"],
    ])},
    "economics-m1-l23": {"data_table": table(["Economist", "Contribution"], [
        ["Robert Solow", "Showed most long-run growth comes from technological progress, not capital accumulation alone"],
    ])},
    "economics-m1-l24": {"data_table": table(["Economist", "Contribution"], [
        ["James Buchanan", "Applied economic reasoning to how political actors and institutions behave (public choice)"],
    ])},
    "economics-m1-l25": {"data_table": table(["Economist", "Contribution"], [
        ["Kahneman & Tversky", "Showed people evaluate outcomes relative to a reference point, weighting losses more than gains"],
    ])},
    "economics-m1-l26": {"data_table": table(["Economist", "Contribution"], [
        ["Thomas Piketty", "Analyzed long-run data showing capital's return has tended to exceed economic growth"],
    ])},
    "economics-m1-l27": {"data_table": table(["Economist", "Contribution"], [
        ["Esther Duflo", "Pioneered randomized control trials to rigorously test development policy interventions"],
    ])},
    "economics-m1-l28": {"data_table": table(["Economist", "Contribution"], [
        ["Irving Fisher", "Showed how debt liquidation can deepen deflation and depression"],
    ])},
    "economics-m1-l29": {"data_table": table(["Economist", "Contribution"], [
        ["John Maynard Keynes", "Explained interest rates as the reward for giving up liquidity"],
    ])},
    "economics-m1-l30": {"data_table": table(["Economist", "Contribution"], [
        ["Friedrich List", "Argued developing industries deserve temporary protection to mature (infant industry argument)"],
    ])},
    "economics-m1-l31": {"data_table": table(["Economist", "Contribution"], [
        ["Alfred Marshall", "Described how firms clustered in a region can gain shared productivity advantages"],
    ])},
    "economics-m1-l32": {"data_table": table(["Economist", "Contribution"], [
        ["Wassily Leontief", "Developed input-output analysis to model how industries depend on each other"],
    ])},
    "economics-m1-l33": {"data_table": table(["Economist", "Contribution"], [
        ["Simon Kuznets", "Proposed inequality first rises then falls as an economy develops"],
    ])},
    "economics-m1-l34": {"data_table": table(["Economist", "Contribution"], [
        ["Arthur Lewis", "Modeled development as labor moving from a low-productivity to a high-productivity sector"],
    ])},
    "economics-m1-l35": {"data_table": table(["Economist", "Contribution"], [
        ["Albert Hirschman", "Argued deliberately unbalanced investment can spur development through linkage effects"],
    ])},
    "economics-m1-l36": {"data_table": table(["Economist", "Contribution"], [
        ["Richard Thaler", "Showed small policy design changes (nudges) can improve decisions without restricting choice"],
    ])},
    "economics-m1-l37": {"data_table": table(["Event", "Feature"], [
        ["South Sea Bubble (1720)", "An early stock speculation bubble driven by inflated expectations"],
    ])},
    "economics-m1-l38": {"data_table": table(["Event", "Feature"], [
        ["Weimar hyperinflation (1921-23)", "Prices spiraled as the government printed money to cover war debts and reparations"],
    ])},
    "economics-m1-l39": {"data_table": table(["Event", "Feature"], [
        ["Bretton Woods collapse (1971)", "The US ended the dollar's gold convertibility, ending the fixed exchange rate system"],
    ])},
    "economics-m1-l40": {"data_table": table(["Event", "Feature"], [
        ["1997 Asian Financial Crisis", "Currency pegs collapsed as capital fled, spreading contagion across the region"],
    ])},
    "economics-m1-l41": {"data_table": table(["Event", "Feature"], [
        ["Great Depression policy responses", "Countries differed sharply in how quickly they left the gold standard and recovered"],
    ])},
    "economics-m1-l42": {"data_table": table(["Event", "Feature"], [
        ["Marshall Plan", "US aid that helped rebuild postwar European economies"],
    ])},
    "economics-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Balance sheet recession", "Prolonged stagnation as firms prioritize debt repayment over investment"],
    ])},
    "economics-m1-l44": {"data_table": table(["Event", "Feature"], [
        ["Icelandic banking collapse (2008)", "Oversized banks failed relative to the small national economy backing them"],
    ])},
    "economics-m1-l45": {"data_table": table(["Event", "Feature"], [
        ["Greek sovereign debt crisis", "Exposed structural weaknesses in a currency union without fiscal union"],
    ])},
    "economics-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Special Economic Zone", "A designated area with favorable policy used to attract export-oriented investment"],
    ])},
    "economics-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Chicago Boys reforms", "Free-market oriented economic reforms implemented in Chile"],
    ])},
    "economics-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["East Asian Miracle debate", "Disputes whether rapid growth came from markets or deliberate state industrial policy"],
    ])},
    "economics-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Transition economy", "A formerly centrally planned economy shifting toward market-based institutions"],
    ])},
    "economics-m1-l50": {"data_table": table(["Event", "Feature"], [
        ["Dutch Tulip Mania", "An early speculative bubble in bulb prices, often used as a cautionary case study"],
    ])},
    "economics-m1-l51": {"data_table": table(["Event", "Feature"], [
        ["1929 Wall Street Crash", "A stock market collapse followed by widespread bank failures"],
    ])},
    "economics-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Entitlement failure", "Famine caused by lack of access to food, not necessarily lack of food supply"],
    ])},
    "economics-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Resource curse", "Resource-rich countries can grow slower due to volatility, corruption, or currency effects"],
    ])},
    "economics-m1-l54": {"data_table": table(["Event", "Feature"], [
        ["Zimbabwean hyperinflation", "Excessive money printing led to extreme, rapidly accelerating price increases"],
    ])},
    "economics-m1-l55": {"data_table": table(["Economist", "Contribution"], [
        ["Guido Calabresi", "Analyzed how tort law should allocate accident costs to the least-cost avoider"],
    ])},
    "economics-m1-l56": {"data_table": table(["Economist", "Contribution"], [
        ["Richard Posner", "Applied economic efficiency analysis broadly across common law doctrines"],
    ])},
    "economics-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Property rights enforcement", "Secure, enforceable property rights are a key precondition for efficient markets"],
    ])},
    "economics-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Antitrust economics", "Analyzes how market power affects prices, output, and consumer welfare"],
    ])},
    "economics-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Coase theorem", "With low bargaining costs, parties can reach an efficient outcome regardless of initial legal entitlement"],
    ])},
    "economics-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Contract breach remedies", "Economic analysis of expectation, reliance, and restitution damages"],
    ])},
    "economics-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Criminal deterrence economics", "Models how the probability and severity of punishment affect crime rates"],
    ])},
    "economics-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Natural monopoly regulation", "Studies how to regulate industries where one firm can serve a market most efficiently"],
    ])},
    "economics-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Bankruptcy law economics", "Analyzes how insolvency rules affect creditor recovery and debtor incentives"],
    ])},
    "economics-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["IP law and economics", "Weighs innovation incentives against the costs of restricting knowledge diffusion"],
    ])},
    "economics-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Agricultural cooperative economics", "Studies how farmers pool resources to gain market power and efficiency"],
    ])},
    "economics-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Post-colonial land reform", "Studies redistribution policies and their effects on agricultural productivity"],
    ])},
    "economics-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Green Revolution impact", "High-yield crop varieties dramatically raised agricultural output across much of Asia"],
    ])},
    "economics-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Central place theory", "Explains the spatial hierarchy and spacing of urban settlements"],
    ])},
    "economics-m1-l69": {"data_table": table(["Economist", "Contribution"], [
        ["Paul Krugman", "Modeled how increasing returns and trade costs shape economic geography"],
    ])},
    "economics-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Land rent gradient", "Land value falls with distance from a city's economic center"],
    ])},
    "economics-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain clustering", "Firms locate near each other to reduce coordination and transport costs"],
    ])},
    "economics-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Industrial park economics", "Concentrates infrastructure and incentives to attract manufacturing investment"],
    ])},
    "economics-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Commodity price cycle", "Recurring boom-bust patterns driven by supply lags and demand shifts"],
    ])},
    "economics-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Agricultural subsidy economics", "Analyzes distortions and distributional effects of farm support policy"],
    ])},
    "economics-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Rural-urban migration model", "Explains labor movement toward cities in response to expected wage gaps"],
    ])},
    "economics-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Sharecropping economics", "Studies incentive problems when a tenant farmer shares output with a landowner"],
    ])},
    "economics-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Winner-take-all market", "Small performance differences translate into vastly unequal rewards"],
    ])},
    "economics-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Network effect", "A good becomes more valuable as more people use it"],
    ])},
    "economics-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Vickrey auction", "A sealed-bid auction where the winner pays the second-highest bid, encouraging honest bidding"],
    ])},
    "economics-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Revelation principle", "Any mechanism outcome can be achieved by one where participants truthfully report information"],
    ])},
    "economics-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Gale-Shapley algorithm", "Finds a stable matching between two groups based on ranked preferences"],
    ])},
    "economics-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Two-sided market", "A platform connecting two distinct user groups who value each other's participation"],
    ])},
    "economics-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Gold standard", "A monetary system where currency value was fixed to a set quantity of gold"],
    ])},
    "economics-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Slave trade institutional legacy", "Studies the long-run economic effects of extractive historical institutions"],
    ])},
    "economics-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Great Divergence debate", "Examines why Western Europe industrialized earlier and faster than other regions"],
    ])},
    "economics-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral public finance", "Applies behavioral insights to understand why people comply with or evade taxes"],
    ])},
    "economics-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Cartel economics (OPEC)", "Studies how producer coordination can restrict output to raise prices"],
    ])},
    "economics-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Bank of England founding", "An early central bank created to help finance government debt and stabilize money"],
    ])},
    "economics-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Company town economics", "A firm controls housing and commerce for its workers, raising economic power concerns"],
    ])},
    "economics-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Solow catch-up hypothesis", "Poorer economies tend to grow faster and converge toward richer ones over time"],
    ])},
    "economics-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Medieval guild system", "Regulated trades and training, shaping early European economic organization"],
    ])},
    "economics-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Physiocrats", "An early school arguing agricultural land was the true source of a nation's wealth"],
    ])},
    "economics-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["German Historical School", "Emphasized historical and institutional context over abstract economic theory"],
    ])},
    "economics-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Canal concessions", "Studies the economics of granting exclusive rights to operate major infrastructure"],
    ])},
    "economics-m1-l95": {"data_table": table(["Economist", "Contribution"], [
        ["Karl Polanyi", "Argued markets are embedded in and shaped by social and political institutions"],
    ])},
    "economics-m1-l96": {"data_table": table(["Economist", "Contribution"], [
        ["Jean Tirole", "Advanced the theory of how to regulate industries with market power and information gaps"],
    ])},
    "economics-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Cantillon effect", "New money entering an economy affects prices unevenly depending on who receives it first"],
    ])},
    "economics-m1-l98": {"data_table": table(["Economist", "Contribution"], [
        ["William Baumol", "Showed labor-intensive services rise in relative cost even without productivity loss"],
    ])},
    "economics-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Lucas critique", "Historical data relationships can break down once policy itself changes behavior"],
    ])},
    "economics-m1-l100": {"data_table": table(["Economist", "Contribution"], [
        ["Herbert Simon", "Argued people satisfice with limited information rather than perfectly optimizing"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"economics-m1-l{base_n}"
    worked_key = f"economics-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Economics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Economics lessons (completing 120/120).")


if __name__ == "__main__":
    main()
