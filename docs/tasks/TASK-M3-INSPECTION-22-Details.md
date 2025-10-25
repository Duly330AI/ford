- [ ] ID: TASK-M3-22
  Title: Anti-Macro Penalty Detection & Application
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/skills.py`, `tests/systems/test_anti_macro.py`
  DependsOn: TASK-M3-06, TASK-M3-24
  Notes:
  Add repeat-action detection that records the tuple (skill_id, target_id, location_tile) and timestamps so repeated interactions within the configurable `repeat_window` (30 seconds default in `progression_rules.json.skill.anti_macro`) can be penalized as described in GAMEPLAY_ADDENDUM_UO.md Section B.
  Apply the anti-macro multiplier by adjusting the computed gain chance via `gain_chance *= (1 - penalty)` where `penalty` defaults to 0.2 but supports overrides from progression rules.
  Decay or clear the penalty state once the player changes target/position or the window expires, using the shared timekeeper to remain deterministic during tests.
  Provide instrumentation hooks for analytics/logging to surface anti-macro events and active penalties.
  Acceptance:
  - [ ] Repeated actions detected correctly.
  - [ ] Penalty applied to gain chance.
  - [ ] Penalty decays after time window.
  Tests:
  - [ ] Repeat detection tests (seeded, timekeeper mock).
  - [ ] Penalty application tests (gain chance reduced).
  - [ ] Decay tests (penalty clears after window).
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
