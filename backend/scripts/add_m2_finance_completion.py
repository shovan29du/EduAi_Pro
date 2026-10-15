#!/usr/bin/env python3
"""Depth pass, M2 Finance: fill in real, hand-checked data_table
content for the M2 Finance lessons not covered by the earlier
breadth-first batch. Brings M2 Finance to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level topics spanning corporate
finance theory (Modigliani-Miller, agency costs, real options), asset
pricing (CAPM, Fama-French factors, behavioral finance), market
microstructure and derivatives pricing, fixed income and credit risk
modeling, bank risk management (VaR, Basel III), M&A and private
equity, corporate governance, sustainable/Islamic/fintech finance,
personal and retirement finance, and systemic risk; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3 was already completed by an earlier breadth-first
batch, so its data_table is hard-coded here for reuse (it falls within
l1-l20, so it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_finance_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Modigliani-Miller theorem", "In a frictionless market, a firm's value is unaffected by how it is financed (debt versus equity)"],
    ["Capital structure irrelevance", "Establishes the baseline case against which real-world capital structure decisions (taxes, bankruptcy costs) are analyzed"],
])

CHARTS: dict[str, dict] = {
    "finance-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Financial risk management", "Identifies, measures, and mitigates exposure to market, credit, liquidity, and operational risks"],
        ["Application", "Underlies decisions ranging from hedging strategy to setting bank capital requirements"],
    ])},
    "finance-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Finance capstone", "An applied culminating project demonstrating end-to-end financial analysis and valuation skill"],
        ["Deliverable", "Typically includes a valuation model, risk analysis, and evaluation of a real or simulated financial decision"],
    ])},
    "finance-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Agency cost", "The cost arising from conflicts of interest between a firm's managers and its shareholders"],
        ["Free cash flow", "Managers with excess free cash flow may overinvest in value-destroying projects rather than returning cash to shareholders"],
    ])},
    "finance-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Signaling theory (dividends)", "A dividend change can convey management's private information about the firm's future prospects to the market"],
        ["Corporate dividend policy", "Explains why dividend increases and cuts often trigger significant stock price reactions"],
    ])},
    "finance-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Dividend irrelevance", "Under Modigliani-Miller assumptions, dividend policy does not affect firm value"],
        ["Clientele effect", "Investors with different tax situations or income needs self-select into stocks with matching dividend policies"],
    ])},
    "finance-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Real options valuation", "Values managerial flexibility (e.g. the option to expand or abandon a project) using option-pricing techniques"],
        ["Capital budgeting application", "Captures strategic flexibility value that standard discounted cash flow analysis often ignores"],
    ])},
    "finance-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Adjusted present value", "Values a project by separately valuing its unlevered cash flows and the value added by financing side effects"],
        ["Leveraged transaction application", "Especially useful for highly leveraged deals where financing effects significantly affect overall value"],
    ])},
    "finance-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Weighted average cost of capital", "A firm's blended required return across its debt and equity financing sources, weighted by their proportions"],
        ["Circularity problem", "Since WACC weights depend on market value, which itself depends on WACC through discounting, the calculation can require iteration"],
    ])},
    "finance-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Capital Asset Pricing Model", "Predicts an asset's expected return based on its systematic risk (beta) relative to the overall market"],
        ["Empirical anomaly", "Real-world returns show patterns (like the size and value effects) that CAPM's single beta factor fails to fully explain"],
    ])},
    "finance-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Fama-French three-factor model", "Extends CAPM by adding size and value factors alongside market risk to explain stock returns"],
        ["Improvement over CAPM", "Explains a substantially larger share of the cross-sectional variation in average stock returns than CAPM alone"],
    ])},
    "finance-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Fama-French five-factor model", "Further extends the three-factor model by adding profitability and investment factors"],
        ["Refinement", "Captures additional return patterns related to firm profitability and asset growth not explained by the earlier three factors"],
    ])},
    "finance-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Arbitrage pricing theory", "Explains asset returns as a linear function of multiple systematic risk factors, without specifying exactly which factors"],
        ["Flexibility", "Offers a more general multi-factor framework than CAPM, letting the relevant factors be determined empirically"],
    ])},
    "finance-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Consumption-based asset pricing", "Prices assets based on how their returns co-move with investors' consumption, since consumption smoothing drives risk aversion"],
        ["Model", "Theoretically elegant but empirically struggles to match observed asset return patterns without additional assumptions"],
    ])},
    "finance-m2-l15": {"data_table": table(["Term", "Meaning"], [
        ["Equity premium puzzle", "Historical stock returns exceed bond returns by more than standard risk aversion models can explain"],
        ["Significance", "A major unresolved puzzle in asset pricing that has motivated much subsequent theoretical and behavioral research"],
    ])},
    "finance-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Prospect theory", "Describes how investors evaluate gains and losses asymmetrically relative to a reference point"],
        ["Market application", "Explains behaviors like the disposition effect and excessive risk-taking to avoid realizing losses"],
    ])},
    "finance-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["Overconfidence", "Investors' tendency to overestimate the precision of their own information or judgment"],
        ["Trading volume application", "Overconfident investors trade more frequently than rational models predict, generating excess trading volume"],
    ])},
    "finance-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Disposition effect", "Investors' tendency to sell winning investments too early and hold losing investments too long"],
        ["Investor behavior", "Runs counter to optimal tax-loss harvesting behavior and is well documented across many investor populations"],
    ])},
    "finance-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Limits to arbitrage", "Real-world constraints (capital, risk) prevent rational arbitrageurs from fully correcting mispricing"],
        ["Noise trader risk", "Arbitrageurs face the risk that irrational traders push prices further from fundamental value before eventually correcting"],
    ])},
    "finance-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Bid-ask spread", "The difference between the highest price a buyer will pay and the lowest price a seller will accept"],
        ["Decomposition", "Can be decomposed into components reflecting order processing cost, inventory risk, and adverse selection risk"],
    ])},
    "finance-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["High-frequency trading", "Uses very fast, algorithmically driven strategies to trade on extremely short time horizons"],
        ["Price discovery", "HFT is credited with tightening spreads and speeding price discovery, while also raising concerns about market stability"],
    ])},
    "finance-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Dark pool", "A private trading venue where orders are not publicly displayed before execution"],
        ["Market fragmentation", "Growth of dark pools has fragmented trading volume across many venues, raising questions about overall price discovery quality"],
    ])},
    "finance-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Black-Scholes-Merton model", "A foundational formula for pricing European options based on a set of simplifying assumptions"],
        ["Model assumptions", "Assumes constant volatility and interest rates, log-normal price movement, and no dividends or transaction costs"],
    ])},
    "finance-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic volatility model", "Allows an asset's volatility itself to follow a random process, unlike Black-Scholes' constant volatility assumption"],
        ["Heston model", "A widely used stochastic volatility model that better captures the observed volatility smile in real option markets"],
    ])},
    "finance-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Jump-diffusion model", "Models asset prices as following continuous diffusion punctuated by sudden discrete jumps"],
        ["Application", "Better captures observed extreme price movements than pure continuous diffusion models like Black-Scholes"],
    ])},
    "finance-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Implied volatility surface", "The pattern of implied volatilities across different strike prices and maturities for a given underlying asset"],
        ["Smile dynamics", "The characteristic non-flat shape (smile or skew) across strikes reveals that market prices deviate from simple Black-Scholes assumptions"],
    ])},
    "finance-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Barrier option", "An exotic option whose payoff depends on whether the underlying asset crosses a specified price barrier"],
        ["Asian option", "An exotic option whose payoff depends on the average price of the underlying over a period, reducing manipulation risk"],
    ])},
    "finance-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Credit default swap", "A derivative contract providing insurance-like protection against a borrower's default"],
        ["Counterparty risk", "The risk that the party providing CDS protection itself fails to fulfill its obligation when a default occurs"],
    ])},
    "finance-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Collateralized debt obligation", "A structured product pooling debt instruments and slicing the cash flows into tranches with different risk levels"],
        ["Tranching mechanics", "Senior tranches absorb losses last and are paid first, while junior tranches bear losses first in exchange for higher yield"],
    ])},
    "finance-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Vasicek model", "A mean-reverting short-rate model for interest rates, allowing for negative rates in its basic form"],
        ["Cox-Ingersoll-Ross model", "A mean-reverting short-rate model with a volatility structure that ensures interest rates remain non-negative"],
    ])},
    "finance-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Heath-Jarrow-Morton framework", "Models the evolution of the entire forward interest rate curve rather than just a single short rate"],
        ["Interest rate application", "Provides a general, arbitrage-free framework nesting many specific short-rate models as special cases"],
    ])},
    "finance-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Duration", "Measures a bond portfolio's sensitivity to small changes in interest rates"],
        ["Convexity", "Captures the curvature in the price-yield relationship that duration alone, a linear approximation, misses for larger rate changes"],
    ])},
    "finance-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Merton's structural model", "Models a firm's equity as a call option on its assets, with default occurring when asset value falls below debt obligations"],
        ["Credit risk application", "Provides a theoretically grounded link between a firm's capital structure and its probability of default"],
    ])},
    "finance-m2-l34": {"data_table": table(["Term", "Meaning"], [
        ["Reduced-form credit risk model", "Models default as a statistically modeled random event with an estimated intensity, without explicitly modeling firm assets"],
        ["Contrast with structural models", "More flexible for fitting to observed market credit spreads, though less theoretically tied to firm fundamentals"],
    ])},
    "finance-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Value at Risk", "The maximum expected loss over a given time horizon at a specified confidence level"],
        ["Methodologies and limitations", "Historical simulation, variance-covariance, and Monte Carlo approaches all have known blind spots, especially in tail risk"],
    ])},
    "finance-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Expected shortfall", "The average loss in the worst-case scenarios beyond the VaR threshold, capturing tail risk VaR misses"],
        ["Coherent risk measure", "Satisfies mathematical properties (like subadditivity) that VaR itself can violate, making it a more theoretically sound risk metric"],
    ])},
    "finance-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Stress testing", "Evaluates how a bank's financial position would perform under an extreme but plausible adverse scenario"],
        ["Scenario analysis application", "Regulators require systematically important banks to demonstrate resilience across multiple defined stress scenarios"],
    ])},
    "finance-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Basel III", "An international regulatory framework strengthening bank capital, leverage, and liquidity requirements after the 2008 crisis"],
        ["Capital adequacy framework", "Sets minimum capital ratios banks must hold relative to their risk-weighted assets"],
    ])},
    "finance-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Liquidity risk", "The risk that a bank cannot meet its short-term obligations without incurring unacceptable losses"],
        ["Liquidity Coverage Ratio", "A Basel III requirement that banks hold enough high-quality liquid assets to survive a 30-day stress scenario"],
    ])},
    "finance-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Synergy valuation", "Estimates the additional value created by combining two companies beyond their standalone values"],
        ["M&A method", "Requires carefully justifying assumed cost savings or revenue enhancements, which are often overestimated in practice"],
    ])},
    "finance-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Leveraged buyout", "An acquisition financed primarily with borrowed money, using the target company's own assets and cash flows as collateral"],
        ["Debt capacity analysis", "Determines how much debt a target company's cash flows can realistically support without excessive default risk"],
    ])},
    "finance-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Private equity fund structure", "Typically organized as a limited partnership with general partners managing capital committed by limited partner investors"],
        ["Carried interest", "The general partner's performance-based share of fund profits, typically around 20% above a specified return hurdle"],
    ])},
    "finance-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Berkus method", "A venture valuation approach assigning value to a pre-revenue startup based on qualitative risk-reduction milestones achieved"],
        ["Scorecard method", "Values a startup by comparing it against typical valuations of similar companies, adjusted by weighted qualitative factors"],
    ])},
    "finance-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["IPO underpricing", "Newly issued shares are systematically priced below their subsequent first-day trading value"],
        ["Underpricing puzzle", "A well-documented anomaly with multiple competing theoretical explanations, none fully conclusive"],
    ])},
    "finance-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Seasoned equity offering", "The sale of additional shares by a company that is already publicly traded"],
        ["Announcement effect", "SEO announcements are typically associated with a negative stock price reaction, often attributed to information asymmetry"],
    ])},
    "finance-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["Corporate governance", "The system of rules and practices by which a company is directed and controlled"],
        ["Board independence", "Independent directors are argued to more effectively monitor management on behalf of shareholders than insider-dominated boards"],
    ])},
    "finance-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Executive compensation design", "Structures pay packages to align executive incentives with shareholder interests"],
        ["Pay-performance sensitivity", "Measures how closely executive compensation actually tracks firm performance, a key governance design metric"],
    ])},
    "finance-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Activist investing", "Investors acquire a stake in a company specifically to influence its strategy or management"],
        ["Shareholder value creation", "Empirical evidence on whether activist campaigns genuinely create long-term value is mixed and debated"],
    ])},
    "finance-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Poison pill", "A defensive tactic making a hostile takeover prohibitively expensive by diluting the acquirer's stake if triggered"],
        ["Anti-takeover defense", "Defended as protecting shareholder value from opportunistic bids, criticized as entrenching underperforming management"],
    ])},
    "finance-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Cross-border M&A", "Acquisitions spanning different countries, adding currency, regulatory, and cultural complexity"],
        ["Valuation challenge", "Must account for factors like differing accounting standards, tax regimes, and political risk not present in domestic deals"],
    ])},
    "finance-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Cash conversion cycle", "The time it takes a company to convert its investments in inventory into cash from sales"],
        ["Working capital optimization", "Shortening the cycle frees up cash without requiring additional external financing"],
    ])},
    "finance-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Trade credit", "Financing extended by a supplier allowing a buyer to pay for goods after delivery"],
        ["Supplier financing strategy", "Can serve as an important, flexible source of short-term working capital financing between businesses"],
    ])},
    "finance-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Corporate cash holding", "Cash and liquid assets a firm keeps on its balance sheet beyond immediate operating needs"],
        ["Precautionary motive theory", "Firms hold extra cash as a buffer against future uncertainty in cash flows and access to external financing"],
    ])},
    "finance-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Capital structure determinants (emerging markets)", "Factors shaping debt-equity choices differ in emerging markets due to underdeveloped capital markets and institutions"],
        ["Emerging market application", "Firms often face higher costs of debt and equity issuance and rely more heavily on retained earnings"],
    ])},
    "finance-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Sovereign debt restructuring", "The process by which a defaulting government renegotiates the terms of its outstanding debt with creditors"],
        ["Mechanism", "Lacks a formal international bankruptcy court, making restructurings often lengthy and contentious negotiations"],
    ])},
    "finance-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Currency risk hedging", "Techniques multinational firms use to manage exposure to exchange rate fluctuations"],
        ["Strategy", "Includes forward contracts, options, and natural hedges like matching foreign-currency revenues to costs"],
    ])},
    "finance-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Transfer pricing", "The price charged for transactions between related entities of a multinational company"],
        ["Multinational tax optimization", "Companies can strategically set transfer prices to shift profits toward lower-tax jurisdictions, subject to regulatory scrutiny"],
    ])},
    "finance-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Managerial overconfidence", "Executives systematically overestimate their own abilities and the likely success of their decisions"],
        ["Behavioral corporate finance", "Explains patterns like excessive M&A activity and overinvestment that rational-manager models struggle to account for"],
    ])},
    "finance-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["ESG integration", "Incorporates environmental, social, and governance factors directly into a company's valuation and investment analysis"],
        ["Corporate valuation application", "Reflects growing evidence and investor demand that ESG factors can materially affect long-term financial performance"],
    ])},
    "finance-m2-l60": {"data_table": table(["Term", "Meaning"], [
        ["Green bond", "A bond whose proceeds are specifically earmarked for environmentally beneficial projects"],
        ["Sustainable finance instrument", "Grew rapidly as investors sought fixed-income options that explicitly fund environmental objectives"],
    ])},
    "finance-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Sukuk", "An Islamic finance instrument structured to comply with Sharia prohibitions on interest, representing partial ownership in an asset"],
        ["Structuring principles", "Returns are generated through asset-based profit-sharing rather than a fixed interest payment"],
    ])},
    "finance-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Riba", "The Islamic finance prohibition on charging or paying interest"],
        ["Risk-sharing contract", "Islamic finance instead structures returns around genuine risk-sharing arrangements between financier and borrower"],
    ])},
    "finance-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Microfinance institution sustainability", "Studies how microfinance lenders balance financial sustainability against their social mission of serving the poor"],
        ["Model", "Faces an inherent tension between charging rates sufficient for operational viability and keeping loans affordable for low-income borrowers"],
    ])},
    "finance-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Fintech lending", "Technology-driven lending platforms that often use non-traditional data sources for credit decisions"],
        ["Alternative credit scoring", "Incorporates data beyond traditional credit history to assess creditworthiness, potentially expanding access to credit"],
    ])},
    "finance-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Asset tokenization", "Represents ownership of a real-world or financial asset as a digital token on a blockchain"],
        ["Blockchain application", "Aims to improve liquidity and fractional ownership of traditionally illiquid assets like real estate"],
    ])},
    "finance-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Central bank digital currency", "A digital form of a country's official currency issued directly by its central bank"],
        ["Design consideration", "Involves trade-offs between privacy, financial stability, and the role of commercial banks in the monetary system"],
    ])},
    "finance-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Robo-advisory", "Automated investment platforms that construct and manage portfolios algorithmically with minimal human intervention"],
        ["Portfolio construction algorithm", "Typically implements modern portfolio theory principles like diversification and periodic rebalancing at low cost"],
    ])},
    "finance-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Safe withdrawal rate", "An estimated sustainable percentage of a retirement portfolio that can be withdrawn annually without depleting it prematurely"],
        ["Retirement income planning research", "Withdrawal rate research must account for sequence-of-returns risk and uncertain lifespan"],
    ])},
    "finance-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Four percent rule", "A widely cited rule of thumb suggesting a 4% initial withdrawal rate historically sustains a retirement portfolio for 30 years"],
        ["Contemporary critique", "Modern research questions whether current market valuations and longer lifespans still support the original 4% figure"],
    ])},
    "finance-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Annuitization puzzle", "Economic theory suggests retirees should annuitize much of their wealth, yet actual annuity purchase rates remain surprisingly low"],
        ["Retirement decision-making", "Explanations include bequest motives, distrust of insurers, and behavioral aversion to giving up control of a lump sum"],
    ])},
    "finance-m2-l71": {"data_table": table(["Term", "Meaning"], [
        ["Sequence-of-returns risk", "The risk that poor investment returns occurring early in retirement disproportionately harm a portfolio's long-term sustainability"],
        ["Decumulation portfolio", "Even with the same average return, the specific order returns occur significantly affects how long withdrawals can be sustained"],
    ])},
    "finance-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Social Security claiming strategy", "Determines the optimal age to begin claiming government retirement benefits given delayed-claiming credits"],
        ["Optimization", "Delaying benefits increases the eventual monthly payment, creating a genuine optimization trade-off against claiming earlier"],
    ])},
    "finance-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Tax-loss harvesting", "Systematically sells losing investments to realize losses that can offset capital gains for tax purposes"],
        ["Algorithm", "Automated tax-loss harvesting algorithms continuously scan portfolios for harvesting opportunities while avoiding wash-sale rule violations"],
    ])},
    "finance-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Asset location", "Strategically places different asset types in taxable versus tax-deferred accounts to minimize overall tax burden"],
        ["Strategy", "Tax-inefficient assets (like bonds) are typically best held in tax-deferred accounts, tax-efficient assets in taxable accounts"],
    ])},
    "finance-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Grantor retained annuity trust", "An estate planning vehicle that lets a grantor transfer future asset appreciation to heirs with minimal gift tax"],
        ["Estate planning application", "Effective when the trust's underlying assets appreciate faster than the IRS-assumed rate used to value the retained annuity"],
    ])},
    "finance-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Irrevocable life insurance trust", "Holds a life insurance policy outside the insured's taxable estate, removing the death benefit from estate tax exposure"],
        ["Estate planning application", "A common tool for providing estate liquidity to pay taxes without increasing the taxable estate itself"],
    ])},
    "finance-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Generation-skipping transfer tax", "A tax applying to wealth transfers that skip a generation, such as gifts directly to grandchildren"],
        ["Planning application", "Requires careful structuring to use available exemptions efficiently when transferring wealth across multiple generations"],
    ])},
    "finance-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Charitable remainder trust", "Provides income to a donor for a period, with the remaining assets ultimately going to a designated charity"],
        ["Philanthropic finance application", "Allows a donor to receive an income stream and tax benefits while ultimately supporting a charitable cause"],
    ])},
    "finance-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Qualified Opportunity Zone", "A US tax incentive program encouraging long-term investment in designated economically distressed areas"],
        ["Investment structure", "Offers capital gains tax deferral and potential exclusion benefits for investments held in a Qualified Opportunity Fund"],
    ])},
    "finance-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Mental accounting", "People treat money differently depending on its subjective source or intended use, rather than as fully fungible"],
        ["Household budgeting application", "Explains behaviors like maintaining a savings account while carrying credit card debt, despite the interest rate mismatch"],
    ])},
    "finance-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Life-cycle hypothesis", "Predicts individuals smooth consumption across their lifetime by saving during working years and drawing down savings in retirement"],
        ["Consumption and saving model", "A foundational framework for understanding household saving behavior over the life course"],
    ])},
    "finance-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Human capital", "An individual's future earning potential, treated as an implicit asset in overall portfolio theory"],
        ["Portfolio theory application", "Young workers' large, relatively bond-like human capital argues for holding more equity risk in their financial portfolio"],
    ])},
    "finance-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Target-date fund", "An investment fund that automatically shifts its asset allocation to become more conservative as a target retirement date approaches"],
        ["Glide path design", "The specific schedule by which the fund's stock-bond mix shifts over time significantly affects risk and expected return outcomes"],
    ])},
    "finance-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Factor investing", "Constructs portfolios targeting specific empirically documented return factors like value or momentum"],
        ["Smart beta strategy", "Systematic, rules-based approaches that aim to capture factor premiums more cheaply than traditional active management"],
    ])},
    "finance-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Liability-driven investment", "A pension fund investment strategy designed to match asset cash flows to the timing of expected future liabilities"],
        ["Pension fund application", "Prioritizes reducing funding-level volatility over maximizing pure investment return"],
    ])},
    "finance-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Defined benefit pension", "A retirement plan promising a specified benefit amount, with the employer bearing investment and longevity risk"],
        ["Actuarial assumption", "Funding calculations depend heavily on assumed future investment returns, mortality rates, and discount rates"],
    ])},
    "finance-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Longevity risk", "The risk that people live longer than expected, straining pension and retirement funding assumptions"],
        ["Mortality-linked security", "Financial instruments designed to transfer longevity risk to capital markets rather than concentrating it in pension funds"],
    ])},
    "finance-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Reverse mortgage", "Allows homeowners, typically retirees, to convert home equity into cash while continuing to live in the home"],
        ["Product design and risk", "Balances lender risk against providing retirees a way to access illiquid home equity for retirement income"],
    ])},
    "finance-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Payday lending", "Short-term, high-interest loans typically targeted at borrowers with limited access to traditional credit"],
        ["Consumer debt behavior economics", "Studied for both its role in providing emergency liquidity and its risk of trapping borrowers in cycles of debt"],
    ])},
    "finance-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Student loan repayment plan", "Various government programs offering different repayment schedules, including income-driven options"],
        ["Optimization", "Choosing the optimal plan depends on expected future income, loan forgiveness eligibility, and total interest cost trade-offs"],
    ])},
    "finance-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Household underdiversification", "Many households hold surprisingly concentrated portfolios (e.g. heavy in employer stock) despite the benefits of diversification"],
        ["Puzzle", "A well-documented anomaly relative to the strong theoretical case for broad diversification"],
    ])},
    "finance-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Financial literacy intervention", "Educational programs aimed at improving individuals' financial knowledge and decision-making"],
        ["Efficacy research", "Rigorous evaluations find mixed and often modest, short-lived effects on actual financial behavior"],
    ])},
    "finance-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Behavioral nudge", "A subtle change in how choices are presented that influences behavior without restricting options"],
        ["Retirement savings enrollment application", "Automatic enrollment defaults have been shown to substantially increase retirement plan participation rates"],
    ])},
    "finance-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Currency carry trade", "Borrows in a low-interest-rate currency to invest in a higher-interest-rate currency, profiting from the rate differential"],
        ["Crash risk", "Carry trades are prone to sudden, sharp reversals during periods of market stress, a well-documented tail risk"],
    ])},
    "finance-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Momentum anomaly", "Assets that have recently performed well tend to continue outperforming in the near term"],
        ["Reversal anomaly", "Over longer horizons, past winners tend to underperform and past losers tend to outperform, reversing the momentum pattern"],
    ])},
    "finance-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["CoVaR", "Measures a financial institution's contribution to overall systemic risk by estimating value at risk conditional on system-wide distress"],
        ["Marginal expected shortfall", "Estimates an institution's expected loss during a systemic crisis, capturing its contribution to overall financial system risk"],
    ])},
    "finance-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Shadow banking", "Credit intermediation activities occurring outside the traditional regulated banking system"],
        ["Financial stability concern", "Its rapid growth before 2008 and relative lack of regulatory oversight are widely cited as contributing to systemic financial risk"],
    ])},
    "finance-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Doctoral thesis seminar", "A capstone forum for presenting and defending an original contribution to finance research"],
        ["Original contribution", "Requires identifying a genuine gap in existing financial theory or evidence and offering a novel, rigorously evaluated resolution"],
    ])},
    "finance-m2-l99": {"data_table": table(["Term", "Meaning"], [
        ["Cryptocurrency exchange microstructure", "Studies the order book dynamics and trading mechanics specific to cryptocurrency trading venues"],
        ["Order book dynamics", "Cryptocurrency markets often exhibit distinctive liquidity and volatility patterns compared with traditional equity markets"],
    ])},
    "finance-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Green swan risk", "Climate-related financial risks that, unlike typical black swan events, are highly likely but difficult to predict precisely in timing"],
        ["Climate-related financial stability", "A growing concern for central banks and regulators assessing systemic risk from climate change impacts"],
    ])},
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Finance"]["lessons"]
    by_id = {lesson["id"]: lesson for lesson in lessons.values()} if isinstance(lessons, dict) else {
        lesson["id"]: lesson for lesson in lessons
    }

    for worked_n in range(101, 121):
        base_n = worked_n - 100
        base_key = f"finance-m2-l{base_n}"
        worked_key = f"finance-m2-l{worked_n}"
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
    print(f"Added {updated} fields across {len(CHARTS)} M2 Finance lessons.")


if __name__ == "__main__":
    main()
