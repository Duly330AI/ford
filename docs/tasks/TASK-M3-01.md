- [ ] ID: TASK-M3-01
  Title: Daten-Schemas & Validatoren (items/skills/loot_tables)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/validation.py`, `data/schemas/items.schema.json`, `data/schemas/skills.schema.json`, `data/schemas/loot_tables.schema.json`, `tests/systems/test_validation.py`
  DependsOn: -
  Notes:
  JSON-Schemas + Python-Validatoren (pydantic/jsonschema). Pruefen: ID-Format, Eindeutigkeit, referentielle Integritaet (Loot-Eintraege referenzieren vorhandene `item_id` oder `table_id`), Wertebereiche.
  Acceptance:
  - [ ] `items.json`, `skills.json`, `loot_tables.json` validieren fehlerfrei.
  - [ ] Fehlende/duplizierte IDs werden mit aussagekraeftigen Fehlermeldungen abgewiesen.
  Tests:
  - [ ] Positiv-/Negativfaelle (fehlende Felder, falsche Typen, zirkulaere Tabellen).
