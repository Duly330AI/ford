# TASK-M1-INPUT-01: Context Input Manager

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P1 (Medium)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M1-10, TASK-M6-UI-01

## Objectives

- Implement context stack manager handling UI > Combat > Overworld > Rebind priorities per INPUT_AND_REBIND.md.
- Normalize input events from Arcade into context-aware action dispatch without direct scene coupling.
- Provide APIs to push/pop contexts, query active context, and register callbacks with conflict resolution.
- Integrate with existing input bindings to ensure backward compatibility for MVP controls.
- Add tests covering context transitions, priority enforcement, and edge cases (nested UI, rebind mode).

## Acceptance Criteria

- Input events routed to highest-priority active context; lower contexts do not receive events when blocked.
- Context manager exposes deterministic stack operations and safe re-entrancy for UI sequences.
- Existing movement/combat input flows remain operational through compatibility shim.
- Tests simulate state transitions verifying correct callbacks triggered or suppressed.
- Developer documentation updated explaining new APIs and migration path for scene input handlers.

## Implementation Notes

- Keep manager within `game/input/` namespace; avoid Arcade imports in systems.
- Provide diagnostic logging toggles for debugging context stack behavior.
- Support temporary contexts with auto-pop semantics (e.g., modal dialogs) via helper utilities.
- Coordinate with rebinding UI task to ensure context transitions when entering listening mode.

## Related Documents

- docs/INPUT_AND_REBIND.md
- docs/ARCHITECTURE.md
- docs/CONVENTIONS.md
- docs/TODO/INPUT_AND_REBIND_TD.md
