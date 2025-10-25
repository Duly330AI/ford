- [ ] ID: TASK-M5-12
  Title: Save-Validator (Referenzen, Balancing)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_validate.py`, `tests/systems/test_save_validate.py`
  DependsOn: TASK-M5-02
  Notes:
  Pruefe referentielle Integritaet: Items existieren, Hotbar verweist auf Slots, Nodes IDs reproduzierbar, Queues gueltig.
  Acceptance:
  - [ ] Validator meldet Missing Item/Skill/Node Fehler mit Pfad.
  - [ ] Validierung laeuft vor Load; blockiert invaliden Save.
  Tests:
  - [ ] Negativtests fuer jede Referenzklasse.
  - [ ] Positive Tests mit vollstaendigem Save.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
