# Content Validation & i18n – Starter

Python: 3.12

## Install
```bash
python -m venv .venv && . .venv/bin/activate
pip install jsonschema
```

## Run validator
```bash
python tools/validate_content.py --root .
# or strict mode
python tools/validate_content.py --root . --strict
```

## i18n check
```bash
python tools/i18n/check_missing_keys.py
```

## Notes
- Canonical reagent ID: `bloodmoos`
- Spellcasting skill: `magery`
- Resist skill: `resisting_spells`
- Schemas are intentionally permissive (`additionalProperties: true`) to avoid blocking iteration.
