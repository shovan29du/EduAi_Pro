#!/usr/bin/env python3
"""Add `wiki_title` to every rendered Practical Skills module and Survival
Skills entry, powering a real live-photo lookup on the frontend (same honest
"real photo or nothing" pattern as the Virtual Museum / Cuisine Centre /
Subject Lessons -- GET /api/museum/thumbnail?wiki_title=...).

Only touches the arrays the frontend actually renders:
  - Practical Skills: pathways.<id>.modules[] (PracticalSkills.jsx's ModuleView)
  - Survival Skills: categories.<id>[] (SurvivalSkills.jsx's SkillDetail)
The legacy `skills` / `levels` structures in practical_skills.json are not
rendered by the current UI, so they're left untouched.

Idempotent: safe to re-run.

Re-run after editing:
    python3 backend/scripts/add_skills_visuals.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRACTICAL_PATH = BASE_DIR / "data" / "practical_skills" / "practical_skills.json"
SURVIVAL_PATH = BASE_DIR / "data" / "survival_skills" / "survival_skills.json"


def main() -> None:
    practical = json.loads(PRACTICAL_PATH.read_text(encoding="utf-8"))
    practical_updated = 0
    for pathway in practical["pathways"].values():
        for module in pathway.get("modules", []):
            if "wiki_title" not in module and module.get("title"):
                module["wiki_title"] = module["title"].strip()
                practical_updated += 1
    PRACTICAL_PATH.write_text(json.dumps(practical, indent=2, ensure_ascii=False) + "\n")

    survival = json.loads(SURVIVAL_PATH.read_text(encoding="utf-8"))
    survival_updated = 0
    for skills in survival["categories"].values():
        for skill in skills:
            if "wiki_title" not in skill and skill.get("name"):
                skill["wiki_title"] = skill["name"].strip()
                survival_updated += 1
    SURVIVAL_PATH.write_text(json.dumps(survival, indent=2, ensure_ascii=False) + "\n")

    print(f"Practical Skills: added wiki_title to {practical_updated} modules.")
    print(f"Survival Skills: added wiki_title to {survival_updated} skills.")


if __name__ == "__main__":
    main()
