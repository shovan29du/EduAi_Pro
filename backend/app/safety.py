import json
import re
from pathlib import Path

SAFE_DIR = Path(__file__).resolve().parent.parent / "safe"


class SafetyFilter:
    """Two-tier content filter.

    - Hard-blocked terms (weapons/drug-synthesis/self-harm instructions,
      CSAM, extremism, hate slurs) are always blocked, at every academic
      level from Grade 1 through Master's. These are never relaxed.
    - "Child" terms (blocked_words.json) are a softer, topic-word filter
      appropriate for young learners. They are applied by default
      (``strict=True``) for backward compatibility, but callers serving
      college/undergraduate/master's/adult content should pass
      ``strict=False`` so normal academic vocabulary (e.g. "violence in
      20th-century history", "alcohol metabolism", "drug policy reform")
      is not mangled for adult learners.
    """

    def __init__(self):
        with open(SAFE_DIR / "blocked_words.json", encoding="utf-8") as f:
            self.blocked_words = json.load(f)["blocked_words"]
        self._child_pattern = re.compile(
            r"\b(" + "|".join(re.escape(w) for w in self.blocked_words) + r")\b",
            re.IGNORECASE,
        )

        self.hard_blocked_terms: list[str] = []
        hard_path = SAFE_DIR / "hard_blocked_terms.json"
        if hard_path.exists():
            with open(hard_path, encoding="utf-8") as f:
                categories = json.load(f).get("categories", {})
            for terms in categories.values():
                self.hard_blocked_terms.extend(terms)

        if self.hard_blocked_terms:
            # Single-word entries get word boundaries; multi-word phrases
            # are matched as-is (word-boundary phrase matching).
            parts = []
            for term in self.hard_blocked_terms:
                escaped = re.escape(term)
                if " " in term:
                    parts.append(escaped)
                else:
                    parts.append(r"\b" + escaped + r"\b")
            self._hard_pattern = re.compile("(" + "|".join(parts) + ")", re.IGNORECASE)
        else:
            self._hard_pattern = None

    def is_safe(self, text: str, strict: bool = True) -> bool:
        if not text:
            return True
        if self._hard_pattern is not None and self._hard_pattern.search(text):
            return False
        if strict and self._child_pattern.search(text):
            return False
        return True

    def sanitize(self, text: str, strict: bool = True) -> str:
        if not text:
            return text
        if self._hard_pattern is not None:
            text = self._hard_pattern.sub(lambda m: "*" * len(m.group(0)), text)
        if strict:
            text = self._child_pattern.sub(lambda m: "*" * len(m.group(0)), text)
        return text

    def validate_resource(self, resource: dict, strict: bool = True) -> bool:
        for value in resource.values():
            if isinstance(value, str) and not self.is_safe(value, strict=strict):
                return False
        return True


safety_filter = SafetyFilter()
