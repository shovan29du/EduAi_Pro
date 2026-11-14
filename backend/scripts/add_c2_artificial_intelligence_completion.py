#!/usr/bin/env python3
"""Depth pass, C2 Artificial Intelligence: fill in real, hand-checked
data_table content for the 69 C2 Artificial Intelligence lessons not
covered by the earlier breadth-first batch. Brings C2 Artificial
Intelligence to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_artificial_intelligence_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "artificial-intelligence-c2-l1": {
        "data_table": table(["Algorithm", "Feature"], [
            ["Breadth-first search", "Explores level by level, guarantees shortest path in unweighted graphs"], ["A* search", "Uses a heuristic to find the optimal path efficiently"],
        ]),
    },
    "artificial-intelligence-c2-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["Adversarial search", "Search where an opponent actively works against the agent's goal"],
        ]),
    },
    "artificial-intelligence-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Monte Carlo Tree Search", "Builds a search tree using random simulations to estimate move quality"],
        ]),
    },
    "artificial-intelligence-c2-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Genetic algorithm", "Evolves candidate solutions using selection, crossover, and mutation"],
        ]),
    },
    "artificial-intelligence-c2-l6": {
        "data_table": table(["Algorithm", "Inspiration"], [
            ["Ant colony optimization", "Mimics ants depositing pheromones to find efficient paths"], ["Particle swarm optimization", "Mimics flocking behavior to explore a search space"],
        ]),
    },
    "artificial-intelligence-c2-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Arc consistency", "Ensures every value in a variable's domain has a compatible value in a connected variable"],
        ]),
    },
    "artificial-intelligence-c2-l8": {
        "data_table": table(["Element", "Example"], [
            ["Predicate", "Loves(x, y)"], ["Quantifier", "∀x (For all x)"],
        ]),
    },
    "artificial-intelligence-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Resolution", "A rule of inference used to prove logical statements by deriving a contradiction"],
        ]),
    },
    "artificial-intelligence-c2-l10": {
        "data_table": table(["Term", "Meaning"], [
            ["Game theory", "Studies strategic interactions where outcomes depend on multiple agents' choices"],
        ]),
    },
    "artificial-intelligence-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Nash equilibrium", "A state where no agent benefits from unilaterally changing strategy"],
        ]),
    },
    "artificial-intelligence-c2-l12": {
        "data_table": table(["Term", "Meaning"], [
            ["Multi-agent system", "Multiple autonomous agents interacting within a shared environment"],
        ]),
    },
    "artificial-intelligence-c2-l13": {
        "data_table": table(["Type", "Feature"], [
            ["Cooperative agents", "Work together toward a shared goal"], ["Competitive agents", "Pursue conflicting individual goals"],
        ]),
    },
    "artificial-intelligence-c2-l14": {
        "data_table": table(["Term", "Meaning"], [
            ["Object detection", "Locates and classifies objects within an image"],
        ]),
    },
    "artificial-intelligence-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["Acoustic model", "Maps audio features to phonemes for speech recognition"],
        ]),
    },
    "artificial-intelligence-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Sensor fusion", "Combines data from multiple sensors for a more accurate environmental understanding"],
        ]),
    },
    "artificial-intelligence-c2-l17": {
        "data_table": table(["Component", "Role"], [
            ["LIDAR", "Measures distance using laser pulses for 3D mapping"], ["Perception stack", "Interprets sensor data to understand the driving environment"],
        ]),
    },
    "artificial-intelligence-c2-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Affective computing", "Systems that recognize, interpret, and respond to human emotions"],
        ]),
    },
    "artificial-intelligence-c2-l19": {
        "data_table": table(["System", "Approach"], [
            ["AlphaGo", "Combined deep neural networks with Monte Carlo Tree Search"],
        ]),
    },
    "artificial-intelligence-c2-l20": {
        "data_table": table(["Term", "Meaning"], [
            ["Cellular automaton", "A grid of cells evolving through simple local rules, producing complex behavior"],
        ]),
    },
    "artificial-intelligence-c2-l21": {
        "data_table": table(["Architecture", "Best For"], [
            ["CNN", "Image and spatial data"], ["RNN", "Sequential data"], ["Transformer", "Long-range sequence dependencies"],
        ]),
    },
    "artificial-intelligence-c2-l22": {
        "data_table": table(["Layer", "Purpose"], [
            ["Convolutional layer", "Extracts spatial features using learnable filters"], ["Pooling layer", "Reduces spatial dimensions while retaining key information"],
        ]),
    },
    "artificial-intelligence-c2-l23": {
        "data_table": table(["Architecture", "Feature"], [
            ["LSTM", "Uses gates to control long-term memory retention"], ["GRU", "A simplified gating mechanism with fewer parameters than LSTM"],
        ]),
    },
    "artificial-intelligence-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Attention", "Lets a model weigh the relevance of different input parts dynamically"],
        ]),
    },
    "artificial-intelligence-c2-l25": {
        "data_table": table(["Component", "Purpose"], [
            ["Self-attention", "Relates each token in a sequence to every other token"], ["Positional encoding", "Injects sequence order information"],
        ]),
    },
    "artificial-intelligence-c2-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Large language model", "A neural network trained on massive text corpora to generate and understand language"],
        ]),
    },
    "artificial-intelligence-c2-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Transfer learning", "Reusing a pretrained model's learned features for a new, related task"], ["Fine-tuning", "Further training a pretrained model on task-specific data"],
        ]),
    },
    "artificial-intelligence-c2-l28": {
        "data_table": table(["Component", "Role"], [
            ["Generator", "Creates synthetic data samples"], ["Discriminator", "Distinguishes real data from generated data"],
        ]),
    },
    "artificial-intelligence-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Diffusion model", "Generates data by learning to reverse a gradual noising process"],
        ]),
    },
    "artificial-intelligence-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Autoencoder", "Learns to compress and reconstruct data through a bottleneck representation"],
        ]),
    },
    "artificial-intelligence-c2-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Variational autoencoder", "An autoencoder learning a probabilistic latent space for generation"],
        ]),
    },
    "artificial-intelligence-c2-l32": {
        "data_table": table(["Technique", "Purpose"], [
            ["Dropout", "Randomly disables neurons during training to reduce overfitting"], ["Weight decay", "Penalizes large weights to encourage simpler models"],
        ]),
    },
    "artificial-intelligence-c2-l33": {
        "data_table": table(["Optimizer", "Feature"], [
            ["SGD", "Updates weights using gradients from mini-batches"], ["Adam", "Combines momentum and adaptive learning rates"],
        ]),
    },
    "artificial-intelligence-c2-l34": {
        "data_table": table(["Term", "Meaning"], [
            ["Batch normalization", "Normalizes layer inputs to stabilize and speed up training"],
        ]),
    },
    "artificial-intelligence-c2-l35": {
        "data_table": table(["Strategy", "Feature"], [
            ["Grid search", "Exhaustively tries every combination of hyperparameters"], ["Random search", "Samples random combinations, often more efficient"],
        ]),
    },
    "artificial-intelligence-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Sequence-to-sequence model", "Maps an input sequence to an output sequence, e.g. for translation"],
        ]),
    },
    "artificial-intelligence-c2-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Named entity recognition", "Identifies and classifies entities like people or organizations in text"],
        ]),
    },
    "artificial-intelligence-c2-l38": {
        "data_table": table(["Challenge", "Detail"], [
            ["Scaling text classification", "Requires efficient models to process very large volumes of text"],
        ]),
    },
    "artificial-intelligence-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["RAG", "Retrieval-Augmented Generation, grounds LLM responses in retrieved external documents"],
        ]),
    },
    "artificial-intelligence-c2-l40": {
        "data_table": table(["Technique", "Example"], [
            ["Few-shot prompting", "Provides examples within the prompt to guide model behavior"],
        ]),
    },
    "artificial-intelligence-c2-l41": {
        "data_table": table(["Metric", "Meaning"], [
            ["Calibration", "Measures whether a model's confidence scores match actual accuracy"],
        ]),
    },
    "artificial-intelligence-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Adversarial example", "An input deliberately perturbed to fool a model into misclassifying it"],
        ]),
    },
    "artificial-intelligence-c2-l43": {
        "data_table": table(["Term", "Meaning"], [
            ["Deep reinforcement learning", "Combines deep neural networks with reinforcement learning to handle complex state spaces"],
        ]),
    },
    "artificial-intelligence-c2-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Policy gradient", "Directly optimizes a policy function using gradient ascent on expected reward"],
        ]),
    },
    "artificial-intelligence-c2-l45": {
        "data_table": table(["Term", "Formula"], [
            ["Q-learning update", "Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') − Q(s,a)]"],
        ]),
        "formulae": ["Q[s][a] += alpha * (r + gamma * max(Q[s_next]) - Q[s][a])"],
    },
    "artificial-intelligence-c2-l46": {
        "data_table": table(["Challenge", "Detail"], [
            ["Non-stationarity", "Other agents' evolving strategies make the environment harder to learn"],
        ]),
    },
    "artificial-intelligence-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Graph neural network", "Learns representations over graph-structured data by aggregating neighbor information"],
        ]),
    },
    "artificial-intelligence-c2-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Self-supervised learning", "Generates training labels automatically from the data itself"],
        ]),
    },
    "artificial-intelligence-c2-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["Federated learning", "Trains a shared model across decentralized data without moving the raw data"],
        ]),
    },
    "artificial-intelligence-c2-l50": {
        "data_table": table(["Technique", "Purpose"], [
            ["Pruning", "Removes unnecessary weights or neurons"], ["Quantization", "Reduces numerical precision to shrink model size"],
        ]),
    },
    "artificial-intelligence-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Scaling laws", "Empirical relationships showing how model performance improves with size and data"],
        ]),
    },
    "artificial-intelligence-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["AI alignment", "Ensuring an AI system's goals and behavior match human intentions"],
        ]),
    },
    "artificial-intelligence-c2-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Interpretability", "Techniques for understanding why a model made a particular decision"],
        ]),
    },
    "artificial-intelligence-c2-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["AI safety", "Research focused on preventing unintended or harmful AI behavior"],
        ]),
    },
    "artificial-intelligence-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Multimodal model", "Processes and relates multiple data types like text, image, and audio together"],
        ]),
    },
    "artificial-intelligence-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["MLOps", "Practices for reliably deploying, monitoring, and maintaining ML models in production"],
        ]),
    },
    "artificial-intelligence-c2-l57": {
        "data_table": table(["Approach", "Detail"], [
            ["Risk-based regulation", "Applies stricter rules to higher-risk AI applications"],
        ]),
    },
    "artificial-intelligence-c2-l58": {
        "data_table": table(["Term", "Meaning"], [
            ["Neurosymbolic AI", "Combines neural network learning with symbolic logical reasoning"],
        ]),
    },
    "artificial-intelligence-c2-l59": {
        "data_table": table(["Practice", "Reason"], [
            ["Publishing code and data", "Enables other researchers to verify and build on published results"],
        ]),
    },
    "artificial-intelligence-c2-l60": {
        "data_table": table(["Area", "Direction"], [
            ["Agentic AI", "Systems that plan and take multi-step actions autonomously"],
        ]),
    },
    "artificial-intelligence-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Tuning MCTS exploration", "Balancing exploration and exploitation in simulated rollouts"],
        ]),
    },
    "artificial-intelligence-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Designing a fitness function", "Guiding a genetic algorithm toward better solutions"],
        ]),
    },
    "artificial-intelligence-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Fusing camera and LIDAR data", "Improving object detection reliability in poor visibility"],
        ]),
    },
    "artificial-intelligence-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Visualizing attention weights", "Interpreting which input tokens a model focused on"],
        ]),
    },
    "artificial-intelligence-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Comparing LLM sizes", "Assessing capability tradeoffs across model scales"],
        ]),
    },
    "artificial-intelligence-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Diagnosing GAN training instability", "Identifying mode collapse in generated outputs"],
        ]),
    },
    "artificial-intelligence-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Comparing diffusion and GAN outputs", "Assessing sample diversity and quality tradeoffs"],
        ]),
    },
    "artificial-intelligence-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a proposed AI regulation", "Assessing its scope and enforcement mechanism"],
        ]),
    },
    "artificial-intelligence-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Comparing search strategies", "Choosing BFS versus A* for a specific pathfinding problem"],
        ]),
    },
    "artificial-intelligence-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Tracing a minimax decision", "Following the game tree to find the optimal move"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Artificial Intelligence"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Artificial Intelligence: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Artificial Intelligence lessons (completing 70/70).")


if __name__ == "__main__":
    main()
