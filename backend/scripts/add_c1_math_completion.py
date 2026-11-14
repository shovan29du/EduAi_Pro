#!/usr/bin/env python3
"""Depth pass, C1 Math: fill in real, hand-checked data_table content
for the 65 C1 Math lessons not covered by the earlier breadth-first
batch. Brings C1 Math to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-c1-l1": {
        "data_table": table(["Concept", "Example"], [
            ["Variable", "x, y, z represent unknown quantities"], ["Function", "f(x) = 2x + 3"],
        ]),
        "formulae": ["f(x) = mx + b"],
    },
    "math-c1-l2": {
        "data_table": table(["Concept", "Meaning"], [
            ["Derivative", "Instantaneous rate of change"], ["Integral", "Accumulated area under a curve"],
        ]),
    },
    "math-c1-l3": {
        "data_table": table(["Function Type", "Graph Shape"], [
            ["Linear", "Straight line"], ["Quadratic", "Parabola"], ["Exponential", "J-curve"],
        ]),
    },
    "math-c1-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Polynomial function", "Sum of terms with non-negative integer exponents"], ["Rational function", "Ratio of two polynomials"],
        ]),
    },
    "math-c1-l5": {
        "data_table": table(["Function", "Formula"], [
            ["Exponential growth", "y = a(1+r)^t"], ["Natural log", "ln(x) is log base e"],
        ]),
        "formulae": ["y = a * e^(kt)"],
    },
    "math-c1-l6": {
        "data_table": table(["Ratio", "Definition"], [
            ["sin(theta)", "opposite / hypotenuse"], ["cos(theta)", "adjacent / hypotenuse"], ["tan(theta)", "opposite / adjacent"],
        ]),
    },
    "math-c1-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Sequence", "An ordered list of numbers"], ["Term", "Each individual number in a sequence"],
        ]),
    },
    "math-c1-l8": {
        "data_table": table(["Notation", "Meaning"], [
            ["Sigma (Σ)", "Represents a sum of a sequence of terms"],
        ]),
        "formulae": ["sum_{i=1}^{n} i = n(n+1)/2"],
    },
    "math-c1-l10": {
        "data_table": table(["Condition", "Meaning"], [
            ["Continuous at x=a", "The limit as x approaches a equals f(a)"],
        ]),
    },
    "math-c1-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Derivative", "The instantaneous rate of change of a function"],
        ]),
        "formulae": ["f'(x) = lim_{h->0} [f(x+h) - f(x)] / h"],
    },
    "math-c1-l13": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Union (u)", "Elements in either set"], ["Intersection (n)", "Elements in both sets"],
        ]),
    },
    "math-c1-l14": {
        "data_table": table(["Operator", "Meaning"], [
            ["AND", "True only if both are true"], ["OR", "True if either is true"], ["NOT", "Reverses the value"],
        ]),
    },
    "math-c1-l15": {
        "data_table": table(["Rule", "Formula"], [
            ["Multiplication principle", "If task A has m ways and task B has n ways, both together have m*n ways"],
        ]),
    },
    "math-c1-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Probability", "The likelihood of an event, from 0 to 1"],
        ]),
        "formulae": ["P(A) = favorable outcomes / total outcomes"],
    },
    "math-c1-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Divisibility", "a is divisible by b if a/b leaves no remainder"],
        ]),
    },
    "math-c1-l18": {
        "data_table": table(["Term", "Meaning"], [
            ["Vector", "A quantity with both magnitude and direction"],
        ]),
    },
    "math-c1-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Identify variables", "Determine what quantities to model"], ["Formulate equations", "Express relationships mathematically"],
        ]),
    },
    "math-c1-l21": {
        "data_table": table(["Concept", "Formula"], [
            ["Absolute value", "|x| is the distance of x from 0"],
        ]),
        "formulae": ["|x - a| = b means x = a + b or x = a - b"],
    },
    "math-c1-l22": {
        "data_table": table(["Method", "Use"], [
            ["Substitution", "Solving a system by expressing one variable in terms of another"], ["Elimination", "Solving by adding/subtracting equations"],
        ]),
    },
    "math-c1-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Matrix", "A rectangular array of numbers"],
        ]),
    },
    "math-c1-l24": {
        "data_table": table(["Term", "Formula"], [
            ["2x2 determinant", "ad - bc"],
        ]),
        "formulae": ["det([[a,b],[c,d]]) = ad - bc"],
    },
    "math-c1-l25": {
        "data_table": table(["Notation", "Example"], [
            ["2D vector", "(x, y)"], ["3D vector", "(x, y, z)"],
        ]),
    },
    "math-c1-l26": {
        "data_table": table(["Product", "Result Type"], [
            ["Dot product", "Scalar"], ["Cross product", "Vector"],
        ]),
        "formulae": ["a . b = |a||b|cos(theta)"],
    },
    "math-c1-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Parametric equations", "Express x and y as functions of a third variable, t"],
        ]),
    },
    "math-c1-l28": {
        "data_table": table(["Term", "Meaning"], [
            ["Polar coordinates", "Locate points using distance (r) and angle (theta) from the origin"],
        ]),
    },
    "math-c1-l29": {
        "data_table": table(["Shape", "Equation Form"], [
            ["Circle", "x^2 + y^2 = r^2"], ["Ellipse", "x^2/a^2 + y^2/b^2 = 1"],
        ]),
    },
    "math-c1-l30": {
        "data_table": table(["Shape", "Equation Form"], [
            ["Parabola", "y = ax^2 + bx + c"], ["Hyperbola", "x^2/a^2 - y^2/b^2 = 1"],
        ]),
    },
    "math-c1-l31": {
        "data_table": table(["Term", "Meaning"], [
            ["Inverse function", "Reverses the effect of the original function, f^-1(f(x)) = x"],
        ]),
    },
    "math-c1-l32": {
        "data_table": table(["Angle", "Coordinates on Unit Circle"], [
            ["0", "(1, 0)"], ["90 degrees", "(0, 1)"],
        ]),
    },
    "math-c1-l33": {
        "data_table": table(["Identity", "Statement"], [
            ["Pythagorean identity", "sin^2(x) + cos^2(x) = 1"],
        ]),
        "formulae": ["sin^2(x) + cos^2(x) = 1"],
    },
    "math-c1-l34": {
        "data_table": table(["Rule", "Formula"], [
            ["Law of sines", "a/sin(A) = b/sin(B) = c/sin(C)"], ["Law of cosines", "c^2 = a^2 + b^2 - 2ab*cos(C)"],
        ]),
    },
    "math-c1-l35": {
        "data_table": table(["Step", "Purpose"], [
            ["Base case", "Proves the statement for the starting value"], ["Inductive step", "Proves it holds for n+1 given it holds for n"],
        ]),
    },
    "math-c1-l36": {
        "data_table": table(["Notation", "Meaning"], [
            ["a mod n", "The remainder when a is divided by n"],
        ]),
    },
    "math-c1-l38": {
        "data_table": table(["Type", "Example"], [
            ["Rational number", "Can be written as a fraction, e.g. 1/2"], ["Irrational number", "Cannot be written as a fraction, e.g. pi"],
        ]),
    },
    "math-c1-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["Piecewise function", "A function defined by different expressions over different intervals"],
        ]),
    },
    "math-c1-l40": {
        "data_table": table(["Notation", "Meaning"], [
            ["(f o g)(x)", "f(g(x)), applying g first then f"],
        ]),
    },
    "math-c1-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Domain", "The set of valid input values"], ["Range", "The set of possible output values"],
        ]),
    },
    "math-c1-l42": {
        "data_table": table(["Transformation", "Effect"], [
            ["f(x) + k", "Shifts the graph up by k"], ["f(x - h)", "Shifts the graph right by h"],
        ]),
    },
    "math-c1-l43": {
        "data_table": table(["Mean Type", "Formula"], [
            ["Arithmetic mean", "Sum of values divided by count"], ["Geometric mean", "nth root of the product of n values"],
        ]),
    },
    "math-c1-l44": {
        "data_table": table(["Measure", "Meaning"], [
            ["Mean", "The average of the data"], ["Median", "The middle value"], ["Mode", "The most frequent value"],
        ]),
    },
    "math-c1-l46": {
        "data_table": table(["Distribution Type", "Example"], [
            ["Discrete", "Number of heads in 10 coin flips"], ["Continuous", "Height of students"],
        ]),
    },
    "math-c1-l47": {
        "data_table": table(["Term", "Formula"], [
            ["Binomial probability", "P(X=k) = C(n,k) p^k (1-p)^(n-k)"],
        ]),
        "formulae": ["P(X=k) = C(n,k) * p^k * (1-p)^(n-k)"],
    },
    "math-c1-l48": {
        "data_table": table(["Term", "Formula"], [
            ["Conditional probability", "P(A|B) = P(A and B) / P(B)"],
        ]),
        "formulae": ["P(A|B) = P(A and B) / P(B)"],
    },
    "math-c1-l49": {
        "data_table": table(["Concept", "Formula"], [
            ["Combinations", "nCr = n!/(r!(n-r)!)"],
        ]),
        "formulae": ["nCr = n! / (r!(n-r)!)"],
    },
    "math-c1-l50": {
        "data_table": table(["Formula", "Use"], [
            ["A = P(1+r/n)^(nt)", "Compound interest"],
        ]),
        "formulae": ["A = P(1 + r/n)^(n*t)"],
    },
    "math-c1-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear programming", "Optimizing a linear objective subject to linear constraints"],
        ]),
    },
    "math-c1-l52": {
        "data_table": table(["Symbol", "Meaning"], [
            ["∈", "'is an element of'"], ["∀", "'for all'"], ["∃", "'there exists'"],
        ]),
    },
    "math-c1-l53": {
        "data_table": table(["Phrase", "Operation"], [
            ["'sum of'", "addition"], ["'product of'", "multiplication"], ["'difference of'", "subtraction"],
        ]),
    },
    "math-c1-l54": {
        "data_table": table(["Method", "Use"], [
            ["Factoring", "Solving quadratics by splitting into factors"],
        ]),
    },
    "math-c1-l55": {
        "data_table": table(["Formula", "Use"], [
            ["Quadratic formula", "Solves ax^2 + bx + c = 0"],
        ]),
        "formulae": ["x = (-b +/- sqrt(b^2 - 4ac)) / 2a"],
    },
    "math-c1-l56": {
        "data_table": table(["Notation", "Meaning"], [
            ["f(3)", "Evaluate the function f at x = 3"],
        ]),
    },
    "math-c1-l57": {
        "data_table": table(["Operation", "Symbol"], [
            ["Union", "u"], ["Intersection", "n"], ["Complement", "A'"],
        ]),
    },
    "math-c1-l58": {
        "data_table": table(["Diagram Feature", "Meaning"], [
            ["Overlapping circles", "Elements shared between sets"],
        ]),
    },
    "math-c1-l59": {
        "data_table": table(["Term", "Meaning"], [
            ["Rate", "A ratio comparing two different units, e.g. km/h"], ["Ratio", "A comparison of two quantities of the same unit"],
        ]),
    },
    "math-c1-l60": {
        "data_table": table(["Proof Type", "Approach"], [
            ["Direct proof", "Shows the conclusion follows logically from premises"], ["Proof by contradiction", "Assumes the opposite and derives a contradiction"],
        ]),
    },
    "math-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Linear function modeling", "Predicting cost from quantity: f(x) = 5x + 20"],
        ]),
    },
    "math-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Rate of change analysis", "Finding instantaneous velocity from a position function"],
        ]),
    },
    "math-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Graph reading", "Identifying intercepts and turning points from a graph"],
        ]),
    },
    "math-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Rational function analysis", "Finding vertical and horizontal asymptotes"],
        ]),
    },
    "math-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Exponential decay modeling", "Radioactive decay: N(t) = N0 * e^(-kt)"],
        ]),
    },
    "math-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Periodic modeling", "Modeling seasonal temperature with a sine function"],
        ]),
    },
    "math-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Sequence analysis", "Finding a recursive formula for a savings account balance"],
        ]),
    },
    "math-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Series summation", "Computing total payments across a loan term"],
        ]),
    },
    "math-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Limit evaluation", "Finding the limit of (x^2-1)/(x-1) as x approaches 1"],
        ]),
        "formulae": ["lim_{x->1} (x^2-1)/(x-1) = 2"],
    },
    "math-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Continuity analysis", "Checking whether a piecewise function is continuous at its boundary"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 Math lessons (completing 70/70).")


if __name__ == "__main__":
    main()
