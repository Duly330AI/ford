- [ ] ID: TASK-M5-10
  Title: Save-Policy Guard (verb. Phasen, Fehlermeldungen)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_policy.py`, `tests/systems/test_save_policy.py`
  DependsOn: TASK-M5-07
  Notes:
  Verbiete Saves waehrend aktiver Kampf-Resolution/Animation. Liefere standardisierte Fehlercodes fuer UI.
  Acceptance:
  - [ ] Policy blockt Save-Requests in verbotenen Phasen; Meldung enthaelt Code.
  - [ ] Unit-Tests decken erlaubte/verbotene Zustandskombinationen ab.
  Tests:
  - [ ] Matrix-Test fuer Kombinationszustand (combat_active, animation_pending, etc.).
