- [ ] ID: TASK-M8-I18N-02-Validation-Tooling
  Title: Localization Validation Tooling (Key Diff, Unused Detection)
  Status: Proposed
  Priority: P2
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `tools/i18n/check_missing_keys.py`, `tests/tools/test_i18n_validation.py`
  DependsOn: TASK-M8-I18N-01, TASK-TOOLING-1
  Notes:
  Implementiere `tools/i18n/check_missing_keys.py`: Compare Base (`en.json`) ↔ Andere Languages, Detect Missing/Extra-Keys, Unused-Entries. Optional Whitelist/Ignore-Lists für Intentionally-Untranslated (Dev-Placeholders). CLI-Output für CI-Consumption mit Detailed-Diff. Windows/macOS/Linux-Compatible. Reuse Existing JSON-Loaders. Caching für Repeated-Runs. Optional `--check-unused` Mode.
  Acceptance:
  - [ ] Tool exits Non-Zero on Missing-Keys (Default), Warnings-Only Mode Optional.
  - [ ] Reporting: Path zu Offending-Key, Suggested-Fix (Add/Remove).
  - [ ] Tests: Multi-Language-Comparisons, Large-JSON-Structures efficient.
  - [ ] Platform-Compatible (Windows/macOS/Linux).
  - [ ] Doku: Usage, Expected-Workflow für Translators/Devs.
  Tests:
  - [ ] **Missing-Key-Test**: Detects missing Entries.
  - [ ] **Extra-Key-Test**: Detects Extra Entries.
  - [ ] **Unused-Detection-Test**: `--check-unused` finds Unused Keys.
  - [ ] **Large-File-Test**: Performance bei großen JSONs acceptable.
  References:
  - docs/LOCALIZATION.md
  - docs/CONVENTIONS.md
  - tools/README.md
