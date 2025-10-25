- [ ] ID: TASK-M4-DIFFICULTY-11-Scaling
  Title: Persistenz-Hooks (Queues, Node-State) - Vorbereitung M5
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_contract.py` (Erweiterung)`, `tests/systems/test_save_contract_m4.py`
  DependsOn: TASK-M4-02, TASK-M4-04
  Notes:
  `to_dict()/from_dict()` fuer: aktive Queue-Jobs (rest_time, recipe_id, reserved_items) und Node-States (`depleted`, `respawn_at`).
  Acceptance:
  - [ ] Roundtrip in-memory; IDs stabil; Fehler bei unbekannten IDs.
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
