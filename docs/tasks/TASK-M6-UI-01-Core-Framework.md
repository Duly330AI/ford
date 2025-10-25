- [ ] ID: TASK-M6-UI-01-Core-Framework
  Title: UI Framework & Architecture (React/TypeScript, Event Bus, State Management)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/framework.py`, `game/ui/event_bus.py`, `tests/ui/test_framework.py`
  DependsOn: -
  Notes:
  Establish the UI foundation from UI_SPEC_UO_STYLE.md Sections 13 and 16, selecting the rendering stack and shared root layout.
  Implement a publish and subscribe event bus covering SKILL_GAIN, HIT_RESULT, LOOT_ADDED, CRAFT_DONE, COMBAT_TURN_START, and related signals.
  Provide reactive state management so bindings like `ui.hp.value` track `stats.hp.current`, with deterministic unit update cadence.
  Ship a markdown-capable tooltip renderer plus layout and hotkey persistence stored in `ui_profile.json` per save slot.
  Integrate Localization-Service (TASK-M8-I18N-01) as the sole source for UI strings when available.
  Acceptance:
  - [ ] UI framework bootstrap renders and responds to resize events.
  - [ ] Event bus publishes and receives subscribed events.
  - [ ] State bindings propagate game data updates without manual refresh calls.
  - [ ] Tooltip engine renders markdown and lazy loads content.
  Tests:
  - [ ] tests/ui/test_framework.py::test_event_bus_pub_sub
  - [ ] tests/ui/test_framework.py::test_state_binding_updates
  - [ ] tests/ui/test_framework.py::test_tooltip_markdown_render
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/LOCALIZATION.md
  - docs/QUEST_SYSTEM.md
