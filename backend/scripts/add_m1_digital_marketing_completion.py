#!/usr/bin/env python3
"""Depth pass, M1 Digital Marketing: fill in real, hand-checked
data_table content for the 119 M1 Digital Marketing lessons not
covered by the earlier breadth-first batch. Brings M1 Digital
Marketing to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning video/
multimedia marketing, privacy/ethics, advanced attribution and
optimization, and applied marketing across emerging channels;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_digital_marketing_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Platform", "Common Video Aspect Ratio"], [
    ["Instagram Stories/Reels", "9:16 (vertical)"],
    ["YouTube", "16:9 (horizontal)"],
    ["Instagram Feed", "1:1 (square) or 4:5"],
])

CHARTS: dict[str, dict] = {
    "digital-marketing-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Video/multimedia marketing", "Uses video and rich media to engage and convert audiences"],
    ])},
    "digital-marketing-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Marketing ethics & data privacy", "Balances effective marketing with respect for consumer rights and data protection"],
    ])},
    "digital-marketing-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Livestream/webinar marketing", "Engages audiences in real time to build trust and generate leads"],
    ])},
    "digital-marketing-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Short-form video strategy", "Uses brief, highly engaging video content (Reels/Shorts) for reach and discovery"],
    ])},
    "digital-marketing-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["YouTube advertising", "Places video ads across YouTube's search, watch, and discovery surfaces"],
    ])},
    "digital-marketing-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Shoppable video", "Lets viewers purchase products directly from an interactive video experience"],
    ])},
    "digital-marketing-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["GDPR / global privacy compliance", "Requires marketers to obtain consent and handle personal data lawfully"],
    ])},
    "digital-marketing-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Cookie-less tracking", "Measures marketing performance without relying on third-party cookies"],
    ])},
    "digital-marketing-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Dark pattern", "A deceptive design choice that manipulates users into unintended actions"],
    ])},
    "digital-marketing-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Marketing data governance", "Establishes policy for how customer data is collected, stored, and used"],
    ])},
    "digital-marketing-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["International marketing strategy", "Adapts marketing plans to succeed across different countries and markets"],
    ])},
    "digital-marketing-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Localization", "Adapts content, language, and cultural references for a specific target market"],
    ])},
    "digital-marketing-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Global/multilingual SEO", "Optimizes content to rank across multiple languages and regions"],
    ])},
    "digital-marketing-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Marketing team operations", "Structures roles and workflows so a marketing team executes efficiently"],
    ])},
    "digital-marketing-m1-l16": {"data_table": table(["Model", "Feature"], [
        ["B2B", "Longer sales cycles, relationship-driven"],
        ["B2C", "Shorter cycles, volume and emotion-driven"],
    ])},
    "digital-marketing-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Startup marketing", "Prioritizes low-cost, high-leverage tactics under tight budget constraints"],
    ])},
    "digital-marketing-m1-l18": {"data_table": table(["Stage (AARRR)", "Meaning"], [
        ["Acquisition, Activation, Retention, Referral, Revenue", "The growth hacking funnel framework"],
    ])},
    "digital-marketing-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Viral marketing", "Designs content and incentives so users spread a message to others themselves"],
    ])},
    "digital-marketing-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Capstone campaign", "Integrates strategy, creative, channels, and measurement into one full campaign design"],
    ])},
    "digital-marketing-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Attribution modeling", "Assigns credit for a conversion across the touchpoints that led to it"],
    ])},
    "digital-marketing-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Programmatic advertising / RTB", "Buys and sells ad inventory automatically via real-time auctions"],
    ])},
    "digital-marketing-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Quality Score", "A search ad platform's rating of ad relevance that affects cost and placement"],
    ])},
    "digital-marketing-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Multivariate testing", "Tests multiple page elements simultaneously to find the best combination"],
    ])},
    "digital-marketing-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling", "Estimates each channel's contribution to overall marketing outcomes"],
    ])},
    "digital-marketing-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["RFM analysis", "Segments customers by Recency, Frequency, and Monetary value"],
    ])},
    "digital-marketing-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Marketing automation workflow", "Triggers personalized messages automatically based on user behavior"],
    ])},
    "digital-marketing-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Account-based marketing", "Targets specific high-value accounts with personalized campaigns"],
    ])},
    "digital-marketing-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Influencer marketing ROI", "Measures the return generated by influencer partnerships"],
    ])},
    "digital-marketing-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Affiliate marketing network", "Pays partners a commission for referred sales or leads"],
    ])},
    "digital-marketing-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Email deliverability", "Ensures emails reach the inbox rather than being filtered as spam"],
    ])},
    "digital-marketing-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral email triggers", "Sends emails automatically based on a specific user action"],
    ])},
    "digital-marketing-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Martech stack", "The set of integrated tools a marketing team uses to execute and measure campaigns"],
    ])},
    "digital-marketing-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Customer data platform", "Unifies customer data from multiple sources into a single profile"],
    ])},
    "digital-marketing-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Retargeting / remarketing", "Re-engages users who previously interacted with a brand but didn't convert"],
    ])},
    "digital-marketing-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Native advertising", "Ads designed to match the look and feel of the platform they appear on"],
    ])},
    "digital-marketing-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Crawl budget", "The number of pages a search engine will crawl on a site within a given time"],
    ])},
    "digital-marketing-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Digital PR / link building", "Earns authoritative backlinks through outreach and newsworthy content"],
    ])},
    "digital-marketing-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Topic clusters / pillar pages", "Organizes content around a core topic linked to supporting subtopic pages"],
    ])},
    "digital-marketing-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Social algorithm optimization", "Tailors content to perform well under a platform's ranking algorithm"],
    ])},
    "digital-marketing-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Community management", "Builds and nurtures an engaged audience around a brand"],
    ])},
    "digital-marketing-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Multi-channel funnel analysis", "Examines how multiple channels interact before a conversion occurs"],
    ])},
    "digital-marketing-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Google Analytics 4", "An event-based analytics platform for measuring cross-platform user behavior"],
    ])},
    "digital-marketing-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Marketing KPI dashboard", "Visualizes the key metrics stakeholders need to judge marketing performance"],
    ])},
    "digital-marketing-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Personalization at scale", "Tailors content to individual users automatically across a large audience"],
    ])},
    "digital-marketing-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic creative optimization", "Automatically assembles and tests ad creative variations for best performance"],
    ])},
    "digital-marketing-m1-l47": {"data_table": table(["Principle", "Detail"], [
        ["Above-the-fold clarity", "The most persuasive value proposition should be visible without scrolling"],
    ])},
    "digital-marketing-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Pricing psychology", "Uses cognitive biases (e.g. charm pricing) to influence purchase decisions"],
    ])},
    "digital-marketing-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Loyalty program design", "Structures rewards to encourage repeat purchases and retention"],
    ])},
    "digital-marketing-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Brand positioning", "Defines how a brand is distinctly perceived relative to competitors"],
    ])},
    "digital-marketing-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Brand equity measurement", "Quantifies the value a brand name adds beyond its functional product"],
    ])},
    "digital-marketing-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Conjoint analysis", "Infers how customers value individual product features by analyzing trade-off choices"],
    ])},
    "digital-marketing-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Neuromarketing", "Studies physiological and neurological responses to marketing stimuli"],
    ])},
    "digital-marketing-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["ASO", "App Store Optimization; improves an app's visibility and conversion in app store search"],
    ])},
    "digital-marketing-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Push notification strategy", "Times and personalizes mobile alerts to re-engage users without annoying them"],
    ])},
    "digital-marketing-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Cookieless attribution", "Measures marketing impact using aggregated or modeled data instead of individual cookies"],
    ])},
    "digital-marketing-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Contextual advertising", "Targets ads based on the content of the page rather than user tracking data"],
    ])},
    "digital-marketing-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Voice assistant marketing", "Optimizes brand presence for voice search and smart speaker interactions"],
    ])},
    "digital-marketing-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Conversational commerce", "Uses chatbots and messaging to guide customers through a purchase"],
    ])},
    "digital-marketing-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Lead nurturing sequence", "A series of automated touches that moves a lead toward a purchase decision"],
    ])},
    "digital-marketing-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Webinar funnel", "Uses a webinar as the central conversion event in a marketing funnel"],
    ])},
    "digital-marketing-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Podcast advertising", "Places brand messages within podcast episodes, often via host reads"],
    ])},
    "digital-marketing-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Connected TV / OTT advertising", "Delivers targeted video ads through internet-streamed television services"],
    ])},
    "digital-marketing-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Digital out-of-home advertising", "Displays dynamic digital ads on public screens and billboards"],
    ])},
    "digital-marketing-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Marketing crisis management", "Responds to reputational threats quickly and transparently to limit damage"],
    ])},
    "digital-marketing-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Influencer contract compliance", "Ensures influencer partnerships meet disclosure laws and brand terms"],
    ])},
    "digital-marketing-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Subscription marketing", "Focuses on acquisition and retention economics unique to recurring-revenue models"],
    ])},
    "digital-marketing-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Customer retention marketing", "Focuses spend and effort on keeping existing customers engaged and buying"],
    ])},
    "digital-marketing-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Win-back campaign", "Re-engages lapsed customers with targeted offers or messaging"],
    ])},
    "digital-marketing-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Marketing budget forecasting", "Predicts future spend needs based on goals and historical performance"],
    ])},
    "digital-marketing-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Marketing ROI measurement", "Quantifies the financial return generated by marketing investment"],
    ])},
    "digital-marketing-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Marketplace/platform marketing", "Promotes a seller's presence within a larger third-party marketplace"],
    ])},
    "digital-marketing-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Social commerce", "Enables purchases directly within social media platforms"],
    ])},
    "digital-marketing-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Live shopping", "Combines livestreaming with real-time purchasing during a broadcast"],
    ])},
    "digital-marketing-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["User-generated content strategy", "Encourages and features customer-created content to build trust"],
    ])},
    "digital-marketing-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Referral marketing", "Incentivizes existing customers to bring in new customers"],
    ])},
    "digital-marketing-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Lead scoring algorithm", "Ranks leads by likelihood to convert based on behavior and fit"],
    ])},
    "digital-marketing-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Nonprofit digital marketing", "Focuses on donor acquisition and mission-driven engagement rather than sales"],
    ])},
    "digital-marketing-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Political/advocacy campaigns", "Mobilizes voters or supporters using targeted digital messaging"],
    ])},
    "digital-marketing-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Marketing compliance in regulated industries", "Ensures marketing claims and data use meet industry-specific legal requirements"],
    ])},
    "digital-marketing-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Financial services marketing", "Navigates strict disclosure and suitability rules unique to financial products"],
    ])},
    "digital-marketing-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare marketing compliance", "Ensures marketing meets patient privacy and medical claims regulations"],
    ])},
    "digital-marketing-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["B2B content syndication", "Distributes content through third-party platforms to reach new B2B audiences"],
    ])},
    "digital-marketing-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Sales and marketing alignment", "Coordinates goals and handoffs between sales and marketing teams"],
    ])},
    "digital-marketing-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Demand generation", "Builds awareness and interest to fill the top of a sales pipeline"],
    ])},
    "digital-marketing-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Cohort retention analytics", "Tracks how a group of users who share a starting point retains over time"],
    ])},
    "digital-marketing-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Experimentation governance", "Establishes standards for how marketing tests are designed and validated"],
    ])},
    "digital-marketing-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["SERP feature optimization", "Targets rich search results (e.g. maps, images) beyond standard blue links"],
    ])},
    "digital-marketing-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Featured snippet optimization", "Formats content to be selected for a search engine's highlighted answer box"],
    ])},
    "digital-marketing-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["AR marketing", "Uses augmented reality experiences to let customers virtually try products"],
    ])},
    "digital-marketing-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Metaverse/virtual world marketing", "Builds brand presence and experiences within persistent virtual environments"],
    ])},
    "digital-marketing-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["CLV analytics", "Predicts the total value a customer will generate over their relationship with a brand"],
    ])},
    "digital-marketing-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Channel mix optimization", "Allocates marketing spend across channels for the best overall return"],
    ])},
    "digital-marketing-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Product-led growth marketing", "Uses the product itself as the primary driver of acquisition and expansion"],
    ])},
    "digital-marketing-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Marketing talent/agency management", "Manages internal teams and external agency relationships effectively"],
    ])},
    "digital-marketing-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Executive marketing data visualization", "Presents marketing performance clearly for leadership decision-making"],
    ])},
    "digital-marketing-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Incrementality testing", "Measures a campaign's true additional impact versus what would have happened anyway"],
    ])},
    "digital-marketing-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Generative engine optimization", "Optimizes content to be surfaced by AI-powered answer engines rather than only search results"],
    ])},
    "digital-marketing-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Data clean room", "Lets two parties analyze combined data without either seeing the other's raw data"],
    ])},
    "digital-marketing-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Advergaming / in-game advertising", "Places brand messages or products within video games"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"digital-marketing-m1-l{base_n}"
    worked_key = f"digital-marketing-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Digital Marketing"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Digital Marketing: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Digital Marketing lessons (completing 120/120).")


if __name__ == "__main__":
    main()
