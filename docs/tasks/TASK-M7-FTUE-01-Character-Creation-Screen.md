- [ ] ID: TASK-M7-FTUE-01
  Title: Character Creation Screen (Presets, Custom Allocation)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/views/char_creation.py`, `data/tutorial/templates.json`, `tests/views/test_char_creation.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-06, TASK-M3-02
  Notes:
  Implementiere Char-Creation-UI: 5 Presets + Custom-Mode mit Stat/Skill-Allocation per TUTORIAL_FTUE.md. Template-Data JSON-driven. Validation, Preview, Confirmation Flows. Localization-Ready. Skip-Option für Returning Players, Tutorial-Flags updated. Reuse bestehende UI-Components. Events für Tutorial-Manager (on_template_selected, on_character_confirmed). Keyboard-Navigation & Controller-Support.
  Acceptance:
  - [ ] 5 Presets + Custom-Mode, Accurate Stat/Skill Previews, Restrictions enforced.
  - [ ] Selected Config persistiert durch Game-Startup, Save/Load kompatibel.
  - [ ] Skip-Option updates Tutorial-Manager, bypasst Scripted-Intro.
  - [ ] Tests: Template-Integrity, Custom-Allocation respects Point-Limits.
  - [ ] Accessibility: Keyboard, Controller Support.
  Tests:
  - [ ] **Template-Selection-Test**: 5 Presets callable & accurate.
  - [ ] **Custom-Allocation-Test**: Point-Limits respected.
  - [ ] **Validation-Test**: Invalid Configs → Errors.
  - [ ] **Persistence-Test**: Config persists nach Selection.
  References:
  - docs/TUTORIAL_FTUE.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
