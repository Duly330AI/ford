- [ ] ID: TASK-M4-19
  Title: Fehlerfaelle & Rollbacks (Transaktionen hart absichern)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/integration/test_crafting_rollback.py`, `tests/integration/test_gather_rollback.py`
  DependsOn: TASK-M4-02, TASK-M4-06
  Notes:
  Tests fuer: Inventar voll beim Craft-Abschluss -> sauberer World-Drop; Disconnect/Abort waehrend Gather -> keine "Geister"-Reservierungen.
  Acceptance:
  - [ ] Alle kritischen Rollbacks nachweislich korrekt.
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
