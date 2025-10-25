- [ ] ID: TASK-M3-EXT-03
  Title: Trap System & Disarm Mechanics (Tinkering + Detect Hidden)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/traps.py`, `tests/systems/test_traps.py`
  DependsOn: TASK-M3-EXT-01, TASK-M3-EXT-04, TASK-M3-06
  Notes:
  Model traps with fields `armed`, `type`, `difficulty`, `power`, `radius`, `on_open`, and `on_fail_disarm` as described in USABLES_AND_CONTAINERS.md Section 3-4, supporting trap archetypes (needle, poison_gas, explosion, dart, fireburst).
  Implement disarm checks using the blended formula `skill = 0.7 * tinkering + 0.3 * detect_hidden` and `P = clamp(0.02, 0.5 + (skill - difficulty)/200, 0.98)`, consuming a Main Action in combat situations.
  Integrate trap triggers with combat damage resolution, leveraging resist systems from `combat_rules.json`.
  Handle failure outcomes that optionally trigger the trap immediately, and expose hooks for logging/telemetry.
  Acceptance:
  - [ ] Trap types implemented (needle, poison, explosion, dart, fire).
  - [ ] Disarm checks use tinkering + detect_hidden.
  - [ ] Trap damage respects resists (from combat_rules.json).
  - [ ] Failure can trigger trap (configurable).
  Tests:
  - [ ] Disarm success/fail tests (seeded).
  - [ ] Trap damage tests (resists applied).
  - [ ] On-failure trigger tests.
