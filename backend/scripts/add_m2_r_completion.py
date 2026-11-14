#!/usr/bin/env python3
"""Depth pass, M2 R: fill in real, hand-checked data_table content for
the M2 R lessons not covered by the earlier breadth-first batch.
Brings M2 R to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning advanced
Bayesian computation (Stan, INLA, brms), structural equation and
multilevel modeling, survival and spatiotemporal statistics, advanced
time series and causal inference methods in R, text mining and NLP,
advanced ML pipelines (tidymodels, gradient boosting internals),
package development and performance (Rcpp, R6, data.table),
psychometrics, genomics/Bioconductor, ecological and econometric
modeling, and advanced statistical computing/simulation methodology;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_r_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Hamiltonian Monte Carlo", "Uses simulated physical dynamics to propose distant, high-acceptance-rate samples from a target distribution"],
    ["No-U-Turn Sampler", "Automatically tunes HMC's trajectory length in Stan, removing a key manual hyperparameter from the sampling process"],
])

CHARTS: dict[str, dict] = {
    "r-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Advanced R programming", "Deep understanding of R's object systems, evaluation model, and performance characteristics"],
        ["Application", "Enables writing efficient, idiomatic R code for complex statistical and data analysis tasks"],
    ])},
    "r-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["R capstone data analysis project", "An applied culminating project demonstrating end-to-end statistical analysis skill in R"],
        ["Deliverable", "Typically includes data wrangling, modeling, diagnostic checking, and clear communication of statistical findings"],
    ])},
    "r-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Integrated Nested Laplace Approximation", "A fast deterministic alternative to MCMC for Bayesian inference in latent Gaussian models"],
        ["R-INLA", "An R package implementing INLA, particularly efficient for spatial and spatiotemporal Bayesian models"],
    ])},
    "r-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian nonparametric model", "A model whose complexity can grow with the data rather than being fixed in advance"],
        ["Dirichlet process", "A distribution over distributions commonly used as a prior for the number of clusters in mixture models, without fixing it beforehand"],
    ])},
    "r-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Models relationships among observed and latent variables using a system of simultaneous equations"],
        ["lavaan", "A widely used R package for fitting structural equation models with a concise model specification syntax"],
    ])},
    "r-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Multilevel structural equation modeling", "Extends SEM to properly account for data nested within groups, such as students within schools"],
        ["Application", "Separates within-group and between-group relationships that a single-level SEM would conflate"],
    ])},
    "r-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian multilevel modeling", "Fits hierarchical models using Bayesian inference, naturally quantifying uncertainty at every level"],
        ["brms", "An R package providing a user-friendly interface to fit complex Bayesian multilevel models using Stan as its backend"],
    ])},
    "r-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Gaussian process regression", "A nonparametric Bayesian regression method defining a distribution over functions"],
        ["GPfit and kernlab", "R packages implementing Gaussian process regression with different kernel and optimization approaches"],
    ])},
    "r-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Functional data analysis", "Treats entire curves or functions, rather than individual data points, as the basic unit of statistical analysis"],
        ["fda package", "Provides R tools for representing, smoothing, and modeling functional data such as growth curves"],
    ])},
    "r-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Competing risks model", "Analyzes time-to-event data where multiple distinct types of events could occur, each precluding the others"],
        ["Survival analysis application", "Standard survival methods can give biased estimates when competing risks are present but ignored"],
    ])},
    "r-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Time-varying covariate", "A predictor variable whose value changes over the course of the observation period rather than staying fixed"],
        ["Cox model extension", "Extends the standard Cox proportional hazards model to properly incorporate covariates that change over time"],
    ])},
    "r-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Joint modeling", "Simultaneously models a longitudinal outcome (repeated measurements) and a time-to-event outcome, capturing their association"],
        ["Application", "More statistically efficient than analyzing the longitudinal and survival data as two separate, unconnected models"],
    ])},
    "r-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Spatial statistics", "Analyzes data with an inherent geographic or spatial structure, accounting for spatial autocorrelation"],
        ["spatstat and sf", "R packages for point pattern analysis (spatstat) and modern spatial vector data handling (sf)"],
    ])},
    "r-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Spatiotemporal modeling", "Jointly models how a phenomenon varies across both space and time"],
        ["Conditional autoregressive prior", "A Bayesian prior structure that models spatial dependence by conditioning each location's value on its neighbors"],
    ])},
    "r-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["State space model", "Represents a time series as a hidden state evolving over time, observed only indirectly through noisy measurements"],
        ["KFAS", "An R package implementing efficient Kalman filtering and smoothing for a broad class of state space models"],
    ])},
    "r-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian structural time series", "Models a time series' components (trend, seasonality) probabilistically for forecasting and causal impact analysis"],
        ["bsts package", "An R package implementing Bayesian structural time series models, notably used for causal impact estimation"],
    ])},
    "r-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Vector autoregression", "Models multiple interdependent time series, where each variable is regressed on past values of itself and the others"],
        ["Structural VAR", "Adds economically motivated identifying restrictions to a VAR to enable causal interpretation of the estimated relationships"],
    ])},
    "r-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Cointegration", "Occurs when two or more non-stationary time series share a stable long-run equilibrium relationship"],
        ["Vector error correction model", "Models both the short-run dynamics and the long-run cointegrating relationship among cointegrated series"],
    ])},
    "r-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Wavelet analysis", "Decomposes a signal into components at different scales and times, unlike Fourier analysis's fixed frequency resolution"],
        ["Nonstationary time series", "Well suited to time series whose frequency characteristics change over time, which Fourier methods handle poorly"],
    ])},
    "r-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Extreme value theory", "Studies the statistical behavior of the most extreme values in a distribution's tail"],
        ["extRemes package", "An R package implementing extreme value theory methods for modeling rare, high-impact events"],
    ])},
    "r-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Copula", "A function modeling the dependence structure between random variables separately from their individual marginal distributions"],
        ["Multivariate dependence application", "Enables flexibly modeling complex joint dependence, including tail dependence, that simple correlation cannot capture"],
    ])},
    "r-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Instrumental variable", "A variable affecting the outcome only through the treatment, used to identify a causal effect despite confounding"],
        ["R implementation", "R packages provide two-stage least squares and related estimators for instrumental variable causal analysis"],
    ])},
    "r-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Estimates a treatment effect by comparing outcome changes over time between treated and control groups"],
        ["Staggered treatment timing", "Modern R estimators correct for bias that arises in traditional DiD when units are treated at different times"],
    ])},
    "r-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic control method", "Constructs a weighted combination of untreated units that approximates a treated unit's pre-treatment trajectory"],
        ["R implementation", "R packages implement the optimization procedures needed to construct synthetic control weights and inference"],
    ])},
    "r-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Targeted maximum likelihood estimation", "A doubly robust estimation framework combining outcome and treatment models for valid causal effect estimates"],
        ["R implementation", "R packages implement TMLE, remaining consistent if either the outcome or treatment model is correctly specified"],
    ])},
    "r-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Causal mediation analysis", "Decomposes a total causal effect into direct and indirect (mediated) pathways"],
        ["mediation package", "An R package implementing modern causal mediation analysis methods with formal identifying assumptions"],
    ])},
    "r-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Propensity score matching", "Matches treated and untreated units with similar estimated probabilities of receiving treatment to reduce confounding bias"],
        ["Diagnostics", "Balance diagnostics check whether matching successfully equalized covariate distributions between treated and control groups"],
    ])},
    "r-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Double machine learning", "Uses flexible ML models to estimate nuisance functions while achieving valid inference for a causal parameter"],
        ["Causal parameter estimation", "R implementations handle high-dimensional confounders better than classical regression-adjustment approaches"],
    ])},
    "r-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Meta-analysis", "Statistically pools effect estimates across multiple studies to produce a combined, more robust estimate"],
        ["metafor package", "A comprehensive R package for conducting a wide range of meta-analytic models and diagnostics"],
    ])},
    "r-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Network meta-analysis", "Simultaneously compares multiple treatments across studies, even when not every pair was directly compared"],
        ["R implementation", "Combines direct and indirect evidence within a single coherent statistical framework to rank treatments"],
    ])},
    "r-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Computational text analysis", "Applies quantitative methods to analyze large collections of text"],
        ["quanteda", "An R package providing an efficient, comprehensive toolkit for text mining and quantitative text analysis"],
    ])},
    "r-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Structural topic model", "Extends standard topic models to incorporate document-level covariates that can influence topic prevalence and content"],
        ["stm package", "An R package implementing structural topic modeling, letting researchers relate topics to metadata like time or source"],
    ])},
    "r-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Word embedding", "A dense vector representation of a word capturing its meaning based on the contexts it appears in"],
        ["R training and analysis", "R packages support both training custom embeddings and analyzing pre-trained embeddings for downstream text analysis"],
    ])},
    "r-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["tidymodels", "A cohesive collection of R packages for modeling and machine learning following tidyverse design principles"],
        ["ML pipeline", "Provides a unified, consistent interface for preprocessing, model fitting, tuning, and evaluation"],
    ])},
    "r-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Recipe (tidymodels)", "A specification of preprocessing steps to apply to data before model fitting, within the tidymodels framework"],
        ["Custom recipe step", "Developers can define new feature engineering steps that integrate seamlessly with the tidymodels preprocessing pipeline"],
    ])},
    "r-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Ensemble stacking", "Combines predictions from multiple base models using a meta-model trained on their outputs"],
        ["stacks package", "An R package implementing model stacking within the tidymodels ecosystem"],
    ])},
    "r-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Gradient boosting", "An ensemble method that sequentially fits models to correct the residual errors of the current ensemble"],
        ["xgboost and lightgbm", "High-performance gradient boosting implementations available as R packages, differing in tree-growth strategy and speed"],
    ])},
    "r-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian Additive Regression Trees", "A Bayesian nonparametric ensemble of regression trees that provides built-in uncertainty quantification"],
        ["R application", "Combines the flexibility of tree ensembles with principled Bayesian uncertainty estimates for predictions"],
    ])},
    "r-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Random forest variable importance", "Quantifies how much each predictor contributes to a random forest's predictive performance"],
        ["Interaction detection", "Specialized methods can identify pairs of variables whose combined effect exceeds what their individual importances suggest"],
    ])},
    "r-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["torch for R", "An R interface to the PyTorch deep learning library, enabling native R deep learning workflows"],
        ["Deep learning in R", "Lets R users build and train neural networks without needing to switch to Python"],
    ])},
    "r-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["SHAP value", "A game-theoretic method that fairly attributes a model prediction's outcome to each input feature's contribution"],
        ["R implementation", "R packages compute SHAP values to explain individual predictions from complex, black-box machine learning models"],
    ])},
    "r-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Cross-validation for dependent data", "Standard random cross-validation is invalid when observations are correlated, such as in time series or clustered data"],
        ["Advanced scheme", "Methods like blocked or grouped cross-validation respect the dependency structure to avoid overly optimistic performance estimates"],
    ])},
    "r-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Conformal prediction", "Produces prediction sets guaranteed to contain the true outcome at a specified confidence level, without distributional assumptions"],
        ["R uncertainty quantification", "R packages implement conformal methods providing distribution-free coverage guarantees for any underlying model"],
    ])},
    "r-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["ggplot2 extension", "Custom geoms, stats, or themes built on top of ggplot2's grammar of graphics framework"],
        ["Custom visualization", "Enables creating specialized, reusable chart types not available in ggplot2's built-in functionality"],
    ])},
    "r-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Shiny", "An R framework for building interactive web applications directly from R code"],
        ["Reactive programming internals", "Shiny's reactivity system automatically re-executes only the parts of an app affected by a changed input"],
    ])},
    "r-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Shiny module", "A self-contained, reusable unit of Shiny UI and server logic with its own namespace"],
        ["Large application design", "Modules prevent naming collisions and improve maintainability as a Shiny application grows in complexity"],
    ])},
    "r-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["S4 class system", "R's more formal object-oriented system with explicit class definitions and multiple dispatch"],
        ["R5 reference class", "R's mutable, reference-semantics object system, closer to conventional object-oriented programming than S4"],
    ])},
    "r-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["R6 class", "A widely used package providing encapsulated, mutable object-oriented programming for R"],
        ["Design pattern (stateful objects)", "R6's reference semantics make it well suited for objects that need to maintain and modify internal state"],
    ])},
    "r-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Rcpp", "An R package that simplifies writing high-performance C++ extensions callable directly from R"],
        ["Performance-critical code", "Lets developers rewrite computational bottlenecks in C++ while keeping the rest of the workflow in R"],
    ])},
    "r-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["RcppArmadillo", "Integrates the Armadillo C++ linear algebra library with Rcpp for high-performance matrix computation"],
        ["Application", "Provides fast, expressive linear algebra operations for computationally intensive statistical routines written in C++"],
    ])},
    "r-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["future framework", "An R package providing a unified, backend-agnostic API for asynchronous and parallel computation"],
        ["furrr", "Combines the future framework with purrr's functional programming style for easy parallel iteration"],
    ])},
    "r-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["renv", "An R package for managing project-specific, reproducible package library snapshots"],
        ["Containerized R environment", "Combining renv with containers (like Docker) ensures both R package versions and the system environment are reproducible"],
    ])},
    "r-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["CRAN-compliant documentation", "Package documentation meeting the Comprehensive R Archive Network's formal submission and quality standards"],
        ["Testing requirement", "CRAN submission requires a well-documented, thoroughly tested package with passing automated checks"],
    ])},
    "r-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["testthat", "The standard R package for writing and running unit tests"],
        ["Advanced testing strategy", "Includes techniques like snapshot testing and testing edge cases specific to statistical code correctness"],
    ])},
    "r-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Continuous integration (R packages)", "Automatically builds, tests, and checks an R package whenever code changes are pushed"],
        ["Pipeline", "Catches regressions and compatibility issues early, before they reach a package's released version"],
    ])},
    "r-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["data.table", "A high-performance R package for fast data manipulation, particularly for very large datasets"],
        ["Internals and performance tuning", "Understanding its internal indexing and memory model helps write especially fast data.table code"],
    ])},
    "r-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Non-equi join", "A table join based on an inequality condition (e.g. date ranges) rather than exact key matching"],
        ["Rolling join", "A join that matches each row to the nearest preceding or following row in another table, useful for time series merging"],
    ])},
    "r-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Tidy evaluation", "dplyr's system for programmatically working with unquoted column names in functions"],
        ["Programming with dplyr", "Enables writing reusable functions that correctly capture and manipulate data-variable expressions"],
    ])},
    "r-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["dbplyr backend", "Translates dplyr's data manipulation syntax into SQL for a specific database system"],
        ["Custom backend", "Writing a custom backend lets dplyr's familiar syntax work against new or unsupported database systems"],
    ])},
    "r-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Multiple imputation", "Creates several plausible complete datasets by imputing missing values, then pools results across them"],
        ["mice package", "A widely used R package implementing multiple imputation by chained equations"],
    ])},
    "r-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Pattern-mixture model", "Models missing data by stratifying analysis according to observed missingness patterns"],
        ["Nonignorable missingness", "Addresses the case where the probability of missingness depends on the unobserved value itself, which standard MI assumes away"],
    ])},
    "r-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Item response theory", "Models the relationship between a person's underlying trait level and their probability of responding correctly to a test item"],
        ["R implementation", "R packages fit various IRT model families for psychometric test analysis"],
    ])},
    "r-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Differential item functioning", "Occurs when a test item behaves differently for different groups even after controlling for overall ability"],
        ["Detection method", "Statistical tests flag items that may be biased or unfairly disadvantage a particular subgroup"],
    ])},
    "r-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive diagnosis model", "A psychometric model that classifies test-takers by which specific skills or knowledge components they have mastered"],
        ["R implementation", "Provides more diagnostically fine-grained information than a single overall ability score from classical IRT"],
    ])},
    "r-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Bioconductor", "An open-source R software repository specifically for genomic and bioinformatics data analysis"],
        ["Genomic data analysis", "Provides standardized data structures and analysis tools for high-throughput biological data"],
    ])},
    "r-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Differential gene expression", "Identifies genes whose expression levels differ significantly between experimental conditions"],
        ["DESeq2", "A widely used Bioconductor package for statistically robust differential expression analysis of RNA-seq count data"],
    ])},
    "r-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Single-cell RNA-seq", "Measures gene expression at the resolution of individual cells rather than bulk tissue averages"],
        ["Seurat", "A widely used R package for analyzing, clustering, and visualizing single-cell RNA sequencing data"],
    ])},
    "r-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Genome-wide association study", "Scans genetic variants across the genome to identify associations with a trait or disease"],
        ["R analysis pipeline", "R packages support the quality control, statistical testing, and visualization stages of GWAS analysis"],
    ])},
    "r-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Phylogenetic comparative method", "Statistical methods that account for shared evolutionary history when comparing traits across species"],
        ["ape and phytools", "R packages providing tools for phylogenetic tree manipulation and comparative analysis"],
    ])},
    "r-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical occupancy model", "Estimates a species' true occupancy probability while accounting for imperfect detection during surveys"],
        ["Ecological modeling application", "Separates the biological occupancy process from the observation process that can miss present species"],
    ])},
    "r-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Species distribution modeling", "Predicts a species' geographic range based on environmental variables at known occurrence locations"],
        ["Maxent", "A widely used maximum-entropy modeling approach for species distribution modeling, integrable with R workflows"],
    ])},
    "r-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Panel data model", "Analyzes data with repeated observations of the same units over time, such as countries or firms"],
        ["plm package", "An R package implementing standard panel data estimators like fixed-effects and random-effects models"],
    ])},
    "r-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Generalized method of moments", "An estimation approach using moment conditions rather than a fully specified likelihood function"],
        ["R implementation", "Well suited to econometric models where the full data-generating distribution is difficult to specify"],
    ])},
    "r-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Quantile regression", "Estimates how predictors affect different points of an outcome's distribution, not just its conditional mean"],
        ["quantreg package", "An R package implementing quantile regression, useful when effects differ across the outcome distribution"],
    ])},
    "r-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Local polynomial smoothing", "Fits a flexible local regression curve without assuming a global functional form"],
        ["Spline smoothing", "Fits piecewise polynomial functions joined smoothly, another flexible nonparametric regression approach"],
    ])},
    "r-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Simulation study", "Uses computer-generated data with known true properties to evaluate a statistical method's performance"],
        ["Design and reporting standard", "Rigorous simulation studies follow structured protocols for parameter choices, replication counts, and result reporting"],
    ])},
    "r-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Power analysis", "Determines the sample size needed to reliably detect an effect of a given size, if it exists"],
        ["Complex multilevel design", "Power calculations for multilevel designs must account for both within-group and between-group sample sizes"],
    ])},
    "r-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Optimal design algorithm", "Computationally selects an experimental design that maximizes statistical efficiency for estimating parameters of interest"],
        ["Advanced experimental design", "Goes beyond standard textbook designs to construct designs tailored to a specific model and constraints"],
    ])},
    "r-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Sequential clinical trial design", "Allows planned interim analyses during a trial, with the option to stop early for efficacy or futility"],
        ["Adaptive design in R", "R packages support simulating and analyzing adaptive trial designs that adjust based on accumulating data"],
    ])},
    "r-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Bridge sampling", "A method for estimating the marginal likelihood needed to compute Bayes factors for Bayesian model comparison"],
        ["WAIC", "The Widely Applicable Information Criterion, an alternative Bayesian model comparison metric estimating out-of-sample predictive accuracy"],
    ])},
    "r-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Prior sensitivity analysis", "Systematically checks how much a Bayesian model's conclusions depend on the specific choice of prior distribution"],
        ["Bayesian workflow application", "A recommended step in responsible Bayesian analysis to ensure conclusions aren't overly driven by an arbitrary prior choice"],
    ])},
    "r-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Simulation-based calibration", "Validates a Bayesian model's implementation by checking that its posterior behaves correctly across many simulated datasets"],
        ["Model validation", "Detects bugs in a model's implementation or sampling procedure that might otherwise go unnoticed"],
    ])},
    "r-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["M-estimator", "A broad class of robust estimators generalizing maximum likelihood estimation to be less sensitive to outliers"],
        ["Breakdown point", "The proportion of contaminated data an estimator can tolerate before producing an arbitrarily wrong result"],
    ])},
    "r-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["High-dimensional regression", "Regression settings where the number of predictors approaches or exceeds the number of observations"],
        ["Penalized method", "Techniques like lasso and elastic net add regularization to make estimation feasible and prevent overfitting in high dimensions"],
    ])},
    "r-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Graphical lasso", "Estimates a sparse network of conditional dependencies among variables using an L1-penalized likelihood"],
        ["Sparse network estimation", "Produces an interpretable network showing only the most significant direct relationships among many variables"],
    ])},
    "r-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Model-based clustering", "Assumes data are generated from a mixture of underlying probability distributions and estimates cluster membership accordingly"],
        ["mclust package", "A widely used R package implementing model-based clustering via Gaussian mixture models"],
    ])},
    "r-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Spectral clustering", "Clusters data using eigenvectors of a similarity graph's Laplacian matrix"],
        ["Community detection", "Applies clustering techniques to identify densely connected communities within network-structured data"],
    ])},
    "r-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["UMAP", "A nonlinear dimensionality reduction technique that preserves both local and some global structure of high-dimensional data"],
        ["t-SNE theory", "An earlier nonlinear technique focused primarily on preserving local neighborhood structure for visualization"],
    ])},
    "r-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Multiple factor analysis", "Extends principal component-style analysis to datasets combining several groups of variables, potentially of mixed types"],
        ["Mixed data type application", "Handles datasets combining both continuous and categorical variables within a unified dimensionality reduction framework"],
    ])},
    "r-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Reinforcement learning simulation", "Models an agent learning to make sequential decisions through simulated trial-and-error interaction"],
        ["R application", "R packages support building and analyzing reinforcement learning simulations for research and applied use"],
    ])},
    "r-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Custom optimization solver", "A purpose-built numerical optimization routine tailored to a specific problem's structure"],
        ["Rcpp and nloptr", "Combining Rcpp's C++ performance with nloptr's optimization algorithms enables building fast custom solvers"],
    ])},
    "r-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Automatic differentiation", "Computes exact derivatives of a function by systematically applying the chain rule through the computation itself"],
        ["TMB", "Template Model Builder, an R package using automatic differentiation for fast, exact-gradient statistical model fitting"],
    ])},
    "r-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Custom likelihood", "A user-written likelihood function for a statistical model not covered by standard built-in estimation routines"],
        ["Maximum likelihood estimation", "Writing a custom likelihood allows fitting bespoke or nonstandard statistical models via numerical optimization"],
    ])},
    "r-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Data provenance", "Tracks the origin and transformation history of data as it moves through an analysis pipeline"],
        ["targets package", "An R package for building reproducible, dependency-aware analysis pipelines that automatically skip up-to-date steps"],
    ])},
    "r-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Small-area estimation", "Produces reliable statistical estimates for geographic areas too small to have adequate direct survey sample sizes"],
        ["Advanced model", "Borrows statistical strength from related areas or auxiliary data to improve estimates for small, sparsely sampled regions"],
    ])},
    "r-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Record linkage", "Identifies records across different datasets that likely refer to the same real-world entity"],
        ["Entity resolution in R", "R packages implement probabilistic and machine-learning-based approaches to matching records without a shared unique identifier"],
    ])},
    "r-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Bootstrap method", "Estimates a statistic's sampling distribution by repeatedly resampling with replacement from the observed data"],
        ["Complex sampling design", "Advanced bootstrap variants correctly account for stratification, clustering, and weighting in complex survey samples"],
    ])},
    "r-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original development of new statistical methodology, implemented in R"],
        ["Original statistical methodology", "Requires identifying a genuine gap in existing statistical methods and rigorously developing and validating a novel approach"],
    ])},
    "r-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Survey weighting", "Adjusts sample data to correctly represent a target population, accounting for unequal selection probabilities"],
        ["Calibration estimation (survey package)", "The R survey package implements calibration methods that adjust weights to match known population totals, improving estimate precision"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["R"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"r-m2-l{base_n}"
        worked_key = f"r-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 R lessons.")


if __name__ == "__main__":
    main()
