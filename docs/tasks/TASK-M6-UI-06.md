- [ ] ID: TASK-M6-UI-06
  Title: Inventory UI (Grid and UO-Freeform Modes, Stack-Split, Drag-Drop)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/inventory.py`, `tests/ui/test_inventory.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-04
  Notes:
  Deliver inventory windows per UI_SPEC_UO_STYLE.md Section 5.1 with toggleable grid and freeform container layouts.
  Show backpack slots, weight, gold, and filters, supporting drag from inventory to paperdoll or hotbar.
  Implement stack split via Shift+Drag, quick transfer via Ctrl+Click, and repair previews with success chance info.
  Acceptance:
  - [ ] Inventory switches between grid and freeform modes.
  - [ ] Stack split dialog appears on Shift+Drag with correct results.
  - [ ] Ctrl+Click moves items to the active container.
  - [ ] Repair preview shows tool requirements, success chance, and durability change.
  - [ ] Drag to paperdoll or hotbar performs the expected action.
  Tests:
  - [ ] tests/ui/test_inventory.py::test_mode_toggle
  - [ ] tests/ui/test_inventory.py::test_stack_split
  - [ ] tests/ui/test_inventory.py::test_quick_transfer
  - [ ] tests/ui/test_inventory.py::test_repair_preview
