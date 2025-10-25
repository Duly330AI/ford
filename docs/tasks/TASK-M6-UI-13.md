- [ ] ID: TASK-M6-UI-13
  Title: Hotkey/Keybind System (Remapping, QWERTZ Default, Macro Support)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/keybinds.py`, `tests/ui/test_keybinds.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Implement the keybind manager from UI_SPEC_UO_STYLE.md Section 10 with QWERTZ defaults for core panels and actions.
  Provide UI for remapping keys with persistence in `ui_profile.json` across save slots.
  Allow macro sequences that execute chained actions such as cast heal then target self.
  Acceptance:
  - [ ] Default QWERTZ bindings open the correct panels and actions.
  - [ ] Key remapping UI saves and loads custom layouts.
  - [ ] Macros execute configured action sequences.
  - [ ] Conflicting assignments surface warnings before save.
  Tests:
  - [ ] tests/ui/test_keybinds.py::test_default_bindings
  - [ ] tests/ui/test_keybinds.py::test_remap_persistence
  - [ ] tests/ui/test_keybinds.py::test_macro_execution
