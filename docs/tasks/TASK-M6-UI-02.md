- [ ] ID: TASK-M6-UI-02
  Title: HUD (HP/Mana/Stamina Bars, Buff/Debuff Pips, Hotbar, Journal, Minimap)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/hud.py`, `tests/ui/test_hud.py`
  DependsOn: TASK-M6-UI-01, TASK-M2-02, TASK-M2-05, TASK-M3-04
  Notes:
  Build the HUD elements defined in UI_SPEC_UO_STYLE.md Sections 2.1-2.4 including status bars, buff pips, hotbar, journal, and minimap.
  Display HP, Mana, Stamina, and Weight with numeric and bar readouts tied to stats updates.
  Expose buff and debuff timers with tooltips listing source, effect, and remaining rounds or seconds.
  Implement a 10-slot hotbar with drag and drop from inventory, cooldown overlays, and journal filters plus minimap encounter bubble rendering.
  Acceptance:
  - [ ] Status bars update in real time when player stats change.
  - [ ] Buff and debuff indicators show accurate durations and tooltips.
  - [ ] Hotbar triggers assigned actions via keys 1-0 and F-keys with cooldown feedback.
  - [ ] Journal records +0.1 skill gains, combat outcomes, and supports category filters.
  - [ ] Minimap renders party, hostiles, containers, and the encounter bubble radius.
  Tests:
  - [ ] tests/ui/test_hud.py::test_status_bar_updates
  - [ ] tests/ui/test_hud.py::test_buff_pip_countdown
  - [ ] tests/ui/test_hud.py::test_hotbar_action_binding
  - [ ] tests/ui/test_hud.py::test_journal_filters
