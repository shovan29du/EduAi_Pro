"""Final top-up pass: new (title, summary) tuples for M1 subjects that fell
slightly short of the 100-lesson minimum after title-collision skips in a
prior mass-generation pass. Consumed by merge_all_subjects_expansion.py.
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "AI Tools": {
        "M1": [
            ("Model Context Protocol Servers for Enterprise Tool Integration", "Designing standardized MCP servers that let AI assistants discover and safely invoke enterprise tools and data sources."),
            ("AI Tools for Wildfire Risk Prediction and Insurance Modeling", "Applying satellite imagery and machine learning tools to forecast wildfire spread and price catastrophe insurance exposure."),
            ("AI Tools for Museum Collection Digitization and Metadata Tagging", "Using computer vision and generative tools to catalog, tag, and cross-reference large digitized museum collections."),
            ("AI Tools for Judicial Sentencing Risk Assessment Auditing", "Evaluating the fairness, transparency, and error rates of AI-assisted recidivism and sentencing risk tools."),
            ("AI Tools for Semiconductor Design Verification", "Applying AI-assisted formal verification and test generation tools to catch chip design defects before fabrication."),
            ("AI Tools for Wildlife Camera Trap Species Identification", "Deploying vision models and annotation tooling to automatically classify species in large-scale camera trap datasets."),
            ("AI Tools for Live Performance Rehearsal Scheduling Optimization", "Using constraint-solving and generative scheduling tools to coordinate complex multi-performer rehearsal logistics."),
            ("AI Tools for Cold Chain Logistics Anomaly Detection", "Applying sensor-fusion AI tools to detect temperature excursions and spoilage risk across pharmaceutical and food cold chains."),
        ],
    },
    "Art History": {
        "M1": [
            ("Chola Bronze Sculpture: Iconometry and Ritual Function", "Examining the lost-wax casting techniques and proportional canons governing South Indian Chola bronze temple sculpture."),
            ("Aboriginal Australian Dot Painting: Iconography and Cultural Protocols", "Studying the symbolic systems and community protocols governing the display and interpretation of Aboriginal dot painting."),
            ("The Kano School and Japanese Screen Painting Tradition", "Analyzing the workshop practices and pictorial conventions of the Kano school's dominance in Japanese screen painting."),
            ("Persian Miniature Painting: The Herat School Tradition", "Tracing the compositional innovations and courtly patronage that defined the Timurid-era Herat school of manuscript painting."),
            ("Andean Textile Art: Inca Iconographic Systems", "Interpreting the geometric and figurative iconography encoded in Inca and pre-Inca Andean woven textiles."),
        ],
    },
    "Artificial Intelligence": {
        "M1": [
            ("World Models and Model-Based Planning for Embodied Agents", "Studying learned world models that let embodied agents simulate outcomes and plan actions before acting."),
            ("Speculative Decoding for LLM Inference Acceleration", "Analyzing draft-and-verify speculative decoding schemes that reduce large language model inference latency."),
            ("Test-Time Compute Scaling in Reasoning Models", "Examining how allocating additional inference-time computation improves reasoning accuracy in modern language models."),
            ("Emergent Communication Protocols in Multi-Agent Systems", "Studying how communication languages spontaneously emerge among learning agents cooperating on shared tasks."),
            ("AI for Automated Scientific Experiment Design", "Exploring AI systems that propose, prioritize, and iterate on experimental designs to accelerate scientific discovery."),
            ("Watermarking Techniques for AI-Generated Content Provenance", "Evaluating statistical watermarking schemes used to mark and later verify AI-generated text, image, and audio content."),
            ("Model Editing and Targeted Knowledge Updating in Neural Networks", "Studying techniques for surgically updating specific factual associations inside a trained neural network without full retraining."),
        ],
    },
    "Big Data": {
        "M1": [
            ("Vector Database Indexing Algorithms for Billion-Scale Similarity Search", "Analyzing approximate nearest-neighbor indexing structures that make similarity search tractable at billion-vector scale."),
        ],
    },
    "Biology": {
        "M1": [
            ("Xenotransplantation Immunological Barriers and Gene-Edited Organ Donors", "Examining the immune rejection mechanisms and gene-editing strategies used to make animal organs viable for human transplantation."),
        ],
    },
    "Business Analytics": {
        "M1": [
            ("Geospatial Analytics for Retail Site Selection Modeling", "Applying spatial statistics and location-intelligence data to model expected performance of candidate retail sites."),
            ("Analytics for Algorithmic Talent Matching in Gig Economy Platforms", "Analyzing the matching algorithms and fairness trade-offs that allocate gig work between platforms, workers, and demand."),
        ],
    },
    "Chemistry": {
        "M1": [
            ("Mechanistic Studies of Photocatalytic CO2-to-Fuel Conversion", "Investigating the reaction mechanisms and catalyst design principles behind converting captured CO2 into usable fuels using light-driven catalysis."),
            ("Metal-Free Organocatalysis for Enantioselective Aldol Reactions", "Studying small-molecule organocatalysts that achieve high enantioselectivity in aldol reactions without transition metals."),
        ],
    },
    "Coding": {
        "M1": [
            ("Content-Addressable Storage Systems for Version Control Internals", "Examining how content-addressable object stores underpin the internal data model of modern version control systems."),
        ],
    },
    "Critical Thinking": {
        "M1": [
            ("Epistemic Trespassing and the Limits of Expert Authority", "Examining when experts overstep their domain of competence and how audiences should weigh cross-domain expert claims."),
            ("The Paradox of Analysis in Conceptual Explication", "Studying the classical puzzle of how a correct conceptual analysis can be both informative and true by definition."),
            ("Robustness Analysis in Model-Based Scientific Reasoning", "Evaluating how scientists build confidence in a conclusion by checking its stability across structurally different models."),
            ("The Problem of Deep Disagreement in Rational Dialogue", "Analyzing Fogelin's thesis that some disagreements rest on divergent framework commitments that argument alone cannot resolve."),
        ],
    },
    "Cybersecurity": {
        "M1": [
            ("Container Image Provenance Verification via Sigstore and Cosign", "Examining keyless signing and transparency-log tooling used to verify the provenance and integrity of container images."),
        ],
    },
    "Data Science": {
        "M1": [
            ("Causal Machine Learning: Double/Debiased Machine Learning Estimators", "Studying double machine learning methods that combine flexible predictive models with valid causal effect estimation."),
            ("Feature Store Point-in-Time Correctness Design", "Examining how feature stores prevent label leakage by guaranteeing point-in-time correct feature retrieval for training."),
            ("Probabilistic Record Linkage and Entity Resolution at Scale", "Applying probabilistic matching models to resolve duplicate and fragmented entity records across large heterogeneous datasets."),
        ],
    },
    "Digital Marketing": {
        "M1": [
            ("Advanced Marketing for Generative Engine Optimization", "Adapting content and structured-data strategy so brands remain discoverable in AI-generated search and chat answers."),
            ("Advanced Marketing Data Clean Room Collaboration Strategies", "Designing privacy-preserving data clean room partnerships that let brands and platforms jointly analyze audience overlap."),
            ("Advanced Marketing for In-Game and Advergaming Advertising", "Evaluating strategies for embedding brand experiences and advertising within video games and interactive game environments."),
        ],
    },
    "Economics": {
        "M1": [
            ("Jean Tirole's Theory of Industrial Organization and Regulation", "Examining Tirole's game-theoretic framework for analyzing imperfect competition and designing regulation of dominant firms."),
            ("The Cantillon Effect and Monetary Transmission Non-Neutrality", "Studying how newly injected money unevenly affects relative prices depending on who receives it first."),
            ("William Baumol's Cost Disease in Service-Sector Economics", "Analyzing why labor-intensive service sectors experience persistent relative cost increases despite limited productivity growth."),
            ("The Lucas Critique and Its Implications for Macroeconomic Policy Modeling", "Examining Lucas's argument that historically estimated macro relationships break down once policy regimes change."),
            ("Herbert Simon's Bounded Rationality and Satisficing Behavior", "Studying Simon's model of decision-making under cognitive limits, where agents satisfice rather than optimize."),
        ],
    },
    "English": {
        "M1": [
            ("New Criticism and the Doctrine of the Intentional Fallacy", "Examining the New Critics' argument that a text's meaning should be assessed independently of the author's intentions."),
            ("Ecopoetics and the Anthropocene Imagination in Contemporary Poetry", "Studying how contemporary poets formally and thematically register ecological crisis and human-driven planetary change."),
            ("Print Ephemera and the Study of Broadside Ballads", "Examining broadside ballads and other cheap print ephemera as sources for literary and social history."),
        ],
    },
    "Finance": {
        "M1": [
            ("Liability Matching in Insurance-Linked Securities: Catastrophe Bonds", "Analyzing how catastrophe bonds transfer insurance risk to capital markets and how investors price triggering events."),
            ("Convertible Bond Arbitrage Strategy Mechanics", "Examining how arbitrageurs hedge convertible bonds against equity, credit, and volatility risk to isolate mispricing."),
            ("Merger Arbitrage Risk and Deal-Spread Dynamics", "Studying how merger arbitrage funds price deal completion risk and the spread between offer and market price."),
            ("Volatility Risk Premium Harvesting Strategies", "Analyzing systematic strategies that sell option volatility to capture the historical gap between implied and realized volatility."),
            ("Repo Market Mechanics and Collateral Rehypothecation", "Examining how repurchase agreements finance securities positions and the risks introduced by collateral rehypothecation."),
            ("Collateralized Loan Obligation Structuring and Risk Tranching", "Studying how leveraged loan pools are structured into CLO tranches with differentiated risk and return profiles."),
            ("Currency Overlay Strategies for Institutional Portfolios", "Examining how institutional investors use currency overlay programs to manage or selectively hedge foreign exchange exposure."),
            ("Behavioral Biases in Financial Advisor-Client Relationships", "Studying how advisor and client cognitive biases interact to shape investment recommendations and portfolio outcomes."),
        ],
    },
    "First Aid": {
        "M1": [
            ("Pediatric Sepsis Recognition and Rapid Response Protocols", "Examining early warning signs of pediatric sepsis and the rapid field response protocols that improve survival."),
            ("Anaphylaxis Biphasic Reaction Monitoring Protocols", "Studying observation-window protocols designed to catch delayed biphasic anaphylactic reactions after initial treatment."),
            ("High-Fidelity Simulation Training for Mass Casualty Response", "Evaluating how high-fidelity simulation exercises prepare responder teams for coordinated mass casualty triage and care."),
            ("Field Management of Traumatic Eye Injuries", "Covering first-response assessment and stabilization techniques for penetrating and blunt traumatic eye injuries."),
            ("Prehospital Recognition of Non-Accidental Trauma in Children", "Training first responders to recognize injury patterns and contextual cues suggestive of non-accidental pediatric trauma."),
        ],
    },
    "Foreign Languages": {
        "M1": [
            ("Xhosa Click Consonant System and Phonetic Analysis", "Analyzing the phonetic inventory and phonological patterning of the click consonants in Xhosa."),
            ("Georgian Verb Polypersonal Agreement System", "Examining how Georgian verbs simultaneously encode agreement with multiple grammatical arguments."),
            ("Mongolian Vertical Script and Orthographic History", "Tracing the historical development and structural features of the traditional Mongolian vertical writing system."),
            ("Catalan Sociolinguistics: Language Policy in Contemporary Spain", "Studying language planning, immersion education, and status debates surrounding Catalan in contemporary Spain."),
            ("Malagasy Language: Austronesian Roots and Verb-Initial Syntax", "Examining Malagasy's Austronesian ancestry and its typologically unusual verb-initial sentence structure."),
            ("Tibetan Honorific Register System", "Analyzing the elaborate honorific vocabulary and register distinctions that structure polite Tibetan speech."),
        ],
    },
    "General Knowledge": {
        "M1": [
            ("History of International Weights and Measures Standardization", "Tracing the international treaties and scientific efforts that standardized units of measurement across nations."),
            ("Famous Diplomatic Incidents and Their Historical Consequences", "Surveying notable diplomatic incidents and examining how they reshaped subsequent international relations."),
        ],
    },
    "Geography": {
        "M1": [
            ("Geography of Submarine Cable Networks and Global Connectivity", "Mapping the physical routing of undersea cables and analyzing their role in global data connectivity and vulnerability."),
            ("Geography of Special Economic Zones and Trade Corridor Development", "Examining how special economic zones are sited and linked to trade corridors to attract investment and exports."),
            ("Geography of Urban Shrinkage and Population Decline", "Studying the spatial and economic dynamics of cities experiencing sustained population and infrastructure decline."),
            ("Geography of Desert Urbanism and Arid-Region City Planning", "Analyzing planning strategies that address water scarcity, heat, and growth pressures in desert and arid-region cities."),
            ("Geography of Freshwater Lake Systems and Transboundary Governance", "Examining governance arrangements that manage shared freshwater lake systems crossing multiple political jurisdictions."),
            ("Geography of High-Speed Rail Networks and Regional Integration", "Studying how high-speed rail corridors reshape regional economic integration and accessibility patterns."),
        ],
    },
    "Health Education": {
        "M1": [
            ("Menstrual Health Education Program Design and Stigma Reduction", "Designing menstrual health curricula that combine accurate information with strategies to reduce stigma and dropout."),
            ("Environmental Justice and Community Health Risk Mapping", "Applying spatial and epidemiological methods to map how environmental hazards disproportionately affect marginalized communities."),
            ("Digital Contact Tracing Ethics and Public Health Surveillance", "Examining the privacy, consent, and equity trade-offs raised by digital contact tracing and surveillance technologies."),
            ("Health Literacy in Low-Literacy Populations: Visual Communication Design", "Designing visual and plain-language health communication strategies for populations with limited literacy."),
            ("Community Health Worker Program Scaling Models", "Studying organizational models for scaling community health worker programs while preserving quality and trust."),
            ("Climate-Resilient Health System Adaptation Planning", "Examining how health systems plan and adapt service delivery to withstand climate-driven shocks and disease shifts."),
            ("Workplace Mental Health Stigma Reduction Interventions", "Evaluating organizational interventions designed to reduce mental health stigma and improve help-seeking at work."),
        ],
    },
    "Islamic Studies": {
        "M1": [
            ("Ibn Khaldun's Muqaddimah and the Theory of Asabiyyah", "Examining Ibn Khaldun's theory of group solidarity (asabiyyah) as a driver of the rise and fall of dynasties."),
            ("Al-Biruni's Comparative Study of Indian Religions", "Studying al-Biruni's pioneering comparative and empirical approach to documenting Indian religious and scientific thought."),
            ("The Barelvi-Deobandi Theological Divide in South Asia", "Examining the historical origins and doctrinal differences between the Barelvi and Deobandi movements in South Asian Islam."),
            ("Zaydi Jurisprudence in Yemeni Islamic Scholarship", "Surveying the distinctive legal methodology and historical development of Zaydi Shi'i jurisprudence in Yemen."),
            ("Ibadi Islam: Theology and Governance in Oman", "Examining the theology, legal tradition, and political history of Ibadi Islam as practiced in Oman."),
            ("The Millet System and Religious Pluralism under Ottoman Rule", "Analyzing how the Ottoman millet system structured legal autonomy and coexistence among religious communities."),
            ("Islamic Manuscript Illumination and Calligraphic Traditions", "Studying the artistic conventions and regional schools of illumination and calligraphy in Islamic manuscript production."),
            ("Contemporary Halal Certification Standards and Global Trade", "Examining how halal certification bodies set standards that shape global food and consumer product trade."),
            ("Islamic Ethics of Artificial Intelligence and Emerging Technology", "Applying classical Islamic ethical frameworks to contemporary questions raised by artificial intelligence and biotechnology."),
            ("Muhammad Abduh and the Foundations of Islamic Modernism", "Examining Abduh's reformist project to reconcile Islamic tradition with reason and modern institutions."),
        ],
    },
    "MBA": {
        "M1": [
            ("Zero-Based Budgeting Implementation in Corporate Turnarounds", "Examining how zero-based budgeting forces line-by-line cost justification to accelerate corporate turnaround programs."),
            ("Blue Ocean Strategy: Value Innovation Frameworks", "Studying the value-innovation framework for creating uncontested market space rather than competing head-to-head."),
            ("Balanced Scorecard Design for Multi-Business-Unit Conglomerates", "Designing balanced scorecard systems that align performance measurement across diverse conglomerate business units."),
            ("Strategic Outsourcing versus Vertical Integration Decision Frameworks", "Applying transaction-cost and capability frameworks to decide when firms should outsource versus vertically integrate."),
            ("Executive Compensation Design and Say-on-Pay Governance", "Examining how executive pay structures are designed and constrained by shareholder say-on-pay governance mechanisms."),
            ("Corporate Turnaround Management and Distressed Leadership", "Studying the leadership practices and sequencing decisions that characterize successful corporate turnarounds."),
            ("Three Horizons Framework for Strategic Innovation Foresight", "Applying the three-horizons model to balance core business performance against emerging and transformational innovation."),
            ("Business Model Canvas Application in Corporate New Venture Design", "Using the business model canvas to design and stress-test new ventures incubated inside established corporations."),
            ("Activity-Based Costing for Strategic Cost Management", "Applying activity-based costing to expose true product and customer profitability for strategic decision-making."),
            ("Earnout Structuring and Post-Acquisition Incentive Alignment", "Designing earnout provisions that align seller incentives with acquirer performance expectations after a deal closes."),
            ("Joint Venture Bargaining Power and Equity Stake Negotiation", "Examining how relative bargaining power shapes equity stakes and control rights in joint venture negotiations."),
            ("Corporate Boardroom Dynamics and Director Independence Assessment", "Studying how boardroom group dynamics and director independence criteria shape effective corporate oversight."),
            ("Horizontal versus Vertical M&A Integration Strategy Selection", "Comparing integration strategies for horizontal and vertical mergers based on synergy source and organizational fit."),
            ("Employer Branding Strategy for Executive Talent Retention", "Designing employer branding strategies aimed at attracting and retaining senior executive talent in competitive markets."),
        ],
    },
    "Machine Learning": {
        "M1": [
            ("Flow Matching and Rectified Flow Generative Models", "Studying flow-matching objectives that train continuous generative models as an alternative to diffusion-based sampling."),
            ("Retrieval-Augmented Fine-Tuning for Domain Adaptation", "Examining fine-tuning strategies that jointly optimize retrieval and generation components for domain-specific tasks."),
            ("State Space Duality in Selective Sequence Models", "Analyzing selective state-space architectures and their duality with attention as efficient long-sequence models."),
            ("Sharpness-Aware Minimization for Generalization", "Studying optimization methods that seek flat loss-landscape minima to improve model generalization."),
            ("Grokking Phenomenon and Delayed Generalization Dynamics", "Investigating the grokking phenomenon in which models generalize long after achieving perfect training accuracy."),
            ("Tabular Deep Learning Architectures versus Gradient Boosting", "Comparing modern deep learning architectures for tabular data against gradient-boosted tree baselines."),
            ("Data-Centric AI: Systematic Dataset Curation Methods", "Studying systematic methods for curating, cleaning, and prioritizing training data to improve model quality."),
        ],
    },
    "Math": {
        "M1": [
            ("Perfectoid Spaces and p-adic Geometry", "Introducing perfectoid spaces and their role in relating characteristic-zero and characteristic-p algebraic geometry."),
            ("Langlands Program: An Introduction to Automorphic Forms", "Introducing the conjectural correspondences between automorphic forms and Galois representations at the heart of the Langlands program."),
            ("Optimal Transport and Wasserstein Gradient Flows", "Studying optimal transport theory and the gradient flows it induces on spaces of probability measures."),
            ("Persistent Homology and Topological Data Analysis", "Applying persistent homology to extract robust topological features from noisy high-dimensional data."),
            ("Free Probability Theory and Random Matrix Universality", "Studying free probability's noncommutative framework and its role in explaining random matrix universality results."),
            ("Motivic Cohomology and Algebraic Cycles", "Introducing motivic cohomology as a tool for studying algebraic cycles and refining classical cohomology theories."),
        ],
    },
    "Music": {
        "M1": [
            ("Byzantine Chant Notation and Modal Theory (Oktoechos)", "Examining the neumatic notation system and eight-mode (oktoechos) theoretical framework of Byzantine chant."),
            ("Flamenco Cante Jondo: Modal and Rhythmic Structure", "Analyzing the modal language and complex compás rhythmic cycles underlying flamenco cante jondo."),
            ("Turkish Makam Theory and Microtonal Tuning Systems", "Studying the melodic makam system and its microtonal intervallic structure in Ottoman and Turkish classical music."),
            ("Andean Panpipe Ensemble Traditions and Sikuri Performance Practice", "Examining the interlocking performance technique and communal structure of Andean sikuri panpipe ensembles."),
        ],
    },
    "Natural Language Processing": {
        "M1": [
            ("Long-Context Retrieval Benchmarking and Needle-in-Haystack Evaluation", "Evaluating how well long-context language models retrieve and use information buried within very long inputs."),
            ("Toxicity Mitigation via Reinforcement Learning from AI Feedback", "Studying RLAIF techniques that use AI-generated feedback signals to reduce toxic language model outputs."),
            ("Morphologically Rich Language Modeling Challenges", "Examining tokenization and modeling challenges that arise when applying NLP architectures to morphologically rich languages."),
            ("Semantic Parsing for Voice Assistant Intent Understanding", "Studying semantic parsing pipelines that convert spoken user utterances into structured voice assistant intents."),
            ("Cross-Lingual Word Sense Disambiguation Techniques", "Examining methods for resolving word sense ambiguity in multilingual and cross-lingual NLP pipelines."),
        ],
    },
    "Operations Management": {
        "M1": [
            ("Operations Management for Data Center Capacity and Cooling Optimization", "Applying operations research methods to optimize data center capacity planning and cooling energy efficiency."),
        ],
    },
    "Philosophy": {
        "M1": [
            ("Alasdair MacIntyre's Critique of Modern Moral Fragmentation", "Examining MacIntyre's argument that modern moral discourse has fragmented from its virtue-based Aristotelian roots."),
            ("Bernard Williams and the Critique of Utilitarian Integrity", "Studying Williams's objection that utilitarianism can require agents to violate their own moral integrity."),
            ("Thomas Nagel and the Subjective Character of Experience", "Examining Nagel's argument that subjective conscious experience resists reduction to objective physical description."),
            ("Iris Murdoch's Moral Vision and the Concept of Attention", "Studying Murdoch's account of moral perception as a disciplined form of attention to reality beyond the self."),
            ("Martha Nussbaum's Theory of Emotions as Cognitive Judgments", "Examining Nussbaum's argument that emotions embody evaluative judgments rather than being mere non-rational feelings."),
            ("Charles Taylor's Sources of the Self and Modern Identity", "Studying Taylor's genealogy of how modern conceptions of selfhood and moral sources developed historically."),
            ("Judith Butler's Performativity and the Metaphysics of Gender", "Examining Butler's account of gender as constituted through repeated performative acts rather than fixed essence."),
            ("Jacques Rancière's Politics of Aesthetic Dissensus", "Studying Rancière's account of politics as a disruption of the sensible order through aesthetic dissensus."),
            ("Alain Badiou's Theory of the Event and Truth Procedures", "Examining Badiou's account of truth as emerging from rare events that rupture established situations."),
            ("Giorgio Agamben's State of Exception and Bare Life", "Studying Agamben's analysis of sovereign power's capacity to suspend law and reduce subjects to bare life."),
            ("Gilles Deleuze and Guattari's Concept of the Rhizome", "Examining the rhizome as a non-hierarchical model of thought and organization opposed to arborescent structures."),
            ("Paul Ricoeur's Hermeneutics of the Self and Narrative Identity", "Studying Ricoeur's account of personal identity as constituted through narrative self-interpretation over time."),
        ],
    },
    "Physical Education & Self-Defense": {
        "M1": [
            ("Krav Maga Threat Assessment and Reflexive Defense Training", "Examining the threat-assessment principles and reflexive response training methods central to Krav Maga."),
            ("Filipino Martial Arts: Weapon-Based Combat Systems Analysis", "Analyzing the stick, blade, and empty-hand transition principles that structure Filipino martial arts training."),
            ("Sports Concussion Return-to-Learn Academic Accommodation Protocols", "Examining graded return-to-learn protocols that support student-athletes' academic reintegration after concussion."),
        ],
    },
    "Physics": {
        "M1": [
            ("Topological Quantum Computing and Anyonic Braiding", "Introducing topological quantum computation, where quasiparticle braiding statistics encode fault-tolerant information."),
        ],
    },
    "Project Management": {
        "M1": [
            ("Agile Contract Models for Outcome-Based Vendor Engagements", "Designing contract structures that align agile delivery practices with outcome-based vendor accountability."),
            ("Project Management for Space Systems and Satellite Program Delivery", "Examining the scheduling, risk, and systems-integration challenges specific to space and satellite program delivery."),
            ("Stakeholder Communication Planning for Politically Sensitive Public Projects", "Designing communication strategies for public infrastructure projects operating under intense political scrutiny."),
            ("Project Knowledge Transfer Strategies During Team Turnover", "Examining methods for preserving project knowledge and continuity when key team members rotate off a program."),
        ],
    },
    "Prompt Engineering": {
        "M1": [
            ("Prompt Engineering for Recommendation Explanation Generation", "Designing prompts that generate clear, trustworthy natural-language explanations for algorithmic recommendations."),
            ("Prompt Engineering for Video Understanding and Temporal Grounding", "Designing prompting strategies that help multimodal models reason about events and their timing within video content."),
            ("Prompt Design for 3D Scene and Spatial Reasoning Tasks", "Crafting prompts that elicit accurate spatial reasoning about object relationships within 3D scenes."),
            ("Prompt Engineering for Automated Unit Test Generation", "Designing prompting strategies that guide code models to produce comprehensive, correct automated unit tests."),
            ("Prompt Engineering for Music and Audio Generation Models", "Examining prompting techniques used to steer style, structure, and mood in text-to-music and audio generation models."),
            ("Cross-Modal Prompt Alignment for Text-to-Image Diffusion Models", "Studying how prompt phrasing and structure align text semantics with visual output in diffusion-based image models."),
            ("Prompt Engineering for Negotiation and Multi-Party Simulation Agents", "Designing prompts that guide language model agents through realistic multi-party negotiation simulations."),
            ("Prompt Design for Regulatory Filing and Compliance Report Drafting", "Crafting prompts that help models draft accurate, well-structured regulatory filings and compliance documentation."),
        ],
    },
    "Python": {
        "M1": [
            ("Building Custom Python Debuggers with sys.settrace", "Using Python's sys.settrace hook to build custom tracing tools and interactive debuggers."),
            ("Advanced Buffer Protocol and Memory Views in Python", "Examining the buffer protocol and memoryview objects that enable zero-copy data sharing between Python objects."),
            ("Writing Python Type Stubs for Third-Party Library Distribution", "Authoring and distributing .pyi type stub packages that add static type information to untyped libraries."),
        ],
    },
    "R": {
        "M1": [
            ("Advanced R for Actuarial Loss Reserving Models", "Implementing actuarial loss reserving techniques such as chain-ladder and bootstrap methods in R."),
            ("Building REST APIs in R with plumber", "Designing and deploying production REST APIs that expose R analytics functions using the plumber package."),
            ("R for Remote Sensing Raster Analysis with terra", "Applying the terra package to process, analyze, and visualize large remote-sensing raster datasets in R."),
            ("Advanced Survey Sampling Weight Calibration in R", "Implementing calibration and post-stratification weighting methods for complex survey samples in R."),
            ("R for Structural Equation Modeling with lavaan", "Specifying and fitting structural equation and latent variable models in R using the lavaan package."),
            ("Building Interactive Maps with mapdeck in R", "Creating GPU-accelerated interactive geospatial visualizations in R using the mapdeck package."),
        ],
    },
    "UI/UX Design": {
        "M1": [
            ("Designing for Neurodivergent Users: Cognitive Accessibility Patterns", "Applying interface patterns that reduce cognitive load and sensory overwhelm for neurodivergent users."),
            ("Design Systems Versioning and Deprecation Strategy", "Designing versioning, migration, and deprecation policies that keep large-scale design systems maintainable over time."),
            ("Biophilic Design Principles in Digital Interface Aesthetics", "Applying biophilic design principles drawn from nature to shape calming, restorative digital interface aesthetics."),
            ("Designing for Low-Vision Users: Adaptive Typography Systems", "Designing adaptive typography and layout systems that scale and reflow to support low-vision users."),
            ("UX Research for B2B Enterprise Buyer Personas", "Conducting UX research that captures the multi-stakeholder decision dynamics of B2B enterprise buyer personas."),
            ("Designing Multi-Device Continuity and Handoff Experiences", "Designing seamless handoff experiences that let users continue tasks fluidly across phone, desktop, and other devices."),
        ],
    },
    "Web Development": {
        "M1": [
            ("Building Offline-Capable Sync Engines with CRDTs for Web Apps", "Designing offline-first web applications that use conflict-free replicated data types to synchronize state across clients."),
            ("Advanced WebGPU Programming for Browser-Based Graphics", "Implementing high-performance browser graphics and compute pipelines using the WebGPU API."),
        ],
    },
}
