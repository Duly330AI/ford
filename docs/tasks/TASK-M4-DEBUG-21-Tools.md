- [ ] ID: TASK-M4-DEBUG-21-Tools
  Title: Levers, Buttons, Doors, Pressure Plates (Toggle Groups)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/toggles.py`, `tests/systems/test_toggles.py`
  DependsOn: TASK-M3-EXT-01
  Notes:
  Implement toggleable world objects (lever, button, door, pressure_plate) using the schemas in USABLES_AND_CONTAINERS.md Section 2 and Section 6, supporting group IDs that map activators to multiple targets.
  Support toggle modes `flip`, `momentary`, and `permanent`, enforcing pressure plate thresholds via `weight_min` and optional `hold_to_activate`.
  Integrate with containers/entities so doors respond to toggle events and traps can be disarmed via grouped levers.
  Acceptance:
  - [ ] Toggle groups work (one lever affects multiple targets).
  - [ ] Modes implemented (flip, momentary, permanent).
  - [ ] Pressure plates trigger on weight threshold.
  - [ ] Doors open/close correctly.
  Tests:
  - [ ] Toggle group tests (1->N targets).
  - [ ] Mode tests (flip vs momentary).
  - [ ] Pressure plate weight tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
