#!/usr/bin/env python3
"""Depth pass, C1 Digital Marketing: fill in real, hand-checked
data_table content for the 69 C1 Digital Marketing lessons not covered
by the earlier breadth-first batch. Brings C1 Digital Marketing to
full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_digital_marketing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "digital-marketing-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Digital marketing", "Promoting products or services through digital channels"],
        ]),
    },
    "digital-marketing-c1-l2": {
        "data_table": table(["Term", "Meaning"], [
            ["SEO", "Search Engine Optimization, improving a site's visibility in search results"],
        ]),
    },
    "digital-marketing-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Buyer persona", "A fictional profile representing a target customer segment"],
        ]),
    },
    "digital-marketing-c1-l5": {
        "data_table": table(["Stage", "Example"], [
            ["Awareness", "Customer discovers the brand"], ["Consideration", "Customer evaluates options"], ["Decision", "Customer makes a purchase"],
        ]),
    },
    "digital-marketing-c1-l6": {
        "data_table": table(["Channel", "Example"], [
            ["Organic search", "SEO"], ["Paid search", "Google Ads"], ["Social media", "Instagram, LinkedIn"],
        ]),
    },
    "digital-marketing-c1-l7": {
        "data_table": table(["Element", "Purpose"], [
            ["Title tag", "Tells search engines the page topic"], ["Meta description", "Summarizes the page in search results"],
        ]),
    },
    "digital-marketing-c1-l8": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify search volume", "Shows how often a keyword is searched"], ["Assess competition", "Shows how hard it is to rank for a keyword"],
        ]),
    },
    "digital-marketing-c1-l9": {
        "data_table": table(["Factor", "Impact"], [
            ["Page load speed", "Slow pages increase bounce rate"],
        ]),
    },
    "digital-marketing-c1-l10": {
        "data_table": table(["Format", "Example"], [
            ["Blog post", "Written article"], ["Video", "Visual, engaging content"], ["Infographic", "Visual data summary"],
        ]),
    },
    "digital-marketing-c1-l11": {
        "data_table": table(["Platform", "Primary Use"], [
            ["LinkedIn", "Professional networking and B2B marketing"], ["Instagram", "Visual content and brand storytelling"],
        ]),
    },
    "digital-marketing-c1-l12": {
        "data_table": table(["Model", "Meaning"], [
            ["CPC", "Cost Per Click, pays per click received"], ["CPM", "Cost Per Mille, pays per 1000 impressions"],
        ]),
    },
    "digital-marketing-c1-l13": {
        "data_table": table(["Practice", "Reason"], [
            ["Mobile-responsive design", "Most web traffic now comes from mobile devices"],
        ]),
    },
    "digital-marketing-c1-l14": {
        "data_table": table(["Metric", "Measures"], [
            ["CTR", "Click-through rate"], ["Conversion rate", "Percentage of visitors who complete a goal"],
        ]),
    },
    "digital-marketing-c1-l15": {
        "data_table": table(["Element", "Purpose"], [
            ["Logo", "Visual mark representing the brand"], ["Tone of voice", "Consistent style of brand communication"],
        ]),
    },
    "digital-marketing-c1-l16": {
        "data_table": table(["Tool", "Purpose"], [
            ["Marketing calendar", "Plans and schedules campaigns and content"],
        ]),
    },
    "digital-marketing-c1-l17": {
        "data_table": table(["Tactic", "Example"], [
            ["Press release", "Announces news to media outlets"],
        ]),
    },
    "digital-marketing-c1-l18": {
        "data_table": table(["Task", "Purpose"], [
            ["Responding to comments", "Builds engagement and trust with the audience"],
        ]),
    },
    "digital-marketing-c1-l19": {
        "data_table": table(["Principle", "Meaning"], [
            ["Transparency", "Being honest about sponsored content and data use"],
        ]),
    },
    "digital-marketing-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Analyzing competitor content", "Identifies gaps and opportunities"],
        ]),
    },
    "digital-marketing-c1-l21": {
        "data_table": table(["Tool", "Purpose"], [
            ["Google Analytics", "Tracks website traffic and user behavior"],
        ]),
    },
    "digital-marketing-c1-l22": {
        "data_table": table(["Source", "Example"], [
            ["Organic", "Search engine results"], ["Referral", "Links from other websites"], ["Direct", "Typed URL"],
        ]),
    },
    "digital-marketing-c1-l23": {
        "data_table": table(["Component", "Purpose"], [
            ["Ad campaign", "Groups related ads and settings"], ["Keyword bidding", "Determines ad placement cost"],
        ]),
    },
    "digital-marketing-c1-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["PPC", "Pay-Per-Click, advertisers pay only when their ad is clicked"],
        ]),
    },
    "digital-marketing-c1-l25": {
        "data_table": table(["Format", "Example"], [
            ["Banner ad", "Visual ad on a publisher's website"],
        ]),
    },
    "digital-marketing-c1-l26": {
        "data_table": table(["Term", "Meaning"], [
            ["Retargeting", "Showing ads to users who previously visited your site"],
        ]),
    },
    "digital-marketing-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Affiliate marketing", "Paying partners a commission for referred sales"],
        ]),
    },
    "digital-marketing-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Influencer marketing", "Partnering with individuals who have an engaged audience"],
        ]),
    },
    "digital-marketing-c1-l29": {
        "data_table": table(["Format", "Example"], [
            ["Explainer video", "Demonstrates a product's value quickly"],
        ]),
    },
    "digital-marketing-c1-l30": {
        "data_table": table(["Tool", "Purpose"], [
            ["Marketing automation platform", "Sends targeted messages based on user behavior"],
        ]),
    },
    "digital-marketing-c1-l31": {
        "data_table": table(["Strategy", "Example"], [
            ["Lead magnet", "Free content offered in exchange for contact info"],
        ]),
    },
    "digital-marketing-c1-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["CRO", "Conversion Rate Optimization, improving the percentage of visitors who convert"],
        ]),
    },
    "digital-marketing-c1-l33": {
        "data_table": table(["Metric", "Meaning"], [
            ["Bounce rate", "Percentage of visitors who leave after viewing one page"],
        ]),
    },
    "digital-marketing-c1-l34": {
        "data_table": table(["Step", "Purpose"], [
            ["Interviewing real customers", "Grounds personas in actual data, not assumptions"],
        ]),
    },
    "digital-marketing-c1-l35": {
        "data_table": table(["Principle", "Reason"], [
            ["Clear call-to-action", "Tells the reader exactly what to do next"],
        ]),
    },
    "digital-marketing-c1-l36": {
        "data_table": table(["Metric", "Meaning"], [
            ["Open rate", "Percentage of recipients who opened the email"],
        ]),
    },
    "digital-marketing-c1-l37": {
        "data_table": table(["Model", "Meaning"], [
            ["Last-click attribution", "Gives all credit to the final touchpoint before conversion"],
        ]),
    },
    "digital-marketing-c1-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["CRM", "Customer Relationship Management, tracks interactions with customers"],
        ]),
    },
    "digital-marketing-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Growth hacking", "Rapid, experimental marketing tactics to grow quickly"],
        ]),
    },
    "digital-marketing-c1-l40": {
        "data_table": table(["Regulation", "Focus"], [
            ["GDPR", "EU regulation on data privacy and consent"],
        ]),
    },
    "digital-marketing-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Native advertising", "Paid content designed to match the look and feel of its platform"],
        ]),
    },
    "digital-marketing-c1-l42": {
        "data_table": table(["Tactic", "Purpose"], [
            ["Abandoned cart emails", "Recovers lost e-commerce sales"],
        ]),
    },
    "digital-marketing-c1-l43": {
        "data_table": table(["Practice", "Reason"], [
            ["Using conversational keywords", "Matches how people phrase voice search queries"],
        ]),
    },
    "digital-marketing-c1-l44": {
        "data_table": table(["Use Case", "Benefit"], [
            ["Chatbot customer support", "Provides instant responses to common questions"],
        ]),
    },
    "digital-marketing-c1-l45": {
        "data_table": table(["Stage", "Example"], [
            ["Top of funnel", "Awareness content"], ["Bottom of funnel", "Purchase-focused content"],
        ]),
    },
    "digital-marketing-c1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["User-generated content", "Content created by customers rather than the brand"],
        ]),
    },
    "digital-marketing-c1-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Allocating by channel performance", "Directs budget toward the highest-return channels"],
        ]),
    },
    "digital-marketing-c1-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["SEM", "Search Engine Marketing, includes both paid and organic search efforts"],
        ]),
    },
    "digital-marketing-c1-l49": {
        "data_table": table(["Term", "Meaning"], [
            ["A/B testing", "Comparing two versions of content to see which performs better"],
        ]),
    },
    "digital-marketing-c1-l50": {
        "data_table": table(["Format", "Benefit"], [
            ["Branded podcast", "Builds deeper audience connection through long-form audio"],
        ]),
    },
    "digital-marketing-c1-l51": {
        "data_table": table(["Element", "Purpose"], [
            ["Disclosure clause", "Ensures sponsored content is legally and ethically labeled"],
        ]),
    },
    "digital-marketing-c1-l52": {
        "data_table": table(["Practice", "Reason"], [
            ["App Store Optimization", "Improves an app's visibility in app store search"],
        ]),
    },
    "digital-marketing-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Programmatic advertising", "Automated, data-driven buying of digital ad space"],
        ]),
    },
    "digital-marketing-c1-l54": {
        "data_table": table(["Program Type", "Example"], [
            ["Points program", "Rewards repeat purchases with redeemable points"],
        ]),
    },
    "digital-marketing-c1-l55": {
        "data_table": table(["Method", "Example"], [
            ["Surveys", "Quantitative customer feedback"], ["Focus groups", "Qualitative in-depth discussion"],
        ]),
    },
    "digital-marketing-c1-l56": {
        "data_table": table(["Element", "Purpose"], [
            ["Consistent color palette", "Reinforces brand recognition across channels"],
        ]),
    },
    "digital-marketing-c1-l57": {
        "data_table": table(["Term", "Meaning"], [
            ["Cross-channel marketing", "Coordinating messaging consistently across multiple platforms"],
        ]),
    },
    "digital-marketing-c1-l58": {
        "data_table": table(["Step", "Purpose"], [
            ["Setting clear objectives", "Guides every subsequent campaign decision"],
        ]),
    },
    "digital-marketing-c1-l59": {
        "data_table": table(["Trend", "Example"], [
            ["AI-generated content", "Increasingly used for personalization at scale"],
        ]),
    },
    "digital-marketing-c1-l60": {
        "data_table": table(["Principle", "Meaning"], [
            ["Honesty in claims", "Avoiding false or misleading advertising"],
        ]),
    },
    "digital-marketing-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Mapping a customer journey", "Outlining the stages a customer goes through before buying"],
        ]),
    },
    "digital-marketing-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Auditing on-page SEO", "Checking a sample page's title tags and headers"],
        ]),
    },
    "digital-marketing-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Identifying funnel drop-off", "Finding where users abandon a sample purchase flow"],
        ]),
    },
    "digital-marketing-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a persona", "Creating a sample buyer persona from customer data"],
        ]),
    },
    "digital-marketing-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Mapping touchpoints", "Listing every interaction a customer has with a brand"],
        ]),
    },
    "digital-marketing-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Choosing a channel mix", "Selecting the best channels for a small business's budget"],
        ]),
    },
    "digital-marketing-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Optimizing a page", "Rewriting a title tag and meta description for a sample page"],
        ]),
    },
    "digital-marketing-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Researching keywords", "Finding relevant keywords for a sample product page"],
        ]),
    },
    "digital-marketing-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Testing usability", "Identifying friction points in a sample checkout page"],
        ]),
    },
    "digital-marketing-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Choosing content formats", "Matching a message to the best format for its audience"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Digital Marketing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Digital Marketing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Digital Marketing lessons (completing 70/70).")


if __name__ == "__main__":
    main()
