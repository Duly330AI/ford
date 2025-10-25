#!/usr/bin/env python3
"""
Migrate reagent display names to IDs in spells.json
Usage: python scripts/migrate_spell_reagents.py
"""
import json
from pathlib import Path

# Mapping: Display Name → Item ID
REAGENT_MAPPING = {
    "Black Pearl": "reagent_black_pearl",
    "Bloodmoss": "reagent_bloodmoss",
    "Blood Moss": "reagent_bloodmoss",  # Alternative spelling
    "Garlic": "reagent_garlic",
    "Ginseng": "reagent_ginseng",
    "Mandrake Root": "reagent_mandrake_root",
    "Nightshade": "reagent_nightshade",
    "Sulfurous Ash": "reagent_sulfurous_ash",
    "Spider's Silk": "reagent_spiders_silk",
}


def migrate_spells(spells_path: Path) -> tuple[int, int]:
    """
    Migrate reagent names to IDs in spells.json

    Returns:
        (spells_modified, reagents_changed)
    """
    with open(spells_path, "r", encoding="utf-8") as f:
        spells = json.load(f)

    spells_modified = 0
    reagents_changed = 0

    for spell in spells:
        spell_id = spell.get("id", "???")
        cost = spell.get("cost", {})
        reagents = cost.get("reagents", {})

        if not reagents or not isinstance(reagents, dict):
            continue

        # Convert keys from display names to IDs
        new_reagents = {}
        spell_changed = False

        for reagent_name, amount in reagents.items():
            if reagent_name in REAGENT_MAPPING:
                new_id = REAGENT_MAPPING[reagent_name]
                new_reagents[new_id] = amount
                reagents_changed += 1
                spell_changed = True
                print(f"  {spell_id}: '{reagent_name}' → '{new_id}'")
            else:
                # Keep as-is if not in mapping (shouldn't happen)
                new_reagents[reagent_name] = amount
                print(f"  WARNING: {spell_id}: Unknown reagent '{reagent_name}'")

        if spell_changed:
            cost["reagents"] = new_reagents
            spells_modified += 1

    # Write back
    with open(spells_path, "w", encoding="utf-8") as f:
        json.dump(spells, f, indent=2, ensure_ascii=False)

    return spells_modified, reagents_changed


def main():
    project_root = Path(__file__).parent.parent
    spells_path = project_root / "data" / "spells.json"

    if not spells_path.exists():
        print(f"ERROR: {spells_path} not found")
        return 1

    print(f"🔄 Migrating reagents in {spells_path}...")
    spells_modified, reagents_changed = migrate_spells(spells_path)

    print("\n✅ Migration complete!")
    print(f"   Spells modified: {spells_modified}")
    print(f"   Reagents changed: {reagents_changed}")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
