#!/usr/bin/env python3
"""Depth pass, M1 Math: fill in real, hand-checked data_table content
for the 96 M1 Math lessons not covered by the earlier breadth-first
batch. Brings M1 Math to full 120/120 coverage.

Structure: l1-l100 are unique graduate-level topics; l101-l120 are
"Worked Analysis" companions reusing the data_table of l1-l20 (direct
1:1 mapping). l3, l9, l28, and l90 were already completed by an
earlier breadth-first batch; l3 and l9 fall within l1-l20 so their
tables are reused for l103 and l109.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "math-m1-l1": {
        "data_table": table(["Concept", "Detail"], [
            ["Graduate probability", "Builds measure-theoretic foundations for rigorous statistical inference"],
        ]),
    },
    "math-m1-l2": {
        "data_table": table(["Concept", "Detail"], [
            ["Proof technique", "Induction, contradiction, and direct proof underlie rigorous discrete mathematics"],
        ]),
    },
    "math-m1-l4": {
        "data_table": table(["Concept", "Detail"], [
            ["Galois group", "Encodes the symmetries of a field extension's roots"],
        ]),
    },
    "math-m1-l5": {
        "data_table": table(["Space", "Feature"], [
            ["Banach space", "Complete normed vector space"],
            ["Hilbert space", "Complete inner product space, a special case of Banach space"],
        ]),
    },
    "math-m1-l6": {
        "data_table": table(["Property", "Meaning"], [
            ["Compactness", "Every open cover has a finite subcover"],
            ["Connectedness", "The space cannot be split into two disjoint nonempty open sets"],
        ]),
    },
    "math-m1-l7": {
        "data_table": table(["Concept", "Detail"], [
            ["Martingale", "A stochastic process whose expected future value equals its present value"],
        ]),
    },
    "math-m1-l8": {
        "data_table": table(["Concept", "Formula"], [
            ["Maximum likelihood estimate", "Parameter value maximizing the likelihood of observed data"],
        ]),
        "formulae": ["theta_hat = argmax(likelihood(theta, data))"],
    },
    "math-m1-l10": {
        "data_table": table(["Concept", "Detail"], [
            ["Spectral graph theory", "Studies graph properties via eigenvalues of associated matrices"],
        ]),
    },
    "math-m1-l11": {
        "data_table": table(["Concept", "Detail"], [
            ["Extremal combinatorics", "Determines the largest/smallest structure avoiding a given property"],
        ]),
    },
    "math-m1-l12": {
        "data_table": table(["Concept", "Detail"], [
            ["Differential geometry", "Studies curves, surfaces, and manifolds using calculus"],
        ]),
    },
    "math-m1-l13": {
        "data_table": table(["Concept", "Detail"], [
            ["Stability analysis", "Determines whether solutions near an equilibrium remain close over time"],
        ]),
    },
    "math-m1-l14": {
        "data_table": table(["Method", "Use"], [
            ["Gradient descent", "Iteratively moves toward a minimum by following the negative gradient"],
        ]),
    },
    "math-m1-l15": {
        "data_table": table(["Concept", "Detail"], [
            ["Category theory", "Studies mathematical structures via objects and structure-preserving morphisms"],
        ]),
    },
    "math-m1-l16": {
        "data_table": table(["Concept", "Detail"], [
            ["Model theory", "Studies mathematical structures using formal logical languages"],
        ]),
    },
    "math-m1-l17": {
        "data_table": table(["Concept", "Detail"], [
            ["Riemann surface", "A one-dimensional complex manifold enabling multi-valued function analysis"],
        ]),
    },
    "math-m1-l18": {
        "data_table": table(["Concept", "Detail"], [
            ["Chaos theory", "Studies deterministic systems highly sensitive to initial conditions"],
        ]),
    },
    "math-m1-l19": {
        "data_table": table(["Concept", "Detail"], [
            ["Measure-theoretic probability", "Grounds probability theory rigorously in measure theory"],
        ]),
    },
    "math-m1-l20": {
        "data_table": table(["Task", "Focus"], [
            ["Capstone investigation", "Applies advanced mathematical tools to an original research question"],
        ]),
    },
    "math-m1-l21": {
        "data_table": table(["Concept", "Detail"], [
            ["Sheaf", "Assigns local data to open sets, enabling gluing of local information"],
        ]),
    },
    "math-m1-l22": {
        "data_table": table(["Concept", "Detail"], [
            ["Étale cohomology", "A cohomology theory suited to algebraic varieties over general fields"],
        ]),
    },
    "math-m1-l23": {
        "data_table": table(["Concept", "Detail"], [
            ["Derived functor", "Extends a functor to measure failure of exactness"],
        ]),
    },
    "math-m1-l24": {
        "data_table": table(["Concept", "Detail"], [
            ["Lie algebra", "Captures infinitesimal structure of a Lie group via a bracket operation"],
        ]),
    },
    "math-m1-l25": {
        "data_table": table(["Concept", "Detail"], [
            ["Scheme", "A generalization of algebraic varieties built by gluing affine pieces"],
        ]),
    },
    "math-m1-l26": {
        "data_table": table(["Operation", "Purpose"], [
            ["Localization", "Formally inverts elements to study a ring near a prime"],
        ]),
    },
    "math-m1-l27": {
        "data_table": table(["Concept", "Detail"], [
            ["Class field theory", "Describes abelian extensions of number fields via arithmetic data"],
        ]),
    },
    "math-m1-l29": {
        "data_table": table(["Concept", "Detail"], [
            ["Modularity", "Elliptic curves correspond to modular forms (proven in the modularity theorem)"],
        ]),
    },
    "math-m1-l30": {
        "data_table": table(["Concept", "Detail"], [
            ["Diophantine equation", "A polynomial equation for which only integer or rational solutions are sought"],
        ]),
    },
    "math-m1-l31": {
        "data_table": table(["Concept", "Detail"], [
            ["Ergodic theorem", "Time averages equal space averages for an ergodic dynamical system"],
        ]),
    },
    "math-m1-l32": {
        "data_table": table(["Concept", "Detail"], [
            ["Topological entropy", "Measures the complexity of orbits in a dynamical system"],
        ]),
    },
    "math-m1-l33": {
        "data_table": table(["Concept", "Detail"], [
            ["Hyperbolic dynamics", "Nearby trajectories diverge exponentially along unstable directions"],
        ]),
    },
    "math-m1-l34": {
        "data_table": table(["Concept", "Detail"], [
            ["Bifurcation", "A small parameter change qualitatively alters a system's long-term behavior"],
        ]),
    },
    "math-m1-l35": {
        "data_table": table(["Concept", "Detail"], [
            ["Sobolev space", "A function space combining integrability with weak derivative control"],
        ]),
    },
    "math-m1-l36": {
        "data_table": table(["Equation Type", "Feature"], [
            ["Elliptic PDE", "No real characteristic curves; models steady-state phenomena"],
        ]),
    },
    "math-m1-l37": {
        "data_table": table(["Concept", "Detail"], [
            ["Conservation law", "A PDE expressing that a quantity's rate of change equals a flux divergence"],
        ]),
        "formulae": ["du/dt + div(f(u)) = 0"],
    },
    "math-m1-l38": {
        "data_table": table(["Method", "Use"], [
            ["Variational method", "Finds PDE solutions by minimizing an associated energy functional"],
        ]),
    },
    "math-m1-l39": {
        "data_table": table(["Concept", "Detail"], [
            ["Spectral theory", "Studies eigenvalues and eigenfunctions of differential operators"],
        ]),
    },
    "math-m1-l40": {
        "data_table": table(["Concept", "Detail"], [
            ["Curvature", "Measures how a Riemannian manifold deviates from flat Euclidean space"],
        ]),
    },
    "math-m1-l41": {
        "data_table": table(["Concept", "Detail"], [
            ["Symplectic form", "A closed, nondegenerate 2-form underlying Hamiltonian mechanics"],
        ]),
    },
    "math-m1-l42": {
        "data_table": table(["Concept", "Detail"], [
            ["Characteristic class", "An invariant measuring the twisting of a fiber bundle"],
        ]),
    },
    "math-m1-l43": {
        "data_table": table(["Concept", "Detail"], [
            ["Spectral sequence", "A computational tool converging to homology via successive approximations"],
        ]),
    },
    "math-m1-l44": {
        "data_table": table(["Concept", "Detail"], [
            ["Knot invariant", "A property of a knot unchanged under continuous deformation"],
        ]),
    },
    "math-m1-l45": {
        "data_table": table(["Concept", "Detail"], [
            ["Morse function", "A smooth function whose critical points reveal a manifold's topology"],
        ]),
    },
    "math-m1-l46": {
        "data_table": table(["Term", "Meaning"], [
            ["Categoricity", "A theory has exactly one model (up to isomorphism) of a given cardinality"],
        ]),
    },
    "math-m1-l47": {
        "data_table": table(["Concept", "Detail"], [
            ["Forcing", "A technique for constructing models to prove statements are independent of set theory's axioms"],
        ]),
    },
    "math-m1-l48": {
        "data_table": table(["Concept", "Detail"], [
            ["Computability", "Studies which functions can be computed by an algorithm or Turing machine"],
        ]),
    },
    "math-m1-l49": {
        "data_table": table(["Concept", "Detail"], [
            ["Ordinal analysis", "Measures a formal theory's proof-theoretic strength via ordinal notation"],
        ]),
    },
    "math-m1-l50": {
        "data_table": table(["Concept", "Detail"], [
            ["Adjoint functor", "A pair of functors satisfying a natural universal correspondence"],
        ]),
    },
    "math-m1-l51": {
        "data_table": table(["Concept", "Detail"], [
            ["Topos", "A category behaving like the category of sets, with its own internal logic"],
        ]),
    },
    "math-m1-l52": {
        "data_table": table(["Concept", "Detail"], [
            ["Combinatorial design", "An arrangement of elements satisfying balance conditions, e.g. a Latin square"],
        ]),
    },
    "math-m1-l53": {
        "data_table": table(["Concept", "Detail"], [
            ["Ramsey theory", "Guarantees ordered substructure must appear once a system is large enough"],
        ]),
    },
    "math-m1-l54": {
        "data_table": table(["Method", "Use"], [
            ["Probabilistic method", "Proves existence of a combinatorial structure by showing positive probability"],
        ]),
    },
    "math-m1-l55": {
        "data_table": table(["Concept", "Detail"], [
            ["Matroid", "An abstraction of linear independence generalizing vector spaces and graphs"],
        ]),
    },
    "math-m1-l56": {
        "data_table": table(["Concept", "Detail"], [
            ["Random graph", "A graph generated by a probabilistic process, e.g. the Erdős-Rényi model"],
        ]),
    },
    "math-m1-l57": {
        "data_table": table(["Concept", "Detail"], [
            ["Symmetric function", "A polynomial invariant under permutation of its variables"],
        ]),
    },
    "math-m1-l58": {
        "data_table": table(["Concept", "Detail"], [
            ["Polytope", "The convex hull of a finite point set in Euclidean space"],
        ]),
    },
    "math-m1-l59": {
        "data_table": table(["Concept", "Detail"], [
            ["Convex duality", "Relates an optimization problem to a corresponding dual problem"],
        ]),
    },
    "math-m1-l60": {
        "data_table": table(["Condition", "Purpose"], [
            ["KKT conditions", "Necessary conditions for optimality in constrained nonlinear optimization"],
        ]),
    },
    "math-m1-l61": {
        "data_table": table(["Concept", "Detail"], [
            ["Semidefinite relaxation", "Relaxes a hard combinatorial problem into a tractable convex one"],
        ]),
    },
    "math-m1-l62": {
        "data_table": table(["Method", "Use"], [
            ["Stochastic gradient descent", "Uses noisy gradient estimates to optimize efficiently at scale"],
        ]),
    },
    "math-m1-l63": {
        "data_table": table(["Theorem", "Statement"], [
            ["Optional stopping theorem", "Under conditions, a martingale's expected value at a stopping time equals its initial value"],
        ]),
    },
    "math-m1-l64": {
        "data_table": table(["Concept", "Detail"], [
            ["Brownian motion", "A continuous-time stochastic process with independent, normally distributed increments"],
        ]),
    },
    "math-m1-l65": {
        "data_table": table(["Concept", "Detail"], [
            ["Stochastic differential equation", "A differential equation driven by a random noise process"],
        ]),
        "formulae": ["dX = mu(X, t) dt + sigma(X, t) dW"],
    },
    "math-m1-l66": {
        "data_table": table(["Concept", "Detail"], [
            ["Large deviations", "Quantifies the exponentially small probability of rare events"],
        ]),
    },
    "math-m1-l67": {
        "data_table": table(["Concept", "Detail"], [
            ["Mixing time", "The time for a Markov chain to approach its stationary distribution"],
        ]),
    },
    "math-m1-l68": {
        "data_table": table(["Concept", "Detail"], [
            ["Point process", "A random collection of points distributed in space or time"],
        ]),
    },
    "math-m1-l69": {
        "data_table": table(["Concept", "Detail"], [
            ["Extreme value theory", "Models the statistical behavior of the maximum or minimum of a sample"],
        ]),
    },
    "math-m1-l70": {
        "data_table": table(["Method", "Feature"], [
            ["Nonparametric inference", "Makes minimal assumptions about the underlying data distribution"],
        ]),
    },
    "math-m1-l71": {
        "data_table": table(["Concept", "Formula"], [
            ["Bayesian updating", "Posterior probability proportional to likelihood times prior"],
        ]),
        "formulae": ["posterior ∝ likelihood * prior"],
    },
    "math-m1-l72": {
        "data_table": table(["Concept", "Detail"], [
            ["High-dimensional statistics", "Addresses inference when the number of variables rivals or exceeds sample size"],
        ]),
    },
    "math-m1-l73": {
        "data_table": table(["Concept", "Detail"], [
            ["VC dimension", "Measures the capacity of a hypothesis class to fit arbitrary labelings"],
        ]),
    },
    "math-m1-l74": {
        "data_table": table(["Model", "Feature"], [
            ["ARIMA", "Combines autoregression, differencing, and moving average terms for time series"],
        ]),
    },
    "math-m1-l75": {
        "data_table": table(["Concept", "Detail"], [
            ["Hazard function", "The instantaneous rate of an event occurring given survival to that point"],
        ]),
    },
    "math-m1-l76": {
        "data_table": table(["Concept", "Detail"], [
            ["Functional data analysis", "Treats entire curves or functions, not scalars, as the unit of observation"],
        ]),
    },
    "math-m1-l77": {
        "data_table": table(["Method", "Use"], [
            ["Finite element method", "Discretizes a domain into elements to numerically solve PDEs"],
        ]),
    },
    "math-m1-l78": {
        "data_table": table(["Concept", "Detail"], [
            ["Stiff ODE", "Requires implicit numerical methods due to rapidly varying solution components"],
        ]),
    },
    "math-m1-l79": {
        "data_table": table(["Method", "Feature"], [
            ["Interior point method", "Traverses the interior of the feasible region toward an optimum"],
        ]),
    },
    "math-m1-l80": {
        "data_table": table(["Concept", "Detail"], [
            ["Gröbner basis", "A generating set for a polynomial ideal enabling algorithmic computation"],
        ]),
    },
    "math-m1-l81": {
        "data_table": table(["Concept", "Detail"], [
            ["Chebyshev polynomial", "Minimizes the maximum approximation error among polynomials of given degree"],
        ]),
    },
    "math-m1-l82": {
        "data_table": table(["Concept", "Detail"], [
            ["Wavelet", "A localized oscillating function used to analyze signals at multiple scales"],
        ]),
    },
    "math-m1-l83": {
        "data_table": table(["Concept", "Detail"], [
            ["Fourier restriction", "Studies how restricting a Fourier transform to a surface affects its behavior"],
        ]),
    },
    "math-m1-l84": {
        "data_table": table(["Concept", "Detail"], [
            ["Bounded operator", "A linear operator on a Hilbert space with finite operator norm"],
        ]),
    },
    "math-m1-l85": {
        "data_table": table(["Concept", "Detail"], [
            ["C*-algebra", "A Banach algebra with an involution satisfying the C* identity"],
        ]),
    },
    "math-m1-l86": {
        "data_table": table(["Concept", "Detail"], [
            ["Distribution (generalized function)", "Extends the notion of function to include objects like the Dirac delta"],
        ]),
    },
    "math-m1-l87": {
        "data_table": table(["Concept", "Detail"], [
            ["Cooperative game solution", "Concepts like the Shapley value allocate payoff among coalition members"],
        ]),
    },
    "math-m1-l88": {
        "data_table": table(["Model", "Feature"], [
            ["SIR model", "Compartmental model tracking Susceptible, Infected, and Recovered populations"],
        ]),
    },
    "math-m1-l89": {
        "data_table": table(["Model", "Feature"], [
            ["Stochastic volatility model", "Treats an asset's volatility itself as a random process"],
        ]),
    },
    "math-m1-l91": {
        "data_table": table(["Concept", "Detail"], [
            ["Elliptic curve cryptography", "Bases security on the difficulty of the elliptic curve discrete logarithm problem"],
        ]),
    },
    "math-m1-l92": {
        "data_table": table(["Concept", "Detail"], [
            ["Tensor", "A multilinear map generalizing scalars, vectors, and matrices"],
        ]),
    },
    "math-m1-l93": {
        "data_table": table(["Concept", "Detail"], [
            ["Differential form", "An object integrated over manifolds, generalizing line and surface integrals"],
        ]),
    },
    "math-m1-l94": {
        "data_table": table(["Logic Type", "Feature"], [
            ["Intuitionistic logic", "Rejects the law of excluded middle, requiring constructive proof"],
            ["Modal logic", "Adds operators for necessity and possibility"],
        ]),
    },
    "math-m1-l95": {
        "data_table": table(["Concept", "Detail"], [
            ["Perfectoid space", "A framework connecting characteristic 0 and characteristic p geometry"],
        ]),
    },
    "math-m1-l96": {
        "data_table": table(["Concept", "Detail"], [
            ["Automorphic form", "A generalization of modular forms central to the Langlands program"],
        ]),
    },
    "math-m1-l97": {
        "data_table": table(["Concept", "Detail"], [
            ["Optimal transport", "Finds the most efficient way to move one distribution of mass to another"],
        ]),
    },
    "math-m1-l98": {
        "data_table": table(["Concept", "Detail"], [
            ["Persistent homology", "Tracks topological features across scales in a dataset"],
        ]),
    },
    "math-m1-l99": {
        "data_table": table(["Concept", "Detail"], [
            ["Free probability", "A noncommutative analogue of probability theory applied to random matrices"],
        ]),
    },
    "math-m1-l100": {
        "data_table": table(["Concept", "Detail"], [
            ["Motivic cohomology", "A cohomology theory unifying invariants across algebraic geometry"],
        ]),
    },
}

# l3 and l9 were already completed by an earlier breadth-first batch.
_l3_source = {
    "data_table": table(["Concept", "Riemann Integration", "Lebesgue Integration"], [
        ["Partitions", "Domain (x-axis)", "Range (y-axis)"],
        ["Dirichlet function (1 on rationals, 0 on irrationals)", "Not integrable", "Integrable (= 0)"],
    ]),
}
_l9_source = {
    "data_table": table(["Number Field", "Degree over ℚ"], [
        ["ℚ(√2)", "2"], ["ℚ(i)", "2"], ["ℚ(∛2)", "3"],
    ]),
}

# l101-l120 "Worked Analysis" lessons reuse the data_table/formulae of l1-l20.
for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"math-m1-l{base_n}"
    if base_key in CHARTS:
        fields = {"data_table": CHARTS[base_key]["data_table"]}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = CHARTS[base_key]["formulae"]
        CHARTS[f"math-m1-l{worked_n}"] = fields
    elif base_n == 3:
        CHARTS[f"math-m1-l{worked_n}"] = dict(_l3_source)
    elif base_n == 9:
        CHARTS[f"math-m1-l{worked_n}"] = dict(_l9_source)


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Math lessons (completing 120/120).")


if __name__ == "__main__":
    main()
