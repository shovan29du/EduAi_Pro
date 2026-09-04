#!/usr/bin/env python3
"""Depth pass, C1 Data Science: fill in real, hand-checked data_table
content for the 69 C1 Data Science lessons not covered by the earlier
breadth-first batch. Brings C1 Data Science to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_data_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "data-science-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Data science", "Extracting insights and knowledge from data using statistics and computing"],
        ]),
    },
    "data-science-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Data wrangling", "Transforming raw data into a clean, usable format"],
        ]),
    },
    "data-science-c1-l4": {
        "data_table": table(["Strategy", "Approach"], [
            ["Mean imputation", "Fills missing values with the column average"], ["Deletion", "Removes rows with missing data"],
        ]),
    },
    "data-science-c1-l5": {
        "data_table": table(["Method", "Approach"], [
            ["Z-score", "Flags points far from the mean"], ["IQR method", "Flags points outside the interquartile range"],
        ]),
    },
    "data-science-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Schema validation", "Checking that data matches expected types and structure"],
        ]),
    },
    "data-science-c1-l7": {
        "data_table": table(["Method", "Description"], [
            ["Random sampling", "Every item has an equal chance of selection"], ["Stratified sampling", "Samples proportionally from subgroups"],
        ]),
    },
    "data-science-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Sampling bias", "When a sample doesn't accurately represent the population"],
        ]),
    },
    "data-science-c1-l9": {
        "data_table": table(["Statistic", "Meaning"], [
            ["Mean", "The average value"], ["Standard deviation", "A measure of spread"],
        ]),
    },
    "data-science-c1-l10": {
        "data_table": table(["Type", "Meaning"], [
            ["Univariate analysis", "Examines a single variable"], ["Bivariate analysis", "Examines the relationship between two variables"],
        ]),
    },
    "data-science-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Web scraping", "Automatically extracting data from websites"],
        ]),
    },
    "data-science-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["API integration", "Programmatically pulling data from an external service"],
        ]),
    },
    "data-science-c1-l13": {
        "data_table": table(["Practice", "Benefit"], [
            ["Clear cell organization", "Makes a Jupyter notebook easier to follow and reproduce"],
        ]),
    },
    "data-science-c1-l14": {
        "data_table": table(["Tool", "Purpose"], [
            ["Git", "Tracks changes to code and data scripts over time"],
        ]),
    },
    "data-science-c1-l15": {
        "data_table": table(["Technique", "Purpose"], [
            ["Tokenization", "Breaks text into analyzable units"],
        ]),
    },
    "data-science-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Cohort analysis", "Tracks how groups of users behave over time based on a shared start point"],
        ]),
    },
    "data-science-c1-l17": {
        "data_table": table(["Method", "Example"], [
            ["Demographic segmentation", "Grouping customers by age or location"],
        ]),
    },
    "data-science-c1-l18": {
        "data_table": table(["Letter", "Meaning"], [
            ["R", "Recency - how recently a customer purchased"], ["F", "Frequency - how often they purchase"], ["M", "Monetary - how much they spend"],
        ]),
    },
    "data-science-c1-l19": {
        "data_table": table(["Framework", "Focus"], [
            ["Data-driven decision making", "Bases decisions on evidence rather than intuition alone"],
        ]),
    },
    "data-science-c1-l20": {
        "data_table": table(["Element", "Purpose"], [
            ["Project writeup", "Explains the problem, method, and findings clearly"],
        ]),
    },
    "data-science-c1-l21": {
        "data_table": table(["Library", "Purpose"], [
            ["Pandas", "Data manipulation and analysis"], ["NumPy", "Numerical computing"],
        ]),
    },
    "data-science-c1-l22": {
        "data_table": table(["Function", "Purpose"], [
            ["np.array()", "Creates a NumPy array"],
        ]),
        "formulae": ["import numpy as np", "arr = np.array([1, 2, 3])"],
    },
    "data-science-c1-l23": {
        "data_table": table(["Function", "Purpose"], [
            ["pd.read_csv()", "Loads a CSV file into a DataFrame"],
        ]),
        "formulae": ["import pandas as pd", "df = pd.read_csv(\"data.csv\")"],
    },
    "data-science-c1-l24": {
        "data_table": table(["Principle", "Reason"], [
            ["Choosing the right chart type", "Matches the visualization to the data and message"],
        ]),
    },
    "data-science-c1-l25": {
        "data_table": table(["Library", "Purpose"], [
            ["Matplotlib", "General-purpose plotting"], ["Seaborn", "Statistical visualization built on Matplotlib"],
        ]),
        "formulae": ["import matplotlib.pyplot as plt", "plt.plot(x, y)"],
    },
    "data-science-c1-l26": {
        "data_table": table(["Command", "Purpose"], [
            ["SELECT", "Retrieves data"], ["WHERE", "Filters results"],
        ]),
        "formulae": ["SELECT * FROM customers WHERE age > 30;"],
    },
    "data-science-c1-l27": {
        "data_table": table(["Type", "Example"], [
            ["Numerical", "Age, income"], ["Categorical", "Country, gender"],
        ]),
    },
    "data-science-c1-l28": {
        "data_table": table(["Statistic", "Meaning"], [
            ["Mean", "Average value"], ["Median", "Middle value"], ["Mode", "Most frequent value"],
        ]),
    },
    "data-science-c1-l29": {
        "data_table": table(["Concern", "Example"], [
            ["Privacy", "Protecting personally identifiable information"],
        ]),
    },
    "data-science-c1-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Collect", "Gathers raw data"], ["Clean", "Prepares data for analysis"], ["Model", "Builds predictive or descriptive models"],
        ]),
    },
    "data-science-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature engineering", "Creating new input variables to improve model performance"],
        ]),
    },
    "data-science-c1-l32": {
        "data_table": table(["Technique", "Purpose"], [
            ["Min-max scaling", "Rescales values to a fixed range"], ["Standardization", "Rescales to zero mean, unit variance"],
        ]),
    },
    "data-science-c1-l33": {
        "data_table": table(["Method", "Description"], [
            ["One-hot encoding", "Converts categories into binary columns"],
        ]),
    },
    "data-science-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Time series data", "Data points collected sequentially over time"],
        ]),
    },
    "data-science-c1-l35": {
        "data_table": table(["Element", "Purpose"], [
            ["Data storytelling", "Communicating insights through narrative and visuals"],
        ]),
    },
    "data-science-c1-l36": {
        "data_table": table(["Tool", "Purpose"], [
            ["Tableau", "Interactive data visualization dashboards"], ["Power BI", "Microsoft's business intelligence platform"],
        ]),
    },
    "data-science-c1-l37": {
        "data_table": table(["Feature", "Purpose"], [
            ["Pivot tables", "Summarizes and aggregates data interactively"],
        ]),
    },
    "data-science-c1-l38": {
        "data_table": table(["Practice", "Benefit"], [
            ["Version control", "Enables reproducible, trackable analysis workflows"],
        ]),
    },
    "data-science-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Data governance", "Policies and processes ensuring data quality and proper use"],
        ]),
    },
    "data-science-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Comparing two versions to determine which performs better"],
        ]),
    },
    "data-science-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["ETL", "Extract, Transform, Load - moves data from source to destination"],
        ]),
    },
    "data-science-c1-l42": {
        "data_table": table(["Concept", "Meaning"], [
            ["Normalization", "Organizing database tables to reduce redundancy"],
        ]),
    },
    "data-science-c1-l43": {
        "data_table": table(["Type", "Example"], [
            ["Document database", "MongoDB"], ["Key-value store", "Redis"],
        ]),
    },
    "data-science-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Data warehouse", "A central repository for structured data from multiple sources"],
        ]),
    },
    "data-science-c1-l45": {
        "data_table": table(["Term", "Formula"], [
            ["Probability", "favorable outcomes / total outcomes"],
        ]),
    },
    "data-science-c1-l46": {
        "data_table": table(["Dimension", "Question"], [
            ["Completeness", "Is any data missing?"], ["Accuracy", "Is the data correct?"],
        ]),
    },
    "data-science-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Geospatial data", "Data with a geographic or location component"],
        ]),
    },
    "data-science-c1-l48": {
        "data_table": table(["Path", "Focus"], [
            ["Data analyst", "Reporting and descriptive analysis"], ["Data scientist", "Predictive modeling and machine learning"],
        ]),
    },
    "data-science-c1-l49": {
        "data_table": table(["Principle", "Reason"], [
            ["Aligning KPIs to goals", "Ensures metrics actually measure what matters"],
        ]),
    },
    "data-science-c1-l50": {
        "data_table": table(["Technique", "Purpose"], [
            ["Data anonymization", "Removes identifying information to protect privacy"],
        ]),
    },
    "data-science-c1-l51": {
        "data_table": table(["Language", "Strength"], [
            ["R", "Strong statistical and visualization libraries"], ["Python", "General-purpose, strong ML ecosystem"],
        ]),
    },
    "data-science-c1-l52": {
        "data_table": table(["Method", "Example"], [
            ["Surveys", "Direct data collection from respondents"], ["Sensors", "Automated data collection from devices"],
        ]),
    },
    "data-science-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Metadata", "Data describing other data, like a column's source and meaning"],
        ]),
    },
    "data-science-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Business intelligence", "Using data analysis to support business decision-making"],
        ]),
    },
    "data-science-c1-l55": {
        "data_table": table(["Practice", "Benefit"], [
            ["Running frequent experiments", "Builds a culture of evidence-based iteration"],
        ]),
    },
    "data-science-c1-l56": {
        "data_table": table(["Method", "Purpose"], [
            ["df.dropna()", "Removes rows with missing values"],
        ]),
        "formulae": ["df.dropna()"],
    },
    "data-science-c1-l57": {
        "data_table": table(["Method", "Purpose"], [
            ["df.merge()", "Combines two DataFrames based on a shared key"],
        ]),
        "formulae": ["pd.merge(df1, df2, on=\"id\")"],
    },
    "data-science-c1-l58": {
        "data_table": table(["Benefit", "Detail"], [
            ["Reproducibility", "Others can re-run the same analysis and get the same results"],
        ]),
    },
    "data-science-c1-l59": {
        "data_table": table(["Step", "Purpose"], [
            ["Defining the problem clearly", "Prevents wasted effort on the wrong question"],
        ]),
    },
    "data-science-c1-l60": {
        "data_table": table(["Principle", "Meaning"], [
            ["Avoiding misleading axes", "Ensures visualizations represent data honestly"],
        ]),
    },
    "data-science-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Scoping a project", "Defining the question, data sources, and success metric"],
        ]),
    },
    "data-science-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Wrangling a messy dataset", "Standardizing inconsistent date formats in a sample table"],
        ]),
    },
    "data-science-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning a dataset", "Fixing typos and duplicate entries in sample data"],
        ]),
    },
    "data-science-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Choosing an imputation strategy", "Deciding between mean imputation and deletion for missing ages"],
        ]),
    },
    "data-science-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Detecting outliers", "Flagging unusually high values in a sample sales dataset"],
        ]),
    },
    "data-science-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Validating a schema", "Checking that a column of ages contains only valid numbers"],
        ]),
    },
    "data-science-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a sampling method", "Selecting stratified sampling for an uneven population"],
        ]),
    },
    "data-science-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Spotting sampling bias", "Identifying why an online survey may not represent all users"],
        ]),
    },
    "data-science-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Profiling a dataset", "Summarizing a sample dataset's key statistics"],
        ]),
    },
    "data-science-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Running a bivariate analysis", "Testing the relationship between two sample variables"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Data Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Data Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Data Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
