# TASK-M8-I18N-01: Localization Service

**Milestone:** M8 - Localization & Internationalization
**Priority:** P2 (Low)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M6-UI-01, TASK-M4-QUEST-02, TASK-M7-FTUE-03

## Objectives

- Implement `game/systems/localization.py` responsible for loading i18n JSON files, resolving keys with parameters, and managing active language.
- Provide runtime language switching, fallback handling, and pluralization helpers per LOCALIZATION.md guidelines.
- Integrate service with UI and text-emitting systems via lightweight adapter/API (e.g. `translate(key, **params)`).
- Ensure service operates headless for tests and exposes deterministic behavior across languages.
- Add tests covering key lookup, fallbacks, parameter substitution, and language switching.

## Acceptance Criteria

- Localization manager loads base language (`en`) plus additional languages (e.g., `de`) with validation.
- Systems/Scenes retrieve translated strings using keys only; missing keys raise descriptive errors in development.
- Service caches lookups for performance and invalidates cache on language change.
- Tests confirm deterministic outputs for repeated lookups and proper error handling for missing/unused keys.
- Documentation describes API usage and integration with UI components.

## Implementation Notes

- Keep localization service independent from UI frameworks; provide minimal dependency injection for scenes.
- Support optional environment variable or config setting for default language selection.
- Align parameter formatting with MessageFormat-style patterns or Python format semantics (documented choice).
- Provide instrumentation (optional) to log missing keys for QA builds.

## Related Documents

- docs/LOCALIZATION.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
- docs/TODO/LOCALIZATION_TD.md
