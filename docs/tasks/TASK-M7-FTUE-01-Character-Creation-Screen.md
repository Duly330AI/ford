# TASK-M7-FTUE-01: Character Creation Screen

**Milestone:** M7 - First Time User Experience
**Priority:** P1 (Medium)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M6-UI-01, TASK-M3-06, TASK-M3-02

## Objectives

- Implement character creation UI featuring preset templates and custom stat/skill allocation per TUTORIAL_FTUE.md.
- Integrate with player entity initialization storing chosen template, stat distribution, and starting gear.
- Provide validation, preview, and confirmation flows including localization-ready copy.
- Support skip option for returning players while preserving unlock flags for FTUE progression.
- Add UI tests covering template selection, custom allocation, and validation errors.

## Acceptance Criteria

- Screen supports 5 presets plus custom mode with accurate stat/skill previews and restrictions.
- Selected configuration persists through game startup and is compatible with save/load schema.
- Skip tutorial option updates tutorial manager flags and bypasses scripted intro when selected.
- Tests verify template data integrity and ensure custom allocation respects point limits.
- Accessibility considerations (keyboard navigation, controller support) addressed.

## Implementation Notes

- Store template data in JSON (e.g., `data/tutorial/templates.json`) to stay data-driven.
- Reuse existing UI components (panels, list widgets) for consistency with rest of M6 UI.
- Expose events for tutorial manager to hook into (on_template_selected, on_character_confirmed).
- Coordinate with localization task to replace inline text with keys once i18n ready.

## Related Documents

- docs/TUTORIAL_FTUE.md
- docs/CONVENTIONS.md
- docs/QUEST_SYSTEM.md
- docs/ARCHITECTURE.md
