# TASK-M1-INPUT-02: Controls JSON Schema & Loader

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P1 (Medium)
**Estimated Effort:** 3d
**Dependencies:** TASK-M1-10, TASK-M1-INPUT-01-Context-Input-Manager

## Objectives

- Define `config/controls.json` structure covering contexts, actions, primary/secondary bindings, chords, repeat settings, and gamepad mappings.
- Create schema `config/schemas/controls.schema.json` enforcing key formats, modifier rules, and conflict validation metadata.
- Implement loader to validate configuration, apply defaults, and expose runtime data to input manager.
- Provide migration tooling/template to regenerate default controls file and document customization steps.
- Add tests verifying schema catches invalid bindings (duplicate primary, reserved chords, bad modifier combos).

## Acceptance Criteria

- Controls config validates at startup; descriptive errors logged for misconfigurations.
- Loader merges user overrides with defaults while preserving deterministic ordering for comparisons.
- Data consumed by context manager and rebinding UI without requiring hardcoded key lists.
- Tests include positive fixture and negative scenarios covering keyboard and gamepad entries.
- Documentation updated with control schema reference and instructions for modders.

## Implementation Notes

- Support platform differences (e.g., Mac vs Windows key names) via normalized identifiers.
- Provide versioning field to allow future migrations and compatibility checks.
- Keep loader deterministic to ensure consistent diffs when saving user customizations.
- Integrate with settings/save system to persist user bindings separately from defaults.

## Related Documents

- docs/INPUT_AND_REBIND.md
- docs/CONVENTIONS.md
- docs/TODO/INPUT_AND_REBIND_TD.md
- docs/ARCHITECTURE.md
