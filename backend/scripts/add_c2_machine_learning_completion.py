#!/usr/bin/env python3
"""Depth pass, C2 Machine Learning: fill in real, hand-checked
data_table/formulae content for the 69 C2 Machine Learning lessons not
covered by the earlier breadth-first batch. Brings C2 Machine Learning
to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_machine_learning_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "machine-learning-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature engineering", "Transforming raw data into inputs that better represent the underlying problem"],
        ]),
    },
    "machine-learning-c2-l2": {
        "data_table": table(["Type", "Formula"], [
            ["Linear regression", "y = b0 + b1*x"],
        ]),
        "formulae": ["y = b0 + b1 * x"],
    },
    "machine-learning-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Kernel trick", "Computes similarity in a high-dimensional space without explicitly transforming the data"],
        ]),
    },
    "machine-learning-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Random forest", "An ensemble of decision trees trained on random subsets of data and features"],
        ]),
    },
    "machine-learning-c2-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Gradient boosting", "Sequentially adds models that correct the errors of previous ones"],
        ]),
    },
    "machine-learning-c2-l7": {
        "data_table": table(["Feature", "Benefit"], [
            ["XGBoost regularization", "Reduces overfitting through L1/L2 penalties on tree complexity"],
        ]),
    },
    "machine-learning-c2-l8": {
        "data_table": table(["Feature", "Benefit"], [
            ["Histogram-based splitting", "Speeds up training by bucketing continuous features"],
        ]),
    },
    "machine-learning-c2-l9": {
        "data_table": table(["Feature", "Benefit"], [
            ["Native categorical support", "CatBoost handles categorical features without manual encoding"],
        ]),
    },
    "machine-learning-c2-l10": {
        "data_table": table(["Method", "Feature"], [
            ["Bagging", "Trains models in parallel on bootstrapped samples to reduce variance"], ["Boosting", "Trains models sequentially to reduce bias"],
        ]),
    },
    "machine-learning-c2-l11": {
        "data_table": table(["Method", "Feature"], [
            ["Stacking", "Trains a meta-model to combine base model predictions"],
        ]),
    },
    "machine-learning-c2-l12": {
        "data_table": table(["Method", "Feature"], [
            ["Filter method", "Selects features based on statistical properties, independent of the model"], ["Wrapper method", "Selects features based on model performance"],
        ]),
    },
    "machine-learning-c2-l13": {
        "data_table": table(["Approach", "Tradeoff"], [
            ["Filter", "Fast but ignores feature interactions"], ["Wrapper", "More accurate but computationally expensive"],
        ]),
    },
    "machine-learning-c2-l14": {
        "data_table": table(["Strategy", "Meaning"], [
            ["One-vs-rest", "Trains one binary classifier per class against all others"],
        ]),
    },
    "machine-learning-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-label classification", "Assigns multiple non-exclusive labels to a single instance"],
        ]),
    },
    "machine-learning-c2-l16": {
        "data_table": table(["Metric", "Use"], [
            ["F1 score", "Balances precision and recall for imbalanced classes"],
        ]),
        "formulae": ["F1 = 2 * (precision * recall) / (precision + recall)"],
    },
    "machine-learning-c2-l17": {
        "data_table": table(["Curve", "Shows"], [
            ["Precision-recall curve", "Tradeoff between precision and recall across thresholds"], ["ROC curve", "Tradeoff between true positive rate and false positive rate"],
        ]),
    },
    "machine-learning-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Model calibration", "Adjusting predicted probabilities so they reflect true likelihoods"],
        ]),
    },
    "machine-learning-c2-l19": {
        "data_table": table(["Technique", "Approach"], [
            ["Oversampling", "Duplicates or synthesizes minority class examples"], ["Undersampling", "Removes majority class examples"],
        ]),
    },
    "machine-learning-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["SMOTE", "Generates synthetic minority class samples by interpolating between existing ones"],
        ]),
    },
    "machine-learning-c2-l21": {
        "data_table": table(["Term", "Meaning"], [
            ["Gaussian mixture model", "Models data as a combination of multiple normal distributions"],
        ]),
    },
    "machine-learning-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["DBSCAN", "Clusters points based on density, identifying outliers as noise"],
        ]),
    },
    "machine-learning-c2-l23": {
        "data_table": table(["Method", "Feature"], [
            ["t-SNE", "Preserves local structure for visualization"], ["UMAP", "Preserves both local and some global structure, often faster"],
        ]),
    },
    "machine-learning-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear Discriminant Analysis", "Finds a linear combination of features that best separates classes"],
        ]),
    },
    "machine-learning-c2-l25": {
        "data_table": table(["Term", "Method"], [
            ["Multicollinearity", "Highly correlated predictors, addressed with ridge or lasso regression"],
        ]),
        "formulae": ["ridge_loss = mse + alpha * sum(w**2)"],
    },
    "machine-learning-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Generalized linear model", "Extends linear regression to non-normal response distributions using a link function"],
        ]),
    },
    "machine-learning-c2-l27": {
        "data_table": table(["Curve", "Reveals"], [
            ["Learning curve", "Shows how training and validation performance change with dataset size"],
        ]),
    },
    "machine-learning-c2-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Nested cross-validation", "Uses an inner loop for hyperparameter tuning and an outer loop for unbiased evaluation"],
        ]),
    },
    "machine-learning-c2-l29": {
        "data_table": table(["Method", "Advantage"], [
            ["Bayesian optimization", "Uses prior results to intelligently choose the next hyperparameters to try"],
        ]),
    },
    "machine-learning-c2-l30": {
        "data_table": table(["Layer", "Role"], [
            ["Input layer", "Receives raw feature values"], ["Hidden layer", "Learns intermediate representations"], ["Output layer", "Produces the final prediction"],
        ]),
    },
    "machine-learning-c2-l31": {
        "data_table": table(["Step", "Purpose"], [
            ["Backpropagation", "Computes gradients by propagating error backward through the network"],
        ]),
    },
    "machine-learning-c2-l32": {
        "data_table": table(["Layer", "Purpose"], [
            ["Convolutional layer", "Extracts local spatial features using filters"],
        ]),
    },
    "machine-learning-c2-l33": {
        "data_table": table(["Feature", "Detail"], [
            ["Recurrent connection", "Passes information from one time step to the next"],
        ]),
    },
    "machine-learning-c2-l34": {
        "data_table": table(["Gate", "Purpose"], [
            ["Forget gate", "Decides what information to discard from memory"], ["Input gate", "Decides what new information to store"],
        ]),
    },
    "machine-learning-c2-l35": {
        "data_table": table(["Technique", "Purpose"], [
            ["Dropout", "Randomly deactivates neurons to reduce overfitting"], ["Batch normalization", "Normalizes activations to stabilize training"],
        ]),
    },
    "machine-learning-c2-l36": {
        "data_table": table(["Optimizer", "Feature"], [
            ["SGD with momentum", "Accelerates convergence by accumulating past gradients"], ["Adam", "Adapts the learning rate per parameter"],
        ]),
    },
    "machine-learning-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Transfer learning", "Reuses a model trained on one task as a starting point for a related task"],
        ]),
    },
    "machine-learning-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Autoencoder", "Learns compressed data representations by reconstructing its own input"],
        ]),
    },
    "machine-learning-c2-l39": {
        "data_table": table(["Component", "Role"], [
            ["Generator", "Produces synthetic samples"], ["Discriminator", "Judges whether samples are real or fake"],
        ]),
    },
    "machine-learning-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Attention mechanism", "Weighs the importance of different input elements dynamically"],
        ]),
    },
    "machine-learning-c2-l41": {
        "data_table": table(["Metric", "Meaning"], [
            ["Demographic parity", "Requires equal positive prediction rates across groups"],
        ]),
    },
    "machine-learning-c2-l42": {
        "data_table": table(["Tool", "Approach"], [
            ["SHAP", "Assigns each feature a contribution value based on game theory"], ["LIME", "Explains individual predictions using a local approximate model"],
        ]),
    },
    "machine-learning-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Recursive feature elimination", "Iteratively removes the least important features and retrains the model"],
        ]),
    },
    "machine-learning-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Data leakage", "Information from outside the training set improperly influences the model"],
        ]),
    },
    "machine-learning-c2-l45": {
        "data_table": table(["Method", "Feature"], [
            ["Weighted averaging", "Combines model predictions with weights reflecting individual accuracy"],
        ]),
    },
    "machine-learning-c2-l46": {
        "data_table": table(["Step", "Purpose"], [
            ["Wrapping a model in an API", "Enables applications to request predictions over a network"],
        ]),
    },
    "machine-learning-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["ML pipeline", "Automates the sequence from data preprocessing to model training and evaluation"],
        ]),
    },
    "machine-learning-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Online learning", "Updates a model incrementally as new data arrives, rather than retraining from scratch"],
        ]),
    },
    "machine-learning-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-armed bandit", "Balances exploring unknown options against exploiting known good ones"],
        ]),
    },
    "machine-learning-c2-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Markov decision process", "A framework modeling decision-making with states, actions, and rewards"],
        ]),
    },
    "machine-learning-c2-l51": {
        "data_table": table(["Term", "Formula"], [
            ["Q-learning", "Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') − Q(s,a)]"],
        ]),
        "formulae": ["Q[s][a] += alpha * (r + gamma * max(Q[s_next]) - Q[s][a])"],
    },
    "machine-learning-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Pseudo-labeling", "Uses a model's confident predictions on unlabeled data as new training labels"],
        ]),
    },
    "machine-learning-c2-l53": {
        "data_table": table(["Plot", "Reveals"], [
            ["Confusion matrix", "Where a classifier confuses one class for another"], ["Residual plot", "Whether regression errors show systematic patterns"],
        ]),
    },
    "machine-learning-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Isolation forest", "Detects anomalies by isolating points that require fewer splits"],
        ]),
    },
    "machine-learning-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Focal loss", "Down-weights easy examples so training focuses on hard, minority-class examples"],
        ]),
    },
    "machine-learning-c2-l56": {
        "data_table": table(["Technique", "Purpose"], [
            ["Reweighting", "Adjusts training sample weights to reduce group-based unfairness"],
        ]),
    },
    "machine-learning-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Automated feature engineering", "Systematically generates and selects candidate features programmatically"],
        ]),
    },
    "machine-learning-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Model drift", "A model's performance degrades as real-world data diverges from training data"],
        ]),
    },
    "machine-learning-c2-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Cost-sensitive learning", "Assigns higher misclassification cost to the minority class during training"],
        ]),
    },
    "machine-learning-c2-l60": {
        "data_table": table(["Framework", "Strength"], [
            ["scikit-learn", "Simple API, ideal for classical ML"], ["PyTorch", "Flexible, widely used for deep learning research"],
        ]),
    },
    "machine-learning-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Fitting a GMM", "Modeling a dataset with overlapping, non-spherical clusters"],
        ]),
    },
    "machine-learning-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Tuning DBSCAN parameters", "Adjusting epsilon and minPts for a given dataset's density"],
        ]),
    },
    "machine-learning-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Comparing LDA and PCA", "Choosing a supervised versus unsupervised dimensionality reduction method"],
        ]),
    },
    "machine-learning-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Debugging vanishing gradients", "Diagnosing why an RNN fails to learn long-range dependencies"],
        ]),
    },
    "machine-learning-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Using an autoencoder for anomaly detection", "Flagging inputs with high reconstruction error"],
        ]),
    },
    "machine-learning-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Tuning isolation forest depth", "Balancing sensitivity and false positive rate for anomaly detection"],
        ]),
    },
    "machine-learning-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Engineering a new feature", "Deriving a ratio feature that improves model performance"],
        ]),
    },
    "machine-learning-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Diagnosing regression fit", "Checking residuals for signs of a non-linear relationship"],
        ]),
    },
    "machine-learning-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Choosing an SVM kernel", "Selecting linear versus RBF based on data separability"],
        ]),
    },
    "machine-learning-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying the kernel trick", "Classifying non-linearly separable data without explicit transformation"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Machine Learning"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Machine Learning: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Machine Learning lessons (completing 70/70).")


if __name__ == "__main__":
    main()
