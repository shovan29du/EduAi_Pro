"""
Final top-up pass (group 49) for UG4 / M1 / M2 lesson minimums.

A small closing pass: a handful of subjects were left just short of their
minimum lesson target after earlier merge passes because a few candidate
titles collided with the global dedup (the same title already existed at
another level). This module supplies new, narrow, non-duplicate topics for
exactly those subjects/levels.
"""

MODULES: dict[str, dict[str, list[tuple[str, str]]]] = {
    "AI Tools": {
        "UG4": [
            ("AI Tools for Numismatic Coin Authentication", "Examines how image-classification and provenance-matching AI tools assist collectors and museums in verifying the authenticity of historical coins."),
            ("AI Tools for Beekeeping Colony Health Monitoring", "Surveys sensor-fed AI monitoring tools that detect early signs of hive stress, disease, and queen failure in commercial apiaries."),
        ],
    },
    "Art History": {
        "UG4": [
            ("The Isenheim Altarpiece: Grünewald's Iconography of Suffering", "Examines Matthias Grünewald's altarpiece as a case study in using graphic imagery of illness and suffering for devotional and therapeutic purposes."),
            ("The Ghent Altarpiece: Theft, Forgery, and Recovery", "Traces the eventful history of the Van Eyck brothers' altarpiece through wartime theft, a still-missing panel, and decades of recovery efforts."),
            ("Artemisia Gentileschi and the Judith Beheading Holofernes Case Study", "Analyzes Artemisia Gentileschi's treatment of the Judith narrative as a case study in gender, biography, and interpretation in Baroque painting."),
        ],
    },
    "Big Data": {
        "UG4": [
            ("HyperLogLog and Probabilistic Cardinality Estimation at Scale", "Introduces the HyperLogLog algorithm for approximating distinct-count queries over massive datasets with minimal memory overhead."),
        ],
    },
    "Cloud Computing": {
        "UG4": [
            ("The 2017 AWS S3 Outage: A Cloud Resilience Case Study", "Analyzes the operational causes and industry-wide impact of the 2017 Amazon S3 outage as a lesson in cloud dependency risk."),
            ("Spot Instance Bidding Strategies for Fault-Tolerant Cloud Workloads", "Covers bidding and interruption-handling strategies for running cost-efficient batch workloads on spot or preemptible cloud instances."),
            ("AWS Well-Architected Framework Review Case Study", "Walks through applying a structured Well-Architected-style review to evaluate an existing cloud workload across reliability, cost, and security pillars."),
        ],
    },
    "Cybersecurity": {
        "UG4": [
            ("The Stuxnet Worm: Anatomy of a Nation-State Cyberweapon", "Dissects the Stuxnet worm's design and delivery as a case study in nation-state-grade malware targeting industrial control systems."),
            ("The SolarWinds Supply Chain Compromise: A Forensic Case Study", "Examines the technical mechanics and detection timeline of the SolarWinds Orion compromise as a landmark supply-chain intrusion."),
            ("The Mirai Botnet and the 2016 Dyn DNS Outage", "Traces how the Mirai IoT botnet was assembled and weaponized to cause the 2016 Dyn DNS outage, disrupting major internet services."),
        ],
    },
    "Digital Marketing": {
        "UG4": [
            ("Dark Social: Measuring Untrackable Peer-to-Peer Content Sharing", "Explores methods for estimating the marketing impact of dark social sharing, such as private messaging and direct links, that evade standard analytics tracking."),
        ],
    },
    "Economics": {
        "UG4": [
            ("Elinor Ostrom and the Governance of the Commons", "Examines Elinor Ostrom's empirical research on how communities self-organize institutions to manage shared resources without privatization or central control."),
            ("Friedrich Hayek and the Knowledge Problem in Economic Planning", "Explores Hayek's argument that dispersed local knowledge makes centralized economic planning inherently inferior to price-coordinated markets."),
            ("The Mississippi Bubble and John Law's Monetary Experiment", "Analyzes John Law's early eighteenth-century paper-money and stock scheme in France as a foundational episode in monetary and speculative bubble history."),
            ("The Long Depression of 1873-1896: A Reassessment", "Reexamines the extended period of price deflation and slow growth following the Panic of 1873 and its debated status as a 'great depression'."),
            ("Amartya Sen's Famine Entitlement Theory", "Presents Sen's argument that famines result from failures of economic entitlement and distribution rather than simple food-supply shortages."),
            ("The Plaza Accord of 1985 and Exchange Rate Realignment", "Examines the coordinated 1985 intervention by major economies to depreciate the US dollar and its lasting effects on global trade imbalances."),
            ("Joseph Schumpeter and the Theory of Creative Destruction", "Explores Schumpeter's account of innovation-driven economic cycles in which new enterprises continuously displace outdated firms and technologies."),
        ],
    },
    "English": {
        "UG4": [
            ("The Harlem Renaissance: Literary Voices and Cultural Awakening", "Surveys the poetry, fiction, and criticism of the Harlem Renaissance as a landmark flowering of African American literary and artistic expression."),
        ],
    },
    "First Aid": {
        "UG4": [
            ("Managing Impaled Object Injuries: Stabilization Principles", "Covers the field principles of stabilizing rather than removing an impaled object and preparing a patient for safe transport."),
        ],
    },
    "MBA": {
        "UG4": [
            ("The Blockbuster-Netflix Case Study in Strategic Disruption", "Analyzes Blockbuster's decline and Netflix's rise as a case study in recognizing and responding to business-model disruption."),
        ],
    },
    "Physics": {
        "UG4": [
            ("The Michelson-Morley Experiment and the Search for Aether", "Examines the famous interferometer experiment that failed to detect a luminiferous aether, motivating the development of special relativity."),
            ("The Franck-Hertz Experiment and Quantized Atomic Energy Levels", "Covers the classic electron-collision experiment that provided direct evidence for discrete quantized energy levels in atoms."),
            ("The Casimir Effect and Vacuum Energy Fluctuations", "Explores the measurable attractive force between closely spaced conducting plates arising from quantum vacuum fluctuations."),
        ],
    },
    "Project Management": {
        "UG4": [
            ("The Sydney Opera House: A Case Study in Project Cost Overrun", "Analyzes the causes of the Sydney Opera House's dramatic schedule delays and cost overruns as a classic megaproject cautionary case."),
            ("The Denver International Airport Baggage System Failure: A Case Study", "Examines the failed automated baggage-handling system rollout at Denver International Airport as a case study in technology-project risk."),
            ("Monte Carlo Simulation for Project Schedule Risk", "Introduces Monte Carlo simulation techniques for modeling probabilistic schedule and cost outcomes under project uncertainty."),
            ("The Boston Big Dig: Lessons in Megaproject Management", "Reviews the Central Artery/Tunnel Project in Boston as a case study in managing scope, cost, and stakeholder pressures on a large infrastructure megaproject."),
            ("Critical Chain Project Management and Buffer Management", "Introduces the critical chain method's use of resource-constrained scheduling and strategically placed buffers to protect project completion dates."),
            ("The Channel Tunnel Project: Cross-Border Megaproject Governance", "Examines the governance and financing challenges of the Channel Tunnel project as a binational infrastructure megaproject."),
        ],
    },
    "Prompt Engineering": {
        "UG4": [
            ("Prompt Engineering for Chain-of-Density Summarization", "Covers the chain-of-density prompting technique for iteratively producing increasingly information-dense summaries from a language model."),
            ("Skeleton-of-Thought Prompting for Parallel Generation", "Introduces a prompting pattern that first generates an answer skeleton and then expands its points in parallel to reduce generation latency."),
            ("Prompt Engineering for SQL Query Generation from Natural Language", "Covers prompt design strategies for reliably translating natural-language questions into correct, schema-aware SQL queries."),
        ],
    },
    "UI/UX Design": {
        "UG4": [
            ("Dark Mode Design Systems: Color and Contrast Adaptation", "Covers the design considerations for adapting color palettes, elevation, and contrast when building a dark-mode variant of a design system."),
        ],
    },
    "World History": {
        "UG4": [
            ("The Congress of Vienna and the Balance of Power in Europe", "Examines the 1814-1815 Congress of Vienna's efforts to redraw European borders and establish a lasting balance-of-power settlement after Napoleon."),
        ],
    },
    "Philosophy": {
        "M1": [
            ("Simone Weil's Philosophy of Attention and Affliction", "Explores Simone Weil's account of attention as a moral and spiritual discipline and her reflections on affliction and suffering."),
        ],
    },
    "R": {
        "M1": [
            ("R for Ecology: Species Distribution Modeling with dismo", "Covers using the dismo package in R to build and evaluate species distribution models from occurrence and environmental raster data."),
        ],
    },
    "Critical Thinking": {
        "M2": [
            ("The Sorites Paradox and Vagueness in Philosophical Logic", "Examines the Sorites paradox of vagueness and surveys formal responses including supervaluationism, fuzzy logic, and epistemicism."),
        ],
    },
}
