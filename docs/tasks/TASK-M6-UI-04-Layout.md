- [ ] ID: TASK-M6-UI-04-Layout
  Title: Character Window (Paperdoll, Attributes, Combat Stats, Resistances)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/character_window.py`, `tests/ui/test_character_window.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-03, TASK-M2-02
  Notes:
  Create the character window described in UI_SPEC_UO_STYLE.md Section 3 with a paperdoll panel and stats tabs.
  Support drag and drop equipping to slots (head, neck, chest, arms, hands, fingers, legs, feet, cloak, belt, backpack) and provide context menus for compare or repair.
  Show attributes, resistances, initiative modifiers, movement, recovery, weight, and daily stat gain arrows with formula tooltips.
  Acceptance:
  - [ ] Paperdoll drag and drop equips and unequips items with stat updates.
  - [ ] Tabs display attributes, combat stats, resistances, and encumbrance data.
  - [ ] Formula tooltips explain derived values such as ATK and movement.
  - [ ] Daily stat gain indicators appear when caps or gains change.
  Tests:
  - [ ] tests/ui/test_character_window.py::test_paperdoll_equip_flow
  - [ ] tests/ui/test_character_window.py::test_stats_tab_values
  - [ ] tests/ui/test_character_window.py::test_formula_tooltip_data
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
