#!/usr/bin/env python3
"""Depth pass, Grade 10 Math: fill in real, hand-checked data_table
content for the Grade 10 Math lessons not covered by the earlier
breadth-first batch. Brings Grade 10 Math to full 50/50 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_grade10_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "grade10.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-g10-l3": {
        "data_table": table(["Term", "Meaning"], [
            ["Regression line", "Best-fit line through a scatter of data"], ["Correlation coefficient", "Measures strength of a linear relationship, -1 to 1"],
        ]),
    },
    "math-g10-l4": {
        "data_table": table(["Proof Type", "Approach"], [
            ["Direct proof", "Shows the conclusion follows logically from premises"], ["Proof by contradiction", "Assumes the opposite and derives a contradiction"],
        ]),
    },
    "math-g10-l5": {
        "data_table": table(["Term", "Meaning"], [
            ["Function", "A relation where each input has exactly one output"], ["Domain", "The set of valid inputs"],
        ]),
    },
    "math-g10-l6": {
        "data_table": table(["Method", "Use"], [
            ["Factoring", "Solving quadratics by splitting into factors"],
        ]),
        "formulae": ["x = (-b +/- sqrt(b^2 - 4ac)) / 2a"],
    },
    "math-g10-l7": {
        "data_table": table(["Term", "Meaning"], [
            ["Degree", "The highest power of the variable in a polynomial"],
        ]),
    },
    "math-g10-l8": {
        "data_table": table(["Theorem", "Statement"], [
            ["Remainder theorem", "The remainder of P(x) divided by (x-a) equals P(a)"],
        ]),
    },
    "math-g10-l9": {
        "data_table": table(["Term", "Meaning"], [
            ["Asymptote", "A line a graph approaches but never touches"],
        ]),
    },
    "math-g10-l10": {
        "data_table": table(["Function", "Form"], [
            ["Exponential growth", "y = a(1+r)^t"],
        ]),
        "formulae": ["y = a(1+r)^t"],
    },
    "math-g10-l12": {
        "data_table": table(["Law", "Statement"], [
            ["Product rule", "log(xy) = log(x) + log(y)"], ["Power rule", "log(x^n) = n*log(x)"],
        ]),
        "formulae": ["log(xy) = log(x) + log(y)"],
    },
    "math-g10-l13": {
        "data_table": table(["Term", "Meaning"], [
            ["Sequence", "An ordered list of numbers"], ["Series", "The sum of a sequence's terms"],
        ]),
    },
    "math-g10-l14": {
        "data_table": table(["Formula", "Purpose"], [
            ["nth term: a + (n-1)d", "Finds a term in an arithmetic sequence"],
        ]),
        "formulae": ["a_n = a_1 + (n-1)d"],
    },
    "math-g10-l15": {
        "data_table": table(["Formula", "Purpose"], [
            ["nth term: a*r^(n-1)", "Finds a term in a geometric sequence"],
        ]),
        "formulae": ["a_n = a_1 * r^(n-1)"],
    },
    "math-g10-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Binomial theorem", "Expands (a+b)^n without full multiplication"],
        ]),
        "formulae": ["(a+b)^n = sum_{k=0}^{n} C(n,k) a^(n-k) b^k"],
    },
    "math-g10-l18": {
        "data_table": table(["Function", "Period"], [
            ["sin(x)", "2*pi"], ["cos(x)", "2*pi"], ["tan(x)", "pi"],
        ]),
    },
    "math-g10-l19": {
        "data_table": table(["Identity", "Statement"], [
            ["Pythagorean identity", "sin^2(x) + cos^2(x) = 1"],
        ]),
        "formulae": ["sin^2(x) + cos^2(x) = 1"],
    },
    "math-g10-l20": {
        "data_table": table(["Step", "Purpose"], [
            ["Isolate the trig function", "Simplifies solving for the angle"],
        ]),
    },
    "math-g10-l21": {
        "data_table": table(["Rule", "Formula"], [
            ["Sine rule", "a/sin(A) = b/sin(B) = c/sin(C)"], ["Cosine rule", "c^2 = a^2 + b^2 - 2ab*cos(C)"],
        ]),
        "formulae": ["a/sin(A) = b/sin(B) = c/sin(C)"],
    },
    "math-g10-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Vector", "A quantity with both magnitude and direction"],
        ]),
    },
    "math-g10-l23": {
        "data_table": table(["Notation", "Example"], [
            ["3D vector", "(x, y, z)"],
        ]),
    },
    "math-g10-l25": {
        "data_table": table(["Term", "Meaning"], [
            ["Determinant", "A scalar value computed from a square matrix"],
        ]),
        "formulae": ["det([[a,b],[c,d]]) = ad - bc"],
    },
    "math-g10-l26": {
        "data_table": table(["Method", "Use"], [
            ["Substitution", "Solves a system by expressing one variable in terms of another"], ["Elimination", "Solves a system by adding/subtracting equations"],
        ]),
    },
    "math-g10-l27": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear programming", "Optimizing a linear objective subject to linear constraints"],
        ]),
    },
    "math-g10-l29": {
        "data_table": table(["Term", "Meaning"], [
            ["Complex plane", "A plane where the x-axis is real and y-axis is imaginary"],
        ]),
    },
    "math-g10-l30": {
        "data_table": table(["Shape", "Equation Form"], [
            ["Circle", "x^2 + y^2 = r^2"], ["Ellipse", "x^2/a^2 + y^2/b^2 = 1"],
        ]),
        "formulae": ["x^2 + y^2 = r^2"],
    },
    "math-g10-l31": {
        "data_table": table(["Shape", "Equation Form"], [
            ["Parabola", "y = ax^2 + bx + c"], ["Hyperbola", "x^2/a^2 - y^2/b^2 = 1"],
        ]),
    },
    "math-g10-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Probability", "The likelihood of an event, from 0 to 1"],
        ]),
    },
    "math-g10-l33": {
        "data_table": table(["Term", "Formula"], [
            ["Conditional probability", "P(A|B) = P(A and B) / P(B)"],
        ]),
        "formulae": ["P(A|B) = P(A and B) / P(B)"],
    },
    "math-g10-l34": {
        "data_table": table(["Concept", "Formula"], [
            ["Permutation", "nPr = n!/(n-r)!"], ["Combination", "nCr = n!/(r!(n-r)!)"],
        ]),
        "formulae": ["nCr = n! / (r!(n-r)!)"],
    },
    "math-g10-l35": {
        "data_table": table(["Fact", "Detail"], [
            ["Normal distribution", "Symmetric bell-shaped curve defined by mean and standard deviation"],
        ]),
    },
    "math-g10-l36": {
        "data_table": table(["Fact", "Detail"], [
            ["Binomial distribution", "Models the number of successes in fixed independent trials"],
        ]),
    },
    "math-g10-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["Null hypothesis", "The default assumption being tested"], ["p-value", "Probability of the observed result under the null hypothesis"],
        ]),
    },
    "math-g10-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Limit", "The value a function approaches as the input approaches a point"],
        ]),
    },
    "math-g10-l39": {
        "data_table": table(["Concept", "Meaning"], [
            ["Rate of change", "How quickly a quantity changes, given by the derivative"],
        ]),
    },
    "math-g10-l40": {
        "data_table": table(["Step", "Purpose"], [
            ["Set derivative to zero", "Finds critical points for optimization"],
        ]),
    },
    "math-g10-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Related rates", "Finding how one rate of change relates to another via a shared equation"],
        ]),
    },
    "math-g10-l42": {
        "data_table": table(["Concept", "Method"], [
            ["Area under a curve", "Found using definite integration"],
        ]),
        "formulae": ["Area = integral from a to b of f(x) dx"],
    },
    "math-g10-l43": {
        "data_table": table(["Method", "Use"], [
            ["Disk method", "Finds volume of a solid of revolution"],
        ]),
    },
    "math-g10-l44": {
        "data_table": table(["Term", "Meaning"], [
            ["Parametric equations", "Express x and y as functions of a third variable, t"],
        ]),
    },
    "math-g10-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Polar coordinates", "Locate points using distance and angle from the origin"],
        ]),
    },
    "math-g10-l46": {
        "data_table": table(["Symbol", "Meaning"], [
            ["Union (A u B)", "Elements in A or B"], ["Intersection (A n B)", "Elements in both A and B"],
        ]),
    },
    "math-g10-l47": {
        "data_table": table(["Step", "Purpose"], [
            ["Base case", "Proves the statement for the starting value"], ["Inductive step", "Proves it holds for n+1 given it holds for n"],
        ]),
    },
    "math-g10-l48": {
        "data_table": table(["Term", "Meaning"], [
            ["Prime number", "A number greater than 1 with only two factors: 1 and itself"],
        ]),
    },
    "math-g10-l49": {
        "data_table": table(["Formula", "Use"], [
            ["A = P(1+r/n)^(nt)", "Compound interest"],
        ]),
        "formulae": ["A = P(1 + r/n)^(n*t)"],
    },
    "math-g10-l50": {
        "data_table": table(["Term", "Meaning"], [
            ["Graph (in graph theory)", "A structure of vertices connected by edges"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in grade10.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} Grade 10 Math lessons (completing 50/50).")


if __name__ == "__main__":
    main()
