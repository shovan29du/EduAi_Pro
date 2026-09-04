#!/usr/bin/env python3
"""Depth pass, C1 Business Studies: fill in real, hand-checked
data_table content for the 99 C1 Business Studies lessons not covered
by the earlier breadth-first batch. Brings C1 Business Studies to full
100/100 coverage.

Note: this subject has 100 lessons structured as 20 topics x 5 modes:
l1-20 Conceptual Foundations, l21-40 Worked Analysis, l41-60 Evidence
and Data, l61-80 Comparative Case Study, l81-100 Applied Research
Seminar (topic N maps to lessons N, N+20, N+40, N+60, N+80).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_business_studies_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


# Each topic (in lesson-index order 1-20) maps to five data_tables, one
# per mode: [Conceptual Foundations, Worked Analysis, Evidence and Data,
# Comparative Case Study, Applied Research Seminar].
TOPICS: list[dict] = [
    {  # 1
        "name": "Business Purpose",
        "foundations": table(["Term", "Meaning"], [["Mission", "Why an organization exists"], ["Vision", "What the organization aims to become"]]),
        "worked": table(["Step", "Example"], [["Defining purpose", "A hospital's mission centers on patient care, not just profit"]]),
        "evidence": table(["Metric", "Insight"], [["Stakeholder surveys", "Reveal how well a stated purpose matches actual practice"]]),
        "case_study": table(["Company", "Purpose Focus"], [["Patagonia", "Environmental sustainability alongside profit"], ["Standard retailer", "Primarily shareholder profit"]]),
        "seminar": table(["Step", "Focus"], [["Auditing a mission statement", "Comparing stated purpose to actual business decisions"]]),
    },
    {  # 2
        "name": "Business Models",
        "foundations": table(["Component", "Meaning"], [["Value proposition", "What unique value a business offers customers"], ["Revenue stream", "How the business earns money"]]),
        "worked": table(["Model", "Example"], [["Subscription model", "Netflix charges a recurring monthly fee"]]),
        "evidence": table(["Metric", "Insight"], [["Customer lifetime value", "Shows long-term revenue potential of a business model"]]),
        "case_study": table(["Company", "Model"], [["Amazon", "Marketplace plus subscription (Prime)"], ["Local bakery", "Direct sales model"]]),
        "seminar": table(["Step", "Focus"], [["Mapping a business model canvas", "Documenting a real company's key value proposition and channels"]]),
    },
    {  # 3
        "name": "Entrepreneurship",
        "foundations": table(["Term", "Meaning"], [["Entrepreneur", "A person who starts and takes on the risk of a new venture"]]),
        "worked": table(["Step", "Example"], [["Validating an idea", "Testing a product concept with a minimum viable product"]]),
        "evidence": table(["Metric", "Insight"], [["Startup survival rate", "Roughly half of new businesses fail within five years"]]),
        "case_study": table(["Founder", "Venture"], [["Sara Blakely", "Bootstrapped Spanx from personal savings"]]),
        "seminar": table(["Step", "Focus"], [["Interviewing a local entrepreneur", "Documenting real challenges faced when launching a venture"]]),
    },
    {  # 4
        "name": "Market Research",
        "foundations": table(["Type", "Example"], [["Primary research", "Surveys conducted directly with target customers"], ["Secondary research", "Analyzing existing industry reports"]]),
        "worked": table(["Step", "Example"], [["Segmenting a market", "Dividing customers by age, income, or behavior"]]),
        "evidence": table(["Metric", "Insight"], [["Market size (TAM)", "Estimates the total potential demand for a product"]]),
        "case_study": table(["Company", "Approach"], [["Coca-Cola", "Extensive taste testing before product launches"]]),
        "seminar": table(["Step", "Focus"], [["Designing a customer survey", "Writing questions that avoid leading bias"]]),
    },
    {  # 5
        "name": "Customer Value",
        "foundations": table(["Term", "Meaning"], [["Customer value", "The perceived benefit a customer gets relative to cost"]]),
        "worked": table(["Step", "Example"], [["Calculating value", "Comparing a product's benefits against its price and alternatives"]]),
        "evidence": table(["Metric", "Insight"], [["Net Promoter Score", "Measures customer likelihood to recommend a business"]]),
        "case_study": table(["Company", "Value Driver"], [["Costco", "Low prices via bulk membership model"], ["Apple", "Premium design and ecosystem integration"]]),
        "seminar": table(["Step", "Focus"], [["Mapping a customer journey", "Identifying where value is gained or lost at each touchpoint"]]),
    },
    {  # 6
        "name": "Marketing Strategy",
        "foundations": table(["Element", "Meaning"], [["The 4 Ps", "Product, Price, Place, Promotion"]]),
        "worked": table(["Step", "Example"], [["Positioning", "Defining how a brand is perceived relative to competitors"]]),
        "evidence": table(["Metric", "Insight"], [["Customer acquisition cost", "Tracks how much it costs to gain one new customer"]]),
        "case_study": table(["Company", "Strategy"], [["Nike", "Emotional brand storytelling over product-feature focus"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a real ad campaign", "Identifying its target segment and positioning strategy"]]),
    },
    {  # 7
        "name": "Operations Management",
        "foundations": table(["Term", "Meaning"], [["Operations management", "Designing and controlling the process of producing goods or services"]]),
        "worked": table(["Metric", "Formula"], [["Throughput", "Units produced divided by time taken"]], ),
        "evidence": table(["Metric", "Insight"], [["Cycle time", "Reveals bottlenecks in a production process"]]),
        "case_study": table(["Company", "Approach"], [["Toyota", "Just-in-time production minimizing inventory"]]),
        "seminar": table(["Step", "Focus"], [["Mapping a real process", "Identifying the slowest step in a workflow"]]),
    },
    {  # 8
        "name": "Supply Chains",
        "foundations": table(["Term", "Meaning"], [["Supply chain", "The network moving a product from raw material to customer"]]),
        "worked": table(["Step", "Example"], [["Identifying a bottleneck", "A single supplier delay can halt entire production"]]),
        "evidence": table(["Metric", "Insight"], [["Lead time", "Measures how long it takes to receive materials after ordering"]]),
        "case_study": table(["Event", "Impact"], [["2021 shipping disruptions", "Exposed risks of relying on single-region suppliers"]]),
        "seminar": table(["Step", "Focus"], [["Tracing a product's supply chain", "Mapping its path from raw material to shelf"]]),
    },
    {  # 9
        "name": "Accounting Fundamentals",
        "foundations": table(["Statement", "Purpose"], [["Income statement", "Shows revenue and expenses over a period"], ["Balance sheet", "Shows assets, liabilities, and equity at a point in time"]]),
        "worked": table(["Formula", "Detail"], [["Assets = Liabilities + Equity", "The fundamental accounting equation"]]),
        "evidence": table(["Metric", "Insight"], [["Profit margin", "Reveals how much of revenue becomes profit"]]),
        "case_study": table(["Scenario", "Insight"], [["Two companies, same revenue", "Different expense control leads to different profit margins"]]),
        "seminar": table(["Step", "Focus"], [["Reading a real income statement", "Identifying revenue, cost, and net income lines"]]),
    },
    {  # 10
        "name": "Corporate Finance",
        "foundations": table(["Term", "Meaning"], [["Capital structure", "The mix of debt and equity a company uses to finance itself"]]),
        "worked": table(["Formula", "Detail"], [["ROI", "(Gain - Cost) / Cost"]]),
        "evidence": table(["Metric", "Insight"], [["Debt-to-equity ratio", "Indicates financial risk from leverage"]]),
        "case_study": table(["Company", "Choice"], [["Startup", "Equity financing to avoid early debt burden"], ["Established firm", "Debt financing to preserve ownership"]]),
        "seminar": table(["Step", "Focus"], [["Comparing financing options", "Weighing debt versus equity for a hypothetical expansion"]]),
    },
    {  # 11
        "name": "People Management",
        "foundations": table(["Term", "Meaning"], [["Human resource management", "Recruiting, developing, and retaining employees"]]),
        "worked": table(["Step", "Example"], [["Structured interviewing", "Reduces bias compared to unstructured conversations"]]),
        "evidence": table(["Metric", "Insight"], [["Employee turnover rate", "High turnover often signals management or culture issues"]]),
        "case_study": table(["Company", "Practice"], [["Google", "Invests heavily in employee development and perks"]]),
        "seminar": table(["Step", "Focus"], [["Designing a hiring process", "Structuring interview questions around role requirements"]]),
    },
    {  # 12
        "name": "Organisational Behaviour",
        "foundations": table(["Term", "Meaning"], [["Organisational culture", "Shared values and norms shaping employee behavior"]]),
        "worked": table(["Step", "Example"], [["Diagnosing team dynamics", "Observing communication patterns in meetings"]]),
        "evidence": table(["Metric", "Insight"], [["Employee engagement score", "Correlates with productivity and retention"]]),
        "case_study": table(["Company", "Culture"], [["Zappos", "Deliberately built a customer-centric culture"]]),
        "seminar": table(["Step", "Focus"], [["Observing a real team", "Identifying formal versus informal communication channels"]]),
    },
    {  # 13
        "name": "Business Law",
        "foundations": table(["Term", "Meaning"], [["Contract", "A legally binding agreement between parties"]]),
        "worked": table(["Element", "Requirement"], [["Valid contract", "Requires offer, acceptance, and consideration"]]),
        "evidence": table(["Case Type", "Insight"], [["Contract disputes", "Often hinge on ambiguous or missing terms"]]),
        "case_study": table(["Scenario", "Lesson"], [["Verbal agreement gone wrong", "Highlights the value of written contracts"]]),
        "seminar": table(["Step", "Focus"], [["Reviewing a sample contract", "Identifying key clauses and potential risks"]]),
    },
    {  # 14
        "name": "Business Ethics",
        "foundations": table(["Term", "Meaning"], [["Business ethics", "Moral principles guiding business conduct"]]),
        "worked": table(["Step", "Example"], [["Evaluating a decision", "Weighing shareholder profit against broader stakeholder impact"]]),
        "evidence": table(["Metric", "Insight"], [["ESG reporting", "Tracks a company's environmental and social impact"]]),
        "case_study": table(["Company", "Issue"], [["Volkswagen", "Emissions scandal highlighted ethical failure in compliance"]]),
        "seminar": table(["Step", "Focus"], [["Analyzing a real ethics case", "Identifying which stakeholders were harmed and how"]]),
    },
    {  # 15
        "name": "Strategy",
        "foundations": table(["Term", "Meaning"], [["Competitive advantage", "What lets a firm outperform rivals sustainably"]]),
        "worked": table(["Tool", "Purpose"], [["SWOT analysis", "Assesses strengths, weaknesses, opportunities, threats"]]),
        "evidence": table(["Metric", "Insight"], [["Market share trend", "Signals whether a strategy is gaining or losing ground"]]),
        "case_study": table(["Company", "Strategy"], [["Southwest Airlines", "Cost leadership through operational simplicity"]]),
        "seminar": table(["Step", "Focus"], [["Running a SWOT analysis", "Applying the framework to a real local business"]]),
    },
    {  # 16
        "name": "Innovation Management",
        "foundations": table(["Term", "Meaning"], [["Disruptive innovation", "A simpler, cheaper offering that eventually displaces incumbents"]]),
        "worked": table(["Step", "Example"], [["Piloting an idea", "Testing a new feature with a small user group first"]]),
        "evidence": table(["Metric", "Insight"], [["R&D spending ratio", "Indicates a firm's investment in future innovation"]]),
        "case_study": table(["Company", "Innovation"], [["Netflix", "Disrupted video rental through streaming"]]),
        "seminar": table(["Step", "Focus"], [["Researching a disruptive innovation", "Tracing how it displaced an established incumbent"]]),
    },
    {  # 17
        "name": "Digital Business",
        "foundations": table(["Term", "Meaning"], [["Digital transformation", "Integrating digital technology into all areas of a business"]]),
        "worked": table(["Step", "Example"], [["Moving to e-commerce", "Shifting sales channels from physical stores to online"]]),
        "evidence": table(["Metric", "Insight"], [["Conversion rate", "Measures the share of website visitors who make a purchase"]]),
        "case_study": table(["Company", "Shift"], [["Blockbuster vs. Netflix", "Failure to digitally adapt led to Blockbuster's decline"]]),
        "seminar": table(["Step", "Focus"], [["Auditing a company's digital presence", "Evaluating its website and online customer experience"]]),
    },
    {  # 18
        "name": "International Business",
        "foundations": table(["Term", "Meaning"], [["Globalization", "Increasing interconnection of national economies and markets"]]),
        "worked": table(["Step", "Example"], [["Market entry", "Choosing between exporting, franchising, or direct investment"]]),
        "evidence": table(["Metric", "Insight"], [["Exchange rate exposure", "Affects the profitability of international transactions"]]),
        "case_study": table(["Company", "Approach"], [["McDonald's", "Adapts its menu locally while keeping a consistent brand"]]),
        "seminar": table(["Step", "Focus"], [["Comparing market entry modes", "Weighing risk and control across two entry strategies"]]),
    },
    {  # 19
        "name": "Risk and Resilience",
        "foundations": table(["Term", "Meaning"], [["Business risk", "The possibility of loss from internal or external factors"]]),
        "worked": table(["Step", "Example"], [["Risk matrix", "Plots risks by likelihood and potential impact"]]),
        "evidence": table(["Metric", "Insight"], [["Business continuity readiness", "Measures preparedness for major disruptions"]]),
        "case_study": table(["Event", "Response"], [["COVID-19 pandemic", "Forced rapid pivots to remote work and delivery models"]]),
        "seminar": table(["Step", "Focus"], [["Building a risk register", "Listing and prioritizing risks for a hypothetical business"]]),
    },
    {  # 20
        "name": "Sustainable Enterprise",
        "foundations": table(["Term", "Meaning"], [["Triple bottom line", "Measures success by people, planet, and profit"]]),
        "worked": table(["Step", "Example"], [["Reducing waste", "Redesigning packaging to cut material use"]]),
        "evidence": table(["Metric", "Insight"], [["Carbon footprint reporting", "Tracks a company's environmental impact over time"]]),
        "case_study": table(["Company", "Practice"], [["IKEA", "Committed to renewable energy across its operations"]]),
        "seminar": table(["Step", "Focus"], [["Auditing sustainability claims", "Checking a company's report against independent verification"]]),
    },
]

MODE_TO_OFFSET = {
    "foundations": 0,
    "worked": 20,
    "evidence": 40,
    "case_study": 60,
    "seminar": 80,
}

CHARTS: dict[str, dict] = {}
for idx, topic in enumerate(TOPICS, start=1):
    for mode, offset in MODE_TO_OFFSET.items():
        lesson_num = idx + offset
        lesson_id = f"business-studies-c1-l{lesson_num}"
        CHARTS[lesson_id] = {"data_table": topic[mode]}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Studies"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Business Studies: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Business Studies lessons (completing 100/100).")


if __name__ == "__main__":
    main()
