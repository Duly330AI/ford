# TASK-M7-FTUE-03: Tutorial UI Overlay

**Milestone:** M7 - First Time User Experience
**Priority:** P1 (Medium)
**Estimated Effort:** 4d
**Dependencies:** TASK-M6-UI-01, TASK-M6-UI-02, TASK-M7-FTUE-02-Tutorial-Manager

## Objectives

- Build overlay system rendering highlight boxes, animated arrows, and contextual instructions referenced in TUTORIAL_FTUE.md.
- Support focus locking on UI elements or world entities with smooth transitions and accessibility options.
- Provide localization-ready text slots and iconography with fallback for missing assets.
- Expose API for tutorial manager to trigger overlays, queue prompts, and auto-dismiss on action completion.
- Add tests covering overlay activation, dismissal, stacking, and controller navigation compatibility.

## Acceptance Criteria

- Overlay highlights respond to tutorial events, following UI layout changes dynamically.
- Prompts display localized text and appropriate control indicators (keyboard/gamepad) based on active bindings.
- System gracefully handles overlapping prompts and ensures only one active highlight at a time per context.
- Tests verify overlay coordinates update when UI elements reposition or resize.
- Documentation explains overlay authoring, including asset naming conventions and performance considerations.

## Implementation Notes

- Utilize existing UI toolkit components where possible; avoid duplicating layout logic.
- Provide fallback no-op implementation for headless tests with logging for assertions.
- Coordinate with localization groundwork to ensure string keys accessible to overlay templates.
- Support theming from art style guide (Phase 10) for consistent visuals.

## Related Documents

- docs/TUTORIAL_FTUE.md
- docs/INPUT_AND_REBIND.md
- docs/CONVENTIONS.md
- docs/TODO/TUTORIAL_FTUE_TD.md
