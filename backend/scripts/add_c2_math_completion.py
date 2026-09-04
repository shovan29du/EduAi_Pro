#!/usr/bin/env python3
"""Depth pass, C2 Math: fill in real, hand-checked data_table/formulae
content for the 65 C2 Math lessons not covered by the earlier
breadth-first batch. Brings C2 Math to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-c2-l1": {
        "data_table": table(["Concept", "Formula"], [
            ["Derivative", "f'(x) = lim(h->0) [f(x+h) - f(x)] / h"],
        ]),
        "formulae": ["f'(x) = lim(h -> 0) (f(x+h) - f(x)) / h"],
    },
    "math-c2-l2": {
        "data_table": table(["Concept", "Formula"], [
            ["Mean", "sum(x) / n"], ["Standard deviation", "sqrt(sum((x - mean)^2) / n)"],
        ]),
    },
    "math-c2-l3": {
        "data_table": table(["Transformation", "Effect"], [
            ["f(x) + k", "Shifts the graph vertically by k"], ["f(x - h)", "Shifts the graph horizontally by h"],
        ]),
    },
    "math-c2-l4": {
        "data_table": table(["Term", "Meaning"], [
            ["Piecewise function", "A function defined by different rules on different intervals"], ["Inverse function", "Reverses the input-output mapping of the original function"],
        ]),
    },
    "math-c2-l5": {
        "data_table": table(["Sequence Type", "Formula"], [
            ["Arithmetic", "a_n = a_1 + (n-1)d"], ["Geometric", "a_n = a_1 * r^(n-1)"],
        ]),
        "formulae": ["a_n = a_1 + (n - 1) * d", "a_n = a_1 * r ** (n - 1)"],
    },
    "math-c2-l6": {
        "data_table": table(["Test", "Use"], [
            ["Ratio test", "Determines convergence by examining the ratio of consecutive terms"],
        ]),
    },
    "math-c2-l7": {
        "data_table": table(["Type", "Meaning"], [
            ["Horizontal asymptote", "The value a function approaches as x approaches infinity"],
        ]),
    },
    "math-c2-l9": {
        "data_table": table(["Rule", "Formula"], [
            ["Chain rule", "d/dx[f(g(x))] = f'(g(x)) * g'(x)"],
        ]),
        "formulae": ["d/dx[f(g(x))] = f'(g(x)) * g'(x)"],
    },
    "math-c2-l10": {
        "data_table": table(["Step", "Purpose"], [
            ["Setting derivative to zero", "Finds critical points where a maximum or minimum may occur"],
        ]),
        "formulae": ["f'(x) = 0"],
    },
    "math-c2-l11": {
        "data_table": table(["Term", "Meaning"], [
            ["Integral", "The accumulated area under a curve over an interval"],
        ]),
        "formulae": ["Integral of f(x) dx from a to b"],
    },
    "math-c2-l13": {
        "data_table": table(["Rule", "Formula"], [
            ["Power rule for integration", "Integral of x^n dx = x^(n+1)/(n+1) + C"],
        ]),
        "formulae": ["Integral(x**n, dx) = x**(n+1)/(n+1) + C"],
    },
    "math-c2-l14": {
        "data_table": table(["Distribution", "Use"], [
            ["Binomial distribution", "Models the number of successes in fixed independent trials"],
        ]),
    },
    "math-c2-l15": {
        "data_table": table(["Concept", "Formula"], [
            ["Permutations", "nPr = n! / (n-r)!"], ["Combinations", "nCr = n! / (r!(n-r)!)"],
        ]),
        "formulae": ["nPr = factorial(n) / factorial(n - r)", "nCr = factorial(n) / (factorial(r) * factorial(n - r))"],
    },
    "math-c2-l16": {
        "data_table": table(["Term", "Meaning"], [
            ["Direct proof", "Establishes a statement true by a straightforward logical chain from premises"],
        ]),
    },
    "math-c2-l17": {
        "data_table": table(["Term", "Meaning"], [
            ["Graph", "A structure made of vertices connected by edges"],
        ]),
    },
    "math-c2-l18": {
        "data_table": table(["Operation", "Rule"], [
            ["Matrix addition", "Add corresponding entries of same-size matrices"], ["Matrix multiplication", "Row-by-column dot products"],
        ]),
    },
    "math-c2-l20": {
        "data_table": table(["Model", "Formula"], [
            ["Linear model", "y = mx + b"],
        ]),
        "formulae": ["y = m * x + b"],
    },
    "math-c2-l21": {
        "data_table": table(["Method", "Use"], [
            ["Gaussian elimination", "Solves systems of linear equations using row operations"],
        ]),
    },
    "math-c2-l22": {
        "data_table": table(["Term", "Meaning"], [
            ["Eigenvalue", "A scalar λ such that Av = λv for eigenvector v"],
        ]),
        "formulae": ["A * v = lambda * v"],
    },
    "math-c2-l23": {
        "data_table": table(["Term", "Meaning"], [
            ["Vector space", "A set of vectors closed under addition and scalar multiplication"],
        ]),
    },
    "math-c2-l24": {
        "data_table": table(["Term", "Meaning"], [
            ["Linear transformation", "A function between vector spaces preserving addition and scalar multiplication"],
        ]),
    },
    "math-c2-l25": {
        "data_table": table(["Term", "Example"], [
            ["Parametric curve", "x(t) = cos(t), y(t) = sin(t) traces a circle"],
        ]),
    },
    "math-c2-l26": {
        "data_table": table(["Coordinate", "Relation"], [
            ["Polar to Cartesian", "x = r cos(θ), y = r sin(θ)"],
        ]),
        "formulae": ["x = r * cos(theta)", "y = r * sin(theta)"],
    },
    "math-c2-l27": {
        "data_table": table(["Conic", "Equation Form"], [
            ["Ellipse", "x²/a² + y²/b² = 1"], ["Hyperbola", "x²/a² - y²/b² = 1"],
        ]),
    },
    "math-c2-l28": {
        "data_table": table(["Identity", "Formula"], [
            ["Double angle", "sin(2θ) = 2 sin(θ)cos(θ)"],
        ]),
        "formulae": ["sin(2*theta) = 2 * sin(theta) * cos(theta)"],
    },
    "math-c2-l29": {
        "data_table": table(["Technique", "Meaning"], [
            ["Proof by contradiction", "Assumes the opposite of the claim and derives a logical impossibility"],
        ]),
    },
    "math-c2-l30": {
        "data_table": table(["Term", "Meaning"], [
            ["Strong induction", "Assumes the statement holds for all values up to k to prove k+1"],
        ]),
    },
    "math-c2-l32": {
        "data_table": table(["Term", "Meaning"], [
            ["Congruence", "a ≡ b (mod n) means a and b have the same remainder when divided by n"],
        ]),
        "formulae": ["a % n == b % n"],
    },
    "math-c2-l33": {
        "data_table": table(["Term", "Formal Definition"], [
            ["Limit", "For every ε>0 there exists δ>0 such that |x-a|<δ implies |f(x)-L|<ε"],
        ]),
    },
    "math-c2-l34": {
        "data_table": table(["Test", "Use"], [
            ["Integral test", "Compares a series to an improper integral to test convergence"],
        ]),
    },
    "math-c2-l35": {
        "data_table": table(["Term", "Formula"], [
            ["Taylor series", "f(x) = sum f^(n)(a)/n! * (x-a)^n"],
        ]),
        "formulae": ["f(x) = sum(f_n_derivative(a) / factorial(n) * (x - a)**n for n in range(N))"],
    },
    "math-c2-l36": {
        "data_table": table(["Term", "Meaning"], [
            ["Partial derivative", "The derivative of a multivariable function with respect to one variable, holding others constant"],
        ]),
        "formulae": ["∂f/∂x holds y constant"],
    },
    "math-c2-l37": {
        "data_table": table(["Integral Type", "Use"], [
            ["Double integral", "Computes volume under a surface over a 2D region"],
        ]),
    },
    "math-c2-l38": {
        "data_table": table(["Term", "Meaning"], [
            ["Differential equation", "An equation relating a function to its derivatives"],
        ]),
    },
    "math-c2-l39": {
        "data_table": table(["Method", "Example"], [
            ["Separation of variables", "dy/dx = ky separates to dy/y = k dx"],
        ]),
        "formulae": ["dy/y = k * dx"],
    },
    "math-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["Markov chain", "A stochastic process where the next state depends only on the current state"],
        ]),
    },
    "math-c2-l41": {
        "data_table": table(["Term", "Meaning"], [
            ["Skewness", "Measures asymmetry of a distribution"], ["Kurtosis", "Measures the 'tailedness' of a distribution"],
        ]),
    },
    "math-c2-l43": {
        "data_table": table(["Term", "Statement"], [
            ["Central Limit Theorem", "Sample means approach a normal distribution as sample size grows"],
        ]),
    },
    "math-c2-l44": {
        "data_table": table(["Term", "Formula"], [
            ["Confidence interval", "x̄ ± z * (σ/√n)"],
        ]),
        "formulae": ["CI = x_bar +/- z * (sigma / sqrt(n))"],
    },
    "math-c2-l45": {
        "data_table": table(["Term", "Meaning"], [
            ["Null hypothesis", "The default assumption of no effect or difference"], ["p-value", "The probability of observing the data if the null hypothesis is true"],
        ]),
    },
    "math-c2-l46": {
        "data_table": table(["Test", "Use"], [
            ["Chi-square test", "Tests independence or goodness of fit for categorical data"],
        ]),
    },
    "math-c2-l47": {
        "data_table": table(["Term", "Formula"], [
            ["Linear regression", "y = b0 + b1*x"],
        ]),
        "formulae": ["y = b0 + b1 * x"],
    },
    "math-c2-l48": {
        "data_table": table(["Term", "Formula"], [
            ["Permutations with repetition", "n^r for r selections from n items with repetition allowed"],
        ]),
        "formulae": ["n ** r"],
    },
    "math-c2-l49": {
        "data_table": table(["Term", "Formula"], [
            ["Expected value", "E[X] = sum(x * P(x))"],
        ]),
        "formulae": ["E_X = sum(x * P_x for x, P_x in distribution)"],
    },
    "math-c2-l50": {
        "data_table": table(["Term", "Formula"], [
            ["Annuity present value", "PV = PMT * [1 - (1+r)^-n] / r"],
        ]),
        "formulae": ["PV = PMT * (1 - (1 + r) ** -n) / r"],
    },
    "math-c2-l51": {
        "data_table": table(["Term", "Meaning"], [
            ["Simplex method", "An algorithm for solving linear programming optimization problems"],
        ]),
    },
    "math-c2-l52": {
        "data_table": table(["Term", "Meaning"], [
            ["Spanning tree", "A subgraph connecting all vertices with no cycles"],
        ]),
    },
    "math-c2-l53": {
        "data_table": table(["Algorithm", "Use"], [
            ["Dijkstra's algorithm", "Finds the shortest path between nodes in a weighted graph"],
        ]),
    },
    "math-c2-l54": {
        "data_table": table(["Boolean Operation", "Set Theory Equivalent"], [
            ["AND", "Intersection"], ["OR", "Union"],
        ]),
    },
    "math-c2-l55": {
        "data_table": table(["Symbol", "Meaning"], [
            ["∀", "For all"], ["∃", "There exists"],
        ]),
    },
    "math-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Complex plane", "A 2D plane representing complex numbers as points"],
        ]),
    },
    "math-c2-l57": {
        "data_table": table(["Method", "Use"], [
            ["Lagrange multipliers", "Finds extrema of a function subject to constraints"],
        ]),
        "formulae": ["grad(f) = lambda * grad(g)"],
    },
    "math-c2-l58": {
        "data_table": table(["Method", "Formula"], [
            ["Newton's method", "x_(n+1) = x_n - f(x_n)/f'(x_n)"],
        ]),
        "formulae": ["x_next = x - f(x) / f_prime(x)"],
    },
    "math-c2-l59": {
        "data_table": table(["Application", "Example"], [
            ["Population growth model", "dP/dt = kP models exponential growth"],
        ]),
        "formulae": ["dP/dt = k * P"],
    },
    "math-c2-l60": {
        "data_table": table(["Term", "Meaning"], [
            ["Countable set", "A set whose elements can be put into one-to-one correspondence with the natural numbers"],
        ]),
    },
    "math-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Computing eigenvalues", "Solving det(A - λI) = 0 for a 2x2 matrix"],
        ]),
        "formulae": ["det(A - lambda * I) = 0"],
    },
    "math-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Checking closure", "Verifying a subset satisfies vector space axioms"],
        ]),
    },
    "math-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Representing a transformation", "Writing a rotation as a matrix"],
        ]),
    },
    "math-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Applying a convergence test", "Determining whether a given series converges"],
        ]),
    },
    "math-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Classifying an equation", "Identifying the order and linearity of a differential equation"],
        ]),
    },
    "math-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Running a hypothesis test", "Comparing a sample mean against a claimed population mean"],
        ]),
    },
    "math-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Translating a statement", "Converting an English claim into predicate logic notation"],
        ]),
    },
    "math-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Comparing cardinalities", "Showing the rationals are countable but the reals are not"],
        ]),
    },
    "math-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Modeling with a distribution", "Choosing a discrete distribution for a counting scenario"],
        ]),
    },
    "math-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Applying the fundamental theorem", "Connecting differentiation and integration in a worked problem"],
        ]),
        "formulae": ["Integral(f'(x), dx, a, b) = f(b) - f(a)"],
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 Math lessons (completing 70/70).")


if __name__ == "__main__":
    main()
