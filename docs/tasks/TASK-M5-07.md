- [ ] ID: TASK-M5-07
  Title: Save-Service/Fassade (sync/async Hooks, Signals)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_service.py`, `tests/integration/test_save_load_service.py`
  DependsOn: TASK-M5-02, TASK-M5-03, TASK-M5-04, TASK-M5-05, TASK-M5-06
  Notes:
  Expose Funktionen save(slot, kind), load(slot, kind), events (before_save, after_save, after_load). Integriere mit Systemen fuer Flush/Reload.
  Acceptance:
  - [ ] Hooks feuern deterministisch; State nach Load entspricht Contract.
  - [ ] Fehlgeschlagene Saves rollen zurueck (keine defekten Dateien).
  Tests:
  - [ ] Integrationstest mit Mock-Systemen fuer before/after Hooks.
  - [ ] Fehlerpfad: Exception in Hook -> Save abgebrochen ohne Dateischaden.
