#!/usr/bin/env python3
"""Breadth-first pass: add genuine, hand-checked data_table / graph /
formulae content to a representative batch of Math lessons at every level
from Grade 1 through Masters Year 2 (Grade 5 Math already has full pilot
coverage via add_grade5_math_lesson_charts.py -- this script deliberately
skips grade5.json).

Every number here is either a real, verifiable mathematical fact (a
Pythagorean triple, a known Riemann zeta value, RSA's textbook p=61/q=53
example, etc.) or explicitly-labelled illustrative example data for a
worked problem (e.g. "Favorite Fruit Survey (Example Data)") -- never a
claim about a specific real-world dataset presented as fact.

This is "breadth first": a solid handful of real lessons per level so every
grade visibly has real content today. Depth (covering every remaining
lesson per level) is deferred to later batches, following the same pattern
established here and in add_grade5_math_lesson_charts.py.

Idempotent: only fills in `data_table` / `graph` / `formulae` fields that
aren't already set, so it won't clobber a hand edit on re-run.

Re-run after editing:
    python3 backend/scripts/add_math_charts_all_levels.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_DIR = BASE_DIR / "syllabus"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


def graph(title, points, x_axis, y_axis):
    return {"title": title, "points": points, "x_axis": x_axis, "y_axis": y_axis}


# ---------------------------------------------------------------------------
# Grade 1
# ---------------------------------------------------------------------------
GRADE1: dict[str, dict] = {
    "math-g1-l3": {
        "data_table": table(["+", "0", "1", "2", "3", "4", "5"], [
            ["0", "0", "1", "2", "3", "4", "5"],
            ["1", "1", "2", "3", "4", "5", "6"],
            ["2", "2", "3", "4", "5", "6", "7"],
            ["3", "3", "4", "5", "6", "7", "8"],
            ["4", "4", "5", "6", "7", "8", "9"],
            ["5", "5", "6", "7", "8", "9", "10"],
        ]),
        "formulae": ["3 + 4 = 7", "5 + 5 = 10"],
    },
    "math-g1-l10": {
        "graph": graph("Skip Counting by 5s", [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], "Step number", "Count"),
        "data_table": table(["Skip by", "Sequence"], [
            ["2s", "2, 4, 6, 8, 10"], ["5s", "5, 10, 15, 20, 25"], ["10s", "10, 20, 30, 40, 50"],
        ]),
    },
    "math-g1-l16": {
        "data_table": table(["Number", "Tens", "Ones"], [
            ["23", "2", "3"], ["47", "4", "7"], ["58", "5", "8"], ["90", "9", "0"],
        ]),
    },
    "math-g1-l17": {
        "data_table": table(["Shape", "Number of Sides", "Number of Corners"], [
            ["Triangle", "3", "3"], ["Square", "4", "4"], ["Rectangle", "4", "4"],
            ["Pentagon", "5", "5"], ["Hexagon", "6", "6"],
        ]),
    },
    "math-g1-l20": {
        "data_table": table(["Coin", "Value"], [
            ["Penny", "1 cent"], ["Nickel", "5 cents"], ["Dime", "10 cents"], ["Quarter", "25 cents"],
        ]),
        "formulae": ["1 nickel = 5 pennies", "1 dime = 2 nickels", "1 quarter = 25 pennies"],
    },
}

# ---------------------------------------------------------------------------
# Grade 2
# ---------------------------------------------------------------------------
GRADE2: dict[str, dict] = {
    "math-g2-l4": {
        "data_table": table(["×", "1", "2", "3", "4", "5"], [
            ["1", "1", "2", "3", "4", "5"],
            ["2", "2", "4", "6", "8", "10"],
            ["3", "3", "6", "9", "12", "15"],
            ["4", "4", "8", "12", "16", "20"],
            ["5", "5", "10", "15", "20", "25"],
        ]),
        "formulae": ["3 × 4 = 12", "5 × 5 = 25"],
    },
    "math-g2-l5": {
        "data_table": table(["Fraction", "Meaning", "Decimal"], [
            ["1/2", "One of two equal parts", "0.5"],
            ["1/4", "One of four equal parts", "0.25"],
            ["3/4", "Three of four equal parts", "0.75"],
        ]),
    },
    "math-g2-l6": {
        "data_table": table(["Coin/Bill", "Value"], [
            ["Penny", "$0.01"], ["Nickel", "$0.05"], ["Dime", "$0.10"],
            ["Quarter", "$0.25"], ["$1 Bill", "$1.00"],
        ]),
    },
    "math-g2-l17": {
        "graph": graph("Favorite Fruit Survey (Example Data)", [8, 5, 10, 3], "Fruit: Apple, Banana, Grape, Orange", "Number of Votes"),
    },
    "math-g2-l19": {
        "data_table": table(["Type", "Examples"], [
            ["Even", "2, 4, 6, 8, 10"], ["Odd", "1, 3, 5, 7, 9"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Grade 3
# ---------------------------------------------------------------------------
GRADE3: dict[str, dict] = {
    "math-g3-l1": {
        "data_table": table(["n", "2×n", "5×n", "10×n"], [
            ["1", "2", "5", "10"], ["2", "4", "10", "20"], ["5", "10", "25", "50"],
            ["8", "16", "40", "80"], ["10", "20", "50", "100"],
        ]),
    },
    "math-g3-l4": {
        "data_table": table(["Rectangle (L × W)", "Perimeter", "Area"], [
            ["4 × 3", "14", "12"], ["5 × 5", "20", "25"], ["6 × 2", "16", "12"],
        ]),
        "formulae": ["Perimeter = 2 × (length + width)", "Area = length × width"],
    },
    "math-g3-l5": {
        "data_table": table(["Fraction", "Decimal"], [
            ["1/10", "0.1"], ["3/10", "0.3"], ["5/10", "0.5"], ["9/10", "0.9"],
        ]),
    },
    "math-g3-l16": {
        "graph": graph("Books Read Each Month (Example Data)", [3, 5, 4, 7, 6, 8], "Month", "Books Read"),
    },
    "math-g3-l20": {
        "data_table": table(["Pattern", "Rule", "Next 3 Terms"], [
            ["2, 4, 6, 8", "+2", "10, 12, 14"],
            ["5, 10, 15, 20", "+5", "25, 30, 35"],
            ["1, 2, 4, 8", "×2", "16, 32, 64"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Grade 4
# ---------------------------------------------------------------------------
GRADE4: dict[str, dict] = {
    "math-g4-l4": {
        "data_table": table(["Angle Type", "Range"], [
            ["Acute", "Less than 90°"], ["Right", "Exactly 90°"],
            ["Obtuse", "Between 90° and 180°"], ["Straight", "Exactly 180°"],
        ]),
    },
    "math-g4-l8": {
        "data_table": table(["Number", "Factors"], [
            ["12", "1, 2, 3, 4, 6, 12"], ["18", "1, 2, 3, 6, 9, 18"],
            ["24", "1, 2, 3, 4, 6, 8, 12, 24"],
        ]),
    },
    "math-g4-l9": {
        "data_table": table(["Number", "Prime or Composite"], [
            ["2", "Prime"], ["7", "Prime"], ["9", "Composite"], ["11", "Prime"], ["15", "Composite"],
        ]),
    },
    "math-g4-l10": {
        "data_table": table(["Fraction", "Equivalent Fractions"], [
            ["1/2", "2/4, 3/6, 4/8"], ["1/3", "2/6, 3/9, 4/12"], ["2/3", "4/6, 6/9, 8/12"],
        ]),
    },
    "math-g4-l14": {
        "data_table": table(["Shape", "Perimeter Formula", "Area Formula"], [
            ["Rectangle", "2(l + w)", "l × w"], ["Square", "4s", "s²"],
            ["Triangle", "a + b + c", "½ × base × height"],
        ]),
    },
    "math-g4-l19": {
        "graph": graph("Class Pet Survey (Example Data)", [12, 7, 4, 9], "Pet: Dog, Cat, Fish, Bird", "Number of Students"),
    },
}

# ---------------------------------------------------------------------------
# Grade 6
# ---------------------------------------------------------------------------
GRADE6: dict[str, dict] = {
    "math-g6-l9": {
        "data_table": table(["Ratio", "Simplified"], [
            ["4:8", "1:2"], ["6:9", "2:3"], ["10:15", "2:3"],
        ]),
    },
    "math-g6-l11": {
        "data_table": table(["Fraction", "Decimal", "Percent"], [
            ["1/4", "0.25", "25%"], ["1/2", "0.5", "50%"], ["3/4", "0.75", "75%"], ["1/5", "0.2", "20%"],
        ]),
    },
    "math-g6-l14": {
        "data_table": table(["Numbers", "GCF", "LCM"], [
            ["12, 18", "6", "36"], ["8, 12", "4", "24"], ["15, 20", "5", "60"],
        ]),
    },
    "math-g6-l16": {
        "data_table": table(["Expression", "Value"], [
            ["2³", "8"], ["3²", "9"], ["5³", "125"], ["10⁴", "10,000"],
        ]),
        "formulae": ["aᵐ × aⁿ = aᵐ⁺ⁿ", "(aᵐ)ⁿ = aᵐⁿ"],
    },
    "math-g6-l20": {
        "formulae": ["Circumference = 2πr", "Circumference = πd"],
        "data_table": table(["Radius", "Circumference (≈)"], [
            ["1", "6.28"], ["5", "31.4"], ["10", "62.8"],
        ]),
    },
    "math-g6-l25": {
        "data_table": table(["Data Set", "Mean", "Median", "Mode", "Range"], [
            ["3, 4, 5, 6, 8, 8", "5.67", "5.5", "8", "5"],
        ]),
        "formulae": ["Mean = (Sum of values) ÷ (Number of values)", "Range = Maximum − Minimum"],
    },
}

# ---------------------------------------------------------------------------
# Grade 7
# ---------------------------------------------------------------------------
GRADE7: dict[str, dict] = {
    "math-g7-l2": {
        "formulae": ["a² + b² = c²"],
        "data_table": table(["a", "b", "c (hypotenuse)"], [
            ["3", "4", "5"], ["6", "8", "10"], ["5", "12", "13"],
        ]),
    },
    "math-g7-l8": {
        "formulae": ["Simple Interest = P × r × t", "Compound Interest = P(1 + r)ᵗ − P"],
        "data_table": table(["Principal", "Rate", "Years", "Simple Interest"], [
            ["$1,000", "5%", "1", "$50"], ["$1,000", "5%", "2", "$100"], ["$1,000", "5%", "3", "$150"],
        ]),
    },
    "math-g7-l15": {
        "data_table": table(["Number", "Square Root", "Cube Root"], [
            ["8", "2.83", "2"], ["27", "5.20", "3"], ["64", "8", "4"],
        ]),
    },
    "math-g7-l21": {
        "formulae": ["Circumference = 2πr", "Area = πr²"],
        "data_table": table(["Radius", "Circumference", "Area"], [
            ["1", "6.28", "3.14"], ["5", "31.4", "78.5"], ["10", "62.8", "314"],
        ]),
    },
    "math-g7-l38": {
        "formulae": ["Speed = Distance ÷ Time"],
        "data_table": table(["Distance (km)", "Time (h)", "Speed (km/h)"], [
            ["100", "2", "50"], ["150", "3", "50"], ["240", "4", "60"],
        ]),
    },
    "math-g7-l40": {
        "data_table": table(["Set Operation", "Symbol", "Meaning"], [
            ["Union", "A ∪ B", "Elements in A or B"],
            ["Intersection", "A ∩ B", "Elements in both A and B"],
            ["Complement", "A′", "Elements not in A"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Grade 8
# ---------------------------------------------------------------------------
GRADE8: dict[str, dict] = {
    "math-g8-l2": {
        "formulae": ["x = (−b ± √(b² − 4ac)) / 2a"],
        "data_table": table(["Equation", "a", "b", "c", "Roots"], [
            ["x² − 5x + 6 = 0", "1", "-5", "6", "2, 3"],
            ["x² − 3x − 4 = 0", "1", "-3", "-4", "4, -1"],
        ]),
    },
    "math-g8-l15": {
        "data_table": table(["n", "n²", "√n"], [
            ["4", "16", "2"], ["9", "81", "3"], ["10", "100", "3.162"],
        ]),
    },
    "math-g8-l16": {
        "data_table": table(["n", "n³", "∛n"], [
            ["2", "8", "1.26"], ["3", "27", "1.442"], ["5", "125", "1.71"],
        ]),
    },
    "math-g8-l27": {
        "data_table": table(["Ladder Length", "Base Distance", "Height Reached"], [
            ["13 ft", "5 ft", "12 ft"], ["10 ft", "6 ft", "8 ft"],
        ]),
        "formulae": ["a² + b² = c²"],
    },
    "math-g8-l34": {
        "formulae": ["Speed = Distance ÷ Time"],
        "data_table": table(["Distance (km)", "Speed (km/h)", "Time (h)"], [
            ["120", "60", "2"], ["300", "75", "4"], ["50", "25", "2"],
        ]),
    },
    "math-g8-l39": {
        "formulae": ["sin θ = opposite / hypotenuse", "cos θ = adjacent / hypotenuse", "tan θ = opposite / adjacent"],
        "data_table": table(["Angle", "sin", "cos", "tan"], [
            ["30°", "0.5", "0.866", "0.577"], ["45°", "0.707", "0.707", "1"], ["60°", "0.866", "0.5", "1.732"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Grade 9
# ---------------------------------------------------------------------------
GRADE9: dict[str, dict] = {
    "math-g9-l9": {
        "formulae": ["x = (−b ± √(b² − 4ac)) / 2a"],
        "data_table": table(["a", "b", "c", "Discriminant", "Roots"], [
            ["1", "-3", "2", "1", "1, 2"], ["1", "2", "-8", "36", "2, -4"],
        ]),
    },
    "math-g9-l16": {
        "data_table": table(["Radical", "Simplified"], [
            ["√50", "5√2"], ["√72", "6√2"], ["√18", "3√2"],
        ]),
    },
    "math-g9-l27": {
        "formulae": ["aₙ = a₁ + (n − 1)d", "Sₙ = n/2 × (2a₁ + (n − 1)d)"],
        "data_table": table(["n", "aₙ (a₁ = 3, d = 4)"], [
            ["1", "3"], ["2", "7"], ["3", "11"], ["4", "15"], ["5", "19"],
        ]),
    },
    "math-g9-l36": {
        "formulae": ["a² + b² = c²"],
        "data_table": table(["a", "b", "c"], [
            ["8", "15", "17"], ["7", "24", "25"], ["9", "40", "41"],
        ]),
    },
    "math-g9-l41": {
        "formulae": ["Circumference = 2πr", "Area = πr²"],
        "data_table": table(["Radius", "Circumference", "Area"], [
            ["2", "12.57", "12.57"], ["4", "25.13", "50.27"], ["6", "37.70", "113.10"],
        ]),
    },
    "math-g9-l48": {
        "formulae": ["(A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ"],
        "data_table": table(["Matrix A", "Matrix B", "A + B"], [
            ["[[1,2],[3,4]]", "[[5,6],[7,8]]", "[[6,8],[10,12]]"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Grade 10
# ---------------------------------------------------------------------------
GRADE10: dict[str, dict] = {
    "math-g10-l1": {
        "formulae": ["d/dx(xⁿ) = n·xⁿ⁻¹", "d/dx(sin x) = cos x", "d/dx(eˣ) = eˣ"],
        "data_table": table(["f(x)", "f'(x)"], [
            ["x³", "3x²"], ["x⁴", "4x³"], ["sin x", "cos x"], ["eˣ", "eˣ"],
        ]),
    },
    "math-g10-l2": {
        "formulae": ["∫xⁿ dx = xⁿ⁺¹/(n+1) + C"],
        "data_table": table(["f(x)", "∫f(x)dx"], [
            ["x²", "x³/3 + C"], ["x³", "x⁴/4 + C"], ["cos x", "sin x + C"],
        ]),
    },
    "math-g10-l11": {
        "formulae": ["logₐ(xy) = logₐx + logₐy", "logₐ(x/y) = logₐx − logₐy"],
        "data_table": table(["x", "log₁₀ x", "ln x"], [
            ["1", "0", "0"], ["10", "1", "2.303"], ["100", "2", "4.605"],
        ]),
    },
    "math-g10-l17": {
        "data_table": table(["Angle", "sin", "cos", "tan"], [
            ["0°", "0", "1", "0"], ["30°", "0.5", "0.866", "0.577"],
            ["45°", "0.707", "0.707", "1"], ["90°", "1", "0", "undefined"],
        ]),
    },
    "math-g10-l24": {
        "formulae": ["det([[a,b],[c,d]]) = ad − bc"],
        "data_table": table(["Matrix", "Determinant"], [
            ["[[2,3],[1,4]]", "5"], ["[[1,0],[0,1]]", "1"],
        ]),
    },
    "math-g10-l28": {
        "data_table": table(["Expression", "Result"], [
            ["(2+3i) + (1−i)", "3+2i"], ["(2+3i) × (1−i)", "5+i"], ["i²", "−1"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level C1
# ---------------------------------------------------------------------------
LEVEL_C1: dict[str, dict] = {
    "math-c1-l9": {
        "data_table": table(["x", "f(x) = (x²−1)/(x−1)"], [
            ["0.9", "1.9"], ["0.99", "1.99"], ["1.01", "2.01"], ["1.1", "2.1"],
        ]),
        "formulae": ["lim(x→1) (x²−1)/(x−1) = 2"],
    },
    "math-c1-l12": {
        "formulae": ["d/dx(xⁿ) = nxⁿ⁻¹", "d/dx(c) = 0"],
        "data_table": table(["f(x)", "f'(x)"], [
            ["x²", "2x"], ["5x³", "15x²"], ["7", "0"],
        ]),
    },
    "math-c1-l19": {
        "data_table": table(["iⁿ", "Value"], [
            ["i¹", "i"], ["i²", "−1"], ["i³", "−i"], ["i⁴", "1"],
        ]),
    },
    "math-c1-l37": {
        "data_table": table(["Number", "Prime Factorization"], [
            ["60", "2² × 3 × 5"], ["84", "2² × 3 × 7"], ["100", "2² × 5²"],
        ]),
    },
    "math-c1-l45": {
        "data_table": table(["Data Set", "Mean", "Variance", "Standard Deviation"], [
            ["2, 4, 4, 4, 5, 5, 7, 9", "5", "4", "2"],
        ]),
        "formulae": ["Variance = (Σ(x − mean)²) / n", "Standard Deviation = √Variance"],
    },
}

# ---------------------------------------------------------------------------
# Level C2
# ---------------------------------------------------------------------------
LEVEL_C2: dict[str, dict] = {
    "math-c2-l8": {
        "formulae": ["(fg)' = f'g + fg'", "(f/g)' = (f'g − fg') / g²"],
        "data_table": table(["f(x)", "g(x)", "(fg)'(x)"], [
            ["x²", "x³", "5x⁴"],
        ]),
    },
    "math-c2-l12": {
        "formulae": ["∫ₐᵇ f'(x)dx = f(b) − f(a)"],
        "data_table": table(["Integral", "Result"], [
            ["∫₀² x²dx", "8/3"], ["∫₁³ 2x dx", "8"],
        ]),
    },
    "math-c2-l19": {
        "data_table": table(["Operation", "Result"], [
            ["(3+2i) + (1+4i)", "4+6i"], ["(3+2i) − (1+4i)", "2−2i"], ["|3+4i|", "5"],
        ]),
    },
    "math-c2-l31": {
        "data_table": table(["gcd(a, b)", "Euclidean Algorithm Steps"], [
            ["gcd(48, 18)", "48 = 2×18 + 12; 18 = 1×12 + 6; 12 = 2×6 + 0 → gcd = 6"],
        ]),
    },
    "math-c2-l42": {
        "data_table": table(["Range", "Percentage of Data"], [
            ["μ ± 1σ", "68%"], ["μ ± 2σ", "95%"], ["μ ± 3σ", "99.7%"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level M1 (Masters Year 1)
# ---------------------------------------------------------------------------
LEVEL_M1: dict[str, dict] = {
    "math-m1-l3": {
        "data_table": table(["Concept", "Riemann Integration", "Lebesgue Integration"], [
            ["Partitions", "Domain (x-axis)", "Range (y-axis)"],
            ["Dirichlet function (1 on rationals, 0 on irrationals)", "Not integrable", "Integrable (= 0)"],
        ]),
    },
    "math-m1-l9": {
        "data_table": table(["Number Field", "Degree over ℚ"], [
            ["ℚ(√2)", "2"], ["ℚ(i)", "2"], ["ℚ(∛2)", "3"],
        ]),
    },
    "math-m1-l28": {
        "formulae": ["ζ(s) = Σ 1/nˢ for n = 1 to ∞", "ζ(2) = π²/6"],
        "data_table": table(["s", "ζ(s) (approx)"], [
            ["2", "1.6449"], ["4", "1.0823"],
        ]),
    },
    "math-m1-l90": {
        "formulae": ["H(X) = −Σ p(x) log₂ p(x)"],
        "data_table": table(["Distribution", "Entropy (bits)"], [
            ["Fair coin (0.5, 0.5)", "1"], ["Biased coin (0.9, 0.1)", "0.469"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level M2 (Masters Year 2)
# ---------------------------------------------------------------------------
LEVEL_M2: dict[str, dict] = {
    "math-m2-l34": {
        "data_table": table(["Fact", "Value"], [
            ["First nontrivial zero (imaginary part)", "≈ 14.135"], ["Conjectured real part", "1/2"],
        ]),
    },
    "math-m2-l15": {
        "data_table": table(["n", "Fermat's Last Theorem (xⁿ + yⁿ = zⁿ)"], [
            ["n = 2", "Has solutions, e.g. 3² + 4² = 5²"],
            ["n > 2", "No positive integer solutions (proved by Andrew Wiles, 1995)"],
        ]),
    },
    "math-m2-l60": {
        "data_table": table(["Knot", "Crossing Number"], [
            ["Unknot", "0"], ["Trefoil knot", "3"], ["Figure-eight knot", "4"],
        ]),
    },
    "math-m2-l71": {
        "data_table": table(["Family of Finite Simple Groups", "Example"], [
            ["Cyclic groups of prime order", "ℤ/pℤ"],
            ["Alternating groups", "Aₙ, n ≥ 5"],
            ["Sporadic groups", "Monster group (order ≈ 8 × 10⁵³)"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level UG1
# ---------------------------------------------------------------------------
LEVEL_UG1: dict[str, dict] = {
    "math-ug1-l3": {
        "formulae": ["eˣ = 1 + x + x²/2! + x³/3! + ...", "sin x = x − x³/3! + x⁵/5! − ..."],
        "data_table": table(["Function", "Maclaurin Series (first terms)"], [
            ["eˣ", "1 + x + x²/2 + x³/6"], ["cos x", "1 − x²/2 + x⁴/24"],
        ]),
    },
    "math-ug1-l19": {
        "formulae": ["det([[a,b],[c,d]]) = ad − bc"],
        "data_table": table(["3×3 Matrix", "Determinant"], [
            ["[[1,2,3],[0,1,4],[5,6,0]]", "1"],
        ]),
    },
    "math-ug1-l38": {
        "data_table": table(["f(t)", "ℒ{f(t)}"], [
            ["1", "1/s"], ["t", "1/s²"], ["eᵃᵗ", "1/(s − a)"], ["sin(at)", "a/(s² + a²)"],
        ]),
    },
    "math-ug1-l48": {
        "data_table": table(["Group", "Order"], [
            ["ℤ/6ℤ", "6"], ["S₃ (symmetric group on 3 elements)", "6"], ["Klein four-group V₄", "4"],
        ]),
    },
    "math-ug1-l54": {
        "formulae": ["P(n,r) = n! / (n − r)!", "C(n,r) = n! / (r!(n − r)!)"],
        "data_table": table(["n, r", "P(n,r)", "C(n,r)"], [
            ["5, 2", "20", "10"], ["6, 3", "120", "20"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level UG2
# ---------------------------------------------------------------------------
LEVEL_UG2: dict[str, dict] = {
    "math-ug2-l9": {
        "data_table": table(["Matrix", "Eigenvalues"], [
            ["[[2,0],[0,3]]", "2, 3"], ["[[4,1],[2,3]]", "5, 2"],
        ]),
    },
    "math-ug2-l28": {
        "formulae": ["∮f(z)dz = 2πi × Σ Res(f, aₖ)"],
        "data_table": table(["f(z)", "Pole", "Residue"], [
            ["1/z", "z = 0", "1"], ["1/(z²+1)", "z = i", "1/(2i)"],
        ]),
    },
    "math-ug2-l29": {
        "formulae": ["f(x) = a₀/2 + Σ(aₙcos(nx) + bₙsin(nx))"],
        "data_table": table(["Function", "Fourier Coefficient Pattern"], [
            ["Square wave", "bₙ = 4/(nπ) for odd n"],
        ]),
    },
    "math-ug2-l40": {
        "data_table": table(["Field Extension", "Degree"], [
            ["ℚ(√2)/ℚ", "2"], ["ℂ/ℝ", "2"], ["𝔽₄/𝔽₂", "2"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level UG3
# ---------------------------------------------------------------------------
LEVEL_UG3: dict[str, dict] = {
    "math-ug3-l12": {
        "data_table": table(["RSA Concept", "Textbook Example"], [
            ["Modulus n = p × q", "p = 61, q = 53 → n = 3233"],
            ["Euler's totient φ(n)", "φ(3233) = 60 × 52 = 3120"],
        ]),
    },
    "math-ug3-l30": {
        "formulae": ["∇f = λ∇g"],
        "data_table": table(["Problem", "Solution"], [
            ["Maximize xy subject to x + y = 10", "x = 5, y = 5, max = 25"],
        ]),
    },
    "math-ug3-l40": {
        "data_table": table(["Game", "Nash Equilibrium"], [
            ["Prisoner's Dilemma", "(Defect, Defect)"], ["Matching Pennies", "Mixed strategy (1/2, 1/2)"],
        ]),
    },
    "math-ug3-l80": {
        "data_table": table(["Fact", "Detail"], [
            ["Theorem statement", "No positive integers a, b, c satisfy aⁿ + bⁿ = cⁿ for n > 2"],
            ["Conjectured by", "Pierre de Fermat, 1637"],
            ["Proved by", "Andrew Wiles, 1994/1995"],
        ]),
    },
}

# ---------------------------------------------------------------------------
# Level UG4
# ---------------------------------------------------------------------------
LEVEL_UG4: dict[str, dict] = {
    "math-ug4-l25": {
        "formulae": ["π(x) ~ x / ln(x)"],
        "data_table": table(["x", "π(x) (actual)", "x/ln(x) (approx)"], [
            ["100", "25", "21.7"], ["1,000", "168", "144.8"], ["10,000", "1,229", "1,085.7"],
        ]),
    },
    "math-ug4-l26": {
        "formulae": ["y² = x³ + ax + b"],
        "data_table": table(["Curve", "Equation"], [
            ["Example elliptic curve", "y² = x³ − x + 1"],
        ]),
    },
    "math-ug4-l59": {
        "formulae": ["C = S₀N(d1) − Ke^(−rt)N(d2)"],
        "data_table": table(["Variable", "Meaning"], [
            ["S₀", "Current stock price"], ["K", "Strike price"], ["r", "Risk-free rate"], ["t", "Time to expiry"],
        ]),
    },
    "math-ug4-l63": {
        "data_table": table(["Public-Key System", "Mathematical Basis"], [
            ["RSA", "Integer factorization"], ["Diffie-Hellman", "Discrete logarithm"],
            ["ECC", "Elliptic curve discrete logarithm"],
        ]),
    },
}

LEVELS: dict[str, dict[str, dict]] = {
    "grade1": GRADE1,
    "grade2": GRADE2,
    "grade3": GRADE3,
    "grade4": GRADE4,
    "grade6": GRADE6,
    "grade7": GRADE7,
    "grade8": GRADE8,
    "grade9": GRADE9,
    "grade10": GRADE10,
    "level_c1": LEVEL_C1,
    "level_c2": LEVEL_C2,
    "level_m1": LEVEL_M1,
    "level_m2": LEVEL_M2,
    "level_ug1": LEVEL_UG1,
    "level_ug2": LEVEL_UG2,
    "level_ug3": LEVEL_UG3,
    "level_ug4": LEVEL_UG4,
}


def main() -> None:
    total_updated = 0
    total_lessons = 0
    for filename, charts in LEVELS.items():
        path = SYLLABUS_DIR / f"{filename}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        lessons = data["subjects"]["Math"]["lessons"]
        by_id = {l["id"]: l for l in lessons}

        missing = [lid for lid in charts if lid not in by_id]
        if missing:
            raise SystemExit(f"Lesson ids not found in {filename}.json Math: {missing}")

        updated = 0
        for lid, fields in charts.items():
            lesson = by_id[lid]
            for key, value in fields.items():
                if key not in lesson:
                    lesson[key] = value
                    updated += 1

        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        total_updated += updated
        total_lessons += len(charts)
        print(f"{filename}: added {updated} fields across {len(charts)} Math lessons.")

    print(f"\nTotal: {total_updated} chart/table/formula fields across {total_lessons} Math lessons in {len(LEVELS)} levels.")


if __name__ == "__main__":
    main()
