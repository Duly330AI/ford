- [ ] ID: TASK-M6-UI-08
  Title: Tooltip System (Data-Driven, Formula Hints, Markdown Support)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/tooltips.py`, `tests/ui/test_tooltips.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Implement the tooltip system from UI_SPEC_UO_STYLE.md Sections 3.2 and 5.3 with data-driven fields for name, rarity, weight, and value.
  Display weapon and armor specifics such as damage type, base delay class, expected recovery, resist values, and durability.
  Add formula hint blocks sourced from combat_rules.json and support markdown rendering with lazy load on hover.
  Acceptance:
  - [ ] Tooltips include required item stats and metadata.
  - [ ] Formula hint block renders for weapons, armor, and derived stats.
  - [ ] Markdown formatting renders in the tooltip body.
  - [ ] Lazy load avoids frame drops when hovering many items.
  Tests:
  - [ ] tests/ui/test_tooltips.py::test_item_field_render
  - [ ] tests/ui/test_tooltips.py::test_formula_hint_block
  - [ ] tests/ui/test_tooltips.py::test_lazy_load_performance
