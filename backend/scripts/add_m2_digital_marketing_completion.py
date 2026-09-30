#!/usr/bin/env python3
"""Depth pass, M2 Digital Marketing: fill in real, hand-checked
data_table content for the M2 Digital Marketing lessons not covered by
the earlier breadth-first batch. Brings M2 Digital Marketing to full
120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning marketing
mix modeling and attribution econometrics, experimentation and testing
methodology, customer data/identity infrastructure, SEO and search
evolution, personalization and marketing automation, privacy-preserving
advertising, and marketing measurement governance; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_digital_marketing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Marketing mix modeling", "Statistically estimates how different marketing channels contribute to a business outcome like sales"],
    ["Bayesian approach", "Incorporates prior knowledge and quantifies uncertainty in estimated channel contributions, unlike a single point estimate"],
])

CHARTS: dict[str, dict] = {
    "digital-marketing-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Growth hacking", "A rapid, experiment-driven approach to identifying scalable, low-cost strategies for user or revenue growth"],
        ["Experimentation", "Systematically tests growth hypotheses through controlled experiments rather than intuition alone"],
    ])},
    "digital-marketing-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Integrated marketing capstone", "An applied culminating project demonstrating end-to-end marketing strategy and measurement skill"],
        ["Deliverable", "Typically includes channel strategy, measurement plan, and evaluation of a real or simulated marketing program"],
    ])},
    "digital-marketing-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Multi-touch attribution", "Distributes credit for a conversion across multiple marketing touchpoints in a customer's journey"],
        ["Shapley value method", "Fairly distributes conversion credit across channels by averaging their marginal contribution over all possible orderings"],
    ])},
    "digital-marketing-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Media mix optimization", "Determines the allocation of marketing spend across channels that maximizes a target outcome"],
        ["Budget constraint", "Optimization must respect a fixed total spend limit, distributing it to the highest-marginal-return channels"],
    ])},
    "digital-marketing-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Cookieless ecosystem", "A digital advertising environment where third-party tracking cookies are increasingly restricted or unavailable"],
        ["Marketing measurement", "Requires new approaches like aggregated reporting and modeled attribution to replace individual-level tracking"],
    ])},
    "digital-marketing-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Incrementality testing", "Measures the true causal lift a marketing activity provides, beyond what would have happened anyway"],
        ["Geo-experiment", "Randomizes advertising treatment at the level of geographic regions to estimate incremental impact"],
    ])},
    "digital-marketing-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value", "The total predicted net value a business will generate from a customer over their entire relationship"],
        ["Probabilistic approach", "Models purchase and churn behavior as probability distributions rather than a single deterministic value"],
    ])},
    "digital-marketing-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Churn prediction", "Estimates the likelihood that a customer will stop engaging with a business"],
        ["Retention marketing", "Uses churn predictions to target at-risk customers with proactive retention interventions"],
    ])},
    "digital-marketing-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Customer data platform", "Unifies customer data from multiple sources into a single, persistent customer profile"],
        ["Identity resolution", "Matches and merges records referring to the same customer across different systems and devices"],
    ])},
    "digital-marketing-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Programmatic advertising", "Automated buying and selling of digital ad inventory through real-time software-driven auctions"],
        ["Real-time bidding", "Ad impressions are auctioned to bidders within milliseconds as a webpage loads"],
    ])},
    "digital-marketing-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Ad fraud", "Deceptive activity that generates fake ad impressions, clicks, or conversions to extract advertiser spend"],
        ["Programmatic detection", "Statistical and behavioral analysis identifies traffic patterns inconsistent with genuine human engagement"],
    ])},
    "digital-marketing-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Adstock", "Models the carryover (lagged) effect of past advertising spend on current outcomes"],
        ["Saturation curve", "Models diminishing marginal returns as spend on a channel increases beyond a certain point"],
    ])},
    "digital-marketing-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Search engine ranking algorithm", "The set of signals and models a search engine uses to order results for a query"],
        ["Algorithm evolution", "Ranking signals have shifted over time from simple keyword matching toward relevance, quality, and user-experience signals"],
    ])},
    "digital-marketing-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Technical SEO", "Optimizes a website's underlying infrastructure and code to improve search engine crawling, indexing, and ranking"],
        ["Core Web Vitals", "A standardized set of page-experience metrics that search engines factor into ranking decisions"],
    ])},
    "digital-marketing-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Structured data markup", "Machine-readable annotations added to webpage content to help search engines understand its meaning"],
        ["Knowledge graph optimization", "Structured markup can help a site's information be surfaced directly in a search engine's knowledge panel"],
    ])},
    "digital-marketing-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Hreflang", "An HTML attribute signaling to search engines which language and region a page variant targets"],
        ["Multi-regional SEO", "Ensures the correct language or country version of a page is shown to users in different regions"],
    ])},
    "digital-marketing-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Voice search optimization", "Adapts content to match the more conversational, question-based phrasing typical of voice queries"],
        ["Strategy", "Prioritizes concise, direct answers likely to be read aloud by a voice assistant"],
    ])},
    "digital-marketing-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Generative AI search optimization", "Adapts content strategy for search experiences that synthesize AI-generated answers rather than only listing links"],
        ["Emerging strategy", "Emphasizes being cited as a trustworthy source within AI-generated summaries, not just ranking highly in traditional results"],
    ])},
    "digital-marketing-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Conversion rate optimization", "Systematically improves the percentage of visitors who complete a desired action"],
        ["Statistical test design", "Requires proper sample size and significance thresholds to draw reliable conclusions from CRO experiments"],
    ])},
    "digital-marketing-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Multivariate testing", "Tests multiple page element variations simultaneously to identify the best-performing combination"],
        ["Digital experience methodology", "Requires larger sample sizes than simple A/B tests since it must evaluate many combinations at once"],
    ])},
    "digital-marketing-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Sequential testing", "Allows continuous monitoring of an experiment's results without inflating the false-positive rate"],
        ["Peeking problem", "Repeatedly checking a fixed-horizon test's results early and stopping based on them inflates the true false-positive rate"],
    ])},
    "digital-marketing-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian A/B testing", "Frames experiment analysis in terms of the probability one variant is better, rather than a binary significance threshold"],
        ["Marketing framework", "Offers more intuitive interpretation of results and natural support for continuous monitoring compared with frequentist testing"],
    ])},
    "digital-marketing-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Personalization engine", "Tailors content or offers to individual users based on their behavior and characteristics"],
        ["Recommendation algorithm design", "Balances relevance, diversity, and business objectives when selecting personalized content"],
    ])},
    "digital-marketing-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic creative optimization", "Automatically generates and tests many ad creative variations, serving the best-performing combination"],
        ["Scale application", "Enables personalized ad creative at a volume impossible for manual production"],
    ])},
    "digital-marketing-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Marketing automation", "Software that executes predefined marketing workflows triggered by customer behavior or attributes"],
        ["Workflow architecture", "Well-designed workflows branch based on customer actions, delivering timely, relevant communications automatically"],
    ])},
    "digital-marketing-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Lead scoring", "Assigns a numeric score to a prospect reflecting their likelihood to convert into a customer"],
        ["Predictive and behavioral approach", "Combines explicit attributes with observed engagement behavior to rank lead quality"],
    ])},
    "digital-marketing-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Account-based marketing", "Targets marketing efforts at specific high-value accounts rather than broad audience segments"],
        ["Strategic framework", "Aligns sales and marketing around a shared list of target accounts with coordinated, personalized outreach"],
    ])},
    "digital-marketing-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["B2B marketing funnel", "Models the stages a business buyer passes through from awareness to purchase"],
        ["Pipeline attribution", "Connects marketing touchpoints to eventual sales pipeline outcomes, often over long, multi-stakeholder sales cycles"],
    ])},
    "digital-marketing-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Attribution modeling", "Assigns credit for a conversion across the touchpoints that contributed to it"],
        ["Long sales cycle", "Extended B2B purchase timelines complicate attribution since many touchpoints occur far apart in time"],
    ])},
    "digital-marketing-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Influencer marketing", "Partners with individuals with an engaged audience to promote a brand or product"],
        ["ROI measurement", "Requires isolating the incremental impact of influencer activity from other concurrent marketing efforts"],
    ])},
    "digital-marketing-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Social media algorithm", "The ranking logic a platform uses to determine what content appears in a user's feed"],
        ["Platform-specific signal", "Each platform weighs different signals (engagement, recency, relationships) differently in its ranking"],
    ])},
    "digital-marketing-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Community-led growth", "Drives business growth by cultivating an engaged user or customer community"],
        ["Strategy", "Relies on organic advocacy and peer influence within the community rather than purely paid acquisition"],
    ])},
    "digital-marketing-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["User-generated content", "Content created by customers or community members rather than the brand itself"],
        ["Strategy and measurement", "Tracks how UGC influences engagement and conversion compared with brand-produced content"],
    ])},
    "digital-marketing-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Brand equity", "The value a brand adds to a product beyond its functional attributes, based on consumer perception"],
        ["Econometric model", "Statistically estimates how brand perception metrics translate into measurable business outcomes like price premium"],
    ])},
    "digital-marketing-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling", "Estimates aggregate channel contribution to outcomes using top-down statistical modeling of historical data"],
        ["Multi-touch attribution reconciliation", "MMM and MTA often disagree; reconciling them combines top-down and bottom-up measurement perspectives"],
    ])},
    "digital-marketing-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Price elasticity", "Measures how much quantity demanded changes in response to a change in price"],
        ["Digital promotion estimation", "Estimates how responsive demand is to discounts and promotional pricing in digital channels"],
    ])},
    "digital-marketing-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic pricing algorithm", "Automatically adjusts prices in response to demand, competition, and inventory signals"],
        ["E-commerce application", "Balances maximizing revenue against maintaining customer trust and perceived price fairness"],
    ])},
    "digital-marketing-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Subscription business metric", "Key performance indicators specific to recurring-revenue businesses, such as MRR and churn rate"],
        ["Cohort retention analysis", "Tracks what fraction of a subscriber cohort remains active over successive periods after signup"],
    ])},
    "digital-marketing-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Net Promoter Score", "A single-question survey metric measuring customer likelihood to recommend a brand"],
        ["Statistical critique", "NPS's simplicity has been criticized for discarding information and having weaker predictive validity than claimed"],
    ])},
    "digital-marketing-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Customer journey map", "A visual representation of the steps a customer takes when interacting with a brand"],
        ["Data-driven reconstruction", "Builds the journey map from actual observed behavioral data rather than assumed or idealized paths"],
    ])},
    "digital-marketing-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Marketing data warehouse", "A centralized repository consolidating marketing data from multiple sources for analysis"],
        ["Modern data stack", "A composable set of tools (ingestion, warehouse, transformation, BI) increasingly used to build marketing analytics infrastructure"],
    ])},
    "digital-marketing-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Server-side tagging", "Moves tag and tracking logic from the browser to a server, improving reliability and control over data collection"],
        ["First-party data collection", "Server-side approaches strengthen first-party data collection as browsers restrict third-party tracking"],
    ])},
    "digital-marketing-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Consent management platform", "Manages and records user consent choices for data collection and processing"],
        ["Regulatory compliance", "Must reliably propagate consent decisions to every downstream marketing and analytics system"],
    ])},
    "digital-marketing-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-preserving advertising", "Advertising technology designed to minimize exposure of individually identifiable user data"],
        ["Technology approach", "Includes techniques like on-device processing and aggregated, differentially private reporting"],
    ])},
    "digital-marketing-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Contextual targeting", "Places ads based on the content of the page being viewed rather than the individual user's identity"],
        ["NLP application", "Natural language processing analyzes page content to determine relevant contextual ad categories"],
    ])},
    "digital-marketing-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Retail media network", "An advertising platform operated by a retailer, monetizing its own first-party shopper data and traffic"],
        ["Platform economics", "Retailers capture ad revenue while advertisers gain access to high-intent purchase-context audiences"],
    ])},
    "digital-marketing-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Marketplace advertising", "Sponsored placements within an e-commerce marketplace's own search and browse results"],
        ["Optimization strategy", "Balances bid levels against product margin and conversion likelihood within the marketplace's auction system"],
    ])},
    "digital-marketing-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Affiliate marketing", "Pays partners a commission for driving referred sales or leads to a business"],
        ["Network fraud detection", "Identifies fraudulent affiliate activity like fake clicks or cookie stuffing designed to claim undeserved commissions"],
    ])},
    "digital-marketing-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Email deliverability", "The likelihood that a sent email successfully reaches the recipient's inbox rather than spam"],
        ["Sender reputation", "Authentication protocols like SPF, DKIM, and DMARC help establish trust and improve deliverability"],
    ])},
    "digital-marketing-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Send-time optimization", "Algorithmically determines the best time to send an email to each individual recipient"],
        ["Algorithm", "Learns from each recipient's historical engagement patterns to predict their most responsive send window"],
    ])},
    "digital-marketing-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Multicollinearity", "Occurs when marketing channels are highly correlated with each other, making their individual effects hard to separate"],
        ["Marketing mix modeling handling", "Requires regularization or additional data sources to reliably disentangle correlated channel effects"],
    ])},
    "digital-marketing-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Conjoint analysis", "Presents respondents with product profiles combining different feature or message levels to infer relative preferences"],
        ["Product and message positioning", "Reveals which product features or marketing messages customers value most highly"],
    ])},
    "digital-marketing-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Media cannibalization", "Occurs when one marketing channel's activity reduces the effectiveness or measured contribution of another"],
        ["Analysis", "Identifies whether increased spend in one channel is actually generating incremental sales or displacing another channel's credit"],
    ])},
    "digital-marketing-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Halo effect", "One marketing channel's activity boosts performance attributed to a different channel"],
        ["Multi-channel measurement", "Complicates isolating each channel's true incremental contribution when cross-channel halo effects are present"],
    ])},
    "digital-marketing-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Quality Score", "A search engine's estimate of an ad's relevance and expected performance, affecting its cost and placement"],
        ["Optimization theory", "Improving relevance signals can lower cost-per-click while improving ad rank simultaneously"],
    ])},
    "digital-marketing-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Marketing experimentation platform", "Internal infrastructure that enables teams to design, run, and analyze marketing experiments systematically"],
        ["Infrastructure design", "Provides standardized experiment design, randomization, and statistical analysis tools across the organization"],
    ])},
    "digital-marketing-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Customer segmentation", "Divides a customer base into groups sharing similar characteristics or behaviors"],
        ["Unsupervised clustering", "Algorithmically discovers natural customer groupings from data without predefined segment labels"],
    ])},
    "digital-marketing-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Predictive lifetime value segmentation", "Groups customers by their forecasted future value rather than only past behavior"],
        ["Strategy", "Enables prioritizing marketing investment toward segments predicted to be most valuable long-term"],
    ])},
    "digital-marketing-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Omnichannel retail", "Integrates marketing and sales across online and offline channels into a unified customer experience"],
        ["Marketing mix modeling application", "Must account for interactions between online advertising and offline in-store sales outcomes"],
    ])},
    "digital-marketing-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Geofencing", "Targets marketing to users based on their physical location within a defined geographic boundary"],
        ["Foot traffic attribution", "Measures whether location-targeted advertising resulted in increased visits to a physical store"],
    ])},
    "digital-marketing-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Marketing technology stack", "The collection of software tools an organization uses to plan, execute, and measure marketing"],
        ["Integration architecture", "Ensures data flows consistently between disparate tools rather than remaining siloed"],
    ])},
    "digital-marketing-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Composable customer experience", "Assembles a customer experience platform from modular, independently replaceable best-of-breed components"],
        ["Platform design", "Offers more flexibility than a single monolithic platform, at the cost of greater integration complexity"],
    ])},
    "digital-marketing-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Predictive churn intervention", "Uses churn risk predictions to trigger proactive retention actions before a customer actually leaves"],
        ["Strategy design", "Must balance intervention cost against the predicted value of retaining each at-risk customer"],
    ])},
    "digital-marketing-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling validation", "Assesses whether an MMM's estimated channel effects are reliable and generalize beyond the fitted data"],
        ["Holdout and backtesting", "Reserves data or uses historical periods not used in fitting to test the model's out-of-sample predictive accuracy"],
    ])},
    "digital-marketing-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Digital shelf analytics", "Monitors how a brand's products appear and perform across online retail search and browse results"],
        ["E-commerce marketing application", "Tracks metrics like search rank, content compliance, and share of voice on retail platforms"],
    ])},
    "digital-marketing-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Video completion rate", "The percentage of viewers who watch a video ad through to its end"],
        ["Creative optimization", "Analyzes drop-off points within the video to identify which creative elements retain or lose viewer attention"],
    ])},
    "digital-marketing-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Cross-device identity graph", "Links a single user's activity across multiple devices into one unified profile"],
        ["Construction and accuracy", "Probabilistic and deterministic matching methods trade off coverage against confidence in the identity linkage"],
    ])},
    "digital-marketing-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Causal impact of brand advertising", "Estimates whether brand advertising causally increases downstream search demand, not just correlates with it"],
        ["Search demand analysis", "Uses time-series causal inference methods to isolate advertising's effect from other demand drivers"],
    ])},
    "digital-marketing-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Loyalty program economics", "Analyzes the cost and revenue impact of a customer loyalty program"],
        ["Points valuation model", "Estimates the true liability and redemption cost represented by outstanding loyalty points"],
    ])},
    "digital-marketing-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Gamification", "Applies game-design elements (points, badges, progress) to non-game contexts to drive engagement"],
        ["Customer engagement design", "Uses gamification mechanics to encourage desired customer behaviors over time"],
    ])},
    "digital-marketing-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics", "Studies systematic deviations from rational choice that affect consumer decisions"],
        ["Marketing messaging application", "Applies principles like anchoring and loss aversion to craft more persuasive marketing messages"],
    ])},
    "digital-marketing-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Neuromarketing", "Studies consumer responses to marketing stimuli using physiological and neurological measurement"],
        ["Physiological measurement", "Includes techniques like eye-tracking and galvanic skin response to capture responses beyond self-report"],
    ])},
    "digital-marketing-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Long-term brand effects", "The cumulative, slow-building impact of brand advertising that extends beyond immediate short-term sales response"],
        ["Marketing mix modeling estimation", "Requires longer time horizons and specialized model structures to detect effects that unfold gradually"],
    ])},
    "digital-marketing-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["International digital marketing", "Adapts marketing strategy and execution for different countries and markets"],
        ["Localization strategy framework", "Structures the balance between global brand consistency and local market relevance"],
    ])},
    "digital-marketing-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cultural consumer behavior", "Studies how cultural context shapes how consumers respond to marketing across different regions"],
        ["Global campaign application", "Global campaigns must account for cultural differences in values, humor, and persuasion norms"],
    ])},
    "digital-marketing-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Marketing data governance", "Establishes standards and processes to ensure marketing data is accurate, consistent, and properly used"],
        ["Metric standardization", "Ensures teams across an organization compute the same metric name the same way, preventing reporting discrepancies"],
    ])},
    "digital-marketing-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Attribution modeling (app-based)", "Assigns credit for app installs and in-app conversions to the marketing touchpoints that drove them"],
        ["App-based business challenge", "Complicated by mobile privacy restrictions limiting individual-level tracking across apps"],
    ])},
    "digital-marketing-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Mobile measurement partner", "A third-party service that provides attribution and analytics for mobile app marketing"],
        ["SKAdNetwork", "Apple's privacy-preserving framework for aggregated, non-individualized app install attribution"],
    ])},
    "digital-marketing-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling software", "Tools and platforms used to build, run, and maintain marketing mix models"],
        ["Architecture and tooling", "Modern MMM increasingly uses open-source Bayesian frameworks rather than proprietary black-box tools"],
    ])},
    "digital-marketing-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Customer advocacy program", "Formal initiatives that encourage satisfied customers to actively promote a brand"],
        ["Referral loop design", "Structures incentives so successful referrals generate new customers who themselves become referrers"],
    ])},
    "digital-marketing-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Content marketing ROI", "Measures the business value generated by content marketing relative to its production and distribution cost"],
        ["Attribution to business outcomes", "Requires connecting content engagement to downstream conversion and revenue, not just traffic metrics"],
    ])},
    "digital-marketing-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Topic cluster", "A content strategy organizing related articles around a central pillar page covering a broad topic comprehensively"],
        ["SEO architecture", "Internal linking between pillar and cluster content signals topical authority to search engines"],
    ])},
    "digital-marketing-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Link building", "Acquiring links from other websites pointing to one's own site to improve search authority"],
        ["Authority and relevance signals", "Search engines weigh both the linking site's authority and its topical relevance to the linked content"],
    ])},
    "digital-marketing-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Subscription and SaaS marketing mix modeling", "Adapts MMM techniques to recurring-revenue business dynamics rather than one-time transactional sales"],
        ["Application", "Must account for lagged conversion to paid subscription and ongoing retention effects, not just immediate purchase"],
    ])},
    "digital-marketing-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Data clean room", "A secure environment where multiple parties can jointly analyze combined data without directly sharing raw underlying data"],
        ["Cross-platform measurement", "Enables measuring cross-platform campaign performance while preserving each party's data privacy"],
    ])},
    "digital-marketing-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Sparse spend data", "Marketing spend data with many zero or missing values, common for smaller or intermittently used channels"],
        ["Marketing mix modeling handling", "Requires specialized statistical techniques to avoid unstable estimates for channels with irregular spend patterns"],
    ])},
    "digital-marketing-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Customer equity", "The total combined lifetime value of all of a company's current and future customers"],
        ["Strategic marketing investment", "Uses customer equity estimates to guide long-term resource allocation across acquisition and retention"],
    ])},
    "digital-marketing-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Brand safety", "Ensures ads don't appear alongside harmful, offensive, or inappropriate content"],
        ["Brand suitability", "A more nuanced standard than brand safety, matching ad placement to a brand's specific tone and values"],
    ])},
    "digital-marketing-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Competitive spend response", "Analyzes how a competitor's marketing spend affects one's own brand's sales and market share"],
        ["Marketing mix modeling application", "Incorporates competitor spend data as an input to more accurately estimate one's own channel effects"],
    ])},
    "digital-marketing-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Customer acquisition cost forecasting", "Predicts how much it will cost to acquire new customers under future market conditions"],
        ["Predictive analytics", "Uses historical acquisition trends and market signals to forecast future acquisition efficiency"],
    ])},
    "digital-marketing-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Cross-media synergy", "The combined effect of multiple channels running together can exceed the sum of their individual effects"],
        ["Marketing mix modeling application", "Requires interaction terms in the model to capture synergistic rather than purely additive channel effects"],
    ])},
    "digital-marketing-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Zero-party data", "Data a customer intentionally and proactively shares with a brand, such as preferences stated in a survey"],
        ["Collection design", "Offers a privacy-friendly alternative to inferred or third-party data, requiring explicit customer incentive to share"],
    ])},
    "digital-marketing-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Marketing analytics center of excellence", "A centralized team providing analytics standards, tooling, and expertise across an organization's marketing function"],
        ["Organizational design", "Balances centralized consistency against the responsiveness of embedding analytics directly within individual marketing teams"],
    ])},
    "digital-marketing-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Customer data ethics", "Considers the moral implications of collecting and using customer data for marketing"],
        ["Algorithmic targeting and vulnerability", "Raises concerns about targeting vulnerable populations with predatory or exploitative marketing based on inferred characteristics"],
    ])},
    "digital-marketing-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian hierarchical model", "Pools information across related groups (e.g. markets) while allowing each group its own parameters"],
        ["Multi-market brand application", "Improves marketing mix modeling precision for individual markets by borrowing statistical strength across markets"],
    ])},
    "digital-marketing-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Post-purchase marketing", "Marketing activities directed at customers after they've already made a purchase"],
        ["Cognitive dissonance reduction", "Reassures customers their purchase decision was sound, reducing buyer's remorse and returns"],
    ])},
    "digital-marketing-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Customer win-back campaign", "Marketing efforts specifically targeted at re-engaging previously lapsed or churned customers"],
        ["Design and measurement", "Requires distinguishing win-back success from customers who would have returned organically anyway"],
    ])},
    "digital-marketing-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling governance", "Establishes processes for maintaining and updating MMM models over time"],
        ["Model refresh cadence", "Determines how frequently a model should be retrained to reflect changing market conditions without becoming unstable"],
    ])},
    "digital-marketing-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to marketing science"],
        ["Original contribution", "Requires identifying a genuine gap in existing marketing measurement methods and offering a novel, rigorously evaluated resolution"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Digital Marketing"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"digital-marketing-m2-l{base_n}"
        worked_key = f"digital-marketing-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Digital Marketing lessons.")


if __name__ == "__main__":
    main()
