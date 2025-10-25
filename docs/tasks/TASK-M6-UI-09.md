- [ ] ID: TASK-M6-UI-09
  Title: Spellbook UI (Circle Tabs, Mana/Reagents, Cast Rounds, Drag-to-Hotbar)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/spellbook.py`, `tests/ui/test_spellbook.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-06
  Notes:
  Create the spellbook from UI_SPEC_UO_STYLE.md Section 6 with circle tabs or thematic filters.
  List spells with mana cost, reagent requirements, cast rounds (modified by INT and Meditation), range, and effects.
  Allow drag to hotbar and right-click macro creation (self or last target).
  Acceptance:
  - [ ] Circle or themed tabs switch spell lists.
  - [ ] Spell entries show mana, reagents, cast time, and range info.
  - [ ] Drag to hotbar assigns spells to slots.
  - [ ] Right-click macro creation records target presets.
  Tests:
  - [ ] tests/ui/test_spellbook.py::test_tab_switching
  - [ ] tests/ui/test_spellbook.py::test_drag_to_hotbar
  - [ ] tests/ui/test_spellbook.py::test_macro_creation
