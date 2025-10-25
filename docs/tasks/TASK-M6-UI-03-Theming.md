- [ ] ID: TASK-M6-UI-03-Theming
  Title: Initiative Bar (Combat Turn Order, Recovery Indicators)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/initiative_bar.py`, `tests/ui/test_initiative_bar.py`
  DependsOn: TASK-M6-UI-01, TASK-M2-08, TASK-M2-04
  Notes:
  Render the combat initiative bar per UI_SPEC_UO_STYLE.md Section 2.5 with portraits arranged by upcoming turn order.
  Highlight the active actor, display movement tiles and remaining actions, and animate recovery or reload cooldown rings.
  Sync initiative updates with combat events so queue changes and delays appear without frame stutter.
  Acceptance:
  - [ ] Initiative list reflects current turn order from the combat engine.
  - [ ] Active actor highlight updates at turn change.
  - [ ] Recovery or reload cooldown rings animate until actions are restored.
  - [ ] Move tiles and remaining actions are visible for the selected combatant.
  Tests:
  - [ ] tests/ui/test_initiative_bar.py::test_order_from_initiative_queue
  - [ ] tests/ui/test_initiative_bar.py::test_cooldown_ring_animation
  - [ ] tests/ui/test_initiative_bar.py::test_move_tiles_display
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
