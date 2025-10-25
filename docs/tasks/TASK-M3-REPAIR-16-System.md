- [ ] ID: TASK-M3-REPAIR-16-System
  Title: Persistenz-Vorbereitung (IDs stabil, Save-Hooks)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_contract.py`, `tests/systems/test_save_contract.py`
  DependsOn: TASK-M3-03, TASK-M3-04, TASK-M3-05, TASK-M3-06, TASK-M3-07, TASK-M3-08, TASK-M3-09, TASK-M3-10, TASK-M3-11, TASK-M3-12
  Notes:
  Noch **keine** Save/Load-Implementierung (kommt M5), aber: definiere klare **Serialisierungs-Form** fuer Inventory/Equipment/Skills/Hotbar (IDs + Mengen/Level).
  Acceptance:
  - [ ] `to_dict()/from_dict()` vorhanden; Roundtrip testbar (in-memory).
  Tests:
  - [ ] Roundtrip-Tests pro System; fehlende IDs -> Fehler.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
