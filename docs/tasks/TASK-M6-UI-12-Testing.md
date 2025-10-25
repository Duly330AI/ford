- [ ] ID: TASK-M6-UI-12
  Title: Interaction Cursor & Targeting System (Use-Target, ESC Cancel, Hover LOS)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/cursor.py`, `tests/ui/test_cursor.py`
  DependsOn: TASK-M6-UI-01, TASK-M1-04
  Notes:
  Build the interaction cursor and targeting flows from UI_SPEC_UO_STYLE.md Section 9.
  Support double-click use, right-click context menus, and the classic use-target cursor with ESC cancel.
  Provide hover overlays for line of sight, range checks, and trap hints when detect hidden is active.
  Acceptance:
  - [ ] Double-click triggers use or interact based on entity type.
  - [ ] Right-click context menu offers configured actions.
  - [ ] Use-target cursor works for skills, spells, and items with ESC cancel.
  - [ ] Hover overlays show LOS, range, and trap hints when applicable.
  Tests:
  - [ ] tests/ui/test_cursor.py::test_double_click_actions
  - [ ] tests/ui/test_cursor.py::test_context_menu_options
  - [ ] tests/ui/test_cursor.py::test_use_target_cancel
  - [ ] tests/ui/test_cursor.py::test_hover_overlays
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
