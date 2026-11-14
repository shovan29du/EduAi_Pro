#!/usr/bin/env python3
"""Depth pass, M1 Machine Learning: fill in real, hand-checked
data_table content for the 119 M1 Machine Learning lessons not
covered by the earlier breadth-first batch. Brings M1 Machine
Learning to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning MLOps,
generative modeling theory, representation learning, reinforcement
learning, and modern training/scaling techniques; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_machine_learning_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Hyperparameter", "A setting configured before training (e.g. learning rate)"],
    ["Bayesian optimization", "Uses a probabilistic model to efficiently search hyperparameter space"],
])

CHARTS: dict[str, dict] = {
    "machine-learning-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Model deployment", "Making a trained model available to serve predictions in production"],
    ])},
    "machine-learning-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["MLOps", "Practices for reliably building, deploying, and monitoring ML systems"],
    ])},
    "machine-learning-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["AutoML", "Automates model selection, feature engineering, and tuning"],
    ])},
    "machine-learning-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automates the design of a network's structure for a pipeline"],
    ])},
    "machine-learning-m1-l6": {"data_table": table(["Concept", "Detail"], [
        ["System design at scale", "Balances latency, throughput, and cost across training and serving infrastructure"],
    ])},
    "machine-learning-m1-l7": {"data_table": table(["Strategy", "Feature"], [
        ["Data parallelism", "Splits a batch across devices, each holding a full model copy"],
        ["Model parallelism", "Splits the model itself across devices"],
    ])},
    "machine-learning-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Inference optimization", "Reduces latency and cost when serving predictions, e.g. via batching or quantization"],
    ])},
    "machine-learning-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Feature store", "A centralized system for managing and serving ML features consistently"],
    ])},
    "machine-learning-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Data versioning", "Tracks changes to training datasets over time for reproducibility"],
    ])},
    "machine-learning-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Model drift", "A deployed model's performance degrades as real-world data distribution shifts"],
    ])},
    "machine-learning-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["A/B testing", "Compares two model versions on live traffic to measure real-world impact"],
    ])},
    "machine-learning-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Reproducibility", "Getting the same result when an experiment is re-run under the same conditions"],
    ])},
    "machine-learning-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Experiment tracking", "Logs hyperparameters, metrics, and artifacts across training runs"],
    ])},
    "machine-learning-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["CI for ML", "Automatically tests and validates model code and data pipelines on each change"],
    ])},
    "machine-learning-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Model rollback", "Reverting to a previous model version when a new one underperforms"],
    ])},
    "machine-learning-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Edge deployment", "Running inference directly on a device rather than a remote server"],
    ])},
    "machine-learning-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Real-time inference", "Serving predictions with strict low-latency requirements"],
    ])},
    "machine-learning-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Distributed data processing", "Preprocesses training data across a cluster to handle large-scale datasets"],
    ])},
    "machine-learning-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["ML capstone", "Integrates data pipeline, modeling, evaluation, and deployment into one project"],
    ])},
    "machine-learning-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Variational autoencoder", "Learns a compressed, probabilistic latent representation of data"],
    ])},
    "machine-learning-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["GAN training dynamics", "A generator and discriminator compete in a minimax game to improve sample realism"],
    ])},
    "machine-learning-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Diffusion model", "Generates data by learning to reverse a gradual noising process"],
    ])},
    "machine-learning-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Energy-based model", "Learns a scalar energy function that is low for likely data"],
    ])},
    "machine-learning-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Spectral graph convolution", "Applies convolution in the graph's spectral (eigenvalue) domain"],
    ])},
    "machine-learning-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Sparse transformer", "Reduces attention's quadratic cost by attending to a limited subset of tokens"],
    ])},
    "machine-learning-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts", "Routes each input to a subset of specialized sub-networks"],
    ])},
    "machine-learning-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Neural tangent kernel", "Describes an infinitely wide network's training dynamics as kernel regression"],
    ])},
    "machine-learning-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["PAC-Bayes bound", "A generalization bound that incorporates a prior over hypotheses"],
    ])},
    "machine-learning-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Double descent", "Test error can decrease, increase, then decrease again as model capacity grows"],
    ])},
    "machine-learning-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Lottery ticket hypothesis", "A dense network contains a sparse subnetwork that trains to comparable accuracy"],
    ])},
    "machine-learning-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to mimic a larger teacher model"],
    ])},
    "machine-learning-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Quantization", "Reduces numeric precision of weights/activations to shrink and speed up a model"],
    ])},
    "machine-learning-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["MAML", "Learns an initialization that adapts quickly to new tasks with few gradient steps"],
    ])},
    "machine-learning-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Few-shot learning", "Learning a new task or class from only a handful of labeled examples"],
    ])},
    "machine-learning-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Zero-shot learning", "Classifying unseen classes using semantic descriptions rather than labeled examples"],
    ])},
    "machine-learning-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive learning", "Learns embeddings by pulling similar examples together, dissimilar ones apart"],
    ])},
    "machine-learning-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Self-supervised learning", "Learns representations from unlabeled data using automatically generated targets"],
    ])},
    "machine-learning-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Masked autoencoding", "Reconstructs randomly hidden parts of an input to learn representations"],
    ])},
    "machine-learning-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Multi-task learning", "Trains one model to solve several related tasks jointly, sharing representations"],
    ])},
    "machine-learning-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Catastrophic forgetting", "A model loses earlier learned skills when trained on new tasks"],
    ])},
    "machine-learning-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Domain adaptation", "Adjusts a model trained on one data distribution to perform well on another"],
    ])},
    "machine-learning-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual reasoning", "Asks what a model's prediction would have been under a different input"],
    ])},
    "machine-learning-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Uncertainty quantification", "Estimates how confident a model's prediction should be"],
    ])},
    "machine-learning-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian deep learning", "Treats network weights as distributions to capture predictive uncertainty"],
    ])},
    "machine-learning-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Gaussian process", "A non-parametric model defining a distribution over functions"],
    ])},
    "machine-learning-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Conformal prediction", "Produces prediction sets with a guaranteed coverage probability"],
    ])},
    "machine-learning-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Certified robustness", "Mathematically guarantees a model's prediction is stable within a bounded input perturbation"],
    ])},
    "machine-learning-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Backdoor attack", "Poisons training data so a model misbehaves only on a hidden trigger pattern"],
    ])},
    "machine-learning-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Membership inference attack", "Infers whether a specific record was part of a model's training data"],
    ])},
    "machine-learning-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "Adds calibrated noise so individual training points cannot be reverse-engineered"],
    ])},
    "machine-learning-m1-l52": {"data_table": table(["Metric", "Measures"], [
        ["Demographic parity", "Whether predicted outcomes are distributed similarly across protected groups"],
    ])},
    "machine-learning-m1-l53": {"data_table": table(["Method", "Feature"], [
        ["SHAP", "Assigns each feature a contribution value based on cooperative game theory"],
        ["LIME", "Explains a single prediction by fitting a simple local surrogate model"],
    ])},
    "machine-learning-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Mechanistic interpretability", "Reverse-engineers the internal circuits a network uses to compute outputs"],
    ])},
    "machine-learning-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Policy gradient", "Directly optimizes a policy's parameters via gradient ascent on expected reward"],
    ])},
    "machine-learning-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Actor-critic", "Combines a policy (actor) with a value estimator (critic) to reduce variance"],
    ])},
    "machine-learning-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Model-based RL", "Learns a model of the environment's dynamics to plan or simulate rollouts"],
    ])},
    "machine-learning-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Offline RL", "Learns a policy purely from a fixed dataset, without further environment interaction"],
    ])},
    "machine-learning-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent RL", "Multiple learning agents interact, producing emergent cooperative or competitive strategy"],
    ])},
    "machine-learning-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Inverse RL", "Infers a reward function from observed expert behavior"],
    ])},
    "machine-learning-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Exploration strategy", "Balances trying new actions against exploiting known-good ones"],
    ])},
    "machine-learning-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical RL", "Decomposes a task into higher-level goals and lower-level sub-policies"],
    ])},
    "machine-learning-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Reward shaping", "Modifies a reward signal to make learning faster without changing the optimal policy"],
    ])},
    "machine-learning-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["RLHF", "Reinforcement learning from human feedback; tunes a model using human preference signals"],
    ])},
    "machine-learning-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Ensemble learning", "Combines multiple models to improve accuracy and robustness over any single model"],
    ])},
    "machine-learning-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Gradient boosting", "Builds an ensemble sequentially, each tree correcting the previous ensemble's errors"],
    ])},
    "machine-learning-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Kernel method", "Implicitly maps data to a higher-dimensional space to make it linearly separable"],
    ])},
    "machine-learning-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Manifold learning", "Recovers a low-dimensional structure assumed to underlie high-dimensional data"],
    ])},
    "machine-learning-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Spectral clustering", "Clusters data using eigenvectors of a similarity graph's Laplacian matrix"],
    ])},
    "machine-learning-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection", "Identifies data points that deviate significantly from expected patterns"],
    ])},
    "machine-learning-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Time series forecasting", "Predicts future values of a sequence using its historical pattern"],
    ])},
    "machine-learning-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["State-space model", "Models sequences via latent states evolving over time, efficient for long contexts"],
    ])},
    "machine-learning-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Neural ODE", "Models a network's hidden state as a continuous-time differential equation"],
    ])},
    "machine-learning-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Physics-informed neural network", "Incorporates known physical equations as constraints during training"],
    ])},
    "machine-learning-m1-l75": {"data_table": table(["Strategy", "Feature"], [
        ["Reinforcement-based NAS", "Trains a controller to propose architectures rewarded by validation performance"],
    ])},
    "machine-learning-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Hyperparameter optimization at scale", "Parallelizes search across many machines using strategies like population-based training"],
    ])},
    "machine-learning-m1-l77": {"data_table": table(["Strategy", "Feature"], [
        ["Data parallelism", "Splits a batch across devices, each holding a full model copy"],
        ["Model parallelism", "Splits the model's layers or parameters across devices"],
    ])},
    "machine-learning-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Pipeline parallelism", "Splits a model into stages processed by different devices in an overlapping pipeline"],
    ])},
    "machine-learning-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Gradient compression", "Reduces communication cost in distributed training by compressing gradients"],
    ])},
    "machine-learning-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning", "Trains a shared model across decentralized devices without centralizing raw data"],
    ])},
    "machine-learning-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Curriculum learning", "Orders training examples from easy to hard to speed up learning"],
    ])},
    "machine-learning-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Active learning", "A model selects the most informative unlabeled examples to query next"],
    ])},
    "machine-learning-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Weak supervision", "Uses noisy, programmatic labeling rules instead of hand-labeled data"],
    ])},
    "machine-learning-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Semi-supervised learning", "Combines a small labeled set with a larger unlabeled set during training"],
    ])},
    "machine-learning-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Pseudo-labeling", "Uses a model's own confident predictions on unlabeled data as extra training labels"],
    ])},
    "machine-learning-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Tabular representation learning", "Learns dense embeddings for structured, table-formatted data"],
    ])},
    "machine-learning-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Probabilistic graphical model inference", "Computes marginal or conditional probabilities over a structured model"],
    ])},
    "machine-learning-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Markov Chain Monte Carlo", "Samples from a complex distribution by constructing a Markov chain"],
    ])},
    "machine-learning-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Optimal transport", "Studies the cheapest way to transform one distribution into another"],
    ])},
    "machine-learning-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Information-theoretic representation learning", "Uses concepts like mutual information to guide what a model's features should encode"],
    ])},
    "machine-learning-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal representation learning", "Learns a shared embedding space across data types such as text and images"],
    ])},
    "machine-learning-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented ML", "Combines a model with retrieved external data at inference time"],
    ])},
    "machine-learning-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Evaluation methodology", "Ensures ML research claims are supported by rigorous, reproducible benchmarking"],
    ])},
    "machine-learning-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Flow matching", "Trains a generative model by directly regressing a velocity field between distributions"],
    ])},
    "machine-learning-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented fine-tuning", "Fine-tunes a model jointly with a retrieval component for a target domain"],
    ])},
    "machine-learning-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["State space duality", "Connects selective state-space models to attention-like formulations"],
    ])},
    "machine-learning-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Sharpness-aware minimization", "Seeks flatter loss minima to improve generalization"],
    ])},
    "machine-learning-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Grokking", "A model suddenly generalizes long after training loss has already plateaued"],
    ])},
    "machine-learning-m1-l99": {"data_table": table(["Approach", "Feature"], [
        ["Tabular deep learning", "Neural architectures adapted for structured data"],
        ["Gradient boosting", "Often still matches or outperforms deep learning on tabular tasks"],
    ])},
    "machine-learning-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Data-centric AI", "Systematically improves training data quality rather than only model architecture"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"machine-learning-m1-l{base_n}"
    worked_key = f"machine-learning-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Machine Learning"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Machine Learning: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Machine Learning lessons (completing 120/120).")


if __name__ == "__main__":
    main()
