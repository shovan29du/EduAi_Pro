#!/usr/bin/env python3
"""Depth pass, C1 Machine Learning: fill in real, hand-checked
data_table content for the 69 C1 Machine Learning lessons not covered
by the earlier breadth-first batch. Brings C1 Machine Learning to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_machine_learning_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "machine-learning-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Machine learning", "Algorithms that improve automatically through experience with data"],
        ]),
    },
    "machine-learning-c1-l2": {
        "data_table": table(["Step", "Purpose"], [
            ["Cleaning", "Removes errors and inconsistencies"], ["Splitting", "Separates data into training and test sets"],
        ]),
    },
    "machine-learning-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["k-NN", "Classifies a point by the majority vote of its k nearest neighbors"],
        ]),
    },
    "machine-learning-c1-l5": {
        "data_table": table(["Term", "Formula"], [
            ["Sigmoid function", "1 / (1 + e^-z)"],
        ]),
        "formulae": ["p = 1 / (1 + e^-z)"],
    },
    "machine-learning-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Perceptron", "A simple linear binary classifier, the basis of neural networks"],
        ]),
    },
    "machine-learning-c1-l7": {
        "data_table": table(["Algorithm", "Feature"], [
            ["ID3", "Builds trees using information gain"], ["C4.5", "Improves on ID3, handles continuous data"],
        ]),
    },
    "machine-learning-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["CART", "Classification and Regression Trees, builds binary decision trees"],
        ]),
    },
    "machine-learning-c1-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Association rule", "A rule describing relationships between items, e.g. 'if A then B'"],
        ]),
    },
    "machine-learning-c1-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Apriori algorithm", "Finds frequent itemsets by iteratively expanding candidate sets"],
        ]),
    },
    "machine-learning-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Market basket analysis", "Finds products frequently purchased together"],
        ]),
    },
    "machine-learning-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Time series", "Data points collected sequentially over time"],
        ]),
    },
    "machine-learning-c1-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["ARIMA", "AutoRegressive Integrated Moving Average, a statistical time series forecasting model"],
        ]),
    },
    "machine-learning-c1-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Exponential smoothing", "Forecasts by weighting recent observations more heavily"],
        ]),
    },
    "machine-learning-c1-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["k-fold cross-validation", "Splits data into k parts, trains and tests k times for reliable evaluation"],
        ]),
    },
    "machine-learning-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Bias", "Error from overly simple assumptions, causes underfitting"], ["Variance", "Error from sensitivity to training data, causes overfitting"],
        ]),
    },
    "machine-learning-c1-l17": {
        "data_table": table(["Technique", "Effect"], [
            ["L1 (Lasso)", "Can shrink some coefficients to exactly zero"], ["L2 (Ridge)", "Shrinks coefficients but rarely to zero"],
        ]),
    },
    "machine-learning-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Collaborative filtering", "Recommends based on similar users' behavior"],
        ]),
    },
    "machine-learning-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Content-based filtering", "Recommends items similar to what a user liked before"],
        ]),
    },
    "machine-learning-c1-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Matrix factorization", "Decomposes a user-item matrix to uncover latent preferences"],
        ]),
    },
    "machine-learning-c1-l21": {
        "data_table": table(["Type", "Description"], [
            ["Supervised learning", "Learns from labeled data"], ["Unsupervised learning", "Finds patterns in unlabeled data"],
        ]),
    },
    "machine-learning-c1-l22": {
        "data_table": table(["Step", "Purpose"], [
            ["Data collection", "Gathers relevant data"], ["Model training", "Fits the algorithm to the data"], ["Evaluation", "Measures performance"],
        ]),
    },
    "machine-learning-c1-l23": {
        "data_table": table(["Split", "Purpose"], [
            ["Training set", "Trains the model"], ["Validation set", "Tunes hyperparameters"], ["Test set", "Evaluates final performance"],
        ]),
    },
    "machine-learning-c1-l24": {
        "data_table": table(["Formula", "Meaning"], [
            ["y = mx + b", "Predicts y from a linear relationship with x"],
        ]),
        "formulae": ["y = mx + b"],
    },
    "machine-learning-c1-l25": {
        "data_table": table(["Metric", "Meaning"], [
            ["MSE", "Mean Squared Error, average of squared prediction errors"], ["R-squared", "Proportion of variance explained by the model"],
        ]),
    },
    "machine-learning-c1-l26": {
        "data_table": table(["Type", "Example"], [
            ["Binary classification", "Spam or not spam"], ["Multi-class classification", "Classifying an image as cat, dog, or bird"],
        ]),
    },
    "machine-learning-c1-l27": {
        "data_table": table(["Metric", "Meaning"], [
            ["Precision", "Of predicted positives, how many were correct"], ["Recall", "Of actual positives, how many were found"],
        ]),
    },
    "machine-learning-c1-l28": {
        "data_table": table(["Cell", "Meaning"], [
            ["True positive", "Correctly predicted positive"], ["False positive", "Incorrectly predicted positive"],
        ]),
    },
    "machine-learning-c1-l29": {
        "data_table": table(["Technique", "Purpose"], [
            ["Min-max scaling", "Rescales features to a fixed range, e.g. 0 to 1"], ["Standardization", "Rescales to zero mean, unit variance"],
        ]),
    },
    "machine-learning-c1-l30": {
        "data_table": table(["Strategy", "Approach"], [
            ["Imputation", "Fills missing values with mean, median, or predicted values"], ["Deletion", "Removes rows or columns with missing data"],
        ]),
    },
    "machine-learning-c1-l31": {
        "data_table": table(["Method", "Description"], [
            ["One-hot encoding", "Converts categories into binary columns"], ["Label encoding", "Assigns each category an integer"],
        ]),
    },
    "machine-learning-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Overfitting", "Model fits training data too closely, performs poorly on new data"], ["Underfitting", "Model is too simple to capture patterns"],
        ]),
    },
    "machine-learning-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["Hyperparameter", "A configuration setting chosen before training, e.g. learning rate"],
        ]),
    },
    "machine-learning-c1-l34": {
        "data_table": table(["Method", "Description"], [
            ["Grid search", "Tests all combinations of specified hyperparameters"], ["Random search", "Tests random combinations, often more efficient"],
        ]),
    },
    "machine-learning-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["k-Means", "Groups data into k clusters based on similarity"],
        ]),
    },
    "machine-learning-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Hierarchical clustering", "Builds a tree of clusters by merging or splitting groups"],
        ]),
    },
    "machine-learning-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["PCA", "Principal Component Analysis, reduces dimensions while preserving variance"],
        ]),
    },
    "machine-learning-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Anomaly detection", "Identifying data points that deviate significantly from the norm"],
        ]),
    },
    "machine-learning-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Perceptron", "The simplest type of artificial neural network unit"],
        ]),
    },
    "machine-learning-c1-l40": {
        "data_table": table(["Function", "Use"], [
            ["ReLU", "Common activation, outputs 0 for negatives, x for positives"], ["Sigmoid", "Squashes output between 0 and 1"],
        ]),
    },
    "machine-learning-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Gradient descent", "Iteratively adjusts parameters to minimize a loss function"],
        ]),
    },
    "machine-learning-c1-l42": {
        "data_table": table(["Loss Function", "Use"], [
            ["MSE", "Regression tasks"], ["Cross-entropy", "Classification tasks"],
        ]),
    },
    "machine-learning-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Algorithmic bias", "Systematic errors that unfairly favor or disfavor certain groups"],
        ]),
    },
    "machine-learning-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Model interpretability", "The degree to which humans can understand a model's decisions"],
        ]),
    },
    "machine-learning-c1-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature importance", "A measure of how much each input variable contributes to predictions"],
        ]),
    },
    "machine-learning-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Data leakage", "When information from outside the training set improperly influences the model"],
        ]),
    },
    "machine-learning-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Ensemble learning", "Combines multiple models to improve overall performance"],
        ]),
    },
    "machine-learning-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Model deployment", "Making a trained model available for use in production"],
        ]),
    },
    "machine-learning-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["ML pipeline", "An automated sequence of data processing and modeling steps"],
        ]),
    },
    "machine-learning-c1-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Comparing two model versions in production to see which performs better"],
        ]),
    },
    "machine-learning-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Reinforcement learning", "An agent learns by receiving rewards or penalties for its actions"],
        ]),
    },
    "machine-learning-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Semi-supervised learning", "Uses a small amount of labeled data with a larger amount of unlabeled data"],
        ]),
    },
    "machine-learning-c1-l53": {
        "data_table": table(["Chart", "Best For"], [
            ["Histogram", "Showing data distribution"], ["Scatter plot", "Showing relationships between two variables"],
        ]),
    },
    "machine-learning-c1-l54": {
        "data_table": table(["Method", "Description"], [
            ["Z-score", "Flags points far from the mean"], ["IQR method", "Flags points outside the interquartile range"],
        ]),
    },
    "machine-learning-c1-l55": {
        "data_table": table(["Term", "Formula"], [
            ["Cross-entropy loss", "Penalizes confident wrong predictions heavily"],
        ]),
    },
    "machine-learning-c1-l56": {
        "data_table": table(["Concern", "Example"], [
            ["Bias amplification", "A model can reinforce unfair patterns present in its training data"],
        ]),
    },
    "machine-learning-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature engineering", "Creating or transforming variables to improve model performance"],
        ]),
    },
    "machine-learning-c1-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Model versioning", "Tracking changes to trained models over time"],
        ]),
    },
    "machine-learning-c1-l59": {
        "data_table": table(["Technique", "Purpose"], [
            ["Oversampling", "Adds copies of the minority class"], ["Undersampling", "Removes examples from the majority class"],
        ]),
    },
    "machine-learning-c1-l60": {
        "data_table": table(["Library", "Use"], [
            ["scikit-learn", "General-purpose machine learning in Python"], ["TensorFlow", "Deep learning framework"],
        ]),
    },
    "machine-learning-c1-l61": {
        "data_table": table(["Term", "Meaning"], [
            ["Naive Bayes", "A probabilistic classifier assuming feature independence"],
        ]),
        "formulae": ["P(A|B) = P(B|A) * P(A) / P(B)"],
    },
    "machine-learning-c1-l62": {
        "data_table": table(["Parameter", "Effect"], [
            ["k value", "Number of neighbors considered; smaller k is more sensitive to noise"],
        ]),
    },
    "machine-learning-c1-l63": {
        "data_table": table(["Model Complexity", "Effect"], [
            ["High complexity", "Low bias, high variance"], ["Low complexity", "High bias, low variance"],
        ]),
    },
    "machine-learning-c1-l64": {
        "data_table": table(["Approach", "Example"], [
            ["User-based collaborative filtering", "Recommends based on similar users"],
        ]),
    },
    "machine-learning-c1-l65": {
        "data_table": table(["Approach", "Example"], [
            ["Content-based filtering", "Recommends movies with similar genres to ones a user liked"],
        ]),
    },
    "machine-learning-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Identifying an ML problem type", "Deciding whether a task is classification or regression"],
        ]),
    },
    "machine-learning-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning a sample dataset", "Handling missing values and duplicate rows"],
        ]),
    },
    "machine-learning-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Applying Naive Bayes", "Classifying an email as spam using word probabilities"],
        ]),
    },
    "machine-learning-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a k value", "Testing different k values for a k-NN classifier"],
        ]),
    },
    "machine-learning-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Interpreting logistic regression output", "Converting a model's output into a probability and decision"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Machine Learning"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Machine Learning: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Machine Learning lessons (completing 70/70).")


if __name__ == "__main__":
    main()
