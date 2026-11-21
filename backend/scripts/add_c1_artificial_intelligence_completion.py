#!/usr/bin/env python3
"""Depth pass, C1 Artificial Intelligence: fill in real, hand-checked
data_table content for the 69 C1 Artificial Intelligence lessons not
covered by the earlier breadth-first batch. Brings C1 Artificial
Intelligence to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_artificial_intelligence_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Artificial intelligence", "Computer systems performing tasks that normally require human intelligence"],
        ]),
    },
    "artificial-intelligence-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Intelligent agent", "A system that perceives its environment and acts to achieve goals"],
        ]),
    },
    "artificial-intelligence-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["CSP", "Constraint Satisfaction Problem, finding values that satisfy a set of constraints"],
        ]),
    },
    "artificial-intelligence-c1-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Backtracking search", "Explores solutions incrementally, undoing choices that violate constraints"],
        ]),
    },
    "artificial-intelligence-c1-l6": {
        "data_table": table(["Algorithm", "Approach"], [
            ["Hill climbing", "Moves toward better neighboring solutions"], ["Simulated annealing", "Allows occasional worse moves to escape local optima"],
        ]),
    },
    "artificial-intelligence-c1-l7": {
        "data_table": table(["Component", "Role"], [
            ["Knowledge base", "Stores facts and rules"], ["Inference engine", "Applies rules to derive conclusions"],
        ]),
    },
    "artificial-intelligence-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Fuzzy logic", "Handles reasoning with degrees of truth rather than strict true/false"],
        ]),
    },
    "artificial-intelligence-c1-l9": {
        "data_table": table(["Era", "Feature"], [
            ["Symbolic AI", "Rule-based reasoning, dominant mid-20th century"], ["Deep learning", "Neural network-based, dominant since 2010s"],
        ]),
    },
    "artificial-intelligence-c1-l10": {
        "data_table": table(["Fact", "Detail"], [
            ["Turing Test", "Proposed by Alan Turing, 1950, tests if a machine's responses are indistinguishable from a human's"],
        ]),
    },
    "artificial-intelligence-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Case-based reasoning", "Solves new problems using solutions to similar past problems"],
        ]),
    },
    "artificial-intelligence-c1-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Recommender system", "Suggests items to users based on preferences or behavior"],
        ]),
    },
    "artificial-intelligence-c1-l13": {
        "data_table": table(["Approach", "Description"], [
            ["Content-based filtering", "Recommends items similar to what a user liked before"],
        ]),
    },
    "artificial-intelligence-c1-l14": {
        "data_table": table(["Application", "Example"], [
            ["Medical imaging analysis", "AI assists in detecting abnormalities in scans"],
        ]),
    },
    "artificial-intelligence-c1-l15": {
        "data_table": table(["Application", "Example"], [
            ["Fraud detection", "AI flags unusual transaction patterns"],
        ]),
    },
    "artificial-intelligence-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Kinematics", "The study of motion of robotic joints and links, without regard to forces"],
        ]),
    },
    "artificial-intelligence-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Computer vision", "Enables computers to interpret and understand visual information"],
        ]),
    },
    "artificial-intelligence-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Speech recognition", "Converts spoken language into text"],
        ]),
    },
    "artificial-intelligence-c1-l19": {
        "data_table": table(["Term", "Meaning"], [
            ["Human-robot interaction", "Studies how humans and robots communicate and collaborate"],
        ]),
    },
    "artificial-intelligence-c1-l20": {
        "data_table": table(["Bias Type", "Example"], [
            ["Confirmation bias", "Designers favor data confirming existing assumptions"],
        ]),
    },
    "artificial-intelligence-c1-l21": {
        "data_table": table(["Paradigm", "Description"], [
            ["Supervised learning", "Learns from labeled data"], ["Unsupervised learning", "Finds patterns in unlabeled data"], ["Reinforcement learning", "Learns via reward signals"],
        ]),
    },
    "artificial-intelligence-c1-l22": {
        "data_table": table(["Task", "Output"], [
            ["Classification", "Predicts a category"], ["Regression", "Predicts a continuous value"],
        ]),
    },
    "artificial-intelligence-c1-l23": {
        "data_table": table(["Formula", "Meaning"], [
            ["y = mx + b", "Predicts y from a linear relationship with x"],
        ]),
        "formulae": ["y = mx + b"],
    },
    "artificial-intelligence-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Logistic regression", "Predicts the probability of a binary outcome"],
        ]),
        "formulae": ["p = 1 / (1 + e^-z)"],
    },
    "artificial-intelligence-c1-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Decision tree", "A model that splits data based on feature values to make predictions"],
        ]),
    },
    "artificial-intelligence-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["k-NN", "Classifies a point based on the majority class of its k nearest neighbors"],
        ]),
    },
    "artificial-intelligence-c1-l27": {
        "data_table": table(["Component", "Role"], [
            ["Neuron", "Basic computational unit"], ["Layer", "A group of neurons processing data together"],
        ]),
    },
    "artificial-intelligence-c1-l28": {
        "data_table": table(["Fact", "Detail"], [
            ["Perceptron limitation", "Cannot solve non-linearly separable problems like XOR"],
        ]),
    },
    "artificial-intelligence-c1-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Backpropagation", "Algorithm that adjusts network weights by propagating error backward"], ["Gradient descent", "Iteratively adjusts parameters to minimize error"],
        ]),
    },
    "artificial-intelligence-c1-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Overfitting", "Model fits training data too closely, performs poorly on new data"], ["Underfitting", "Model is too simple to capture patterns"],
        ]),
    },
    "artificial-intelligence-c1-l31": {
        "data_table": table(["Split", "Purpose"], [
            ["Training set", "Trains the model"], ["Validation set", "Tunes hyperparameters"], ["Test set", "Evaluates final performance"],
        ]),
    },
    "artificial-intelligence-c1-l32": {
        "data_table": table(["Metric", "Meaning"], [
            ["Accuracy", "Percentage of correct predictions"], ["Precision", "Of predicted positives, how many were correct"], ["Recall", "Of actual positives, how many were found"],
        ]),
    },
    "artificial-intelligence-c1-l33": {
        "data_table": table(["Term", "Meaning"], [
            ["k-Means", "Groups data into k clusters based on similarity"],
        ]),
    },
    "artificial-intelligence-c1-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["PCA", "Principal Component Analysis, reduces data to fewer dimensions while preserving variance"],
        ]),
    },
    "artificial-intelligence-c1-l35": {
        "data_table": table(["Term", "Meaning"], [
            ["NLP", "Natural Language Processing, enables computers to understand human language"],
        ]),
    },
    "artificial-intelligence-c1-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Bag-of-words", "Represents text as word frequency counts, ignoring order"],
        ]),
    },
    "artificial-intelligence-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Word embedding", "Represents words as dense vectors capturing semantic meaning"],
        ]),
    },
    "artificial-intelligence-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["CNN", "Convolutional Neural Network, effective for image data"],
        ]),
    },
    "artificial-intelligence-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["RNN", "Recurrent Neural Network, effective for sequential data like text or time series"],
        ]),
    },
    "artificial-intelligence-c1-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Reinforcement learning", "An agent learns by receiving rewards or penalties for actions"],
        ]),
    },
    "artificial-intelligence-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["MDP", "Markov Decision Process, a framework for modeling decision-making with states, actions, and rewards"],
        ]),
    },
    "artificial-intelligence-c1-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Knowledge representation", "How AI systems store and structure facts about the world"],
        ]),
    },
    "artificial-intelligence-c1-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Semantic network", "Represents knowledge as nodes and labeled relationships"], ["Ontology", "A formal representation of concepts and their relationships"],
        ]),
    },
    "artificial-intelligence-c1-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Bayesian network", "A graphical model representing probabilistic relationships between variables"],
        ]),
    },
    "artificial-intelligence-c1-l45": {
        "data_table": table(["Formula", "Use"], [
            ["Bayes' theorem", "Updates the probability of a hypothesis given new evidence"],
        ]),
        "formulae": ["P(A|B) = P(B|A) * P(A) / P(B)"],
    },
    "artificial-intelligence-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["AI planning", "Determining a sequence of actions to achieve a goal"],
        ]),
    },
    "artificial-intelligence-c1-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["NLG", "Natural Language Generation, produces human-readable text from data"],
        ]),
    },
    "artificial-intelligence-c1-l48": {
        "data_table": table(["Component", "Purpose"], [
            ["Intent recognition", "Identifies what the user wants"], ["Dialogue management", "Determines the chatbot's response flow"],
        ]),
    },
    "artificial-intelligence-c1-l49": {
        "data_table": table(["Application", "Example"], [
            ["Self-driving cars", "Use sensors and AI to navigate without human input"],
        ]),
    },
    "artificial-intelligence-c1-l50": {
        "data_table": table(["Concern", "Example"], [
            ["Accountability", "Who is responsible when an automated decision causes harm?"],
        ]),
    },
    "artificial-intelligence-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Data bias", "Training data that reflects and perpetuates societal biases"],
        ]),
    },
    "artificial-intelligence-c1-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Explainable AI", "AI systems designed so their decisions can be understood by humans"],
        ]),
    },
    "artificial-intelligence-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Model deployment", "Making a trained model available for real-world use"],
        ]),
    },
    "artificial-intelligence-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["Feature engineering", "Creating or transforming input variables to improve model performance"],
        ]),
    },
    "artificial-intelligence-c1-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Cross-validation", "Splits data into multiple folds to more reliably evaluate a model"],
        ]),
    },
    "artificial-intelligence-c1-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Ensemble method", "Combines multiple models to improve overall prediction accuracy"],
        ]),
    },
    "artificial-intelligence-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["SVM", "Support Vector Machine, finds the optimal boundary separating classes"],
        ]),
    },
    "artificial-intelligence-c1-l58": {
        "data_table": table(["Application", "Example"], [
            ["Time series forecasting", "Predicting future stock prices or demand from historical data"],
        ]),
    },
    "artificial-intelligence-c1-l59": {
        "data_table": table(["Hardware", "Best For"], [
            ["CPU", "General-purpose sequential tasks"], ["GPU", "Parallel processing, well-suited to neural networks"], ["TPU", "Specialized for tensor operations"],
        ]),
    },
    "artificial-intelligence-c1-l60": {
        "data_table": table(["Subfield", "Focus"], [
            ["Machine learning engineer", "Builds and deploys ML systems"], ["Data scientist", "Analyzes data to extract insights"],
        ]),
    },
    "artificial-intelligence-c1-l61": {
        "data_table": table(["Technique", "Purpose"], [
            ["Constraint propagation", "Reduces the search space in a CSP before searching"],
        ]),
    },
    "artificial-intelligence-c1-l62": {
        "data_table": table(["Approach", "Description"], [
            ["Collaborative filtering", "Recommends items based on similar users' preferences"],
        ]),
    },
    "artificial-intelligence-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Diagnostic support", "AI flags patterns in patient data for clinician review"],
        ]),
    },
    "artificial-intelligence-c1-l64": {
        "data_table": table(["Term", "Meaning"], [
            ["Activation function", "Introduces non-linearity into a neural network, e.g. ReLU or sigmoid"],
        ]),
    },
    "artificial-intelligence-c1-l65": {
        "data_table": table(["Term", "Meaning"], [
            ["Learning rate", "Controls how much weights are adjusted during gradient descent"],
        ]),
    },
    "artificial-intelligence-c1-l66": {
        "data_table": table(["Concept", "Meaning"], [
            ["Exploration vs exploitation", "Balancing trying new actions against using known good ones"],
        ]),
    },
    "artificial-intelligence-c1-l67": {
        "data_table": table(["Component", "Meaning"], [
            ["State", "The current situation"], ["Action", "A choice the agent can make"], ["Reward", "Feedback signal for an action"],
        ]),
    },
    "artificial-intelligence-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Identifying AI applications", "Classifying real-world tools as narrow or general AI"],
        ]),
    },
    "artificial-intelligence-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Modeling an agent", "Defining the percepts, actions, and goals of a sample intelligent agent"],
        ]),
    },
    "artificial-intelligence-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying propositional logic", "Evaluating a truth table for a sample logical statement"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Artificial Intelligence"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Artificial Intelligence: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Artificial Intelligence lessons (completing 70/70).")


if __name__ == "__main__":
    main()
