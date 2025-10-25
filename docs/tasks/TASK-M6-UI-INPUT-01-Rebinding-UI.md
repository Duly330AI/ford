# TASK-M6-UI-INPUT-01: Rebinding UI

**Milestone:** M6 - Complete UI System
**Priority:** P1 (Medium)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M6-UI-01, TASK-M1-INPUT-01-Context-Input-Manager, TASK-M1-INPUT-02-Controls-JSON-Schema

## Objectives

- Build dedicated rebinding screen supporting keyboard and gamepad mappings with search/filter by action.
- Implement listening mode capturing next input, validating conflicts, and offering swap/replace/cancel options.
- Surface conflict resolution UX as per INPUT_AND_REBIND.md including chord handling and reserved keys messaging.
- Support export/import/reset of control profiles leveraging controls loader APIs.
- Add UI tests covering binding flow, conflict detection, and persistence round-trips.
- Use localization service (TASK-M8-I18N-01) for all UI copy, including conflict dialog text and prompts.

## Acceptance Criteria

- Rebinding UI updates controls config and propagates changes to active input manager without restart.
- Conflicting bindings present dialog with options described in design (swap, replace, cancel) and behave deterministically.
- Gamepad and keyboard bindings display simultaneously; chords/hold modifiers indicated visually.
- Tests simulate binding updates ensuring data saved and reloaded correctly.
- Accessibility considerations addressed (narration/visual cues) per project UI conventions.

## Implementation Notes

- Use context stack to enter exclusive rebind mode preventing gameplay inputs during capture.
- Provide virtualization for long action lists to maintain performance.
- Expose telemetry hooks for future analysis (optional toggle).
- Coordinate with localization system to ensure UI strings are key-driven (anticipating Phase 9 work).

## Related Documents

- docs/INPUT_AND_REBIND.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
- docs/TODO/INPUT_AND_REBIND_TD.md
