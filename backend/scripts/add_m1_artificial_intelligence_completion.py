#!/usr/bin/env python3
"""Depth pass, M1 Artificial Intelligence: fill in real, hand-checked
data_table content for the 119 M1 Artificial Intelligence lessons not
covered by the earlier breadth-first batch. Brings M1 Artificial
Intelligence to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics in AI safety,
alignment, interpretability, and frontier research (distinct from the
classical/technical AI algorithms covered at C1/C2 level); l101-l120
are "Worked Analysis" companions reusing the data_table of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_artificial_intelligence_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["AI Alignment", "Ensuring AI systems act according to human intentions and values"],
    ["Reward hacking", "When an AI optimizes for a proxy reward in an unintended way"],
])

CHARTS: dict[str, dict] = {
    "artificial-intelligence-m1-l1": {"data_table": table(["Concept", "Detail"], [
        ["AI ethics", "Studies the moral principles guiding the design and deployment of AI systems"],
    ])},
    "artificial-intelligence-m1-l2": {"data_table": table(["Concept", "Detail"], [
        ["AI safety", "Studies how to prevent AI systems from causing unintended harm"],
    ])},
    "artificial-intelligence-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Specification gaming", "An agent satisfies the literal reward while violating the designer's intent"],
    ])},
    "artificial-intelligence-m1-l5": {"data_table": table(["Practice", "Purpose"], [
        ["Red-teaming", "Deliberately probes a system for failure modes before deployment"],
    ])},
    "artificial-intelligence-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["RLHF", "Reinforcement learning from human feedback; tunes a model using human preference signals"],
    ])},
    "artificial-intelligence-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Scalable oversight", "Techniques for supervising AI systems whose outputs exceed direct human evaluation capacity"],
    ])},
    "artificial-intelligence-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against a written set of principles"],
    ])},
    "artificial-intelligence-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Interpretability", "Understanding why a model produces a given output, used to catch unsafe behavior"],
    ])},
    "artificial-intelligence-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI (XAI)", "Methods that make a model's decisions understandable to humans"],
    ])},
    "artificial-intelligence-m1-l11": {"data_table": table(["Approach", "Feature"], [
        ["Interpretable-by-design model", "Uses architectures (e.g. decision trees, linear models) whose reasoning is directly readable"],
    ])},
    "artificial-intelligence-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Model auditing", "Systematically tests a deployed model for bias, safety, and performance issues"],
    ])},
    "artificial-intelligence-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["AGI", "Artificial general intelligence; a hypothetical system matching human-level ability across domains"],
    ])},
    "artificial-intelligence-m1-l14": {"data_table": table(["Question", "Relevance to AI"], [
        ["Does understanding require consciousness?", "Central debate in philosophy of mind applied to AI systems"],
    ])},
    "artificial-intelligence-m1-l15": {"data_table": table(["Concept", "Detail"], [
        ["Computability", "Some problems are provably unsolvable by any algorithm, bounding what AI can achieve"],
    ])},
    "artificial-intelligence-m1-l16": {"data_table": table(["Framework", "Focus"], [
        ["EU AI Act", "Risk-tiered regulation of AI systems by application domain"],
    ])},
    "artificial-intelligence-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["AI risk assessment", "Systematically identifies and rates potential harms before deployment"],
    ])},
    "artificial-intelligence-m1-l18": {"data_table": table(["Concept", "Detail"], [
        ["Dual-use AI", "Technology developed for civilian use that can also serve military applications"],
    ])},
    "artificial-intelligence-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic accountability", "Holding the operators of an automated system responsible for its outcomes"],
    ])},
    "artificial-intelligence-m1-l20": {"data_table": table(["Area", "Current direction"], [
        ["Frontier AI research", "Spans scaling, alignment, reasoning, and multimodal capability"],
    ])},
    "artificial-intelligence-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian network", "A graph encoding probabilistic dependencies between variables"],
    ])},
    "artificial-intelligence-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Markov Decision Process", "Models sequential decisions with states, actions, transitions, and rewards"],
    ])},
    "artificial-intelligence-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo Tree Search", "Builds a search tree using random rollouts to estimate move value"],
    ])},
    "artificial-intelligence-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Policy gradient", "Directly optimizes a policy's parameters via gradient ascent on expected reward"],
    ])},
    "artificial-intelligence-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent RL", "Multiple learning agents interact, producing emergent cooperative or competitive strategy"],
    ])},
    "artificial-intelligence-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automates the design of neural network structures"],
    ])},
    "artificial-intelligence-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Self-attention", "Computes weighted relationships between all tokens in a sequence"],
    ])},
    "artificial-intelligence-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts", "Routes each input to a subset of specialized sub-networks"],
    ])},
    "artificial-intelligence-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Diffusion model", "Generates images by learning to reverse a gradual noising process"],
    ])},
    "artificial-intelligence-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Variational autoencoder", "Learns a compressed, probabilistic latent representation of data"],
    ])},
    "artificial-intelligence-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network", "Learns representations by passing messages along graph edges"],
    ])},
    "artificial-intelligence-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Meta-learning", "Trains a model to adapt quickly to new tasks from few examples"],
    ])},
    "artificial-intelligence-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive learning", "Learns embeddings by pulling similar examples together and pushing dissimilar ones apart"],
    ])},
    "artificial-intelligence-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Neuro-symbolic AI", "Combines neural pattern recognition with symbolic logical reasoning"],
    ])},
    "artificial-intelligence-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Description logic", "A formal language for representing and reasoning about structured knowledge"],
    ])},
    "artificial-intelligence-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Automated theorem proving", "Uses algorithms to derive proofs of logical statements automatically"],
    ])},
    "artificial-intelligence-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Constraint satisfaction problem", "Finds variable assignments meeting a set of constraints"],
    ])},
    "artificial-intelligence-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["PDDL", "A standardized language for describing planning problems for automated solvers"],
    ])},
    "artificial-intelligence-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Genetic programming", "Evolves computer programs using selection, mutation, and crossover"],
    ])},
    "artificial-intelligence-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Fuzzy logic", "Allows truth values between 0 and 1 for reasoning under vagueness"],
    ])},
    "artificial-intelligence-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Active learning", "A model selects the most informative unlabeled examples to query next"],
    ])},
    "artificial-intelligence-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Curriculum learning", "Orders training examples from easy to hard to speed up learning"],
    ])},
    "artificial-intelligence-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "Adds calibrated noise so individual data points cannot be reverse-engineered"],
    ])},
    "artificial-intelligence-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial example", "An input crafted with small perturbations to fool a model"],
    ])},
    "artificial-intelligence-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to mimic a larger teacher model"],
    ])},
    "artificial-intelligence-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Catastrophic forgetting", "A model loses earlier learned skills when trained on new tasks"],
    ])},
    "artificial-intelligence-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Causal discovery", "Infers cause-effect structure from observational data alone"],
    ])},
    "artificial-intelligence-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual reasoning", "Asks what would have happened under a different, hypothetical condition"],
    ])},
    "artificial-intelligence-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Mechanistic interpretability", "Reverse-engineers the internal circuits a neural network uses to compute outputs"],
    ])},
    "artificial-intelligence-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Sparse autoencoder", "Decomposes neural activations into a small set of interpretable features"],
    ])},
    "artificial-intelligence-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Probing classifier", "A simple classifier trained on a model's internal representations to test what they encode"],
    ])},
    "artificial-intelligence-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought", "Prompts a model to generate intermediate reasoning steps before an answer"],
    ])},
    "artificial-intelligence-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning", "A model performs a new task from examples in the prompt without weight updates"],
    ])},
    "artificial-intelligence-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented generation", "Combines a language model with retrieved external documents at inference time"],
    ])},
    "artificial-intelligence-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Agentic model", "A model that plans, calls tools, and acts over multiple steps toward a goal"],
    ])},
    "artificial-intelligence-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal model", "Jointly processes and relates data from multiple modalities such as text and images"],
    ])},
    "artificial-intelligence-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["End-to-end speech model", "Maps audio directly to text without separate hand-engineered stages"],
    ])},
    "artificial-intelligence-m1-l58": {"data_table": table(["Metric", "Measures"], [
        ["BLEU / ROUGE", "N-gram overlap between generated and reference text"],
    ])},
    "artificial-intelligence-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Sequence-to-sequence model", "Maps an input sequence to an output sequence, e.g. for translation"],
    ])},
    "artificial-intelligence-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Object detection", "Locates and classifies objects within an image"],
    ])},
    "artificial-intelligence-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Semantic segmentation", "Classifies every pixel of an image into a category"],
    ])},
    "artificial-intelligence-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["3D scene reconstruction", "Recovers 3D geometry from one or more 2D images"],
    ])},
    "artificial-intelligence-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Neural radiance field (NeRF)", "Learns a continuous volumetric scene representation for novel view synthesis"],
    ])},
    "artificial-intelligence-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Sensor fusion", "Combines data from multiple sensors for a more reliable perception estimate"],
    ])},
    "artificial-intelligence-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Motion planning", "Computes a feasible, collision-free path for an autonomous agent"],
    ])},
    "artificial-intelligence-m1-l66": {"data_table": table(["Principle", "Detail"], [
        ["Legibility", "A robot's actions should signal its intent clearly to nearby humans"],
    ])},
    "artificial-intelligence-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Affective computing", "Systems that recognize, interpret, and respond to human emotion"],
    ])},
    "artificial-intelligence-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Collaborative filtering", "Recommends items based on patterns across many users' preferences"],
    ])},
    "artificial-intelligence-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Cold-start problem", "Poor recommendation quality for new users or items with little history"],
    ])},
    "artificial-intelligence-m1-l70": {"data_table": table(["Metric", "Measures"], [
        ["Demographic parity", "Whether outcomes are distributed similarly across protected groups"],
    ])},
    "artificial-intelligence-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["AI safety via debate", "Two AI systems argue opposing sides so a human judge can better evaluate the truth"],
    ])},
    "artificial-intelligence-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification", "Mathematically proves a neural network satisfies a given property"],
    ])},
    "artificial-intelligence-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Sample complexity", "The number of training examples needed to learn a concept to a target accuracy"],
    ])},
    "artificial-intelligence-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["PAC learning", "A theoretical framework bounding how much data is needed for probably-approximately-correct learning"],
    ])},
    "artificial-intelligence-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["VC dimension", "A measure of a model class's capacity to fit arbitrary labelings of points"],
    ])},
    "artificial-intelligence-m1-l76": {"data_table": table(["Theorem", "Implication"], [
        ["No Free Lunch", "No single algorithm outperforms all others across every possible problem"],
    ])},
    "artificial-intelligence-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Kolmogorov complexity", "The length of the shortest program that can produce a given output"],
    ])},
    "artificial-intelligence-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Turing Test", "Judges machine intelligence by whether its responses are indistinguishable from a human's"],
    ])},
    "artificial-intelligence-m1-l79": {"data_table": table(["Argument", "Claim"], [
        ["Chinese Room", "Symbol manipulation alone, without understanding, could produce apparently intelligent output"],
    ])},
    "artificial-intelligence-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Embodied cognition", "Argues intelligence emerges from an agent's physical interaction with its environment"],
    ])},
    "artificial-intelligence-m1-l81": {"data_table": table(["Architecture", "Feature"], [
        ["SOAR / ACT-R", "Cognitive architectures modeling human reasoning as rule-based production systems"],
    ])},
    "artificial-intelligence-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Common sense reasoning", "Everyday background knowledge that remains difficult for AI systems to reliably apply"],
    ])},
    "artificial-intelligence-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Analogical reasoning", "Transfers a relational pattern learned in one domain to a structurally similar domain"],
    ])},
    "artificial-intelligence-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Program synthesis", "Automatically generates a program from examples or a formal specification"],
    ])},
    "artificial-intelligence-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Neural program induction", "Learns to produce or execute programs using a neural network"],
    ])},
    "artificial-intelligence-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["AI for hypothesis generation", "Proposes candidate scientific hypotheses for human researchers to test"],
    ])},
    "artificial-intelligence-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["AutoML", "Automates model selection, feature engineering, and hyperparameter tuning"],
    ])},
    "artificial-intelligence-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Energy-based model", "Learns a scalar energy function that is low for likely data and high otherwise"],
    ])},
    "artificial-intelligence-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Normalizing flow", "Transforms a simple distribution into a complex one via invertible mappings with exact likelihoods"],
    ])},
    "artificial-intelligence-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Spiking neural network", "Models neurons that communicate via discrete timed spikes, closer to biological computation"],
    ])},
    "artificial-intelligence-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Quantum machine learning", "Explores using quantum computation to accelerate or enhance learning algorithms"],
    ])},
    "artificial-intelligence-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Data contamination", "Test data leaking into training data, inflating apparent benchmark performance"],
    ])},
    "artificial-intelligence-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Scaling law", "An empirical relationship between model size, data, compute, and performance"],
    ])},
    "artificial-intelligence-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["World model", "An internal model an agent learns to simulate and plan within its environment"],
    ])},
    "artificial-intelligence-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Speculative decoding", "Uses a small draft model to propose tokens that a larger model verifies, speeding inference"],
    ])},
    "artificial-intelligence-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Test-time compute", "Spending extra computation at inference (e.g. more reasoning steps) to improve answer quality"],
    ])},
    "artificial-intelligence-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Emergent communication", "Agents develop their own signaling protocol while learning to cooperate"],
    ])},
    "artificial-intelligence-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Automated experiment design", "AI proposes and prioritizes which scientific experiments to run next"],
    ])},
    "artificial-intelligence-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "Embeds a detectable signal in AI-generated content to trace its provenance"],
    ])},
    "artificial-intelligence-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Model editing", "Directly updates a specific fact stored in a trained model's weights"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"artificial-intelligence-m1-l{base_n}"
    worked_key = f"artificial-intelligence-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Artificial Intelligence"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Artificial Intelligence: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Artificial Intelligence lessons (completing 120/120).")


if __name__ == "__main__":
    main()
