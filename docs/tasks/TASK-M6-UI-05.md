- [ ] ID: TASK-M6-UI-05
  Title: Skills Window (0.1 Display, Locks, Caps, Curves, Train/Use)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/skills_window.py`, `tests/ui/test_skills_window.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-06, TASK-M3-23, TASK-M3-24
  Notes:
  Implement the skills window from UI_SPEC_UO_STYLE.md Section 4 with search, category filters, and 0.1 precision values.
  Display total skill cap progress, lock icons for UP, LOCK, and DOWN states, and curve profile indicators with tooltips.
  Track recent usage context and expose a Train or Use button for safe practice actions, plus a detail panel showing stat affinities and linked recipes.
  Acceptance:
  - [ ] Skills list shows 0.1 precision values and total cap progress.
  - [ ] Lock icons toggle states and reflect auto-drop behavior.
  - [ ] Curve profile indicators render with explanatory tooltips.
  - [ ] Train or Use button triggers configured practice actions.
  - [ ] Detail panel surfaces stat affinities and linked recipes or spells.
  Tests:
  - [ ] tests/ui/test_skills_window.py::test_precision_display
  - [ ] tests/ui/test_skills_window.py::test_lock_toggle
  - [ ] tests/ui/test_skills_window.py::test_train_button_action
