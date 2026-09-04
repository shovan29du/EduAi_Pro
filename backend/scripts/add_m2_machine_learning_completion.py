#!/usr/bin/env python3
"""Depth pass, M2 Machine Learning: fill in real, hand-checked
data_table content for the M2 Machine Learning lessons not covered by
the earlier breadth-first batch. Brings M2 Machine Learning to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
generalization theory, generative modeling, self-supervised and
meta-learning, model compression, causal/robust learning,
interpretability, reinforcement learning theory, and large-model
scaling/alignment topics.

Offset quirk (unlike most M2 subjects): l101 is a standalone "Thesis
Capstone" lesson with no l1-l20 counterpart, and l102-l120 are "Worked
Analysis" companions reusing the data_table of l1-l19 with a shifted
1:1 mapping (base_n = worked_n - 101, valid for worked_n 102-120). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it maps to l104).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_machine_learning_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Neural tangent kernel", "Describes the training dynamics of an infinitely wide neural network as equivalent to kernel regression"],
    ["Wide network limit", "As width grows, the network's function stays close to its linearization around initialization throughout training"],
])

CHARTS: dict[str, dict] = {
    "machine-learning-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Responsible ML", "Practices ensuring a deployed model's decisions are fair, transparent, robust, and accountable"],
        ["Key pillars", "Fairness, interpretability, privacy, and robustness are commonly cited pillars of responsible ML practice"],
    ])},
    "machine-learning-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["ML research methods", "Rigorous experimental design, ablation studies, and statistically sound comparison against baselines"],
        ["Capstone framing", "A graduate ML capstone should isolate one clear research question and test it with controlled comparisons"],
    ])},
    "machine-learning-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["PAC-Bayesian bound", "A generalization bound expressed in terms of a KL divergence between a learned posterior and a fixed prior over hypotheses"],
        ["Deep learning application", "Provides some of the tightest known non-vacuous generalization guarantees for large overparameterized networks"],
    ])},
    "machine-learning-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Double descent", "Test error can rise near the interpolation threshold before falling again as model capacity keeps increasing"],
        ["Model risk curve", "Challenges the classical U-shaped bias-variance curve as the sole predictor of generalization"],
    ])},
    "machine-learning-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Lottery ticket hypothesis", "A randomly initialized dense network contains a sparse subnetwork that, trained in isolation, matches full-network accuracy"],
        ["Sparse subnetwork discovery", "Iterative pruning and rewinding to early weights is the classic method for finding such winning tickets"],
    ])},
    "machine-learning-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Diffusion model", "Generates data by learning to reverse a gradual noising process applied to training examples"],
        ["Score-based modeling", "Trains a network to estimate the gradient of the data's log-density at each noise level"],
    ])},
    "machine-learning-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Normalizing flow", "Transforms a simple base distribution into a complex one via a sequence of invertible, differentiable mappings"],
        ["Exact likelihood", "Unlike VAEs or GANs, flows allow exact computation of the likelihood of a data point via the change-of-variables formula"],
    ])},
    "machine-learning-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Variational autoencoder", "Learns a probabilistic latent representation by optimizing a tractable lower bound on the data likelihood (the ELBO)"],
        ["Posterior collapse", "A failure mode where the model ignores the latent variable, relying only on the decoder to reconstruct data"],
    ])},
    "machine-learning-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive self-supervised learning", "Learns representations by pulling together augmented views of the same example and pushing apart different examples"],
        ["Theoretical grounding", "Can be framed as approximately maximizing a mutual information bound between representations of related views"],
    ])},
    "machine-learning-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Masked autoencoding", "Trains a model to reconstruct randomly masked portions of an input, learning representations without labels"],
        ["Vision pretraining", "Masking a high fraction of image patches forces the model to learn holistic, semantically useful representations"],
    ])},
    "machine-learning-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["MAML", "Model-agnostic meta-learning trains initial parameters that can adapt to a new task in only a few gradient steps"],
        ["Meta-learning theory", "Optimizes for post-adaptation performance across a distribution of tasks, not performance on any single task"],
    ])},
    "machine-learning-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian optimization", "Builds a probabilistic surrogate model of an expensive objective to decide which point to evaluate next"],
        ["Black-box hyperparameter search", "Well suited when each evaluation (a full model training run) is costly, since it minimizes the number of evaluations needed"],
    ])},
    "machine-learning-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Differentiable NAS", "Relaxes the discrete architecture search space into a continuous one so gradients can guide the search"],
        ["Evolutionary NAS", "Uses population-based mutation and selection to explore the discrete architecture space directly"],
    ])},
    "machine-learning-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to match a larger teacher model's output distribution"],
        ["Teacher-student compression", "Soft targets from the teacher transfer more nuanced information than hard labels alone"],
    ])},
    "machine-learning-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Quantization-aware training", "Simulates low-precision arithmetic during training so weights adapt to quantization error before deployment"],
        ["Low-precision inference", "Enables running models with reduced memory and compute cost using 8-bit or lower-precision weights"],
    ])},
    "machine-learning-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Structured pruning", "Removes entire structural units (channels, filters) rather than individual weights"],
        ["Compression benefit", "Yields a smaller dense model that runs faster on standard hardware without specialized sparse-matrix support"],
    ])},
    "machine-learning-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network expressiveness", "The theoretical limit on which graph structures a GNN architecture can distinguish"],
        ["Weisfeiler-Lehman test", "Standard message-passing GNNs are provably no more powerful than the 1-WL graph isomorphism test"],
    ])},
    "machine-learning-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Equivariant neural network", "A network whose output transforms predictably when its input undergoes a known symmetry transformation"],
        ["Symmetry-preserving learning", "Building in known symmetries improves sample efficiency for tasks with inherent geometric structure"],
    ])},
    "machine-learning-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Geometric deep learning", "Extends deep learning to non-Euclidean domains such as graphs, manifolds, and meshes"],
        ["Non-Euclidean domain", "Requires generalized notions of convolution and locality that don't assume a regular grid structure"],
    ])},
    "machine-learning-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Causal representation learning", "Learns latent variables corresponding to causal factors underlying observed data, not merely correlational features"],
        ["Observational data", "Causal factors are generally underdetermined by observational data alone without further structural assumptions"],
    ])},
    "machine-learning-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Invariant risk minimization", "Learns a predictor whose optimal relationship to the label is invariant across multiple training environments"],
        ["Out-of-distribution generalization", "Aims to discard spurious environment-specific correlations in favor of stable causal features"],
    ])},
    "machine-learning-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Domain adaptation theory", "Studies how a source-trained model can be adapted to perform well on a related target distribution"],
        ["Distributional shift bound", "Generalization bounds relate target error to source error plus a measure of distance between the two distributions"],
    ])},
    "machine-learning-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial robustness", "A model's ability to maintain correct predictions under small, adversarially crafted input perturbations"],
        ["Certified defense", "Provides a mathematical guarantee that no perturbation within a bound can change the model's output, unlike empirical defenses"],
    ])},
    "machine-learning-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Adversarial example", "An input crafted with a small perturbation designed to cause a model misclassification"],
        ["Transferability", "Adversarial examples crafted for one model often also fool other independently trained models"],
    ])},
    "machine-learning-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["DP-SGD", "Adds calibrated noise to clipped per-example gradients during training to provide a formal differential privacy guarantee"],
        ["Privacy-utility trade-off", "Stronger privacy guarantees (more noise) generally come at the cost of reduced model accuracy"],
    ])},
    "machine-learning-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning", "Trains a shared model across decentralized clients without centralizing their raw data"],
        ["Non-IID client data", "Client data distributions differ from each other, complicating convergence guarantees that assume identical distributions"],
    ])},
    "machine-learning-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Membership inference attack", "Determines whether a specific data point was part of a model's training set from its output behavior"],
        ["Privacy risk", "Successful attacks can reveal sensitive information about individuals whose data was used in training"],
    ])},
    "machine-learning-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Model inversion attack", "Reconstructs approximate training examples by exploiting a trained model's outputs or gradients"],
        ["Training data reconstruction", "Especially concerning when training data contains sensitive personal information"],
    ])},
    "machine-learning-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Mechanistic interpretability", "Reverse-engineers a trained network's weights into human-understandable algorithms"],
        ["Circuit-level analysis", "Identifies minimal subgraphs of components (attention heads, neurons) implementing a specific computation"],
    ])},
    "machine-learning-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Sparse autoencoder", "Decomposes a network's dense internal activations into a larger set of sparse, more interpretable features"],
        ["Superposed features", "Addresses the problem that networks often represent more concepts than they have dimensions"],
    ])},
    "machine-learning-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Shapley value", "A game-theoretic method that fairly attributes a prediction's outcome to each input feature's contribution"],
        ["Attribution method", "Averages a feature's marginal contribution across all possible orderings of the other features"],
    ])},
    "machine-learning-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual explanation", "Identifies the minimal change to an input that would flip a black-box model's prediction"],
        ["Black-box model", "Applicable without needing access to the model's internal structure, only its input-output behavior"],
    ])},
    "machine-learning-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Concept bottleneck model", "Forces predictions to pass through an intermediate layer of human-interpretable concepts before the final output"],
        ["Interpretable pipeline", "Lets a practitioner intervene on the concept layer to understand or correct the model's reasoning"],
    ])},
    "machine-learning-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Curriculum learning", "Trains a model on examples ordered from easier to harder rather than in random order"],
        ["Training order optimization", "The order in which examples are presented can meaningfully affect convergence speed and final performance"],
    ])},
    "machine-learning-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Active learning", "A model selects which unlabeled examples to have labeled next to maximize learning per labeling cost"],
        ["Query strategy", "Uncertainty sampling and expected model change are common strategies for choosing informative examples"],
    ])},
    "machine-learning-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Semi-supervised learning", "Combines a small labeled dataset with a larger unlabeled dataset to improve learning"],
        ["Consistency regularization", "Encourages the model to produce similar outputs for an unlabeled example and its perturbed version"],
    ])},
    "machine-learning-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Self-training", "A model labels unlabeled data with its own confident predictions and retrains on the expanded pseudo-labeled set"],
        ["Theoretical guarantee", "Convergence generally requires the model's initial predictions to be sufficiently accurate to avoid reinforcing errors"],
    ])},
    "machine-learning-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Multi-task learning", "Trains a single model to perform several related tasks simultaneously, sharing representations across them"],
        ["Gradient conflict", "Occurs when different tasks' gradients point in opposing directions, requiring balancing techniques"],
    ])},
    "machine-learning-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Elastic weight consolidation", "Penalizes changes to parameters deemed important for previously learned tasks during sequential training"],
        ["Sequential task learning", "Aims to mitigate catastrophic forgetting when a model must learn new tasks over time"],
    ])},
    "machine-learning-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Policy gradient theorem", "Provides a formula for the gradient of expected return with respect to policy parameters, without needing a model of the environment"],
        ["Derivation basis", "Underlies practical algorithms like REINFORCE and actor-critic methods"],
    ])},
    "machine-learning-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Proximal policy optimization", "Updates a policy while constraining how far it can move from the previous policy, improving training stability"],
        ["Trust region constraint", "Prevents destructively large policy updates that could collapse performance"],
    ])},
    "machine-learning-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Offline reinforcement learning", "Learns a policy from a fixed, previously collected dataset without further environment interaction"],
        ["Fixed batch dataset", "The policy must avoid overestimating the value of actions poorly represented in the static dataset"],
    ])},
    "machine-learning-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Model-based reinforcement learning", "Learns a model of environment dynamics and uses it for planning, rather than relying purely on trial and error"],
        ["World model learning", "A more sample-efficient approach than model-free RL, at the cost of potential model-bias errors"],
    ])},
    "machine-learning-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Sparse-reward exploration", "Techniques for effective exploration when an agent receives useful reward feedback only rarely"],
        ["Exploration strategy", "Intrinsic motivation and curiosity-driven bonuses are common approaches to encourage exploration absent frequent reward"],
    ])},
    "machine-learning-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Credit assignment problem", "Determining which agent(s) and which action(s) were responsible for a shared outcome"],
        ["Multi-agent RL", "Especially difficult when multiple agents act simultaneously and share a joint reward signal"],
    ])},
    "machine-learning-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Inverse reinforcement learning", "Infers an unknown reward function from observed expert behavior, rather than assuming it is given"],
        ["Reward function recovery", "The inferred reward can generalize expert intent to states not directly observed in the demonstrations"],
    ])},
    "machine-learning-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Gaussian process", "A nonparametric Bayesian model defining a distribution over functions, used for regression with uncertainty estimates"],
        ["Nonparametric regression", "Model complexity grows with the data rather than being fixed in advance, unlike parametric models"],
    ])},
    "machine-learning-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian deep learning", "Treats a network's weights as random variables with a posterior distribution rather than single point estimates"],
        ["Posterior approximation", "Exact Bayesian inference is intractable for deep networks, so variational or ensemble methods approximate the posterior"],
    ])},
    "machine-learning-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Deep ensemble", "Trains multiple independently initialized networks and combines their predictions"],
        ["Predictive uncertainty quantification", "Disagreement among ensemble members provides a practical estimate of predictive uncertainty"],
    ])},
    "machine-learning-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Conformal prediction", "Produces prediction sets guaranteed to contain the true outcome at a specified confidence level, without distributional assumptions"],
        ["Distribution-free uncertainty", "Coverage guarantees hold regardless of the underlying data distribution, given exchangeability"],
    ])},
    "machine-learning-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Optimal transport", "A mathematical framework for measuring the minimal cost of transforming one distribution into another"],
        ["Generative modeling application", "Underlies Wasserstein GANs, which use an optimal-transport-based distance for more stable training"],
    ])},
    "machine-learning-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["GAN training stability", "The generator and discriminator's adversarial training dynamic is prone to oscillation and mode collapse"],
        ["Stability theory", "Analyzes conditions (e.g. gradient penalties, spectral normalization) that help training converge reliably"],
    ])},
    "machine-learning-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Energy-based model", "Defines a probability distribution implicitly via an energy function, with likely samples having low energy"],
        ["Contrastive divergence", "An approximate training method that estimates the gradient using short MCMC chains rather than exact sampling"],
    ])},
    "machine-learning-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Scaled dot-product attention", "Computes attention weights via the dot product of queries and keys, scaled to control gradient magnitude"],
        ["Attention derivation", "The scaling factor prevents dot products from growing too large in magnitude as the key dimension increases"],
    ])},
    "machine-learning-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Efficient transformer", "Architectures that reduce attention's quadratic time and memory complexity for long sequences"],
        ["Long-sequence modeling", "Techniques include sparse attention patterns, linear attention approximations, and chunked processing"],
    ])},
    "machine-learning-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Mixture-of-experts", "Routes each input to a sparse subset of specialized expert subnetworks rather than the whole model"],
        ["Sparse model scaling", "Increases total parameter count while keeping per-token compute roughly constant"],
    ])},
    "machine-learning-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Scaling law", "An empirical power-law relationship between model loss and model size, data size, or compute"],
        ["Neural language model performance", "Enables predicting the performance of a larger model from smaller-scale training runs"],
    ])},
    "machine-learning-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Emergent ability", "A qualitative skill that appears abruptly once a model crosses a scale threshold, absent in smaller models"],
        ["Phase transition", "The sharp, non-smooth jump in capability resembles a phase transition rather than gradual improvement"],
    ])},
    "machine-learning-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["In-context learning theory", "Studies why large language models can adapt to new tasks from examples in their prompt, without weight updates"],
        ["Large language model", "In-context learning capability tends to emerge and strengthen with model scale"],
    ])},
    "machine-learning-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Chain-of-thought prompting", "Prompts a model to generate intermediate reasoning steps before its final answer"],
        ["Emergent reasoning capability", "Often improves accuracy on multi-step tasks, and its benefit tends to grow with model scale"],
    ])},
    "machine-learning-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["RLHF", "Fine-tunes a model using a reward signal derived from human preference comparisons"],
        ["Reward modeling", "A separate model is trained to predict human preference scores, which then guides the policy's RL fine-tuning"],
    ])},
    "machine-learning-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Direct preference optimization", "Fine-tunes a model directly on preference data using a closed-form loss, without a separate reward model"],
        ["RLHF alternative", "Simplifies the RLHF pipeline by removing the reinforcement learning step and its associated instability"],
    ])},
    "machine-learning-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Constitutional AI", "Trains a model to critique and revise its own outputs against a written set of principles"],
        ["Self-critique alignment", "Reduces reliance on large volumes of human preference labels by encoding guidance as explicit rules"],
    ])},
    "machine-learning-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Mechanistic analysis of in-context learning", "Investigates which internal circuits enable a model to adapt behavior from prompt examples"],
        ["Induction head", "A key identified circuit that predicts the next token by finding and copying from a prior similar context"],
    ])},
    "machine-learning-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented generation", "Conditions a language model's output on documents retrieved from an external knowledge source at inference time"],
        ["Architecture design", "Combines a retriever module with a generator module, jointly or separately optimized"],
    ])},
    "machine-learning-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Vector database", "Stores high-dimensional embeddings and supports fast approximate nearest-neighbor search over them"],
        ["Semantic search indexing", "Index structures like HNSW enable sub-linear search over millions or billions of embeddings"],
    ])},
    "machine-learning-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Model calibration", "The alignment between a model's predicted confidence and its actual accuracy"],
        ["Structured prediction", "Calibration is harder to define and measure for sequence outputs than for single-label classification"],
    ])},
    "machine-learning-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Label noise", "Training labels that are incorrect due to annotation error or ambiguity"],
        ["Robust training method", "Loss correction and sample reweighting techniques reduce the impact of mislabeled examples on the trained model"],
    ])},
    "machine-learning-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Class imbalance", "A dataset where some classes have far fewer examples than others, biasing naive training toward the majority class"],
        ["Cost-sensitive and resampling methods", "Reweight the loss or resample the data to compensate for unequal class frequencies"],
    ])},
    "machine-learning-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Online learning", "Updates a model incrementally as data arrives sequentially, rather than training on a fixed batch"],
        ["Regret minimization", "Measures performance by comparing cumulative loss against the best fixed strategy in hindsight"],
    ])},
    "machine-learning-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Upper confidence bound", "Selects the action with the highest optimistic estimate of its potential reward, balancing exploration and exploitation"],
        ["Thompson sampling", "Selects actions by sampling from a posterior belief distribution over each action's expected reward"],
    ])},
    "machine-learning-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Kernel method", "Implicitly maps data into a high-dimensional feature space via a kernel function, enabling nonlinear learning with linear algorithms"],
        ["Representer theorem", "Guarantees that the optimal solution to many kernel-based learning problems can be written as a combination of training examples"],
    ])},
    "machine-learning-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Spectral clustering", "Clusters data using eigenvectors of a similarity graph's Laplacian matrix"],
        ["Graph Laplacian theory", "Captures the graph's connectivity structure in a way that reveals natural cluster boundaries"],
    ])},
    "machine-learning-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Manifold learning", "Assumes high-dimensional data lies on a lower-dimensional curved manifold and seeks to recover that structure"],
        ["Nonlinear dimensionality reduction", "Techniques like t-SNE and UMAP preserve local neighborhood structure when projecting to lower dimensions"],
    ])},
    "machine-learning-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Topological data analysis", "Uses tools from topology to study the shape of data, robust to noise and choice of metric"],
        ["Persistent homology", "Tracks topological features (connected components, loops) across multiple scales of the data"],
    ])},
    "machine-learning-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Deep state space model", "Combines a learned linear or nonlinear state-space recurrence with deep learning for sequence modeling"],
        ["Time series forecasting", "Offers efficient long-range sequence modeling as an alternative to attention-based forecasting models"],
    ])},
    "machine-learning-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection", "Identifies data points that deviate substantially from the expected distribution"],
        ["High-dimensional data streams", "Detecting anomalies is harder in high dimensions due to the curse of dimensionality affecting distance measures"],
    ])},
    "machine-learning-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Fairness metric", "A quantitative criterion for whether a model treats different demographic groups equitably"],
        ["Mathematical incompatibility", "Certain fairness definitions, such as calibration and equalized odds, cannot generally be satisfied simultaneously"],
    ])},
    "machine-learning-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic recourse", "Identifies the minimal changes an individual could make to receive a different, more favorable model decision"],
        ["Actionable counterfactual fairness", "Recourse should propose changes to features an individual can actually control, not immutable characteristics"],
    ])},
    "machine-learning-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Data valuation", "Quantifies how much each training example contributes to a model's overall performance"],
        ["ML pipeline application", "Used for pricing data contributions, curating datasets, and identifying harmful or low-value examples"],
    ])},
    "machine-learning-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Influence function", "Approximates how much a model's output would change if a given training point were removed, without retraining"],
        ["Training data attribution", "Identifies which training examples most influenced a specific model prediction"],
    ])},
    "machine-learning-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Loss landscape geometry", "The shape of the loss function over a network's high-dimensional parameter space"],
        ["Mode connectivity", "Different local minima found by training are often connected by low-loss paths through parameter space"],
    ])},
    "machine-learning-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Sharpness-aware minimization", "Explicitly optimizes for parameters in a flat region of the loss landscape, not just low loss value"],
        ["Flat minima generalization", "Flatter minima are empirically and theoretically associated with better generalization to unseen data"],
    ])},
    "machine-learning-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Second-order optimization", "Uses curvature information (e.g. an approximate Hessian) to inform parameter updates, beyond first-order gradients"],
        ["Large-scale training", "Approximate second-order methods aim to capture some curvature benefit while remaining tractable at scale"],
    ])},
    "machine-learning-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Learning rate schedule", "A plan for how the learning rate changes over the course of training"],
        ["Warmup dynamics", "Gradually increasing the learning rate at the start of training stabilizes early updates before the main schedule takes over"],
    ])},
    "machine-learning-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Batch normalization", "Normalizes layer activations using batch statistics to stabilize and accelerate training"],
        ["Internal covariate shift debate", "The original explanation for why batch norm works has been contested by later theoretical analyses"],
    ])},
    "machine-learning-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Implicit regularization", "Gradient descent itself, without explicit penalty terms, biases overparameterized models toward simpler solutions"],
        ["Overparameterized regime", "Explains why heavily overparameterized networks trained without explicit regularization can still generalize well"],
    ])},
    "machine-learning-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Self-supervised speech representation", "Learns useful audio representations from raw waveforms without transcription labels"],
        ["wav2vec-style pretraining", "Trains a model to distinguish true future audio segments from distractors, similar to contrastive learning"],
    ])},
    "machine-learning-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal contrastive pretraining", "Trains representations so matched pairs across modalities (e.g. image and text) map close together"],
        ["CLIP-style architecture", "Uses a contrastive loss over large-scale image-text pairs to learn a shared embedding space"],
    ])},
    "machine-learning-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Cross-modal retrieval", "Finds items in one modality (e.g. images) that best match a query in another modality (e.g. text)"],
        ["Alignment theory", "Relies on a shared embedding space where semantic similarity across modalities corresponds to geometric closeness"],
    ])},
    "machine-learning-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Neural radiance field", "Represents a 3D scene implicitly as a neural network mapping spatial coordinates to color and density"],
        ["Implicit 3D representation", "Enables photorealistic novel-view synthesis without an explicit mesh or voxel representation"],
    ])},
    "machine-learning-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Physics-informed neural network", "Incorporates known governing differential equations directly into the network's training loss"],
        ["PDE-constrained learning", "Lets the network respect physical laws even in regions with sparse or no direct training data"],
    ])},
    "machine-learning-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Graph attention network", "Learns to weight the importance of each neighboring node's features when aggregating graph information"],
        ["Learned edge importance", "Unlike fixed-weight aggregation, attention lets the model adaptively focus on the most relevant neighbors"],
    ])},
    "machine-learning-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Hyperbolic embedding", "Embeds data into hyperbolic (negatively curved) space, which naturally accommodates tree-like hierarchical structure"],
        ["Hierarchical data representation", "Hyperbolic space can represent exponentially growing hierarchies with far fewer dimensions than Euclidean space"],
    ])},
    "machine-learning-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Zero-shot learning", "A model performs a task or recognizes a class it has never seen labeled examples of during training"],
        ["Few-shot learning", "A model adapts to a new task from only a small number of labeled examples"],
    ])},
    "machine-learning-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Model merging", "Combines the weights of multiple fine-tuned models into a single model without additional training"],
        ["Weight interpolation across fine-tunes", "Simple linear averaging of weights can, surprisingly, combine capabilities when models share a common pretraining lineage"],
    ])},
    "machine-learning-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["LoRA", "Low-rank adaptation fine-tunes a model by learning small low-rank update matrices rather than all original weights"],
        ["Adapter method", "Inserts small trainable modules into a frozen pretrained model, updating only a small fraction of parameters"],
    ])},
    "machine-learning-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Watermarking", "Embeds a statistically detectable signal into a generative model's output for later identification"],
        ["Output provenance", "Enables tracing generated content back to its source model, aiding accountability and misuse detection"],
    ])},
    "machine-learning-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Machine unlearning", "Removes the influence of specific training examples from a trained model without full retraining"],
        ["Efficient removal", "Motivated by privacy regulations granting individuals the right to have their data's influence deleted"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Machine Learning"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    CHARTS["machine-learning-m2-l101"] = {"data_table": table(["Term", "Meaning"], [
        ["Thesis capstone", "An original research project demonstrating independent mastery of machine learning research methods"],
        ["Original research project", "Requires a clear hypothesis, appropriate baselines, and a rigorous experimental evaluation"],
    ])}

    for worked_n in range(102, 121):
        base_n = worked_n - 101
        base_key = f"machine-learning-m2-l{base_n}"
        worked_key = f"machine-learning-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Machine Learning lessons.")


if __name__ == "__main__":
    main()
