- [ ] ID: TASK-M5-02
  Title: Save-Contract Implementierung (to_dict/from_dict)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_contract.py`, `tests/systems/test_save_contract_roundtrip.py`
  DependsOn: TASK-M5-01, TASK-M3-16, TASK-M4-11
  Notes:
  Serialisiere/Deserialisiere Game-State (Player, Inventory/Hotbar, Equipment, Skills, Crafting, Nodes, RNG). Nutze stabile IDs, keine direkten Objekt-Referenzen.
  Acceptance:
  - [ ] Roundtrip (dict -> contract -> dict) liefert identische Daten fuer Beispielzustand.
  - [ ] Fehlende Pflichtfelder loesen ValidationError mit Kontext aus.
  Tests:
  - [ ] Roundtrip-Tests fuer Kernsysteme.
  - [ ] Fehlerfall-Tests (fehlende Items, falsche Typen).
