#!/usr/bin/env python3
"""Depth pass, M1 UI/UX Design: fill in real, hand-checked data_table
content for the 119 M1 UI/UX Design lessons not covered by the
earlier breadth-first batch. Brings M1 UI/UX Design to full 120/120
coverage.

Structure: l1-l100 are unique graduate-level topics spanning UX
writing/research methods, design systems, emerging interface
modalities (voice, AR/VR, AI), and design leadership/operations;
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Preserves the subject's lesson-ID prefix quirk: l1-l100 use
"ui/ux-design-m1-" (with a literal slash) while l101-l120 use the
slash-free "ui-ux-design-m1-".

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_ui_ux_design_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Voice", "A brand's consistent personality in writing"],
    ["Tone", "How that voice adapts to context (e.g. error vs. success message)"],
])

CHARTS: dict[str, dict] = {
    "ui/ux-design-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["UX writing / microcopy", "Crafts the small pieces of interface text that guide user action"],
    ])},
    "ui/ux-design-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Design thinking", "A human-centered process of empathizing, defining, ideating, prototyping, and testing"],
    ])},
    "ui/ux-design-m1-l4": {"data_table": table(["Principle", "Detail"], [
        ["Clear error messages", "Explain what went wrong and how to fix it, without blame"],
    ])},
    "ui/ux-design-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Conversational UI writing", "Designs chatbot dialogue that feels natural and guides the user efficiently"],
    ])},
    "ui/ux-design-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["UX content localization", "Adapts interface text for language, tone, and cultural context, not just translation"],
    ])},
    "ui/ux-design-m1-l7": {"data_table": table(["State", "Writing goal"], [
        ["Onboarding", "Sets expectations and builds early confidence"],
        ["Empty state", "Explains what to do next when there's nothing to show yet"],
    ])},
    "ui/ux-design-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["Ideation facilitation", "Guides a group through structured brainstorming toward useful ideas"],
    ])},
    "ui/ux-design-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Design sprint", "A time-boxed, five-day process for solving problems through prototyping and testing"],
    ])},
    "ui/ux-design-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["How Might We", "Reframes a problem statement as an open, actionable question for ideation"],
    ])},
    "ui/ux-design-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Co-design", "Involves users directly as collaborators in the design process"],
    ])},
    "ui/ux-design-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Conversational interface design", "Designs interactions built around natural language rather than visual controls"],
    ])},
    "ui/ux-design-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["A/B testing (UX)", "Compares two design variants with real users to decide which performs better"],
    ])},
    "ui/ux-design-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Heuristic evaluation", "Experts review an interface against established usability principles"],
    ])},
    "ui/ux-design-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Diary study", "Participants record their experiences with a product over an extended period"],
    ])},
    "ui/ux-design-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Ethnographic research", "Observes users in their natural context to understand real-world behavior"],
    ])},
    "ui/ux-design-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Service blueprint", "Maps the front-stage and back-stage steps that deliver a service experience"],
    ])},
    "ui/ux-design-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Design critique culture", "Structures feedback sessions to improve design quality constructively"],
    ])},
    "ui/ux-design-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["UX ROI measurement", "Quantifies the business value delivered by design improvements"],
    ])},
    "ui/ux-design-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["UX case study", "Documents a design process and outcome for a portfolio audience"],
    ])},
    "ui/ux-design-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Component API design", "Defines a reusable design system component's configurable props and behavior"],
    ])},
    "ui/ux-design-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Design tokens", "Named values (color, spacing) that keep styling consistent across platforms"],
    ])},
    "ui/ux-design-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["WCAG 2.2", "The current web content accessibility guidelines defining conformance levels"],
    ])},
    "ui/ux-design-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Screen reader compatibility", "Ensures assistive technology can correctly interpret and announce interface content"],
    ])},
    "ui/ux-design-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Contrast ratio", "A measurable value ensuring text remains readable against its background"],
    ])},
    "ui/ux-design-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Motion design principles", "Uses animation purposefully to guide attention and communicate state changes"],
    ])},
    "ui/ux-design-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Micro-interaction", "A small, focused moment of feedback triggered by a single user action"],
    ])},
    "ui/ux-design-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Information architecture", "Organizes and structures content so users can find what they need"],
    ])},
    "ui/ux-design-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Mental model diagram", "Visualizes how users expect a system to work, to compare against its actual design"],
    ])},
    "ui/ux-design-m1-l30": {"data_table": table(["Principle", "Detail"], [
        ["Gestalt proximity", "Elements placed close together are perceived as related"],
    ])},
    "ui/ux-design-m1-l31": {"data_table": table(["Law", "Statement"], [
        ["Fitts's Law", "Time to reach a target depends on its distance and size"],
    ])},
    "ui/ux-design-m1-l32": {"data_table": table(["Law", "Statement"], [
        ["Hick's Law", "Decision time increases with the number and complexity of choices"],
    ])},
    "ui/ux-design-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Eye-tracking research", "Records where users look to reveal attention patterns on an interface"],
    ])},
    "ui/ux-design-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Biometric UX research", "Uses physiological signals (e.g. skin response) to measure user reactions"],
    ])},
    "ui/ux-design-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Usability testing protocol", "A structured plan for observing users completing tasks with a design"],
    ])},
    "ui/ux-design-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Remote unmoderated testing", "Collects usability data from users completing tasks independently, without a facilitator"],
    ])},
    "ui/ux-design-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Quantitative UX research", "Uses surveys and statistical analysis to measure user attitudes at scale"],
    ])},
    "ui/ux-design-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Research repository", "Centralizes past research findings so insights can be reused across teams"],
    ])},
    "ui/ux-design-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Senior design critique framework", "A structured method for giving actionable feedback at a strategic level"],
    ])},
    "ui/ux-design-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["UX-engineering collaboration", "Coordinates design and development to ship a design faithfully and efficiently"],
    ])},
    "ui/ux-design-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["DesignOps", "Streamlines tools, process, and staffing so design teams can work efficiently at scale"],
    ])},
    "ui/ux-design-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Scaling design teams", "Structures roles and processes so design quality holds as an organization grows"],
    ])},
    "ui/ux-design-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["High-fidelity prototyping", "Builds interactive prototypes closely resembling the final product's look and feel"],
    ])},
    "ui/ux-design-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Hardware-software prototyping", "Rapidly builds prototypes combining physical devices with software interfaces"],
    ])},
    "ui/ux-design-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Voice UI design pattern", "Structures spoken interactions to be clear and forgiving of ambiguity"],
    ])},
    "ui/ux-design-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Multimodal interface design", "Combines voice, touch, and gesture inputs into a coherent interaction model"],
    ])},
    "ui/ux-design-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["AR interface design", "Overlays digital content onto the user's real-world environment"],
    ])},
    "ui/ux-design-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["VR environment design", "Designs fully immersive 3D spaces and interactions for virtual reality"],
    ])},
    "ui/ux-design-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Spatial computing interaction", "Designs interfaces that respond to a user's position and movement in 3D space"],
    ])},
    "ui/ux-design-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Wearable device constraints", "Designs for very small screens, glanceable info, and limited input methods"],
    ])},
    "ui/ux-design-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Automotive UX", "Designs in-vehicle interfaces that minimize driver distraction"],
    ])},
    "ui/ux-design-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Ambient computing design", "Designs interfaces that blend into the environment rather than demanding focused attention"],
    ])},
    "ui/ux-design-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Dark pattern", "A deceptive design choice that manipulates users into unintended actions"],
    ])},
    "ui/ux-design-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Designing for trust", "Uses transparency and consistency to build user confidence in a product"],
    ])},
    "ui/ux-design-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Privacy-centered design", "Makes data collection and use transparent and minimizes unnecessary exposure"],
    ])},
    "ui/ux-design-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Consent flow design", "Presents data-sharing choices clearly so users can make informed decisions"],
    ])},
    "ui/ux-design-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Fintech UX pattern", "Balances trust, security, and clarity in interfaces handling users' money"],
    ])},
    "ui/ux-design-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare UX", "Designs with patient safety as a primary constraint alongside usability"],
    ])},
    "ui/ux-design-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Designing for children", "Accounts for developing motor and cognitive skills in interface design"],
    ])},
    "ui/ux-design-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Designing for older adults", "Accounts for age-related changes in vision, motor control, and technology familiarity"],
    ])},
    "ui/ux-design-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Cross-cultural UX adaptation", "Adjusts design conventions to match cultural expectations across regions"],
    ])},
    "ui/ux-design-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Global design system", "Supports multiple regions and languages within one consistent design foundation"],
    ])},
    "ui/ux-design-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Low-bandwidth design", "Optimizes interfaces to remain usable on slow connections and constrained devices"],
    ])},
    "ui/ux-design-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Progressive disclosure", "Reveals complexity gradually so users aren't overwhelmed upfront"],
    ])},
    "ui/ux-design-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Onboarding optimization", "Refines the first-use experience to improve activation and retention"],
    ])},
    "ui/ux-design-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Notification design strategy", "Balances timely alerts against the risk of overwhelming or annoying users"],
    ])},
    "ui/ux-design-m1-l67": {"data_table": table(["State", "Design goal"], [
        ["Empty state", "Guides the user toward a productive next action"],
        ["Error state", "Explains what went wrong and how to recover"],
    ])},
    "ui/ux-design-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Dashboard data visualization", "Presents complex data so users can quickly interpret and act on it"],
    ])},
    "ui/ux-design-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise data table design", "Balances density and clarity for interfaces displaying large, complex datasets"],
    ])},
    "ui/ux-design-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["CLI/developer tool UX", "Designs command-line and technical tool interfaces for an expert user base"],
    ])},
    "ui/ux-design-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Developer experience (DX)", "Evaluates an API's usability from the perspective of the developers who use it"],
    ])},
    "ui/ux-design-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["B2B SaaS onboarding", "Guides new business users to their first meaningful value in a software product"],
    ])},
    "ui/ux-design-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise software UX pattern", "Design conventions suited to complex, permission-heavy business applications"],
    ])},
    "ui/ux-design-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tenant SaaS design", "Designs interfaces that adapt cleanly to different customer configurations"],
    ])},
    "ui/ux-design-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Advanced innovation workshop facilitation", "Guides senior stakeholders through structured design thinking exercises"],
    ])},
    "ui/ux-design-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Speculative design", "Uses design artifacts to provoke discussion about possible futures"],
    ])},
    "ui/ux-design-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Design fiction", "Builds narrative scenarios to explore the implications of future technology"],
    ])},
    "ui/ux-design-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Human-centered AI design", "Keeps user needs and understanding central when designing AI-powered features"],
    ])},
    "ui/ux-design-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Explainable AI interfaces", "Helps users understand why an AI system produced a given output"],
    ])},
    "ui/ux-design-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["Generative AI product design", "Designs interfaces for interacting with unpredictable, generative model outputs"],
    ])},
    "ui/ux-design-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Conversational AI beyond chatbots", "Extends conversational design into agents, assistants, and multi-turn workflows"],
    ])},
    "ui/ux-design-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Trust calibration", "Helps users form an accurate sense of how much to rely on an AI system"],
    ])},
    "ui/ux-design-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Ethical AI-driven UX frameworks", "Guides responsible design decisions when AI shapes user experience"],
    ])},
    "ui/ux-design-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["HEART framework", "Measures Happiness, Engagement, Adoption, Retention, and Task success"],
    ])},
    "ui/ux-design-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Funnel analysis (UX)", "Measures where users drop off across sequential steps toward a goal"],
    ])},
    "ui/ux-design-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Longitudinal UX study design", "Tracks user experience and behavior change over an extended time period"],
    ])},
    "ui/ux-design-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Competitive benchmarking (UX)", "Compares a product's usability against competitors on defined criteria"],
    ])},
    "ui/ux-design-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Design culture leadership", "Builds shared values and practices that raise design quality organization-wide"],
    ])},
    "ui/ux-design-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Design debt", "Accumulated inconsistencies and shortcuts in a product's design that slow future work"],
    ])},
    "ui/ux-design-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Design system adoption metrics", "Measures how widely and consistently teams use a shared design system"],
    ])},
    "ui/ux-design-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Regulatory UX writing", "Ensures interface text meets legal and compliance requirements clearly"],
    ])},
    "ui/ux-design-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Multi-channel content strategy", "Plans consistent messaging across web, app, email, and other touchpoints"],
    ])},
    "ui/ux-design-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Offline-first design", "Designs an app to remain usable and sync correctly without a network connection"],
    ])},
    "ui/ux-design-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Leadership portfolio review", "Evaluates a design leader's strategic impact, not just individual craft"],
    ])},
    "ui/ux-design-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Cognitive accessibility", "Designs interfaces that are easier to understand and use for neurodivergent users"],
    ])},
    "ui/ux-design-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Design system versioning", "Manages breaking changes and deprecation as a design system evolves"],
    ])},
    "ui/ux-design-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Biophilic design", "Incorporates nature-inspired patterns and elements into digital interface aesthetics"],
    ])},
    "ui/ux-design-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive typography", "Adjusts text size and contrast dynamically to support low-vision users"],
    ])},
    "ui/ux-design-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["B2B buyer persona research", "Characterizes the distinct needs of enterprise buyers versus end users"],
    ])},
    "ui/ux-design-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Multi-device continuity", "Lets a user resume a task seamlessly when switching between devices"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"ui/ux-design-m1-l{base_n}"
    worked_key = f"ui-ux-design-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["UI/UX Design"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json UI/UX Design: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 UI/UX Design lessons (completing 120/120).")


if __name__ == "__main__":
    main()
