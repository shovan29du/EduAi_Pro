#!/usr/bin/env python3
"""Depth pass, M2 Operations Management: fill in real, hand-checked
data_table content for the M2 Operations Management lessons not
covered by the earlier breadth-first batch. Brings M2 Operations
Management to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning
stochastic inventory theory and supply chain contracts, revenue
management and pricing, queueing theory and service operations, supply
chain network design and resilience, logistics and distribution
optimization, sustainable/circular operations, lean/quality
methodology, digital manufacturing (digital twins, predictive
maintenance), behavioral operations, healthcare operations research,
data-driven/prescriptive analytics, platform and gig-economy
operations, procurement and supply risk, project scheduling theory,
and advanced operational optimization methods; l101-l120 are "Worked
Analysis" companions reusing the data_table of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch,
so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_operations_management_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Newsvendor model", "Determines the optimal order quantity for a perishable product balancing overstock and understock costs"],
    ["Stochastic inventory theory extension", "Extends the classical single-period model to more realistic settings with correlated or dynamic demand"],
])

CHARTS: dict[str, dict] = {
    "operations-management-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Operations technology", "Digital tools and systems supporting the planning and execution of operational processes"],
        ["Automation application", "Automating repetitive operational tasks frees capacity for higher-value decision-making and exception handling"],
    ])},
    "operations-management-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Operations management capstone", "An applied culminating project demonstrating end-to-end operations analysis and design skill"],
        ["Deliverable", "Typically includes process analysis, quantitative modeling, and evaluation of a real or simulated operational problem"],
    ])},
    "operations-management-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Multi-echelon inventory optimization", "Jointly optimizes inventory levels across multiple stages of a supply chain rather than each stage independently"],
        ["Application", "Captures interactions between stages that single-echelon optimization would miss, often reducing total system-wide inventory"],
    ])},
    "operations-management-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Bullwhip effect", "Order variability amplifies as it moves upstream through a supply chain, even when end-customer demand is relatively stable"],
        ["Mitigation strategy", "Includes information sharing, shorter lead times, and stable pricing to reduce the distortions that amplify demand variability"],
    ])},
    "operations-management-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Vendor-managed inventory", "The supplier, rather than the buyer, takes responsibility for managing and replenishing inventory at the buyer's location"],
        ["Contract design", "Must align incentives so the supplier is motivated to maintain appropriate inventory levels rather than over- or under-stocking"],
    ])},
    "operations-management-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Revenue management", "Optimizes pricing and inventory allocation across customer segments to maximize total revenue"],
        ["Dynamic pricing optimization", "Adjusts prices in real time based on remaining capacity and time until a perishable service or product expires"],
    ])},
    "operations-management-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Buyback contract", "A supply chain contract where the supplier agrees to repurchase unsold inventory from the buyer at a specified price"],
        ["Revenue-sharing contract", "Aligns supply chain incentives by having the buyer share a portion of realized revenue with the supplier, rather than paying a fixed wholesale price"],
    ])},
    "operations-management-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Robust optimization", "Finds decisions that perform well across a range of possible parameter values, rather than optimizing for one assumed scenario"],
        ["Supply chain design application", "Useful when demand or cost parameters are uncertain and a single point-estimate optimization could perform poorly"],
    ])},
    "operations-management-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic programming", "An optimization framework explicitly incorporating probability distributions over uncertain parameters into the decision model"],
        ["Capacity planning under uncertainty", "Determines capacity investment decisions that perform well across the range of possible future demand scenarios"],
    ])},
    "operations-management-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Queueing theory", "Mathematical study of waiting lines, modeling arrival rates, service rates, and resulting wait times"],
        ["Service operations application", "Applied to determine appropriate staffing and capacity levels to meet target customer wait-time service levels"],
    ])},
    "operations-management-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Fluid approximation", "Approximates a large-scale stochastic queueing system's average behavior using deterministic differential equations"],
        ["Diffusion approximation", "A more refined approximation capturing the random fluctuations around the fluid-level average behavior"],
    ])},
    "operations-management-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Yield management", "Dynamically adjusts pricing and allocation of a fixed, perishable capacity to maximize total revenue"],
        ["Airline and hospitality application", "A classic and highly developed application domain given these industries' fixed capacity and perishable inventory"],
    ])},
    "operations-management-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Assemble-to-order system", "Holds inventory of standardized components, assembling them into a final product only after receiving a customer order"],
        ["Component commonality", "Using shared components across multiple end products reduces overall inventory needed to meet varied demand"],
    ])},
    "operations-management-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Postponement strategy", "Delays product differentiation as late as possible in the supply chain to maintain flexibility"],
        ["Global supply chain design application", "Reduces the risk of holding the wrong finished-product mix by keeping products generic longer"],
    ])},
    "operations-management-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Risk pooling", "Aggregating demand across multiple locations or products reduces relative demand variability due to statistical averaging"],
        ["Distribution network design application", "A key rationale for centralizing inventory, since pooled demand is proportionally less variable than the sum of separate local demands"],
    ])},
    "operations-management-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Facility location model", "Determines optimal locations for facilities (warehouses, plants) to minimize cost while meeting demand"],
        ["Disruption risk", "Modern models incorporate the risk that a facility becomes unavailable, favoring designs resilient to potential disruptions"],
    ])},
    "operations-management-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Supply chain resilience", "A supply chain's ability to withstand and recover from significant disruptions"],
        ["Disruption recovery strategy", "Includes strategies like supplier diversification, safety stock, and flexible capacity to speed recovery"],
    ])},
    "operations-management-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Network flow optimization", "Determines the most efficient way to route goods through a network of nodes and links subject to capacity constraints"],
        ["Global logistics application", "Underlies decisions about which routes and transportation modes to use to move goods across a global network"],
    ])},
    "operations-management-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Vehicle routing problem", "Determines optimal delivery routes for a fleet of vehicles serving a set of customers"],
        ["Advanced metaheuristic solution", "Techniques like genetic algorithms and tabu search find high-quality solutions to this NP-hard problem within practical time limits"],
    ])},
    "operations-management-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Cross-docking", "Transfers incoming shipments directly to outbound vehicles with minimal or no intermediate storage"],
        ["Operations design and scheduling", "Requires tight coordination of inbound and outbound schedules to avoid unnecessary staging delays"],
    ])},
    "operations-management-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Warehouse slotting", "Determines the optimal physical placement of products within a warehouse to minimize picking time and effort"],
        ["Optimization model", "Places high-velocity items in easily accessible locations, reducing overall order fulfillment time"],
    ])},
    "operations-management-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Last-mile delivery optimization", "Minimizes the cost and time of the final delivery leg from a distribution point to the end customer"],
        ["Micro-fulfillment design", "Small, strategically located fulfillment centers close to customers can significantly reduce last-mile delivery time and cost"],
    ])},
    "operations-management-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Closed-loop supply chain", "Integrates forward product distribution with reverse flows for return, repair, or recycling"],
        ["Sustainable design application", "Designs the supply chain from the outset to support material recovery and product lifecycle extension"],
    ])},
    "operations-management-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Circular economy model", "An economic model minimizing waste by keeping resources in use through reuse, repair, and recycling"],
        ["Operations strategy application", "Requires rethinking product design and supply chain flows around material recovery rather than one-way consumption"],
    ])},
    "operations-management-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Carbon footprint optimization", "Explicitly incorporates carbon emissions as a cost or constraint in supply chain network design decisions"],
        ["Application", "Balances traditional cost objectives against emissions reduction goals when designing transportation and facility networks"],
    ])},
    "operations-management-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Green supplier selection", "Evaluates and chooses suppliers based on environmental performance criteria alongside traditional cost and quality factors"],
        ["Sustainable sourcing model", "Formalizes environmental criteria into the supplier evaluation and selection process"],
    ])},
    "operations-management-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Total productive maintenance", "A maintenance philosophy involving all employees in maximizing equipment effectiveness and minimizing downtime"],
        ["Reliability-centered maintenance", "Systematically determines the most effective maintenance strategy for each piece of equipment based on its failure modes"],
    ])},
    "operations-management-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Statistical process control", "Uses control charts to monitor a process and detect when it deviates from expected statistical behavior"],
        ["Multivariate quality monitoring", "Extends control charting to simultaneously monitor multiple correlated quality characteristics"],
    ])},
    "operations-management-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Theory of constraints", "Focuses improvement efforts on identifying and elevating a system's single most limiting bottleneck"],
        ["Throughput accounting", "An alternative to traditional cost accounting that prioritizes decisions maximizing throughput through the system's constraint"],
    ])},
    "operations-management-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Lean Six Sigma", "Combines Lean's waste elimination focus with Six Sigma's statistical variation reduction methodology"],
        ["Complex service system integration", "Adapting manufacturing-origin lean/six sigma tools to the more variable, less repeatable nature of complex services"],
    ])},
    "operations-management-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Value stream mapping", "Visualizes all the steps, delays, and information flows involved in delivering a product or service"],
        ["Complex multi-product process application", "More challenging to construct and interpret when multiple product lines share overlapping process steps"],
    ])},
    "operations-management-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Kanban system", "A visual signaling system that triggers production or replenishment only when downstream demand actually occurs"],
        ["Pull production theory", "Contrasts with push production, which schedules output based on forecasts rather than actual downstream consumption signals"],
    ])},
    "operations-management-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Constraint-based scheduling", "Formulates job shop scheduling as a constraint satisfaction problem, finding a feasible sequence meeting all specified constraints"],
        ["Job shop application", "Well suited to complex scheduling scenarios with many interdependent constraints that simple dispatch rules can't easily satisfy"],
    ])},
    "operations-management-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Flexible manufacturing system", "A production system capable of adapting to produce a variety of products with minimal reconfiguration"],
        ["Design and control", "Balances the higher upfront cost of flexible equipment against the operational benefit of adapting quickly to changing product mixes"],
    ])},
    "operations-management-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Digital twin", "A virtual, continuously updated model of a physical asset or process"],
        ["Manufacturing process optimization", "Enables simulating and testing process changes virtually before implementing them on the actual physical production line"],
    ])},
    "operations-management-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Predictive maintenance", "Uses sensor data to predict equipment failures before they occur, enabling proactive maintenance"],
        ["Sensor data analytics application", "Reduces unplanned downtime compared with purely scheduled or reactive maintenance approaches"],
    ])},
    "operations-management-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Additive manufacturing", "Builds parts layer by layer directly from a digital design, as opposed to traditional subtractive manufacturing"],
        ["Supply chain implication", "Enables on-demand, distributed production, potentially reducing the need for large centralized inventories of certain parts"],
    ])},
    "operations-management-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Reshoring", "Relocating manufacturing or sourcing back to a company's home country after previously offshoring it"],
        ["Geopolitical risk strategy", "Increasingly considered as a way to reduce exposure to geopolitical tensions and long-distance supply chain disruption"],
    ])},
    "operations-management-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral operations management", "Studies how real human cognitive biases affect operational decision-making, departing from purely rational-agent models"],
        ["Cognitive bias application", "Reveals systematic, predictable deviations from textbook-optimal operational decisions observed in actual practice"],
    ])},
    "operations-management-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Pull-to-center effect", "Decision-makers in newsvendor experiments systematically order quantities biased toward the mean demand, deviating from the profit-maximizing quantity"],
        ["Newsvendor decision bias", "A well-documented behavioral anomaly showing real ordering decisions differ systematically from the theoretically optimal newsvendor solution"],
    ])},
    "operations-management-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral contract design", "Incorporates behavioral biases of contracting parties into supply chain contract design, rather than assuming pure rationality"],
        ["Supply chain coordination application", "Contracts assuming perfect rationality can perform worse in practice than contracts designed accounting for known biases"],
    ])},
    "operations-management-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Operations-marketing interface", "Studies the interaction between pricing and inventory decisions, which are traditionally managed by separate functions"],
        ["Joint pricing and inventory decision", "Jointly optimizing both decisions typically outperforms optimizing each function's decisions independently"],
    ])},
    "operations-management-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Service operations design", "Structures a service delivery system's processes and capacity"],
        ["Capacity and demand synchronization", "Since services generally can't be inventoried, matching capacity to fluctuating demand in real time is a central design challenge"],
    ])},
    "operations-management-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Healthcare operations research", "Applies operations research methods to improve healthcare delivery processes"],
        ["Patient flow optimization", "Models how patients move through a healthcare system to identify and reduce bottlenecks causing delays"],
    ])},
    "operations-management-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Operating room scheduling", "Assigns surgical cases to available operating room time slots"],
        ["Scheduling under uncertainty", "Must account for uncertain surgery durations, which can cause costly overtime or underutilized capacity if poorly estimated"],
    ])},
    "operations-management-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Emergency department capacity planning", "Determines appropriate staffing and resource levels to handle emergency department patient volume"],
        ["Model", "Must account for highly variable and unpredictable arrival patterns characteristic of emergency care"],
    ])},
    "operations-management-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Blood supply chain management", "Coordinates the collection, storage, and distribution of donated blood products"],
        ["Perishability modeling", "Blood products have strict, short shelf lives, requiring careful inventory management to minimize both shortages and waste"],
    ])},
    "operations-management-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Multi-objective optimization", "Finds solutions that balance trade-offs among several competing objectives rather than optimizing just one"],
        ["Sustainable operations design application", "Balances traditional cost objectives against environmental and social sustainability objectives simultaneously"],
    ])},
    "operations-management-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Simulation-based optimization", "Combines simulation models with optimization search to find good decisions for complex, uncertain operational systems"],
        ["Complex operational system application", "Well suited when a system is too complex for closed-form analytical optimization but can be effectively simulated"],
    ])},
    "operations-management-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Discrete-event simulation", "Models a system as a sequence of discrete events changing system state at specific points in time"],
        ["Process redesign methodology", "Enables testing proposed process changes virtually before costly real-world implementation"],
    ])},
    "operations-management-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Agent-based modeling", "Simulates a system as a collection of autonomous, interacting agents following individual behavioral rules"],
        ["Supply chain dynamics application", "Captures emergent system-level behavior arising from the interaction of many individually simple decision rules"],
    ])},
    "operations-management-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Data-driven demand forecasting", "Uses statistical and machine learning models trained on historical data to predict future demand"],
        ["Machine learning approach", "Can capture complex nonlinear demand patterns that traditional time series methods might miss"],
    ])},
    "operations-management-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Prescriptive analytics", "Goes beyond predicting outcomes to recommend specific actions that optimize a decision"],
        ["Operational decision-making application", "Combines forecasting with optimization to directly generate actionable operational recommendations"],
    ])},
    "operations-management-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic capacity allocation", "Continuously adjusts allocated compute or service capacity in response to real-time demand"],
        ["Cloud service operations application", "Enables efficient resource utilization by scaling capacity up or down as actual demand fluctuates"],
    ])},
    "operations-management-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Two-sided market matching", "Connects two distinct groups of platform participants (e.g. drivers and riders) efficiently"],
        ["Platform operations pricing", "Sets prices on both sides of the market to balance supply and demand while maintaining platform sustainability"],
    ])},
    "operations-management-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Gig economy workforce scheduling", "Matches independent gig workers to tasks or shifts in a flexible, on-demand labor marketplace"],
        ["Matching algorithm", "Balances worker preferences and availability against fluctuating task demand to optimize overall marketplace efficiency"],
    ])},
    "operations-management-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Crowdsourced delivery", "Uses a distributed network of independent couriers, rather than a dedicated fleet, to fulfill deliveries"],
        ["Network design application", "Offers flexible capacity scaling but requires careful incentive and routing design to ensure reliable service"],
    ])},
    "operations-management-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Omnichannel retail operations", "Integrates inventory and fulfillment across online and physical retail channels into a unified system"],
        ["Inventory integration application", "Enables capabilities like buy-online-pickup-in-store by treating inventory across channels as a single shared pool"],
    ])},
    "operations-management-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic assortment optimization", "Adjusts which products are offered over time based on observed demand patterns"],
        ["Demand learning application", "Balances exploring which products sell well against exploiting current knowledge of proven top performers"],
    ])},
    "operations-management-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Multi-armed bandit", "Balances exploring uncertain options against exploiting known good ones to maximize cumulative reward"],
        ["Operational experimentation application", "Applied to operational decisions like pricing or assortment where the best option must be learned through ongoing experimentation"],
    ])},
    "operations-management-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Forecast combination", "Combines predictions from multiple individual forecasting models into a single, often more accurate, ensemble forecast"],
        ["Ensemble method", "Diverse forecasting models often make different errors, so combining them can reduce overall forecast error"],
    ])},
    "operations-management-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Sales and operations planning", "A structured process aligning sales forecasts, production plans, and financial plans across an organization"],
        ["Integration framework", "Ensures demand and supply planning decisions are made consistently across different functional areas"],
    ])},
    "operations-management-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Master production schedule", "A detailed plan specifying what products to produce and when, over a planning horizon"],
        ["Rolling horizon uncertainty", "Must be periodically re-planned as new information arrives, balancing plan stability against responsiveness to changing conditions"],
    ])},
    "operations-management-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Capacitated lot-sizing problem", "Determines production quantities and timing over multiple periods subject to capacity constraints"],
        ["Advanced formulation", "Extended formulations incorporate setup costs, backlogging, and multi-item interactions for more realistic production planning"],
    ])},
    "operations-management-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Inventory-dependent demand pricing", "Sets prices accounting for the fact that observed inventory levels themselves can influence customer demand"],
        ["Dynamic pricing application", "Captures effects like scarcity signaling, where low visible inventory can increase perceived urgency and demand"],
    ])},
    "operations-management-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Procurement auction design", "Structures a competitive bidding process for selecting and pricing supplier contracts"],
        ["Strategic sourcing application", "Well-designed auction formats can significantly reduce procurement costs while maintaining supplier participation incentives"],
    ])},
    "operations-management-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Supplier risk assessment", "Evaluates the likelihood and potential impact of a supplier's failure to deliver as expected"],
        ["Network analysis application", "Maps supplier interdependencies to reveal hidden concentration risk beyond direct, immediately visible suppliers"],
    ])},
    "operations-management-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Multi-tier supply chain visibility", "Tracks and monitors suppliers beyond just direct, first-tier relationships"],
        ["Traceability system", "Enables identifying risks or issues originating deep in the supply chain that direct-supplier-only monitoring would miss"],
    ])},
    "operations-management-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Blockchain provenance tracking", "Uses a shared, tamper-resistant ledger to record a product's origin and chain of custody through the supply chain"],
        ["Supply chain application", "Provides verifiable proof of a product's authenticity and handling history to all parties in the chain"],
    ])},
    "operations-management-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Operations strategy trade-off", "Operational decisions typically require balancing competing objectives like cost, quality, and flexibility"],
        ["Framework", "Firms must explicitly choose which priorities to emphasize, since maximizing all simultaneously is rarely feasible"],
    ])},
    "operations-management-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Real options theory (capacity investment)", "Values managerial flexibility in the timing of capacity investment decisions using option-pricing techniques"],
        ["Investment timing application", "Captures the value of waiting for more demand information before committing to an irreversible capacity expansion"],
    ])},
    "operations-management-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Global supply chain network design", "Determines the optimal configuration of facilities and flows across an international supply chain"],
        ["Tariff uncertainty application", "Must account for the risk of future tariff changes, which can significantly alter the cost-optimal network configuration"],
    ])},
    "operations-management-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Inventory routing problem", "Jointly optimizes vehicle routing and inventory replenishment decisions rather than treating them separately"],
        ["Integrated distribution decision", "Coordinating routing and inventory decisions together typically outperforms optimizing each independently"],
    ])},
    "operations-management-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Perishable inventory management", "Manages inventory of products with a limited useful shelf life"],
        ["Age-dependent demand", "Models how customer demand may itself depend on a product's remaining freshness or age, complicating optimal ordering"],
    ])},
    "operations-management-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Dual sourcing", "Procures a component or product from two suppliers rather than relying on a single source"],
        ["Supply disruption risk mitigation", "Provides redundancy that reduces the impact of a single supplier's failure, at the cost of reduced volume-based pricing leverage"],
    ])},
    "operations-management-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Newsvendor network", "Extends the classical single-product newsvendor model to settings with multiple substitutable products"],
        ["Substitutable product inventory", "Accounts for the fact that unmet demand for one product may shift to a similar substitute product rather than being lost entirely"],
    ])},
    "operations-management-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Operational hedging", "Uses operational flexibility (like dual sourcing or flexible capacity) rather than financial instruments to manage risk"],
        ["Exchange rate and commodity risk application", "Complements financial hedging by building resilience directly into the operational structure of the supply chain"],
    ])},
    "operations-management-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Resource-constrained project scheduling problem", "Schedules project tasks accounting for both precedence relationships and limited shared resources"],
        ["Advanced scheduling", "A classic NP-hard scheduling problem central to realistic project planning beyond simple critical path analysis"],
    ])},
    "operations-management-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Critical chain project management", "Focuses project scheduling on the resource-constrained longest path, adding buffers to protect the overall project completion date"],
        ["Theory", "Addresses behavioral tendencies like student syndrome and multitasking that traditional critical path methods don't explicitly account for"],
    ])},
    "operations-management-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Agile project management", "An iterative approach to project management emphasizing flexibility and incremental delivery"],
        ["Hybrid application in operations", "Combines agile's adaptability with traditional operations management's structured planning for projects with evolving requirements"],
    ])},
    "operations-management-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian methods (operational risk)", "Updates probability estimates of operational risk as new evidence becomes available, using Bayes' theorem"],
        ["Risk quantification application", "Provides a principled way to combine prior risk assessments with newly observed operational incident data"],
    ])},
    "operations-management-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Digital supply chain transformation", "The process of integrating digital technologies throughout supply chain planning and execution"],
        ["IoT integration", "Internet of Things sensors provide real-time visibility into inventory, equipment, and shipment status across the supply chain"],
    ])},
    "operations-management-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Machine learning anomaly detection", "Identifies unusual patterns in operational process data that may indicate a problem"],
        ["Application", "Can flag emerging quality or process issues earlier than traditional statistical process control alone"],
    ])},
    "operations-management-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Distributionally robust optimization", "Optimizes against the worst case over a set of plausible probability distributions, rather than assuming one exactly known distribution"],
        ["Ambiguity application", "Well suited to operational settings where the true demand distribution is uncertain, not just its specific parameters"],
    ])},
    "operations-management-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Advanced simulation optimization", "Combines detailed simulation with formal search algorithms to design complex service networks"],
        ["Service network design application", "Enables optimizing network configuration decisions that are too complex to model with closed-form analytical methods"],
    ])},
    "operations-management-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Coordinating contract", "A supply chain contract structured so that each independent party's self-interested decisions collectively achieve system-optimal outcomes"],
        ["Decentralized multi-tier application", "Extends contract coordination theory beyond simple two-party relationships to more complex multi-tier supply chains"],
    ])},
    "operations-management-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic fleet management", "Continuously reassigns and repositions vehicles in response to real-time demand and location information"],
        ["Repositioning strategy", "Proactively moves idle vehicles toward anticipated future demand to reduce response times"],
    ])},
    "operations-management-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Capacity sharing", "Multiple companies jointly use shared logistics or production capacity rather than each maintaining separate dedicated capacity"],
        ["Collaborative logistics network", "Can reduce costs and improve utilization by pooling demand across multiple companies' otherwise separate networks"],
    ])},
    "operations-management-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Servitization", "A business strategy shift from selling a physical product to selling the outcomes or use of that product as a service"],
        ["Product-as-a-service operations strategy", "Requires fundamentally rethinking operations around ongoing service delivery rather than a one-time product sale"],
    ])},
    "operations-management-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Analytics-driven root cause analysis", "Uses data analysis techniques to systematically identify the underlying cause of quality failures"],
        ["Application", "Moves beyond manual investigation to leverage patterns across large volumes of quality data"],
    ])},
    "operations-management-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Design of experiments", "A structured statistical methodology for efficiently testing how multiple factors affect a process outcome"],
        ["Complex process optimization application", "Identifies which factors and factor interactions most significantly affect process performance, guiding optimization"],
    ])},
    "operations-management-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Dynamic discounting", "A buyer offers early payment in exchange for a discount, with terms flexibly negotiated rather than fixed"],
        ["Reverse factoring", "A financing arrangement where a third-party financier pays suppliers early on behalf of the buyer, improving supplier cash flow"],
    ])},
    "operations-management-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Operational resilience metric", "Quantitative measures assessing how well an operational system can withstand and recover from disruption"],
        ["Stress testing framework", "Systematically evaluates operational performance under simulated severe but plausible disruption scenarios"],
    ])},
    "operations-management-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Approximate dynamic programming", "Uses approximation techniques to make sequential decision problems tractable when exact dynamic programming is computationally infeasible"],
        ["Sequential operational decision application", "Enables solving realistically sized multi-period operational decision problems that exact methods cannot handle"],
    ])},
    "operations-management-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Mechanism design (internal markets)", "Designs the rules of an internal resource allocation process so that self-interested business units reveal their true resource needs"],
        ["Internal resource allocation market", "Uses market-like mechanisms within an organization to allocate scarce shared resources efficiently"],
    ])},
    "operations-management-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Data envelopment analysis", "A nonparametric method that measures the relative efficiency of comparable operating units"],
        ["Operational efficiency benchmarking", "Identifies which operating units are on the efficient frontier and which have room for operational improvement"],
    ])},
    "operations-management-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Master's thesis research seminar", "A forum for presenting and defending original operations and supply chain management research to faculty and peers"],
        ["Operations research", "Emphasizes a clearly stated research question, rigorous quantitative methodology, and meaningful practical or theoretical contribution"],
    ])},
    "operations-management-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Cold chain logistics", "Manages temperature-controlled transportation and storage throughout a supply chain"],
        ["Pharmaceutical distribution application", "Critical for pharmaceuticals like vaccines that lose efficacy if exposed to temperatures outside a strict required range"],
    ])},
    "operations-management-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Humanitarian relief supply chain", "Coordinates the delivery of emergency aid and supplies during disaster response"],
        ["Demand surge coordination", "Must rapidly scale operations to meet a sudden, extreme spike in demand under highly constrained and uncertain conditions"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Operations Management"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"operations-management-m2-l{base_n}"
        worked_key = f"operations-management-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Operations Management lessons.")


if __name__ == "__main__":
    main()
