- [ ] ID: TASK-M6-UI-16-Menu-Character
  Title: UI Event Bus & Data Bindings (Game Events to UI Updates)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/event_bus.py`, `tests/ui/test_event_bindings.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Extend the event bus per UI_SPEC_UO_STYLE.md Section 13 to cover SKILL_GAIN, STAT_GAIN, HIT_RESULT, LOOT_ADDED, CRAFT_DONE, COMBAT_TURN_START, COMBAT_TURN_END, UI_TOAST, and CONTAINER_RESPAWNED.
  Map bindings for hp, resistances, skills (0.1 precision), weapon recovery predictions, and inventory updates.
  Provide diagnostic tools to inspect event queues and binding latency.
  Acceptance:
  - [ ] Event bus handles all named events with fan-out to subscribers.
  - [ ] Bindings update UI elements for stats, resistances, skills, and weapon recovery in real time.
  - [ ] Precision for skills remains at 0.1 increments without rounding drift.
  - [ ] Diagnostics report queue depth and last dispatch timestamp.
  Tests:
  - [ ] tests/ui/test_event_bindings.py::test_event_dispatch
  - [ ] tests/ui/test_event_bindings.py::test_binding_updates
  - [ ] tests/ui/test_event_bindings.py::test_skill_precision
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/QUEST_SYSTEM.md
