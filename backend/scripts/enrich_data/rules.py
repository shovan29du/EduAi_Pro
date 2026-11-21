from .rules_tech import RULES as _A
from .rules_econ import RULES as _B
from .rules_science import RULES as _C
from .rules_history import RULES as _D

# The first batch of rules was written for graduate lessons. Equation-heavy ones
# stay at graduate level (and the advanced undergraduate years); the rest, which
# are mostly real events and examples, suit every level.
_MASTERS_ONLY = {"stochastic", "topology", "riemann", "particle", "condensed", "compchem", "neuro",
                 "options", "var", "mm", "econometrics", "linalg"}
_ADVANCED = {"gen", "rl", "cnn", "distributed", "complexity", "gametheory", "matching", "infotheory",
             "quantumcomp", "spectro", "polymer", "transformer", "optim", "capbudget", "bonds"}

RULES = _A + _B + _C + _D
for _r in RULES:
    if _r["id"] in _MASTERS_ONLY:
        _r["levels"] = ["m1", "m2"]
    elif _r["id"] in _ADVANCED:
        _r["levels"] = ["ug3", "ug4", "m1", "m2"]
    elif _r["levels"] is None:
        _r["levels"] = None

from .rules_charts import RULES as _E  # noqa: E402
from .rules_ug_stem import RULES as _F  # noqa: E402
from .rules_ug_social import RULES as _G  # noqa: E402
from .rules_ug_tech import RULES as _H  # noqa: E402

RULES = RULES + _E + _F + _G + _H

from .rules_school import RULES as _S  # noqa: E402
from .rules_school import SCHOOL_OK  # noqa: E402

RULES = RULES + _S

# Levels at which a rule applies. A rule that names no level suits College Level 1
# upward; school Grades 6-10 only get rules that are explicitly marked for them.
_ADULT = ["c1", "c2", "ug1", "ug2", "ug3", "ug4", "m1", "m2"]
for _r in RULES:
    if _r["levels"] is None:
        _r["levels"] = list(_ADULT)
    if _r["id"] in SCHOOL_OK:
        _r["levels"] = sorted(set(_r["levels"]) | set(SCHOOL_OK[_r["id"]]), key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x))
