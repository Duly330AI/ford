- [ ] ID: TASK-M6-UI-10
  Title: Crafting UI (Recipe List, Detail Panel, Queue with Priorities, Success Tooltip)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/crafting.py`, `tests/ui/test_crafting.py`
  DependsOn: TASK-M6-UI-01, TASK-M4-02
  Notes:
  Match UI_SPEC_UO_STYLE.md Section 7 with recipe filters, detail panel, and queue management.
  Show ingredient counts, required tools or stations, success chance with sweet spot info, craft time, and XP hints.
  Support priority queue editing and indicate combat lock behavior when crafting is paused.
  Acceptance:
  - [ ] Recipe list filters by category, station, and skill requirement.
  - [ ] Detail panel lists inputs, outputs, success chance, time, and XP hints.
  - [ ] Queue view allows reordering and priority changes.
  - [ ] Combat lock disables crafting interactions while showing queue status.
  Tests:
  - [ ] tests/ui/test_crafting.py::test_recipe_filters
  - [ ] tests/ui/test_crafting.py::test_success_tooltip
  - [ ] tests/ui/test_crafting.py::test_queue_priority_mods
  - [ ] tests/ui/test_crafting.py::test_combat_lock_indicator
