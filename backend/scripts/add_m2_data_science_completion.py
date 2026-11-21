#!/usr/bin/env python3
"""Depth pass, M2 Data Science: fill in real, hand-checked data_table
content for the M2 Data Science lessons not covered by the earlier
breadth-first batch. Brings M2 Data Science to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning causal
inference, Bayesian and deep generative modeling, representation
learning, explainability and fairness, data-centric AI and MLOps,
recommender systems and bandits, experimental design, and statistical
learning theory; l101-l120 are "Worked Analysis" companions reusing
the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_data_science_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Double machine learning", "Uses flexible ML models to estimate nuisance functions while achieving valid inference for a causal parameter"],
    ["Causal inference", "Estimates the effect of a treatment on an outcome, distinct from merely predicting the outcome"],
])

CHARTS: dict[str, dict] = {
    "data-science-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Data science in industry", "Applies statistical and machine learning methods to solve concrete business or product problems"],
        ["Practical constraint", "Industry work must balance model quality against latency, cost, interpretability, and maintainability requirements"],
    ])},
    "data-science-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Data science capstone", "An applied culminating project demonstrating end-to-end data science skill on a real dataset and problem"],
        ["Deliverable", "Typically includes problem framing, data preparation, modeling, evaluation, and clear communication of results"],
    ])},
    "data-science-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Targeted maximum likelihood estimation", "A doubly robust estimation framework that combines outcome and treatment models for valid causal effect estimates"],
        ["Doubly robust", "Remains consistent if either the outcome model or the treatment model is correctly specified, not necessarily both"],
    ])},
    "data-science-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic control method", "Constructs a weighted combination of untreated units that approximates a treated unit's pre-treatment trajectory"],
        ["Comparative case study", "Well suited when only one or a few units receive a treatment, such as a single region's policy change"],
    ])},
    "data-science-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Regression discontinuity design", "Estimates a causal effect by comparing outcomes just above and below a treatment-assignment threshold"],
        ["Advanced estimation", "Modern approaches carefully select bandwidth and use local polynomial regression to reduce bias near the cutoff"],
    ])},
    "data-science-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Estimates a treatment effect by comparing outcome changes over time between treated and control groups"],
        ["Staggered treatment timing", "Modern estimators correct for bias that arises in traditional DiD when units are treated at different times"],
    ])},
    "data-science-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian structural time series", "Models a time series' components (trend, seasonality) probabilistically to estimate a counterfactual baseline"],
        ["Causal impact", "Compares observed post-intervention outcomes against the model's counterfactual prediction to estimate an effect"],
    ])},
    "data-science-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Gaussian process", "A nonparametric Bayesian model defining a distribution over functions, used for regression with uncertainty estimates"],
        ["Nonparametric regression", "Model complexity grows with the data rather than being fixed in advance, unlike parametric models"],
    ])},
    "data-science-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Variational inference", "Approximates an intractable posterior distribution by optimizing over a simpler family of distributions"],
        ["Scalable Bayesian models", "Turns Bayesian inference into an optimization problem, making it tractable for large datasets and complex models"],
    ])},
    "data-science-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Hamiltonian Monte Carlo", "Uses simulated physical dynamics to propose distant, high-acceptance-rate samples from a target distribution"],
        ["NUTS sampler", "The No-U-Turn Sampler automatically tunes HMC's trajectory length, removing a key manual hyperparameter"],
    ])},
    "data-science-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Probabilistic graphical model", "Represents a joint distribution's conditional independence structure using a graph"],
        ["Structure learning", "Algorithmically infers the graph structure itself from data, rather than assuming it is known in advance"],
    ])},
    "data-science-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Variational autoencoder", "Learns a probabilistic latent representation by optimizing a tractable lower bound on the data likelihood"],
        ["Deep generative model", "Uses a neural network to model complex, high-dimensional data distributions"],
    ])},
    "data-science-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Diffusion probabilistic model", "Generates data by learning to reverse a gradual noising process applied to training examples"],
        ["Deep generative model", "Currently among the strongest performing approaches for high-fidelity image and audio generation"],
    ])},
    "data-science-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Normalizing flow", "Transforms a simple base distribution into a complex one via a sequence of invertible, differentiable mappings"],
        ["Density estimation", "Uniquely among generative models, flows allow exact computation of a data point's likelihood"],
    ])},
    "data-science-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Graph neural network", "A neural architecture that learns representations by passing messages along the edges of a graph"],
        ["Message passing framework", "Each node iteratively aggregates information from its neighbors to update its own representation"],
    ])},
    "data-science-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Graph representation learning", "Learns low-dimensional vector representations of nodes that preserve graph structural properties"],
        ["Node embedding", "Embeds each node such that structurally or semantically similar nodes end up close together in vector space"],
    ])},
    "data-science-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Transformer for tabular data", "Adapts attention-based architectures to structured tabular datasets, an area where tree ensembles often still excel"],
        ["Design challenge", "Tabular features lack the inherent sequential or spatial structure that transformers were originally designed to exploit"],
    ])},
    "data-science-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Self-supervised representation learning", "Learns useful representations from unlabeled data using a pretext task derived from the data itself"],
        ["Pretext task", "A task with automatically generated labels (e.g. predicting a masked portion) that encourages useful representation learning"],
    ])},
    "data-science-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Contrastive learning", "Learns representations by pulling together embeddings of related examples and pushing apart unrelated ones"],
        ["Framework design", "Choices of augmentation, negative sampling, and loss function substantially affect representation quality"],
    ])},
    "data-science-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Meta-learning", "Trains a model across many tasks so it can adapt quickly to a new, related task from limited data"],
        ["Learning to learn", "Optimizes for fast post-adaptation performance across a task distribution, rather than performance on one fixed task"],
    ])},
    "data-science-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Few-shot learning", "A model adapts to a new task from only a small number of labeled examples"],
        ["Zero-shot learning", "A model performs a task or recognizes a class it has never seen labeled examples of during training"],
    ])},
    "data-science-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Multi-task learning", "Trains a single model to perform several related tasks simultaneously, sharing representations across them"],
        ["Shared representation design", "Deciding which layers to share versus keep task-specific is a key architectural choice affecting transfer benefits"],
    ])},
    "data-science-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Domain adaptation", "Adapts a model trained on a source distribution to perform well on a related target distribution"],
        ["Distribution shift", "The mismatch between training and deployment data distributions that domain adaptation aims to correct for"],
    ])},
    "data-science-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Out-of-distribution detection", "Identifies inputs that differ substantially from a model's training distribution"],
        ["Practical purpose", "Flags cases where a model's predictions should not be trusted, since they fall outside its area of competence"],
    ])},
    "data-science-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Conformal prediction", "Produces prediction sets guaranteed to contain the true outcome at a specified confidence level, without distributional assumptions"],
        ["Distribution-free uncertainty", "Coverage guarantees hold regardless of the underlying data distribution, given exchangeability"],
    ])},
    "data-science-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian deep learning", "Treats a network's weights as random variables with a posterior distribution rather than single point estimates"],
        ["Epistemic uncertainty", "Uncertainty arising from limited model knowledge, reducible with more data, distinct from inherent data noise"],
    ])},
    "data-science-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Model calibration", "The alignment between a model's predicted probability and its actual observed frequency of correctness"],
        ["Probabilistic forecast", "A well-calibrated forecast's stated probabilities should match empirical outcome frequencies across many predictions"],
    ])},
    "data-science-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["SHAP", "A unified explainability framework based on Shapley values that attributes a prediction to each input feature"],
        ["Shapley value attribution", "Fairly distributes a prediction's outcome across features by averaging their marginal contribution over all orderings"],
    ])},
    "data-science-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI", "Methods that make a model's predictions understandable to human stakeholders"],
        ["Counterfactual explanation generation", "Identifies the minimal input change that would have flipped the model's prediction"],
    ])},
    "data-science-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Interpretable machine learning", "Building or approximating models whose reasoning process is directly understandable, not just explainable after the fact"],
        ["Rule-based surrogate model", "A simple, interpretable model (e.g. a decision list) trained to approximate a complex black-box model's behavior"],
    ])},
    "data-science-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Fairness metric", "A quantitative criterion for whether a model treats different demographic groups equitably"],
        ["Bias mitigation", "Techniques applied before, during, or after training to reduce unwanted disparities in a predictive model's outcomes"],
    ])},
    "data-science-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic auditing", "Systematically evaluates a deployed predictive system for accuracy, fairness, and unintended harms"],
        ["Deployed system", "Auditing a live system reveals issues that offline evaluation on static test sets can miss"],
    ])},
    "data-science-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Data-centric AI", "Focuses on systematically improving training data quality rather than only iterating on model architecture"],
        ["Label error detection", "Automated methods flag likely mislabeled examples in a dataset for review or correction"],
    ])},
    "data-science-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Active learning", "A model selects which unlabeled examples to have labeled next to maximize learning per labeling cost"],
        ["Label-efficient training", "Reduces the total number of labels needed to reach a target performance level compared with random sampling"],
    ])},
    "data-science-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Weak supervision", "Trains a model using noisy, imprecise, or indirect labeling sources rather than fully hand-labeled data"],
        ["Programmatic labeling", "Uses heuristic labeling functions written as code to generate large volumes of weak training labels"],
    ])},
    "data-science-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Semi-supervised learning", "Combines a small labeled dataset with a larger unlabeled dataset to improve learning"],
        ["Pseudo-labeling", "Uses a model's own confident predictions on unlabeled data as additional training labels"],
    ])},
    "data-science-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Federated learning", "Trains a shared model across decentralized clients without centralizing their raw data"],
        ["Decentralized training", "Only model updates, not raw data, are communicated, offering privacy benefits over centralized training"],
    ])},
    "data-science-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "A mathematical guarantee that a query's output changes negligibly whether or not any single individual's data is included"],
        ["ML pipeline application", "Applied at the training stage to bound how much any individual data point can influence the resulting model"],
    ])},
    "data-science-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge distillation", "Trains a smaller student model to mimic a larger teacher model's output distribution"],
        ["Model compression", "Reduces deployment cost while retaining much of the larger model's predictive performance"],
    ])},
    "data-science-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Neural architecture search", "Automatically searches a space of network designs to find one that performs well on a target task"],
        ["Methodology", "Search strategies range from reinforcement learning and evolutionary methods to gradient-based relaxations"],
    ])},
    "data-science-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hyperparameter optimization", "Builds a probabilistic surrogate model of the objective to intelligently choose which hyperparameters to try next"],
        ["Bandit-based method", "Approaches like Hyperband allocate more compute to promising configurations and stop poor ones early"],
    ])},
    "data-science-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["AutoML", "Automates the end-to-end machine learning pipeline, from feature engineering through model selection and tuning"],
        ["Pipeline automation", "Aims to reduce the manual expertise required to build a strong-performing model for a given dataset"],
    ])},
    "data-science-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["State-space model ensemble", "Combines multiple state-space time series models to produce a more robust forecast"],
        ["Time series forecasting", "Ensembling reduces the risk of relying on any single model's potentially wrong structural assumptions"],
    ])},
    "data-science-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Probabilistic time series forecasting", "Produces a full predictive distribution over future values, not just a single point estimate"],
        ["Deep learning approach", "Neural forecasting models can capture complex nonlinear temporal patterns while still outputting calibrated uncertainty"],
    ])},
    "data-science-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection", "Identifies data points that deviate substantially from the expected distribution"],
        ["High-dimensional streaming data", "Must detect anomalies in real time as data arrives continuously, without storing the full history"],
    ])},
    "data-science-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Change point detection", "Identifies moments where a time series' underlying statistical properties shift"],
        ["Non-stationary time series", "A series whose statistical properties change over time, requiring adaptive rather than fixed models"],
    ])},
    "data-science-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Survival analysis", "Models the time until an event of interest occurs, handling censored observations where the event hasn't yet happened"],
        ["Machine learning extension", "Modern methods combine flexible ML models with survival analysis' handling of censored data"],
    ])},
    "data-science-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Matrix factorization", "Decomposes a user-item interaction matrix into lower-dimensional latent factor matrices"],
        ["Recommender system at scale", "Must handle extremely sparse matrices with millions of users and items efficiently"],
    ])},
    "data-science-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Sequential recommendation", "Models a user's evolving preferences based on the order of their past interactions"],
        ["Session-based model", "Makes recommendations using only the current session's behavior, useful when user identity is unknown"],
    ])},
    "data-science-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Multi-armed bandit", "Balances exploring uncertain options against exploiting known good ones to maximize cumulative reward"],
        ["Online experimentation", "Continuously adapts which options are shown based on accumulating evidence, unlike a fixed A/B test allocation"],
    ])},
    "data-science-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Contextual bandit", "Extends the bandit framework by choosing actions based on observed context features for each decision"],
        ["Personalized decision-making", "Enables tailoring recommendations or interventions to each individual's specific context"],
    ])},
    "data-science-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Reinforcement learning", "Learns a policy that maximizes cumulative reward through trial-and-error interaction with an environment"],
        ["Sequential decision optimization", "Applicable when decisions made now affect the context and rewards available for future decisions"],
    ])},
    "data-science-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Offline reinforcement learning", "Learns a policy from a fixed, previously collected dataset without further environment interaction"],
        ["Logged data", "Common in industry settings where live experimentation is costly, risky, or otherwise constrained"],
    ])},
    "data-science-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Causal discovery", "Algorithmically infers a plausible causal graph structure from purely observational data"],
        ["Observational data", "Requires additional assumptions (e.g. no unmeasured confounders) since causal structure is generally underdetermined by observation alone"],
    ])},
    "data-science-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Represents a system of causal relationships as a set of equations linking variables"],
        ["Causal system", "Enables both estimating the strength of causal paths and simulating the effect of interventions"],
    ])},
    "data-science-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Instrumental variable estimation", "Uses a variable affecting the outcome only through the treatment to identify a causal effect despite confounding"],
        ["High dimensions", "Modern methods combine machine learning with instrumental variables when many potential confounders are present"],
    ])},
    "data-science-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Heterogeneous treatment effect", "The causal effect of a treatment varies across different subgroups or individuals"],
        ["Estimation", "Machine learning methods like causal forests estimate how treatment effects vary as a function of observed covariates"],
    ])},
    "data-science-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Uplift modeling", "Predicts the incremental effect of a treatment on an individual, rather than their outcome probability alone"],
        ["Targeted intervention", "Identifies which individuals will respond most positively to a treatment, focusing limited resources effectively"],
    ])},
    "data-science-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sequential experimental design", "Adapts an experiment's design based on data accumulated during the experiment itself"],
        ["Adaptive trial", "Can reallocate more participants to better-performing arms as evidence accumulates, improving efficiency"],
    ])},
    "data-science-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Power analysis", "Determines the sample size needed to reliably detect an effect of a given size, if it exists"],
        ["Complex experimental design", "Power calculations become more involved for designs with multiple factors, clustering, or interim analyses"],
    ])},
    "data-science-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Quasi-experimental method", "Estimates causal effects from observational data using design features that approximate randomization"],
        ["Observational data science", "Applied when a true randomized experiment is infeasible, unethical, or too costly to run"],
    ])},
    "data-science-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Statistical process control", "Monitors a process over time to detect when it deviates from expected statistical behavior"],
        ["Data quality monitoring", "Applies control-chart techniques to flag unexpected shifts in data pipeline quality or distribution"],
    ])},
    "data-science-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Data lineage", "Tracks the origin and transformation history of data as it moves through a pipeline"],
        ["Provenance tracking system", "Enables reproducibility and debugging by recording exactly how a dataset or feature was derived"],
    ])},
    "data-science-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Feature store", "A centralized system for storing, versioning, and serving machine learning features consistently across training and serving"],
        ["ML system architecture", "Prevents training-serving skew by ensuring the same feature computation logic is used in both contexts"],
    ])},
    "data-science-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["MLOps", "Practices for reliably building, deploying, and maintaining machine learning systems in production"],
        ["Continuous training pipeline", "Automatically retrains and redeploys models as new data becomes available, reducing manual intervention"],
    ])},
    "data-science-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Model monitoring", "Tracks a deployed model's performance and input characteristics over time"],
        ["Drift detection", "Identifies when the production data distribution diverges enough from training data to warrant retraining"],
    ])},
    "data-science-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Distributed computing framework", "Software (e.g. Spark) that coordinates data processing across many machines in a cluster"],
        ["Large-scale data processing", "Enables processing datasets too large to fit or process efficiently on a single machine"],
    ])},
    "data-science-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Graph database", "Stores data as nodes and relationships, optimized for traversal-heavy queries over connected data"],
        ["Query optimization", "Graph query planners must estimate the cost of traversal paths, differing fundamentally from relational join optimization"],
    ])},
    "data-science-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Vector database", "Stores high-dimensional embeddings and supports fast approximate nearest-neighbor search over them"],
        ["Similarity search at scale", "Index structures like HNSW enable sub-linear search over millions or billions of embeddings"],
    ])},
    "data-science-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Streaming data architecture", "A system design for processing continuously arriving data with low latency"],
        ["Exactly-once processing", "Guarantees each record affects the output state exactly once, even after failures and restarts"],
    ])},
    "data-science-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh", "A decentralized data architecture where domain teams own and serve their own data products"],
        ["Decentralized platform architecture", "Contrasts with a single centralized data team owning all pipelines, aiming to improve scalability and ownership"],
    ])},
    "data-science-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving record linkage", "Matches records referring to the same entity across datasets without revealing the underlying sensitive identifiers"],
        ["Technique", "Uses cryptographic hashing or secure computation so matching can occur without exposing raw personal data"],
    ])},
    "data-science-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic data generation", "Creates artificial data that statistically resembles real data without exposing actual individual records"],
        ["Privacy-preserving analytics", "Enables sharing and analysis of data-like resources while reducing the risk of re-identifying real individuals"],
    ])},
    "data-science-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Topological data analysis", "Uses tools from topology to study the shape of data, robust to noise and choice of metric"],
        ["Persistent homology", "Tracks topological features (connected components, loops) across multiple scales of the data"],
    ])},
    "data-science-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Manifold learning", "Assumes high-dimensional data lies on a lower-dimensional curved manifold and seeks to recover that structure"],
        ["Nonlinear dimensionality reduction", "Techniques like t-SNE and UMAP preserve local neighborhood structure when projecting to lower dimensions"],
    ])},
    "data-science-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Spectral clustering", "Clusters data using eigenvectors of a similarity graph's Laplacian matrix"],
        ["Graph partitioning", "Frames clustering as finding a graph cut that minimizes connections between groups while balancing group sizes"],
    ])},
    "data-science-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Robust statistics", "Estimation methods designed to remain accurate even when data contains outliers or violates model assumptions"],
        ["Outlier-resistant estimation", "Methods like the median or trimmed mean are far less sensitive to extreme values than the ordinary mean"],
    ])},
    "data-science-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["High-dimensional inference", "Statistical inference when the number of features approaches or exceeds the number of observations"],
        ["Curse of dimensionality", "Distances and density estimates behave counterintuitively as dimensionality grows, degrading many classical methods"],
    ])},
    "data-science-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Lasso", "Adds an L1 penalty to regression, driving some coefficients exactly to zero and performing automatic feature selection"],
        ["Elastic net", "Combines L1 and L2 penalties, handling correlated features better than lasso alone"],
    ])},
    "data-science-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Stacking", "Combines predictions from multiple base models using a meta-model trained on their outputs"],
        ["Boosting theory", "Sequentially trains models to correct the errors of the previous ensemble, provably reducing training error under mild conditions"],
    ])},
    "data-science-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Gradient boosting", "Sequentially fits models to the residual errors of the current ensemble, framed as gradient descent in function space"],
        ["Advanced implementation", "Modern libraries add regularization, histogram-based splitting, and parallelization for speed and accuracy"],
    ])},
    "data-science-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Kernel method", "Implicitly maps data into a high-dimensional feature space via a kernel function, enabling nonlinear learning with linear algorithms"],
        ["Reproducing kernel Hilbert space", "The mathematical space in which kernel methods implicitly operate, providing their theoretical foundation"],
    ])},
    "data-science-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["VC dimension", "A measure of a hypothesis class's capacity to fit arbitrary labelings of a set of points"],
        ["Generalization bound", "Relates a model's training error, VC dimension, and sample size to a guarantee on its test error"],
    ])},
    "data-science-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["PAC learning", "A theoretical framework defining what it means for a learning algorithm to probably approximately correctly learn a concept"],
        ["Sample complexity", "The number of training examples required to guarantee a learning algorithm reaches a target accuracy with high probability"],
    ])},
    "data-science-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Non-convex optimization", "Optimizing objective functions with multiple local minima, as is typical for deep neural network training"],
        ["ML landscape", "Despite non-convexity, gradient-based methods empirically find good solutions for many overparameterized deep networks"],
    ])},
    "data-science-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Second-order optimization", "Uses curvature information (e.g. an approximate Hessian) to inform parameter updates, beyond first-order gradients"],
        ["Deep learning application", "Approximate second-order methods aim to capture curvature benefits while remaining tractable at large scale"],
    ])},
    "data-science-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Transformer fine-tuning", "Adapts a large pretrained language model to a specific downstream task using additional targeted training"],
        ["Fine-tuning strategy", "Approaches range from full fine-tuning to parameter-efficient methods that update only a small fraction of weights"],
    ])},
    "data-science-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Retrieval-augmented generation", "Conditions a language model's output on documents retrieved from an external knowledge source at inference time"],
        ["Architecture", "Combines a retriever module with a generator module, jointly or separately optimized"],
    ])},
    "data-science-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Self-supervised pretraining (vision)", "Learns visual representations from unlabeled images using a pretext task derived from the images themselves"],
        ["Computer vision strategy", "Reduces reliance on large labeled image datasets, which are expensive to produce"],
    ])},
    "data-science-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal learning", "Trains models that jointly process and relate information from more than one modality, such as vision and language"],
        ["Joint representation", "Learns a shared embedding space where related concepts across modalities map close together"],
    ])},
    "data-science-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Data ethics", "Considers the moral implications of collecting, analyzing, and acting on data"],
        ["Institutional review", "Formal oversight processes that evaluate the ethical risks of data science projects involving human data"],
    ])},
    "data-science-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Reproducibility", "The ability for others to obtain the same results using the same data and code"],
        ["Computational standard", "Version control, environment specification, and documented pipelines all support reproducible data science"],
    ])},
    "data-science-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Statistical significance", "A result unlikely to have occurred by chance alone under a null hypothesis, given a chosen threshold"],
        ["Big data caveat", "With very large sample sizes, even trivially small and practically meaningless effects can reach statistical significance"],
    ])},
    "data-science-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Multiple hypothesis testing", "Testing many hypotheses simultaneously increases the chance of false positives unless corrected for"],
        ["False discovery rate control", "Methods like Benjamini-Hochberg control the expected proportion of false positives among rejected hypotheses"],
    ])},
    "data-science-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Bootstrap inference", "Estimates a statistic's sampling distribution by repeatedly resampling with replacement from the observed data"],
        ["Permutation-based inference", "Tests a hypothesis by comparing an observed statistic to its distribution under random relabelings of the data"],
    ])},
    "data-science-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic network analysis", "Studies how a network's structure and properties change over time"],
        ["Temporal graph model", "Represents edges as time-stamped events rather than a single static snapshot of connections"],
    ])},
    "data-science-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Topic modeling", "Discovers latent thematic structure across a collection of documents"],
        ["Latent Dirichlet Allocation", "A generative probabilistic model representing each document as a mixture of latent topics"],
    ])},
    "data-science-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Large-scale A/B testing infrastructure", "Systems that reliably run, monitor, and analyze many concurrent controlled experiments"],
        ["Design consideration", "Must handle experiment interaction effects, sample ratio mismatches, and consistent user bucketing at scale"],
    ])},
    "data-science-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to data science methodology"],
        ["Original contribution", "Requires identifying a genuine gap in existing methods and offering a novel, rigorously evaluated resolution"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Data Science"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"data-science-m2-l{base_n}"
        worked_key = f"data-science-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Data Science lessons.")


if __name__ == "__main__":
    main()
