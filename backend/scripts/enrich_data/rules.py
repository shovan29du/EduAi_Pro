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
