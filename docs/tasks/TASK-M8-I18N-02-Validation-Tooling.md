# TASK-M8-I18N-02: Localization Validation Tooling

**Milestone:** M8 - Localization & Internationalization
**Priority:** P2 (Low)
**Estimated Effort:** 2-3d
**Dependencies:** TASK-M8-I18N-01-Localization-Service, TASK-TOOLING-1

## Objectives

- Implement `tools/i18n/check_missing_keys.py` comparing base (`en.json`) with other language files to detect missing/extra keys and unused entries.
- Support optional whitelist/ignore lists for intentionally untranslated keys (dev placeholders).
- Provide CLI output suitable for CI consumption with detailed diff of missing nodes.
- Add unit tests covering scenarios: missing key, extra key, placeholder detection, nested dictionaries.
- Document usage in CONTRIBUTING/README for translators and developers.

## Acceptance Criteria

- Tool exits with non-zero status on missing keys by default; optional flags permit warnings-only mode.
- Reporting includes path to offending key and suggested fix (add/remove entry).
- Tests cover multi-language comparisons and handle large JSON structures efficiently.
- Script compatible with Windows/macOS/Linux environments (no platform-specific assumptions).
- Documentation updated pointing to tooling and expected workflow.

## Implementation Notes

- Reuse existing JSON loading utilities to ensure consistent formatting and ordering.
- Consider caching parsed JSON to avoid duplicate work when tool run repeatedly in CI.
- Provide `--check-unused` mode to detect keys not referenced in source (integration with static analysis optional).
- Integrate with localization manager to optionally list runtime-missing keys.

## Related Documents

- docs/LOCALIZATION.md
- docs/CONVENTIONS.md
- docs/TODO/LOCALIZATION_TD.md
- tools/README.md (if exists)
