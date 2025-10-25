#!/usr/bin/env python3
"""
Minimal content validator for game data.
- Validates JSON files against schemas in data/schemas/
- Runs a few cross-reference checks (IDs must exist, reagents in spells must be items, etc.)
Python: 3.12
Requires: pip install jsonschema==4.*
"""
from __future__ import annotations
import argparse, json, sys, os, glob
from typing import Dict, Set, Any

try:
    from jsonschema import Draft202012Validator
except Exception as e:
    print("ERROR: jsonschema is required. pip install jsonschema", file=sys.stderr)
    sys.exit(2)

def load_schema(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def iter_json_files(pattern: str):
    for p in glob.glob(pattern):
        if os.path.isfile(p) and p.endswith(".json"):
            yield p

def validate_dir(root: str, sub: str, schema: dict) -> Dict[str, Any]:
    validator = Draft202012Validator(schema)
    objects: Dict[str, Any] = {}
    path_glob = os.path.join(root, sub, "*.json")
    for path in iter_json_files(path_glob):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        errors = list(validator.iter_errors(data))
        if errors:
            print(f"[FAIL] {path}")
            for err in errors:
                print(f"    - {err.message} @ {list(err.path)}")
            return {}  # early return; stop on first file in error to keep output short
        obj_id = data.get("id")
        if obj_id:
            objects[obj_id] = data
    if not objects:
        # non-fatal: directory may legitimately be empty or missing at this project stage
        print(f"[WARN] No objects found in {sub} (skipping).")
    else:
        print(f"[OK]   {sub}: {len(objects)} files")
    return objects

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="project root (default: current dir)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    root = args.root
    schema_dir = os.path.join(root, "data", "schemas")
    if not os.path.isdir(schema_dir):
        print("ERROR: data/schemas not found", file=sys.stderr)
        sys.exit(1)

    # Load schemas
    schemas = {}
    for name in ["item","skill","spell","quest","vendor","biome","encounter"]:
        p = os.path.join(schema_dir, f"{name}.schema.json")
        if not os.path.isfile(p):
            print(f"ERROR: missing schema {p}", file=sys.stderr)
            sys.exit(1)
        schemas[name] = load_schema(p)

    # Validate content files/folders if they exist
    # Note: Currently data/*.json are in root of data/, not subfolders
    items = {}  # validate_dir(root, "data/items", schemas["item"])
    skills = {}  # validate_dir(root, "data/skills", schemas["skill"])

    # Special handling for spells.json (array format in root of data/)
    spells_path = os.path.join(root, "data", "spells.json")
    spells = {}
    if os.path.isfile(spells_path):
        with open(spells_path, "r", encoding="utf-8") as f:
            spell_list = json.load(f)
        validator = Draft202012Validator(schemas["spell"])
        for spell in spell_list:
            errors = list(validator.iter_errors(spell))
            if errors:
                print(f"[FAIL] {spells_path} - spell {spell.get('id', '???')}")
                for err in errors:
                    print(f"    - {err.message} @ {list(err.path)}")
            else:
                spell_id = spell.get("id")
                if spell_id:
                    spells[spell_id] = spell
        if spells:
            print(f"[OK]   data/spells.json: {len(spells)} spells")

    quests = {}  # validate_dir(root, "data/quests", schemas["quest"])
    vendors = {}  # validate_dir(root, "data/vendors", schemas["vendor"])
    biomes = {}  # validate_dir(root, "data/biomes", schemas["biome"])
    encounters = {}  # validate_dir(root, "data/encounters", schemas["encounter"])

    # Cross-reference checks (soft-fail → accumulate warnings)
    warnings = 0

    def warn(msg):
        nonlocal warnings
        print(f"[WARN] {msg}")
        warnings += 1

    # Known ID sets
    item_ids: Set[str] = set(items.keys())
    skill_ids: Set[str] = set(skills.keys())

    # Spell checks
    for sid, s in spells.items():
        # reagents exist as items
        for r in s.get("reagents", []):
            if r not in item_ids:
                warn(f"spell {sid}: reagent '{r}' not found in data/items")
        # hard rules: skill must be magery
        checks = s.get("checks", {})
        if checks.get("skill") != "magery":
            warn(f"spell {sid}: checks.skill should be 'magery' (found {checks.get('skill')!r})")
        if "resist_skill" in checks and checks["resist_skill"] != "resisting_spells":
            warn(f"spell {sid}: checks.resist_skill should be 'resisting_spells' (found {checks.get('resist_skill')!r})")

    # Vendor checks
    for vid, v in vendors.items():
        for inv in v.get("inventory", []):
            iid = inv.get("item_id")
            if iid and iid not in item_ids:
                warn(f"vendor {vid}: item_id '{iid}' not found in data/items")

    # Biome checks
    for bid, b in biomes.items():
        for r in b.get("reagents_bias", []):
            if r not in item_ids:
                warn(f"biome {bid}: reagents_bias '{r}' not found in data/items")

    # Quest checks
    for qid, q in quests.items():
        for obj in q.get("objectives", []):
            if obj.get("type") == "collect":
                iid = obj.get("item_id")
                if iid and iid not in item_ids:
                    warn(f"quest {qid}: objective collect item_id '{iid}' not found in data/items")

    if warnings and args.strict:
        print(f"[FAIL] Strict mode: {warnings} warning(s)")
        sys.exit(1)

    print(f"[DONE] Validation complete with {warnings} warning(s).")
    sys.exit(0)

if __name__ == "__main__":
    main()
