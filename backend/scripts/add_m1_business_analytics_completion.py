#!/usr/bin/env python3
"""Depth pass, M1 Business Analytics: fill in real, hand-checked
data_table content for the 119 M1 Business Analytics lessons not
covered by the earlier breadth-first batch. Brings M1 Business
Analytics to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning causal
inference for business, experimentation, risk/pricing analytics, and
analytics organization/governance; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_business_analytics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Prior", "Belief before new data"],
    ["Posterior", "Updated belief after new data"],
])

CHARTS: dict[str, dict] = {
    "business-analytics-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Risk analytics", "Uses data and statistical models to quantify and manage business risk"],
    ])},
    "business-analytics-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["People analytics", "Applies data analysis to workforce decisions such as hiring and retention"],
    ])},
    "business-analytics-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["SARIMA", "Extends ARIMA to model seasonal patterns in a time series"],
    ])},
    "business-analytics-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Causal inference", "Estimates the effect of a business action from observational, non-experimental data"],
    ])},
    "business-analytics-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Causal impact experimental design", "Structures data collection so an intervention's effect can be isolated"],
    ])},
    "business-analytics-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Tests hypothesized causal relationships among multiple latent and observed variables"],
    ])},
    "business-analytics-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Optimization under uncertainty", "Chooses decisions that perform well across a range of uncertain future outcomes"],
    ])},
    "business-analytics-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic simulation", "Models a system using repeated random sampling to estimate outcomes"],
    ])},
    "business-analytics-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Multivariate statistical analysis", "Analyzes relationships among several variables measured together"],
    ])},
    "business-analytics-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Panel data analysis", "Analyzes data tracking the same entities across multiple time periods"],
    ])},
    "business-analytics-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Survival analysis (business)", "Models the time until an event such as customer churn or default"],
    ])},
    "business-analytics-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["ML pipeline for analytics", "Chains data preparation, modeling, and evaluation into a repeatable workflow"],
    ])},
    "business-analytics-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["MLOps for analytics", "Applies deployment and monitoring discipline to business analytics models"],
    ])},
    "business-analytics-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["M&A analytics strategy", "Uses data analysis to evaluate and integrate mergers and acquisitions"],
    ])},
    "business-analytics-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise risk analytics", "Quantifies risk exposure across an entire organization's operations"],
    ])},
    "business-analytics-m1-l17": {"data_table": table(["Principle", "Detail"], [
        ["Preattentive attributes", "Visual properties like color and position the eye processes without conscious effort"],
    ])},
    "business-analytics-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Analytics leadership", "Drives organizational adoption and change management around data-driven decisions"],
    ])},
    "business-analytics-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Research methods for analytics", "Applies rigorous methodology to frame and answer business analytics questions"],
    ])},
    "business-analytics-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Predictive model deployment", "Moves a validated predictive model into a live business decision process"],
    ])},
    "business-analytics-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Propensity score matching", "Pairs treated and untreated units with similar likelihood of treatment"],
    ])},
    "business-analytics-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Compares the change over time between a treated group and a control group"],
    ])},
    "business-analytics-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Regression discontinuity design", "Estimates a treatment effect by comparing units just above and below an eligibility cutoff"],
    ])},
    "business-analytics-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Instrumental variables", "Uses a variable correlated with treatment but not the outcome to estimate a causal effect"],
    ])},
    "business-analytics-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Synthetic control", "Constructs a weighted composite of comparison units to estimate a counterfactual"],
    ])},
    "business-analytics-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Multi-armed bandit", "Dynamically allocates traffic toward better-performing variants during an experiment"],
    ])},
    "business-analytics-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Always-valid p-values", "Allow an experiment's significance to be checked continuously without inflating error rates"],
    ])},
    "business-analytics-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Uplift modeling", "Predicts the incremental effect of an intervention on an individual, not just their outcome"],
    ])},
    "business-analytics-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value", "Predicts the total value a customer will generate over their relationship with a business"],
    ])},
    "business-analytics-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Churn prediction", "Estimates the probability a customer will stop using a product or service"],
    ])},
    "business-analytics-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Market basket analysis", "Finds items frequently purchased together using association rule mining"],
    ])},
    "business-analytics-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Price elasticity", "Measures how demand changes in response to a change in price"],
    ])},
    "business-analytics-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Conjoint analysis", "Infers how customers value individual product features by analyzing trade-off choices"],
    ])},
    "business-analytics-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic pricing", "Adjusts prices in real time based on demand, inventory, and competitor signals"],
    ])},
    "business-analytics-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Multi-touch attribution", "Assigns credit for a conversion across multiple marketing touchpoints"],
    ])},
    "business-analytics-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling", "Estimates each marketing channel's contribution to overall business outcomes"],
    ])},
    "business-analytics-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Cohort analysis", "Tracks how a group of users who share a starting point behaves over time"],
    ])},
    "business-analytics-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Funnel analysis", "Measures where users drop off across sequential steps toward a conversion"],
    ])},
    "business-analytics-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Network analysis (organizational)", "Maps informal relationships and influence patterns within an organization"],
    ])},
    "business-analytics-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Text analytics (customer feedback)", "Extracts structured themes and sentiment from unstructured customer comments"],
    ])},
    "business-analytics-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Topic modeling", "Discovers latent themes in a collection of customer voice-of-customer text"],
    ])},
    "business-analytics-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Anomaly detection (fraud)", "Flags financial transactions that deviate from expected behavioral patterns"],
    ])},
    "business-analytics-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Credit scoring model", "Predicts a borrower's likelihood of repayment from historical financial data"],
    ])},
    "business-analytics-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Value at Risk", "Estimates the maximum expected loss over a time horizon at a given confidence level"],
    ])},
    "business-analytics-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo simulation (risk)", "Runs many randomized scenarios to estimate the distribution of possible business outcomes"],
    ])},
    "business-analytics-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Decision tree analysis", "Maps sequential choices and uncertain outcomes to evaluate strategic options"],
    ])},
    "business-analytics-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Real options valuation", "Values managerial flexibility to adapt an investment as new information arrives"],
    ])},
    "business-analytics-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain network optimization", "Finds the lowest-cost configuration of facilities and flows across a supply chain"],
    ])},
    "business-analytics-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Inventory optimization", "Balances holding costs against stockout risk under uncertain demand"],
    ])},
    "business-analytics-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Vehicle routing problem", "Finds the most efficient set of delivery routes for a fleet of vehicles"],
    ])},
    "business-analytics-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Workforce scheduling optimization", "Assigns staff to shifts to meet demand while minimizing cost"],
    ])},
    "business-analytics-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Statistical process control", "Uses control charts to monitor and maintain process quality (Six Sigma)"],
    ])},
    "business-analytics-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Design of experiments", "Systematically varies process factors to identify what drives improvement"],
    ])},
    "business-analytics-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Balanced scorecard", "Tracks performance across financial, customer, process, and learning perspectives"],
    ])},
    "business-analytics-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Data-driven OKRs", "Measures objectives and key results using quantitative, auditable metrics"],
    ])},
    "business-analytics-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Predictive maintenance", "Forecasts equipment failure before it happens using sensor and usage data"],
    ])},
    "business-analytics-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Brand sentiment monitoring", "Tracks public sentiment toward a brand across text and social sources"],
    ])},
    "business-analytics-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Customer segmentation", "Groups customers into meaningful clusters based on shared characteristics or behavior"],
    ])},
    "business-analytics-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Recommendation engine", "Suggests products to users based on their behavior and preferences"],
    ])},
    "business-analytics-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Data storytelling", "Presents analytical findings through a clear narrative supported by visualization"],
    ])},
    "business-analytics-m1-l61": {"data_table": table(["Concept", "Distinction"], [
        ["Statistical significance", "Whether an effect is unlikely to be due to chance"],
        ["Business significance", "Whether an effect is large enough to matter for decisions"],
    ])},
    "business-analytics-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Analytics maturity model", "Assesses how advanced an organization's data capabilities are, from basic reporting to AI"],
    ])},
    "business-analytics-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Data-driven culture change", "Manages the organizational shift toward decisions grounded in evidence"],
    ])},
    "business-analytics-m1-l64": {"data_table": table(["Concern", "Detail"], [
        ["Predictive employment analytics ethics", "Risk of embedding historical bias into hiring or promotion decisions"],
    ])},
    "business-analytics-m1-l65": {"data_table": table(["Concern", "Detail"], [
        ["Algorithmic pricing", "Coordinated algorithmic pricing can raise antitrust concerns even without explicit collusion"],
    ])},
    "business-analytics-m1-l66": {"data_table": table(["Method", "Feature"], [
        ["SHAP", "Assigns each feature a contribution value based on cooperative game theory"],
        ["LIME", "Explains a single prediction by fitting a simple local surrogate model"],
    ])},
    "business-analytics-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Model risk management", "Governs the development, validation, and monitoring of models in regulated industries"],
    ])},
    "business-analytics-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Data product management", "Treats analytics outputs and pipelines as products with users and roadmaps"],
    ])},
    "business-analytics-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Self-service analytics governance", "Balances broad data access with controls that keep analysis trustworthy"],
    ])},
    "business-analytics-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Analytics translator", "Bridges technical analytics teams and business stakeholders"],
    ])},
    "business-analytics-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Scenario planning", "Explores multiple plausible futures to stress-test business strategy"],
    ])},
    "business-analytics-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Competitive benchmarking", "Compares an organization's metrics against industry peers"],
    ])},
    "business-analytics-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Web analytics", "Analyzes user sessions and funnels to understand website behavior"],
    ])},
    "business-analytics-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Mobile app analytics", "Tracks retention and engagement metrics specific to mobile app usage"],
    ])},
    "business-analytics-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["A/B test power analysis", "Determines the sample size needed to reliably detect a meaningful effect"],
    ])},
    "business-analytics-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Multivariate testing", "Tests multiple design elements simultaneously to find the best combination"],
    ])},
    "business-analytics-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Heterogeneous treatment effects", "Estimates how an intervention's impact varies across different subgroups"],
    ])},
    "business-analytics-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian A/B testing", "Uses posterior probability of improvement rather than frequentist p-values to decide a test"],
    ])},
    "business-analytics-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Data blending", "Combines data from multiple sources into a unified view for analysis"],
    ])},
    "business-analytics-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Employee attrition risk modeling", "Predicts which employees are most likely to leave"],
    ])},
    "business-analytics-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["ESG analytics", "Measures and reports environmental, social, and governance performance"],
    ])},
    "business-analytics-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Graph-based fraud detection", "Uses network structure to spot suspicious clusters of connected transactions"],
    ])},
    "business-analytics-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Feature adoption analytics", "Measures how quickly and widely users adopt a new product feature"],
    ])},
    "business-analytics-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Data ethics review board", "Reviews analytics projects for fairness, privacy, and appropriate use"],
    ])},
    "business-analytics-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic workforce capacity planning", "Forecasts staffing needs against fluctuating demand"],
    ])},
    "business-analytics-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Customer journey analytics", "Tracks a customer's interactions across touchpoints over an extended period"],
    ])},
    "business-analytics-m1-l87": {"data_table": table(["Principle", "Detail"], [
        ["Cognitive load", "Overly complex visualizations increase the mental effort required to interpret data"],
    ])},
    "business-analytics-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Communicating uncertainty", "Presents confidence intervals and error alongside point estimates to stakeholders"],
    ])},
    "business-analytics-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Root cause analysis", "Systematically traces a business problem back to its underlying cause"],
    ])},
    "business-analytics-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory risk forecasting", "Predicts the likelihood and impact of upcoming regulatory changes"],
    ])},
    "business-analytics-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Data mesh (analytics)", "Decentralizes data ownership to domain teams rather than one central analytics team"],
    ])},
    "business-analytics-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Subscription pricing analytics", "Models pricing strategy specific to recurring-revenue businesses"],
    ])},
    "business-analytics-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics in model design", "Incorporates predictable human biases into analytics model assumptions"],
    ])},
    "business-analytics-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Cross-border data governance", "Manages analytics compliance across differing national data regulations"],
    ])},
    "business-analytics-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Simulation-based optimization", "Combines simulation and optimization to improve complex operational systems"],
    ])},
    "business-analytics-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Complaint root-cause clustering", "Groups similar customer complaints to identify systemic issues"],
    ])},
    "business-analytics-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Pricing fairness auditing", "Checks whether pricing algorithms produce disparate outcomes across customer groups"],
    ])},
    "business-analytics-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Next-best-offer modeling", "Predicts which product or offer is most likely to convert a given customer"],
    ])},
    "business-analytics-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Geospatial site selection", "Uses location data to identify optimal sites for retail expansion"],
    ])},
    "business-analytics-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Algorithmic talent matching", "Matches gig workers to opportunities using predictive analytics"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"business-analytics-m1-l{base_n}"
    worked_key = f"business-analytics-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Business Analytics"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Business Analytics: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Business Analytics lessons (completing 120/120).")


if __name__ == "__main__":
    main()
