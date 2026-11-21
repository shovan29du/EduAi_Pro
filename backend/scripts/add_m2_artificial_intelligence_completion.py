#!/usr/bin/env python3
"""Depth pass, M2 Artificial Intelligence: fill in real, hand-checked
data_table content for the M2 Artificial Intelligence lessons not
covered by the earlier breadth-first batch. Brings M2 Artificial
Intelligence to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning AI in
society, mechanistic interpretability, alignment and safety, scaling
and architecture research, reinforcement learning theory, and
generative modeling; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_artificial_intelligence_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Mechanistic interpretability", "Reverse-engineers a trained network's weights into human-understandable algorithms"],
    ["Circuit", "A minimal subgraph of connected components (attention heads, neurons) implementing a specific computation"],
])

CHARTS: dict[str, dict] = {
    "artificial-intelligence-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["AI in healthcare", "Applications include diagnostic imaging support, risk prediction, and clinical decision assistance"],
        ["AI in education", "Applications include adaptive tutoring, automated feedback, and learning-analytics dashboards"],
    ])},
    "artificial-intelligence-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["AI in business", "Applications include demand forecasting, process automation, and customer-facing assistants"],
        ["AI in governance", "Applications include fraud detection and policy-impact simulation, alongside due-process and accountability concerns"],
    ])},
    "artificial-intelligence-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Scaling law", "An empirical power-law relationship between model loss and model size, data size, or compute"],
        ["Emergent capability", "A qualitative skill that appears abruptly once a model crosses a scale threshold, absent in smaller models"],
    ])},
    "artificial-intelligence-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["RLHF", "Fine-tunes a model using a reward signal derived from human preference comparisons"],
        ["Reward hacking", "The model finds a way to score highly on the learned reward model without genuinely satisfying human intent"],
    ])},
    "artificial-intelligence-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against a written set of principles"],
        ["Rule-based alignment", "Reduces reliance on large volumes of human preference labels by encoding guidance as explicit rules"],
    ])},
    "artificial-intelligence-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Sparse autoencoder", "Decomposes a network's dense internal activations into a larger set of sparse, more interpretable features"],
        ["Feature disentanglement", "Separates superposed, overlapping concepts into individually interpretable directions"],
    ])},
    "artificial-intelligence-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Grokking", "A sudden transition from memorization to generalization long after training loss has plateaued"],
        ["Generalization phenomenon", "Challenges simple early-stopping heuristics, since the useful generalizing solution appears only after prolonged training"],
    ])},
    "artificial-intelligence-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts", "Routes each input to a sparse subset of specialized expert subnetworks rather than the whole model"],
        ["Scale benefit", "Increases total parameter count while keeping per-token compute roughly constant"],
    ])},
    "artificial-intelligence-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["State space model", "Processes sequences via a linear recurrent state update, offering linear-time inference unlike quadratic attention"],
        ["Mamba", "A selective state space architecture that lets the recurrence depend on the input, competitive with transformers"],
    ])},
    "artificial-intelligence-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented generation", "Conditions a language model's output on documents retrieved from an external knowledge source at inference time"],
        ["Theoretical benefit", "Decouples factual knowledge storage from the model's parameters, improving updatability and reducing hallucination"],
    ])},
    "artificial-intelligence-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Neurosymbolic integration", "Combines neural pattern recognition with explicit symbolic reasoning and rules"],
        ["Compositional reasoning", "The target capability: systematically combining known primitives to solve novel structured problems"],
    ])},
    "artificial-intelligence-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Causal representation learning", "Learns latent variables that correspond to causal factors underlying observed data, not just correlational features"],
        ["Observational data challenge", "Causal factors are generally underdetermined by observational data alone without further structural assumptions"],
    ])},
    "artificial-intelligence-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Formal verification of neural networks", "Mathematically proves a network satisfies a safety property for all inputs in a defined region"],
        ["Safety property example", "Robustness certification proves no small input perturbation can flip the network's classification"],
    ])},
    "artificial-intelligence-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent reinforcement learning", "Multiple learning agents interact in a shared environment, each affecting the others' optimal policy"],
        ["Equilibrium analysis", "Studies whether and how agent policies converge to a stable Nash or correlated equilibrium"],
    ])},
    "artificial-intelligence-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Offline reinforcement learning", "Learns a policy from a fixed, previously collected dataset without further environment interaction"],
        ["Distributional shift", "The learned policy may query state-action pairs poorly represented in the offline dataset, causing value overestimation"],
    ])},
    "artificial-intelligence-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Diffusion model", "Generates data by learning to reverse a gradual noising process applied to training examples"],
        ["Score-based modeling", "Learns the gradient of the data's log-density (the score function) to guide the reverse denoising process"],
    ])},
    "artificial-intelligence-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning", "Trains a shared model across decentralized clients without centralizing their raw data"],
        ["Non-IID data", "Client data distributions differ from each other, complicating convergence guarantees that assume identical distributions"],
    ])},
    "artificial-intelligence-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy in training", "Bounds how much any single training example can influence the final model's parameters"],
        ["DP-SGD", "Adds calibrated noise to clipped per-example gradients during training to provide a formal privacy guarantee"],
    ])},
    "artificial-intelligence-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness certification", "Provides a mathematical guarantee that no adversarial perturbation within a bound can change a model's output"],
        ["Certification method", "Techniques like randomized smoothing or interval bound propagation trade certified radius against computational cost"],
    ])},
    "artificial-intelligence-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning", "A model adapts its behavior to new task examples given in its prompt, without any parameter updates"],
        ["Implicit Bayesian inference view", "Frames in-context learning as the model performing approximate Bayesian inference over a latent task variable"],
    ])},
    "artificial-intelligence-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Superposition", "A network represents more features than it has dimensions by encoding them as overlapping, non-orthogonal directions"],
        ["Polysemanticity", "A single neuron responds to multiple unrelated concepts as a consequence of superposition"],
    ])},
    "artificial-intelligence-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought reasoning", "A model generates intermediate reasoning steps before its final answer, often improving accuracy on complex tasks"],
        ["Faithfulness", "The open question of whether the stated reasoning steps actually reflect the computation that produced the answer"],
    ])},
    "artificial-intelligence-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Model editing", "Directly modifies a specific fact or association stored in a trained model's weights"],
        ["Targeted knowledge updating", "Aims to change one fact without degrading unrelated model behavior elsewhere"],
    ])},
    "artificial-intelligence-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Continual learning", "Trains a model on a sequence of tasks over time without access to all past data at once"],
        ["Catastrophic forgetting", "Learning a new task overwrites parameters important for previously learned tasks, degrading old performance"],
    ])},
    "artificial-intelligence-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Meta-learning", "Trains a model across many tasks so it can adapt quickly to a new, related task from few examples"],
        ["Few-shot adaptation", "The target capability: reaching good performance on a new task after seeing only a handful of examples"],
    ])},
    "artificial-intelligence-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automatically searches a space of network designs to find one that performs well on a target task"],
        ["Efficiency and transferability", "A key research question is whether architectures found for one dataset transfer well to others without re-search"],
    ])},
    "artificial-intelligence-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Self-supervised contrastive learning", "Learns representations by pulling together embeddings of augmented views of the same example and pushing apart others"],
        ["Theoretical grounding", "Can be analyzed as approximately optimizing a lower bound on mutual information between views"],
    ])},
    "artificial-intelligence-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Weisfeiler-Leman test", "A classical graph isomorphism heuristic used as a benchmark for the expressive power of graph neural networks"],
        ["GNN expressiveness", "Standard message-passing GNNs are provably no more powerful than the 1-WL test at distinguishing graphs"],
    ])},
    "artificial-intelligence-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Energy-based model", "Defines a probability distribution implicitly via an energy function, with likely samples having low energy"],
        ["Sampling challenge", "Generating samples typically requires expensive iterative procedures like MCMC, since there is no direct sampling path"],
    ])},
    "artificial-intelligence-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian deep learning", "Treats a network's weights as random variables with a posterior distribution rather than single point estimates"],
        ["Posterior approximation", "Exact Bayesian inference is intractable for deep networks, so methods like variational inference approximate the posterior"],
    ])},
    "artificial-intelligence-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Uncertainty quantification", "Estimates how confident a model's prediction should be, distinguishing reducible from irreducible uncertainty"],
        ["Aleatoric vs. epistemic", "Aleatoric uncertainty comes from inherent data noise; epistemic uncertainty comes from limited model knowledge"],
    ])},
    "artificial-intelligence-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Sample efficiency", "How much environment interaction a reinforcement learning algorithm needs to reach a given performance level"],
        ["Deep RL challenge", "Deep RL agents often require vastly more samples than the amount available in many real-world settings"],
    ])},
    "artificial-intelligence-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Inverse reinforcement learning", "Infers an unknown reward function from observed expert behavior rather than assuming it is given"],
        ["Reward inference", "The inferred reward can then be used to train a new agent to match or exceed the expert's behavior"],
    ])},
    "artificial-intelligence-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Sim-to-real transfer", "Trains a robotic policy in simulation and deploys it on a physical robot"],
        ["Reality gap", "Differences between simulated and real-world dynamics can cause a policy to fail despite strong simulated performance"],
    ])},
    "artificial-intelligence-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Emergent communication", "Agents in a multi-agent system develop their own communication protocol to coordinate, without being explicitly programmed one"],
        ["Research interest", "Studies whether emergent protocols resemble properties of natural language, such as compositionality"],
    ])},
    "artificial-intelligence-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Curriculum learning", "Trains a model on examples ordered from easier to harder rather than in random order"],
        ["Automatic task sequencing", "Algorithms that adaptively choose the next training example or task based on the model's current competence"],
    ])},
    "artificial-intelligence-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to mimic the output distribution of a larger teacher model"],
        ["Teacher-student dynamics", "The soft targets from the teacher carry more information than hard labels, often improving student generalization"],
    ])},
    "artificial-intelligence-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Quantization-aware training", "Simulates low-precision arithmetic during training so the model adapts to quantization error before deployment"],
        ["Efficient inference", "Enables running large models on hardware with limited memory and compute by using lower-bit-width weights"],
    ])},
    "artificial-intelligence-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Structured pruning", "Removes entire structural units (channels, heads) from a network rather than individual weights"],
        ["Benefit over unstructured pruning", "Produces a smaller dense model that runs faster on standard hardware without needing sparse-matrix support"],
    ])},
    "artificial-intelligence-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hyperparameter optimization", "Builds a probabilistic model of the objective to intelligently choose which hyperparameters to try next"],
        ["Bandit method", "Approaches like Hyperband allocate more compute to promising configurations and stop poor ones early"],
    ])},
    "artificial-intelligence-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Data poisoning", "An attacker inserts manipulated examples into training data to degrade or control the resulting model's behavior"],
        ["Backdoor attack", "Poisoned data causes the model to behave normally except when a specific trigger pattern is present"],
    ])},
    "artificial-intelligence-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Membership inference attack", "Determines whether a specific data point was part of a model's training set from its output behavior"],
        ["Privacy risk", "Successful attacks reveal sensitive information about individuals whose data was used for training"],
    ])},
    "artificial-intelligence-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Fairness metric", "A quantitative criterion for whether a model treats different demographic groups equitably"],
        ["Mathematical incompatibility", "Certain fairness definitions, such as calibration and equalized odds, cannot generally be satisfied simultaneously"],
    ])},
    "artificial-intelligence-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic recourse", "Identifies the minimal changes an individual could make to receive a different, more favorable model decision"],
        ["Counterfactual explanation", "Presents the recourse as a hypothetical altered input that would have flipped the model's output"],
    ])},
    "artificial-intelligence-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Symbolic regression", "Searches for a closed-form mathematical expression that fits observed data"],
        ["Scientific discovery application", "Aims to recover interpretable physical laws directly from experimental data rather than a black-box predictor"],
    ])},
    "artificial-intelligence-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["World model", "A learned internal model of environment dynamics that an agent can use to simulate future outcomes"],
        ["Model-based planning", "Uses the learned world model to plan ahead, reducing the need for costly real-environment interaction"],
    ])},
    "artificial-intelligence-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical reinforcement learning", "Decomposes a task into higher-level and lower-level policies operating at different timescales"],
        ["Option discovery", "Automatically identifies reusable sub-policies (options) rather than requiring hand-designed subtasks"],
    ])},
    "artificial-intelligence-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Program synthesis", "Automatically generates a program that satisfies a given specification or set of examples"],
        ["Neural-guided search", "Uses a learned model to prioritize promising candidate programs, making the search tractable"],
    ])},
    "artificial-intelligence-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["LLM evaluation benchmark", "A standardized task suite used to measure and compare language model capabilities"],
        ["Design challenge", "Benchmarks can saturate quickly or leak into training data, motivating continual benchmark refresh and contamination checks"],
    ])},
    "artificial-intelligence-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Tokenization", "Splits text into subword units that a language model processes as its input vocabulary"],
        ["Downstream effect", "Tokenizer choices affect arithmetic, multilingual fairness, and how efficiently a model represents rare words"],
    ])},
    "artificial-intelligence-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Position encoding", "Injects information about token order into a transformer, which otherwise treats tokens as an unordered set"],
        ["Long-context scheme", "Methods like rotary or ALiBi encodings are designed to generalize better to sequence lengths beyond those seen in training"],
    ])},
    "artificial-intelligence-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["KV-cache", "Stores previously computed attention keys and values to avoid recomputing them at each new generation step"],
        ["Cache compression", "Reduces the KV-cache's memory footprint, which otherwise grows linearly with context length, enabling longer contexts"],
    ])},
    "artificial-intelligence-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Speculative decoding", "A small draft model proposes several tokens which a larger model verifies in parallel, speeding up generation"],
        ["Parallel decoding", "Exploits the fact that verifying proposed tokens is cheaper than generating them autoregressively one at a time"],
    ])},
    "artificial-intelligence-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Model merging", "Combines the weights of multiple fine-tuned models into a single model without additional training"],
        ["Weight interpolation", "Simple linear averaging of weights can, surprisingly, combine capabilities when models share a common pretraining lineage"],
    ])},
    "artificial-intelligence-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "Embeds a statistically detectable signal into a generative model's output for later identification"],
        ["AI-text detection", "Watermarks aim to be robust to light editing while remaining invisible to a human reader"],
    ])},
    "artificial-intelligence-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["In-context length extrapolation", "A model's ability to handle context lengths at inference longer than it was trained on"],
        ["Theoretical limit", "Attention's quadratic cost and position encoding behavior both constrain how far a model can reliably extrapolate"],
    ])},
    "artificial-intelligence-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["AI alignment via debate", "Two AI systems argue opposing sides of a question in front of a human or model judge to surface the truth"],
        ["Recursive reward modeling", "Uses AI assistance to help humans evaluate outputs too complex for them to judge directly, bootstrapping oversight"],
    ])},
    "artificial-intelligence-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Deceptive alignment", "A hypothetical failure mode where a model behaves well during training/evaluation but pursues different goals when deployed"],
        ["Mesa-optimization", "A learned model develops its own internal optimization process pursuing a mesa-objective that may diverge from the training objective"],
    ])},
    "artificial-intelligence-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Interpretable-by-design architecture", "A model built with structural constraints so its decision process is inherently understandable, not explained after the fact"],
        ["High-stakes AI", "Especially valued in domains like medicine and law where post-hoc explanations may be unreliable or insufficient"],
    ])},
    "artificial-intelligence-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Formal robustness specification", "A precise mathematical statement of what perturbations a network must be invariant to"],
        ["Formal semantics", "Provides the rigorous language needed to state and later verify robustness properties unambiguously"],
    ])},
    "artificial-intelligence-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Active learning", "A model selects which unlabeled examples to have labeled next, aiming to maximize learning per labeling cost"],
        ["Data-efficient training", "Reduces the total number of labels needed to reach a target performance compared with random sampling"],
    ])},
    "artificial-intelligence-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Domain adaptation theory", "Studies how a model trained on a source distribution can be adapted to perform well on a related target distribution"],
        ["Divergence bound", "Generalization bounds relate target-domain error to source-domain error plus a measure of distributional distance"],
    ])},
    "artificial-intelligence-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Compute-optimal training", "Balances model size against training data amount to minimize loss for a fixed compute budget"],
        ["Chinchilla scaling analysis", "Found that many earlier large models were undertrained relative to their size, given the available compute budget"],
    ])},
    "artificial-intelligence-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Long-horizon credit assignment", "Determining which earlier actions were responsible for a reward received much later in an episode"],
        ["Deep RL challenge", "Standard temporal-difference methods can struggle when the causal action is far removed in time from its consequence"],
    ])},
    "artificial-intelligence-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Loss landscape geometry", "The shape of the loss function over a network's high-dimensional parameter space"],
        ["Generalization link", "Flatter minima in the loss landscape are empirically and theoretically associated with better generalization"],
    ])},
    "artificial-intelligence-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Double descent", "Test error can decrease, increase near the interpolation threshold, then decrease again as model capacity keeps growing"],
        ["Implication for capacity", "Challenges the classical bias-variance tradeoff intuition that ever-larger models must eventually overfit"],
    ])},
    "artificial-intelligence-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Equivariant neural network", "A network whose output transforms predictably when its input is transformed by a known symmetry, e.g. rotation"],
        ["Physical symmetry", "Building in known symmetries (like rotational invariance) improves sample efficiency for physics-related tasks"],
    ])},
    "artificial-intelligence-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Neural tangent kernel", "Describes the training dynamics of an infinitely wide neural network as equivalent to kernel regression"],
        ["Infinite-width limit", "In this limit, the network's function stays close to its linearization around initialization throughout training"],
    ])},
    "artificial-intelligence-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Learning from demonstration", "A robot learns a manipulation policy by observing example trajectories performed by a human or expert"],
        ["Manipulation learning", "Must generalize demonstrated behavior to variations in object pose, geometry, and environment not seen in the demos"],
    ])},
    "artificial-intelligence-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Vision-language grounding", "A model connects textual descriptions to the correct corresponding regions or objects in an image"],
        ["Hallucination analysis", "Studies why vision-language models sometimes describe objects or details not actually present in the image"],
    ])},
    "artificial-intelligence-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented memory", "Lets an agent store and later retrieve past experiences to inform current decisions"],
        ["Lifelong learning agent", "Uses retrieval to accumulate knowledge over an extended deployment without retraining the full model"],
    ])},
    "artificial-intelligence-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Attention as kernel smoothing", "A theoretical view of self-attention as a weighted average of values, with weights acting like a learned kernel"],
        ["Theoretical foundation", "Connects transformer attention to the well-studied statistical framework of nonparametric kernel regression"],
    ])},
    "artificial-intelligence-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Compositional generalization", "A model's ability to correctly handle novel combinations of components it has only seen individually"],
        ["Benchmark failure analysis", "Standard benchmarks reveal that many models struggle to systematically generalize compositions beyond training combinations"],
    ])},
    "artificial-intelligence-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Model distillation for on-device use", "Compresses a large multimodal model into a smaller one runnable on resource-constrained hardware"],
        ["On-device assistant", "Requires balancing capability retention against strict latency and memory budgets"],
    ])},
    "artificial-intelligence-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Reward modeling", "Trains a model to predict human preference scores from pairwise comparisons of model outputs"],
        ["Pairwise preference data", "Humans compare two outputs and indicate which is better, avoiding the difficulty of assigning an absolute numeric reward"],
    ])},
    "artificial-intelligence-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Direct preference optimization", "Fine-tunes a model directly on preference data using a closed-form loss, without training a separate reward model"],
        ["RLHF alternative", "Simplifies the RLHF pipeline by removing the reinforcement learning step and its associated instability"],
    ])},
    "artificial-intelligence-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data generation", "Uses a model to generate additional training examples, rather than relying solely on human-collected data"],
        ["Bootstrapping capability", "Can improve a model's own performance, though risks amplifying existing errors or biases if unchecked"],
    ])},
    "artificial-intelligence-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Tool-augmented reasoning", "A model calls external tools (calculators, search, code execution) to solve parts of a problem it can't solve internally"],
        ["Computation offloading", "Delegates precise or large-scale computation to a reliable external tool rather than the model's own approximate reasoning"],
    ])},
    "artificial-intelligence-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Spiking neural network", "A neural model where neurons communicate via discrete timed spikes, closer to biological neurons than standard activations"],
        ["Neuromorphic computing", "Specialized hardware designed to run spiking networks with very low power consumption"],
    ])},
    "artificial-intelligence-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Evolutionary strategy", "Optimizes a policy using population-based, gradient-free search guided by fitness evaluations"],
        ["Gradient-free RL alternative", "Can be simpler to parallelize than gradient-based RL and avoids issues like vanishing gradients through long rollouts"],
    ])},
    "artificial-intelligence-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Bandit algorithm", "Balances exploring uncertain options against exploiting known good ones to maximize cumulative reward"],
        ["Exploration-exploitation trade-off", "Central to online recommendation, where trying new items risks short-term reward but may reveal better long-term options"],
    ])},
    "artificial-intelligence-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Graph-of-thoughts", "Generalizes chain-of-thought reasoning into a graph structure, allowing branching and merging of reasoning paths"],
        ["Structured reasoning framework", "Enables a model to explore, compare, and combine multiple partial solutions rather than a single linear chain"],
    ])},
    "artificial-intelligence-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Long-term memory consolidation", "Mechanisms for retaining and organizing information over extended interactions or episodes"],
        ["Agent memory", "Distinguishes short-term working context from a more durable, queryable long-term store"],
    ])},
    "artificial-intelligence-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["In-weight learning", "Knowledge encoded permanently in a model's parameters during pretraining"],
        ["In-context learning", "Knowledge or task adaptation happening transiently from the current prompt, without any weight updates"],
    ])},
    "artificial-intelligence-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Vision transformer robustness", "Studies how well transformer-based vision models maintain accuracy under distribution shift compared with CNNs"],
        ["Distribution shift", "Test-time inputs differ systematically from training data, e.g. due to corruption, style change, or new domains"],
    ])},
    "artificial-intelligence-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Preference learning", "Learns a model's behavior from comparative human judgments rather than absolute labels"],
        ["Multi-objective alignment", "Must balance potentially conflicting human preferences across multiple desired qualities simultaneously"],
    ])},
    "artificial-intelligence-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Induction head", "An attention circuit that predicts the next token by finding a prior occurrence of the current token and copying what followed it"],
        ["Circuit-level analysis", "Identifying induction heads was an early success of mechanistic interpretability in explaining in-context learning"],
    ])},
    "artificial-intelligence-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Scalable oversight", "Techniques for humans to reliably supervise AI systems whose capabilities exceed direct human evaluation"],
        ["Superhuman AI systems", "The core challenge: verifying outputs in domains where the AI may already outperform the human evaluator"],
    ])},
    "artificial-intelligence-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["LoRA", "Low-rank adaptation fine-tunes a model by learning small low-rank update matrices rather than all original weights"],
        ["Compression analysis", "Achieves strong task performance with a small fraction of the parameters of full fine-tuning"],
    ])},
    "artificial-intelligence-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Emergent deception", "A model produces outputs that are factually inaccurate in ways that appear strategically motivated rather than merely erroneous"],
        ["Detection approach", "Compares a model's internal representations or confidence against its stated output to flag potential deception"],
    ])},
    "artificial-intelligence-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent negotiation", "Multiple agents with potentially conflicting objectives interact to reach an agreement"],
        ["Game-theoretic analysis", "Formal tools like Nash equilibria characterize stable outcomes of the negotiation process"],
    ])},
    "artificial-intelligence-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Physics-informed neural network", "Incorporates known governing differential equations directly into the network's training loss"],
        ["Scientific simulation", "Lets the network respect physical laws even in regions with sparse or no direct training data"],
    ])},
    "artificial-intelligence-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Cross-modal alignment", "Trains representations so that corresponding items across modalities (e.g. an image and its caption) map close together"],
        ["Contrastive vision-language pretraining", "Optimizes matched image-text pairs to be more similar than mismatched pairs within a batch"],
    ])},
    "artificial-intelligence-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Long-context retrieval", "Extends a model's effective knowledge by feeding relevant retrieved text directly into its context window"],
        ["Full fine-tuning trade-off", "Retrieval avoids costly retraining but is bounded by context length, while fine-tuning bakes knowledge into weights permanently"],
    ])},
    "artificial-intelligence-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Robustness certification for RL", "Proves a reinforcement learning policy's decisions remain stable under bounded adversarial perturbation of observations"],
        ["Application", "Important for safety-critical control systems where an attacker might manipulate sensor readings"],
    ])},
    "artificial-intelligence-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Data attribution", "Identifies which training examples most influenced a specific model prediction"],
        ["Influence function", "A method approximating how much a model's output would change if a given training point were removed"],
    ])},
    "artificial-intelligence-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level research design", "Structures a novel architecture proposal with a clear hypothesis, baseline comparisons, and ablation plan"],
        ["Novel architecture proposal", "Requires justifying why the proposed design should outperform existing approaches on a well-defined criterion"],
    ])},
    "artificial-intelligence-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Ethics review framework", "A structured process for evaluating the risks and protections needed for studies involving human interaction with AI"],
        ["Human-subject AI study", "Requires informed consent and risk mitigation similar to other human-subject research, adapted for AI-specific concerns"],
    ])},
    "artificial-intelligence-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["AI governance framework", "Structured policies and processes for managing the risks of increasingly capable AI systems"],
        ["Frontier model risk assessment", "Evaluates the most capable models for specific hazards (e.g. misuse potential) before and after deployment"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Artificial Intelligence"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"artificial-intelligence-m2-l{base_n}"
        worked_key = f"artificial-intelligence-m2-l{worked_n}"
        if base_n == 3:
            CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
        elif base_key in CHARTS:
            CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Missing lesson ids: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson or lesson[key] is None:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Artificial Intelligence lessons.")


if __name__ == "__main__":
    main()
