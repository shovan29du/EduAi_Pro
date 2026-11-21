#!/usr/bin/env python3
"""Depth pass, M2 MBA: fill in real, hand-checked data_table content
for the M2 MBA lessons not covered by the earlier breadth-first batch.
Brings M2 MBA to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning corporate
strategy and M&A (real options, LBO structuring, post-merger
integration), governance and stakeholder theory, organizational
behavior/leadership, innovation and business model strategy, marketing
and pricing strategy, digital transformation strategy, corporate
finance strategy, operations/supply chain strategy, crisis and
turnaround management, nonmarket strategy, HR/talent strategy, and
emerging strategic domains (ESG, geopolitical risk, AI adoption);
l101-l120 are "Worked Analysis" companions reusing the data_table of
l1-l20 (direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch, so its data_table is hard-coded here for reuse
(it falls within l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_mba_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Real options valuation", "Values managerial flexibility (e.g. the option to expand or abandon a project) using option-pricing techniques"],
    ["Strategic capital budgeting", "Captures the value of staged, flexible investment decisions that traditional discounted cash flow analysis often ignores"],
])

CHARTS: dict[str, dict] = {
    "mba-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Business consulting skills", "Structured problem-solving, client communication, and analytical frameworks used to advise organizations"],
        ["Application", "Combines hypothesis-driven analysis with clear synthesis and recommendation delivery for executive stakeholders"],
    ])},
    "mba-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["MBA capstone", "An applied culminating project demonstrating integrated strategic and analytical business skill"],
        ["Deliverable", "Typically a comprehensive strategic analysis and recommendation for a real or simulated business challenge"],
    ])},
    "mba-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral agency theory", "Extends principal-agent theory by incorporating executives' psychological biases and risk preferences"],
        ["Executive compensation design", "Recognizes that executives don't always respond to incentives as purely rational, risk-neutral agents would"],
    ])},
    "mba-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic capabilities", "An organization's ability to sense, seize, and reconfigure resources to adapt to changing environments"],
        ["Sustained competitive advantage", "Argues that in fast-changing markets, the capacity to adapt matters more than any fixed set of static resources"],
    ])},
    "mba-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Platform strategy", "Builds a business around facilitating interactions between distinct groups of users"],
        ["Multi-sided market design", "Must balance pricing and features across each side of the platform to attract and retain all participant groups"],
    ])},
    "mba-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Post-merger integration", "The process of combining two organizations' operations, systems, and cultures after an acquisition closes"],
        ["Failure mode", "Common failure causes include cultural clashes, unrealistic synergy assumptions, and inadequate integration planning"],
    ])},
    "mba-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Leveraged buyout", "An acquisition financed primarily with borrowed money, using the target company's own assets and cash flows as collateral"],
        ["Value creation lever", "Includes operational improvement, multiple expansion, and financial leverage as the primary sources of LBO investment returns"],
    ])},
    "mba-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Corporate governance", "The system of rules and practices by which a company is directed and controlled"],
        ["Board effectiveness research", "Studies how board composition, independence, and processes relate to actual firm performance outcomes"],
    ])},
    "mba-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Activist investor campaign", "An investor acquires a stake in a company specifically to influence its strategy or management"],
        ["Shareholder value theory", "Empirical evidence on whether activist campaigns genuinely create long-term shareholder value remains debated"],
    ])},
    "mba-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Cross-border merger valuation", "Values an acquisition target operating in a different country with a different currency"],
        ["Currency risk", "Must incorporate exchange rate volatility and hedging costs into the valuation and deal structuring"],
    ])},
    "mba-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain finance", "Financial arrangements optimizing cash flow across a company's supply chain relationships"],
        ["Working capital optimization", "Techniques like supply chain financing can free up cash without straining supplier relationships"],
    ])},
    "mba-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["COSO framework", "A widely adopted framework for designing and evaluating an organization's internal control and enterprise risk management systems"],
        ["ISO 31000", "An international standard providing principles and guidelines for risk management applicable across all types of organizations"],
    ])},
    "mba-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Scenario planning", "Constructs multiple plausible future narratives to stress-test strategy against uncertainty, rather than predicting one future"],
        ["Strategic foresight application", "Aims to widen decision-makers' perceived range of possibilities rather than forecast a single outcome"],
    ])},
    "mba-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Blue ocean strategy", "Seeks to create uncontested market space rather than competing head-to-head in existing, crowded markets"],
        ["Value innovation", "Simultaneously pursues differentiation and low cost by fundamentally reshaping the industry's value proposition"],
    ])},
    "mba-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["VRIN framework", "Identifies resources as sources of sustained competitive advantage when they are Valuable, Rare, Inimitable, and Non-substitutable"],
        ["Dynamic resource fit", "Extends the static VRIN model to consider how well resources continue to fit a changing competitive environment over time"],
    ])},
    "mba-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Transaction cost economics", "Analyzes the costs of coordinating economic activity through markets versus internal organizational hierarchy"],
        ["Make-or-buy decision", "A firm should internalize an activity (make) when the transaction costs of contracting for it externally (buy) exceed internal coordination costs"],
    ])},
    "mba-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Ambidextrous organization", "Simultaneously pursues exploitation of existing capabilities and exploration of new opportunities"],
        ["Balancing exploration and exploitation", "Requires distinct organizational structures or processes since the two modes often require conflicting management approaches"],
    ])},
    "mba-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Corporate venture capital", "A large corporation invests in external startups to gain strategic insight or access to innovation"],
        ["Internal innovation ecosystem", "Complements internal R&D by tapping into external entrepreneurial innovation the corporation couldn't easily generate alone"],
    ])},
    "mba-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Disruptive innovation theory", "Clayton Christensen's theory that new entrants can displace incumbents by initially serving overlooked, low-end market segments"],
        ["Contemporary critique", "Later scholars have questioned the theory's predictive power and its applicability outside its original historical examples"],
    ])},
    "mba-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Business model canvas", "A visual framework mapping a business's value proposition, customers, channels, and economics across nine building blocks"],
        ["Business model innovation", "Systematically reconsidering these building blocks can reveal opportunities beyond incremental product improvement"],
    ])},
    "mba-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Strategic alliance governance", "The structures and mechanisms coordinating a partnership between independent firms"],
        ["Partner selection criteria", "Well-chosen partners share compatible strategic goals and complementary, non-overlapping resources"],
    ])},
    "mba-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Global value chain", "The full range of activities, spanning multiple countries, involved in bringing a product to market"],
        ["Governance structure", "Ranges from arm's-length market transactions to fully hierarchical ownership, depending on the complexity of coordination needed"],
    ])},
    "mba-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Institutional void", "The absence of well-functioning market-supporting institutions (like reliable contract enforcement) in an emerging market"],
        ["Market entry strategy", "Firms must adapt their strategy, sometimes building the missing institutional infrastructure themselves, to succeed despite these voids"],
    ])},
    "mba-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Base of the pyramid", "Refers to the largest, poorest socio-economic segment of the global population"],
        ["Business model design", "Requires radically rethinking product design, pricing, and distribution to serve this segment profitably and sustainably"],
    ])},
    "mba-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Corporate social responsibility", "A firm's voluntary commitments to social and environmental goals beyond legal requirements"],
        ["Shareholder value trade-off", "A long-debated question in strategy is whether CSR investments enhance or detract from long-run shareholder value"],
    ])},
    "mba-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["ESG integration", "Incorporates environmental, social, and governance factors directly into investment analysis and decision-making"],
        ["Institutional investment application", "Reflects growing evidence and investor demand that ESG factors can materially affect long-term financial performance"],
    ])},
    "mba-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Stakeholder theory", "Holds that a firm should be managed to balance the interests of all its stakeholders, not just shareholders"],
        ["Shareholder primacy debate", "Contests the traditional view that maximizing shareholder wealth is a firm's sole or primary legitimate objective"],
    ])},
    "mba-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Organizational culture change", "The process of deliberately shifting a company's shared values, norms, and behaviors"],
        ["Post-acquisition integration application", "Cultural mismatch between merging organizations is a commonly cited cause of failed post-acquisition integration"],
    ])},
    "mba-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Executive succession planning", "A structured process for identifying and developing future leaders to fill key executive roles"],
        ["CEO transition risk", "Poorly managed CEO transitions are associated with strategic drift and elevated stock price volatility"],
    ])},
    "mba-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Talent management analytics", "Applies data analysis to workforce decisions like hiring, development, and retention"],
        ["Predictive workforce planning", "Uses historical data to forecast future talent needs and risks, such as likely attrition"],
    ])},
    "mba-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Global mobility strategy", "Coordinates the deployment of employees across international locations for a multinational company"],
        ["Multinational workforce deployment", "Must navigate complex visa, tax, and cultural adaptation considerations across the countries involved"],
    ])},
    "mba-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Integrative bargaining", "A negotiation approach seeking mutually beneficial outcomes by expanding the total value available, rather than just dividing a fixed pie"],
        ["Value creation", "Contrasts with purely distributive bargaining, which treats negotiation as a zero-sum competition over a fixed resource"],
    ])},
    "mba-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["GLOBE study", "A large cross-cultural research project identifying dimensions of cultural variation and their relationship to leadership expectations"],
        ["Cross-cultural leadership competency", "Reveals that effective leadership behaviors vary significantly depending on a culture's specific values and norms"],
    ])},
    "mba-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Servant leadership", "A leadership philosophy prioritizing serving followers' growth and needs to enable their best performance"],
        ["Organizational performance outcome", "Research links servant leadership to improved employee engagement and, in some studies, firm performance"],
    ])},
    "mba-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Design thinking", "A human-centered problem-solving methodology emphasizing empathy, ideation, and rapid prototyping"],
        ["Strategic management methodology", "Increasingly applied beyond product design to broader strategic planning and organizational problem-solving"],
    ])},
    "mba-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Lean startup methodology", "Emphasizes rapid, iterative experimentation to validate a business idea before large-scale investment"],
        ["Corporate innovation lab application", "Adapted by large corporations to bring startup-style rapid validation discipline to internal innovation efforts"],
    ])},
    "mba-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic pricing", "Automatically adjusts prices in response to demand, competition, and inventory signals"],
        ["Algorithmic pricing model", "Uses algorithms, sometimes machine-learning-driven, to continuously optimize pricing decisions in real time"],
    ])},
    "mba-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Customer lifetime value", "The total predicted net value a business will generate from a customer over their entire relationship"],
        ["Strategic segmentation application", "Enables prioritizing marketing and retention investment toward the customer segments predicted to be most valuable"],
    ])},
    "mba-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Brand equity", "The value a brand adds to a product beyond its functional attributes, based on consumer perception"],
        ["Valuation methodology", "Methods estimate this value through approaches like price premium analysis or discounted future brand-attributable cash flows"],
    ])},
    "mba-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Marketing mix modeling", "Statistically estimates how different marketing channels contribute to a business outcome like sales"],
        ["Media attribution analytics", "Distributes credit for outcomes across marketing touchpoints, informing budget allocation decisions"],
    ])},
    "mba-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Digital transformation strategy", "A structured organizational plan for adopting digital technologies to fundamentally change how a business operates"],
        ["Legacy system migration", "A major practical challenge, since transformation often requires replacing deeply embedded legacy technology infrastructure"],
    ])},
    "mba-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["AI adoption strategy", "A structured organizational approach to identifying, piloting, and scaling artificial intelligence applications"],
        ["Enterprise operations application", "Requires balancing quick operational wins against building the longer-term data and talent foundation for sustained AI value"],
    ])},
    "mba-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Data monetization strategy", "Approaches for generating direct or indirect revenue value from an organization's data assets"],
        ["Information asset valuation", "Requires methods for quantifying the economic value of data, which lacks the established valuation conventions of physical assets"],
    ])},
    "mba-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Cybersecurity risk governance", "Board-level oversight structures and processes for managing an organization's cybersecurity risk"],
        ["Board-level application", "Increasingly treated as a core governance responsibility given cybersecurity's significant potential financial and reputational impact"],
    ])},
    "mba-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Sustainability-linked financing", "Loan or bond terms tied to a borrower achieving specific sustainability performance targets"],
        ["Green bond structuring", "Green bonds specifically earmark proceeds for environmentally beneficial projects, distinct from broader sustainability-linked instruments"],
    ])},
    "mba-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Circular economy business model", "A business model minimizing waste by keeping resources in use through reuse, repair, and recycling"],
        ["Transformation application", "Requires rethinking product design, revenue models, and supply chains around durability and material recovery"],
    ])},
    "mba-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral economics", "Studies systematic deviations from rational choice that affect decision-making"],
        ["Organizational decision-making application", "Applied to understand and design against biases like anchoring and overconfidence in corporate decisions"],
    ])},
    "mba-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Game-theoretic competitive strategy", "Analyzes strategic interactions among a small number of competing firms using formal game theory"],
        ["Oligopolistic competition model", "Models how firms' pricing and capacity decisions depend on anticipating rivals' likely responses"],
    ])},
    "mba-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Innovation diffusion theory", "Explains how, why, and at what rate new ideas and products spread through a population"],
        ["Market adoption curve", "The classic S-shaped adoption curve segments adopters into innovators, early adopters, early/late majority, and laggards"],
    ])},
    "mba-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Strategic human capital theory", "Views a firm's employee skills and knowledge as a strategic resource contributing to competitive advantage"],
        ["Firm performance link", "Research examines how investment in and management of human capital translates into measurable firm performance outcomes"],
    ])},
    "mba-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Family business governance", "Governance structures balancing family ownership dynamics with professional business management"],
        ["Succession dynamics", "Family business succession introduces unique challenges around family relationships alongside standard leadership transition concerns"],
    ])},
    "mba-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Private equity value creation playbook", "A structured set of operational and financial levers PE firms apply to improve portfolio company performance"],
        ["Application", "Typically combines operational improvements, strategic repositioning, and financial engineering"],
    ])},
    "mba-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Venture capital term sheet", "A document outlining the key terms and conditions of a proposed venture investment"],
        ["Deal economics", "Terms like valuation, liquidation preference, and board seats significantly affect the ultimate economic split between founders and investors"],
    ])},
    "mba-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["IPO underpricing", "Newly issued shares are systematically priced below their subsequent first-day trading value"],
        ["Timing anomaly", "Both underpricing and the observed clustering of IPOs during favorable market windows remain active research puzzles"],
    ])},
    "mba-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Trade-off theory (capital structure)", "Firms balance the tax benefits of debt against the increased risk of financial distress to find an optimal capital structure"],
        ["Pecking order theory", "Firms prefer internal financing first, then debt, and equity issuance last, due to information asymmetry costs"],
    ])},
    "mba-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral corporate finance", "Studies how managerial psychological biases affect corporate financial decisions"],
        ["Managerial overconfidence", "Overconfident executives tend to overinvest and overestimate the success of major deals, a well-documented pattern in the finance literature"],
    ])},
    "mba-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Transfer pricing", "The price charged for transactions between related entities of a multinational company"],
        ["Tax optimization strategy", "Multinationals can strategically set transfer prices to shift profits toward lower-tax jurisdictions, subject to regulatory scrutiny"],
    ])},
    "mba-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Currency hedging strategy", "Techniques multinational firms use to manage exposure to exchange rate fluctuations"],
        ["Treasury operations application", "Includes forward contracts, options, and natural hedges like matching foreign-currency revenues to costs"],
    ])},
    "mba-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sovereign risk assessment", "Evaluates the risk that a country's government actions or instability could harm a foreign investment"],
        ["International market entry application", "Informs decisions about which markets to enter and what risk mitigation structures to use"],
    ])},
    "mba-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Strategic alliance (pharmaceutical R&D)", "Collaborative agreements between pharmaceutical companies to jointly develop new drugs"],
        ["Global R&D application", "Shares the enormous cost and risk of drug development while combining complementary scientific and commercial capabilities"],
    ])},
    "mba-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Operations strategy trade-off", "Operational decisions typically require balancing competing objectives like cost, quality, and flexibility"],
        ["Trade-off framework", "Firms must explicitly choose which priorities to emphasize, since maximizing all simultaneously is rarely feasible"],
    ])},
    "mba-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Six Sigma", "A structured methodology (DMAIC) for reducing process variation and defects"],
        ["Lean management integration", "Combines Six Sigma's statistical rigor with Lean's waste-elimination focus for comprehensive enterprise process improvement"],
    ])},
    "mba-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain resilience", "A supply chain's ability to withstand and recover from significant disruptions"],
        ["Post-disruption strategy", "Strategies like supplier diversification and increased inventory buffers have gained prominence following major recent disruptions"],
    ])},
    "mba-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Reverse logistics", "The process of moving goods from their final destination back through the supply chain for return, repair, or recycling"],
        ["Closed-loop supply chain design", "Integrates forward and reverse flows into a single system designed for material recovery and reuse"],
    ])},
    "mba-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Strategic sourcing", "A systematic approach to selecting suppliers that optimizes total value, not just lowest price"],
        ["Supplier relationship portfolio management", "Segments suppliers by strategic importance, applying different relationship management approaches to each segment"],
    ])},
    "mba-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Corporate turnaround strategy", "A structured plan for restoring a declining company to financial and operational health"],
        ["Organizational crisis management", "Requires rapid, decisive action across cost structure, strategy, and stakeholder communication during a crisis"],
    ])},
    "mba-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Bankruptcy reorganization", "A legal process allowing a financially distressed company to restructure its debts while continuing operations"],
        ["Stakeholder negotiation strategy", "Requires negotiating competing claims among creditors, shareholders, and other stakeholders within the reorganization process"],
    ])},
    "mba-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Nonmarket strategy", "Manages a firm's relationships with government, regulators, and other non-market stakeholders"],
        ["Regulatory and political risk management", "Complements traditional market-based competitive strategy by addressing risks arising from the political and regulatory environment"],
    ])},
    "mba-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Antitrust strategy (digital platforms)", "How large digital platform companies navigate increasing antitrust scrutiny and potential regulatory intervention"],
        ["Digital platform market application", "A rapidly evolving area given growing regulatory concern about market power in digital platform businesses"],
    ])},
    "mba-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Say-on-pay regulation", "Requires companies to hold shareholder votes, often non-binding, on executive compensation packages"],
        ["Executive compensation design under regulation", "Compensation committees must design packages that can withstand shareholder scrutiny under these voting requirements"],
    ])},
    "mba-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Diversity, equity, and inclusion strategy", "Organizational initiatives aimed at building a more diverse and equitable workforce and culture"],
        ["Firm performance link", "Research on the relationship between DEI initiatives and firm financial performance shows a range of findings across studies"],
    ])},
    "mba-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Organizational network analysis", "Analyzes the informal relationships and communication patterns within an organization, distinct from the formal org chart"],
        ["Informal influence mapping", "Reveals actual influential connectors and information brokers who may not hold formal leadership titles"],
    ])},
    "mba-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Kotter's change model", "An eight-step framework for leading organizational change, from establishing urgency to anchoring new approaches in culture"],
        ["Application in practice", "Widely used, though practitioners note that real-world change often requires adapting the linear model to a more iterative process"],
    ])},
    "mba-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Knowledge management system", "Captures, organizes, and makes accessible an organization's collective knowledge and expertise"],
        ["Organizational learning theory", "Connects knowledge management practice to broader theories of how organizations learn and improve over time"],
    ])},
    "mba-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Strategic foresight", "Systematic processes for anticipating and preparing for future possibilities"],
        ["Weak signal detection", "Identifies early, faint indicators of emerging trends before they become obvious, giving organizations a strategic head start"],
    ])},
    "mba-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Corporate reputation management", "Actively shapes and protects how external stakeholders perceive an organization"],
        ["Crisis communication strategy", "Requires rapid, transparent, and consistent messaging to limit reputational damage during a crisis event"],
    ])},
    "mba-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["International joint venture governance", "Structures for managing a jointly owned business entity between partners from different countries"],
        ["Conflict resolution", "Must anticipate and provide mechanisms for resolving disagreements arising from partners' differing goals and cultural expectations"],
    ])},
    "mba-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Digital ecosystem orchestration", "Coordinates a network of complementary partners around a central digital platform"],
        ["Complementor management", "Balances the platform's own interests against maintaining a healthy, motivated ecosystem of third-party complementors"],
    ])},
    "mba-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Subscription economy business model", "Generates recurring revenue through ongoing subscription relationships rather than one-time transactions"],
        ["Churn analytics", "Analyzes and predicts customer cancellation to inform retention strategy, a critical metric for subscription business health"],
    ])},
    "mba-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Activity-based costing", "Assigns overhead costs to products or services based on the specific activities that actually drive those costs"],
        ["Strategic cost management at scale", "Provides more accurate cost visibility than traditional broad overhead allocation, informing better strategic pricing and product decisions"],
    ])},
    "mba-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Corporate diversification strategy", "A firm's decision to expand into multiple, potentially unrelated business lines"],
        ["Conglomerate discount", "Diversified conglomerates often trade at a valuation discount relative to the sum of their individual business units' standalone value"],
    ])},
    "mba-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Spin-off", "Separates a business unit into an independent, publicly traded company"],
        ["Divestiture value unlocking", "Can unlock shareholder value when the market values focused, independent businesses more highly than a diversified parent"],
    ])},
    "mba-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Strategic HR analytics", "Applies data analysis to workforce strategy decisions at an organizational level"],
        ["Retention modeling", "Predicts which employees are at highest risk of leaving, enabling targeted, proactive retention interventions"],
    ])},
    "mba-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Agile organizational design", "Structures teams and decision-making for rapid adaptation, originally developed in software but now applied broadly"],
        ["Beyond software development application", "Extends agile principles like cross-functional teams and iterative planning to non-software business functions"],
    ])},
    "mba-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Corporate philanthropy strategy", "A firm's structured approach to charitable giving and community investment"],
        ["Shared value creation", "Frames philanthropy as most effective when it also aligns with and reinforces the firm's core competitive strategy"],
    ])},
    "mba-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["International trade policy", "Government policies governing tariffs, quotas, and trade agreements between countries"],
        ["Multinational strategy impact", "Trade policy shifts can significantly reshape multinational firms' sourcing, manufacturing location, and pricing strategies"],
    ])},
    "mba-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Robust decision-making", "A strategic decision framework designed to perform well across many possible future scenarios, rather than optimizing for one predicted future"],
        ["Deep uncertainty application", "Particularly valuable when future conditions are so uncertain that assigning reliable probabilities to different scenarios isn't feasible"],
    ])},
    "mba-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Corporate innovation metrics", "Quantitative measures used to track and manage an organization's innovation activities and outcomes"],
        ["Portfolio balancing", "Metrics help ensure an innovation portfolio balances incremental, adjacent, and transformational initiatives appropriately"],
    ])},
    "mba-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Executive decision bias (M&A)", "Systematic psychological biases, like overconfidence and confirmation bias, that affect executive judgment during acquisitions"],
        ["M&A application", "A significant contributor to the well-documented pattern of overpayment and poor strategic fit in many acquisitions"],
    ])},
    "mba-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Strategic human capital investment", "Deliberate organizational investment in developing employee skills for emerging, strategically important roles"],
        ["Emerging technology role application", "Addresses talent gaps in fast-evolving areas like AI and data science where external hiring alone may be insufficient"],
    ])},
    "mba-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["State-owned enterprise governance", "Governance structures for companies that are wholly or partially owned by a government"],
        ["Hybrid enterprise application", "Must balance commercial objectives with the political and social mandates often attached to state ownership"],
    ])},
    "mba-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Global talent war strategy", "An organization's approach to competing for scarce, highly sought-after talent in a global labor market"],
        ["Employer value proposition design", "Articulates what a company distinctively offers employees to attract and retain talent amid intense competition"],
    ])},
    "mba-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Coopetition", "Simultaneous cooperation and competition between firms that are otherwise rivals"],
        ["Theory", "Explains how competitors can benefit from collaborating on shared infrastructure or standards while still competing on other dimensions"],
    ])},
    "mba-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Corporate restructuring (activist pressure)", "Organizational and strategic changes a company undertakes in response to activist investor demands"],
        ["Activist pressure campaign application", "Restructuring under activist pressure often includes divestitures, cost cuts, or governance changes demanded by the activist"],
    ])},
    "mba-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Digital platform antitrust remedy", "Regulatory interventions addressing perceived anticompetitive behavior by large digital platforms"],
        ["Structural separation", "A particularly aggressive remedy requiring a platform to divest or separate parts of its business to restore competition"],
    ])},
    "mba-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Enterprise architecture strategy", "A structured approach to aligning an organization's technology systems with its business strategy"],
        ["Legacy system rationalization", "Systematically identifies which legacy systems to modernize, replace, or retire to reduce technical debt and cost"],
    ])},
    "mba-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Strategic workforce reskilling", "Organizational programs to retrain employees for new roles as automation changes job requirements"],
        ["Automation-driven disruption application", "A proactive strategy to retain and redeploy talent rather than relying solely on external hiring or layoffs"],
    ])},
    "mba-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Geopolitical supply chain risk", "The risk that political tensions or conflicts between countries disrupt a firm's global supply chain"],
        ["Corporate strategy application", "Has driven increased corporate interest in supply chain diversification and regionalization strategies"],
    ])},
    "mba-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Thesis capstone", "A culminating project requiring original strategic consulting research on a genuine business challenge"],
        ["Original strategic consulting research project", "Requires identifying a real strategic gap and developing a rigorously supported, actionable recommendation"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["MBA"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"mba-m2-l{base_n}"
        worked_key = f"mba-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 MBA lessons.")


if __name__ == "__main__":
    main()
