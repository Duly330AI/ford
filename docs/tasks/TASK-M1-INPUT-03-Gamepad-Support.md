# TASK-M1-INPUT-03: Gamepad Support

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P1 (Medium)
**Estimated Effort:** 4d
**Dependencies:** TASK-M1-INPUT-01-Context-Input-Manager, TASK-M1-INPUT-02-Controls-JSON-Schema

## Objectives

- Implement gamepad input handling including axis deadzones, button mapping, sensitivity curves, and rumble hooks.
- Normalize gamepad events through input manager, allowing context-aware action dispatch identical to keyboard flow.
- Provide configuration fields in controls JSON for gamepad-specific bindings and calibration settings.
- Add tests/simulations verifying deadzone handling, analog navigation, and context switching behavior.
- Document supported controllers and troubleshooting steps for designers/testers.

## Acceptance Criteria

- Gamepad inputs map to actions across contexts without interfering with keyboard/mouse bindings.
- Deadzone and sensitivity settings configurable via controls JSON and applied at runtime.
- Rebinding UI recognizes gamepad inputs and updates configuration accordingly.
- Tests cover analog stick thresholds, button chords, and combination with keyboard usage.
- Accessibility/support docs updated with controller guidelines.

## Implementation Notes

- Abstract platform-specific differences (Xbox/PlayStation layouts) via mapping tables in config.
- Provide optional rumble callbacks for future feedback features (no Arcade coupling in systems layer).
- Ensure deterministic mapping names for use in localization and analytics.
- Coordinate with FTUE/tutorial tasks to include controller prompts where applicable.

## Related Documents

- docs/INPUT_AND_REBIND.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
- docs/TODO/INPUT_AND_REBIND_TD.md
