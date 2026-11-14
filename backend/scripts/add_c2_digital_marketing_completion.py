#!/usr/bin/env python3
"""Depth pass, C2 Digital Marketing: fill in real, hand-checked
data_table content for the 69 C2 Digital Marketing lessons not covered
by the earlier breadth-first batch. Brings C2 Digital Marketing to full
70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_digital_marketing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "digital-marketing-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Content marketing", "Creating valuable content to attract and retain a target audience"],
        ]),
    },
    "digital-marketing-c2-l2": {
        "data_table": table(["Platform", "Best For"], [
            ["Instagram", "Visual storytelling and brand aesthetics"], ["LinkedIn", "B2B networking and professional content"],
        ]),
    },
    "digital-marketing-c2-l4": {
        "data_table": table(["Element", "Purpose"], [
            ["Brand narrative", "Creates emotional connection beyond product features"],
        ]),
    },
    "digital-marketing-c2-l5": {
        "data_table": table(["Channel", "Feature"], [
            ["Owned media", "Content on channels the brand controls, like its website"], ["Earned media", "Organic mentions and shares from others"],
        ]),
    },
    "digital-marketing-c2-l6": {
        "data_table": table(["Feature", "Use"], [
            ["Instagram Reels", "Short-form video for reach and discovery"], ["Facebook Groups", "Community building around shared interests"],
        ]),
    },
    "digital-marketing-c2-l7": {
        "data_table": table(["Feature", "Use"], [
            ["LinkedIn Sponsored Content", "Native ads promoting posts to a professional audience"],
        ]),
    },
    "digital-marketing-c2-l8": {
        "data_table": table(["Feature", "Detail"], [
            ["TikTok trends", "Short-form video content driven by sounds and challenges"],
        ]),
    },
    "digital-marketing-c2-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Social listening", "Monitoring social platforms for brand mentions and sentiment"],
        ]),
    },
    "digital-marketing-c2-l10": {
        "data_table": table(["Practice", "Reason"], [
            ["Consistent visual branding", "Builds recognition across all social content"],
        ]),
    },
    "digital-marketing-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Backlink", "A link from another website pointing to yours, signaling authority to search engines"],
        ]),
    },
    "digital-marketing-c2-l12": {
        "data_table": table(["Factor", "Detail"], [
            ["Google Business Profile", "A key factor in local search visibility"],
        ]),
    },
    "digital-marketing-c2-l13": {
        "data_table": table(["Factor", "Detail"], [
            ["Page load speed", "A technical SEO factor affecting both ranking and user experience"],
        ]),
    },
    "digital-marketing-c2-l14": {
        "data_table": table(["Element", "Purpose"], [
            ["Clear call to action", "Guides visitors toward the desired conversion action"],
        ]),
    },
    "digital-marketing-c2-l15": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Comparing two variants to determine which performs better"],
        ]),
    },
    "digital-marketing-c2-l16": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Lead magnet", "An incentive offered in exchange for an email signup"],
        ]),
    },
    "digital-marketing-c2-l17": {
        "data_table": table(["Element", "Purpose"], [
            ["Subject line", "The first thing determining whether an email gets opened"],
        ]),
    },
    "digital-marketing-c2-l18": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Guest appearances", "Expands podcast reach through cross-promotion"],
        ]),
    },
    "digital-marketing-c2-l19": {
        "data_table": table(["Metric", "Meaning"], [
            ["Watch time", "A key ranking signal for YouTube's recommendation algorithm"],
        ]),
    },
    "digital-marketing-c2-l20": {
        "data_table": table(["Category", "Example"], [
            ["Paid media", "Advertising spend across channels"], ["Owned media", "Content production and website costs"],
        ]),
    },
    "digital-marketing-c2-l21": {
        "data_table": table(["Metric", "Formula"], [
            ["Quality Score", "Affects ad rank and cost-per-click in Google Ads"],
        ]),
    },
    "digital-marketing-c2-l22": {
        "data_table": table(["Check", "Purpose"], [
            ["Crawl error audit", "Identifies pages search engines can't properly index"],
        ]),
    },
    "digital-marketing-c2-l23": {
        "data_table": table(["Model", "Approach"], [
            ["First-touch attribution", "Credits the first interaction in the customer journey"], ["Multi-touch attribution", "Distributes credit across multiple touchpoints"],
        ]),
    },
    "digital-marketing-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Marketing mix modeling", "Statistically estimates each channel's contribution to sales"],
        ]),
    },
    "digital-marketing-c2-l25": {
        "data_table": table(["Metric", "Formula"], [
            ["Customer lifetime value", "Average purchase value x purchase frequency x customer lifespan"],
        ]),
        "formulae": ["CLV = avg_purchase_value * purchase_frequency * customer_lifespan"],
    },
    "digital-marketing-c2-l26": {
        "data_table": table(["Concept", "Meaning"], [
            ["Statistical significance", "Confirms whether an observed test result is likely real, not random chance"],
        ]),
    },
    "digital-marketing-c2-l27": {
        "data_table": table(["Segment", "Trigger"], [
            ["Behavioral segmentation", "Groups users by actions like purchase history or engagement"],
        ]),
    },
    "digital-marketing-c2-l28": {
        "data_table": table(["Element", "Purpose"], [
            ["Trigger", "Initiates an automated marketing workflow based on user behavior"],
        ]),
    },
    "digital-marketing-c2-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Programmatic advertising", "Automated, real-time bidding for ad placements across platforms"],
        ]),
    },
    "digital-marketing-c2-l30": {
        "data_table": table(["Step", "Purpose"], [
            ["Using real customer data", "Grounds a persona in actual behavior rather than assumptions"],
        ]),
    },
    "digital-marketing-c2-l31": {
        "data_table": table(["Strategy", "Detail"], [
            ["Lookalike audiences", "Targets new users resembling an existing high-value customer base"],
        ]),
    },
    "digital-marketing-c2-l32": {
        "data_table": table(["Consideration", "Detail"], [
            ["Cultural localization", "Adapting messaging beyond translation to fit local context"],
        ]),
    },
    "digital-marketing-c2-l33": {
        "data_table": table(["Layer", "Example"], [
            ["CRM", "Manages customer relationships and data"], ["Marketing automation platform", "Executes multi-channel campaigns"],
        ]),
    },
    "digital-marketing-c2-l34": {
        "data_table": table(["Element", "Purpose"], [
            ["Editorial calendar", "Coordinates content production and publishing schedules"],
        ]),
    },
    "digital-marketing-c2-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Competitive analysis", "Identifies gaps a brand can occupy in the market"],
        ]),
    },
    "digital-marketing-c2-l36": {
        "data_table": table(["Stage", "Focus"], [
            ["Awareness", "Customer first discovers the brand"], ["Consideration", "Customer evaluates options"], ["Decision", "Customer makes a purchase choice"],
        ]),
    },
    "digital-marketing-c2-l37": {
        "data_table": table(["Application", "Example"], [
            ["Predictive analytics", "Forecasting which customers are likely to churn"],
        ]),
    },
    "digital-marketing-c2-l38": {
        "data_table": table(["Metric", "Meaning"], [
            ["Engagement rate", "Measures audience interaction relative to reach"],
        ]),
    },
    "digital-marketing-c2-l39": {
        "data_table": table(["Framework", "Focus"], [
            ["AARRR (Pirate Metrics)", "Acquisition, Activation, Retention, Referral, Revenue"],
        ]),
    },
    "digital-marketing-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["First-party data", "Data collected directly from a company's own audience"],
        ]),
    },
    "digital-marketing-c2-l41": {
        "data_table": table(["Element", "Purpose"], [
            ["KPI dashboard", "Visualizes key metrics for quick, ongoing decision-making"],
        ]),
    },
    "digital-marketing-c2-l42": {
        "data_table": table(["Term", "Meaning"], [
            ["Account-based marketing", "Targets specific high-value accounts with personalized campaigns"],
        ]),
    },
    "digital-marketing-c2-l43": {
        "data_table": table(["Step", "Purpose"], [
            ["Iterative A/B testing", "Continuously refines a landing page's conversion rate"],
        ]),
    },
    "digital-marketing-c2-l44": {
        "data_table": table(["Step", "Purpose"], [
            ["Reallocating budget by ROI", "Shifts spend toward the highest-performing channels"],
        ]),
    },
    "digital-marketing-c2-l45": {
        "data_table": table(["Metric", "Meaning"], [
            ["View-through rate", "Measures how much of a video ad viewers actually watch"],
        ]),
    },
    "digital-marketing-c2-l46": {
        "data_table": table(["Metric", "Formula"], [
            ["Churn rate", "Customers lost / total customers at start of period"],
        ]),
        "formulae": ["churn_rate = customers_lost / customers_at_start"],
    },
    "digital-marketing-c2-l47": {
        "data_table": table(["Term", "Meaning"], [
            ["Structured data", "Markup helping search engines display rich results like star ratings"],
        ]),
    },
    "digital-marketing-c2-l48": {
        "data_table": table(["Step", "Purpose"], [
            ["Pre-drafted response templates", "Speeds up consistent messaging during a marketing crisis"],
        ]),
    },
    "digital-marketing-c2-l49": {
        "data_table": table(["Technique", "Example"], [
            ["Dynamic content", "Personalizes page content based on visitor attributes"],
        ]),
    },
    "digital-marketing-c2-l50": {
        "data_table": table(["Model", "Feature"], [
            ["In-house team", "Full control but higher fixed cost"], ["Agency", "Flexible expertise without full-time hiring"],
        ]),
    },
    "digital-marketing-c2-l51": {
        "data_table": table(["Intent Type", "Example"], [
            ["Informational", "'What is SEO'"], ["Transactional", "'Buy SEO software'"],
        ]),
    },
    "digital-marketing-c2-l52": {
        "data_table": table(["Challenge", "Detail"], [
            ["Cross-device tracking", "Connecting the same user's behavior across phone, tablet, and desktop"],
        ]),
    },
    "digital-marketing-c2-l53": {
        "data_table": table(["Element", "Purpose"], [
            ["Tiered rewards", "Incentivizes increased customer spending and loyalty over time"],
        ]),
    },
    "digital-marketing-c2-l54": {
        "data_table": table(["Metric", "Formula"], [
            ["Marketing ROI", "(Revenue attributed to marketing - cost) / cost"],
        ]),
        "formulae": ["ROI = (revenue - cost) / cost"],
    },
    "digital-marketing-c2-l55": {
        "data_table": table(["Term", "Meaning"], [
            ["Native advertising", "Paid content matching the form and function of the platform it appears on"],
        ]),
    },
    "digital-marketing-c2-l56": {
        "data_table": table(["Tool", "Use"], [
            ["Chatbot", "Automates real-time customer conversations and lead qualification"],
        ]),
    },
    "digital-marketing-c2-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Incrementality testing", "Measures the true causal lift a marketing campaign generates"],
        ]),
    },
    "digital-marketing-c2-l58": {
        "data_table": table(["Regulation", "Region"], [
            ["GDPR", "European Union data privacy regulation"], ["CCPA", "California data privacy regulation"],
        ]),
    },
    "digital-marketing-c2-l59": {
        "data_table": table(["Component", "Purpose"], [
            ["Integrated campaign plan", "Aligns messaging consistently across every channel"],
        ]),
    },
    "digital-marketing-c2-l60": {
        "data_table": table(["Trend", "Detail"], [
            ["AI-generated content", "Growing use of AI tools to accelerate content production"],
        ]),
    },
    "digital-marketing-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Estimating channel contribution", "Isolating which channels drove a sales increase"],
        ]),
    },
    "digital-marketing-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Planning a content calendar", "Scheduling posts around key product launches"],
        ]),
    },
    "digital-marketing-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Choosing distribution channels", "Matching content type to the platform where it performs best"],
        ]),
    },
    "digital-marketing-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a content strategy", "Aligning content themes with audience needs at each funnel stage"],
        ]),
    },
    "digital-marketing-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a platform mix", "Matching social platforms to a brand's target audience"],
        ]),
    },
    "digital-marketing-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Auditing a content calendar", "Checking for balanced topic and format coverage"],
        ]),
    },
    "digital-marketing-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing a brand story", "Identifying its emotional hook and core message"],
        ]),
    },
    "digital-marketing-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing owned vs earned media", "Assessing which drove more traffic in a campaign"],
        ]),
    },
    "digital-marketing-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Analyzing an ad's performance", "Reviewing engagement metrics on a real Instagram ad"],
        ]),
    },
    "digital-marketing-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Building a B2B content plan", "Mapping LinkedIn content to a sales funnel stage"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Digital Marketing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Digital Marketing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Digital Marketing lessons (completing 70/70).")


if __name__ == "__main__":
    main()
