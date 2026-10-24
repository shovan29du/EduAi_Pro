#!/usr/bin/env python3
"""Depth pass, M2 Health Education: fill in real, hand-checked
data_table content for the M2 Health Education lessons not covered by
the earlier breadth-first batch. Brings M2 Health Education to full
120/120 coverage.

Structure differs from most M2 subjects: l1-l100 are unique doctoral-
level topics spanning health science/epidemiology research methods,
behavior-change theory, program evaluation, global and public health,
and health technology/ethics; l101-l120 are "Independent Capstone"
lessons on 20 foundational health-education topics (Health Literacy,
Nutrition, Physical Activity, ... through Personal Health Planning)
that are NOT reuses of l1-l20 content -- their titles and content are
distinct introductory topics, so all 120 lessons get individually
authored data_table entries. l3 was already completed by an earlier
breadth-first batch, so it is left untouched here.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_health_education_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "health-education-m2-l1": {"data_table": table(["Concept", "Key Point"], [
        ["Advanced health science research", "Applies rigorous quantitative and qualitative methods to generate evidence for health policy and practice"],
        ["Epidemiology", "The study of disease distribution and determinants in populations, underpinning public health decision-making"],
    ])},
    "health-education-m2-l2": {"data_table": table(["Concept", "Key Point"], [
        ["Personal health", "Individual-level physical, mental, and social wellbeing, shaped by behavior, environment, and access to care"],
        ["Wellbeing research", "Graduate methods combine self-report measures with objective biomarkers to assess personal health outcomes"],
    ])},
    "health-education-m2-l4": {"data_table": table(["Concept", "Key Point"], [
        ["Systematic review", "A structured, reproducible synthesis of all available evidence on a defined research question"],
        ["Meta-analysis", "Statistically pools effect sizes from included studies to produce one combined, more precise estimate"],
    ])},
    "health-education-m2-l5": {"data_table": table(["Concept", "Key Point"], [
        ["Public health leadership", "Sets strategic direction and mobilizes resources across agencies to address population health priorities"],
        ["Management competencies", "Includes budgeting, workforce development, and coordinating multi-sector partnerships"],
    ])},
    "health-education-m2-l6": {"data_table": table(["Concept", "Key Point"], [
        ["Monitoring", "Ongoing tracking of program implementation indicators to ensure activities occur as planned"],
        ["Evaluation", "Periodic assessment of whether a program achieved its intended health outcomes"],
    ])},
    "health-education-m2-l7": {"data_table": table(["Concept", "Key Point"], [
        ["Research ethics", "Principles (respect for persons, beneficence, justice) governing the ethical conduct of human-subjects research"],
        ["Responsible conduct", "Includes informed consent, IRB oversight, data integrity, and honest reporting of results"],
    ])},
    "health-education-m2-l8": {"data_table": table(["Concept", "Key Point"], [
        ["Grant writing", "Crafting a compelling, methodologically sound proposal that matches a funder's priorities"],
        ["Research proposal", "Typically includes specific aims, significance, approach, and a feasible budget and timeline"],
    ])},
    "health-education-m2-l9": {"data_table": table(["Concept", "Key Point"], [
        ["Community-based participatory research", "Researchers and community members share power throughout the research process, from question-setting to dissemination"],
        ["Benefit", "Increases relevance and trust, improving both data quality and the likelihood interventions are adopted"],
    ])},
    "health-education-m2-l10": {"data_table": table(["Concept", "Key Point"], [
        ["Master's capstone", "An applied culminating project that demonstrates integration of health education theory, methods, and practice"],
        ["Deliverable", "Typically a needs assessment, program design, or evaluation plan addressing a real community health issue"],
    ])},
    "health-education-m2-l11": {"data_table": table(["Concept", "Key Point"], [
        ["Health Belief Model", "Predicts health behavior from perceived susceptibility, severity, benefits, and barriers"],
        ["Critique", "Omits social and environmental determinants, and its constructs can be difficult to operationalize consistently"],
    ])},
    "health-education-m2-l12": {"data_table": table(["Concept", "Key Point"], [
        ["Theory of Planned Behavior", "Behavior is predicted by intention, which is shaped by attitudes, subjective norms, and perceived behavioral control"],
        ["Application", "Widely used to design interventions targeting the specific belief driving low intention for a health behavior"],
    ])},
    "health-education-m2-l13": {"data_table": table(["Concept", "Key Point"], [
        ["Social Cognitive Theory", "Behavior, personal factors, and environment reciprocally influence one another"],
        ["Self-efficacy", "Confidence in one's ability to execute a behavior; a strong predictor of successful health behavior change"],
    ])},
    "health-education-m2-l14": {"data_table": table(["Concept", "Key Point"], [
        ["Transtheoretical Model", "Behavior change progresses through stages: precontemplation, contemplation, preparation, action, maintenance"],
        ["Application", "Interventions are tailored to an individual's current stage rather than assuming readiness for immediate action"],
    ])},
    "health-education-m2-l15": {"data_table": table(["Concept", "Key Point"], [
        ["Diffusion of Innovations", "New practices spread through a population via adopter categories: innovators, early adopters, early/late majority, laggards"],
        ["Public health practice", "Guides how to sequence dissemination strategies to accelerate adoption of a new health practice"],
    ])},
    "health-education-m2-l16": {"data_table": table(["Concept", "Key Point"], [
        ["Ecological model", "Frames health behavior as shaped by nested levels: individual, interpersonal, organizational, community, and policy"],
        ["Multilevel intervention", "Effective programs often target several levels simultaneously rather than the individual alone"],
    ])},
    "health-education-m2-l17": {"data_table": table(["Concept", "Key Point"], [
        ["PRECEDE-PROCEED", "A structured planning model that works backward from desired outcomes to identify contributing behavioral and environmental factors"],
        ["Program planning", "Guides needs assessment, intervention design, implementation, and evaluation as one integrated process"],
    ])},
    "health-education-m2-l18": {"data_table": table(["Concept", "Key Point"], [
        ["Community-based participatory research", "Applies the shared-power research model specifically to designing health education content and delivery"],
        ["Health education relevance", "Ensures curricula reflect the community's own language, priorities, and cultural context"],
    ])},
    "health-education-m2-l19": {"data_table": table(["Concept", "Key Point"], [
        ["Health literacy", "The capacity to obtain, process, and understand basic health information needed to make appropriate decisions"],
        ["Measurement", "Assessed via tools like the Newest Vital Sign; low literacy is linked to worse health outcomes"],
    ])},
    "health-education-m2-l20": {"data_table": table(["Concept", "Key Point"], [
        ["Social determinants of health", "Conditions in which people are born, grow, live, work, and age that shape health outcomes"],
        ["Theoretical framework", "The WHO Commission on Social Determinants links structural drivers to intermediary factors and health inequities"],
    ])},
    "health-education-m2-l21": {"data_table": table(["Concept", "Key Point"], [
        ["Health equity", "Everyone has a fair opportunity to attain their full health potential"],
        ["Health equality", "Providing everyone the same resources, which may not achieve equity if starting needs differ"],
    ])},
    "health-education-m2-l22": {"data_table": table(["Concept", "Key Point"], [
        ["Structural competency", "Trains health professionals to recognize how institutions and policies, not just individual behavior, shape patient health"],
        ["Curricular shift", "Moves health professional education beyond cultural competency toward addressing upstream structural causes"],
    ])},
    "health-education-m2-l23": {"data_table": table(["Concept", "Key Point"], [
        ["Epidemiological transition", "Describes a population's shift from infectious-disease mortality toward chronic, noncommunicable disease burden"],
        ["Implication", "Health systems must adapt resource allocation as a population moves through the transition"],
    ])},
    "health-education-m2-l24": {"data_table": table(["Concept", "Key Point"], [
        ["Syndemic theory", "Analyzes how two or more diseases cluster and interact within a population, amplified by social conditions"],
        ["Co-occurring conditions", "Addressing syndemics requires integrated interventions rather than treating each condition in isolation"],
    ])},
    "health-education-m2-l25": {"data_table": table(["Concept", "Key Point"], [
        ["Risk communication", "Conveys hazard information to the public in ways that support informed decisions during emergencies"],
        ["Public health emergency", "Effective messages are timely, transparent, and consistent to maintain public trust"],
    ])},
    "health-education-m2-l26": {"data_table": table(["Concept", "Key Point"], [
        ["Health communication campaign", "A planned, theory-driven effort to influence health knowledge, attitudes, or behavior in a target audience"],
        ["Evaluation", "Assessed through reach, message recall, attitude shift, and ultimately behavior change indicators"],
    ])},
    "health-education-m2-l27": {"data_table": table(["Concept", "Key Point"], [
        ["Social marketing", "Applies commercial marketing principles (product, price, place, promotion) to promote beneficial health behaviors"],
        ["Public health application", "Segments audiences and positions the desired behavior as delivering a tangible benefit to the target group"],
    ])},
    "health-education-m2-l28": {"data_table": table(["Concept", "Key Point"], [
        ["Nudge theory", "Alters the choice architecture to steer behavior in a beneficial direction without restricting options"],
        ["Health intervention", "Examples include default enrollment in wellness programs or placing healthier foods at eye level"],
    ])},
    "health-education-m2-l29": {"data_table": table(["Concept", "Key Point"], [
        ["Motivational interviewing", "A collaborative counseling style that elicits a client's own motivation for behavior change"],
        ["Evidence base", "Meta-analyses show consistent, moderate effects across substance use, diet, and adherence behaviors"],
    ])},
    "health-education-m2-l30": {"data_table": table(["Concept", "Key Point"], [
        ["Harm reduction", "Prioritizes reducing the negative consequences of risky behavior over requiring abstinence"],
        ["Substance use programs", "Includes needle exchange and supervised consumption sites as evidence-based harm reduction strategies"],
    ])},
    "health-education-m2-l31": {"data_table": table(["Concept", "Key Point"], [
        ["Vaccine hesitancy", "Delay or refusal of vaccination despite availability, driven by psychological and social factors"],
        ["Determinants", "Includes trust in institutions, perceived risk, social norms, and complacency about disease severity"],
    ])},
    "health-education-m2-l32": {"data_table": table(["Concept", "Key Point"], [
        ["Herd immunity threshold", "The proportion of a population that must be immune to interrupt sustained disease transmission"],
        ["Program design", "Threshold depends on a pathogen's basic reproduction number (R0); higher R0 requires higher coverage"],
    ])},
    "health-education-m2-l33": {"data_table": table(["Concept", "Key Point"], [
        ["Logic model", "Diagrams a program's inputs, activities, outputs, and outcomes to clarify its intended causal chain"],
        ["Theory of change", "Articulates the underlying assumptions about why and how a program is expected to produce its outcomes"],
    ])},
    "health-education-m2-l34": {"data_table": table(["Concept", "Key Point"], [
        ["Randomized controlled trial", "Randomly assigns participants to intervention or control to estimate a program's causal effect"],
        ["Health education research", "The gold standard for causal evaluation, though ethical and practical constraints often limit feasibility"],
    ])},
    "health-education-m2-l35": {"data_table": table(["Concept", "Key Point"], [
        ["Implementation science", "Studies methods to promote the systematic uptake of research findings into routine practice"],
        ["Frameworks", "Models like RE-AIM and CFIR structure evaluation of adoption, fidelity, and sustainability"],
    ])},
    "health-education-m2-l36": {"data_table": table(["Concept", "Key Point"], [
        ["Dissemination research", "Studies how to spread evidence-based interventions to broader audiences and settings"],
        ["Distinction from implementation", "Dissemination focuses on active spread of information; implementation focuses on adoption within a specific setting"],
    ])},
    "health-education-m2-l37": {"data_table": table(["Concept", "Key Point"], [
        ["School-based health education", "Curricula delivered within the school setting to build lifelong health knowledge and skills"],
        ["Curriculum design", "Effective programs are age-appropriate, skills-based, and integrated across multiple grade levels"],
    ])},
    "health-education-m2-l38": {"data_table": table(["Concept", "Key Point"], [
        ["Comprehensive sexuality education", "Covers a broad range of topics including consent, relationships, and reproductive health, not abstinence alone"],
        ["Evidence base", "Associated with delayed sexual initiation and increased contraceptive use compared with abstinence-only programs"],
    ])},
    "health-education-m2-l39": {"data_table": table(["Concept", "Key Point"], [
        ["Adolescent risk behavior surveillance", "Systematic monitoring of behaviors such as substance use and unsafe sex among youth populations"],
        ["Use", "Surveillance data guide the design and targeting of adolescent health education programs"],
    ])},
    "health-education-m2-l40": {"data_table": table(["Concept", "Key Point"], [
        ["Chronic disease self-management", "Equips patients with skills to manage their own condition day to day, alongside clinical care"],
        ["Health education role", "Structured programs improve self-efficacy and can reduce hospitalizations for chronic conditions"],
    ])},
    "health-education-m2-l41": {"data_table": table(["Concept", "Key Point"], [
        ["Diabetes self-management education", "Teaches blood glucose monitoring, diet, medication adherence, and complication prevention"],
        ["Program design", "Individualized education plans improve glycemic control more than generic printed materials"],
    ])},
    "health-education-m2-l42": {"data_table": table(["Concept", "Key Point"], [
        ["Cardiovascular risk reduction", "Targets modifiable risk factors: diet, physical activity, smoking, and blood pressure control"],
        ["Behavioral intervention", "Combining education with counseling and follow-up produces larger risk-factor reductions than education alone"],
    ])},
    "health-education-m2-l43": {"data_table": table(["Concept", "Key Point"], [
        ["Tobacco control policy", "Includes taxation, smoke-free laws, advertising restrictions, and cessation support"],
        ["Cessation program evaluation", "Combining counseling with pharmacotherapy roughly doubles quit rates compared with either alone"],
    ])},
    "health-education-m2-l44": {"data_table": table(["Concept", "Key Point"], [
        ["Nutrition education theory", "Draws on behavior-change models to explain why knowledge alone rarely changes dietary habits"],
        ["Dietary behavior change", "Effective programs address skills, environment, and motivation, not just nutrition facts"],
    ])},
    "health-education-m2-l45": {"data_table": table(["Concept", "Key Point"], [
        ["Physical activity promotion", "Encourages movement through both individual education and supportive environments"],
        ["Environmental and policy approaches", "Includes walkable infrastructure, safe parks, and workplace activity policies"],
    ])},
    "health-education-m2-l46": {"data_table": table(["Concept", "Key Point"], [
        ["Obesity prevention program", "Multi-component interventions targeting diet, activity, and environment across settings"],
        ["Evaluation", "Assessed via BMI trends, but also process measures like program reach and dietary/activity change"],
    ])},
    "health-education-m2-l47": {"data_table": table(["Concept", "Key Point"], [
        ["Mental health literacy", "Knowledge and beliefs about mental disorders that aid their recognition, management, and prevention"],
        ["Stigma reduction", "Contact-based education with people who have lived experience is among the most effective stigma-reduction strategies"],
    ])},
    "health-education-m2-l48": {"data_table": table(["Concept", "Key Point"], [
        ["Suicide prevention program", "Multi-level strategies spanning screening, gatekeeper training, and means restriction"],
        ["Evaluation framework", "Assessed via process indicators and, cautiously, longer-term outcome trends given rare-event statistical challenges"],
    ])},
    "health-education-m2-l49": {"data_table": table(["Concept", "Key Point"], [
        ["Trauma-informed approach", "Recognizes the widespread impact of trauma and avoids practices that could re-traumatize participants"],
        ["Health education application", "Builds safety, trustworthiness, and choice into program design and delivery"],
    ])},
    "health-education-m2-l50": {"data_table": table(["Concept", "Key Point"], [
        ["Emergency preparedness education", "Builds public knowledge and skills for responding to disasters and health emergencies"],
        ["Disaster preparedness", "Effective curricula combine risk communication with concrete, actionable preparedness steps"],
    ])},
    "health-education-m2-l51": {"data_table": table(["Concept", "Key Point"], [
        ["One Health framework", "Recognizes the interconnection between human, animal, and environmental health"],
        ["Application", "Guides integrated surveillance and response to zoonotic disease and environmental health threats"],
    ])},
    "health-education-m2-l52": {"data_table": table(["Concept", "Key Point"], [
        ["Global health governance", "The system of institutions, norms, and actors that coordinate cross-border health action"],
        ["World Health Organization", "Sets international health regulations and coordinates responses to global health emergencies"],
    ])},
    "health-education-m2-l53": {"data_table": table(["Concept", "Key Point"], [
        ["Universal health coverage", "Ensures all people access needed health services without financial hardship"],
        ["Policy design and financing", "Requires balancing service breadth, population coverage, and the share of costs covered"],
    ])},
    "health-education-m2-l54": {"data_table": table(["Concept", "Key Point"], [
        ["Maternal and child health program", "Targets outcomes across pregnancy, birth, and early childhood development"],
        ["Evaluation", "Tracked via indicators such as maternal mortality ratio and childhood immunization coverage"],
    ])},
    "health-education-m2-l55": {"data_table": table(["Concept", "Key Point"], [
        ["Reproductive health education", "Covers contraception, fertility, and reproductive rights across the life course"],
        ["Family planning programs", "Access to comprehensive contraceptive counseling reduces unintended pregnancy rates"],
    ])},
    "health-education-m2-l56": {"data_table": table(["Concept", "Key Point"], [
        ["STI prevention education", "Combines risk knowledge, testing access, and skills for safer sexual practices"],
        ["Program design", "Most effective when paired with accessible, low-barrier testing and treatment services"],
    ])},
    "health-education-m2-l57": {"data_table": table(["Concept", "Key Point"], [
        ["HIV prevention education", "Builds awareness of transmission routes and prevention options"],
        ["Combination prevention", "Layers behavioral, biomedical (e.g. PrEP), and structural strategies for greater effectiveness than any single approach"],
    ])},
    "health-education-m2-l58": {"data_table": table(["Concept", "Key Point"], [
        ["Outbreak communication", "Delivers timely, accurate information to the public during an infectious disease outbreak"],
        ["Strategy", "Balances transparency about uncertainty with clear, actionable guidance to maintain public trust"],
    ])},
    "health-education-m2-l59": {"data_table": table(["Concept", "Key Point"], [
        ["Antimicrobial resistance", "The evolution of pathogens that no longer respond to drugs that once controlled them"],
        ["Public health education strategy", "Promotes appropriate prescribing and completion of prescribed antimicrobial courses"],
    ])},
    "health-education-m2-l60": {"data_table": table(["Concept", "Key Point"], [
        ["Environmental health literacy", "Understanding of how environmental exposures affect health, enabling protective action"],
        ["Risk perception", "Public perception of environmental risk often diverges from measured exposure levels, complicating communication"],
    ])},
    "health-education-m2-l61": {"data_table": table(["Concept", "Key Point"], [
        ["Occupational health education", "Trains workers to recognize and avoid workplace hazards"],
        ["Workplace safety programs", "Combine hazard training with engineering and administrative controls to reduce injury rates"],
    ])},
    "health-education-m2-l62": {"data_table": table(["Concept", "Key Point"], [
        ["Culturally tailored intervention", "Adapts content, language, and delivery to the values and norms of a specific community"],
        ["Effectiveness", "Tailored interventions generally outperform generic programs in engagement and outcome measures"],
    ])},
    "health-education-m2-l63": {"data_table": table(["Concept", "Key Point"], [
        ["Health education for aging populations", "Addresses chronic disease management, fall prevention, and cognitive health"],
        ["Design consideration", "Must account for sensory, mobility, and health-literacy differences common among older adults"],
    ])},
    "health-education-m2-l64": {"data_table": table(["Concept", "Key Point"], [
        ["Genomic literacy", "Public understanding of genetic concepts needed to interpret personal genomic information"],
        ["Personalized medicine education", "Prepares both patients and providers to use genomic data in treatment decisions"],
    ])},
    "health-education-m2-l65": {"data_table": table(["Concept", "Key Point"], [
        ["Digital health literacy", "The ability to find, evaluate, and use health information from digital sources"],
        ["Telemedicine era", "Growing reliance on remote care makes digital literacy a determinant of care access"],
    ])},
    "health-education-m2-l66": {"data_table": table(["Concept", "Key Point"], [
        ["mHealth intervention", "Delivers health education or support via mobile devices and apps"],
        ["Design and evaluation", "Effectiveness depends on user engagement retention, which mHealth apps often struggle to sustain over time"],
    ])},
    "health-education-m2-l67": {"data_table": table(["Concept", "Key Point"], [
        ["Health misinformation on social media", "False or misleading health claims can spread faster than corrective information"],
        ["Implication", "Health educators increasingly need social-media-specific literacy and counter-messaging strategies"],
    ])},
    "health-education-m2-l68": {"data_table": table(["Concept", "Key Point"], [
        ["Program fidelity", "The degree to which a program is delivered as originally designed and intended"],
        ["Quality assurance", "Regular fidelity monitoring helps ensure outcome evaluations reflect the intervention as intended, not a diluted version"],
    ])},
    "health-education-m2-l69": {"data_table": table(["Concept", "Key Point"], [
        ["Health coaching", "A client-centered process supporting individuals in setting and achieving personal health goals"],
        ["Theoretical basis", "Draws on motivational interviewing and self-determination theory to sustain intrinsic motivation"],
    ])},
    "health-education-m2-l70": {"data_table": table(["Concept", "Key Point"], [
        ["Behavioral economics", "Studies systematic deviations from rational choice that affect health decisions"],
        ["Health policy application", "Default options and commitment devices can improve outcomes like retirement savings for health plans and screening uptake"],
    ])},
    "health-education-m2-l71": {"data_table": table(["Concept", "Key Point"], [
        ["Health insurance literacy", "Understanding of insurance terms and structures needed to select and use coverage effectively"],
        ["Consumer decision-making", "Low insurance literacy is linked to selecting plans poorly matched to actual healthcare needs"],
    ])},
    "health-education-m2-l72": {"data_table": table(["Concept", "Key Point"], [
        ["Food insecurity", "Limited or uncertain access to adequate food, closely linked to poor diet-related health outcomes"],
        ["Nutrition policy intervention", "Programs such as food assistance and school meals aim to reduce insecurity's health impact"],
    ])},
    "health-education-m2-l73": {"data_table": table(["Concept", "Key Point"], [
        ["Built environment", "The human-made surroundings, including infrastructure, that shape opportunities for physical activity"],
        ["Walkability research", "Neighborhoods with higher walkability are associated with greater physical activity and lower obesity rates"],
    ])},
    "health-education-m2-l74": {"data_table": table(["Concept", "Key Point"], [
        ["Green space access", "Availability of parks and natural areas within a community"],
        ["Population health outcomes", "Greater green space access is associated with better mental health and increased physical activity"],
    ])},
    "health-education-m2-l75": {"data_table": table(["Concept", "Key Point"], [
        ["Air quality health education", "Informs the public about pollution exposure and protective actions"],
        ["Risk communication", "Effective messaging translates technical air quality indices into clear, actionable guidance"],
    ])},
    "health-education-m2-l76": {"data_table": table(["Concept", "Key Point"], [
        ["Climate change health impact", "Includes heat-related illness, shifting infectious disease patterns, and food/water insecurity"],
        ["Adaptation education", "Prepares communities and health systems to anticipate and respond to climate-driven health risks"],
    ])},
    "health-education-m2-l77": {"data_table": table(["Concept", "Key Point"], [
        ["Water, sanitation, and hygiene (WASH)", "Access to clean water and sanitation is foundational to preventing infectious disease"],
        ["Education programs", "Hygiene education paired with infrastructure investment produces larger health gains than either alone"],
    ])},
    "health-education-m2-l78": {"data_table": table(["Concept", "Key Point"], [
        ["Health policy analysis", "Systematically examines how a policy is likely to affect health outcomes and stakeholders"],
        ["Agenda-setting theory", "Explains how certain health issues rise to political priority while others are overlooked"],
    ])},
    "health-education-m2-l79": {"data_table": table(["Concept", "Key Point"], [
        ["Social ecology of health promotion", "Frames interventions as operating across individual, interpersonal, and societal levels simultaneously"],
        ["Design implication", "Programs addressing only one level often see limited or unsustained impact"],
    ])},
    "health-education-m2-l80": {"data_table": table(["Concept", "Key Point"], [
        ["Health coalition", "A formal alliance of organizations working together toward a shared health goal"],
        ["Community mobilization", "Coalitions leverage diverse resources and legitimacy to sustain long-term health initiatives"],
    ])},
    "health-education-m2-l81": {"data_table": table(["Concept", "Key Point"], [
        ["Cultural competency training", "Prepares health professionals to provide effective care across diverse cultural backgrounds"],
        ["Health professions education", "Increasingly integrated as a required, longitudinal component rather than a single course"],
    ])},
    "health-education-m2-l82": {"data_table": table(["Concept", "Key Point"], [
        ["Implicit bias training", "Aims to raise awareness of unconscious biases that can affect clinical decision-making"],
        ["Healthcare delivery", "Evidence on training's effect on actual patient outcomes remains mixed and is an active research area"],
    ])},
    "health-education-m2-l83": {"data_table": table(["Concept", "Key Point"], [
        ["Informed consent", "Ensures patients understand and voluntarily agree to a procedure or study before it proceeds"],
        ["Health literacy ethics", "Consent is only meaningfully informed if information is communicated at a comprehensible literacy level"],
    ])},
    "health-education-m2-l84": {"data_table": table(["Concept", "Key Point"], [
        ["Bioethics", "Examines the moral dimensions of health interventions, including autonomy, beneficence, and justice"],
        ["Public health intervention design", "Population-level measures can create tension between individual liberty and collective benefit"],
    ])},
    "health-education-m2-l85": {"data_table": table(["Concept", "Key Point"], [
        ["Quarantine and isolation policy", "Restricts movement of exposed or infected individuals to limit disease spread"],
        ["Ethical considerations", "Must balance public health protection against restrictions on individual liberty, requiring due process safeguards"],
    ])},
    "health-education-m2-l86": {"data_table": table(["Concept", "Key Point"], [
        ["Pandemic preparedness curriculum", "Trains health professionals and the public in coordinated outbreak response"],
        ["Design", "Combines technical epidemiological content with risk communication and ethics training"],
    ])},
    "health-education-m2-l87": {"data_table": table(["Concept", "Key Point"], [
        ["Serious games", "Games designed primarily for educational or training purposes rather than entertainment"],
        ["Health education technology", "Used to build health knowledge and skills through interactive simulation"],
    ])},
    "health-education-m2-l88": {"data_table": table(["Concept", "Key Point"], [
        ["Virtual reality applications", "Immersive simulations used to practice health behaviors or clinical skills in a controlled setting"],
        ["Behavior training", "Shows promise for exposure-based and procedural training where real-world practice is costly or risky"],
    ])},
    "health-education-m2-l89": {"data_table": table(["Concept", "Key Point"], [
        ["Community resilience", "A community's capacity to withstand and recover from a public health emergency"],
        ["Emergency recovery", "Resilient communities combine strong social networks with pre-established emergency infrastructure"],
    ])},
    "health-education-m2-l90": {"data_table": table(["Concept", "Key Point"], [
        ["Health education workforce development", "Builds the pipeline of trained professionals to deliver health education programs"],
        ["Certification", "Credentialing (e.g. Certified Health Education Specialist) standardizes competencies across the field"],
    ])},
    "health-education-m2-l91": {"data_table": table(["Concept", "Key Point"], [
        ["Certification standards evaluation", "Assesses whether credentialing exams and requirements actually predict effective practice"],
        ["Quality implication", "Robust standards protect program quality but must be periodically updated as the field evolves"],
    ])},
    "health-education-m2-l92": {"data_table": table(["Concept", "Key Point"], [
        ["Cross-cultural adaptation", "Modifies health education materials for linguistic and cultural appropriateness in a new population"],
        ["Process", "Involves translation, back-translation, and community review to preserve meaning and relevance"],
    ])},
    "health-education-m2-l93": {"data_table": table(["Concept", "Key Point"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to health education research"],
        ["Original contribution", "Requires identifying a genuine gap in the existing evidence base and proposing a novel, testable resolution"],
    ])},
    "health-education-m2-l94": {"data_table": table(["Concept", "Key Point"], [
        ["Precision public health", "Uses genomic and other multi-omic data to target interventions to the subgroups most likely to benefit"],
        ["Targeted intervention", "Moves beyond one-size-fits-all public health messaging toward stratified, evidence-based targeting"],
    ])},
    "health-education-m2-l95": {"data_table": table(["Concept", "Key Point"], [
        ["Refugee and displaced population health education", "Addresses unique barriers including trauma, language, and disrupted access to care"],
        ["Program design", "Requires trauma-informed, culturally responsive, and often mobile or temporary delivery models"],
    ])},
    "health-education-m2-l96": {"data_table": table(["Concept", "Key Point"], [
        ["Peer-led health education", "Trained community members deliver health content to their own peer group"],
        ["Efficacy evidence", "Peer-led models can increase trust and relevance, particularly effective among adolescents and marginalized groups"],
    ])},
    "health-education-m2-l97": {"data_table": table(["Concept", "Key Point"], [
        ["Citizen science", "Engages members of the public in collecting or analyzing health-relevant data"],
        ["Community health surveillance", "Expands surveillance capacity and builds community ownership of local health data"],
    ])},
    "health-education-m2-l98": {"data_table": table(["Concept", "Key Point"], [
        ["Planetary health education", "Frames human health as inseparable from the health of Earth's natural systems"],
        ["Ecosystem-wellbeing link", "Curricula connect biodiversity loss and environmental degradation to downstream human health impacts"],
    ])},
    "health-education-m2-l99": {"data_table": table(["Concept", "Key Point"], [
        ["Sleep health education", "Builds public understanding of sleep's role in physical and mental health"],
        ["Circadian-informed curricula", "Incorporates circadian rhythm science into school and workplace health education timing and content"],
    ])},
    "health-education-m2-l100": {"data_table": table(["Concept", "Key Point"], [
        ["Menstrual health education", "Covers biological, hygienic, and social aspects of menstruation"],
        ["Policy and program design", "Effective programs pair education with access to menstrual products and stigma-reduction efforts"],
    ])},
    "health-education-m2-l101": {"data_table": table(["Concept", "Key Point"], [
        ["Health literacy", "The capacity to find, understand, and act on basic health information"],
        ["Practical impact", "Low health literacy is associated with poorer medication adherence and higher hospitalization rates"],
    ])},
    "health-education-m2-l102": {"data_table": table(["Concept", "Key Point"], [
        ["Nutrition", "The intake and use of food to support growth, energy, and health"],
        ["Balanced diet", "Adequate intake across macronutrients and micronutrients supports long-term health and disease prevention"],
    ])},
    "health-education-m2-l103": {"data_table": table(["Concept", "Key Point"], [
        ["Physical activity", "Any bodily movement that expends energy, ranging from daily tasks to structured exercise"],
        ["Recommended guideline", "Most health authorities recommend at least 150 minutes of moderate activity per week for adults"],
    ])},
    "health-education-m2-l104": {"data_table": table(["Concept", "Key Point"], [
        ["Sleep science", "Studies the physiological stages and functions of sleep in restoring the body and brain"],
        ["Health relevance", "Chronic sleep deprivation is linked to impaired cognition, weight gain, and cardiovascular risk"],
    ])},
    "health-education-m2-l105": {"data_table": table(["Concept", "Key Point"], [
        ["Mental wellbeing", "A state encompassing emotional stability, coping ability, and a sense of purpose"],
        ["Protective factors", "Social connection, physical activity, and adequate sleep all support mental wellbeing"],
    ])},
    "health-education-m2-l106": {"data_table": table(["Concept", "Key Point"], [
        ["Stress management", "Techniques to reduce and cope with the physiological and psychological effects of stress"],
        ["Common techniques", "Includes deep breathing, physical activity, time management, and social support"],
    ])},
    "health-education-m2-l107": {"data_table": table(["Concept", "Key Point"], [
        ["Sexual and reproductive health", "Encompasses physical, emotional, and social wellbeing related to sexuality and reproduction"],
        ["Core components", "Includes access to contraception, STI prevention, and comprehensive, accurate education"],
    ])},
    "health-education-m2-l108": {"data_table": table(["Concept", "Key Point"], [
        ["Communicable disease", "An illness caused by an infectious agent that can spread from person to person"],
        ["Prevention", "Vaccination, hygiene, and prompt treatment are core strategies for limiting transmission"],
    ])},
    "health-education-m2-l109": {"data_table": table(["Concept", "Key Point"], [
        ["Noncommunicable disease", "A chronic condition, such as heart disease or diabetes, that is not transmitted between people"],
        ["Risk factors", "Largely driven by diet, physical inactivity, tobacco use, and alcohol consumption"],
    ])},
    "health-education-m2-l110": {"data_table": table(["Concept", "Key Point"], [
        ["Medicines", "Substances used to prevent, treat, or manage disease and its symptoms"],
        ["Vaccines", "Biological preparations that train the immune system to recognize and fight specific pathogens"],
    ])},
    "health-education-m2-l111": {"data_table": table(["Concept", "Key Point"], [
        ["Substance-use prevention", "Programs that build knowledge, skills, and social support to reduce the risk of substance misuse"],
        ["Effective approach", "Skills-based programs addressing peer pressure outperform purely fact-based drug education"],
    ])},
    "health-education-m2-l112": {"data_table": table(["Concept", "Key Point"], [
        ["First aid", "Immediate care given to an injured or ill person before professional medical help arrives"],
        ["Core skills", "Includes assessing responsiveness, controlling bleeding, and performing CPR when needed"],
    ])},
    "health-education-m2-l113": {"data_table": table(["Concept", "Key Point"], [
        ["Injury prevention", "Strategies that reduce the likelihood or severity of unintentional injuries"],
        ["Common approaches", "Includes safety equipment use, environmental modification, and behavior-focused education"],
    ])},
    "health-education-m2-l114": {"data_table": table(["Concept", "Key Point"], [
        ["Environmental health", "The study of how environmental factors affect human health"],
        ["Key exposures", "Air and water quality, chemical exposure, and sanitation all directly influence health outcomes"],
    ])},
    "health-education-m2-l115": {"data_table": table(["Concept", "Key Point"], [
        ["Workplace health", "Programs and conditions that support employee physical and mental wellbeing"],
        ["Common elements", "Ergonomic design, safety training, and access to wellness resources"],
    ])},
    "health-education-m2-l116": {"data_table": table(["Concept", "Key Point"], [
        ["Public health system", "The organizations, policies, and resources that work together to protect and improve population health"],
        ["Core functions", "Assessment, policy development, and assurance form the classic three core public health functions"],
    ])},
    "health-education-m2-l117": {"data_table": table(["Concept", "Key Point"], [
        ["Health inequality", "Measurable differences in health outcomes between population groups"],
        ["Contributing factors", "Income, education, geography, and access to care all contribute to observed disparities"],
    ])},
    "health-education-m2-l118": {"data_table": table(["Concept", "Key Point"], [
        ["Digital health", "The use of technology, such as apps and telemedicine, to support health monitoring and care"],
        ["Growing role", "Digital tools expand access but also raise new questions about equity and data privacy"],
    ])},
    "health-education-m2-l119": {"data_table": table(["Concept", "Key Point"], [
        ["Healthcare decision-making", "The process of choosing among treatment or care options based on evidence and personal values"],
        ["Shared decision-making", "Involves patients as active participants alongside clinicians in weighing risks and benefits"],
    ])},
    "health-education-m2-l120": {"data_table": table(["Concept", "Key Point"], [
        ["Personal health planning", "Setting individualized goals and strategies for maintaining and improving one's own health"],
        ["Key components", "Combines self-assessment, goal-setting, and periodic review of progress toward health goals"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Health Education"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Health Education lessons.")


if __name__ == "__main__":
    main()
