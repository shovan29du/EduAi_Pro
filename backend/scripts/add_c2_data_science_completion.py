#!/usr/bin/env python3
"""Depth pass, C2 Data Science: fill in real, hand-checked
data_table/formulae content for the 69 C2 Data Science lessons not
covered by the earlier breadth-first batch. Brings C2 Data Science to
full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_data_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "data-science-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Exploratory data analysis", "Investigating a dataset's structure and patterns before formal modeling"],
        ]),
    },
    "data-science-c2-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Descriptive statistics", "Summarizes and describes the main features of a dataset"],
        ]),
    },
    "data-science-c2-l4": {
        "data_table": table(["Distribution", "Use"], [
            ["Normal distribution", "Models naturally occurring continuous data"], ["Poisson distribution", "Models count data over a fixed interval"],
        ]),
    },
    "data-science-c2-l5": {
        "data_table": table(["Term", "Statement"], [
            ["Central Limit Theorem", "Sample means approach a normal distribution as sample size grows"],
        ]),
    },
    "data-science-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Null hypothesis", "The default assumption of no effect, which the test tries to reject"],
        ]),
    },
    "data-science-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["p-value", "The probability of observing the data (or more extreme) if the null hypothesis is true"],
        ]),
    },
    "data-science-c2-l8": {
        "data_table": table(["Error", "Meaning"], [
            ["Type I error", "Rejecting a true null hypothesis, a false positive"], ["Type II error", "Failing to reject a false null hypothesis, a false negative"],
        ]),
    },
    "data-science-c2-l9": {
        "data_table": table(["Test", "Use"], [
            ["Mann-Whitney U test", "Compares two independent groups without assuming normality"],
        ]),
    },
    "data-science-c2-l10": {
        "data_table": table(["Method", "Meaning"], [
            ["Bootstrap", "Resamples data with replacement to estimate a statistic's sampling distribution"],
        ]),
    },
    "data-science-c2-l11": {
        "data_table": table(["Fallacy", "Meaning"], [
            ["Cherry picking", "Selecting only data that supports a desired conclusion"],
        ]),
    },
    "data-science-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Simpson's Paradox", "A trend appearing in separate groups reverses when the groups are combined"],
        ]),
    },
    "data-science-c2-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Survivorship bias", "Drawing conclusions only from entities that 'survived' a selection process"],
        ]),
    },
    "data-science-c2-l14": {
        "data_table": table(["Term", "Formula"], [
            ["Linear regression", "y = b0 + b1*x"],
        ]),
        "formulae": ["y = b0 + b1 * x"],
    },
    "data-science-c2-l15": {
        "data_table": table(["Diagnostic", "Checks"], [
            ["Residual plot", "Whether error terms are randomly distributed"], ["VIF", "Whether predictors are highly correlated with each other"],
        ]),
    },
    "data-science-c2-l16": {
        "data_table": table(["Use Case", "Detail"], [
            ["Logistic regression", "Predicts the probability of a binary business outcome, like churn"],
        ]),
    },
    "data-science-c2-l17": {
        "data_table": table(["Metric", "Meaning"], [
            ["AIC", "Balances model fit and complexity, penalizing extra parameters"], ["BIC", "Similar to AIC but penalizes complexity more heavily"],
        ]),
    },
    "data-science-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Statistical process control", "Uses statistical methods to monitor and control a process"],
        ]),
    },
    "data-science-c2-l19": {
        "data_table": table(["Chart Type", "Use"], [
            ["Control chart", "Tracks process metrics over time against upper and lower limits"],
        ]),
    },
    "data-science-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Bayesian inference", "Updates probability estimates as new evidence becomes available, using Bayes' theorem"],
        ]),
        "formulae": ["P(A|B) = P(B|A) * P(A) / P(B)"],
    },
    "data-science-c2-l21": {
        "data_table": table(["Feature", "Purpose"], [
            ["Window function", "Performs calculations across a set of rows related to the current row"], ["CTE", "A named temporary result set improving query readability"],
        ]),
        "formulae": ["SELECT name, RANK() OVER (ORDER BY score DESC) FROM students;"],
    },
    "data-science-c2-l22": {
        "data_table": table(["Technique", "Example"], [
            ["Polynomial features", "Creates interaction and power terms from existing features"],
        ]),
    },
    "data-science-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["PCA", "Projects data onto orthogonal components that capture the most variance"],
        ]),
    },
    "data-science-c2-l24": {
        "data_table": table(["Type", "Example"], [
            ["Supervised learning", "Predicting house prices from labeled data"], ["Unsupervised learning", "Clustering customers without labels"],
        ]),
    },
    "data-science-c2-l25": {
        "data_table": table(["Algorithm", "Feature"], [
            ["K-Means", "Partitions data into a fixed number of clusters"], ["Hierarchical clustering", "Builds a tree of nested clusters"],
        ]),
    },
    "data-science-c2-l26": {
        "data_table": table(["Model", "Feature"], [
            ["Decision tree", "Splits data using a series of feature-based decisions"], ["Random forest", "An ensemble of decision trees for improved accuracy"],
        ]),
    },
    "data-science-c2-l27": {
        "data_table": table(["Metric", "Formula"], [
            ["Precision", "TP / (TP + FP)"], ["Recall", "TP / (TP + FN)"],
        ]),
        "formulae": ["precision = TP / (TP + FP)", "recall = TP / (TP + FN)"],
    },
    "data-science-c2-l28": {
        "data_table": table(["Metric", "Formula"], [
            ["RMSE", "sqrt(mean((y_true - y_pred)^2))"],
        ]),
        "formulae": ["RMSE = sqrt(mean((y_true - y_pred) ** 2))"],
    },
    "data-science-c2-l29": {
        "data_table": table(["Technique", "Purpose"], [
            ["K-fold cross-validation", "Splits data into k parts to get a robust estimate of model performance"],
        ]),
    },
    "data-science-c2-l30": {
        "data_table": table(["Component", "Meaning"], [
            ["Trend", "The long-term direction of a time series"], ["Seasonality", "Regular, repeating patterns within a time series"],
        ]),
    },
    "data-science-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["ARIMA", "Combines autoregression, differencing, and moving averages to model time series"],
        ]),
    },
    "data-science-c2-l32": {
        "data_table": table(["Task", "Example"], [
            ["Text classification", "Categorizing customer support tickets by topic"],
        ]),
    },
    "data-science-c2-l33": {
        "data_table": table(["Approach", "Feature"], [
            ["Lexicon-based sentiment", "Scores text using a predefined dictionary of sentiment words"],
        ]),
    },
    "data-science-c2-l34": {
        "data_table": table(["Component", "Purpose"], [
            ["Spark", "A distributed computing engine for processing large-scale datasets"],
        ]),
    },
    "data-science-c2-l35": {
        "data_table": table(["Tool", "Purpose"], [
            ["Airflow", "Schedules and monitors multi-step data pipeline workflows"],
        ]),
    },
    "data-science-c2-l36": {
        "data_table": table(["Tool", "Feature"], [
            ["Tableau", "Enables interactive, drag-and-drop data exploration and dashboards"],
        ]),
    },
    "data-science-c2-l37": {
        "data_table": table(["Element", "Purpose"], [
            ["Control group", "Provides a baseline for comparison in an experiment"],
        ]),
    },
    "data-science-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-armed bandit", "Dynamically allocates more traffic to better-performing variants during a test"],
        ]),
    },
    "data-science-c2-l39": {
        "data_table": table(["Method", "Purpose"], [
            ["Propensity score matching", "Reduces confounding bias when estimating causal effects from observational data"],
        ]),
    },
    "data-science-c2-l40": {
        "data_table": table(["Type", "Feature"], [
            ["Collaborative filtering", "Recommends based on similar users' preferences"], ["Content-based filtering", "Recommends based on item attributes"],
        ]),
    },
    "data-science-c2-l41": {
        "data_table": table(["Method", "Feature"], [
            ["Isolation forest", "Detects anomalies by isolating points requiring fewer splits"],
        ]),
    },
    "data-science-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Neural network", "A layered model that learns patterns through weighted, non-linear transformations"],
        ]),
    },
    "data-science-c2-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Wrapping a model in an API", "Allows other systems to request predictions over a network"],
        ]),
    },
    "data-science-c2-l44": {
        "data_table": table(["Tool", "Approach"], [
            ["SHAP", "Assigns each feature a contribution value based on game theory"], ["LIME", "Explains individual predictions with a local approximate model"],
        ]),
    },
    "data-science-c2-l45": {
        "data_table": table(["Technique", "Approach"], [
            ["SMOTE", "Generates synthetic minority class examples"], ["Class weighting", "Penalizes misclassifying minority class examples more heavily"],
        ]),
    },
    "data-science-c2-l46": {
        "data_table": table(["Structure", "Use"], [
            ["Multi-index DataFrame", "Represents hierarchical, higher-dimensional data in a 2D table"],
        ]),
    },
    "data-science-c2-l47": {
        "data_table": table(["Platform", "Feature"], [
            ["Cloud notebooks", "Provide scalable, managed compute for data science without local setup"],
        ]),
    },
    "data-science-c2-l48": {
        "data_table": table(["Stage", "Purpose"], [
            ["Ingestion", "Collects raw data into the pipeline"], ["Serving", "Delivers model predictions to downstream consumers"],
        ]),
    },
    "data-science-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithmic bias", "Systematic unfairness in a model's predictions across different groups"],
        ]),
    },
    "data-science-c2-l50": {
        "data_table": table(["Test", "Use"], [
            ["ANOVA", "Compares means across three or more groups"],
        ]),
    },
    "data-science-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Monte Carlo simulation", "Uses repeated random sampling to estimate a range of possible outcomes"],
        ]),
    },
    "data-science-c2-l52": {
        "data_table": table(["Metric", "Meaning"], [
            ["Centrality", "Measures how important a node is within a network"],
        ]),
    },
    "data-science-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["MLOps", "Applies DevOps practices to reliably build, deploy, and monitor ML models"],
        ]),
    },
    "data-science-c2-l54": {
        "data_table": table(["Method", "Feature"], [
            ["TF-IDF", "Weighs words by frequency in a document relative to their rarity across all documents"], ["Word embeddings", "Represent words as dense vectors capturing semantic meaning"],
        ]),
    },
    "data-science-c2-l55": {
        "data_table": table(["Principle", "Reason"], [
            ["Leading with the takeaway", "Executives need the conclusion before the supporting detail"],
        ]),
    },
    "data-science-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Streaming data", "Continuous, real-time data processed incrementally as it arrives"],
        ]),
    },
    "data-science-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear programming", "Optimizes a linear objective subject to linear constraints"],
        ]),
    },
    "data-science-c2-l58": {
        "data_table": table(["Element", "Purpose"], [
            ["End-to-end project", "Demonstrates the full pipeline from raw data to a deployed, communicated result"],
        ]),
    },
    "data-science-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Survey weighting", "Adjusts sample data so it better represents the target population"],
        ]),
    },
    "data-science-c2-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias-variance tradeoff", "Balancing underfitting (high bias) against overfitting (high variance)"],
        ]),
    },
    "data-science-c2-l61": {
        "data_table": table(["Step", "Purpose"], [
            ["Formulating a testable hypothesis", "Defines a clear, falsifiable statement before collecting evidence"],
        ]),
    },
    "data-science-c2-l62": {
        "data_table": table(["Metric", "Formula"], [
            ["Accuracy", "(TP + TN) / total predictions"],
        ]),
        "formulae": ["accuracy = (TP + TN) / total"],
    },
    "data-science-c2-l63": {
        "data_table": table(["Metric", "Meaning"], [
            ["R-squared", "The proportion of variance in the outcome explained by the model"],
        ]),
    },
    "data-science-c2-l64": {
        "data_table": table(["Method", "Feature"], [
            ["Leave-one-out cross-validation", "Uses a single observation as the test set in each iteration"],
        ]),
    },
    "data-science-c2-l65": {
        "data_table": table(["Approach", "Feature"], [
            ["Model-based sentiment classifier", "Trains on labeled data to predict sentiment more flexibly than a lexicon"],
        ]),
    },
    "data-science-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Profiling a new dataset", "Identifying missing values, outliers, and variable distributions"],
        ]),
    },
    "data-science-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a summary statistic", "Selecting median over mean for a skewed distribution"],
        ]),
    },
    "data-science-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting a correlation coefficient", "Assessing the strength and direction of a relationship between variables"],
        ]),
    },
    "data-science-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a distribution to model data", "Selecting Poisson for count-based event data"],
        ]),
    },
    "data-science-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying the CLT", "Justifying the use of a normal approximation for a sample mean"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Data Science"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Data Science: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Data Science lessons (completing 70/70).")


if __name__ == "__main__":
    main()
