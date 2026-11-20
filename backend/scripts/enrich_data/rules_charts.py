"""Charts for lessons whose topic is best understood from a picture of a curve
or a series. Curves are computed from the stated formula and labelled as
illustrative; real-world series use well-documented published figures."""
import math

from . import F, Case, Chart, Rule


def curve(fn, xs, name="y", places=4):
    return [{"x": round(x, 4), name: round(fn(x), places)} for x in xs]


def frange(a, b, step):
    n = int(round((b - a) / step))
    return [a + i * step for i in range(n + 1)]


def merge(*series):
    """Join per-series row lists that share x values."""
    rows = {}
    for rowlist in series:
        for row in rowlist:
            rows.setdefault(row["x"], {"x": row["x"]}).update({k: v for k, v in row.items() if k != "x"})
    return [rows[x] for x in sorted(rows)]


def _pdf(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def _binom(n, p):
    return lambda k: math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def _sir(beta=0.3, gamma=0.1, i0=0.001, days=160):
    s, i, r, rows = 1 - i0, i0, 0.0, []
    for d in range(days + 1):
        if d % 4 == 0:
            rows.append({"x": d, "Susceptible": round(s * 100, 2), "Infected": round(i * 100, 2), "Recovered": round(r * 100, 2)})
        ds, di, dr = -beta * s * i, beta * s * i - gamma * i, gamma * i
        s, i, r = s + ds, i + di, r + dr
    return rows


def _titration():
    rows = []
    for v in frange(0, 50, 2.5):
        total = (25 + v) / 1000
        if abs(v - 25) < 1e-9:
            ph = 7.0
        elif v < 25:
            ph = -math.log10((0.0025 - 0.1 * v / 1000) / total)
        else:
            ph = 14 + math.log10((0.1 * v / 1000 - 0.0025) / total)
        rows.append({"x": v, "pH": round(ph, 2)})
    return rows


def _trajectory(theta_deg, v=20.0, g=9.81):
    th = math.radians(theta_deg)
    def y(x):
        val = x * math.tan(th) - g * x * x / (2 * v * v * math.cos(th) ** 2)
        return round(val, 3) if val >= 0 else None
    return y


RULES = [
Rule("ch_normal", r"(?<!Multiple )Hypothesis Test|Normal Distribution|Central Limit|Confidence Interval|Z-Score|Standard Deviation", "", ["Math", "Data Science", "Business Analytics", "Science", "Biology", "R", "Python", "Economics", "Finance", "Health Education", "Machine Learning"],
     [F("Normal density", "f(x) = e^(−(x−μ)² ÷ 2σ²) ÷ (σ√(2π))", "About 68% of values lie within 1σ of the mean, 95% within 2σ and 99.7% within 3σ")],
     charts=[Chart("The standard normal curve", "line", "z-score (standard deviations from the mean)", "Density", curve(_pdf, frange(-4, 4, 0.25), "Standard normal"), ["Standard normal"], "Computed from the formula; μ = 0, σ = 1.")]),
Rule("ch_binom", r"Binomial|Bernoulli|Discrete Probability|(?<!Joint )Probability Distributions", "", ["Math", "Data Science", "Business Analytics", "Biology", "R", "Python"],
     [F("Binomial probability", "P(X = k) = C(n, k) · pᵏ · (1 − p)^(n−k)", "Chance of k successes in n independent trials")],
     charts=[Chart("Ten coin tosses versus a biased coin", "bar", "Number of heads k", "Probability",
                   merge(curve(_binom(10, 0.5), range(11), "p = 0.5"), curve(_binom(10, 0.3), range(11), "p = 0.3")), ["p = 0.5", "p = 0.3"], "Binomial distribution with n = 10.")]),
Rule("ch_logistic", r"Population (Growth|Ecology|Dynamics)|Carrying Capacity|Logistic Growth|Exponential Growth", "", ["Biology", "Environmental Science", "Science", "Geography", "Math", "Social Studies"],
     [F("Logistic growth", "dN/dt = r·N·(1 − N/K)", "K is the carrying capacity; growth slows as N approaches K")],
     charts=[Chart("Exponential versus logistic growth", "line", "Time", "Population",
                   merge([{"x": t, "Exponential (no limit)": round(5 * math.exp(0.35 * t), 1)} for t in frange(0, 14, 1) if 5 * math.exp(0.35 * t) <= 150],
                         curve(lambda t: 100 / (1 + 19 * math.exp(-0.35 * t)), frange(0, 14, 1), "Logistic (K = 100)", 1)),
                   ["Exponential (no limit)", "Logistic (K = 100)"], "Illustrative curves with r = 0.35 and N₀ = 5; the exponential curve is cut off once it passes 150.")]),
Rule("ch_decay", r"Radioactiv|Half-Life|Nuclear Decay|Radiocarbon|Carbon Dating|Radiometric", "", ["Physics", "Chemistry", "Science", "Environmental Science", "World History", "Biology", "Health Education"],
     [F("Radioactive decay", "N(t) = N₀ · (½)^(t ÷ t½)", "After each half-life half of the nuclei remain")],
     charts=[Chart("Fraction remaining after each half-life", "line", "Half-lives elapsed", "Fraction remaining", curve(lambda n: 0.5 ** n, frange(0, 5, 0.25), "Fraction remaining"), ["Fraction remaining"],
                   "Carbon-14 has a half-life of about 5,730 years, so 3 half-lives ≈ 17,190 years.")]),
Rule("ch_supply", r"Supply and Demand|Market Equilibrium|Price Mechanism|Demand and Supply|Law of Demand|Market Structures", "", ["Economics", "Business Studies", "MBA", "Finance", "Social Studies", "Business Analytics"],
     [], charts=[Chart("Supply, demand and the equilibrium price", "line", "Price ($)", "Quantity",
                   merge(curve(lambda p: 100 - 2 * p, frange(0, 50, 5), "Quantity demanded", 1), curve(lambda p: max(0.0, 4 * p - 20), frange(0, 50, 5), "Quantity supplied", 1)),
                   ["Quantity demanded", "Quantity supplied"], "Illustrative numbers: demand Qd = 100 − 2P and supply Qs = 4P − 20 meet at P = $20, Q = 60.")]),
Rule("ch_compound", r"Time Value of Money|Compound Interest|Present Value|Future Value|Savings and Investing|Retirement Planning", "", ["Finance", "Economics", "MBA", "Business Studies", "Math", "General Knowledge", "Business Analytics"],
     [F("Compound interest", "FV = PV · (1 + r)ᵗ", "Rule of 72: money doubles in about 72 ÷ (rate in %) years")],
     charts=[Chart("$1,000 at 5% a year: simple versus compound interest", "line", "Years", "Value ($)",
                   merge(curve(lambda t: 1000 + 50 * t, frange(0, 30, 5), "Simple interest", 0), curve(lambda t: 1000 * 1.05 ** t, frange(0, 30, 5), "Compound interest", 0)),
                   ["Simple interest", "Compound interest"], "Computed from the formulas.")]),
Rule("ch_activation", r"(^|: )Neural Networks?(:|$)|Activation Function|Perceptron|Deep Learning (Basics|Fundamentals)|Logistic Regression", "", ["Artificial Intelligence", "Machine Learning", "Data Science", "Natural Language Processing"],
     [F("Sigmoid and ReLU", "σ(x) = 1 ÷ (1 + e^(−x)),   ReLU(x) = max(0, x)", "Activation functions add non-linearity to a neural network")],
     charts=[Chart("Common activation functions", "line", "Input x", "Output",
                   merge(curve(lambda x: 1 / (1 + math.exp(-x)), frange(-6, 6, 0.5), "Sigmoid"), curve(math.tanh, frange(-6, 6, 0.5), "tanh"), curve(lambda x: max(0.0, x), frange(-6, 6, 0.5), "ReLU")),
                   ["Sigmoid", "tanh", "ReLU"], "Computed from the formulas.")]),
Rule("ch_bigo", r"Big-O|Big O|Algorithm Analysis|Time Complexity|Complexity Analysis|Sorting|Binary Search|Searching Algorithm|Recursion", "", ["Computer Science Engineering", "Python", "JavaScript", "Coding", "ICT & Computer Science", "R", "Data Science", "Web Development"],
     [], charts=[Chart("How running time grows with input size n", "line", "Input size n", "Steps",
                   merge(curve(lambda n: n, range(1, 11), "n", 1), curve(lambda n: n * math.log2(n), range(1, 11), "n log₂ n", 1), curve(lambda n: n * n, range(1, 11), "n²", 1), curve(lambda n: 2 ** n, range(1, 11), "2ⁿ", 1)),
                   ["n", "n log₂ n", "n²", "2ⁿ"], "Computed step counts; exponential algorithms become unusable very quickly.")]),
Rule("ch_projectile", r"Projectile|(?<!Relativistic )Kinematics|Motion in (Two|2) Dimensions|Free Fall", "", ["Physics", "Science", "Physical Education & Self-Defense", "Math"],
     [F("Range of a projectile", "R = v² · sin(2θ) ÷ g", "Maximum range at θ = 45° when launch and landing heights are equal")],
     charts=[Chart("Paths of a ball launched at 20 m/s", "line", "Horizontal distance (m)", "Height (m)",
                   merge(*[[{"x": x, name: _trajectory(a)(x)} for x in frange(0, 40, 2)] + [{"x": round(20.0 ** 2 * math.sin(math.radians(2 * a)) / 9.81, 2), name: 0}] for a, name in ((30, "30°"), (45, "45°"), (60, "60°"))]),
                   ["30°", "45°", "60°"], "Computed with g = 9.81 m/s², ignoring air resistance. 30° and 60° land at the same place.")]),
Rule("ch_titration", r"Titration|Acid-Base|Acids and Bases|pH and|Buffer", "", ["Chemistry", "Science", "Biology", "Cooking", "Environmental Science"],
     [F("pH", "pH = −log₁₀[H⁺]", "pH 7 is neutral at 25 °C")],
     charts=[Chart("Titrating 25 mL of 0.1 M HCl with 0.1 M NaOH", "line", "NaOH added (mL)", "pH", _titration(), ["pH"], "Computed; the steep jump near 25 mL marks the equivalence point.")]),
Rule("ch_lorenz", r"Gini|Lorenz|Income Inequality|Wealth Inequality|Income Distribution|Inequality Measurement", "", ["Economics", "Social Studies", "World Politics", "Civics", "Geography", "Business Studies"],
     [F("Gini coefficient", "G = 1 − 2 ∫₀¹ L(p) dp", "0 means perfect equality, 1 means one person has everything")],
     charts=[Chart("A Lorenz curve for an unequal society", "line", "Share of population (poorest first)", "Share of income",
                   merge(curve(lambda p: p, frange(0, 1, 0.1), "Perfect equality", 3), curve(lambda p: p * p, frange(0, 1, 0.1), "Example Lorenz curve (Gini = 0.33)", 3)),
                   ["Perfect equality", "Example Lorenz curve (Gini = 0.33)"], "Illustrative: L(p) = p² gives a Gini coefficient of ⅓.")]),
Rule("ch_breakeven", r"Break-Even|Cost-Volume|CVP Analysis|Contribution Margin|Cost Structures", "", ["Finance", "MBA", "Business Studies", "Operations Management", "Business Analytics", "Economics", "Project Management"],
     [F("Break-even quantity", "Q* = Fixed costs ÷ (Price − Variable cost per unit)", "Here 2,000 ÷ (10 − 6) = 500 units")],
     charts=[Chart("Break-even analysis", "line", "Units sold", "Dollars",
                   merge(curve(lambda q: 10 * q, frange(0, 1000, 100), "Revenue", 0), curve(lambda q: 2000 + 6 * q, frange(0, 1000, 100), "Total cost", 0)),
                   ["Revenue", "Total cost"], "Illustrative: price $10, variable cost $6, fixed costs $2,000; the lines cross at 500 units.")]),
Rule("ch_forgetting", r"Forgetting Curve|Spaced Repetition|Memory and Learning|Vocabulary Acquisition|Study Techniques|Learning Strategies", "", ["Foreign Languages", "English", "Critical Thinking", "Health Education", "Philosophy"],
     [F("Ebbinghaus forgetting curve", "R = e^(−t ÷ S)", "R is retention, t is time since learning and S is memory strength")],
     charts=[Chart("Retention over two weeks, with and without review", "line", "Days since learning", "Retention (%)",
                   merge(curve(lambda t: 100 * math.exp(-t / 2), frange(0, 14, 1), "No review (S = 2)", 1), curve(lambda t: 100 * math.exp(-t / 6), frange(0, 14, 1), "After spaced review (S = 6)", 1)),
                   ["No review (S = 2)", "After spaced review (S = 6)"], "Illustrative curves from Ebbinghaus's formula.")]),
Rule("ch_ppf", r"Production Possibilit|Opportunity Cost|Scarcity|Comparative Advantage", "", ["Economics", "Business Studies", "Social Studies", "MBA"],
     [], charts=[Chart("A production possibilities frontier", "line", "Units of good X", "Units of good Y", curve(lambda x: math.sqrt(100 - x * x), frange(0, 10, 1), "Production possibilities frontier", 2),
                   ["Production possibilities frontier"], "Illustrative: X² + Y² = 100. Points on the curve use all resources efficiently; moving along it shows the opportunity cost.")]),
Rule("ch_enzyme", r"Enzyme|Michaelis|Enzyme Kinetics", "", ["Biology", "Chemistry", "Science", "Health Education"],
     [F("Michaelis–Menten equation", "v = Vmax · [S] ÷ (Km + [S])", "Km is the substrate concentration at which v = Vmax ÷ 2")],
     charts=[Chart("Enzyme rate versus substrate concentration", "line", "Substrate concentration [S]", "Reaction rate v",
                   merge(curve(lambda s: 100 * s / (5 + s), frange(0, 50, 2.5), "No inhibitor", 1), curve(lambda s: 100 * s / (10 + s), frange(0, 50, 2.5), "Competitive inhibitor (Km doubles)", 1)),
                   ["No inhibitor", "Competitive inhibitor (Km doubles)"], "Illustrative: Vmax = 100, Km = 5. A competitive inhibitor raises Km but not Vmax.")]),
Rule("ch_slit", r"Double-Slit|Interference|Wave-Particle|Wave Optics", "", ["Physics", "Science", "Chemistry"],
     [F("Bright fringes", "d · sin θ = m · λ", "Slit spacing d, wavelength λ, order m")],
     charts=[Chart("Double-slit interference pattern", "line", "sin θ", "Relative intensity", curve(lambda s: math.cos(math.pi * 10 * s) ** 2, frange(-0.3, 0.3, 0.005), "Intensity"), ["Intensity"], "Computed for d = 10λ; ignores the single-slit envelope.")]),
Rule("ch_sir", r"Epidemic|Pandemic|Contagion|SIR Model|Disease Modeling|Infectious Disease|Outbreak", "", ["Biology", "Health Education", "Math", "Science", "Data Science", "Social Studies", "Environmental Science", "First Aid"],
     [F("Basic reproduction number", "R₀ = β ÷ γ", "If R₀ > 1 an outbreak can grow; herd immunity needs about 1 − 1/R₀ of people immune")],
     charts=[Chart("An epidemic in a SIR model (R₀ = 3)", "line", "Days", "% of population", _sir(), ["Susceptible", "Infected", "Recovered"], "Computed with β = 0.3 and γ = 0.1 per day, starting with 0.1% infected.")]),
Rule("ch_keeling", r"Climate Change|Global Warming|Greenhouse|Carbon Cycle|Keeling|Atmospheric Composition|Climate Science", "", None,
     [], charts=[Chart("Atmospheric CO₂ at Mauna Loa", "line", "Year", "CO₂ (ppm)",
                   [{"x": x, "CO₂ (ppm)": y} for x, y in ((1960, 316.9), (1970, 325.7), (1980, 338.8), (1990, 354.4), (2000, 369.7), (2010, 389.9), (2015, 400.8), (2020, 414.2), (2023, 421.1))],
                   ["CO₂ (ppm)"], "NOAA annual means, rounded. Source: NOAA Global Monitoring Laboratory.")],
     cases=[Case("The Keeling Curve", "1958–present", "Charles Keeling began measuring CO₂ on Mauna Loa in 1958 and showed concentrations rising year after year, with a seasonal rhythm from northern forests.", "Careful long-term measurement revealed the human fingerprint on the atmosphere.", "Keeling Curve")]),
Rule("ch_population", r"Population (Growth|Dynamics|Studies|Geography)|Demograph|Human Population|Overpopulation|Malthus", "", None,
     [], charts=[Chart("Years taken for world population to add each billion", "line", "Year", "World population (billions)",
                   [{"x": x, "Population (billions)": y} for x, y in ((1804, 1), (1927, 2), (1960, 3), (1974, 4), (1987, 5), (1999, 6), (2011, 7), (2022, 8))],
                   ["Population (billions)"], "UN milestone years: it took until 1804 to reach 1 billion but only 11–12 years for each of the latest billions.")]),
Rule("ch_depression", r"Great Depression|Interwar|New Deal|Stock Market Crash|Wall Street Crash", "", None,
     [], charts=[Chart("US unemployment rate, 1929–1940", "line", "Year", "Unemployment (%)",
                   [{"x": x, "Unemployment (%)": y} for x, y in ((1929, 3.2), (1930, 8.7), (1931, 15.9), (1932, 23.6), (1933, 24.9), (1934, 21.7), (1935, 20.1), (1936, 16.9), (1937, 14.3), (1938, 19.0), (1939, 17.2), (1940, 14.6))],
                   ["Unemployment (%)"], "Approximate historical estimates (Lebergott series); different sources vary by a point or two.")]),
Rule("ch_cosmic", r"Dark Matter|Dark Energy|Cosmology|Big Bang|Expanding Universe|Large-Scale Structure", "", ["Physics", "Science", "General Knowledge"],
     [], charts=[Chart("What the Universe is made of", "bar", "Component", "Share of total energy (%)",
                   [{"x": "Ordinary matter", "Share (%)": 4.9}, {"x": "Dark matter", "Share (%)": 26.8}, {"x": "Dark energy", "Share (%)": 68.3}],
                   ["Share (%)"], "Planck 2018 results.")]),
Rule("ch_moore", r"Moore's Law|Transistor|Microprocessor|Semiconductor|Computer Architecture|History of Computing|Computer Hardware|Digital Logic", "", ["Computer Science Engineering", "ICT & Computer Science", "Physics", "Cloud Computing", "General Knowledge", "Coding"],
     [], charts=[Chart("Transistors per processor (log scale)", "line", "Year", "Transistors",
                   [{"x": x, "Transistors": y} for x, y in ((1971, 2300), (1978, 29000), (1985, 275000), (1993, 3100000), (2000, 42000000), (2006, 291000000), (2020, 16000000000))],
                   ["Transistors"], "Intel 4004, 8086, 80386, Pentium, Pentium 4, Core 2 Duo and Apple M1 (rounded). Counts have grown roughly exponentially.", True)],
     cases=[Case("Moore's Law", "1965", "Gordon Moore observed that the number of components on a chip was doubling about every year, later revised to about every two years.", "A forecast that guided the whole industry's roadmap for decades.", "Moore's law")]),
Rule("ch_ionisation", r"Periodic (Table|Trends|Properties)|Ionization Energy|Ionisation Energy|Atomic Structure|Electron Configuration|Atomic Radius", "", ["Chemistry", "Physics", "Science"],
     [], charts=[Chart("First ionisation energy across period 2", "bar", "Element", "Energy (kJ/mol)",
                   [{"x": e, "kJ/mol": v} for e, v in (("Li", 520), ("Be", 900), ("B", 801), ("C", 1086), ("N", 1402), ("O", 1314), ("F", 1681), ("Ne", 2081))],
                   ["kJ/mol"], "Energy rises across the period, with small dips at B and O explained by electron configuration.")]),
Rule("ch_earth", r"Plate Tectonics|Earth's Interior|Structure of the Earth|Earth Structure|Seismic|Earthquake|Volcan", "", ["Geography", "Science", "Environmental Science", "Physics", "General Knowledge"],
     [], charts=[Chart("Thickness of Earth's layers", "bar", "Layer", "Thickness (km)",
                   [{"x": "Crust (continental, typical)", "km": 35}, {"x": "Mantle", "km": 2850}, {"x": "Outer core", "km": 2260}, {"x": "Inner core (radius)", "km": 1220}],
                   ["km"], "Approximate values; Earth's radius is about 6,371 km.")]),
Rule("ch_macros", r"Macronutrient|Nutrition|Calorie|Energy Balance|Diet|Metabolism", "", ["Health Education", "Cooking", "Biology", "Physical Education & Self-Defense", "Science", "First Aid"],
     [], charts=[Chart("Energy in each gram of nutrient", "bar", "Nutrient", "kcal per gram",
                   [{"x": "Carbohydrate", "kcal/g": 4}, {"x": "Protein", "kcal/g": 4}, {"x": "Fat", "kcal/g": 9}, {"x": "Alcohol", "kcal/g": 7}],
                   ["kcal/g"], "Standard Atwater energy factors.")]),
Rule("ch_atmosphere", r"Earth's Atmosphere|Atmospheric Structure|Layers of the Atmosphere|Meteorology|Weather and Climate|Weather Systems", "", ["Geography", "Science", "Physics", "Environmental Science", "General Knowledge"],
     [], charts=[Chart("Temperature through the atmosphere (International Standard Atmosphere)", "line", "Altitude (km)", "Temperature (°C)",
                   [{"x": x, "°C": y} for x, y in ((0, 15), (11, -56.5), (20, -56.5), (32, -44.5), (47, -2.5), (51, -2.5), (71, -58.5), (86, -86.5))],
                   ["°C"], "Temperature falls through the troposphere, rises in the stratosphere (ozone absorbs UV), falls in the mesosphere.")]),
Rule("ch_regression", r"Linear Regression|Regression Analysis|Least Squares|Simple Regression|Correlation", "", ["Math", "Data Science", "Business Analytics", "Economics", "R", "Python", "Machine Learning", "Science", "Finance", "Biology"],
     [F("Simple linear regression", "ŷ = β₀ + β₁·x,   β₁ = Σ(x − x̄)(y − ȳ) ÷ Σ(x − x̄)²", "The least-squares line minimises the sum of squared vertical errors")],
     charts=[Chart("Anscombe's first dataset with its least-squares line", "scatter", "x", "y",
                   [{"x": x, "Observed": y} for x, y in zip((10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5), (8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68))]
                   + [{"x": x, "Fitted line": round(3.0 + 0.5 * x, 2)} for x in (3, 15)],
                   ["Observed"], "Real data from Anscombe (1973); the fitted line is y = 3.0 + 0.5x.", lines=["Fitted line"])]),
Rule("ch_overfit", r"Overfitting|Bias-Variance|Regularization|Cross-Validation", "", ["Machine Learning", "Artificial Intelligence", "Data Science", "Business Analytics", "R", "Python"],
     charts=[Chart("Training versus validation error as a model grows more complex", "line", "Model complexity", "Error",
                   merge(curve(lambda c: 1.0 / (1 + 0.8 * c), frange(0, 10, 1), "Training error", 3), curve(lambda c: 1.0 / (1 + 0.8 * c) + 0.012 * c * c, frange(0, 10, 1), "Validation error", 3)),
                   ["Training error", "Validation error"], "Illustrative: training error keeps falling, but validation error rises once the model starts fitting noise (overfitting).")]),
]
