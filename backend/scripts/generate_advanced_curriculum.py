#!/usr/bin/env python3
"""Generate syllabus JSON files for the college / undergraduate / master's levels
(C1, C2, UG1, UG2, UG3, UG4, M1, M2).

Produces backend/syllabus/level_<id>.json for each level, in the same shape as the
existing backend/syllabus/gradeN.json files (``{"level": "C1", "subjects": {...}}``)
so the existing frontend components (SubjectLessons, BookList, MediaSection, ...)
and resource schema work unchanged.

Re-run this script any time the topic ladders below are edited:

    python3 backend/scripts/generate_advanced_curriculum.py
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"

LEVEL_IDS = ["C1", "C2", "UG1", "UG2", "UG3", "UG4", "M1", "M2"]

LEVEL_LABELS = {
    "C1": "College Level 1",
    "C2": "College Level 2",
    "UG1": "Undergraduate Year 1",
    "UG2": "Undergraduate Year 2",
    "UG3": "Undergraduate Year 3",
    "UG4": "Undergraduate Year 4",
    "M1": "Master's Year 1",
    "M2": "Master's Year 2",
}

DIFFICULTY_BY_LEVEL = {
    "C1": "college-introductory",
    "C2": "college-intermediate",
    "UG1": "undergraduate-foundational",
    "UG2": "undergraduate-intermediate",
    "UG3": "undergraduate-advanced",
    "UG4": "undergraduate-capstone",
    "M1": "graduate-core",
    "M2": "graduate-advanced",
}

DEPTH_ADJECTIVE = {
    "C1": "an introductory",
    "C2": "an intermediate college-level",
    "UG1": "a foundational undergraduate",
    "UG2": "an applied undergraduate",
    "UG3": "an advanced undergraduate",
    "UG4": "a capstone-level undergraduate",
    "M1": "a graduate-core",
    "M2": "an advanced graduate/research-level",
}

TIME_BY_LEVEL = {
    "C1": 45, "C2": 50, "UG1": 55, "UG2": 60, "UG3": 65, "UG4": 70, "M1": 80, "M2": 90,
}

PASS_SCORE_BY_LEVEL = {
    "C1": 60, "C2": 62, "UG1": 65, "UG2": 68, "UG3": 70, "UG4": 72, "M1": 75, "M2": 78,
}


def _wikipedia(topic: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote_plus(topic).replace("+", "_")


def _wikipedia_search(topic: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote_plus(topic)


def _youtube_search(topic: str) -> str:
    return "https://www.youtube.com/results?search_query=" + quote_plus(topic)


def _mit_ocw_search(topic: str) -> str:
    return "https://ocw.mit.edu/search/?q=" + quote_plus(topic)


def _coursera_search(topic: str) -> str:
    return "https://www.coursera.org/search?query=" + quote_plus(topic)


def _khan_academy() -> str:
    return "https://www.khanacademy.org/"


def _openstax() -> str:
    return "https://openstax.org/subjects"


def _investopedia_search(topic: str) -> str:
    return "https://www.investopedia.com/search?q=" + quote_plus(topic)


def _huggingface_course() -> str:
    return "https://huggingface.co/learn/nlp-course"


def _fast_ai() -> str:
    return "https://www.fast.ai/"


def _plato_stanford() -> str:
    return "https://plato.stanford.edu/"


def _who() -> str:
    return "https://www.who.int/"


def _un() -> str:
    return "https://www.un.org/en/"


def _epa() -> str:
    return "https://www.epa.gov/environmental-topics"


def _python_docs() -> str:
    return "https://docs.python.org/3/"


def _r_project() -> str:
    return "https://www.r-project.org/"


def _mdn_search(topic: str) -> str:
    return "https://developer.mozilla.org/en-US/search?q=" + quote_plus(topic)


def _anthropic_prompting_guide() -> str:
    return "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"


def _smarthistory_search(topic: str) -> str:
    return "https://smarthistory.org/?s=" + quote_plus(topic)


def _kaggle_search(topic: str) -> str:
    return "https://www.kaggle.com/search?q=" + quote_plus(topic)


# ─── External course-provider integration (search/catalog links only) ──────
# No login or personal account is used or required here -- these are honest,
# always-real catalog/search URLs on each provider's own site. There is no
# public API for embedding a specific person's paid Udemy library or Netflix/
# Prime Video catalog into a third-party app, so this is the closest genuine
# integration: one click from any module straight into that provider's real
# search results for the same topic.

def _udemy_search(topic: str) -> str:
    return "https://www.udemy.com/courses/search/?q=" + quote_plus(topic)


def _edx_search(topic: str) -> str:
    return "https://www.edx.org/search?q=" + quote_plus(topic)


def _harvard_online_search(topic: str) -> str:
    return "https://pll.harvard.edu/catalog?keywords=" + quote_plus(topic)


def _class_central_search(topic: str) -> str:
    """Class Central aggregates free/audit courses from every major provider
    (Coursera, edX, MIT OCW, HarvardX, and more) in one search."""
    return "https://www.classcentral.com/search?q=" + quote_plus(topic)


def _pinterest_search(topic: str) -> str:
    return "https://www.pinterest.com/search/pins/?q=" + quote_plus(topic)


def _external_courses(subject: str, topic: str) -> list[dict]:
    """Real catalog/search links on each provider's own site for this topic.

    No personal account, login, or API key is used -- this is not a
    'connected account' integration, just an honest one-click search into
    each provider's real, live catalog for the same topic.
    """
    query = f"{topic} {subject}"
    return [
        {"title": "Udemy — course search", "url": _udemy_search(query), "source": "Udemy", "safe": True},
        {"title": "Coursera — course search", "url": _coursera_search(query), "source": "Coursera", "safe": True},
        {"title": "edX — course search", "url": _edx_search(query), "source": "edX", "safe": True},
        {"title": "MIT OpenCourseWare — search", "url": _mit_ocw_search(query), "source": "MIT OpenCourseWare", "safe": True},
        {"title": "Harvard Online — free course search", "url": _harvard_online_search(query), "source": "Harvard Online Learning", "safe": True},
        {"title": "Class Central — free course search (aggregates Coursera/edX/MIT/Harvard & more)", "url": _class_central_search(query), "source": "Class Central", "safe": True},
        {"title": "Pinterest — study notes & visual resources", "url": _pinterest_search(f"{topic} {subject} study notes"), "source": "Pinterest", "safe": True},
    ]


# ─── Flagship subjects with explicit, bespoke module ladders ────────────────
# Each list has exactly 16 (module_title, one_line_summary) entries, distributed
# two-per-level across the 8 levels (C1..M2), matching the task's example lists.

FLAGSHIP_MODULES: dict[str, list[tuple[str, str]]] = {
    "Artificial Intelligence": [
        ("Introduction to AI", "What intelligence and 'artificial' intelligence mean, and a tour of AI's history and subfields."),
        ("Intelligent Agents", "Modelling AI systems as agents that perceive an environment and choose actions to achieve goals."),
        ("Search Algorithms", "Uninformed and informed search (BFS, DFS, A*) for solving problems as a search over states."),
        ("Adversarial Search & Games", "Minimax, alpha-beta pruning, and how AI plays games like chess and Go."),
        ("Knowledge Representation", "Representing facts and rules with logic, semantic networks, and ontologies."),
        ("Reasoning & Expert Systems", "Rule-based expert systems and inference engines that mimic specialist decision-making."),
        ("Planning", "Classical planning, STRIPS-style representations, and plan search for multi-step goals."),
        ("Uncertainty & Probabilistic Reasoning", "Bayesian networks and reasoning about AI decisions under uncertainty."),
        ("Machine Learning Foundations for AI", "How learning from data fits into the broader AI toolbox alongside search and logic."),
        ("Neural Networks", "Perceptrons, multilayer networks, backpropagation, and why depth matters."),
        ("Generative AI", "Generative models (GANs, diffusion models, large language models) and how they create new content."),
        ("Natural Language & Vision for AI", "How AI systems perceive language and images as inputs to intelligent behaviour."),
        ("AI Ethics", "Bias, fairness, transparency, and accountability in AI system design and deployment."),
        ("AI Safety", "Robustness, alignment, and risk management for advanced AI systems."),
        ("AI in Society: Healthcare & Education", "Applied AI case studies in diagnosis support, tutoring systems, and adaptive learning."),
        ("AI in Society: Business & Governance", "Applied AI case studies in industry automation, policy, and regulation of AI."),
    ],
    "Machine Learning": [
        ("Introduction to Machine Learning", "What learning from data means, and the difference between AI, ML, and deep learning."),
        ("Data Preparation", "Cleaning, normalizing, and splitting data into training, validation, and test sets."),
        ("Feature Engineering", "Designing and selecting the input features that make learning algorithms effective."),
        ("Regression", "Linear and polynomial regression for predicting continuous outcomes."),
        ("Classification", "Logistic regression, decision trees, and k-NN for predicting categorical outcomes."),
        ("Supervised Learning", "The supervised learning framework: labelled data, loss functions, and generalization."),
        ("Unsupervised Learning", "Learning structure from unlabelled data: dimensionality reduction and density estimation."),
        ("Clustering", "K-means, hierarchical clustering, and DBSCAN for grouping similar data points."),
        ("Model Evaluation", "Cross-validation, precision/recall/F1, ROC curves, and avoiding overfitting."),
        ("Ensemble Methods", "Bagging, boosting, and random forests for combining many weak models."),
        ("Deep Learning Basics", "Feedforward networks, activation functions, and gradient descent training."),
        ("Reinforcement Learning", "Agents that learn by trial and error using rewards, Markov decision processes, and Q-learning."),
        ("Model Deployment Basics", "Packaging a trained model behind an API and monitoring it after deployment."),
        ("MLOps", "Versioning data and models, CI/CD for ML pipelines, and production monitoring."),
        ("Responsible ML", "Fairness, bias auditing, interpretability, and privacy-preserving machine learning."),
        ("ML Capstone & Research Methods", "Designing an original ML experiment, from hypothesis to evaluation and write-up."),
    ],
    "Natural Language Processing": [
        ("Introduction to NLP", "What NLP is, and why human language is hard for computers to process."),
        ("Text Preprocessing", "Cleaning, normalizing, and preparing raw text for downstream NLP tasks."),
        ("Tokenization", "Splitting text into words, subwords, and sentences as the first modelling step."),
        ("Language Models", "N-gram and neural language models that estimate the probability of word sequences."),
        ("Word Embeddings", "Word2Vec, GloVe, and how dense vectors capture word meaning and similarity."),
        ("Syntax & Parsing", "Part-of-speech tagging and parsing sentence structure computationally."),
        ("Sentiment Analysis", "Classifying the emotional tone or opinion expressed in a piece of text."),
        ("Sequence Models", "RNNs and LSTMs for modelling order and long-range dependencies in text."),
        ("Transformers", "Self-attention and the transformer architecture behind modern NLP systems."),
        ("Large Language Models", "How LLMs are pretrained, fine-tuned, and prompted for downstream tasks."),
        ("Question Answering", "Extractive and generative approaches to answering questions from text."),
        ("Machine Translation", "Sequence-to-sequence and transformer-based approaches to translating between languages."),
        ("Speech & Text Interfaces", "Connecting speech recognition and synthesis to text-based NLP pipelines."),
        ("Retrieval-Augmented Generation", "Combining search/retrieval with generation to ground LLM answers in real documents."),
        ("NLP Ethics & Bias", "Bias in training corpora, representational harms, and fairness in language technology."),
        ("NLP Capstone & Research Methods", "Designing an original NLP project, from data collection to evaluation."),
    ],
    "Data Science": [
        ("Introduction to Data Science", "The data science lifecycle: asking questions, collecting data, and communicating findings."),
        ("Data Wrangling", "Cleaning, reshaping, and joining messy real-world datasets."),
        ("Exploratory Data Analysis", "Summary statistics and visualization to understand a dataset before modelling."),
        ("Statistics for Data Science", "Descriptive and inferential statistics used to draw conclusions from data."),
        ("Data Visualization", "Designing charts and dashboards that communicate insights accurately and clearly."),
        ("Databases & SQL", "Querying relational databases to extract and aggregate data for analysis."),
        ("Predictive Modelling", "Applying regression and classification models to real datasets."),
        ("Big Data Tools", "Working with data too large for a single machine using distributed tools."),
        ("Experiment Design & A/B Testing", "Designing controlled experiments and interpreting statistical significance."),
        ("Time Series Analysis", "Forecasting methods for data that changes over time."),
        ("Data Storytelling", "Turning an analysis into a narrative and recommendation for decision-makers."),
        ("Data Ethics & Privacy", "Responsible collection, use, and anonymization of personal data."),
        ("Applied Machine Learning for Data Science", "Feature engineering and model selection in an applied data science workflow."),
        ("Data Engineering Fundamentals", "Building pipelines that move and transform data reliably."),
        ("Data Science in Industry", "Case studies of data science applied in business, healthcare, and public policy."),
        ("Data Science Capstone", "An end-to-end applied project: a real dataset, a business question, and a data-driven answer."),
    ],
    "Business Analytics": [
        ("Introduction to Business Analytics", "How organizations use data to improve decisions, from descriptive to prescriptive analytics."),
        ("Descriptive Analytics", "Summarizing historical business performance with KPIs and dashboards."),
        ("Data-Driven Decision Making", "Frameworks for turning analysis into concrete business recommendations."),
        ("Business Statistics", "Statistical foundations for analysing sales, operations, and customer data."),
        ("Predictive Analytics", "Forecasting demand, churn, and risk using statistical and ML models."),
        ("Customer & Marketing Analytics", "Segmentation, lifetime value, and campaign analysis."),
        ("Operations & Supply Chain Analytics", "Optimizing inventory, logistics, and process efficiency with data."),
        ("Financial Analytics", "Using analytics for budgeting, risk assessment, and investment decisions."),
        ("Prescriptive Analytics & Optimization", "Linear programming and optimization for resource allocation decisions."),
        ("Data Visualization for Business", "Dashboards and executive reporting with BI tools."),
        ("Analytics Strategy & Change Management", "Building a data-driven culture and analytics capability inside an organization."),
        ("Applied Machine Learning for Business", "Using ML models responsibly to support (not replace) business judgement."),
        ("Risk Analytics", "Quantifying and communicating business, credit, and operational risk."),
        ("People Analytics", "Using data to inform hiring, retention, and workforce planning decisions."),
        ("Business Analytics Ethics & Governance", "Data governance, privacy, and ethical use of analytics in decision-making."),
        ("Business Analytics Capstone", "A consulting-style analytics project solving a real organizational problem."),
    ],
    "Web Development": [
        ("HTML & CSS Fundamentals", "Structuring content with HTML and styling it with CSS -- the foundation of every web page."),
        ("JavaScript Fundamentals", "Variables, functions, and control flow for making web pages interactive."),
        ("Responsive Web Design", "Layouts (flexbox, grid, media queries) that adapt to phones, tablets, and desktops."),
        ("DOM Manipulation & Events", "Reading and updating a page live in the browser in response to user actions."),
        ("Frontend Frameworks", "Component-based UI development with a modern framework such as React."),
        ("State Management in Frontend Apps", "Managing shared application data across components as an app grows."),
        ("Backend Development Fundamentals", "Server-side logic and routing with a framework such as Node.js/Express."),
        ("Databases for Web Apps", "Storing and querying application data with SQL and NoSQL databases."),
        ("RESTful APIs & HTTP", "Designing and consuming HTTP APIs that connect frontend and backend."),
        ("Authentication & Authorization", "Verifying who a user is and what they're allowed to do in a web app."),
        ("Full-Stack Project Architecture", "Structuring a complete application: frontend, backend, database, and deployment."),
        ("Web Security Fundamentals", "Common vulnerabilities (the OWASP Top 10) and how to defend against them."),
        ("Performance Optimization & Caching", "Making web apps load and respond fast at scale."),
        ("Testing & Quality Assurance", "Unit, integration, and end-to-end testing for web applications."),
        ("DevOps & Deployment", "CI/CD pipelines, containers, and deploying a web app to production."),
        ("Full-Stack Capstone", "Designing, building, and deploying a complete full-stack web application."),
    ],
    "Cybersecurity": [
        ("Introduction to Cybersecurity", "Core concepts of confidentiality, integrity, and availability, and why security matters."),
        ("Networking Fundamentals for Security", "How data moves across networks, and where common attack surfaces arise."),
        ("Operating System Security", "Hardening, permissions, and security models in modern operating systems."),
        ("Cryptography Fundamentals", "Encryption, hashing, and digital signatures that protect data and identity."),
        ("Web Application Security", "Defending web applications against common vulnerabilities (OWASP Top 10)."),
        ("Threat Modeling & Risk Assessment", "Systematically identifying and prioritizing security risks in a system."),
        ("Malware Analysis Fundamentals", "How malicious software behaves and how analysts study it safely."),
        ("Authorized Security Testing Basics", "Ethical, permission-based penetration testing methodology and scope."),
        ("Identity & Access Management", "Authentication, authorization, and least-privilege access design."),
        ("Security Operations & Incident Response", "Detecting, responding to, and recovering from security incidents."),
        ("Cloud Security Fundamentals", "Securing data and workloads in cloud environments."),
        ("Governance, Risk & Compliance", "Security policy, regulatory frameworks, and organizational risk management."),
        ("Digital Forensics Fundamentals", "Preserving and analyzing digital evidence after a security incident."),
        ("Security Auditing & Vulnerability Management", "Finding, tracking, and remediating vulnerabilities systematically."),
        ("Advanced Threat Intelligence", "Tracking attacker techniques and emerging threats at an organizational level."),
        ("Cybersecurity Capstone", "An authorized security assessment project in a lab/sandboxed environment."),
    ],
    "Cloud Computing": [
        ("Introduction to Cloud Computing", "What cloud computing is, and why organizations moved workloads off their own hardware."),
        ("Cloud Service Models", "The differences between IaaS, PaaS, and SaaS and when to use each."),
        ("Virtualization & Containers", "How virtual machines and containers (e.g. Docker) isolate and package workloads."),
        ("Cloud Storage Solutions", "Object, block, and file storage trade-offs in the cloud."),
        ("Cloud Networking Fundamentals", "Virtual networks, load balancing, and connecting cloud resources securely."),
        ("Compute Services & Auto-Scaling", "Running and automatically scaling workloads to match demand."),
        ("Serverless Computing", "Running code without managing servers, and when serverless fits."),
        ("Cloud Databases", "Managed relational and NoSQL database services in the cloud."),
        ("Cloud Security & Identity Management", "Securing cloud accounts, resources, and data access."),
        ("Infrastructure as Code", "Defining and provisioning cloud infrastructure through version-controlled code."),
        ("Container Orchestration", "Managing many containers reliably at scale with a tool such as Kubernetes."),
        ("Cloud Cost Management & Optimization", "Monitoring and controlling cloud spend as usage grows."),
        ("Multi-Cloud & Hybrid Cloud Strategy", "Combining multiple cloud providers or on-premises and cloud infrastructure."),
        ("Cloud Monitoring & Observability", "Logging, metrics, and tracing to understand system health in production."),
        ("Cloud Architecture Design Patterns", "Common reliable, scalable architecture patterns for cloud systems."),
        ("Cloud Architecture Capstone", "Designing a scalable, secure cloud architecture for a real-world scenario."),
    ],
    "Digital Marketing": [
        ("Introduction to Digital Marketing", "The digital marketing landscape and how channels fit together."),
        ("Search Engine Optimization Fundamentals", "How search engines rank content, and how to structure content to be found."),
        ("Content Marketing Strategy", "Planning and creating content that attracts and retains an audience."),
        ("Social Media Marketing", "Building and engaging an audience across social platforms."),
        ("Email Marketing", "Building lists and campaigns that nurture leads and customers."),
        ("Pay-Per-Click Advertising", "Running and optimizing paid search and display ad campaigns."),
        ("Marketing Analytics & Data", "Measuring campaign performance and attributing results to channels."),
        ("Conversion Rate Optimization", "Testing and improving how many visitors take a desired action."),
        ("Brand Strategy & Positioning", "Defining what a brand stands for and how it's differentiated."),
        ("Influencer & Affiliate Marketing", "Partnering with creators and affiliates to reach new audiences."),
        ("Marketing Automation", "Using tools to trigger personalized marketing at scale."),
        ("E-commerce Marketing", "Marketing strategies specific to online retail and conversion funnels."),
        ("Video & Multimedia Marketing", "Producing and distributing video content across platforms."),
        ("Marketing Ethics & Data Privacy", "Responsible use of customer data and honest marketing practice."),
        ("Growth Hacking & Experimentation", "Rapid, data-driven experimentation to find scalable growth levers."),
        ("Integrated Marketing Capstone", "Designing a complete, multi-channel digital marketing campaign."),
    ],
    "UI/UX Design": [
        ("Introduction to UI/UX Design", "The difference between user interface and user experience design, and why both matter."),
        ("User Research Fundamentals", "Interviews, surveys, and observation methods for understanding users."),
        ("Information Architecture", "Organizing content and navigation so users can find what they need."),
        ("Wireframing & Prototyping", "Sketching and testing interface ideas before writing code."),
        ("Visual Design Principles", "Layout, hierarchy, contrast, and balance in interface design."),
        ("Typography & Color Theory", "Choosing type and color systems that communicate and are accessible."),
        ("Interaction Design", "Designing how a user moves through and interacts with an interface."),
        ("Usability Testing", "Observing real users to find and fix interface problems."),
        ("Design Systems & Component Libraries", "Building reusable, consistent design components at scale."),
        ("Accessibility in Design", "Designing interfaces usable by people with a wide range of abilities."),
        ("Mobile & Responsive Design", "Adapting interface design across phone, tablet, and desktop."),
        ("Design Tooling Workflows", "Efficient design and handoff workflows using tools such as Figma."),
        ("UX Writing & Microcopy", "Writing the small pieces of text that guide users through a product."),
        ("Design Thinking & Ideation", "Structured creative methods for generating and evaluating design solutions."),
        ("Advanced UX Research Methods", "Quantitative and mixed-methods research for mature products."),
        ("UX Design Capstone", "An end-to-end product design project from research through polished prototype."),
    ],
    "Project Management": [
        ("Introduction to Project Management", "What a project is, and the core role of a project manager."),
        ("Project Life Cycle & Initiation", "Defining a project's goals, scope, and stakeholders before work begins."),
        ("Scope Management", "Defining and controlling what is -- and isn't -- part of a project."),
        ("Time & Schedule Management", "Building and tracking realistic project schedules."),
        ("Cost Estimation & Budgeting", "Estimating and managing a project's budget through its life cycle."),
        ("Risk Management", "Identifying, assessing, and planning responses to project risks."),
        ("Agile & Scrum Fundamentals", "Iterative delivery, sprints, and the core Scrum roles and ceremonies."),
        ("Kanban & Lean Methods", "Visualizing work and limiting work-in-progress to improve flow."),
        ("Stakeholder Management & Communication", "Keeping the right people informed and aligned throughout a project."),
        ("Team Leadership & Conflict Resolution", "Leading a project team and resolving disagreements constructively."),
        ("Quality Management", "Building quality checkpoints into a project rather than inspecting for it at the end."),
        ("Procurement & Vendor Management", "Managing external vendors and contracts within a project."),
        ("Project Portfolio Management", "Prioritizing and balancing multiple projects across an organization."),
        ("Program Management", "Coordinating a group of related projects toward a shared strategic goal."),
        ("Advanced Agile Scaling", "Scaling agile practices across multiple teams (e.g. SAFe, LeSS)."),
        ("Project Management Capstone", "Planning and managing a complete project from charter to closure."),
    ],
    "Economics": [
        ("Introduction to Economics", "Scarcity, opportunity cost, and the basic questions every economy must answer."),
        ("Supply and Demand", "How prices emerge from the interaction of buyers and sellers in a market."),
        ("Elasticity", "Measuring how responsive quantity demanded/supplied is to price and other changes."),
        ("Market Structures", "Perfect competition, monopoly, oligopoly, and monopolistic competition."),
        ("Consumer & Producer Theory", "Utility maximization and cost/profit-maximizing production decisions."),
        ("Macroeconomic Indicators", "GDP, unemployment, and inflation as measures of an economy's health."),
        ("Aggregate Demand & Supply", "Modelling the whole economy's output and price level together."),
        ("Fiscal Policy", "How government spending and taxation influence the economy."),
        ("Monetary Policy", "How central banks use interest rates and money supply to manage the economy."),
        ("International Trade", "Comparative advantage and the gains and costs of trading across borders."),
        ("Exchange Rates & the Balance of Payments", "How currencies are valued and how international accounts balance."),
        ("Behavioral Economics", "How real human decision-making departs from purely rational models."),
        ("Development Economics", "Why some economies grow faster than others, and how policy can help."),
        ("Econometrics Fundamentals", "Using statistical methods to test economic theories against real data."),
        ("Game Theory in Economics", "Strategic decision-making between competing economic actors."),
        ("Economics Capstone & Research Methods", "Designing and conducting an original piece of economic research."),
    ],
    "Finance": [
        ("Personal Finance Fundamentals", "Budgeting, saving, and the time value of money."),
        ("Financial Statements", "Reading a balance sheet, income statement, and cash flow statement."),
        ("Time Value of Money", "Present value, future value, and discounting cash flows."),
        ("Risk and Return", "The trade-off between expected return and the risk investors must accept."),
        ("Corporate Finance Fundamentals", "How firms raise, allocate, and manage capital."),
        ("Capital Budgeting", "Evaluating whether a company's investment projects create value (NPV, IRR)."),
        ("Cost of Capital", "Estimating the return a company must earn to satisfy its investors."),
        ("Equity Markets", "How stocks are issued, traded, and valued."),
        ("Fixed Income & Bonds", "How bonds are priced and what drives interest rate risk."),
        ("Portfolio Theory", "Diversification and the trade-off between risk and return across assets."),
        ("Derivatives Fundamentals", "Options, futures, and how they are used to hedge or speculate."),
        ("Financial Markets & Institutions", "How banks, exchanges, and regulators shape the financial system."),
        ("Valuation Methods", "Discounted cash flow and comparable-company approaches to valuing a business."),
        ("Behavioral Finance", "How psychology and bias affect investor and market behaviour."),
        ("Financial Risk Management", "Identifying, measuring, and mitigating financial risk in an organization."),
        ("Finance Capstone", "Building a complete valuation or investment analysis for a real company."),
    ],
    "Philosophy": [
        ("Introduction to Philosophy", "What philosophy is, and its major branches (metaphysics, epistemology, ethics, logic)."),
        ("Logic & Argumentation", "Constructing and evaluating valid arguments."),
        ("Ancient Philosophy", "Socrates, Plato, and Aristotle's foundational questions about knowledge and the good life."),
        ("Medieval Philosophy", "How Augustine, Aquinas, and others reconciled faith and reason."),
        ("Modern Philosophy", "Descartes, Locke, Hume, and Kant on knowledge, mind, and reality."),
        ("Ethics: Consequentialism & Deontology", "Comparing outcome-based and duty-based moral theories."),
        ("Virtue Ethics", "Character and flourishing as the basis of ethical life, from Aristotle onward."),
        ("Political Philosophy", "Justice, authority, and the legitimate basis of the state."),
        ("Epistemology", "What knowledge is, and how (if at all) we can be justified in our beliefs."),
        ("Metaphysics", "The nature of reality, existence, causation, and identity."),
        ("Philosophy of Mind", "Consciousness, the mind-body problem, and personal identity."),
        ("Philosophy of Science", "What makes a theory scientific, and how scientific knowledge progresses."),
        ("Existentialism", "Freedom, authenticity, and meaning in a world without given purpose."),
        ("Applied Ethics", "Philosophy applied to real dilemmas in medicine, technology, business, and the environment."),
        ("Contemporary Philosophy", "Major 20th/21st-century movements and debates."),
        ("Philosophy Capstone", "An original philosophical essay defending a thesis with rigorous argument."),
    ],
    "Art History": [
        ("Introduction to Art History", "How art historians analyze and interpret visual works across time."),
        ("Prehistoric & Ancient Art", "Cave paintings through Egyptian, Greek, and Roman art."),
        ("Medieval Art", "Byzantine, Romanesque, and Gothic art and architecture."),
        ("Renaissance Art", "The rebirth of classical ideals in Italy and Northern Europe."),
        ("Baroque & Rococo Art", "Drama, movement, and ornamentation in 17th-18th century art."),
        ("19th-Century Art", "Romanticism, Realism, and the birth of Impressionism."),
        ("Modern Art Movements", "Cubism, Surrealism, and Expressionism in the early 20th century."),
        ("Contemporary Art", "Art since 1945, from Abstract Expressionism to conceptual art."),
        ("Non-Western Art Traditions", "Art historical traditions of Asia, Africa, and the Americas."),
        ("Islamic Art & Architecture", "Calligraphy, geometric pattern, and architecture across the Islamic world."),
        ("Art and Patronage", "How churches, courts, and collectors shaped what art was made."),
        ("Art Criticism & Theory", "Frameworks for interpreting meaning and value in art."),
        ("Museums & Curation", "How museums collect, preserve, and present art to the public."),
        ("Art Markets & Provenance", "How art is bought, sold, authenticated, and traced through history."),
        ("Digital Art History", "Using digital tools and databases in art historical research."),
        ("Art History Capstone", "An original research paper analyzing a work or movement in depth."),
    ],
    "Python": [
        ("Python Fundamentals", "Variables, data types, and basic operators."),
        ("Control Flow & Functions", "Conditionals, loops, and writing reusable functions."),
        ("Data Structures in Python", "Lists, dictionaries, sets, and tuples."),
        ("Object-Oriented Python", "Classes, objects, inheritance, and encapsulation."),
        ("File I/O & Error Handling", "Reading/writing files and handling exceptions gracefully."),
        ("Python Standard Library", "Common built-in modules for everyday tasks."),
        ("Working with Data Libraries", "Introduction to NumPy and pandas for data manipulation."),
        ("APIs & Web Requests in Python", "Fetching and working with data from web APIs."),
        ("Testing in Python", "Writing unit tests with pytest/unittest."),
        ("Automation & Scripting", "Using Python to automate repetitive tasks."),
        ("Python for Data Analysis", "Cleaning, analyzing, and visualizing data with pandas/matplotlib."),
        ("Python Web Development Basics", "Building a simple web app with Flask or Django."),
        ("Advanced Python", "Decorators, generators, and context managers."),
        ("Packaging & Virtual Environments", "Managing dependencies and distributing Python code."),
        ("Concurrency in Python", "Threading, multiprocessing, and async I/O."),
        ("Python Capstone Project", "Designing and building a complete Python application."),
    ],
    "R": [
        ("R Fundamentals & RStudio", "Getting started with R syntax and the RStudio environment."),
        ("Vectors & Data Types", "R's core data types and vectorized operations."),
        ("Data Frames & the Tidyverse", "Working with tabular data using tidyverse conventions."),
        ("Data Visualization with ggplot2", "Building publication-quality plots layer by layer."),
        ("Data Wrangling with dplyr", "Filtering, transforming, and summarizing data efficiently."),
        ("Statistical Analysis in R", "Running and interpreting common statistical tests."),
        ("R Markdown & Reporting", "Combining code, output, and narrative in reproducible reports."),
        ("Functions & Control Flow in R", "Writing custom functions and control structures."),
        ("Working with CRAN Packages", "Finding, installing, and using R's package ecosystem."),
        ("R for Machine Learning", "Building predictive models using R's ML packages."),
        ("Time Series Analysis in R", "Modelling and forecasting time-dependent data."),
        ("Shiny Web Apps", "Building interactive data applications with Shiny."),
        ("R for Specialized Domains", "Applying R in fields like bioinformatics or econometrics."),
        ("Debugging & Testing in R", "Finding and fixing bugs, and testing R code."),
        ("Advanced R Programming", "Functional programming and performance in R."),
        ("R Capstone Data Analysis Project", "An end-to-end data analysis project in R."),
    ],
    "JavaScript": [
        ("JavaScript Fundamentals", "Variables, types, and operators in JavaScript."),
        ("Functions & Scope", "Function declarations, closures, and variable scope."),
        ("Arrays & Objects", "JavaScript's core data structures and their methods."),
        ("DOM Manipulation", "Reading and updating a web page dynamically."),
        ("Asynchronous JavaScript", "Callbacks, promises, and async/await."),
        ("Modern JavaScript (ES6+)", "Arrow functions, destructuring, and other modern syntax."),
        ("Error Handling & Debugging", "Catching errors and debugging JavaScript effectively."),
        ("Modules & Bundling", "Organizing code into modules and bundling it for production."),
        ("Node.js Fundamentals", "Running JavaScript outside the browser on the server."),
        ("Working with APIs", "Fetching and handling JSON data from web APIs."),
        ("Frontend Frameworks Overview", "Comparing React, Vue, and Angular at a conceptual level."),
        ("TypeScript Basics", "Adding static types to JavaScript for safer code."),
        ("Testing JavaScript", "Writing unit and integration tests for JS code."),
        ("Build Tools & Package Managers", "npm/yarn and bundlers like Vite/webpack."),
        ("Advanced JavaScript Patterns", "Design patterns and performance techniques in JS."),
        ("JavaScript Capstone Project", "Building and deploying a complete JavaScript application."),
    ],
    "Prompt Engineering": [
        ("Introduction to Prompt Engineering", "Why the way you ask an AI model matters as much as what you ask."),
        ("How LLMs Interpret Prompts", "A conceptual model of how language models process instructions."),
        ("Zero-Shot & Few-Shot Prompting", "Getting good results with no examples versus a few examples."),
        ("Chain-of-Thought Prompting", "Encouraging step-by-step reasoning for better answers."),
        ("Role & Persona Prompting", "Shaping model behaviour by assigning it a role or persona."),
        ("Prompt Templates & Reusability", "Designing reusable prompt structures for repeated tasks."),
        ("System Prompts vs User Prompts", "How different prompt roles shape model behaviour."),
        ("Structured Output Prompting", "Getting reliable JSON or other structured formats from a model."),
        ("Prompt Chaining & Pipelines", "Breaking a complex task into a sequence of connected prompts."),
        ("Retrieval-Augmented Prompting", "Grounding prompts in real documents to reduce hallucination."),
        ("Evaluating Prompt Quality", "Systematically testing and comparing different prompts."),
        ("Prompt Injection & Security", "Understanding and defending against adversarial prompt manipulation."),
        ("Prompt Engineering for Coding Tasks", "Effective prompting patterns for code generation and review."),
        ("Prompt Engineering for Creative Tasks", "Prompting for writing, brainstorming, and creative work."),
        ("Advanced Agentic Prompting", "Prompting patterns for multi-step, tool-using AI agents."),
        ("Prompt Engineering Capstone", "Building a tested prompt library for a real application."),
    ],
    "Computer Science Engineering": [
        ("Introduction to Computer Science Engineering", "The discipline's scope, from hardware to software systems."),
        ("Data Structures & Algorithms", "Core structures and algorithms every CSE program covers."),
        ("Computer Organization & Architecture", "How a CPU, memory, and I/O systems actually work."),
        ("Discrete Mathematics for CSE", "Logic, set theory, and combinatorics underlying computer science."),
        ("Operating Systems", "Processes, memory management, and how an OS manages hardware."),
        ("Computer Networks", "How data moves reliably across networks including the Internet."),
        ("Database Systems", "Relational models, SQL, and transaction management."),
        ("Software Engineering Principles", "Designing, building, and maintaining large software systems."),
        ("Theory of Computation", "Automata, formal languages, and the limits of computation."),
        ("Compiler Design", "How source code is translated into executable machine code."),
        ("Object-Oriented Design & Patterns", "Structuring maintainable, extensible software."),
        ("Distributed Systems", "Designing systems that run across many machines reliably."),
        ("Computer Security Fundamentals", "Core security principles for CSE engineers."),
        ("Embedded Systems", "Programming hardware-constrained, real-time computing systems."),
        ("Advanced Algorithms", "Complexity theory and advanced algorithmic design techniques."),
        ("CSE Capstone Project", "Designing and building a substantial software/systems project."),
    ],
    "Big Data": [
        ("Introduction to Big Data", "The scale, variety, and velocity that define 'big data' problems."),
        ("The Hadoop Ecosystem", "HDFS and MapReduce for distributed storage and processing."),
        ("Apache Spark Fundamentals", "In-memory distributed computing for large-scale data."),
        ("Distributed File Systems", "How data is stored reliably across many machines."),
        ("NoSQL Databases for Big Data", "Document, key-value, and column-family stores at scale."),
        ("Data Ingestion Pipelines", "Getting large volumes of data into a big data system reliably."),
        ("Stream Processing", "Processing data in real time as it arrives (Kafka, Spark Streaming)."),
        ("Data Lakes & Data Warehouses", "Storing and organizing big data for analysis."),
        ("Big Data Query Engines", "SQL-on-Hadoop tools for querying huge datasets."),
        ("Spark SQL & DataFrames", "Structured processing at big-data scale."),
        ("Machine Learning at Scale", "Training models on datasets too large for a single machine."),
        ("Big Data Governance & Quality", "Ensuring data is trustworthy, documented, and compliant at scale."),
        ("Cloud-Based Big Data Platforms", "Managed big data services in the cloud."),
        ("Big Data Security & Privacy", "Protecting sensitive data across distributed big data systems."),
        ("Big Data Architecture Design", "Designing end-to-end big data systems for real workloads."),
        ("Big Data Capstone", "Building an end-to-end big data pipeline for a real dataset."),
    ],
    "MBA": [
        ("Introduction to MBA Studies", "The scope of a business administration education and core disciplines."),
        ("Managerial Accounting", "Using accounting information to make internal business decisions."),
        ("Corporate Finance for Managers", "Capital budgeting and financing decisions from a manager's view."),
        ("Marketing Management", "Segmentation, targeting, positioning, and the marketing mix."),
        ("Organizational Behavior", "How individuals and groups behave within organizations."),
        ("Strategic Management", "Analyzing competitive advantage and setting long-term company direction."),
        ("Business Law & Ethics", "Legal and ethical foundations every manager must understand."),
        ("Negotiation & Persuasion", "Structured approaches to reaching favorable agreements."),
        ("Leadership Development", "Theories and practice of effective organizational leadership."),
        ("Entrepreneurship & New Ventures", "Identifying opportunities and launching new businesses."),
        ("Global Business Strategy", "Managing operations and strategy across international markets."),
        ("Business Analytics for Managers", "Using data to support high-stakes managerial decisions."),
        ("Human Resource Management", "Recruiting, developing, and retaining organizational talent."),
        ("Corporate Strategy & M&A", "Growth strategy, mergers, and acquisitions at the corporate level."),
        ("Business Consulting Skills", "Structuring and solving ambiguous business problems."),
        ("MBA Capstone", "An integrative consulting-style project solving a real business challenge."),
    ],
    "Operations Management": [
        ("Introduction to Operations Management", "How organizations design and manage the processes that create value."),
        ("Process Design & Analysis", "Mapping and improving business processes."),
        ("Supply Chain Management", "Coordinating suppliers, production, and distribution."),
        ("Inventory Management", "Balancing inventory costs against service levels."),
        ("Quality Management", "Six Sigma, TQM, and systematic approaches to quality."),
        ("Lean Operations", "Eliminating waste and improving flow in operations."),
        ("Capacity Planning", "Matching production capacity to demand over time."),
        ("Project Scheduling", "Sequencing and scheduling work to meet deadlines efficiently."),
        ("Operations Strategy", "Aligning operational choices with overall business strategy."),
        ("Logistics & Distribution", "Moving goods efficiently from production to customer."),
        ("Service Operations Management", "Applying operations principles to service (not just manufacturing) businesses."),
        ("Sustainability in Operations", "Designing environmentally responsible operations."),
        ("Operations Analytics", "Using data and models to optimize operational decisions."),
        ("Global Operations Management", "Managing operations across multiple countries and facilities."),
        ("Operations Technology & Automation", "Robotics, automation, and digital tools in modern operations."),
        ("Operations Management Capstone", "Redesigning a real operational process for measurable improvement."),
    ],
    "AI Tools": [
        ("The AI Tools Landscape", "A map of the major categories of practical AI tools available today."),
        ("Conversational AI Assistants", "Effective everyday use of assistants like Claude, ChatGPT, and Gemini."),
        ("AI Writing & Productivity Tools", "Using AI to draft, edit, and organize written work."),
        ("AI Image & Video Generation Tools", "Practical use of generative image and video tools."),
        ("AI Coding Assistants", "Using tools like GitHub Copilot to accelerate software development."),
        ("AI Tools for Research & Data Analysis", "Using AI to summarize literature and analyze data faster."),
        ("No-Code AI App Builders", "Building simple AI-powered applications without traditional coding."),
        ("AI Tools for Business Workflows", "Integrating AI tools into everyday business processes."),
        ("Evaluating & Choosing AI Tools", "Criteria for selecting the right AI tool for a task."),
        ("Ethical & Responsible Use of AI Tools", "Using AI tools honestly, safely, and transparently."),
        ("AI Tools for Education", "Using AI tools to support learning and teaching."),
        ("AI Automation & Agents", "Using AI to automate multi-step tasks and workflows."),
        ("Building Simple AI-Powered Workflows", "Connecting AI tools together to solve a real task."),
        ("Integrating Multiple AI Tools", "Combining several AI tools into a single working process."),
        ("The Future of AI Tooling", "Emerging trends in the practical AI tools landscape."),
        ("AI Tools Capstone", "Assembling and documenting an AI tool stack for a real project."),
    ],
}

# ─── Existing subjects: theme ladders (auto-expanded across the 8 levels) ──
# Each subject maps to a short list of core themes that are cycled through the
# 8 levels with an increasing depth qualifier, so every level gets a
# meaningfully distinct, correctly-named module without hand-authoring 200+
# bespoke topics.

DEPTH_QUALIFIER_BY_LEVEL = {
    "C1": "Foundations of",
    "C2": "Building on",
    "UG1": "Core Theory:",
    "UG2": "Applied Methods:",
    "UG3": "Advanced",
    "UG4": "Capstone Study:",
    "M1": "Graduate Theory:",
    "M2": "Graduate Research Methods:",
}

EXISTING_SUBJECT_THEMES: dict[str, list[str]] = {
    "Math": ["Algebra & Functions", "Calculus", "Statistics & Probability", "Discrete Mathematics & Proof"],
    "English": ["Composition & Rhetoric", "Literary Analysis", "Academic Writing", "Linguistics"],
    "Science": ["Scientific Method & Measurement", "Earth & Space Science", "Life Science", "Physical Science"],
    "Geography": ["Physical Geography", "Human Geography", "Geopolitics & Globalization", "Geographic Information Systems"],
    "World History": ["Ancient & Classical Civilizations", "Medieval & Early Modern History", "Modern World History", "Historiography & Research Methods"],
    "Islamic Studies": ["Quranic Studies", "Islamic History & Civilization", "Islamic Ethics & Jurisprudence", "Comparative Religious Thought"],
    "Coding": ["Programming Fundamentals", "Data Structures & Algorithms", "Software Engineering Practice", "Systems & Architecture"],
    "World Literature": ["Classic World Literature", "Modern & Contemporary Literature", "Literary Theory & Criticism", "Comparative Literature"],
    "Art": ["Art Fundamentals & Technique", "Art History", "Design & Visual Communication", "Contemporary & Critical Art Practice"],
    "Music": ["Music Theory Fundamentals", "Music History", "Performance & Ear Training", "Music Technology & Composition"],
    "Survival Skills": ["Outdoor Safety Fundamentals", "Wilderness First Response", "Navigation & Resource Management", "Advanced Expedition & Risk Management"],
    "Cooking": ["Kitchen Fundamentals & Food Safety", "Global Cuisines", "Nutrition & Menu Design", "Culinary Arts Management"],
    "Foreign Languages": ["Beginner Communication", "Intermediate Grammar & Conversation", "Advanced Reading & Writing", "Applied Translation & Linguistics"],
    "General Knowledge": ["Current Affairs Fundamentals", "Global Institutions & Systems", "Media & Information Literacy", "Interdisciplinary General Studies"],
    "Social Studies": ["Society & Institutions", "Culture & Identity", "Comparative Social Systems", "Social Research Methods"],
    "Environmental Science": ["Ecosystems & Biodiversity", "Climate Science", "Environmental Policy", "Sustainability & Applied Environmental Management"],
    "Physical Education & Self-Defense": ["Fitness Fundamentals", "Applied Self-Defense Technique", "Sports Science", "Coaching & Performance Management"],
    "First Aid": ["Basic First Aid & CPR", "Emergency Response Protocols", "Wilderness & Remote Medicine", "Advanced Life Support Concepts"],
    "Physics": ["Classical Mechanics", "Electricity, Magnetism & Waves", "Modern & Quantum Physics", "Advanced Theoretical Physics"],
    "Chemistry": ["General & Inorganic Chemistry", "Organic Chemistry", "Physical Chemistry", "Advanced & Analytical Chemistry"],
    "Biology": ["Cell & Molecular Biology", "Genetics & Evolution", "Physiology & Anatomy", "Advanced & Systems Biology"],
    "Critical Thinking": ["Logic & Argument Structure", "Cognitive Bias & Fallacies", "Evidence Evaluation & Research Literacy", "Applied Decision Analysis"],
    "Civics": ["Government & Constitutions", "Rights, Law & Institutions", "Civic Participation & Public Policy", "Comparative Governance"],
    "Health Education": ["Personal Health & Wellbeing", "Public Health Fundamentals", "Health Systems & Policy", "Advanced Health Science & Epidemiology"],
    "Business Studies": ["Business Fundamentals", "Management & Organizational Behaviour", "Strategy & Entrepreneurship", "Advanced Corporate Strategy"],
    "World Politics": ["International Relations Fundamentals", "Comparative Political Systems", "Global Governance & Diplomacy", "Advanced Geopolitical Analysis"],
    "ICT & Computer Science": ["Computer Systems Fundamentals", "Networks & Databases", "Computer Science Theory", "Advanced Computing & Research Topics"],
}

RESOURCE_SITE_BY_SUBJECT: dict[str, str] = {
    "Math": "khan", "Science": "khan", "Physics": "khan", "Chemistry": "khan", "Biology": "khan",
    "Economics": "investopedia", "Finance": "investopedia", "Business Studies": "coursera",
    "Business Analytics": "coursera", "Data Science": "coursera",
    "Artificial Intelligence": "mit", "Machine Learning": "fastai", "Natural Language Processing": "huggingface",
    "Philosophy": "plato", "Critical Thinking": "plato",
    "Environmental Science": "epa", "Health Education": "who", "World Politics": "un", "Civics": "un",
    "Web Development": "mit", "Cybersecurity": "coursera", "Cloud Computing": "coursera",
    "Digital Marketing": "coursera", "UI/UX Design": "coursera", "Project Management": "coursera",
    "Art History": "smarthistory", "Python": "python_docs", "R": "r_project", "JavaScript": "mdn",
    "Prompt Engineering": "anthropic_prompting", "Computer Science Engineering": "mit",
    "Big Data": "kaggle", "MBA": "coursera", "Operations Management": "coursera", "AI Tools": "coursera",
}


def _resource_links(subject: str, topic: str) -> tuple[str, str]:
    """Return (book_or_text_url, video_url) for a subject/topic pairing."""
    site = RESOURCE_SITE_BY_SUBJECT.get(subject)
    if site == "khan":
        text_url = _khan_academy()
    elif site == "investopedia":
        text_url = _investopedia_search(topic)
    elif site == "coursera":
        text_url = _coursera_search(topic)
    elif site == "mit":
        text_url = _mit_ocw_search(topic)
    elif site == "fastai":
        text_url = _fast_ai()
    elif site == "huggingface":
        text_url = _huggingface_course()
    elif site == "plato":
        text_url = _plato_stanford()
    elif site == "epa":
        text_url = _epa()
    elif site == "who":
        text_url = _who()
    elif site == "un":
        text_url = _un()
    elif site == "smarthistory":
        text_url = _smarthistory_search(topic)
    elif site == "python_docs":
        text_url = _python_docs()
    elif site == "r_project":
        text_url = _r_project()
    elif site == "mdn":
        text_url = _mdn_search(topic)
    elif site == "anthropic_prompting":
        text_url = _anthropic_prompting_guide()
    elif site == "kaggle":
        text_url = _kaggle_search(topic)
    else:
        text_url = _wikipedia_search(topic)
    return text_url, _youtube_search(f"{topic} {subject} lecture")


def _lesson_for(subject: str, level: str, index: int, title: str, summary: str) -> dict:
    difficulty = DIFFICULTY_BY_LEVEL[level]
    level_label = LEVEL_LABELS[level]
    text_url, video_url = _resource_links(subject, title)
    key_concepts = [w.strip(",.:&") for w in title.replace("&", "and").split() if len(w) > 3][:5] or [title]
    lesson_id = f"{subject.lower().replace(' ', '-').replace('&', 'and')}-{level.lower()}-l{index}"
    return {
        "id": lesson_id,
        "title": title,
        "unit": title,
        "level": level,
        "subject": subject,
        "difficulty": difficulty,
        "estimated_time_minutes": TIME_BY_LEVEL[level],
        "learning_objectives": [
            f"Explain the core ideas of {title.lower()} at {level_label} depth.",
            f"Apply {title.lower()} concepts to worked examples and problems.",
            f"Critically discuss how {title.lower()} connects to real-world practice in {subject.lower()}.",
        ],
        "reading_material": summary,
        "key_concepts": key_concepts,
        "practical_activities": [
            f"Guided worked example on {title.lower()}",
            f"Small-group discussion / problem set on {title.lower()}",
        ],
        "exercises": [
            {"q": f"In your own words, what is the central idea behind {title.lower()}?", "type": "short_answer",
             "answer": summary},
        ],
        "homework": {"task": f"Write a short summary connecting {title.lower()} to one real-world example.", "due": "next_class"},
        "revision": {"notes": summary, "tip": f"Review {title.lower()} before moving to the next module."},
        "quiz": {
            "questions": [
                {"q": f"Which best describes {title.lower()}?", "options": [summary, "Unrelated to this subject", "Not covered at this level", "None of the above"], "answer": summary},
            ]
        },
        "assessment": {"type": "written_test", "criteria": [f"Understands {title.lower()}", "Applies concept correctly", "Connects to real-world context"], "passing_score": PASS_SCORE_BY_LEVEL[level]},
        "prerequisites": [],
        "next_lessons": [],
        "textbook_references": [text_url],
        "video_reference": video_url,
        "progress_tracking": {"completion_required": True, "min_quiz_score": PASS_SCORE_BY_LEVEL[level]},
    }


def _subject_content(subject: str, level: str, modules: list[tuple[str, str]]) -> dict:
    level_label = LEVEL_LABELS[level]
    lessons = [_lesson_for(subject, level, i + 1, title, summary) for i, (title, summary) in enumerate(modules)]
    primary_topic = modules[0][0]
    text_url, video_url = _resource_links(subject, primary_topic)

    books = [{
        "id": f"{subject.lower().replace(' ', '-')}-{level.lower()}-book1",
        "title": f"{subject}: {level_label} Reader",
        "author": "Curated open resource",
        "edition": "Online",
        "cover": "",
        "link": text_url,
        "rating": 4.5,
        "country": "International",
        "paid": False,
        "safe": True,
        "source": "Curated open-access curriculum resource",
    }]
    video_resources = [{
        "title": f"{primary_topic} — {level_label} overview",
        "url": video_url,
        "description": f"Curated video search for {primary_topic.lower()} at {level_label}.",
        "thumbnail": "",
        "type": "video",
        "safe": True,
    }]
    text_resources = [{"title": f"{subject} reference: {primary_topic}", "url": text_url, "source": "Curated open resource", "safe": True}]
    textbooks = [{"title": f"{subject} {level_label} Companion", "url": text_url, "source": "Curated open resource", "safe": True}]
    info_cards = [{
        "title": "Did You Know?",
        "fact": modules[0][1],
        "safe": True,
    }]
    quiz_bank = [
        {
            "question": f"What is the focus of the '{title}' module?",
            "type": "multiple_choice",
            "options": [summary, "Not part of this subject at this level", "A topic covered only in an earlier level", "None of the above"],
            "answer": summary,
        }
        for title, summary in modules[:3]
    ]
    exam = {
        "questions": [
            {"question": f"Briefly explain: {title}.", "type": "short_answer", "answer": summary}
            for title, summary in modules[:3]
        ],
        "passing_score": PASS_SCORE_BY_LEVEL[level],
    }
    project_ideas = [
        f"Design a mini-project applying '{title}' to a real dataset, case, or scenario relevant to {subject.lower()}."
        for title, _ in modules[:2]
    ] + [f"Prepare a {level_label.lower()} presentation comparing two modules covered in this level of {subject}."]
    real_world_examples = [
        f"How '{title}' shows up in real-world {subject.lower()} practice: {summary}"
        for title, summary in modules
    ][:3]
    learning_path = (
        f"At {level_label}, {subject} progresses through {', '.join(t for t, _ in modules)}. "
        f"Learners should complete modules in order, attempt the quiz after each module, and take the level exam once "
        f"all modules are complete before advancing to the next level."
    )

    return {
        "books": books,
        "video_resources": video_resources,
        "cartoon_videos": [],
        "text_resources": text_resources,
        "infographics": [],
        "quiz_bank": quiz_bank,
        "exam": exam,
        "textbooks": textbooks,
        "audio_resources": [],
        "comics": [],
        "drawing_activities": [],
        "info_cards": info_cards,
        "news_resources": [],
        "lessons": lessons,
        "project_ideas": project_ideas,
        "real_world_examples": real_world_examples,
        "learning_path": learning_path,
        "external_courses": _external_courses(subject, primary_topic),
    }


def build_level_file(level: str) -> dict:
    subjects: dict[str, dict] = {}

    # Flagship subjects: 2 bespoke modules per level (16 modules / 8 levels).
    level_index = LEVEL_IDS.index(level)
    for subject, all_modules in FLAGSHIP_MODULES.items():
        pair = all_modules[level_index * 2:level_index * 2 + 2]
        subjects[subject] = _subject_content(subject, level, pair)

    # Existing subjects: cycle through core themes with a depth qualifier.
    qualifier = DEPTH_QUALIFIER_BY_LEVEL[level]
    for subject, themes in EXISTING_SUBJECT_THEMES.items():
        theme = themes[level_index % len(themes)]
        title = f"{qualifier} {theme}".strip()
        depth = DEPTH_ADJECTIVE[level]
        summary = (
            f"{title} is {depth} module in {subject}, deepening prior levels with more rigorous theory, "
            f"worked examples, and assessment matched to {LEVEL_LABELS[level]}."
        )
        # A second, complementary module keeps each level from feeling like a single lesson.
        theme2 = themes[(level_index + 1) % len(themes)]
        title2 = f"{qualifier} {theme2}".strip()
        summary2 = (
            f"{title2} extends {subject} at {LEVEL_LABELS[level]}, connecting {theme2.lower()} to practical "
            f"problems, projects, and real-world case studies."
        )
        subjects[subject] = _subject_content(subject, level, [(title, summary), (title2, summary2)])

    return {"level": level, "level_label": LEVEL_LABELS[level], "subjects": subjects}


def main() -> None:
    SYLLABUS_DIR.mkdir(parents=True, exist_ok=True)
    for level in LEVEL_IDS:
        data = build_level_file(level)
        out_path = SYLLABUS_DIR / f"level_{level.lower()}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {out_path} ({len(data['subjects'])} subjects)")


if __name__ == "__main__":
    main()
