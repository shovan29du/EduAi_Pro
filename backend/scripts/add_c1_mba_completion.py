#!/usr/bin/env python3
"""Depth pass, C1 MBA: fill in real, hand-checked data_table content
for the 69 C1 MBA lessons not covered by the earlier breadth-first
batch. Brings C1 MBA to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_mba_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "mba-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["MBA", "Master of Business Administration, a graduate business management degree"],
        ]),
    },
    "mba-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Managerial accounting", "Uses financial data internally to guide business decisions"],
        ]),
    },
    "mba-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Supply and demand", "Determines market price and quantity"], ["Elasticity", "Measures responsiveness of quantity to price changes"],
        ]),
    },
    "mba-c1-l5": {
        "data_table": table(["Statement", "Purpose"], [
            ["Balance sheet", "Shows assets, liabilities, and equity"], ["Income statement", "Shows revenue and expenses over time"],
        ]),
    },
    "mba-c1-l6": {
        "data_table": table(["P", "Meaning"], [
            ["Product", "What is being sold"], ["Price", "What it costs"], ["Place", "Where it's sold"], ["Promotion", "How it's marketed"],
        ]),
    },
    "mba-c1-l7": {
        "data_table": table(["Structure", "Feature"], [
            ["Functional", "Organized by department"], ["Matrix", "Blends functional and project reporting"],
        ]),
    },
    "mba-c1-l8": {
        "data_table": table(["Skill", "Purpose"], [
            ["Active listening", "Ensures accurate understanding in business conversations"],
        ]),
    },
    "mba-c1-l9": {
        "data_table": table(["Principle", "Meaning"], [
            ["Transparency", "Honest, open business practices build stakeholder trust"],
        ]),
    },
    "mba-c1-l10": {
        "data_table": table(["Factor", "Effect"], [
            ["Social influence", "Peers and culture shape purchasing decisions"],
        ]),
    },
    "mba-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Value chain", "The sequence of activities that create and deliver a product's value"],
        ]),
    },
    "mba-c1-l12": {
        "data_table": table(["Principle", "Meaning"], [
            ["Time value of money", "A dollar today is worth more than a dollar in the future"],
        ]),
        "formulae": ["PV = FV / (1 + r)^n"],
    },
    "mba-c1-l13": {
        "data_table": table(["Function", "Example"], [
            ["Recruitment", "Attracting and hiring talent"], ["Compensation", "Managing pay and benefits"],
        ]),
    },
    "mba-c1-l14": {
        "data_table": table(["Concept", "Use"], [
            ["Regression analysis", "Models relationships between business variables"],
        ]),
    },
    "mba-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["E-commerce", "Buying and selling goods or services online"],
        ]),
    },
    "mba-c1-l16": {
        "data_table": table(["Stage", "Description"], [
            ["Forming", "Team members get acquainted"], ["Performing", "Team works effectively together"],
        ]),
    },
    "mba-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Contract law", "Governs legally binding agreements between parties"],
        ]),
    },
    "mba-c1-l18": {
        "data_table": table(["Technique", "Benefit"], [
            ["Time blocking", "Dedicates specific slots to specific tasks"],
        ]),
    },
    "mba-c1-l19": {
        "data_table": table(["Trait", "Meaning"], [
            ["Risk tolerance", "Willingness to accept uncertainty for potential reward"],
        ]),
    },
    "mba-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify the core issue", "Focuses analysis on the real business problem"],
        ]),
    },
    "mba-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Corporate governance", "The system of rules and practices directing a company"],
        ]),
    },
    "mba-c1-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["Set vision and goals", "Defines the company's long-term direction"],
        ]),
    },
    "mba-c1-l23": {
        "data_table": table(["Letter", "Meaning"], [
            ["S", "Strengths"], ["W", "Weaknesses"], ["O", "Opportunities"], ["T", "Threats"],
        ]),
    },
    "mba-c1-l24": {
        "data_table": table(["Block", "Purpose"], [
            ["Value proposition", "What makes the offering compelling"], ["Customer segments", "Who the offering serves"],
        ]),
    },
    "mba-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["CVP analysis", "Studies how costs, volume, and profit interact"],
        ]),
    },
    "mba-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Budget", "A financial plan estimating income and expenses over a period"],
        ]),
    },
    "mba-c1-l27": {
        "data_table": table(["Formula", "Meaning"], [
            ["Break-even point", "Fixed costs / (price - variable cost)"],
        ]),
        "formulae": ["Break-even units = Fixed Costs / (Price - Variable Cost)"],
    },
    "mba-c1-l28": {
        "data_table": table(["Type", "Example"], [
            ["Demographic segmentation", "Age, income"], ["Psychographic segmentation", "Lifestyle, values"],
        ]),
    },
    "mba-c1-l29": {
        "data_table": table(["Extended P", "Meaning"], [
            ["People", "Staff delivering the service"], ["Process", "How the service is delivered"], ["Physical evidence", "Tangible cues of quality"],
        ]),
    },
    "mba-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Brand equity", "The added value a brand name brings beyond the product itself"],
        ]),
    },
    "mba-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Organizational behavior", "Studies how individuals and groups act within organizations"],
        ]),
    },
    "mba-c1-l32": {
        "data_table": table(["Style", "Description"], [
            ["Transformational", "Inspires through vision"], ["Transactional", "Rewards and manages by task completion"],
        ]),
    },
    "mba-c1-l33": {
        "data_table": table(["Theory", "Idea"], [
            ["Maslow's hierarchy", "People are motivated by progressively higher needs"], ["Herzberg's two-factor theory", "Separates hygiene factors from true motivators"],
        ]),
    },
    "mba-c1-l34": {
        "data_table": table(["Element", "Purpose"], [
            ["Performance review", "Evaluates employee contributions periodically"],
        ]),
    },
    "mba-c1-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Recruitment", "Attracts candidates"], ["Onboarding", "Integrates new hires into the organization"],
        ]),
    },
    "mba-c1-l36": {
        "data_table": table(["Component", "Example"], [
            ["Base salary", "Fixed pay"], ["Benefits", "Health insurance, retirement contributions"],
        ]),
    },
    "mba-c1-l37": {
        "data_table": table(["Concept", "Meaning"], [
            ["BATNA", "Best Alternative To a Negotiated Agreement"],
        ]),
    },
    "mba-c1-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Clear structure", "Guides the audience through the argument logically"],
        ]),
    },
    "mba-c1-l39": {
        "data_table": table(["Ratio", "Formula"], [
            ["Current ratio", "Current assets / current liabilities"],
        ]),
        "formulae": ["Current ratio = Current assets / Current liabilities"],
    },
    "mba-c1-l40": {
        "data_table": table(["Statement", "Shows"], [
            ["Balance sheet", "Financial position at a point in time"], ["Income statement", "Performance over a period"],
        ]),
    },
    "mba-c1-l41": {
        "data_table": table(["Category", "Meaning"], [
            ["Operating activities", "Cash from core business operations"], ["Financing activities", "Cash from debt and equity transactions"],
        ]),
    },
    "mba-c1-l42": {
        "data_table": table(["Formula", "Meaning"], [
            ["Working capital", "Current assets minus current liabilities"],
        ]),
        "formulae": ["Working capital = Current assets - Current liabilities"],
    },
    "mba-c1-l43": {
        "data_table": table(["Strategy", "Meaning"], [
            ["Risk mitigation", "Reduces the likelihood or impact of a risk"],
        ]),
    },
    "mba-c1-l44": {
        "data_table": table(["Concept", "Meaning"], [
            ["Equilibrium price", "Where quantity supplied equals quantity demanded"],
        ]),
    },
    "mba-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["International business", "Commercial activities that cross national borders"],
        ]),
    },
    "mba-c1-l46": {
        "data_table": table(["Barrier", "Effect"], [
            ["Tariff", "A tax on imports that raises their price"],
        ]),
    },
    "mba-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["CSR reporting", "Publicly disclosing a company's social and environmental impact"],
        ]),
    },
    "mba-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Change management", "Structured approach to transitioning individuals through organizational change"],
        ]),
    },
    "mba-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Innovation management", "Systematically fostering and implementing new ideas"],
        ]),
    },
    "mba-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Startup", "A young company designed to grow quickly, often around a novel idea"],
        ]),
    },
    "mba-c1-l51": {
        "data_table": table(["Method", "Description"], [
            ["Discounted cash flow", "Values a business based on projected future cash flows"],
        ]),
    },
    "mba-c1-l52": {
        "data_table": table(["Model", "Description"], [
            ["Rational decision-making model", "Systematically evaluates all alternatives before choosing"],
        ]),
    },
    "mba-c1-l53": {
        "data_table": table(["Tool", "Purpose"], [
            ["Excel", "Spreadsheet analysis"], ["Tableau", "Visual data dashboards"],
        ]),
    },
    "mba-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["CRM", "Customer Relationship Management, tracks and manages customer interactions"],
        ]),
    },
    "mba-c1-l55": {
        "data_table": table(["Function", "Purpose"], [
            ["Sales forecasting", "Predicts future revenue based on trends"],
        ]),
    },
    "mba-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Brand positioning", "How a brand is perceived relative to competitors in customers' minds"],
        ]),
    },
    "mba-c1-l57": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify stakeholders affected", "Clarifies who is impacted by an ethical dilemma"],
        ]),
    },
    "mba-c1-l58": {
        "data_table": table(["Concept", "Meaning"], [
            ["Cross-cultural management", "Leading effectively across different cultural contexts"],
        ]),
    },
    "mba-c1-l59": {
        "data_table": table(["Skill", "Purpose"], [
            ["Following up after meeting someone", "Builds and maintains professional relationships"],
        ]),
    },
    "mba-c1-l60": {
        "data_table": table(["Element", "Purpose"], [
            ["Capstone project", "Applies MBA coursework to a real or simulated business problem"],
        ]),
    },
    "mba-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Selecting an MBA focus", "Choosing a concentration aligned with a career goal"],
        ]),
    },
    "mba-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Calculating product cost", "Allocating overhead costs across units produced"],
        ]),
    },
    "mba-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Applying a strategic framework", "Using Porter's Five Forces on a sample industry"],
        ]),
    },
    "mba-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing price elasticity", "Predicting demand change from a sample price increase"],
        ]),
    },
    "mba-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Reading financial statements", "Assessing a company's health from sample statements"],
        ]),
    },
    "mba-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Applying the 4Ps", "Designing a marketing mix for a sample new product"],
        ]),
    },
    "mba-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Choosing an org structure", "Deciding between functional and matrix for a growing company"],
        ]),
    },
    "mba-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Writing a business memo", "Communicating a decision clearly to a team"],
        ]),
    },
    "mba-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an ethics case", "Weighing stakeholder interests in a sample dilemma"],
        ]),
    },
    "mba-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Predicting consumer response", "Assessing how a price change affects purchase decisions"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["MBA"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json MBA: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 MBA lessons (completing 70/70).")


if __name__ == "__main__":
    main()
