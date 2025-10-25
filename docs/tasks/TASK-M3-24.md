- [ ] ID: TASK-M3-24
  Title: Skill Progression Formula (Sweet-Spot, Slowdown, progression_rules.json)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/skills.py`, `tests/systems/test_skill_progression.py`
  DependsOn: TASK-M3-06
  Notes:
  Implement the UO-style skill gain formula outlined in GAMEPLAY_ADDENDUM_UO.md Section B, combining success probability, sweet-spot weighting, slowdown curves, and anti-macro penalties into the final gain chance.
  Load curve definitions and configuration (base multipliers, min/max gain, increment) from `progression_rules.json.curves`, keyed by the `xp_curve` entry in `skills.json`.
  Support slowdown modes `linear`, `quadratic`, `cubic`, and `sqrt`, and expose a deterministic helper for unit tests to evaluate gain chances at given skill levels.
  Integrate with the anti-macro multiplier provided by TASK-M3-22 to ensure final probabilities honor penalties before rolling for the +0.1 gain.
  Acceptance:
  - [ ] Sweet-spot formula works (max gain at p_success ~0.5).
  - [ ] Slowdown curves implemented (quadratic default).
  - [ ] Curves loaded from `progression_rules.json`.
  - [ ] Gain increments are always +0.1.
  Tests:
  - [ ] Sweet-spot tests (varying p_success).
  - [ ] Slowdown tests (skill 0/50/90 -> different gains).
  - [ ] Curve profile tests (linear vs quadratic).
  - [ ] Deterministic gain tests (seeded).
