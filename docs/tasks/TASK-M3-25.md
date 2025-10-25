- [ ] ID: TASK-M3-25
  Title: Stat Gain System (on Skill Gain, Affinities, Daily Caps)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/stats.py`, `tests/systems/test_stat_gains.py`
  DependsOn: TASK-M3-21, TASK-M3-24
  Notes:
  Subscribe to the finalized skill gain event stream and roll stat gains for STR, DEX, INT, and STAM using affinity weights from `skills.json[id].stats` together with the `gain_on_skill_gain` scalar in `progression_rules.json.stats`.
  Maintain per-stat daily gain counters (float) that reset on the configured day boundary (game time or real time) and clamp additional gains once `*_daily_cap` is met.
  Ensure gains apply in +0.1 increments and persist via the existing save/load pipeline alongside stat totals and daily counters.
  Provide debugging metrics or logging hooks so design can audit stat gain frequency across sessions.
  Acceptance:
  - [ ] Stat gain rolls fire on skill gain.
  - [ ] Affinities correctly weight rolls.
  - [ ] Daily caps enforced (soft cap, no gains if exceeded).
  - [ ] Daily counters reset at midnight.
  Tests:
  - [ ] Stat gain roll tests (seeded).
  - [ ] Daily cap enforcement tests.
  - [ ] Reset tests (timekeeper mock).
