- [ ] ID: TASK-M6-UI-07
  Title: Container UI (Lock/Trap Status, Take All, Sort, Respawn Timer)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/container_window.py`, `tests/ui/test_container_window.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-EXT-01
  Notes:
  Follow UI_SPEC_UO_STYLE.md Section 5.2 to render container windows with lock and trap indicators.
  Provide Lockpick, Disarm, Take All, Sort, and Filter buttons, plus drag and drop between container and inventory.
  Surface respawn timers when available and align styles with container metadata.
  Acceptance:
  - [ ] Lock and trap icons reflect container state.
  - [ ] Lockpick and disarm buttons call the respective systems.
  - [ ] Take All and Sort actions update inventories correctly.
  - [ ] Respawn timer countdown displays when configured.
  - [ ] Drag interactions move items between container and backpack.
  Tests:
  - [ ] tests/ui/test_container_window.py::test_lock_trap_icons
  - [ ] tests/ui/test_container_window.py::test_action_buttons
  - [ ] tests/ui/test_container_window.py::test_respawn_timer
