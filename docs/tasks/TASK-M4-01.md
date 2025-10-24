- [ ] ID: TASK-M4-01
  Title: Rezept- & Node-Schemas + Validatoren
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/validation.py` (Erweiterung)`, `data/schemas/recipes.schema.json`, `data/schemas/nodes.schema.json`, `data/schemas/stations.schema.json`, `tests/systems/test_validation_m4.py`
  DependsOn: TASK-M3-01
  Notes:
  Felder (Vorschlag):
        - **recipes.json**: `id`, `station`, `inputs[{item_id, qty}]`, `outputs[{item_id, qty_min, qty_max}]`, `time_sec`, `skill{ id, min, xp_gain }`, `tool_required?`, `success{ chance, crit_chance, crit_bonus }`, `fail_returns?[]`.
        - **nodes.json**: `id`, `type(ore/tree/herb)`, `tier`, `yield{ table_id|item_id, qty_min, qty_max }`, `respawn_sec`, `tool_required`, `skill{id, xp_gain}`, `hp?` (fuer zaehe Nodes), `rarity` (Spawngewicht).
        - **stations.json** (optional): `id (forge/alchemy)`, `ui_name`, `queue_limit`, `process_parallel?`.
  Acceptance:
  - [ ] Alle drei Dateien validieren korrekt; klare Fehlermeldungen.
  Tests:
  - [ ] Positiv/Negativ: fehlende Felder, falsche Typen, ungueltige Referenzen.
