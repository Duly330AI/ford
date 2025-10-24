- [ ] ID: TASK-M4-08
  Title: Crafting-UI (Queue, Progress, Input/Output, Fehlerfaelle)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/scenes/ui_crafting.py`, `tests/smoke/test_ui_crafting_import.py`
  DependsOn: TASK-M4-03
  Notes:
  Minimal-UI: Rezeptliste (filterbar), Queue mit Fortschritt, Buttons Start/Cancel, Hinweise bei fehlenden Items/Tools/Skill. **Nur Adapter-Tests** (keine GL in Unit).
  Acceptance:
  - [ ] Cancel rollt Reservierungen korrekt zurueck.
  - [ ] UI reagiert auf State-Updates (Adapter).
  Tests:
  - [ ] TBD
