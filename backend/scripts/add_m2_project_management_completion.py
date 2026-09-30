#!/usr/bin/env python3
"""Depth pass, M2 Project Management: fill in real, hand-checked
data_table content for the M2 Project Management lessons not covered
by the earlier breadth-first batch. Brings M2 Project Management to
full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning megaproject
theory and forecasting bias, quantitative risk analysis, portfolio
governance, team/leadership theory, sector-specific PM case studies,
emerging technology in PM, PM research methodology, contract and
finance theory, and organizational PM maturity; l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_project_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Optimism bias", "The systematic tendency for project planners to underestimate costs, schedules, and risks"],
    ["Reference class forecasting", "Estimates a project's outcome by comparing it against actual outcomes of a class of similar past projects"],
])

CHARTS: dict[str, dict] = {
    "project-management-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Agile scaling", "Extends agile practices from a single team to coordinate multiple teams working on a shared large program"],
        ["Advanced framework", "Frameworks like SAFe and LeSS address the coordination, dependency, and governance challenges of scaling agile"],
    ])},
    "project-management-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Project management capstone", "An applied culminating project demonstrating end-to-end project planning and delivery skill"],
        ["Deliverable", "Typically includes a project charter, risk analysis, schedule, and evaluation of a real or simulated project"],
    ])},
    "project-management-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Iron law of megaprojects", "Bent Flyvbjerg's finding that megaprojects are systematically over budget, over time, and under-benefit"],
        ["Megaproject research", "Documented across thousands of projects internationally, suggesting a structural rather than incidental pattern"],
    ])},
    "project-management-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Complexity theory", "Studies how systems with many interacting components exhibit emergent, hard-to-predict behavior"],
        ["Program governance application", "Recognizes that large programs behave more like complex adaptive systems than simple, fully plannable machines"],
    ])},
    "project-management-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Systems engineering V-model", "Structures a project as parallel decomposition (left side) and integration/verification (right side) phases"],
        ["Schedule integration", "Aligns detailed engineering milestones with the overall project schedule to synchronize design and verification"],
    ])},
    "project-management-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Econometric cost overrun modeling", "Statistically analyzes historical infrastructure project data to identify predictors of budget overruns"],
        ["Infrastructure application", "Reveals systematic factors (project type, size, procurement method) associated with larger cost overruns"],
    ])},
    "project-management-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Front-end loading", "Invests significant planning effort early in a capital project, before major spending commitments begin"],
        ["Capital project planning", "Higher upfront planning rigor is strongly associated with better cost and schedule outcomes for large capital projects"],
    ])},
    "project-management-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Design structure matrix", "A matrix-based tool mapping dependencies between a project's tasks or components"],
        ["Dependency mapping", "Reveals clusters of tightly coupled tasks that should be planned or executed together"],
    ])},
    "project-management-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Actor-network theory", "Treats both human and non-human elements (technologies, documents) as actors shaping a project's outcome"],
        ["Stakeholder analysis application", "Broadens stakeholder analysis to consider how tools and artifacts, not just people, influence project dynamics"],
    ])},
    "project-management-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Institutional isomorphism", "The tendency for organizations facing similar institutional pressures to adopt similar structures and practices"],
        ["Public infrastructure delivery", "Explains why public infrastructure projects across different agencies often converge on similar delivery models"],
    ])},
    "project-management-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Temporary organization", "A theoretical framing of projects as organizations deliberately created to exist only for a bounded duration"],
        ["Project theory", "Highlights how projects' temporariness shapes distinct dynamics around trust, learning, and coordination"],
    ])},
    "project-management-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian updating", "Revises a probability estimate as new evidence becomes available, using Bayes' theorem"],
        ["Project risk register application", "Risk likelihood and impact estimates should be systematically updated as a project progresses and new information emerges"],
    ])},
    "project-management-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Monte Carlo schedule simulation", "Runs many randomized simulations of task duration uncertainty to estimate a project's overall completion date distribution"],
        ["Schedule risk analysis", "Produces a probabilistic completion date range rather than a single deterministic estimate"],
    ])},
    "project-management-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Real options analysis", "Values managerial flexibility (e.g. the option to expand or delay) using option-pricing techniques"],
        ["Staged investment application", "Captures the value of phasing large investments to preserve the option to adjust as uncertainty resolves"],
    ])},
    "project-management-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Value-at-risk", "The maximum expected loss over a given time horizon at a specified confidence level"],
        ["Project portfolio application", "Quantifies the aggregate downside risk exposure across an organization's entire project portfolio"],
    ])},
    "project-management-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Fault tree analysis", "A top-down deductive method mapping the combinations of events that could lead to a defined failure"],
        ["Project failure mode application", "Systematically identifies the root causes and their logical combinations that could cause project failure"],
    ])},
    "project-management-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Six Sigma DMAIC", "A structured problem-solving methodology: Define, Measure, Analyze, Improve, Control"],
        ["Project governance integration", "Applies DMAIC's structured process improvement discipline to reduce variation in project delivery"],
    ])},
    "project-management-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Reference class forecasting methodology", "The specific step-by-step process for selecting a comparison class and adjusting a project estimate accordingly"],
        ["Application", "Requires identifying a sufficiently large and relevant reference class of comparable past projects"],
    ])},
    "project-management-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Copula", "A function that models the dependence structure between random variables separately from their individual marginal distributions"],
        ["Correlated risk modeling", "Captures how project risks (e.g. schedule and cost overruns) tend to move together rather than independently"],
    ])},
    "project-management-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Decision tree analysis", "Maps a sequence of decisions and uncertain outcomes as branches to evaluate the expected value of each path"],
        ["Contingent choice", "Well suited to project decisions where a later choice depends on the outcome of an earlier uncertain event"],
    ])},
    "project-management-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Resource-constrained project scheduling", "Schedules tasks accounting for limited shared resources, not just task dependencies"],
        ["Scheduling heuristic", "Since the exact optimization problem is computationally hard, practical heuristics find good, though not always optimal, schedules"],
    ])},
    "project-management-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Stage-gate governance", "Divides a project or portfolio into stages separated by formal review gates that approve continued investment"],
        ["Innovation portfolio application", "Allows an organization to kill or redirect underperforming innovation projects before further investment"],
    ])},
    "project-management-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Efficient frontier", "The set of portfolios offering the best possible expected return for each level of risk"],
        ["Portfolio selection application", "Applies portfolio theory to selecting a mix of projects that balances aggregate expected value against risk"],
    ])},
    "project-management-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Balanced scorecard", "A strategic framework tracking performance across financial, customer, process, and learning/growth perspectives"],
        ["Program strategy alignment", "Ensures individual program objectives are explicitly linked to and measured against overall organizational strategy"],
    ])},
    "project-management-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Benefits dependency network", "Maps how specific project outputs lead to enabling changes, which in turn produce intended business benefits"],
        ["Mapping application", "Makes explicit the causal chain assumed between delivering a project and realizing its intended value"],
    ])},
    "project-management-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Lean portfolio governance", "Applies lean principles to managing a portfolio of agile initiatives, emphasizing flow and minimizing waste"],
        ["Agile enterprise application", "Coordinates funding and prioritization decisions across many agile teams without reverting to heavyweight traditional governance"],
    ])},
    "project-management-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Analytic hierarchy process", "A structured technique for organizing and analyzing complex decisions using pairwise comparisons"],
        ["Project prioritization application", "Derives consistent relative priority scores for competing projects from a structured comparison process"],
    ])},
    "project-management-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic portfolio rebalancing", "Periodically reallocates resources among projects in a portfolio as circumstances and priorities change"],
        ["Application", "Keeps a portfolio aligned with evolving strategic priorities rather than locking in initial funding decisions permanently"],
    ])},
    "project-management-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Public-private partnership", "A long-term contractual arrangement between a government body and a private entity to deliver public infrastructure or services"],
        ["Governance structure", "Requires carefully designed risk allocation and oversight mechanisms across the public and private partners"],
    ])},
    "project-management-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Relational contract theory", "Emphasizes ongoing relationship and mutual adaptation over rigidly specifying every contingency in a contract upfront"],
        ["Alliance contracting application", "Underpins collaborative contracting models that share risk and reward among project partners"],
    ])},
    "project-management-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Distributed leadership", "Leadership functions are shared across multiple team members rather than concentrated in a single formal leader"],
        ["Virtual project team application", "Particularly relevant for geographically distributed teams where a single leader cannot maintain constant direct oversight"],
    ])},
    "project-management-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Psychological safety", "A shared belief that a team is safe for interpersonal risk-taking, such as admitting mistakes or raising concerns"],
        ["High-reliability team application", "Critical in high-stakes project teams where suppressing safety-relevant concerns can lead to catastrophic outcomes"],
    ])},
    "project-management-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Conflict resolution", "Structured approaches for addressing and resolving disagreements within a team"],
        ["Cross-cultural project team", "Must account for cultural differences in how conflict is expressed and appropriately addressed"],
    ])},
    "project-management-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Servant leadership", "A leadership philosophy prioritizing serving team members' growth and needs to enable their best performance"],
        ["Agile transformation application", "Aligns with agile values by positioning leaders as enablers and obstacle-removers rather than directive commanders"],
    ])},
    "project-management-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Trust formation", "The process by which team members come to rely on one another's reliability and good intentions"],
        ["Temporary multi-organization team", "Trust must form unusually quickly in project teams that lack the extended shared history of permanent organizations"],
    ])},
    "project-management-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Sensemaking theory", "Describes how individuals and groups construct meaning from ambiguous or unexpected events"],
        ["Project crisis response application", "Explains how project teams collectively interpret and respond to a sudden crisis or unexpected disruption"],
    ])},
    "project-management-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Emotional intelligence", "The capacity to recognize, understand, and manage one's own and others' emotions"],
        ["Program director competency", "A key leadership competency for managing stakeholder relationships and team dynamics under program-level pressure"],
    ])},
    "project-management-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Groupthink", "Cohesive groups suppress dissent and critical evaluation to preserve consensus and morale"],
        ["Steering committee mitigation", "Structured devil's-advocate roles and anonymous input channels help counteract groupthink in governance bodies"],
    ])},
    "project-management-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Institutional logics", "The underlying belief systems and norms that guide behavior within different types of organizations"],
        ["Cross-sector partnership conflict", "Public, private, and nonprofit partners often bring conflicting institutional logics that must be actively managed"],
    ])},
    "project-management-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Pharmaceutical R&D gate review", "A formal decision point evaluating whether a drug development project should proceed to the next costly phase"],
        ["Portfolio governance application", "Balances scientific promise against the escalating cost of failure at later development stages"],
    ])},
    "project-management-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Integrated project delivery", "A collaborative construction delivery method aligning all parties' interests through shared risk and reward"],
        ["Design-build comparison", "Contrasts with design-build's more sequential, single-point-of-responsibility delivery model"],
    ])},
    "project-management-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Earned value management", "Measures project performance by comparing planned, actual, and earned value of completed work"],
        ["Defense acquisition compliance", "Mandated on many government defense programs as a standardized cost and schedule performance reporting requirement"],
    ])},
    "project-management-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["IT project failure taxonomy", "A structured classification of the common recurring causes of information technology project failures"],
        ["Application", "Helps organizations diagnose and address systemic patterns rather than treating each IT failure as an isolated incident"],
    ])},
    "project-management-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Humanitarian logistics", "The specialized management of supply chains delivering aid in disaster or crisis response"],
        ["Project management application", "Requires extreme flexibility and speed given unpredictable, rapidly evolving humanitarian conditions"],
    ])},
    "project-management-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Film production scheduling", "Coordinates highly interdependent resources (cast, crew, locations) under tight, fixed timelines"],
        ["Scheduling model", "Must account for constraints unique to media production, like actor availability windows and location permits"],
    ])},
    "project-management-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Space mission lifecycle", "The formal phased process (concept, design, build, launch, operations) governing space project development"],
        ["Project management application", "Extremely high reliability requirements and irreversible failure modes shape a distinctively conservative project approach"],
    ])},
    "project-management-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Clinical trial project management", "Coordinates the complex, regulated process of testing a new treatment's safety and efficacy"],
        ["Milestone structure", "Organized around regulatory phases (I, II, III) with strict compliance and patient-safety requirements at each stage"],
    ])},
    "project-management-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Renewable energy infrastructure risk allocation", "Determines which project party bears specific risks like weather variability or grid connection delays"],
        ["Risk allocation practice", "Well-structured allocation assigns each risk to the party best able to manage or absorb it"],
    ])},
    "project-management-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Post-merger integration", "The structured process of combining two organizations' operations, systems, and cultures after an acquisition"],
        ["Program management application", "Treated as a large, time-critical program with distinct workstreams across every functional area of the business"],
    ])},
    "project-management-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["AI-augmented predictive scheduling", "Uses machine learning models to forecast schedule risk and likely delays based on historical project data"],
        ["Application", "Can flag high-risk tasks earlier than traditional manual schedule review"],
    ])},
    "project-management-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin", "A virtual, continuously updated model of a physical asset or process"],
        ["Construction monitoring application", "Enables real-time comparison of actual construction progress against the planned digital model"],
    ])},
    "project-management-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Smart contract", "Self-executing code deployed on a blockchain whose logic and state are enforced by the network"],
        ["Project payment application", "Can automatically release payments to contractors once verifiable milestone conditions are met"],
    ])},
    "project-management-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Machine learning cost overrun prediction", "Trains models on historical project data to forecast the likelihood and magnitude of future cost overruns"],
        ["Application", "Enables earlier, more targeted risk mitigation than relying solely on manual expert judgment"],
    ])},
    "project-management-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Network science of communication", "Analyzes a project team's communication patterns as a graph to identify structural bottlenecks"],
        ["Team application", "Can reveal isolated team members or overloaded communication hubs that risk becoming single points of failure"],
    ])},
    "project-management-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Sustainability-integrated PM standard", "Formal project management frameworks that explicitly incorporate environmental and social sustainability criteria"],
        ["Application", "Embeds sustainability considerations into project selection, planning, and evaluation rather than treating it as a separate concern"],
    ])},
    "project-management-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Circular economy", "An economic model minimizing waste by keeping resources in use through reuse, repair, and recycling"],
        ["Deliverable design application", "Applies circular principles to how a project's outputs are designed for eventual reuse or disassembly"],
    ])},
    "project-management-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Resilience engineering", "Designs systems and processes to adapt to and recover from unexpected disruptions"],
        ["Project risk management application", "Focuses on building adaptive capacity, not just preventing anticipated risks through predefined plans"],
    ])},
    "project-management-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge management system", "Captures, organizes, and makes accessible an organization's accumulated project experience"],
        ["Multi-project firm application", "Enables lessons from one project to systematically inform planning on future, unrelated projects"],
    ])},
    "project-management-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Text mining (post-mortems)", "Applies natural language processing to extract patterns from written project retrospective documents"],
        ["Lessons learned application", "Surfaces recurring themes across many post-mortems that manual review of individual documents would miss"],
    ])},
    "project-management-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Grounded theory", "A qualitative method that builds theory inductively from patterns discovered in the data itself"],
        ["PM research application", "Used to develop new theoretical frameworks explaining project phenomena directly from practitioner data"],
    ])},
    "project-management-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Case study methodology", "In-depth, contextualized examination of one or a few instances to generate rich understanding"],
        ["Megaproject analysis application", "Well suited to studying megaprojects, which are too few and too complex for large-sample statistical analysis"],
    ])},
    "project-management-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Mixed-methods research design", "Combines qualitative and quantitative approaches to draw on the strengths of both"],
        ["PM doctoral study application", "Common in project management doctoral research to triangulate statistical patterns with rich contextual explanation"],
    ])},
    "project-management-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Delphi method", "Iteratively collects and shares anonymous expert estimates across rounds, converging toward a group judgment"],
        ["Project risk consensus application", "Builds expert consensus on risk likelihood or impact without the social pressure dynamics of a face-to-face panel"],
    ])},
    "project-management-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Longitudinal study", "Tracks the same subjects (e.g. project teams) repeatedly over an extended period"],
        ["Team performance application", "Reveals how team performance evolves over a project's lifecycle rather than a single snapshot"],
    ])},
    "project-management-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Action research", "A cyclical research approach where practitioners study and improve their own practice through iterative intervention"],
        ["Practitioner-led PM study application", "Lets practicing project managers generate rigorous research insight directly from their own ongoing work"],
    ])},
    "project-management-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Bibliometric analysis", "Quantitatively analyzes patterns in academic publications, such as citation networks and topic trends"],
        ["PM literature application", "Reveals how the project management research field's focus areas have evolved over time"],
    ])},
    "project-management-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Structural equation modeling", "Models relationships among observed and latent variables, such as unobserved success factors driving observed outcomes"],
        ["Success factor research application", "Tests theoretical models of which underlying factors most strongly predict project success"],
    ])},
    "project-management-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Ethnographic method", "Immersive, in-context observation to understand a group's culture and practices from the inside"],
        ["Project culture application", "Reveals the informal norms and practices shaping a project team's actual day-to-day behavior"],
    ])},
    "project-management-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Meta-analysis", "Statistically pools effect estimates across multiple studies to produce a combined, more robust estimate"],
        ["Success criteria research application", "Synthesizes findings across many individual PM studies to identify consistently validated success predictors"],
    ])},
    "project-management-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Alliance contracting", "A collaborative contract structure where all parties share project risk and reward under a single agreement"],
        ["Pain-gain mechanism", "Adjusts each party's compensation based on whether the project performs better or worse than a target cost"],
    ])},
    "project-management-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["FIDIC contract", "A widely used international standard form of construction contract with defined risk allocation clauses"],
        ["Risk allocation clause", "Specifies which party bears responsibility for specific categories of risk during construction"],
    ])},
    "project-management-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Claims", "Formal requests for additional time or compensation due to circumstances beyond the contractor's control"],
        ["International dispute resolution", "Complex international contracts often specify arbitration mechanisms to resolve claims outside domestic courts"],
    ])},
    "project-management-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Target cost contract", "Sets an agreed target cost, with savings or overruns shared between client and contractor according to a formula"],
        ["Share mechanism", "Aligns incentives so the contractor benefits from finding cost efficiencies rather than maximizing billable costs"],
    ])},
    "project-management-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Vendor risk management", "Systematically assesses and mitigates risks posed by external suppliers in a project's supply chain"],
        ["Global supply chain application", "Increasingly important given the complexity and geographic dispersion of modern project supply chains"],
    ])},
    "project-management-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Intellectual property governance", "Establishes clear ownership and usage rights for IP generated during a collaborative project"],
        ["Collaborative R&D application", "Especially important in multi-partner research projects where IP ownership might otherwise be ambiguous"],
    ])},
    "project-management-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Force majeure clause", "A contract provision excusing performance failures caused by extraordinary events beyond a party's control"],
        ["Interpretation", "Courts and arbitrators must interpret whether a specific disruptive event qualifies as covered under the clause's language"],
    ])},
    "project-management-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Performance bond", "A financial guarantee ensuring a contractor completes a project according to contract terms"],
        ["Surety (construction)", "A third party guarantees the contractor's obligations, compensating the owner if the contractor defaults"],
    ])},
    "project-management-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Discounted cash flow sensitivity", "Tests how a project's valuation changes as key assumptions (discount rate, cash flow timing) are varied"],
        ["Capital appraisal application", "Reveals which assumptions most significantly affect the investment decision's outcome"],
    ])},
    "project-management-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Cost of capital", "The required rate of return needed to justify a capital investment"],
        ["Infrastructure finance estimation", "Accurately estimating this rate is essential to correctly evaluate whether an infrastructure project creates value"],
    ])},
    "project-management-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Public sector comparator", "A benchmark estimate of what a project would cost if delivered through traditional public procurement"],
        ["PPP value analysis", "Used to assess whether a public-private partnership genuinely offers better value than conventional delivery"],
    ])},
    "project-management-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Real exchange rate risk", "The risk that currency value changes will affect the real cost or return of a cross-border project"],
        ["Cross-border finance application", "Requires hedging or contractual mechanisms to manage exposure for internationally financed projects"],
    ])},
    "project-management-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Project finance", "Financing structured around a project's own cash flows and assets rather than the sponsor's general balance sheet"],
        ["Non-recourse debt", "Lenders can only claim the project's assets and cash flows, not the sponsoring company's other assets, if the project fails"],
    ])},
    "project-management-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Life-cycle costing", "Evaluates an asset's total cost including acquisition, operation, maintenance, and disposal, not just upfront price"],
        ["Asset-intensive decision application", "Prevents choosing a cheaper upfront option that turns out more expensive over the asset's full operating life"],
    ])},
    "project-management-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Tornado diagram", "A chart ranking input variables by how much they affect an output, showing the most sensitive variables at top"],
        ["Capital budgeting sensitivity application", "Quickly identifies which few assumptions matter most for a capital investment decision"],
    ])},
    "project-management-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Inflation-indexed contract pricing", "Adjusts contract payments automatically based on a specified inflation index"],
        ["Model", "Protects both parties from unpredictable cost erosion or windfall over a long-duration contract"],
    ])},
    "project-management-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Kanban flow metric", "Measures the rate and consistency of work items moving through a Kanban system, such as cycle time and throughput"],
        ["Enterprise program application", "Tracks the overall delivery flow health of a large program composed of many Kanban-managed teams"],
    ])},
    "project-management-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Theory of constraints", "Focuses improvement efforts on identifying and elevating a system's single most limiting bottleneck"],
        ["Multi-project application", "Applied to project environments to find the shared resource constraint limiting overall portfolio throughput"],
    ])},
    "project-management-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Complex project manager competency framework", "Defines the specific skills and behaviors required to successfully lead highly complex projects"],
        ["Application", "Goes beyond standard PM competencies to address the ambiguity and adaptive leadership complex projects demand"],
    ])},
    "project-management-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Crisis project management", "Adapts standard project management practices to the extreme uncertainty and urgency of a crisis response"],
        ["Pandemic response case", "Real-world pandemic projects illustrate rapid replanning and radically compressed decision cycles under crisis conditions"],
    ])},
    "project-management-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Ethical decision-making framework", "A structured process for reasoning through project decisions with genuine ethical trade-offs"],
        ["Project trade-off application", "Helps project leaders navigate conflicts between competing stakeholder interests systematically rather than ad hoc"],
    ])},
    "project-management-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Decision fatigue", "Declining decision quality after making many decisions, due to depleted cognitive resources"],
        ["Steering committee application", "Long governance meetings with many agenda items risk lower-quality decisions on later items"],
    ])},
    "project-management-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Systemic risk contagion", "The spread of risk or failure from one project to others sharing resources, dependencies, or organizational context"],
        ["Portfolio application", "A failure in one interdependent project can cascade to affect the performance of related projects in a portfolio"],
    ])},
    "project-management-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Digital PMO", "A project management office that uses integrated software and analytics to manage projects rather than manual reporting"],
        ["Analytics dashboard", "Provides real-time, data-driven visibility into portfolio health rather than relying on periodic manual status reports"],
    ])},
    "project-management-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Post-project review", "A structured evaluation conducted after a project's completion to capture what worked and what didn't"],
        ["Organizational learning loop", "Ensures lessons from completed projects are systematically fed back into how future projects are planned"],
    ])},
    "project-management-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Hofstede's cultural dimensions", "A framework characterizing cultures along dimensions like individualism and power distance"],
        ["Global rollout application", "Informs how project communication, decision authority, and change management should adapt across different cultural contexts"],
    ])},
    "project-management-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Agile-waterfall hybrid governance", "Combines agile execution flexibility with waterfall's formal milestone and compliance requirements"],
        ["Regulated industry application", "Common in regulated sectors that require formal documentation and approval gates alongside agile delivery"],
    ])},
    "project-management-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["GRI standards", "Global Reporting Initiative standards for reporting an organization's environmental, social, and governance impacts"],
        ["Project closeout integration", "Incorporates sustainability impact reporting as part of formal project completion and handover"],
    ])},
    "project-management-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Earned schedule method", "Extends earned value management to derive a schedule variance measured in time rather than cost units"],
        ["Completion forecasting", "Provides a more intuitive time-based forecast of project completion than traditional earned value schedule metrics"],
    ])},
    "project-management-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Organizational project management maturity model", "A structured framework assessing an organization's project management capability against progressive maturity levels"],
        ["Assessment framework", "Enables organizations to benchmark their PM practices and identify a roadmap for capability improvement"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Project Management"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"project-management-m2-l{base_n}"
        worked_key = f"project-management-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Project Management lessons.")


if __name__ == "__main__":
    main()
