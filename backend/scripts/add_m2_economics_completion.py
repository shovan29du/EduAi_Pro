#!/usr/bin/env python3
"""Depth pass, M2 Economics: fill in real, hand-checked data_table
content for the M2 Economics lessons not covered by the earlier
breadth-first batch. Brings M2 Economics to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning modern
quantitative economics (DSGE, ML for economists, field experiments),
canonical economist/theory profiles (Coase, Ostrom, Sen, Arrow,
Solow, Piketty, Duflo), law and economics, extensive economic history
(financial crises, monetary history, hyperinflation episodes), urban
and economic geography, agricultural and development economics, labor
and public economics, health and environmental economics, and
international/trade economics; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping). l3
was already completed by an earlier breadth-first batch, so its
data_table is hard-coded here for reuse (it falls within l1-l20, so it
is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_economics_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["DSGE model", "Dynamic Stochastic General Equilibrium models explain aggregate economic fluctuations from optimizing agents' behavior over time"],
    ["Quantitative macroeconomics", "Calibrates and estimates DSGE models against real macroeconomic data to analyze policy and business cycle questions"],
])

CHARTS: dict[str, dict] = {
    "economics-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Game theory", "Studies strategic interaction where each agent's optimal choice depends on the choices of others"],
        ["Economic application", "Used to model competition, bargaining, and coordination problems across nearly every field of economics"],
    ])},
    "economics-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Economics capstone", "An applied culminating project demonstrating original economic research and methodology skill"],
        ["Research methods", "Requires a clearly stated research question, appropriate identification strategy, and rigorous empirical analysis"],
    ])},
    "economics-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Heterogeneous-agent macroeconomics", "Models economies where individual agents differ in wealth, income, and circumstances, rather than assuming one representative agent"],
        ["Application", "Captures how aggregate outcomes like inequality and monetary policy transmission depend on the underlying distribution of agents"],
    ])},
    "economics-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Empirical industrial organization", "Uses structural and reduced-form econometric methods to study firm behavior and market competition"],
        ["Application", "Estimates demand and cost parameters to analyze mergers, pricing, and market power empirically"],
    ])},
    "economics-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Field experiment", "A randomized experiment conducted in a real-world setting rather than a controlled laboratory"],
        ["RCT design", "Random assignment to treatment and control groups enables credible causal inference about a policy's effect"],
    ])},
    "economics-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Networks in economics", "Studies how economic outcomes are shaped by the structure of relationships connecting agents"],
        ["Application", "Explains phenomena like information diffusion, risk-sharing, and market contagion that depend on network structure"],
    ])},
    "economics-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Machine learning for economists", "Applies ML techniques to prediction and causal inference problems in economic research"],
        ["Application", "Used for tasks like flexible demand estimation and identifying heterogeneous treatment effects in policy evaluation"],
    ])},
    "economics-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Climate economics", "Studies the economic causes and consequences of climate change and policy responses to it"],
        ["Integrated assessment model", "Combines climate science and economic models to estimate the social cost of carbon and evaluate policy options"],
    ])},
    "economics-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral finance", "Studies how psychological biases cause financial markets and investor behavior to deviate from pure rational-agent predictions"],
        ["Application", "Explains anomalies like momentum and excess volatility that traditional efficient market models struggle to account for"],
    ])},
    "economics-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Coase theorem", "When transaction costs are zero, parties will bargain to an efficient outcome regardless of initial legal entitlement"],
        ["Transaction cost economics", "Explains why real-world institutions and contracts matter once the zero-transaction-cost assumption is relaxed"],
    ])},
    "economics-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Elinor Ostrom", "Nobel laureate who demonstrated that communities can sustainably self-govern shared resources without privatization or state control"],
        ["Governing the Commons", "Her research documented design principles that allow local institutions to successfully manage common-pool resources"],
    ])},
    "economics-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Thomas Schelling", "Nobel laureate whose segregation model showed extreme neighborhood segregation can emerge from mild individual preferences"],
        ["Residential segregation model", "Demonstrates how aggregate patterns can differ dramatically from what individual preferences alone would suggest"],
    ])},
    "economics-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Amartya Sen", "Nobel laureate who developed the capability approach, measuring wellbeing by real freedoms people have, not just income"],
        ["Capability approach", "Shifted welfare economics focus from resources alone toward what people are actually able to do and be"],
    ])},
    "economics-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Liquidity trap", "A situation where interest rates are near zero and monetary policy loses effectiveness at stimulating demand"],
        ["Keynes's General Theory", "Introduced the liquidity trap concept as part of his broader theory of aggregate demand-driven economic fluctuations"],
    ])},
    "economics-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Gary Becker", "Nobel laureate who applied economic analysis to non-market behavior, including family and household decisions"],
        ["Economics of the family", "Modeled marriage, fertility, and household division of labor using rational choice and specialization frameworks"],
    ])},
    "economics-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Richard Thaler", "Nobel laureate credited with institutionalizing behavioral economics as a mainstream field within economics"],
        ["Institutionalization", "Bridged psychological insights about decision-making with formal economic modeling and policy application"],
    ])},
    "economics-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Prospect theory", "Kahneman and Tversky's model describing how people evaluate gains and losses asymmetrically relative to a reference point"],
        ["Economic modeling application", "Incorporated into economic models to explain behaviors like loss aversion that expected utility theory cannot"],
    ])},
    "economics-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Kenneth Arrow", "Nobel laureate who, with Gerard Debreu, proved the existence of a general equilibrium under specified conditions"],
        ["General equilibrium existence proof", "A foundational mathematical result establishing markets can, in principle, simultaneously clear across an entire economy"],
    ])},
    "economics-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Robert Solow", "Nobel laureate whose growth model attributed long-run economic growth primarily to technological progress"],
        ["Growth accounting", "A method decomposing observed output growth into contributions from capital, labor, and total factor productivity"],
    ])},
    "economics-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Paul Romer", "Nobel laureate who developed endogenous growth theory, explaining technological progress as an economic outcome rather than external assumption"],
        ["Endogenous growth theory", "Models how deliberate investment in research and ideas can sustain long-run growth, unlike Solow's exogenous technology assumption"],
    ])},
    "economics-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Robert Lucas", "Nobel laureate whose rational expectations critique reshaped how macroeconomic policy effects are modeled"],
        ["Rational expectations revolution", "Argued that agents' forward-looking expectations must be modeled consistently, undermining some traditional Keynesian policy predictions"],
    ])},
    "economics-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Efficient market hypothesis", "Eugene Fama's theory that asset prices fully reflect all available information"],
        ["Debate", "Contested by behavioral economists who document persistent anomalies like bubbles that seem inconsistent with full efficiency"],
    ])},
    "economics-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Robert Shiller", "Nobel laureate known for documenting excess volatility in asset markets relative to what efficient markets theory predicts"],
        ["Irrational Exuberance", "His influential analysis of asset bubbles, warning of overvaluation in both the dot-com and housing markets"],
    ])},
    "economics-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Thomas Piketty", "Economist known for extensive historical data analysis of wealth and income inequality across countries"],
        ["Capital in the Twenty-First Century", "Argued that when the return on capital exceeds economic growth, wealth inequality tends to rise over time"],
    ])},
    "economics-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Angus Deaton", "Nobel laureate known for rigorous empirical analysis of consumption, poverty, and welfare measurement"],
        ["Global poverty analysis", "His work refined how household survey data is used to accurately measure poverty and wellbeing across countries"],
    ])},
    "economics-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Esther Duflo", "Nobel laureate who pioneered randomized evaluation methods for assessing anti-poverty program effectiveness"],
        ["Randomized evaluation", "Applies the rigor of medical-trial-style randomized experiments to test which development interventions actually work"],
    ])},
    "economics-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Abhijit Banerjee", "Nobel laureate and co-author of Poor Economics, advocating rigorous, evidence-based approaches to fighting poverty"],
        ["Poor Economics framework", "Argues effective poverty reduction requires understanding specific decision-making contexts poor households actually face"],
    ])},
    "economics-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Oliver Williamson", "Nobel laureate known for analyzing how firms choose governance structures based on transaction characteristics"],
        ["Asset specificity", "Explains why firms vertically integrate when transactions require highly specialized, relationship-specific investments"],
    ])},
    "economics-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Richard Posner", "A leading figure in law and economics who evaluated legal rules by their efficiency in maximizing social wealth"],
        ["Wealth maximization framework", "Argues legal rules should be designed to allocate resources to their highest-valued economic use"],
    ])},
    "economics-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Tragedy of the commons", "Individually rational use of a shared resource can lead to its collective overexploitation and depletion"],
        ["Property rights (law and economics)", "Clearly defined property rights are one classic solution proposed to align individual incentives with resource sustainability"],
    ])},
    "economics-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Default rule", "A contract term that applies automatically unless parties explicitly agree to something different"],
        ["Contract law efficiency", "Well-designed default rules reduce the transaction costs of contracting by matching what most parties would have chosen anyway"],
    ])},
    "economics-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Tort liability rule", "The legal standard determining when a party must compensate another for harm caused"],
        ["Economic analysis", "Analyzes how different liability standards (negligence vs. strict liability) affect parties' incentives to take precautions"],
    ])},
    "economics-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Chicago School antitrust", "An approach emphasizing consumer welfare and economic efficiency as the primary standard for antitrust enforcement"],
        ["Perspective", "Generally more skeptical than earlier approaches of aggressive intervention against large firm size alone"],
    ])},
    "economics-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["South Sea Bubble", "A 1720 British stock market speculative bubble and crash centered on the South Sea Company"],
        ["Economic history significance", "An early and well-documented case study of speculative mania and its economic consequences"],
    ])},
    "economics-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Tulip mania", "A period of extreme speculative price increases in tulip bulb contracts in the Dutch Republic in the 1630s"],
        ["Early modern speculation", "Often cited as one of history's first recorded speculative asset bubbles"],
    ])},
    "economics-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Bretton Woods system", "The post-WWII international monetary system pegging currencies to the US dollar, itself convertible to gold"],
        ["Collapse", "Ended in 1971 when the US suspended dollar-gold convertibility, ushering in the era of floating exchange rates"],
    ])},
    "economics-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Gold standard", "A monetary system where a currency's value is directly linked to a fixed quantity of gold"],
        ["Interwar deflation", "Adherence to the gold standard is widely blamed for constraining monetary policy and worsening the deflationary spiral of the Great Depression"],
    ])},
    "economics-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Marshall Plan", "US-funded program providing large-scale financial assistance to rebuild Western European economies after WWII"],
        ["European reconstruction", "Widely credited with accelerating post-war European economic recovery and fostering economic integration"],
    ])},
    "economics-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Great Depression policy response", "The mix of fiscal, monetary, and regulatory measures governments used to address the 1930s economic collapse"],
        ["Analysis", "Debated extensively for lessons on the effectiveness and timing of different policy interventions during severe downturns"],
    ])},
    "economics-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Stagflation", "The simultaneous occurrence of high inflation and high unemployment, seen prominently in the 1970s"],
        ["Episode significance", "Challenged the previously assumed stable tradeoff between inflation and unemployment (the Phillips curve)"],
    ])},
    "economics-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Latin American debt crisis", "A severe sovereign debt crisis affecting multiple Latin American countries beginning in 1982"],
        ["Origins", "Triggered by a combination of high external borrowing, rising global interest rates, and falling commodity export revenues"],
    ])},
    "economics-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Asian financial crisis", "A 1997 currency and financial crisis that spread across several East and Southeast Asian economies"],
        ["Causes", "Involved sudden capital flight, currency devaluations, and exposed vulnerabilities in short-term foreign-currency borrowing"],
    ])},
    "economics-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["2008 global financial crisis", "A severe worldwide financial crisis triggered by the collapse of the US subprime mortgage market"],
        ["Origins", "Rooted in excessive leverage, complex securitized mortgage products, and inadequate financial regulation"],
    ])},
    "economics-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Eurozone sovereign debt crisis", "A crisis beginning around 2009 in which several eurozone countries faced unsustainable government debt levels"],
        ["Analysis", "Exposed structural challenges of a shared currency without unified fiscal policy across member states"],
    ])},
    "economics-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Japan's lost decades", "An extended period of economic stagnation and deflation in Japan following its early 1990s asset bubble collapse"],
        ["Policy lessons", "Widely studied for lessons on the persistence of deflationary stagnation and the limits of monetary policy near the zero lower bound"],
    ])},
    "economics-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Weimar Republic hyperinflation", "An extreme hyperinflation episode in Germany in the early 1920s"],
        ["Causes", "Driven by excessive money creation to finance war reparations and government deficits, destroying the currency's value"],
    ])},
    "economics-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Dutch East India Company", "One of the earliest joint-stock companies, often cited as a foundational example of modern corporate capitalism"],
        ["Early corporate capitalism", "Pioneered practices like tradable shares and limited liability that shaped the development of modern financial markets"],
    ])},
    "economics-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Industrial Revolution productivity", "The period of dramatic technological change and sustained productivity growth beginning in 18th-century Britain"],
        ["Economic transformation", "Marked the historical transition from stagnant pre-industrial growth to sustained modern economic growth"],
    ])},
    "economics-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Bengal famine", "A devastating famine in British-ruled Bengal in 1943 with significant loss of life"],
        ["Colonial economic policy", "Analyzed by economists like Amartya Sen as a failure of entitlements and distribution rather than solely food supply"],
    ])},
    "economics-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Marshallian supply-demand cross", "Alfred Marshall's foundational diagram depicting market equilibrium at the intersection of supply and demand curves"],
        ["Origins", "Became the standard visual and analytical framework underlying most introductory and advanced price theory"],
    ])},
    "economics-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Monocentric city model", "Models a city as organized around a single central business district, with land use determined by commuting cost trade-offs"],
        ["Urban economics application", "Explains classic patterns like declining population density and land rent with distance from the city center"],
    ])},
    "economics-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Agglomeration economies", "Productivity and cost benefits firms gain from locating near other firms and a concentrated labor market"],
        ["Firm location", "Explains why certain industries cluster geographically despite higher land and labor costs in dense urban areas"],
    ])},
    "economics-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Housing market filtering", "As housing ages, it tends to filter down to lower-income occupants over time"],
        ["Segmentation", "Explains how the existing housing stock naturally sorts across different income segments of the population"],
    ])},
    "economics-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Land rent gradient", "Land rents decline predictably with distance from a city's central business district"],
        ["Commuting cost trade-off", "Households and firms trade off higher land rent near the center against lower commuting costs"],
    ])},
    "economics-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["New Economic Geography", "Paul Krugman's framework explaining regional specialization through the interaction of increasing returns and transport costs"],
        ["Application", "Explains why economic activity clusters unevenly across regions rather than dispersing uniformly"],
    ])},
    "economics-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Core-periphery model", "Models how economic activity concentrates in a developed \"core\" region while other regions remain a less-developed \"periphery\""],
        ["Regional development application", "Explains persistent regional inequality as a self-reinforcing outcome of agglomeration forces"],
    ])},
    "economics-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Cluster theory", "Michael Porter's framework explaining how geographically concentrated industries gain competitive advantage"],
        ["Regional competitiveness", "Shared infrastructure, specialized labor, and knowledge spillovers within a cluster boost the competitiveness of member firms"],
    ])},
    "economics-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Land tenure system", "The set of rules governing rights to own, use, and transfer agricultural land"],
        ["Productivity effect", "Secure and well-defined land tenure is generally associated with greater agricultural investment and productivity"],
    ])},
    "economics-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Sharecropping contract", "A tenancy arrangement where a farmer pays a share of the crop rather than fixed rent to a landowner"],
        ["Economics of sharecropping", "Studied as a classic example of a contract balancing risk-sharing against reduced tenant work incentives"],
    ])},
    "economics-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Commodity price volatility", "Large, unpredictable fluctuations in agricultural commodity prices"],
        ["Futures market", "Allows farmers and buyers to hedge against price volatility by locking in prices for future delivery"],
    ])},
    "economics-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Green Revolution", "A mid-20th-century transformation of agriculture through high-yield crop varieties and modern farming techniques"],
        ["Economic impact", "Dramatically increased agricultural productivity in many developing countries, though with debated distributional effects"],
    ])},
    "economics-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Lewis model", "Models economic development as labor moving from a low-productivity traditional sector to a modern industrial sector"],
        ["Dual economy", "Describes developing economies characterized by a coexisting traditional agricultural sector and a modern industrial sector"],
    ])},
    "economics-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Solow-Swan model", "A growth model attributing long-run growth to capital accumulation, labor, and exogenous technological progress"],
        ["Poor country application", "Predicts poorer countries should grow faster than richer ones as they converge toward similar steady-state income levels"],
    ])},
    "economics-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Microfinance", "Provides small loans and financial services to individuals typically excluded from traditional banking"],
        ["Grameen Bank model", "A pioneering microfinance institution using group lending to extend credit to poor borrowers without traditional collateral"],
    ])},
    "economics-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Structural adjustment program", "Loan conditions imposed by international financial institutions requiring policy reforms like austerity and liberalization"],
        ["Africa application", "Widely debated for their mixed record of promoting macroeconomic stability against significant short-term social costs"],
    ])},
    "economics-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Rosen-Roback model", "Models how wages and housing prices jointly adjust to compensate workers for differences in local amenities and productivity"],
        ["Compensating differential", "Explains why otherwise identical workers earn different wages in different locations due to local cost-of-living and amenity differences"],
    ])},
    "economics-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Card-Krueger natural experiment", "A famous study using a minimum wage increase in New Jersey to empirically test its employment effects"],
        ["Minimum wage finding", "Found no significant negative employment effect, challenging simple textbook competitive-labor-market predictions"],
    ])},
    "economics-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Monopsony power", "A single or dominant employer's ability to set wages below the competitive level due to limited worker outside options"],
        ["Local labor market application", "Recent research finds significant monopsony power in many local labor markets, affecting minimum wage policy analysis"],
    ])},
    "economics-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Ramsey rule", "Optimal commodity taxes should be set inversely proportional to the price elasticity of demand for each good"],
        ["Optimal taxation", "Minimizes the total efficiency loss (deadweight loss) from taxation for a given amount of revenue raised"],
    ])},
    "economics-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Tiebout model", "Models households \"voting with their feet\" by choosing to live in the local jurisdiction whose public goods and taxes they prefer"],
        ["Local public goods", "Suggests competition among local governments can lead to efficient provision of local public goods"],
    ])},
    "economics-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Mirrlees optimal income tax", "Derives the income tax schedule that maximizes social welfare given that individual productivity is not directly observable"],
        ["Theory", "Balances redistribution against the efficiency cost of taxation discouraging high-productivity individuals' work effort"],
    ])},
    "economics-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Grossman model", "Models health as a form of capital that individuals invest in and that depreciates over time"],
        ["Health capital", "Frames healthcare spending as an investment in the stock of health capital rather than pure consumption"],
    ])},
    "economics-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Adverse selection", "Occurs when one party in a transaction has more information, leading to a skewed pool of participants"],
        ["Insurance market application", "In health insurance, higher-risk individuals are more likely to seek coverage, potentially destabilizing the insurance pool"],
    ])},
    "economics-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Coase approach to externalities", "Argues that with clearly defined property rights and low transaction costs, parties can bargain to resolve externalities efficiently"],
        ["Environmental application", "Contrasts with Pigouvian taxation as an alternative approach to correcting externalities like pollution"],
    ])},
    "economics-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Pigouvian tax", "A tax set equal to the external cost of an activity, aligning private incentives with social cost"],
        ["Practice", "Applied to activities like carbon emissions to internalize their environmental cost into market prices"],
    ])},
    "economics-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Cap-and-trade", "A market-based system setting a total emissions cap and allowing firms to trade emission allowances"],
        ["US Acid Rain Program", "A landmark cap-and-trade program that successfully reduced sulfur dioxide emissions at lower cost than command-and-control regulation"],
    ])},
    "economics-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Federal Reserve founding", "The US central bank was established in 1913 in response to recurring banking panics"],
        ["Monetary history significance", "Created a lender of last resort and centralized monetary authority that reshaped US financial stability"],
    ])},
    "economics-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Paul Volcker's disinflation", "The Federal Reserve's aggressive interest rate increases in the early 1980s to break persistent high inflation"],
        ["Outcome", "Successfully reduced inflation but caused a sharp recession, illustrating the real economic cost of disinflation"],
    ])},
    "economics-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Friedman and Schwartz", "Authors of the influential Monetary History of the United States, emphasizing money supply's central role in economic fluctuations"],
        ["Monetary history thesis", "Argued Federal Reserve policy mistakes significantly worsened the severity of the Great Depression"],
    ])},
    "economics-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Plaza Accord", "A 1985 agreement among major economies to jointly depreciate the US dollar against other currencies"],
        ["Currency realignment", "Illustrates coordinated international monetary policy intervention to address large trade imbalances"],
    ])},
    "economics-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Mundell-Fleming model", "Models how fiscal and monetary policy effectiveness depends on a country's exchange rate regime and capital mobility"],
        ["Open economy application", "Shows monetary policy is more effective under floating exchange rates, fiscal policy under fixed rates, with free capital flow"],
    ])},
    "economics-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Optimum currency area theory", "Analyzes the conditions under which countries benefit from sharing a common currency"],
        ["Theory", "Key criteria include labor mobility and fiscal transfer mechanisms to absorb asymmetric economic shocks between member regions"],
    ])},
    "economics-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Heckscher-Ohlin model", "Predicts a country will export goods that intensively use its relatively abundant factor of production"],
        ["Factor endowments", "Explains trade patterns based on differences in countries' relative endowments of capital and labor"],
    ])},
    "economics-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Stolper-Samuelson theorem", "Shows that trade opening raises the real return to a country's abundant factor and lowers the return to its scarce factor"],
        ["Application", "Explains why trade can create both winners and losers within a country, not just between countries"],
    ])},
    "economics-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["NAFTA", "A trade agreement liberalizing trade among the United States, Canada, and Mexico beginning in 1994"],
        ["Regional economic impact", "Empirical studies find mixed effects, boosting overall trade while causing concentrated job losses in some US manufacturing sectors"],
    ])},
    "economics-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Deng Xiaoping's reforms", "Market-oriented economic reforms beginning in the late 1970s that transformed China's centrally planned economy"],
        ["Economic transformation", "Introduced market incentives and opened China to foreign investment, driving decades of rapid economic growth"],
    ])},
    "economics-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Chilean economic reforms", "Free-market economic reforms implemented in Chile under the Pinochet regime beginning in the 1970s"],
        ["Analysis", "A widely debated case study examining the economic outcomes and social costs of rapid market liberalization under an authoritarian government"],
    ])},
    "economics-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Douglass North", "Nobel laureate known for analyzing how institutions shape long-run economic performance"],
        ["Path dependence theory", "Argues historical institutional choices constrain and shape a society's subsequent range of possible economic development paths"],
    ])},
    "economics-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Enclosure movement", "The historical process of converting communally used land in Britain into privately owned, fenced parcels"],
        ["Economic history significance", "Debated for its role in both agricultural productivity gains and displacement of rural communities"],
    ])},
    "economics-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["James Buchanan", "Nobel laureate who founded public choice theory, applying economic analysis to political decision-making"],
        ["Constitutional economics", "Studies how the rules governing political and economic institutions themselves should be designed"],
    ])},
    "economics-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Economic model of crime", "Gary Becker's framework treating criminal behavior as a rational response to the expected costs and benefits of committing a crime"],
        ["Policy implication", "Implies that both the probability and severity of punishment influence deterrence, informing criminal justice policy design"],
    ])},
    "economics-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Panic of 1907", "A severe US financial crisis triggered by a failed stock speculation and resulting bank runs"],
        ["Path to central banking", "Directly motivated the creation of the Federal Reserve as a lender of last resort to prevent future panics"],
    ])},
    "economics-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Rust Belt deindustrialization", "The decline of manufacturing employment across the historically industrial US Midwest and Northeast"],
        ["Economic geography analysis", "Attributed to a combination of automation, globalization, and shifting comparative advantage in manufacturing"],
    ])},
    "economics-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Rent control", "Government-imposed limits on how much landlords can charge or increase rent"],
        ["Economic analysis", "Economists broadly find rent control tends to reduce housing supply and quality over the long run despite short-term tenant benefits"],
    ])},
    "economics-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Common Agricultural Policy", "The European Union's system of agricultural subsidies and market interventions"],
        ["Subsidy economics", "Analyzed for its effects on farm incomes, food prices, and trade distortions affecting non-EU agricultural producers"],
    ])},
    "economics-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Louisiana Purchase", "The 1803 US acquisition of a vast territory from France for approximately $15 million"],
        ["Economic transaction analysis", "Analyzed as a landmark example of the economic value and long-run returns of a major territorial land acquisition"],
    ])},
    "economics-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Intellectual property rights economics", "Analyzes the tradeoff between incentivizing innovation through temporary monopoly rights and the efficiency cost of restricted access"],
        ["Application", "Informs policy debates over optimal patent length and scope to balance innovation incentives against consumer welfare"],
    ])},
    "economics-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Vickrey-Clarke-Groves auction", "A mechanism design framework where truthful bidding is each participant's dominant strategy"],
        ["Mechanism design", "Studies how to design rules of an interaction (like an auction) so that self-interested participants are incentivized to reveal true information"],
    ])},
    "economics-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Diamond-Mortensen-Pissarides model", "A Nobel Prize-winning model explaining unemployment as resulting from frictions in matching workers to jobs"],
        ["Search and matching theory", "Analyzes labor markets where finding a suitable job or employee takes time and effort rather than clearing instantaneously"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Economics"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"economics-m2-l{base_n}"
        worked_key = f"economics-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Economics lessons.")


if __name__ == "__main__":
    main()
