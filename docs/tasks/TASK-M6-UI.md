- [ ] ID: TASK-M6-UI
  Title: Complete UI System (UO-Style HUD, Paperdoll, Skills, Inventory, Tooltips)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `docs/UI_SYSTEM_OVERVIEW.md`
  DependsOn: TASK-M3-02, TASK-M3-06, TASK-M4-02, TASK-M2-08
  Notes:
  Summarize UI_SPEC_UO_STYLE.md Sections 1-14 and CROSS_REFERENCE_ANALYSIS.md Section 11 to outline the UI feature set and integration points.
  Document guiding principles: data-first readability, modular docking windows, localization keys, and accessibility expectations.
  Break down milestone scope into TASK-M6-UI-01 through TASK-M6-UI-17 with links to inventory, skills, crafting, and initiative systems.
  Capture follow-up questions around controller support, theming, and macro defaults in the overview document.
  Verweis auf TASK-M8-I18N-01..03: alle UI-Bildschirme verwenden künftig Localization-Service statt harter Strings.
  Acceptance:
  - [ ] All subtasks reach Status: Done and are referenced from the overview.
  - [ ] docs/UI_SYSTEM_OVERVIEW.md records the architecture, dependencies, and accessibility notes from the spec.
  - [ ] UI integration smoke tests demonstrate real-time updates for HP, skills (0.1 precision), and encounter events.
  Tests:
  - [ ] tests/ui/test_ui_system.py::test_data_binding_smoke
  - [ ] tests/ui/test_ui_system.py::test_layout_profile_roundtrip
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/INPUT_AND_REBIND.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/LOCALIZATION.md
  - docs/QUEST_SYSTEM.md
