- [ ] ID: TASK-QUALITY-2
  Title: Architectural Compliance Tests (systems/* Zero Arcade Imports)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: $_, $_
  DependsOn: TASK-M1-01..16, TASK-M2-01..18
  Notes:
  Validate all modules under `game/systems/*` import neither arcade nor game scene modules, following ARCHITECTURE.md Sections 1 and 21.
  Enforce the same restriction for `game/util/*` except adapter stubs `util/camera.py` and `util/feedback.py`, plus their tests under `tests/systems/*` and `tests/util/*`.
  Use AST parsing to detect direct and indirect imports (`import arcade`, `from arcade import X`, `import game.scenes.Y`).
  Integrate the compliance test into CI so it runs before unit tests and update architecture docs with the rule.
  Acceptance:
  - [ ] Compliance test scans `game/systems/*` and fails if arcade imports are present.
  - [ ] Compliance test scans `game/util/*` (excluding adapters) and fails on arcade imports.
  - [ ] CI workflow executes the compliance test prior to unit tests.
  - [ ] Architecture documentation notes the zero-arcade rule for systems/util packages.
  Tests:
  - [ ] tests/architecture/test_compliance.py::test_detects_arcade_import
  - [ ] tests/architecture/test_compliance.py::test_adapter_exemptions
  - [ ] tests/architecture/test_compliance.py::test_ci_entrypoint
