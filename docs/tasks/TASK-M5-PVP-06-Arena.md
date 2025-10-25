- [ ] ID: TASK-M5-06
  Title: Save-Slots Manager (create/list/load/delete)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_slots.py`, `tests/systems/test_save_slots.py`
  DependsOn: TASK-M5-04, TASK-M5-05
  Notes:
  API: list_slots(), save(slot, payload, mode), load(slot, mode), delete(slot). Unterstuetzt manuell/auto/quick Variationen.
  Acceptance:
  - [ ] Slot-Liste sortiert nach Updated-At; inkl. Autosave Rotation.
  - [ ] Loeschen entfernt Dateien + Manifest-Eintrag atomar.
  Tests:
  - [ ] Slot-Rotation fuer Autosaves (max n).
  - [ ] Fehlerfall: Laden eines fehlenden Slots -> SaveNotFoundError.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
