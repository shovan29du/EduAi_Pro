#!/usr/bin/env python3
"""Depth pass, M2 Business Analytics: fill in real, hand-checked
data_table content for the M2 Business Analytics lessons not covered
by the earlier breadth-first batch. Brings M2 Business Analytics to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning causal
marketing/business inference, customer analytics (CLV, churn,
attribution), experimentation infrastructure, supply chain and
operations analytics, risk and fraud analytics, and enterprise data
architecture/governance; l101-l120 are "Worked Analysis" companions
reusing the data_table of l1-l20 (direct 1:1 mapping). l3 was already
completed by an earlier breadth-first batch, so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_business_analytics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Difference-in-differences", "Estimates a treatment effect by comparing outcome changes over time between treated and control groups"],
    ["Causal inference", "Estimates the effect of a business action on an outcome, distinct from merely predicting the outcome"],
])

CHARTS: dict[str, dict] = {
    "business-analytics-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Analytics ethics", "Considers the fairness, transparency, and societal impact of data-driven business decisions"],
        ["Analytics governance", "Formal policies and review processes ensuring analytics models are used responsibly and consistently"],
    ])},
    "business-analytics-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Business analytics capstone", "An applied culminating project demonstrating end-to-end analytics skill on a real business problem"],
        ["Deliverable", "Typically includes problem framing, data preparation, modeling, evaluation, and clear stakeholder communication"],
    ])},
    "business-analytics-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic control method", "Constructs a weighted combination of untreated markets that approximates a treated market's pre-intervention trend"],
        ["Market intervention evaluation", "Well suited when only one or a few markets receive an intervention, such as a regional campaign"],
    ])},
    "business-analytics-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Regression discontinuity design", "Estimates a causal effect by comparing outcomes just above and below a threshold"],
        ["Marketing threshold effect", "Applies RDD to marketing rules with a hard cutoff, such as a discount triggered above a spending threshold"],
    ])},
    "business-analytics-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Instrumental variable", "A variable affecting the outcome only through the treatment, used to identify a causal effect despite confounding"],
        ["Endogenous pricing", "Prices are often set based on factors that also affect demand, requiring IV methods to isolate the causal price effect"],
    ])},
    "business-analytics-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian structural time series", "Models a time series' components (trend, seasonality) probabilistically to estimate a counterfactual baseline"],
        ["Marketing mix modeling", "Estimates how much each marketing channel contributes to overall sales or conversions"],
    ])},
    "business-analytics-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Multi-touch attribution", "Distributes credit for a conversion across multiple marketing touchpoints in a customer's journey"],
        ["Shapley value allocation", "Fairly distributes conversion credit across channels by averaging their marginal contribution over all possible orderings"],
    ])},
    "business-analytics-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Uplift modeling", "Predicts the incremental effect of a marketing action on an individual customer, not just their outcome probability"],
        ["Individual-level treatment effect", "Identifies which customers will respond most positively to an intervention, focusing resources effectively"],
    ])},
    "business-analytics-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value", "The total predicted net value a business will generate from a customer over their entire relationship"],
        ["Hierarchical Bayesian method", "Pools information across customer segments to produce more stable CLV estimates for individuals with sparse history"],
    ])},
    "business-analytics-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Survival analysis", "Models the time until an event of interest occurs, handling censored observations where the event hasn't yet happened"],
        ["Churn prediction", "Applies survival methods to estimate when a customer is likely to stop being a customer"],
    ])},
    "business-analytics-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Markov chain attribution", "Models a customer's journey as a sequence of states and estimates each channel's contribution by simulating its removal"],
        ["Multichannel conversion path", "The full sequence of marketing touchpoints a customer encounters before converting"],
    ])},
    "business-analytics-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Propensity score matching", "Matches treated and untreated units with similar estimated probabilities of receiving treatment to reduce confounding bias"],
        ["Observational business experiment", "Used when a randomized experiment is infeasible, approximating a controlled comparison from observational data"],
    ])},
    "business-analytics-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Sequential A/B testing", "Allows continuous monitoring of an experiment's results without inflating the false-positive rate"],
        ["Always-valid confidence sequence", "A statistical technique enabling valid inference at any point in time, not just at a pre-specified sample size"],
    ])},
    "business-analytics-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Multi-armed bandit", "Balances exploring uncertain options against exploiting known good ones to maximize cumulative reward"],
        ["Dynamic pricing optimization", "Continuously adjusts prices based on accumulating evidence about demand response, rather than a fixed test allocation"],
    ])},
    "business-analytics-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Contextual bandit", "Extends the bandit framework by choosing actions based on observed context features for each decision"],
        ["Personalized recommendation ranking", "Enables tailoring which items are shown to each individual user's specific context"],
    ])},
    "business-analytics-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Network effect", "A product becomes more valuable to each user as more users join the platform"],
        ["Two-sided marketplace analytics", "Must measure how growth on one side (e.g. sellers) affects value and growth on the other side (e.g. buyers)"],
    ])},
    "business-analytics-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Cohort-based retention curve", "Tracks what fraction of a group of users acquired at the same time remain active over subsequent periods"],
        ["Parametric decay model", "Fits a mathematical decay function to the retention curve to forecast long-run retention beyond observed data"],
    ])},
    "business-analytics-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Marketing attribution bias", "Systematic error in estimated channel contribution caused by unmeasured factors driving both exposure and conversion"],
        ["Selection on unobservables", "Occurs when customers exposed to a channel differ systematically from those who aren't, in ways not captured by the data"],
    ])},
    "business-analytics-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical time series", "Forecasts at multiple aggregation levels (e.g. product, category, total) that must sum consistently"],
        ["Reconciliation", "Adjusts forecasts across levels so that disaggregated forecasts sum to the aggregate forecast, improving overall accuracy"],
    ])},
    "business-analytics-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Price elasticity", "Measures how much quantity demanded changes in response to a change in price"],
        ["Scanner panel data", "Point-of-sale transaction data used to estimate real-world price-response relationships"],
    ])},
    "business-analytics-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Conjoint analysis", "Presents respondents with product profiles combining different feature levels to infer their relative preferences"],
        ["Willingness-to-pay estimation", "Derives how much value customers place on specific product features from their conjoint choices"],
    ])},
    "business-analytics-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Discrete choice model", "Models a customer's choice among a finite set of alternatives based on their attributes"],
        ["Random coefficients logit", "Allows preference weights to vary across individuals, capturing heterogeneity that a standard logit model cannot"],
    ])},
    "business-analytics-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain network optimization", "Determines optimal facility locations and flows to minimize cost while meeting demand"],
        ["Demand uncertainty", "Robust or stochastic optimization methods account for the fact that future demand is not known with certainty"],
    ])},
    "business-analytics-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Newsvendor model", "Determines the optimal order quantity for a perishable product balancing overstock and understock costs"],
        ["Correlated demand", "Extends the classical single-item model to account for demand correlations across multiple products"],
    ])},
    "business-analytics-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Real options valuation", "Values managerial flexibility (e.g. the option to expand or abandon a project) using option-pricing techniques"],
        ["Capital investment decision", "Captures the value of waiting for more information, which traditional discounted cash flow analysis ignores"],
    ])},
    "business-analytics-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo simulation", "Uses repeated random sampling to estimate the distribution of possible outcomes for a complex, uncertain system"],
        ["Enterprise risk quantification", "Simulates many scenarios to characterize a firm's overall risk exposure beyond a single point estimate"],
    ])},
    "business-analytics-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Value-at-risk", "The maximum expected loss over a given time horizon at a specified confidence level"],
        ["Expected shortfall", "The average loss in the worst-case scenarios beyond the value-at-risk threshold, capturing tail risk VaR misses"],
    ])},
    "business-analytics-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Copula", "A function that models the dependence structure between random variables separately from their individual marginal distributions"],
        ["Portfolio risk analytics", "Captures how different risk factors move together, especially important during extreme joint events"],
    ])},
    "business-analytics-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Text mining", "Extracts structured signals and patterns from unstructured text data"],
        ["Earnings call sentiment", "Applies text mining to management commentary in earnings calls to extract forward-looking sentiment signals"],
    ])},
    "business-analytics-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Topic modeling", "Discovers latent thematic structure across a collection of documents"],
        ["Customer feedback categorization", "Automatically groups large volumes of customer comments into interpretable themes at scale"],
    ])},
    "business-analytics-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Graph analytics", "Analyzes relationships between entities represented as a network of nodes and edges"],
        ["Fraud ring detection", "Identifies clusters of accounts or transactions whose connection patterns suggest coordinated fraudulent activity"],
    ])},
    "business-analytics-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection", "Identifies data points that deviate substantially from expected transaction behavior"],
        ["High-dimensional financial stream", "Must flag suspicious transactions in real time despite the high dimensionality of transaction features"],
    ])},
    "business-analytics-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI", "Methods that make a model's predictions understandable to human stakeholders"],
        ["Credit risk scoring", "Explanations are often required by regulation so applicants and regulators can understand a lending decision"],
    ])},
    "business-analytics-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Fairness-constrained ML", "Incorporates explicit fairness criteria as constraints during model training, not just post-hoc auditing"],
        ["Lending decision model", "Must balance predictive accuracy against legal and ethical requirements for equitable treatment across groups"],
    ])},
    "business-analytics-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Feature store", "A centralized system for storing, versioning, and serving machine learning features consistently across training and serving"],
        ["Production analytics pipeline", "Prevents training-serving skew by ensuring the same feature logic is used in both contexts"],
    ])},
    "business-analytics-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Model monitoring", "Tracks a deployed model's performance and input characteristics over time"],
        ["Drift detection", "Identifies when the production data distribution diverges enough from training data to warrant retraining"],
    ])},
    "business-analytics-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Ensemble stacking", "Combines predictions from multiple base models using a meta-model trained on their outputs"],
        ["Forecasting competition", "Stacking diverse model types is a common strategy for winning business forecasting competitions"],
    ])},
    "business-analytics-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Gradient boosted tree", "An ensemble method that sequentially fits trees to correct the residual errors of the current ensemble"],
        ["Interpretability", "Feature importance and Shapley-based explanations help translate boosted tree predictions into business-actionable insight"],
    ])},
    "business-analytics-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Optimal transport", "A mathematical framework for measuring the minimal cost of transforming one distribution into another"],
        ["Customer segmentation alignment", "Can align segment definitions across time periods or data sources to keep segmentation comparisons consistent"],
    ])},
    "business-analytics-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Reinforcement learning", "Learns a policy that maximizes cumulative reward through trial-and-error interaction with an environment"],
        ["Inventory replenishment", "Learns ordering policies that adapt to demand patterns better than static reorder-point rules"],
    ])},
    "business-analytics-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Simulation-optimization", "Combines simulation models with optimization search to find good decisions under complex, uncertain dynamics"],
        ["Workforce scheduling", "Applies simulation-optimization to find staffing schedules that balance cost against uncertain demand for labor"],
    ])},
    "business-analytics-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Queueing theory", "Mathematical study of waiting lines, modeling arrival rates, service rates, and resulting wait times"],
        ["Contact center capacity planning", "Uses queueing models to determine staffing levels that keep customer wait times within target service levels"],
    ])},
    "business-analytics-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Robust optimization", "Finds decisions that perform well across a range of possible parameter values, rather than optimizing for one assumed scenario"],
        ["Parameter ambiguity", "Useful when demand or cost parameters are uncertain and a single point-estimate optimization could perform poorly"],
    ])},
    "business-analytics-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Data envelopment analysis", "A nonparametric method that measures the relative efficiency of comparable operating units"],
        ["Multi-branch benchmarking", "Identifies which branches or units are operating on the efficient frontier and which have room for improvement"],
    ])},
    "business-analytics-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Models relationships among observed and latent variables, such as unobserved satisfaction driving observed behaviors"],
        ["Customer satisfaction driver", "Identifies which underlying factors most strongly influence overall customer satisfaction"],
    ])},
    "business-analytics-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Panel data fixed-effects model", "Controls for unobserved, time-invariant characteristics of each unit when estimating relationships over time"],
        ["Firm performance analysis", "Isolates the effect of a variable of interest from confounding firm-specific factors that don't change over time"],
    ])},
    "business-analytics-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Estimates a treatment effect by comparing outcome changes over time between treated and control groups"],
        ["Staggered timing correction", "Modern estimators correct for bias that arises in traditional DiD when units are treated at different times"],
    ])},
    "business-analytics-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Media mix modeling", "Statistically estimates how different advertising channels contribute to a business outcome like sales"],
        ["Adstock and saturation", "Models the carryover (lagged) effect and diminishing returns of advertising spend over time"],
    ])},
    "business-analytics-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Geo-experiment", "Randomizes advertising treatment at the level of geographic regions rather than individual users"],
        ["Incremental lift measurement", "Estimates the true causal contribution of advertising by comparing treated versus control geographic regions"],
    ])},
    "business-analytics-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-constrained attribution", "Estimates marketing effectiveness when individual-level tracking data is limited by privacy regulations"],
        ["Data environment", "Increasingly requires aggregate or differentially private measurement approaches instead of user-level tracking"],
    ])},
    "business-analytics-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Differential privacy", "A mathematical guarantee that a query's output changes negligibly whether or not any single individual's data is included"],
        ["Aggregated business reporting", "Applies formal privacy guarantees when publishing aggregate business metrics derived from customer data"],
    ])},
    "business-analytics-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Federated analytics", "Computes aggregate insights across multiple organizations' data without centralizing the underlying raw data"],
        ["Cross-organization insight", "Enables collaborative analysis while each party retains control over its own sensitive data"],
    ])},
    "business-analytics-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh", "A decentralized data architecture where domain teams own and serve their own data products"],
        ["Decentralized analytics ownership", "Contrasts with a single centralized data team owning all pipelines and metrics"],
    ])},
    "business-analytics-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Metric tree decomposition", "Breaks a top-level business metric down into its constituent driver metrics"],
        ["North star metric diagnostics", "Helps identify which specific driver metric is responsible for a change in the overall north star metric"],
    ])},
    "business-analytics-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Guardrail metric", "A metric monitored during an experiment to ensure the primary goal isn't achieved at the expense of another important outcome"],
        ["Safe experimentation program", "Systematically checking guardrails prevents shipping changes that harm metrics outside the primary hypothesis"],
    ])},
    "business-analytics-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Novelty effect", "A temporary change in user behavior caused merely by a feature being new, not its lasting value"],
        ["Primacy effect", "Users initially resist a change out of habit, potentially underestimating a genuinely better feature's long-run effect"],
    ])},
    "business-analytics-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Network interference", "Occurs when one user's treatment assignment affects outcomes for other, connected users in an experiment"],
        ["Randomized marketplace experiment", "Standard A/B test assumptions can be violated when treated and control users interact, e.g. compete for the same limited supply"],
    ])},
    "business-analytics-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Cluster-randomized experiment", "Randomizes treatment at the level of groups (e.g. markets) rather than individuals to reduce interference"],
        ["Interference mitigation", "Reduces bias from users influencing each other's outcomes across treatment and control conditions"],
    ])},
    "business-analytics-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Switchback experiment", "Alternates the treatment applied to an entire system (e.g. a market) across successive time periods"],
        ["Marketplace pricing test", "Useful for testing pricing or supply-side interventions where individual-level randomization would cause interference"],
    ])},
    "business-analytics-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hierarchical model", "Pools information across related groups (e.g. markets) while allowing each group its own parameters"],
        ["Multi-market experiment pooling", "Improves estimate precision for individual markets by borrowing statistical strength from other markets"],
    ])},
    "business-analytics-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Meta-analysis", "Statistically pools effect estimates across multiple studies or experiments to produce a combined estimate"],
        ["Experimentation program aggregation", "Synthesizes learnings across many individual experiments run over time within an organization"],
    ])},
    "business-analytics-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Power analysis", "Determines the sample size needed to reliably detect an effect of a given size, if it exists"],
        ["Long-horizon retention metric", "Requires larger samples or longer run times since retention effects unfold and are measured over extended periods"],
    ])},
    "business-analytics-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Ratio metric", "A metric expressed as the ratio of two random quantities, such as conversion rate"],
        ["Delta method", "Approximates the variance of a ratio metric using a first-order Taylor expansion, enabling valid statistical tests"],
    ])},
    "business-analytics-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Bootstrap resampling", "Estimates a statistic's sampling distribution by repeatedly resampling with replacement from the observed data"],
        ["Non-normal metric inference", "Avoids relying on normal-distribution assumptions that can be inaccurate for skewed business metrics"],
    ])},
    "business-analytics-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Data quality framework", "A structured set of checks and standards ensuring data used for analytics is accurate and reliable"],
        ["Enterprise analytics trust", "Stakeholders are more likely to act on analytics insights when data quality is systematically verified"],
    ])},
    "business-analytics-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Semantic layer", "A unified layer defining business metrics consistently, so different teams don't compute the same metric differently"],
        ["Consistent metric definition", "Prevents the common problem of two dashboards reporting different numbers for what should be the same metric"],
    ])},
    "business-analytics-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Change data capture", "Detects and streams changes made to a source database in near real time"],
        ["Real-time analytics pipeline", "Enables downstream analytics systems to stay synchronized with operational data as it changes"],
    ])},
    "business-analytics-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Slowly changing dimension", "A data warehouse pattern for tracking how a dimension's attributes change over time"],
        ["Analytical data warehouse", "Correctly handling historical attribute changes is essential for accurate point-in-time analysis"],
    ])},
    "business-analytics-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Star schema", "A simple, denormalized data warehouse design optimized for fast analytical queries"],
        ["Data vault modeling", "A more flexible, auditable warehouse design better suited to frequently changing source systems"],
    ])},
    "business-analytics-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Columnar storage", "Stores each column contiguously rather than each row, improving scan performance for analytical queries"],
        ["Query optimization", "Column compression and vectorized execution give large speedups for typical wide analytical scans"],
    ])},
    "business-analytics-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Data lineage", "Tracks the origin and transformation history of data as it moves through a pipeline"],
        ["Regulatory auditability", "Enables demonstrating to regulators exactly how a reported number was derived from source data"],
    ])},
    "business-analytics-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Statistical process control chart", "A time-ordered chart with control limits used to detect when a process deviates from expected behavior"],
        ["Operational metric monitoring", "Flags unexpected shifts in operational metrics before they become larger problems"],
    ])},
    "business-analytics-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Six Sigma DMAIC", "A structured problem-solving methodology: Define, Measure, Analyze, Improve, Control"],
        ["Process variation reduction", "Systematically identifies and reduces the root causes of unwanted variation in a business process"],
    ])},
    "business-analytics-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Predictive maintenance", "Uses sensor data to predict equipment failures before they occur, enabling proactive maintenance"],
        ["Sensor time series data", "Continuous measurements from equipment sensors that feed into failure-prediction models"],
    ])},
    "business-analytics-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Remaining useful life", "An estimate of how much longer a piece of equipment can operate before failure"],
        ["Survival-based degradation model", "Applies survival analysis techniques to model gradual equipment degradation over time"],
    ])},
    "business-analytics-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Optimal stopping theory", "Determines the best time to take an action to maximize expected reward, given sequentially revealed information"],
        ["Sequential hiring decision", "Applies optimal stopping to decide when to stop interviewing candidates and make an offer"],
    ])},
    "business-analytics-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Game-theoretic pricing model", "Analyzes how competing firms' pricing decisions interact strategically"],
        ["Competitive pricing dynamics", "Models how a firm's optimal price depends on anticipating competitors' responses"],
    ])},
    "business-analytics-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Auction theory", "Studies how different auction formats affect bidding behavior and revenue outcomes"],
        ["Programmatic advertising market", "Real-time ad exchanges use auction mechanisms to allocate ad impressions to bidders"],
    ])},
    "business-analytics-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Mechanism design", "Designs the rules of an interaction so that participants are incentivized to act in a desired way"],
        ["Incentive-compatible allocation", "A well-designed mechanism ensures truthful participation is each participant's best strategy"],
    ])},
    "business-analytics-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics nudge", "A subtle change in how choices are presented that influences behavior without restricting options"],
        ["Digital product design", "Product teams use nudges (like defaults) to guide users toward beneficial choices"],
    ])},
    "business-analytics-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Prospect theory", "Describes how people evaluate potential losses and gains asymmetrically relative to a reference point"],
        ["Pricing perception", "Explains why framing a price as a discount from a reference price affects perceived value more than the price alone"],
    ])},
    "business-analytics-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Social network analysis", "Studies the structure of relationships between individuals to understand influence and information flow"],
        ["Viral growth loop", "A self-reinforcing cycle where existing users bring in new users, driving organic product growth"],
    ])},
    "business-analytics-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Community detection algorithm", "Identifies densely connected clusters of nodes within a larger network"],
        ["Customer segmentation network", "Applies community detection to group customers based on their relational or behavioral connections"],
    ])},
    "business-analytics-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Off-policy estimator", "Estimates how a new recommendation policy would have performed using data collected under a different, older policy"],
        ["Recommender system evaluation", "Avoids the cost and risk of deploying an untested policy live before estimating its likely performance"],
    ])},
    "business-analytics-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Counterfactual learning", "Trains a ranking model using feedback collected under a different policy than the one being learned"],
        ["Logged bandit feedback", "Historical data recording which items were shown and how users responded, used to train improved ranking policies"],
    ])},
    "business-analytics-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Causal discovery", "Algorithmically infers a plausible causal graph structure from observational business process data"],
        ["Root cause analysis", "Uses the inferred causal structure to identify which upstream factor is truly driving an observed business problem"],
    ])},
    "business-analytics-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Double machine learning", "Uses flexible ML models to estimate nuisance functions while achieving valid inference for a causal parameter"],
        ["High-dimensional causal estimation", "Handles settings with many potential confounding variables better than classical regression adjustment"],
    ])},
    "business-analytics-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Heterogeneous treatment effect", "The causal effect of a business action varies across different customer subgroups"],
        ["Causal forest", "A tree-ensemble method that estimates how treatment effects vary as a function of observed customer characteristics"],
    ])},
    "business-analytics-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Targeted maximum likelihood estimation", "A doubly robust estimation framework combining outcome and treatment models for valid causal effect estimates"],
        ["Business causal inference", "Remains consistent if either the outcome model or treatment model is correctly specified"],
    ])},
    "business-analytics-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Mediation analysis", "Decomposes a total causal effect into direct and indirect (mediated) pathways"],
        ["Customer journey decomposition", "Identifies which intermediate touchpoints mediate the effect of an intervention on final customer outcomes"],
    ])},
    "business-analytics-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Real-time streaming analytics", "Processes and analyzes data continuously as it arrives, rather than in periodic batches"],
        ["Operational dashboard", "Provides business stakeholders with up-to-the-minute visibility into key operational metrics"],
    ])},
    "business-analytics-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Lambda architecture", "Combines a batch layer for accuracy with a speed layer for low-latency approximate results, later reconciled"],
        ["Kappa architecture", "Simplifies lambda architecture by processing all data, batch and real-time, through a single stream-processing pipeline"],
    ])},
    "business-analytics-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Explainability requirement", "Regulated industries often mandate that model decisions can be explained to affected individuals and regulators"],
        ["Regulated financial analytics", "Models used for credit or insurance decisions face particular scrutiny for interpretability and fairness"],
    ])},
    "business-analytics-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Adverse action notice", "A legally required explanation given to an applicant when a credit decision is unfavorable"],
        ["Interpretable credit model", "Must support generating specific, accurate reasons for a denial, favoring inherently interpretable models"],
    ])},
    "business-analytics-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Cross-validation for time series", "Standard random cross-validation is invalid for time-dependent data since it can leak future information into training"],
        ["Time-dependent forecasting", "Requires validation schemes that respect temporal order, such as rolling-origin evaluation"],
    ])},
    "business-analytics-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Feature leakage", "Occurs when a training feature contains information that would not actually be available at prediction time"],
        ["Detection", "Careful review of feature timing relative to the prediction point is needed to catch subtle leakage before deployment"],
    ])},
    "business-analytics-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Champion-challenger framework", "Runs a new candidate model (challenger) alongside the current production model (champion) to compare performance safely"],
        ["Production model governance", "Provides a controlled, low-risk process for evaluating and eventually promoting improved models"],
    ])},
    "business-analytics-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Multi-objective optimization", "Finds solutions that balance trade-offs among several competing objectives rather than optimizing just one"],
        ["Balanced scorecard trade-off", "Applies multi-objective methods to balance financial, customer, process, and growth metrics against each other"],
    ])},
    "business-analytics-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis-level capstone", "A culminating project requiring original design and evaluation of an end-to-end analytics system"],
        ["Causal analytics system design", "Integrates causal inference methodology into a deployable, production-grade analytics pipeline"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Analytics"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"business-analytics-m2-l{base_n}"
        worked_key = f"business-analytics-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Business Analytics lessons.")


if __name__ == "__main__":
    main()
