#!/usr/bin/env python3
"""
Add display_name to all skills in skills.json by converting ID to title case.
Usage: python scripts/migrate_skill_display_names.py
"""
import json
from pathlib import Path


def id_to_display_name(skill_id: str) -> str:
    """
    Convert skill ID to display name.
    Examples:
        swords -> Swords
        evaluate_intelligence -> Evaluate Intelligence
        bowcraft_fletching -> Bowcraft Fletching
    """
    # Replace underscores with spaces and title case each word
    return skill_id.replace("_", " ").title()


def migrate_skills(skills_path: Path) -> tuple[int, int]:
    """
    Add display_name to all skills in skills.json.

    Returns:
        (skills_modified, total_skills)
    """
    with open(skills_path, "r", encoding="utf-8") as f:
        skills = json.load(f)

    skills_modified = 0

    for skill in skills:
        skill_id = skill.get("id", "???")

        if "display_name" not in skill:
            display_name = id_to_display_name(skill_id)
            skill["display_name"] = display_name
            skills_modified += 1
            print(f"  {skill_id}: display_name = '{display_name}'")
        else:
            print(f"  {skill_id}: already has display_name = '{skill['display_name']}'")

    # Write back
    with open(skills_path, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)

    return skills_modified, len(skills)


def main():
    project_root = Path(__file__).parent.parent
    skills_path = project_root / "data" / "skills.json"

    if not skills_path.exists():
        print(f"ERROR: {skills_path} not found")
        return 1

    print(f"🔄 Adding display_name to skills in {skills_path}...")
    skills_modified, total_skills = migrate_skills(skills_path)

    print("\n✅ Migration complete!")
    print(f"   Skills modified: {skills_modified}")
    print(f"   Total skills: {total_skills}")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
