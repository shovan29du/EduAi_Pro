#!/usr/bin/env python3
"""Depth pass, C2 Business Analytics: fill in real, hand-checked
data_table/formulae content for the 69 C2 Business Analytics lessons
not covered by the earlier breadth-first batch. Brings C2 Business
Analytics to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_business_analytics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "business-analytics-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Data-driven decision making", "Basing business choices on data analysis rather than intuition alone"],
        ]),
    },
    "business-analytics-c2-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Descriptive statistics", "Summarizes key features of a business dataset"],
        ]),
    },
    "business-analytics-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Null hypothesis", "The default assumption a business test tries to reject"],
        ]),
    },
    "business-analytics-c2-l5": {
        "data_table": table(["Term", "Formula"], [
            ["Confidence interval", "x̄ ± z * (σ/√n)"],
        ]),
        "formulae": ["CI = x_bar +/- z * (sigma / sqrt(n))"],
    },
    "business-analytics-c2-l6": {
        "data_table": table(["Component", "Meaning"], [
            ["Trend", "Long-term direction in a time series"], ["Seasonality", "Regular repeating patterns tied to a calendar cycle"],
        ]),
    },
    "business-analytics-c2-l7": {
        "data_table": table(["Method", "Feature"], [
            ["Moving average", "Smooths data using an average of recent periods"], ["Exponential smoothing", "Weighs recent observations more heavily than older ones"],
        ]),
    },
    "business-analytics-c2-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Data warehouse", "A centralized repository optimized for reporting and analysis"],
        ]),
    },
    "business-analytics-c2-l9": {
        "data_table": table(["Concept", "Purpose"], [
            ["Normalization", "Reduces data redundancy in a relational schema"],
        ]),
    },
    "business-analytics-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Data mining", "Discovering patterns and relationships in large datasets"],
        ]),
    },
    "business-analytics-c2-l11": {
        "data_table": table(["Application", "Detail"], [
            ["Customer segmentation", "Groups customers by shared behavior or characteristics using clustering"],
        ]),
    },
    "business-analytics-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Market basket analysis", "Discovers products frequently purchased together"],
        ]),
    },
    "business-analytics-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Compares two variants to determine which performs better"],
        ]),
    },
    "business-analytics-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Decision tree", "Splits data on features to reach a business classification or prediction"],
        ]),
    },
    "business-analytics-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["ANOVA", "Compares means across three or more business groups"],
        ]),
    },
    "business-analytics-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Chi-square test", "Tests whether two categorical business variables are independent"],
        ]),
    },
    "business-analytics-c2-l17": {
        "data_table": table(["Tool", "Purpose"], [
            ["Power BI", "Builds interactive business dashboards from connected data sources"],
        ]),
    },
    "business-analytics-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Process mapping", "Visualizes a business process to identify bottlenecks and inefficiencies"],
        ]),
    },
    "business-analytics-c2-l19": {
        "data_table": table(["Metric", "Meaning"], [
            ["Sell-through rate", "The percentage of inventory sold within a period"],
        ]),
    },
    "business-analytics-c2-l20": {
        "data_table": table(["Property", "Detail"], [
            ["Volume, velocity, variety", "The core characteristics distinguishing big data from traditional data"],
        ]),
    },
    "business-analytics-c2-l21": {
        "data_table": table(["Use Case", "Detail"], [
            ["Logistic regression", "Predicts the probability of a binary outcome like customer churn"],
        ]),
    },
    "business-analytics-c2-l22": {
        "data_table": table(["Method", "Feature"], [
            ["Random forest", "Combines many decision trees to improve predictive accuracy"],
        ]),
    },
    "business-analytics-c2-l23": {
        "data_table": table(["Technique", "Purpose"], [
            ["K-fold cross-validation", "Provides a robust estimate of a business model's performance"],
        ]),
    },
    "business-analytics-c2-l24": {
        "data_table": table(["Method", "Purpose"], [
            ["Recursive feature elimination", "Iteratively removes weak features to improve model interpretability"],
        ]),
    },
    "business-analytics-c2-l25": {
        "data_table": table(["Metric", "Formula"], [
            ["Customer lifetime value", "avg purchase value x purchase frequency x customer lifespan"],
        ]),
        "formulae": ["CLV = avg_purchase_value * purchase_frequency * customer_lifespan"],
    },
    "business-analytics-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Churn prediction", "Estimates the likelihood a customer will stop doing business with a company"],
        ]),
    },
    "business-analytics-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Marketing mix modeling", "Statistically estimates how much each channel contributes to sales"],
        ]),
    },
    "business-analytics-c2-l28": {
        "data_table": table(["Model", "Approach"], [
            ["Last-touch attribution", "Credits the final touchpoint before conversion"], ["Multi-touch attribution", "Distributes credit across all touchpoints"],
        ]),
    },
    "business-analytics-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Uplift modeling", "Predicts the incremental effect of a marketing action on an individual customer"],
        ]),
    },
    "business-analytics-c2-l30": {
        "data_table": table(["Consideration", "Purpose"], [
            ["Sample size calculation", "Ensures an experiment has enough power to detect a real effect"],
        ]),
    },
    "business-analytics-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Causal inference", "Determines whether a business action actually caused an observed outcome"],
        ]),
    },
    "business-analytics-c2-l32": {
        "data_table": table(["Method", "Purpose"], [
            ["Difference-in-differences", "Estimates causal effect by comparing treated and control groups before and after an intervention"],
        ]),
    },
    "business-analytics-c2-l33": {
        "data_table": table(["Method", "Feature"], [
            ["ARIMA", "Models autocorrelation for more accurate time series forecasts"],
        ]),
    },
    "business-analytics-c2-l34": {
        "data_table": table(["Application", "Purpose"], [
            ["Demand forecasting", "Predicts future product demand to optimize inventory and supply chains"],
        ]),
    },
    "business-analytics-c2-l35": {
        "data_table": table(["Method", "Purpose"], [
            ["Linear programming", "Optimizes a business objective subject to resource constraints"],
        ]),
    },
    "business-analytics-c2-l36": {
        "data_table": table(["Method", "Purpose"], [
            ["Monte Carlo simulation", "Models a range of possible business outcomes using random sampling"],
        ]),
    },
    "business-analytics-c2-l37": {
        "data_table": table(["Layer", "Purpose"], [
            ["Semantic layer", "Provides a consistent business-friendly view over raw data sources"],
        ]),
    },
    "business-analytics-c2-l38": {
        "data_table": table(["Model", "Feature"], [
            ["Star schema", "Organizes a fact table surrounded by dimension tables for fast analytics queries"],
        ]),
    },
    "business-analytics-c2-l39": {
        "data_table": table(["Function", "Purpose"], [
            ["RANK() OVER", "Assigns a rank to rows within a partition"],
        ]),
        "formulae": ["SELECT name, RANK() OVER (ORDER BY revenue DESC) FROM sales;"],
    },
    "business-analytics-c2-l40": {
        "data_table": table(["Feature", "Purpose"], [
            ["Embedded predictive model", "Surfaces model predictions directly within a business dashboard"],
        ]),
    },
    "business-analytics-c2-l41": {
        "data_table": table(["Method", "Feature"], [
            ["K-means clustering", "Groups customers into a fixed number of segments based on behavior"],
        ]),
    },
    "business-analytics-c2-l42": {
        "data_table": table(["Type", "Feature"], [
            ["Collaborative filtering", "Recommends based on similar users' preferences"],
        ]),
    },
    "business-analytics-c2-l43": {
        "data_table": table(["Technique", "Purpose"], [
            ["Sentiment analysis", "Extracts customer opinion polarity from feedback text"],
        ]),
    },
    "business-analytics-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Credit scoring", "Predicts the likelihood a borrower will default on a loan"],
        ]),
    },
    "business-analytics-c2-l45": {
        "data_table": table(["Method", "Feature"], [
            ["Anomaly detection", "Flags unusual transactions that may indicate fraud"],
        ]),
    },
    "business-analytics-c2-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Dynamic pricing", "Adjusts prices in real time based on demand, competition, or inventory"],
        ]),
    },
    "business-analytics-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Yield management", "Maximizes revenue by adjusting prices and availability based on predicted demand"],
        ]),
    },
    "business-analytics-c2-l48": {
        "data_table": table(["Application", "Detail"], [
            ["Predictive HR model", "Forecasts employee attrition risk based on engagement and performance data"],
        ]),
    },
    "business-analytics-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Operations research", "Applies mathematical methods to optimize complex business operations"],
        ]),
    },
    "business-analytics-c2-l50": {
        "data_table": table(["Tool", "Purpose"], [
            ["Control chart", "Monitors whether a business process remains within acceptable limits"],
        ]),
    },
    "business-analytics-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Data governance", "Establishes policies ensuring data quality, security, and proper use"],
        ]),
    },
    "business-analytics-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Analytics Center of Excellence", "A centralized team setting standards and best practices for analytics across an organization"],
        ]),
    },
    "business-analytics-c2-l53": {
        "data_table": table(["Practice", "Reason"], [
            ["Explaining models simply", "Builds stakeholder trust and enables informed business decisions"],
        ]),
    },
    "business-analytics-c2-l54": {
        "data_table": table(["Principle", "Reason"], [
            ["Leading with the takeaway", "Executives need the conclusion before the supporting detail"],
        ]),
    },
    "business-analytics-c2-l55": {
        "data_table": table(["Role", "Focus"], [
            ["Analytics translator", "Bridges technical analysts and business stakeholders"],
        ]),
    },
    "business-analytics-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Real-time analytics", "Processes and analyzes data as it's generated, enabling immediate action"],
        ]),
    },
    "business-analytics-c2-l57": {
        "data_table": table(["Concern", "Detail"], [
            ["Model bias", "A predictive model systematically disadvantaging a particular group"],
        ]),
    },
    "business-analytics-c2-l58": {
        "data_table": table(["Metric", "Formula"], [
            ["Analytics ROI", "(Value generated - project cost) / project cost"],
        ]),
        "formulae": ["ROI = (value_generated - cost) / cost"],
    },
    "business-analytics-c2-l59": {
        "data_table": table(["Tool", "Purpose"], [
            ["Spark", "Processes large-scale business datasets across distributed compute clusters"],
        ]),
    },
    "business-analytics-c2-l60": {
        "data_table": table(["Component", "Purpose"], [
            ["End-to-end project", "Demonstrates the full pipeline from raw data to a business recommendation"],
        ]),
    },
    "business-analytics-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Validating a churn model", "Testing on holdout data before deploying to production"],
        ]),
    },
    "business-analytics-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting churn drivers", "Identifying which features most influence customer attrition risk"],
        ]),
    },
    "business-analytics-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Estimating channel contribution", "Isolating which marketing channels drove a sales increase"],
        ]),
    },
    "business-analytics-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Flagging a suspicious transaction", "Applying a fraud model's output to a real case"],
        ]),
    },
    "business-analytics-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Setting analytics standards", "Defining shared metric definitions across business units"],
        ]),
    },
    "business-analytics-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a metric to guide a decision", "Selecting the KPI most relevant to a specific business question"],
        ]),
    },
    "business-analytics-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Summarizing sales data", "Computing mean, median, and spread for a quarter's revenue"],
        ]),
    },
    "business-analytics-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a revenue model", "Using multiple predictors to forecast quarterly revenue"],
        ]),
    },
    "business-analytics-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Testing a business claim", "Applying hypothesis testing to a proposed process change"],
        ]),
    },
    "business-analytics-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Estimating a business metric", "Building a confidence interval around an average order value"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Analytics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Business Analytics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Business Analytics lessons (completing 70/70).")


if __name__ == "__main__":
    main()
