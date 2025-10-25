- [ ] ID: TASK-M5-MESSAGING-09-Chat
  Title: QuickSave/QuickLoad UI Adapter
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/scenes/ui_save.py`, `tests/smoke/test_ui_save_import.py`
  DependsOn: TASK-M5-07
  Notes:
  Keybinds: F5 QuickSave, F9 QuickLoad (mit Bestaetigung). Adapter-only; keine Arcade-Abhaengigkeit in Tests.
  Acceptance:
  - [ ] UI ruft Save-Service korrekt auf; verhindert Doppel-Trigger.
  - [ ] Headless Tests koennen Adapter importieren.
  Tests:
  - [ ] Smoke-Test (Import, Handler Aufruf).
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
