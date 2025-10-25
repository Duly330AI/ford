# TASK-M8-I18N-03: CI Integration for Localization Checks

**Milestone:** M8 - Localization & Internationalization
**Priority:** P2 (Low)
**Estimated Effort:** 2d
**Dependencies:** TASK-M8-I18N-02-Validation-Tooling, TASK-TOOLING-1

## Objectives

- Update `.github/workflows/ci.yml` (or equivalent pipeline) to run localization validation tool on each build.
- Ensure CI step fails on missing keys, providing actionable logs for contributors.
- Add caching or matrix integration to keep pipeline runtime minimal.
- Document new CI behavior in CONTRIBUTING or tooling docs to set contributor expectations.
- Add smoke test verifying workflow changes using `act` or dry-run instructions (if feasible).

## Acceptance Criteria

- CI pipeline executes localization check script and fails when discrepancies detected.
- Workflow logs clearly identify language file causing failure and summarize missing/extra keys.
- Pipeline adjustments maintain reasonable runtime (<1 min added) and reuse existing caching strategies where possible.
- Documentation updated with instructions for running check locally prior to pushing.
- Optional: Provide badge/summary in PR template referencing localization status.

## Implementation Notes

- Consider separate job or stage to isolate localization failures from unit tests for clarity.
- Provide environment variable toggles for skip scenarios (e.g., emergency hotfix) with documented usage.
- Coordinate with repository maintainers to match existing workflow patterns (naming, caching, Python version).
- Ensure script executed with consistent Python version as other tooling to avoid dependency drift.

## Related Documents

- docs/LOCALIZATION.md
- .github/workflows/ci.yml
- docs/CONVENTIONS.md
- docs/TODO/LOCALIZATION_TD.md
