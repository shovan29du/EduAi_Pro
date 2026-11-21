#!/usr/bin/env python3
"""Depth pass, M2 Math: fill in real, hand-checked data_table content
for the M2 Math lessons not covered by the earlier breadth-first
batch. Brings M2 Math to full 120/120 coverage.

Structure: l1-l100 are unique doctoral-level pure and applied
mathematics research topics; l101-l120 are "Worked Analysis"
companions reusing the data_table of l1-l20 (direct 1:1 mapping).
l15, l34, l60, and l71 were already completed by an earlier
breadth-first batch; l15 falls within l1-l20 so its data_table is
hard-coded here for reuse at l115.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m2_math_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L15_SOURCE = table(["n", "Fermat's Last Theorem (xⁿ + yⁿ = zⁿ)"], [
    ["n = 2", "Has solutions, e.g. 3² + 4² = 5²"],
    ["n > 2", "No positive integer solutions (proved by Andrew Wiles, 1995)"],
])

CHARTS: dict[str, dict] = {
    "math-m2-l1": {"data_table": table(["Term", "Meaning"], [
        ["Proof by induction", "Establishes a base case, then shows each case implies the next"],
    ])},
    "math-m2-l2": {"data_table": table(["Term", "Meaning"], [
        ["Function", "A rule assigning each input exactly one output, studied via algebraic structure"],
    ])},
    "math-m2-l3": {"data_table": table(["Term", "Meaning"], [
        ["Étale cohomology", "A cohomology theory for schemes that plays the role of singular cohomology in algebraic geometry"],
    ])},
    "math-m2-l4": {"data_table": table(["Term", "Meaning"], [
        ["Perfectoid space", "A p-adic geometric object whose tilting equivalence connects mixed and equal characteristic"],
    ])},
    "math-m2-l5": {"data_table": table(["Term", "Meaning"], [
        ["Langlands correspondence", "Conjecturally relates Galois representations to automorphic representations of GL(n)"],
    ])},
    "math-m2-l6": {"data_table": table(["Term", "Meaning"], [
        ["Algebraic K-theory", "Studies invariants of rings via sequences of abelian groups K_0, K_1, ..."],
    ])},
    "math-m2-l7": {"data_table": table(["Term", "Meaning"], [
        ["Ricci flow", "Evolves a Riemannian metric to smooth out curvature, used by Perelman to prove the Poincaré Conjecture"],
    ])},
    "math-m2-l8": {"data_table": table(["Term", "Meaning"], [
        ["Mirror symmetry", "Relates the complex geometry of one Calabi-Yau manifold to the symplectic geometry of its mirror"],
    ])},
    "math-m2-l9": {"data_table": table(["Term", "Meaning"], [
        ["Floer homology", "An infinite-dimensional analogue of Morse homology used in symplectic topology"],
    ])},
    "math-m2-l10": {"data_table": table(["Term", "Meaning"], [
        ["Gromov-Witten invariant", "Counts holomorphic curves in a symplectic manifold satisfying given constraints"],
    ])},
    "math-m2-l11": {"data_table": table(["Term", "Meaning"], [
        ["Weil conjectures", "Predicted deep properties of zeta functions of varieties over finite fields, proved via étale cohomology"],
    ])},
    "math-m2-l12": {"data_table": table(["Term", "Meaning"], [
        ["Trace formula", "Relates spectral data of automorphic forms to geometric data of a group"],
    ])},
    "math-m2-l13": {"data_table": table(["Term", "Meaning"], [
        ["Iwasawa theory", "Studies growth of arithmetic invariants in towers of number fields using p-adic L-functions"],
    ])},
    "math-m2-l14": {"data_table": table(["Term", "Meaning"], [
        ["Birch and Swinnerton-Dyer conjecture", "Relates the rank of an elliptic curve's rational points to the order of vanishing of its L-function"],
    ])},
    "math-m2-l16": {"data_table": table(["Term", "Meaning"], [
        ["Shimura variety", "A higher-dimensional generalization of modular curves central to arithmetic geometry"],
    ])},
    "math-m2-l17": {"data_table": table(["Term", "Meaning"], [
        ["abc conjecture", "Relates the prime factors of a, b, and a+b, with major implications for number theory if proved"],
    ])},
    "math-m2-l18": {"data_table": table(["Term", "Meaning"], [
        ["Fargues-Fontaine curve", "A fundamental geometric object in p-adic Hodge theory built from perfectoid techniques"],
    ])},
    "math-m2-l19": {"data_table": table(["Term", "Meaning"], [
        ["Derived algebraic geometry", "Extends algebraic geometry using derived rings to handle non-transverse intersections"],
    ])},
    "math-m2-l20": {"data_table": table(["Term", "Meaning"], [
        ["Topological quantum field theory", "Assigns algebraic invariants to manifolds functorially via a cobordism category"],
    ])},
    "math-m2-l21": {"data_table": table(["Term", "Meaning"], [
        ["Atiyah-Singer index theorem", "Equates the analytic index of an elliptic operator to a topological invariant"],
    ])},
    "math-m2-l22": {"data_table": table(["Term", "Meaning"], [
        ["Geometric Langlands program", "A geometric reformulation of the Langlands correspondence over function fields"],
    ])},
    "math-m2-l23": {"data_table": table(["Term", "Meaning"], [
        ["Decomposition theorem", "Describes how pushforwards of perverse sheaves decompose into simpler pieces"],
    ])},
    "math-m2-l24": {"data_table": table(["Term", "Meaning"], [
        ["Hodge theory", "Decomposes cohomology of complex manifolds using harmonic forms and period domains"],
    ])},
    "math-m2-l25": {"data_table": table(["Term", "Meaning"], [
        ["Higgs bundle", "A vector bundle with an extra field used in nonabelian Hodge theory correspondences"],
    ])},
    "math-m2-l26": {"data_table": table(["Term", "Meaning"], [
        ["Yang-Mills mass gap", "A Clay Millennium Problem asking whether quantum Yang-Mills theory has a positive mass gap"],
    ])},
    "math-m2-l27": {"data_table": table(["Term", "Meaning"], [
        ["Navier-Stokes existence", "A Millennium Problem on whether smooth solutions to Navier-Stokes always exist in 3D"],
    ])},
    "math-m2-l28": {"data_table": table(["Term", "Meaning"], [
        ["Regularity theory (Navier-Stokes)", "Studies whether solutions remain smooth or can develop singularities over time"],
    ])},
    "math-m2-l29": {"data_table": table(["Term", "Meaning"], [
        ["Monge-Kantorovich problem", "Finds the cheapest way to transport one probability distribution into another"],
    ])},
    "math-m2-l30": {"data_table": table(["Term", "Meaning"], [
        ["Wasserstein gradient flow", "Models evolution equations as steepest descent in the space of probability measures"],
    ])},
    "math-m2-l31": {"data_table": table(["Term", "Meaning"], [
        ["Concentration of measure", "In high dimensions, functions of many independent variables concentrate sharply near their mean"],
    ])},
    "math-m2-l32": {"data_table": table(["Term", "Meaning"], [
        ["Free probability", "A noncommutative analogue of probability theory used to study random matrices"],
    ])},
    "math-m2-l33": {"data_table": table(["Term", "Meaning"], [
        ["Universality (random matrices)", "Local eigenvalue statistics of large random matrices often depend only on broad symmetry class"],
    ])},
    "math-m2-l35": {"data_table": table(["Term", "Meaning"], [
        ["Sieve methods", "Techniques for estimating the size of sets of integers with restricted prime factorizations"],
    ])},
    "math-m2-l36": {"data_table": table(["Term", "Meaning"], [
        ["Green-Tao theorem", "The primes contain arbitrarily long arithmetic progressions"],
    ])},
    "math-m2-l37": {"data_table": table(["Term", "Meaning"], [
        ["Freiman's theorem", "A set with small sumset must be structurally close to a generalized arithmetic progression"],
    ])},
    "math-m2-l38": {"data_table": table(["Term", "Meaning"], [
        ["Szemerédi's regularity lemma", "Any large graph can be approximated by a bounded number of pseudo-random pieces"],
    ])},
    "math-m2-l39": {"data_table": table(["Term", "Meaning"], [
        ["Ergodic Ramsey theory", "Uses ergodic theory to prove combinatorial results about patterns in sets of integers"],
    ])},
    "math-m2-l40": {"data_table": table(["Term", "Meaning"], [
        ["Entropy (ergodic theory)", "Measures the rate of information generation by a dynamical system, a key invariant"],
    ])},
    "math-m2-l41": {"data_table": table(["Term", "Meaning"], [
        ["Thermodynamic formalism", "Applies statistical mechanics concepts like equilibrium states to dynamical systems"],
    ])},
    "math-m2-l42": {"data_table": table(["Term", "Meaning"], [
        ["Mandelbrot set", "The set of complex parameters c for which the orbit of 0 under z²+c stays bounded"],
    ])},
    "math-m2-l43": {"data_table": table(["Term", "Meaning"], [
        ["Teichmüller space", "Parametrizes complex structures on a surface up to isotopy"],
    ])},
    "math-m2-l44": {"data_table": table(["Term", "Meaning"], [
        ["Mapping class group", "The group of isotopy classes of self-homeomorphisms of a surface"],
    ])},
    "math-m2-l45": {"data_table": table(["Term", "Meaning"], [
        ["Hyperbolic group", "A finitely generated group whose Cayley graph satisfies a thin-triangles condition"],
    ])},
    "math-m2-l46": {"data_table": table(["Term", "Meaning"], [
        ["CAT(0) cube complex", "A nonpositively curved space built from cubes, central to geometric group theory"],
    ])},
    "math-m2-l47": {"data_table": table(["Term", "Meaning"], [
        ["Virtual Haken conjecture", "Every hyperbolic 3-manifold has a finite cover that is Haken (proved by Agol)"],
    ])},
    "math-m2-l48": {"data_table": table(["Term", "Meaning"], [
        ["Infinity-category", "A categorical framework encoding higher homotopies between morphisms, not just equality"],
    ])},
    "math-m2-l49": {"data_table": table(["Term", "Meaning"], [
        ["Topos theory", "Studies categories that behave like the category of sheaves, unifying geometry and logic"],
    ])},
    "math-m2-l50": {"data_table": table(["Term", "Meaning"], [
        ["Univalent foundations", "A foundation of mathematics where equivalent types can be identified (via homotopy type theory)"],
    ])},
    "math-m2-l51": {"data_table": table(["Term", "Meaning"], [
        ["Cobordism hypothesis", "Classifies fully extended topological field theories via dualizable objects"],
    ])},
    "math-m2-l52": {"data_table": table(["Term", "Meaning"], [
        ["Chromatic homotopy theory", "Organizes stable homotopy theory into layers ('chromatic levels') via formal group laws"],
    ])},
    "math-m2-l53": {"data_table": table(["Term", "Meaning"], [
        ["Kervaire invariant one problem", "Determined in which dimensions manifolds with Kervaire invariant one exist"],
    ])},
    "math-m2-l54": {"data_table": table(["Term", "Meaning"], [
        ["Surgery theory", "Classifies manifolds by systematically cutting and regluing to change topology"],
    ])},
    "math-m2-l55": {"data_table": table(["Term", "Meaning"], [
        ["Exotic R^4", "There exist smooth structures on 4-dimensional Euclidean space not diffeomorphic to the standard one"],
    ])},
    "math-m2-l56": {"data_table": table(["Term", "Meaning"], [
        ["Donaldson/Seiberg-Witten invariants", "Gauge-theoretic invariants that distinguish smooth structures on 4-manifolds"],
    ])},
    "math-m2-l57": {"data_table": table(["Term", "Meaning"], [
        ["Instanton Floer homology", "A Floer-theoretic invariant of 3-manifolds built from Yang-Mills instantons"],
    ])},
    "math-m2-l58": {"data_table": table(["Term", "Meaning"], [
        ["Heegaard Floer homology", "A powerful package of invariants for 3-manifolds and knots defined via Heegaard diagrams"],
    ])},
    "math-m2-l59": {"data_table": table(["Term", "Meaning"], [
        ["Khovanov homology", "A categorification of the Jones polynomial assigning a chain complex to a knot"],
    ])},
    "math-m2-l61": {"data_table": table(["Term", "Meaning"], [
        ["Symplectic field theory", "A framework generalizing Floer theory to contact and symplectic cobordisms"],
    ])},
    "math-m2-l62": {"data_table": table(["Term", "Meaning"], [
        ["Weinstein conjecture", "Every Reeb vector field on a closed contact manifold admits at least one periodic orbit"],
    ])},
    "math-m2-l63": {"data_table": table(["Term", "Meaning"], [
        ["Microlocal sheaf theory", "Studies sheaves via their singular support, applied to symplectic geometry"],
    ])},
    "math-m2-l64": {"data_table": table(["Term", "Meaning"], [
        ["Fukaya category", "An A-infinity category built from Lagrangian submanifolds, central to homological mirror symmetry"],
    ])},
    "math-m2-l65": {"data_table": table(["Term", "Meaning"], [
        ["Cluster algebra", "A commutative algebra generated by mutating variables that reveals surprising positivity structure"],
    ])},
    "math-m2-l66": {"data_table": table(["Term", "Meaning"], [
        ["Quiver representation", "An assignment of vector spaces and linear maps to a directed graph, studied via moduli of sheaves"],
    ])},
    "math-m2-l67": {"data_table": table(["Term", "Meaning"], [
        ["Geometric representation theory", "Studies representations of reductive groups using geometric objects like flag varieties"],
    ])},
    "math-m2-l68": {"data_table": table(["Term", "Meaning"], [
        ["Kazhdan-Lusztig conjectures", "Relate multiplicities in representations of Lie algebras to Kazhdan-Lusztig polynomials"],
    ])},
    "math-m2-l69": {"data_table": table(["Term", "Meaning"], [
        ["Vertex operator algebra", "An algebraic structure formalizing conformal field theory's operator product expansions"],
    ])},
    "math-m2-l70": {"data_table": table(["Term", "Meaning"], [
        ["Monstrous moonshine", "A surprising connection between the Monster group and modular functions like the j-invariant"],
    ])},
    "math-m2-l72": {"data_table": table(["Term", "Meaning"], [
        ["Deformation quantization", "Constructs a noncommutative algebra deforming the classical functions on a Poisson manifold"],
    ])},
    "math-m2-l73": {"data_table": table(["Term", "Meaning"], [
        ["Spectral triple", "The core data of noncommutative geometry, generalizing Riemannian manifolds algebraically"],
    ])},
    "math-m2-l74": {"data_table": table(["Term", "Meaning"], [
        ["Baum-Connes conjecture", "Relates the K-theory of a group's reduced C*-algebra to its equivariant K-homology"],
    ])},
    "math-m2-l75": {"data_table": table(["Term", "Meaning"], [
        ["Von Neumann factor", "A von Neumann algebra with trivial center, classified into types I, II, and III"],
    ])},
    "math-m2-l76": {"data_table": table(["Term", "Meaning"], [
        ["Subfactor theory", "Studies inclusions of von Neumann factors via invariants like the Jones index and planar algebras"],
    ])},
    "math-m2-l77": {"data_table": table(["Term", "Meaning"], [
        ["Random graph model", "A probabilistic model (e.g. Erdős–Rényi) exhibiting sharp phase transitions in connectivity"],
    ])},
    "math-m2-l78": {"data_table": table(["Term", "Meaning"], [
        ["Percolation theory", "Studies connectivity of random subgraphs of a lattice as edge probability varies"],
    ])},
    "math-m2-l79": {"data_table": table(["Term", "Meaning"], [
        ["Schramm-Loewner evolution", "A family of random curves describing scaling limits of 2D lattice models at criticality"],
    ])},
    "math-m2-l80": {"data_table": table(["Term", "Meaning"], [
        ["Stochastic PDE", "A partial differential equation driven by random noise, blending analysis and probability"],
    ])},
    "math-m2-l81": {"data_table": table(["Term", "Meaning"], [
        ["Malliavin calculus", "A stochastic calculus of variations used to study smoothness of probability laws"],
    ])},
    "math-m2-l82": {"data_table": table(["Term", "Meaning"], [
        ["Rough path theory", "Extends stochastic calculus to make sense of integrals against very irregular paths"],
    ])},
    "math-m2-l83": {"data_table": table(["Term", "Meaning"], [
        ["Free boundary problem", "A PDE problem where the domain's boundary is itself an unknown to be solved for"],
    ])},
    "math-m2-l84": {"data_table": table(["Term", "Meaning"], [
        ["Elliptic/parabolic regularity", "Studies conditions under which solutions to PDEs are smooth"],
    ])},
    "math-m2-l85": {"data_table": table(["Term", "Meaning"], [
        ["Viscosity solution", "A weak solution concept for fully nonlinear PDEs lacking classical smoothness"],
    ])},
    "math-m2-l86": {"data_table": table(["Term", "Meaning"], [
        ["Mean curvature flow", "Evolves a surface in the direction that most rapidly decreases its area"],
    ])},
    "math-m2-l87": {"data_table": table(["Term", "Meaning"], [
        ["Willmore conjecture", "Identified the torus minimizing the Willmore energy among immersed tori"],
    ])},
    "math-m2-l88": {"data_table": table(["Term", "Meaning"], [
        ["Isoperimetric inequality", "Among regions of fixed volume, the ball minimizes surface area (with Riemannian generalizations)"],
    ])},
    "math-m2-l89": {"data_table": table(["Term", "Meaning"], [
        ["Spectral geometry", "Studies how much of a shape's geometry is determined by the spectrum of its Laplacian"],
    ])},
    "math-m2-l90": {"data_table": table(["Term", "Meaning"], [
        ["Pontryagin maximum principle", "Gives necessary conditions for an optimal control trajectory via a Hamiltonian system"],
    ])},
    "math-m2-l91": {"data_table": table(["Term", "Meaning"], [
        ["Hamilton-Jacobi equation", "A first-order nonlinear PDE central to optimal control, solved via viscosity solutions"],
    ])},
    "math-m2-l92": {"data_table": table(["Term", "Meaning"], [
        ["Mean field games", "Models strategic interaction among a very large number of similar rational agents"],
    ])},
    "math-m2-l93": {"data_table": table(["Term", "Meaning"], [
        ["Compressed sensing", "Recovers sparse signals from far fewer measurements than classical sampling theory requires"],
    ])},
    "math-m2-l94": {"data_table": table(["Term", "Meaning"], [
        ["Lasso", "A regression method that induces sparsity via an L1 penalty, central to high-dimensional statistics"],
    ])},
    "math-m2-l95": {"data_table": table(["Term", "Meaning"], [
        ["Semidefinite programming relaxation", "Approximates hard combinatorial optimization problems using convex SDP relaxations"],
    ])},
    "math-m2-l96": {"data_table": table(["Term", "Meaning"], [
        ["Unique games conjecture", "A conjecture in complexity theory implying strong hardness of approximation results"],
    ])},
    "math-m2-l97": {"data_table": table(["Term", "Meaning"], [
        ["Expander graph", "A sparse graph that is highly connected, characterized by a spectral gap"],
    ])},
    "math-m2-l98": {"data_table": table(["Term", "Meaning"], [
        ["Discrepancy theory", "Measures how uniformly a set can be split or colored relative to a family of subsets"],
    ])},
    "math-m2-l99": {"data_table": table(["Component", "Purpose"], [
        ["Thesis research seminar", "Presents and defends original mathematical research toward a master's thesis"],
    ])},
    "math-m2-l100": {"data_table": table(["Term", "Meaning"], [
        ["Cohen-Lenstra heuristics", "Predict the statistical distribution of class groups of random number fields"],
    ])},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"math-m2-l{base_n}"
    worked_key = f"math-m2-l{worked_n}"
    if base_n == 15:
        CHARTS[worked_key] = {"data_table": dict(_L15_SOURCE)}
    elif base_key in CHARTS:
        CHARTS[worked_key] = {"data_table": dict(CHARTS[base_key]["data_table"])}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Math"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m2.json Math: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M2 Math lessons.")


if __name__ == "__main__":
    main()
