- [ ] ID: TASK-M8-I18N-01-Localization-Service
  Title: Localization Service (Key Resolution, Language Switching)
  Status: Proposed
  Priority: P2
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/localization.py`, `data/localization/*.json`, `tests/systems/test_localization.py`
  DependsOn: TASK-M6-UI-01, TASK-M4-QUEST-02, TASK-M7-FTUE-03
  Notes:
  Implementiere LocalizationService: Load i18n-JSON-Files, Key-Resolution mit Parameters, Active-Language-Mgmt. Runtime-Language-Switching, Fallback-Handling, Pluralization-Helpers. Lightweight Adapter für UI/Text-Systems: `translate(key, **params)`. Headless-Testbar. Cache Lookups, Invalidate bei Language-Change. Optional Env-Var für Default-Language. MessageFormat oder Python-Format-Semantik. Optional Instrumentation für Missing-Keys-Logging.
  Acceptance:
  - [ ] Localization-Manager loaded Base (`en`) + Additional Languages (z.B. `de`), Validation.
  - [ ] Systems/Scenes retrieve Translated-Strings via Keys-Only, Missing-Keys → Errors (Dev).
  - [ ] Service cached Lookups für Performance, Cache invalidated on Language-Change.
  - [ ] Tests: Deterministic Outputs per Lookup, Error-Handling für Missing/Unused-Keys.
  - [ ] Doku: API-Usage, UI-Integration.
  Tests:
  - [ ] **Key-Lookup-Test**: Valid Keys → Correct Strings.
  - [ ] **Fallback-Test**: Missing Keys → Fallback-Language (EN).
  - [ ] **Parameter-Substitution-Test**: Params replaced in Template.
  - [ ] **Language-Switch-Test**: Runtime Language-Change works.
  References:
  - docs/LOCALIZATION.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
