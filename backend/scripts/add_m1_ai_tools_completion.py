#!/usr/bin/env python3
"""Depth pass, M1 AI Tools: fill in real, hand-checked data_table
content for the 119 M1 AI Tools lessons not covered by the earlier
breadth-first batch. Brings M1 AI Tools to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
enterprise AI orchestration and agent frameworks, LLMOps tooling
(evaluation, fine-tuning, guardrails), and applied AI tools across a
wide range of professional and industry domains; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls
within l1-l20, so it is also reused for l103).

This is the final subject of the M1 (Masters Year 1) depth pass,
completing 53/53 subjects at this level.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_ai_tools_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Component", "Role"], [
    ["Planner", "Decides the sequence of actions to take"],
    ["Executor", "Carries out the chosen actions/tool calls"],
    ["Memory", "Stores context across steps"],
])

CHARTS: dict[str, dict] = {
    "ai-tools-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["AI-powered workflow", "Chains AI tool calls together to automate a multi-step task"],
    ])},
    "ai-tools-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tool integration", "Combines several AI services into one coherent working pipeline"],
    ])},
    "ai-tools-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["AI forecasting tools", "Use models to project future business metrics from historical data"],
    ])},
    "ai-tools-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise evaluation framework", "Systematically compares AI models against business-specific success criteria"],
    ])},
    "ai-tools-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise creative operations", "Uses AI tools to scale content production while maintaining brand quality"],
    ])},
    "ai-tools-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["Advanced RAG architecture", "Combines retrieval and generation with re-ranking and multi-hop lookups"],
    ])},
    "ai-tools-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["AI-assisted systems engineering", "Uses AI tools to support requirements analysis and system design work"],
    ])},
    "ai-tools-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Quantitative investment AI tools", "Apply AI models to analyze financial data and inform investment decisions"],
    ])},
    "ai-tools-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["Multi-agent enterprise orchestration", "Coordinates several specialized AI agents to complete a business process"],
    ])},
    "ai-tools-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Media production pipeline", "Chains AI tools for generating, editing, and finalizing media content"],
    ])},
    "ai-tools-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["AI governance framework", "Establishes oversight and accountability for how an organization deploys AI"],
    ])},
    "ai-tools-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise portfolio AI strategy", "Uses AI tools to inform decisions across a company's project portfolio"],
    ])},
    "ai-tools-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Resilient AI integration", "Designs AI tool integrations to degrade gracefully rather than fail completely"],
    ])},
    "ai-tools-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Organizational knowledge management (AI)", "Uses AI tools to capture, search, and surface institutional knowledge"],
    ])},
    "ai-tools-m1-l16": {"data_table": table(["Term", "Meaning"], [
        ["Code generation research frontiers", "Tracks emerging techniques improving AI-assisted software development"],
    ])},
    "ai-tools-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Research synthesis tools", "Use AI to summarize and connect findings across many research sources"],
    ])},
    "ai-tools-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise AI automation strategy", "Plans organization-wide adoption of AI to automate repetitive workflows"],
    ])},
    "ai-tools-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Global regulatory AI strategy", "Navigates varying international AI regulation when deploying tools globally"],
    ])},
    "ai-tools-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Capstone AI-tools project", "Integrates multiple AI tools into one working end-to-end application"],
    ])},
    "ai-tools-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Vector database selection", "Chooses a vector store based on scale, latency, and filtering needs for retrieval"],
    ])},
    "ai-tools-m1-l22": {"data_table": table(["Pattern", "Feature"], [
        ["Chain-of-thought", "Prompts a model to generate intermediate reasoning steps before an answer"],
        ["Self-consistency", "Samples multiple reasoning paths and takes the most common final answer"],
    ])},
    "ai-tools-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["Function calling / tool-use API", "Lets a model choose to invoke a defined external function with structured arguments"],
    ])},
    "ai-tools-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["LangChain", "A framework for composing LLM calls, tools, and memory into pipelines"],
    ])},
    "ai-tools-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["LlamaIndex", "A framework for connecting LLMs to structured and unstructured data for retrieval"],
    ])},
    "ai-tools-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["AutoGen", "A framework for building multi-agent conversations that collaborate on tasks"],
    ])},
    "ai-tools-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["CrewAI", "A framework that orchestrates agents with defined roles working as a team"],
    ])},
    "ai-tools-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Semantic Kernel", "Microsoft's framework for integrating LLMs into enterprise applications"],
    ])},
    "ai-tools-m1-l29": {"data_table": table(["Term", "Meaning"], [
        ["Guardrails / output validation", "Enforces structural and safety constraints on a model's generated output"],
    ])},
    "ai-tools-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Evaluation harness", "Automates running a model against benchmark tasks and scoring the results"],
    ])},
    "ai-tools-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["LoRA / QLoRA", "Efficiently fine-tunes a large model by training small low-rank adapter weights"],
    ])},
    "ai-tools-m1-l32": {"data_table": table(["Term", "Meaning"], [
        ["Model quantization", "Reduces numeric precision of weights to shrink a model for edge deployment"],
    ])},
    "ai-tools-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Hallucination detection tooling", "Automatically flags model outputs likely to contain fabricated claims"],
    ])},
    "ai-tools-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Prompt injection defense", "Detects and blocks malicious instructions embedded within model input"],
    ])},
    "ai-tools-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["Data labeling/annotation tools", "Support humans (or AI) in producing labeled data for model training"],
    ])},
    "ai-tools-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["A/B testing generative outputs", "Compares two prompt or model variants on real usage to measure quality"],
    ])},
    "ai-tools-m1-l37": {"data_table": table(["Term", "Meaning"], [
        ["Token budget monitoring", "Tracks and controls API token usage to manage LLM operating costs"],
    ])},
    "ai-tools-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Latency optimization (LLM serving)", "Reduces response time for production language model deployments"],
    ])},
    "ai-tools-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Legal contract review tools", "Use AI to extract and flag key clauses from legal documents automatically"],
    ])},
    "ai-tools-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Compliance monitoring tools", "Use AI to continuously check regulated-industry activity against requirements"],
    ])},
    "ai-tools-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Fraud pattern detection tools", "Use AI to flag unusual financial transaction patterns"],
    ])},
    "ai-tools-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Cybersecurity threat hunting tools", "Use AI to proactively surface suspicious activity in security data"],
    ])},
    "ai-tools-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["Literature review automation", "Uses AI to summarize and synthesize findings across scientific papers"],
    ])},
    "ai-tools-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Drug candidate screening tools", "Use AI to predict promising molecular candidates for drug development"],
    ])},
    "ai-tools-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Climate scenario modeling tools", "Use AI to simulate and analyze possible future climate outcomes"],
    ])},
    "ai-tools-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive learning path tools", "Personalize educational content sequencing to an individual learner's progress"],
    ])},
    "ai-tools-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Resume screening tools", "Use AI to filter and rank job applicants against role requirements"],
    ])},
    "ai-tools-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Demand sensing tools", "Use AI to detect near-real-time shifts in supply chain demand signals"],
    ])},
    "ai-tools-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Support ticket triage tools", "Use AI to categorize and route customer service requests automatically"],
    ])},
    "ai-tools-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Sales pipeline forecasting tools", "Use AI to predict deal outcomes and revenue from CRM data"],
    ])},
    "ai-tools-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["UX wireframe generation tools", "Use AI to quickly produce interface layout drafts from a text description"],
    ])},
    "ai-tools-m1-l52": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge graph construction tools", "Use AI to automatically extract entities and relationships into a graph"],
    ])},
    "ai-tools-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Aspect-based sentiment analysis", "Identifies sentiment toward specific attributes within a piece of text"],
    ])},
    "ai-tools-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Personal financial advisory automation", "Uses AI to generate personalized financial guidance at scale"],
    ])},
    "ai-tools-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Real estate valuation modeling", "Uses AI to estimate property values from comparable sales and features"],
    ])},
    "ai-tools-m1-l56": {"data_table": table(["Term", "Meaning"], [
        ["Insurance underwriting automation", "Uses AI to assess risk and price policies more efficiently"],
    ])},
    "ai-tools-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Legal e-discovery review", "Uses AI to efficiently identify relevant documents in litigation"],
    ])},
    "ai-tools-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Patent prior art search", "Uses AI to find existing patents relevant to a new invention"],
    ])},
    "ai-tools-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["Academic peer review assistance", "Uses AI to help reviewers assess manuscript quality and flag issues"],
    ])},
    "ai-tools-m1-l60": {"data_table": table(["Term", "Meaning"], [
        ["Scientific figure generation", "Uses AI to produce charts and diagrams for research publications"],
    ])},
    "ai-tools-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Robotics control interface design", "Uses AI to translate high-level commands into robot control signals"],
    ])},
    "ai-tools-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Autonomous vehicle scenario simulation", "Uses AI to generate and test edge-case driving scenarios safely"],
    ])},
    "ai-tools-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Red team adversarial testing", "Deliberately probes an AI system for failure modes before deployment"],
    ])},
    "ai-tools-m1-l64": {"data_table": table(["Metric", "Measures"], [
        ["Recall@k", "Whether relevant documents appear in the top-k retrieved results"],
    ])},
    "ai-tools-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Multi-modal content pipeline", "Chains AI tools generating text, image, and audio into one output"],
    ])},
    "ai-tools-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Automated captioning", "Uses AI to generate accessible text descriptions for audio and video content"],
    ])},
    "ai-tools-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive language learning platforms", "Use AI to adjust lesson difficulty to a learner's demonstrated proficiency"],
    ])},
    "ai-tools-m1-l68": {"data_table": table(["Term", "Meaning"], [
        ["Elder care monitoring systems", "Use AI to detect falls or health changes from sensor data"],
    ])},
    "ai-tools-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["Agricultural yield prediction", "Uses AI to forecast crop output from satellite and weather data"],
    ])},
    "ai-tools-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Energy grid load balancing", "Uses AI to optimize electricity distribution against fluctuating demand"],
    ])},
    "ai-tools-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Warehouse robotics coordination", "Uses AI to schedule and route robots efficiently within a warehouse"],
    ])},
    "ai-tools-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Retail inventory forecasting", "Uses AI to predict stock needs and reduce overstock or stockouts"],
    ])},
    "ai-tools-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Personalized marketing generation", "Uses AI to tailor campaign content to individual customer segments"],
    ])},
    "ai-tools-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Brand voice consistency auditing", "Uses AI to check generated content matches a brand's defined tone"],
    ])},
    "ai-tools-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Crisis communication drafting", "Uses AI to quickly generate accurate, sensitive messaging during a crisis"],
    ])},
    "ai-tools-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Public policy impact simulation", "Uses AI to model likely outcomes of proposed policy changes"],
    ])},
    "ai-tools-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Journalistic fact-checking pipelines", "Use AI to verify claims against trusted sources at speed"],
    ])},
    "ai-tools-m1-l78": {"data_table": table(["Term", "Meaning"], [
        ["Cross-lingual semantic search", "Retrieves relevant results across languages by matching meaning, not exact words"],
    ])},
    "ai-tools-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Voice assistant dialogue design", "Uses AI tools to script natural, effective spoken interactions"],
    ])},
    "ai-tools-m1-l80": {"data_table": table(["Term", "Meaning"], [
        ["AR/VR content generation", "Uses AI to produce immersive 3D assets and environments"],
    ])},
    "ai-tools-m1-l81": {"data_table": table(["Term", "Meaning"], [
        ["Procedural game content generation", "Uses AI to algorithmically generate levels, items, or narrative content"],
    ])},
    "ai-tools-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Automated music mastering", "Uses AI to apply final audio processing to a music track"],
    ])},
    "ai-tools-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Film rough-cut editing assistance", "Uses AI to suggest initial cuts and pacing from raw footage"],
    ])},
    "ai-tools-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Storyboard generation", "Uses AI to visualize a script's scenes as sequential draft images"],
    ])},
    "ai-tools-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Architectural rendering automation", "Uses AI to produce realistic visualizations from building design specs"],
    ])},
    "ai-tools-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Fashion trend forecasting", "Uses AI to predict upcoming style trends from social and sales data"],
    ])},
    "ai-tools-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Vendor evaluation framework", "Systematically compares third-party AI vendors against enterprise requirements"],
    ])},
    "ai-tools-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Third-party AI security auditing", "Reviews external AI tool integrations for data exposure and vulnerability risk"],
    ])},
    "ai-tools-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Data governance compliance (AI deployment)", "Ensures AI tools handle data according to regulatory requirements"],
    ])},
    "ai-tools-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Voice cloning ethical safeguards", "Adds consent and misuse-prevention controls to voice synthesis tools"],
    ])},
    "ai-tools-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Podcast production automation", "Uses AI to assist with editing, show notes, and transcription for podcasts"],
    ])},
    "ai-tools-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Meeting transcription/action-items", "Uses AI to transcribe meetings and extract follow-up tasks automatically"],
    ])},
    "ai-tools-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Model Context Protocol", "A standard for connecting AI models to external tools and data sources uniformly"],
    ])},
    "ai-tools-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Wildfire risk prediction tools", "Use AI to forecast fire risk from weather, vegetation, and terrain data"],
    ])},
    "ai-tools-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Museum digitization/metadata tagging", "Uses AI to catalog and describe collection items at scale"],
    ])},
    "ai-tools-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Judicial risk assessment auditing", "Reviews AI-based sentencing tools for fairness and bias"],
    ])},
    "ai-tools-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Semiconductor design verification", "Uses AI to help verify chip designs meet their specifications"],
    ])},
    "ai-tools-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["Wildlife camera trap species ID", "Uses AI image recognition to automatically identify animal species"],
    ])},
    "ai-tools-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Rehearsal scheduling optimization", "Uses AI to coordinate complex live-performance scheduling constraints"],
    ])},
    "ai-tools-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Cold chain anomaly detection", "Uses AI to flag temperature or handling deviations in perishable logistics"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"ai-tools-m1-l{base_n}"
    worked_key = f"ai-tools-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["AI Tools"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json AI Tools: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 AI Tools lessons (completing 120/120).")


if __name__ == "__main__":
    main()
