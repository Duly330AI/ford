- [ ] ID: TASK-M2-23
  Title: Combat Rules Validation (Load & Validate combat_rules.json at Startup)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: $_, $_, $_
  DependsOn: TASK-M2-02, TASK-M2-12
  Notes:
  Create `data/schemas/combat_rules.schema.json` (JSON Schema Draft-07) capturing required sections hit_chance, parry, damage, movement, recovery, ranged, initiative, dodge.
  Load and validate `combat_rules.json` during startup before gameplay systems initialize, aborting with a descriptive error on failure.
  Check numeric ranges and relationships (e.g., min <= max, probabilities within 0..1, weapon base delay map keys valid).
  Reference CROSS_REFERENCE_ANALYSIS.md Section 14 and ensure missing/wrong fields produce actionable messages.
  Acceptance:
  - [ ] Schema file defines required sections and constraints for combat rules.
  - [ ] Startup validation runs automatically and aborts on invalid data with clear messaging.
  - [ ] All numeric ranges and weapon delay keys are verified against the schema.
  - [ ] Valid combat_rules.json passes without warnings.
  Tests:
  - [ ] tests/util/test_combat_rules_validation.py::test_valid_rules_pass
  - [ ] tests/util/test_combat_rules_validation.py::test_missing_key_fails
  - [ ] tests/util/test_combat_rules_validation.py::test_out_of_range_fails
  - [ ] tests/util/test_combat_rules_validation.py::test_invalid_weapon_key
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
