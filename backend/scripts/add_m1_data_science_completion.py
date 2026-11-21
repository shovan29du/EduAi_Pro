#!/usr/bin/env python3
"""Depth pass, M1 Data Science: fill in real, hand-checked data_table
content for the 119 M1 Data Science lessons not covered by the
earlier breadth-first batch. Brings M1 Data Science to full 120/120
coverage.

Structure: l1-l100 are unique graduate-level topics spanning data
engineering, MLOps, advanced statistics/causal inference, and applied
data science domains; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_data_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["MLOps Stage", "Purpose"], [
    ["Model training", "Building the model from data"],
    ["Model deployment", "Putting the model into production"],
    ["Model monitoring", "Tracking performance over time"],
])

CHARTS: dict[str, dict] = {
    "data-science-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Applied machine learning", "Uses ML methods to solve concrete data science business problems"],
    ])},
    "data-science-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Data engineering", "Builds the pipelines and infrastructure that make data usable for analysis"],
    ])},
    "data-science-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Deployment pipeline", "Automates moving a trained model from development into production"],
    ])},
    "data-science-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["CI for data science", "Automatically tests and validates data/model code on each change"],
    ])},
    "data-science-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Production monitoring", "Tracks a deployed model's live performance and data drift"],
    ])},
    "data-science-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Data pipeline", "An automated sequence of steps that moves and transforms data from source to destination"],
    ])},
    "data-science-m1-l8": {"data_table": table(["Approach", "Order"], [
        ["ETL", "Transform data before loading it into the warehouse"],
        ["ELT", "Load raw data first, then transform it inside the warehouse"],
    ])},
    "data-science-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Workflow orchestration (Airflow)", "Schedules and manages dependencies between data pipeline tasks"],
    ])},
    "data-science-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Data quality monitoring", "Continuously checks incoming data for validity, completeness, and consistency"],
    ])},
    "data-science-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Star schema", "Organizes a data warehouse into a central fact table linked to dimension tables"],
    ])},
    "data-science-m1-l12": {"data_table": table(["Store", "Feature"], [
        ["Data warehouse", "Structured, curated data optimized for analytics"],
        ["Data lake", "Raw data of any format stored at scale"],
    ])},
    "data-science-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Dimensional modeling", "Structures data around measurable facts and descriptive dimensions for analytics"],
    ])},
    "data-science-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Slowly changing dimension", "A dimension table strategy for tracking how attribute values change over time"],
    ])},
    "data-science-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Real-time streaming", "Processes data continuously as it arrives, rather than in scheduled batches"],
    ])},
    "data-science-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Apache Kafka", "A distributed event streaming platform for high-throughput data pipelines"],
    ])},
    "data-science-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Stream processing", "Computes results continuously over an unbounded flow of events"],
    ])},
    "data-science-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Event-driven system", "Components react to events as they occur rather than polling on a schedule"],
    ])},
    "data-science-m1-l19": {"data_table": table(["Component", "Purpose"], [
        ["Data science capstone", "Integrates data pipeline, modeling, evaluation, and deployment into one project"],
    ])},
    "data-science-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["End-to-end pipeline", "Connects ingestion, transformation, modeling, and serving into one working system"],
    ])},
    "data-science-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Feature engineering", "Transforms raw data into informative inputs that improve model performance"],
    ])},
    "data-science-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Automated feature selection", "Algorithmically identifies the most predictive subset of available features"],
    ])},
    "data-science-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["ARIMA", "Models a time series using its own past values, differencing, and past forecast errors"],
    ])},
    "data-science-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Prophet", "A forecasting tool designed for time series with strong seasonal effects and holidays"],
    ])},
    "data-science-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Temporal convolutional network", "Applies causal convolutions to model sequential/time-series data"],
    ])},
    "data-science-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection", "Identifies data points that deviate significantly from expected patterns"],
    ])},
    "data-science-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Isolation forest", "Detects outliers by measuring how easily a point is isolated via random splits"],
    ])},
    "data-science-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["DBSCAN / HDBSCAN", "Density-based clustering that finds clusters of arbitrary shape without a fixed count"],
    ])},
    "data-science-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Gaussian mixture model", "Models data as a weighted combination of several Gaussian distributions"],
    ])},
    "data-science-m1-l30": {"data_table": table(["Method", "Use"], [
        ["t-SNE / UMAP", "Nonlinear dimensionality reduction for visualizing high-dimensional data"],
    ])},
    "data-science-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Principal component analysis", "Projects data onto orthogonal directions of maximum variance"],
    ])},
    "data-science-m1-l32": {"data_table": table(["Method", "Feature"], [
        ["Stacking", "Trains a meta-model to combine predictions from several base models"],
        ["Blending", "Combines model predictions on a held-out set rather than via cross-validation"],
    ])},
    "data-science-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hyperparameter optimization", "Uses a probabilistic model to efficiently search hyperparameter space"],
    ])},
    "data-science-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Time series cross-validation", "Validates using forward-chaining splits to avoid leaking future data into training"],
    ])},
    "data-science-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Causal inference", "Estimates the effect of an intervention from observational, non-experimental data"],
    ])},
    "data-science-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Propensity score matching", "Pairs treated and untreated units with similar likelihood of receiving treatment"],
    ])},
    "data-science-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Compares the change over time between a treated group and a control group"],
    ])},
    "data-science-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Sequential testing", "Allows an A/B test's significance to be checked continuously without inflating false positives"],
    ])},
    "data-science-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Multi-armed bandit", "Dynamically allocates traffic toward better-performing variants during an experiment"],
    ])},
    "data-science-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Cox proportional hazards", "Models how covariates affect the instantaneous risk of an event occurring"],
    ])},
    "data-science-m1-l41": {"data_table": table(["Method", "Use"], [
        ["Bootstrap", "Resamples data with replacement to estimate a statistic's sampling distribution"],
        ["Permutation test", "Shuffles labels to build a null distribution for a test statistic"],
    ])},
    "data-science-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian statistics", "Updates a prior belief with observed data to form a posterior distribution"],
    ])},
    "data-science-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Text analytics", "Extracts structured insight from unstructured natural-language data"],
    ])},
    "data-science-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Latent Dirichlet Allocation", "Discovers latent topics in a document collection as distributions over words"],
    ])},
    "data-science-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Sentiment analysis", "Classifies text according to the emotional attitude it expresses"],
    ])},
    "data-science-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["NER pipeline", "Identifies and classifies named entities (people, places, organizations) in text"],
    ])},
    "data-science-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Collaborative filtering at scale", "Recommends items using patterns across many users, engineered for large datasets"],
    ])},
    "data-science-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Matrix factorization", "Decomposes a user-item interaction matrix into lower-dimensional latent factors"],
    ])},
    "data-science-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Network science", "Analyzes the structure and dynamics of relationships within graph-structured data"],
    ])},
    "data-science-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network", "Learns representations by passing messages along graph edges"],
    ])},
    "data-science-m1-l51": {"data_table": table(["Principle", "Detail"], [
        ["Preattentive attributes", "Visual properties like color and position that the eye processes without conscious effort"],
    ])},
    "data-science-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Interactive dashboard", "Lets viewers filter and drill into data to support data storytelling"],
    ])},
    "data-science-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Query optimization", "Restructures or indexes a SQL query to reduce execution time on large datasets"],
    ])},
    "data-science-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Apache Spark", "A distributed computing framework for large-scale data processing"],
    ])},
    "data-science-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Spark performance tuning", "Adjusts partitioning, caching, and resource allocation to speed up Spark jobs"],
    ])},
    "data-science-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Data version control", "Tracks changes to datasets over time to make experiments reproducible"],
    ])},
    "data-science-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Feature store", "A centralized system for managing and serving ML features consistently"],
    ])},
    "data-science-m1-l58": {"data_table": table(["Method", "Feature"], [
        ["SHAP", "Assigns each feature a contribution value based on cooperative game theory"],
        ["LIME", "Explains a single prediction by fitting a simple local surrogate model"],
    ])},
    "data-science-m1-l59": {"data_table": table(["Metric", "Measures"], [
        ["Demographic parity", "Whether outcomes are distributed similarly across protected groups"],
    ])},
    "data-science-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Bias mitigation", "Techniques applied before, during, or after training to reduce unfair model outcomes"],
    ])},
    "data-science-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Data governance", "Policies and processes ensuring data is accurate, secure, and properly used"],
    ])},
    "data-science-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Master data management", "Maintains a single, authoritative source of an organization's core data entities"],
    ])},
    "data-science-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Data lineage", "Traces the origin and transformations a piece of data underwent through a pipeline"],
    ])},
    "data-science-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Data catalog", "An organized inventory of an organization's datasets and their metadata"],
    ])},
    "data-science-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data generation", "Creates artificial data that mimics real data's statistical properties"],
    ])},
    "data-science-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "Adds calibrated noise so individual records cannot be reverse-engineered"],
    ])},
    "data-science-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Statistical power analysis", "Determines the sample size needed to reliably detect an effect if it exists"],
    ])},
    "data-science-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Factorial design", "Tests multiple factors simultaneously by varying them in combination"],
    ])},
    "data-science-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Robust regression", "Reduces the influence of outliers on a fitted regression model"],
    ])},
    "data-science-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Quantile regression", "Models a specific percentile of the response variable rather than only its mean"],
    ])},
    "data-science-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Missing data imputation", "Fills in absent values using statistical or model-based estimates"],
    ])},
    "data-science-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Multiple imputation by chained equations", "Imputes missing values iteratively, generating several plausible complete datasets"],
    ])},
    "data-science-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Data cleaning at scale", "Automates detecting and fixing errors across very large datasets"],
    ])},
    "data-science-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Data profiling", "Automatically summarizes a dataset's structure, distribution, and quality issues"],
    ])},
    "data-science-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Geospatial analysis", "Analyzes data with location or spatial coordinates"],
    ])},
    "data-science-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Kriging", "A geostatistical interpolation method that estimates values at unsampled locations"],
    ])},
    "data-science-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Computer vision for data science", "Applies image-based models to extract structured features from visual data"],
    ])},
    "data-science-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Image augmentation", "Applies transformations to training images to improve model generalization"],
    ])},
    "data-science-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Model compression", "Reduces a model's size and computation via quantization or pruning"],
    ])},
    "data-science-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to mimic a larger teacher model"],
    ])},
    "data-science-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["AutoML", "Automates model selection, feature engineering, and hyperparameter tuning"],
    ])},
    "data-science-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automates the design of a network's structure"],
    ])},
    "data-science-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Responsible AI", "Considers fairness, transparency, and accountability throughout the data science lifecycle"],
    ])},
    "data-science-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Notebook-to-production workflow", "Converts exploratory notebook code into reliable, testable production code"],
    ])},
    "data-science-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh", "Decentralizes data ownership to domain teams rather than one central data team"],
    ])},
    "data-science-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Data contract", "A formal agreement defining the schema and guarantees of data shared between teams"],
    ])},
    "data-science-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Cohort analysis", "Tracks how a group of users who share a starting point behaves over time"],
    ])},
    "data-science-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value", "Predicts the total value a customer will generate over their relationship with a business"],
    ])},
    "data-science-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Churn prediction", "Estimates the probability a customer will stop using a product or service"],
    ])},
    "data-science-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Market basket analysis", "Finds items frequently purchased together using association rule mining"],
    ])},
    "data-science-m1-l91": {"data_table": table(["Metric", "Measures"], [
        ["MAPE / RMSE", "Common metrics for evaluating forecast accuracy"],
    ])},
    "data-science-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Data science project management", "Plans and coordinates the iterative, uncertain nature of data science work"],
    ])},
    "data-science-m1-l93": {"data_table": table(["Pitfall", "Risk"], [
        ["p-hacking", "Testing many hypotheses until one appears significant by chance"],
    ])},
    "data-science-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Multi-touch attribution", "Assigns credit for a conversion across multiple marketing touchpoints"],
    ])},
    "data-science-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Text embeddings and vector search", "Represents text as dense vectors and retrieves similar items by vector distance"],
    ])},
    "data-science-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Genomics data science", "Applies statistical and ML methods to large-scale genetic sequencing data"],
    ])},
    "data-science-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Financial risk modeling", "Applies statistical models to estimate and manage financial exposure"],
    ])},
    "data-science-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Double/debiased ML", "Combines machine learning with debiasing procedures to estimate causal effects validly"],
    ])},
    "data-science-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Point-in-time correctness", "Ensures a feature store only uses data that was actually available at prediction time"],
    ])},
    "data-science-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Entity resolution", "Identifies and links records that refer to the same real-world entity across sources"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"data-science-m1-l{base_n}"
    worked_key = f"data-science-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Data Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Data Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Data Science lessons (completing 120/120).")


if __name__ == "__main__":
    main()
