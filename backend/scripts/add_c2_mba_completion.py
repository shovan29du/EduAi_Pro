#!/usr/bin/env python3
"""Depth pass, C2 MBA: fill in real, hand-checked data_table content
for the 69 C2 MBA lessons not covered by the earlier breadth-first
batch. Brings C2 MBA to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_mba_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mba-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Time value of money", "A dollar today is worth more than a dollar in the future"],
        ]),
    },
    "mba-c2-l2": {
        "data_table": table(["Element", "Purpose"], [
            ["The 4 Ps", "Product, Price, Place, Promotion, core levers of marketing strategy"],
        ]),
    },
    "mba-c2-l4": {
        "data_table": table(["Indicator", "Meaning"], [
            ["GDP growth", "Reflects overall economic expansion or contraction"], ["Inflation rate", "Reflects the pace of rising prices, affecting purchasing power"],
        ]),
    },
    "mba-c2-l5": {
        "data_table": table(["Concept", "Effect"], [
            ["Increased demand", "Raises equilibrium price if supply stays constant"],
        ]),
    },
    "mba-c2-l6": {
        "data_table": table(["Step", "Purpose"], [
            ["Segmentation", "Divides the market into distinct customer groups"], ["Positioning", "Defines how a brand is perceived relative to competitors"],
        ]),
    },
    "mba-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Organizational culture", "Shared values and norms shaping employee behavior"],
        ]),
    },
    "mba-c2-l8": {
        "data_table": table(["Practice", "Reason"], [
            ["Leading with the takeaway", "Executives need the conclusion before supporting detail"],
        ]),
    },
    "mba-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Corporate social responsibility", "A company's commitment to ethical, social, and environmental accountability"],
        ]),
    },
    "mba-c2-l10": {
        "data_table": table(["Type", "Example"], [
            ["Primary research", "Surveys conducted directly with customers"], ["Secondary research", "Analyzing existing industry reports"],
        ]),
    },
    "mba-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Value chain", "The sequence of activities a firm performs to deliver a valuable product"],
        ]),
    },
    "mba-c2-l12": {
        "data_table": table(["Term", "Formula"], [
            ["NPV", "Sum of discounted cash flows minus initial investment"],
        ]),
        "formulae": ["NPV = sum(CF_t / (1 + r) ** t for t in years) - initial_investment"],
    },
    "mba-c2-l13": {
        "data_table": table(["Step", "Purpose"], [
            ["Structured interviewing", "Reduces bias compared to unstructured conversations"],
        ]),
    },
    "mba-c2-l14": {
        "data_table": table(["Term", "Formula"], [
            ["Linear regression", "y = b0 + b1*x"],
        ]),
        "formulae": ["y = b0 + b1 * x"],
    },
    "mba-c2-l15": {
        "data_table": table(["Channel", "Feature"], [
            ["SEO", "Organic search visibility"], ["Paid social", "Targeted advertising on social platforms"],
        ]),
    },
    "mba-c2-l16": {
        "data_table": table(["Style", "Feature"], [
            ["Collaborating", "Seeks a win-win solution through open discussion"], ["Avoiding", "Sidesteps the conflict entirely"],
        ]),
    },
    "mba-c2-l17": {
        "data_table": table(["Element", "Requirement"], [
            ["Valid contract", "Offer, acceptance, and consideration"],
        ]),
    },
    "mba-c2-l18": {
        "data_table": table(["Constraint", "Tradeoff"], [
            ["Iron triangle", "Scope, time, and cost are interdependent constraints"],
        ]),
    },
    "mba-c2-l19": {
        "data_table": table(["Section", "Purpose"], [
            ["Executive summary", "Concisely introduces the business concept and opportunity"],
        ]),
    },
    "mba-c2-l20": {
        "data_table": table(["Skill", "Practiced"], [
            ["Cross-functional decision making", "Applying finance, marketing, and operations knowledge together"],
        ]),
    },
    "mba-c2-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Agency theory", "Examines conflicts of interest between managers (agents) and shareholders (principals)"],
        ]),
    },
    "mba-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Real options", "Applies financial options theory to value strategic flexibility in business decisions"],
        ]),
    },
    "mba-c2-l23": {
        "data_table": table(["Concept", "Meaning"], [
            ["Blue ocean strategy", "Creates uncontested market space rather than competing in existing markets"],
        ]),
    },
    "mba-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Business model innovation", "Redesigning how a company creates, delivers, and captures value"],
        ]),
    },
    "mba-c2-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Activity-based costing", "Assigns overhead costs based on actual activities driving those costs"],
        ]),
    },
    "mba-c2-l26": {
        "data_table": table(["Choice", "Tradeoff"], [
            ["Debt financing", "Preserves ownership but adds financial risk"], ["Equity financing", "Avoids debt but dilutes ownership"],
        ]),
    },
    "mba-c2-l27": {
        "data_table": table(["Term", "Formula"], [
            ["Break-even point", "Fixed costs / (price - variable cost per unit)"],
        ]),
        "formulae": ["break_even_units = fixed_costs / (price - variable_cost_per_unit)"],
    },
    "mba-c2-l28": {
        "data_table": table(["Model", "Focus"], [
            ["Behavioral segmentation", "Groups customers by purchasing behavior"], ["Psychographic segmentation", "Groups customers by values and lifestyle"],
        ]),
    },
    "mba-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Integrated marketing communications", "Coordinates all promotional messages for a consistent brand experience"],
        ]),
    },
    "mba-c2-l30": {
        "data_table": table(["Strategy", "Example"], [
            ["Brand extension", "Applying an established brand name to a new product category"],
        ]),
    },
    "mba-c2-l31": {
        "data_table": table(["Structure", "Feature"], [
            ["Functional structure", "Groups employees by specialty"], ["Matrix structure", "Combines functional and project-based reporting"],
        ]),
    },
    "mba-c2-l32": {
        "data_table": table(["Style", "Focus"], [
            ["Transformational leadership", "Inspires change through vision"], ["Transactional leadership", "Motivates through rewards and clear expectations"],
        ]),
    },
    "mba-c2-l33": {
        "data_table": table(["Theory", "Focus"], [
            ["Self-determination theory", "Emphasizes autonomy, competence, and relatedness as intrinsic motivators"],
        ]),
    },
    "mba-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Succession planning", "Preparing internal candidates to fill key leadership roles over time"],
        ]),
    },
    "mba-c2-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["Pay-for-performance", "Ties compensation directly to measurable individual or company results"],
        ]),
    },
    "mba-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Collective bargaining", "Negotiation between employers and organized labor over employment terms"],
        ]),
    },
    "mba-c2-l37": {
        "data_table": table(["Strategy", "Meaning"], [
            ["BATNA", "Establishes a fallback position that strengthens negotiating leverage"],
        ]),
    },
    "mba-c2-l38": {
        "data_table": table(["Practice", "Reason"], [
            ["Transparent crisis messaging", "Preserves stakeholder trust during a difficult event"],
        ]),
    },
    "mba-c2-l39": {
        "data_table": table(["Statement", "Focus"], [
            ["Income statement", "Revenue and expenses over a period"], ["Balance sheet", "Assets, liabilities, and equity at a point in time"],
        ]),
    },
    "mba-c2-l40": {
        "data_table": table(["Phase", "Focus"], [
            ["Valuation", "Determining what the target company is worth"], ["Integration", "Combining operations, culture, and systems post-deal"],
        ]),
    },
    "mba-c2-l41": {
        "data_table": table(["Method", "Feature"], [
            ["Direct method", "Forecasts cash inflows and outflows directly"], ["Indirect method", "Adjusts net income for non-cash items"],
        ]),
    },
    "mba-c2-l42": {
        "data_table": table(["Term", "Formula"], [
            ["Cash conversion cycle", "Days inventory + days receivable - days payable"],
        ]),
        "formulae": ["CCC = DIO + DSO - DPO"],
    },
    "mba-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Enterprise risk management", "A holistic framework for identifying and managing risks across an organization"],
        ]),
    },
    "mba-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Nash equilibrium", "A state where no competitor benefits from unilaterally changing strategy"],
        ]),
    },
    "mba-c2-l45": {
        "data_table": table(["Mode", "Risk Level"], [
            ["Exporting", "Low risk, low control"], ["Foreign direct investment", "High risk, high control"],
        ]),
    },
    "mba-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Global supply chain", "Coordinating sourcing, production, and distribution across multiple countries"],
        ]),
    },
    "mba-c2-l47": {
        "data_table": table(["Approach", "Meaning"], [
            ["Shared value strategy", "Integrates social impact directly into core business strategy"],
        ]),
    },
    "mba-c2-l48": {
        "data_table": table(["Model", "Focus"], [
            ["Kotter's 8-step model", "A structured framework for leading organizational change"],
        ]),
    },
    "mba-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Open innovation", "Sourcing ideas from outside the organization's own R&D"],
        ]),
    },
    "mba-c2-l50": {
        "data_table": table(["Stage", "Focus"], [
            ["Startup stage", "Finding product-market fit"], ["Growth stage", "Scaling operations and market reach"],
        ]),
    },
    "mba-c2-l51": {
        "data_table": table(["Method", "Approach"], [
            ["DCF", "Values a company based on projected future cash flows"], ["Comparable company analysis", "Values a company relative to similar public firms"],
        ]),
    },
    "mba-c2-l52": {
        "data_table": table(["Tool", "Purpose"], [
            ["Decision tree", "Maps out choices and their probable outcomes under uncertainty"],
        ]),
    },
    "mba-c2-l53": {
        "data_table": table(["Application", "Example"], [
            ["Predictive analytics", "Forecasting demand to guide strategic resource allocation"],
        ]),
    },
    "mba-c2-l54": {
        "data_table": table(["Metric", "Formula"], [
            ["Customer lifetime value", "avg purchase value x purchase frequency x customer lifespan"],
        ]),
        "formulae": ["CLV = avg_purchase_value * purchase_frequency * customer_lifespan"],
    },
    "mba-c2-l55": {
        "data_table": table(["Decision", "Consideration"], [
            ["Territory design", "Balances sales potential and rep workload across regions"],
        ]),
    },
    "mba-c2-l56": {
        "data_table": table(["Strategy", "Focus"], [
            ["Cost leadership", "Competes on being the lowest-cost producer"], ["Differentiation", "Competes on unique value beyond price"],
        ]),
    },
    "mba-c2-l57": {
        "data_table": table(["Theory", "Meaning"], [
            ["Stakeholder theory", "A firm should balance the interests of all affected parties, not just shareholders"],
        ]),
    },
    "mba-c2-l58": {
        "data_table": table(["Challenge", "Detail"], [
            ["Time zone coordination", "Requires establishing overlapping hours or asynchronous workflows"],
        ]),
    },
    "mba-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Strategic alliance", "A cooperative agreement between firms to pursue shared objectives"],
        ]),
    },
    "mba-c2-l60": {
        "data_table": table(["Component", "Purpose"], [
            ["Integrative capstone", "Applies finance, marketing, strategy, and operations to one real business case"],
        ]),
    },
    "mba-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Identifying uncontested market space", "Finding a customer need competitors overlook"],
        ]),
    },
    "mba-c2-l62": {
        "data_table": table(["Section", "Purpose"], [
            ["Financial projections", "Demonstrates the venture's expected path to profitability"],
        ]),
    },
    "mba-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Evaluating a capital project", "Applying NPV to decide whether to approve an investment"],
        ]),
    },
    "mba-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Applying the 4 Ps", "Designing a go-to-market plan for a new product"],
        ]),
    },
    "mba-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Running a Five Forces analysis", "Assessing competitive intensity in a real industry"],
        ]),
    },
    "mba-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting macro indicators", "Assessing how rising interest rates affect a business plan"],
        ]),
    },
    "mba-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Applying supply and demand", "Predicting price effects of a shifting market curve"],
        ]),
    },
    "mba-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a positioning statement", "Defining a brand's unique value proposition"],
        ]),
    },
    "mba-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Diagnosing a culture problem", "Identifying misalignment between stated values and actual behavior"],
        ]),
    },
    "mba-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Structuring an executive memo", "Writing a concise, action-oriented business recommendation"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["MBA"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json MBA: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 MBA lessons (completing 70/70).")


if __name__ == "__main__":
    main()
