- [ ] ID: TASK-M6-UI-14-Menu-Main
  Title: Window Management (Docking, Size, Transparency, Layouts)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/window_manager.py`, `tests/ui/test_window_manager.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Add window management capabilities from UI_SPEC_UO_STYLE.md Section 11 including docking, resizing, and transparency.
  Support layout profiles for overworld, combat, and crafting views, with profile hotkeys.
  Implement UI scale adjustments from 80% to 150% with preview before apply.
  Acceptance:
  - [ ] Windows can dock to edges or stack with snap guides.
  - [ ] Resize and transparency settings persist per window.
  - [ ] Users switch between at least three saved layouts.
  - [ ] UI scale adjustment applies globally within the allowed range.
  Tests:
  - [ ] tests/ui/test_window_manager.py::test_docking_snap
  - [ ] tests/ui/test_window_manager.py::test_layout_profile_switch
  - [ ] tests/ui/test_window_manager.py::test_ui_scale_range
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
