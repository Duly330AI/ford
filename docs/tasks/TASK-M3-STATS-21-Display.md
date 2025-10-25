- [ ] ID: TASK-M3-STATS-21-Display
  Title: Stat Affinity System (STR/DEX/INT/STAM gains on skill gains)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/stats.py`, `tests/systems/test_stat_affinities.py`
  DependsOn: TASK-M3-06, TASK-M2-02
  Notes:
  Load per-skill stat affinity weights from `skills.json` and expose them through the stats subsystem so skill gain events can request weighted rolls as described in GAMEPLAY.md Section 4 and GAMEPLAY_ADDENDUM_UO.md Section B.
  Integrate affinity-driven stat checks into the existing skill gain signal emitted by TASK-M3-06, applying the formula `P(stat_gain) = base_chance * affinity_weight * (1 - today_gains / daily_cap)` using parameters from `progression_rules.json.stats`.
  Track per-stat daily gain counters (float, 0.1 increments) and prevent rolls once the configured `*_daily_cap` is reached, persisting counters via the save/load pipeline.
  Provide hooks for the UI and analytics to query affinity tables and current daily progress for STR, DEX, INT, and STAM.
  Acceptance:
  - [ ] Stat gain rolls fire on skill gains.
  - [ ] Affinities from `skills.json` correctly weight rolls.
  - [ ] Daily caps enforced (no gains if cap reached today).
  - [ ] Stat gains persist in save/load.
  Tests:
  - [ ] Affinity weighting tests (seeded).
  - [ ] Daily cap enforcement tests.
  - [ ] Multi-skill stat gain tests (cumulative).
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
