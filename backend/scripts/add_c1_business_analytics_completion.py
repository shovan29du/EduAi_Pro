#!/usr/bin/env python3
"""Depth pass, C1 Business Analytics: fill in real, hand-checked
data_table content for the 69 C1 Business Analytics lessons not
covered by the earlier breadth-first batch. Brings C1 Business
Analytics to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_business_analytics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "business-analytics-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Business analytics", "Using data analysis to drive business decisions"],
        ]),
    },
    "business-analytics-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Descriptive analytics", "Summarizes what has happened using historical data"],
        ]),
    },
    "business-analytics-c1-l4": {
        "data_table": table(["Step", "Purpose"], [
            ["Removing duplicates", "Ensures each record is counted once"],
        ]),
    },
    "business-analytics-c1-l5": {
        "data_table": table(["Principle", "Reason"], [
            ["Aligning KPIs to strategy", "Ensures metrics reflect what the business actually cares about"],
        ]),
    },
    "business-analytics-c1-l6": {
        "data_table": table(["Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["GROUP BY", "Aggregates rows sharing a value"],
        ]),
        "formulae": ["SELECT region, SUM(sales) FROM orders GROUP BY region;"],
    },
    "business-analytics-c1-l7": {
        "data_table": table(["Method", "Description"], [
            ["Random sampling", "Every item has an equal chance of selection"], ["Convenience sampling", "Uses easily accessible respondents"],
        ]),
    },
    "business-analytics-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Probability", "The likelihood of an event occurring, from 0 to 1"],
        ]),
    },
    "business-analytics-c1-l9": {
        "data_table": table(["Chart Type", "Best For"], [
            ["Bar chart", "Comparing categories"], ["Line chart", "Trends over time"],
        ]),
    },
    "business-analytics-c1-l10": {
        "data_table": table(["Platform", "Feature"], [
            ["Power BI", "Microsoft's business intelligence tool"], ["Tableau", "Interactive visual analytics platform"],
        ]),
    },
    "business-analytics-c1-l11": {
        "data_table": table(["Element", "Purpose"], [
            ["Unbiased question wording", "Avoids leading respondents toward a particular answer"],
        ]),
    },
    "business-analytics-c1-l12": {
        "data_table": table(["Measure", "Meaning"], [
            ["Mean", "The average"], ["Standard deviation", "A measure of how spread out the data is"],
        ]),
    },
    "business-analytics-c1-l13": {
        "data_table": table(["Tool", "Purpose"], [
            ["Pivot table", "Summarizes and reorganizes data interactively"],
        ]),
    },
    "business-analytics-c1-l14": {
        "data_table": table(["Type", "Example"], [
            ["Internal data", "Sales records, CRM data"], ["External data", "Market research, public datasets"],
        ]),
    },
    "business-analytics-c1-l15": {
        "data_table": table(["Element", "Purpose"], [
            ["KPI card", "Shows a key metric at a glance"], ["Filter", "Lets users narrow the displayed data"],
        ]),
    },
    "business-analytics-c1-l16": {
        "data_table": table(["Formula", "Purpose"], [
            ["VLOOKUP", "Finds a value in a table by matching a key"], ["SUMIF", "Sums values matching a condition"],
        ]),
    },
    "business-analytics-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Data governance", "Policies ensuring data quality, security, and proper use"],
        ]),
    },
    "business-analytics-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Correlation", "A statistical relationship between two variables"],
        ]),
    },
    "business-analytics-c1-l19": {
        "data_table": table(["Formula", "Meaning"], [
            ["y = mx + b", "Predicts y from a linear relationship with x"],
        ]),
        "formulae": ["y = mx + b"],
    },
    "business-analytics-c1-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Executive summary", "Gives decision-makers the key findings up front"],
        ]),
    },
    "business-analytics-c1-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Predictive analytics", "Uses historical data to forecast future outcomes"],
        ]),
    },
    "business-analytics-c1-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Prescriptive analytics", "Recommends specific actions based on data analysis"],
        ]),
    },
    "business-analytics-c1-l23": {
        "data_table": table(["Stage", "Description"], [
            ["Descriptive", "Reports what happened"], ["Predictive", "Forecasts what might happen"], ["Prescriptive", "Recommends what to do"],
        ]),
    },
    "business-analytics-c1-l24": {
        "data_table": table(["Level", "Example"], [
            ["Nominal", "Categories with no order, e.g. color"], ["Ordinal", "Categories with order, e.g. rating"],
        ]),
    },
    "business-analytics-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Data warehouse", "A central repository for structured data used in reporting and analysis"],
        ]),
    },
    "business-analytics-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Data model", "A structured representation of how data entities relate to each other"],
        ]),
    },
    "business-analytics-c1-l27": {
        "data_table": table(["Method", "Example"], [
            ["Demographic segmentation", "Grouping customers by age or income"],
        ]),
    },
    "business-analytics-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Cohort analysis", "Tracks a group of users who share a common starting point over time"],
        ]),
    },
    "business-analytics-c1-l29": {
        "data_table": table(["Stage", "Example"], [
            ["Awareness", "Top of the funnel"], ["Purchase", "Bottom of the funnel"],
        ]),
    },
    "business-analytics-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Churn", "The rate at which customers stop doing business with a company"],
        ]),
    },
    "business-analytics-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Customer lifetime value", "The total revenue expected from a customer over their relationship with a business"],
        ]),
    },
    "business-analytics-c1-l32": {
        "data_table": table(["Metric", "Meaning"], [
            ["Conversion rate", "Percentage of visitors who complete a desired action"],
        ]),
    },
    "business-analytics-c1-l33": {
        "data_table": table(["Tool", "Purpose"], [
            ["Google Analytics", "Tracks website traffic and user behavior"],
        ]),
    },
    "business-analytics-c1-l34": {
        "data_table": table(["Metric", "Meaning"], [
            ["ROI", "Return on Investment, measures profitability of a spend"],
        ]),
    },
    "business-analytics-c1-l35": {
        "data_table": table(["Metric", "Meaning"], [
            ["Throughput", "The rate at which a process completes units of work"],
        ]),
    },
    "business-analytics-c1-l36": {
        "data_table": table(["Metric", "Meaning"], [
            ["Inventory turnover", "How many times inventory is sold and replaced over a period"],
        ]),
    },
    "business-analytics-c1-l37": {
        "data_table": table(["Metric", "Meaning"], [
            ["Employee turnover rate", "The percentage of employees who leave over a period"],
        ]),
    },
    "business-analytics-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Risk analytics", "Quantifying and analyzing potential threats to business operations"],
        ]),
    },
    "business-analytics-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Pricing analytics", "Using data to optimize product pricing strategy"],
        ]),
    },
    "business-analytics-c1-l40": {
        "data_table": table(["Method", "Description"], [
            ["Moving average", "Smooths data by averaging recent periods"],
        ]),
    },
    "business-analytics-c1-l41": {
        "data_table": table(["Element", "Purpose"], [
            ["Narrative arc", "Guides the audience through data to a clear conclusion"],
        ]),
    },
    "business-analytics-c1-l42": {
        "data_table": table(["Principle", "Reason"], [
            ["Placing key metrics prominently", "Draws attention to what matters most"],
        ]),
    },
    "business-analytics-c1-l43": {
        "data_table": table(["Framework", "Feature"], [
            ["OKRs", "Objectives and Key Results, links goals to measurable outcomes"],
        ]),
    },
    "business-analytics-c1-l44": {
        "data_table": table(["Step", "Purpose"], [
            ["Gathering evidence before deciding", "Reduces reliance on guesswork"],
        ]),
    },
    "business-analytics-c1-l45": {
        "data_table": table(["Feature", "Purpose"], [
            ["Power Query", "Cleans and transforms data before loading into Excel"],
        ]),
    },
    "business-analytics-c1-l46": {
        "data_table": table(["Join Type", "Result"], [
            ["Inner join", "Only matching rows from both tables"], ["Left join", "All rows from the left table plus matches"],
        ]),
        "formulae": ["SELECT * FROM orders o INNER JOIN customers c ON o.customer_id = c.id;"],
    },
    "business-analytics-c1-l47": {
        "data_table": table(["Function", "Purpose"], [
            ["SUM()", "Totals a column"], ["COUNT()", "Counts rows"], ["AVG()", "Averages a column"],
        ]),
    },
    "business-analytics-c1-l48": {
        "data_table": table(["Practice", "Reason"], [
            ["Avoiding 3D charts", "Distorts perception of data values"],
        ]),
    },
    "business-analytics-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["p-value", "The probability of observing results as extreme, assuming no real effect"],
        ]),
    },
    "business-analytics-c1-l50": {
        "data_table": table(["Method", "Approach"], [
            ["IQR method", "Flags points outside the interquartile range"],
        ]),
    },
    "business-analytics-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Business process analytics", "Analyzing workflows to find inefficiencies"],
        ]),
    },
    "business-analytics-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Competitive benchmarking", "Comparing performance metrics against industry competitors"],
        ]),
    },
    "business-analytics-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Market basket analysis", "Finds products frequently purchased together"],
        ]),
    },
    "business-analytics-c1-l54": {
        "data_table": table(["Question Type", "Use"], [
            ["Likert scale", "Measures agreement on a numeric scale"],
        ]),
    },
    "business-analytics-c1-l55": {
        "data_table": table(["Principle", "Meaning"], [
            ["Informed consent", "Ensuring people know how their data will be used"],
        ]),
    },
    "business-analytics-c1-l56": {
        "data_table": table(["Element", "Purpose"], [
            ["Narrative chart", "Highlights a specific insight rather than showing all data equally"],
        ]),
    },
    "business-analytics-c1-l57": {
        "data_table": table(["Category", "Example"], [
            ["Spreadsheet tools", "Excel"], ["BI platforms", "Tableau, Power BI"],
        ]),
    },
    "business-analytics-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-service analytics", "Allows non-technical users to explore data independently"],
        ]),
    },
    "business-analytics-c1-l59": {
        "data_table": table(["Step", "Purpose"], [
            ["Defining stakeholders and objectives", "Aligns the analytics project with business needs"],
        ]),
    },
    "business-analytics-c1-l60": {
        "data_table": table(["Career", "Focus"], [
            ["Business analyst", "Translates data into actionable business recommendations"],
        ]),
    },
    "business-analytics-c1-l61": {
        "data_table": table(["Element", "Purpose"], [
            ["Data storytelling", "Combines data, narrative, and visuals to communicate insights"],
        ]),
    },
    "business-analytics-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Identifying a business question", "Turning a vague concern into an answerable analytics question"],
        ]),
    },
    "business-analytics-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Summarizing sales history", "Reporting last quarter's total and average sales"],
        ]),
    },
    "business-analytics-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a spreadsheet model", "Projecting revenue under different growth assumptions"],
        ]),
    },
    "business-analytics-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning sales data", "Fixing inconsistent date and currency formats"],
        ]),
    },
    "business-analytics-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Designing a KPI", "Choosing a metric that reflects a specific business goal"],
        ]),
    },
    "business-analytics-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Writing a SQL query", "Retrieving total sales by region from a sample database"],
        ]),
    },
    "business-analytics-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a sample", "Selecting an appropriate survey sample size for a company"],
        ]),
    },
    "business-analytics-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Applying probability", "Estimating the chance of a customer churning from sample data"],
        ]),
    },
    "business-analytics-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a chart type", "Selecting the best chart to show quarterly revenue trends"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Analytics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Business Analytics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Business Analytics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
