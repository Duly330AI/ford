- [ ] ID: TASK-M5-16
  Title: Slot-UI Erweiterung (Slotliste, Umbenennen, Loeschen)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/scenes/ui_save_slots.py`, `tests/smoke/test_ui_save_slots_import.py`
  DependsOn: TASK-M5-06, TASK-M5-07
  Notes:
  Liste Slots mit Metadaten (Spielzeit, Datum, Seed). Buttons: Laden, Loeschen, Umbenennen (mit Bestaetigung).
  Acceptance:
  - [ ] UI-Befehle rufen Save-Service korrekt auf.
  - [ ] Headless Tests koennen Adapter instanziieren.
  Tests:
  - [ ] Smoke Test fuer UI-Adapter.
  - [ ] Rename/Delete rufen Save-Service Mocks auf.
