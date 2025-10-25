- [ ] ID: TASK-M2-AI-01
  Title: Perception & Threat Memory System
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/ai_perception.py`, `tests/systems/test_ai_perception.py`
  DependsOn: TASK-M1-04, TASK-M2-11
  Notes:
  Implement line-of-sight perception using the Bresenham ray approach outlined in AI_DESIGN.md Section 3 and reinforced in docs/CROSS_REFERENCE_ANALYSIS.md Section 1.
  Maintain a per-actor threat ledger with configurable decay, threat caps, and prioritization heuristics so noise and visibility scores (0 to 1) influence targeting decisions.
  Track last-seen positions, investigation timers, and visibility classifications to support overworld investigate behavior and combat re-engagement.
  Surface perception snapshots to the blackboard schema defined in data/blackboard_keys.json for downstream systems.
  Acceptance:
  - [ ] LOS checks respect wall and obstacle data produced by TASK-M1-04 and maintain parity with AI_DESIGN.md Section 3 examples.
  - [ ] Threat memory decays deterministically over time without oscillation once targets leave vision.
  - [ ] Last-seen positions persist for the configured number of turns and drive investigate triggers.
  - [ ] Noise visibility scores alter threat weighting according to design coefficients.
  Tests:
  - [ ] LOS unit tests covering straight, diagonal, and obstructed paths.
  - [ ] Threat decay tests exercising multiple seeds and ensuring monotonic decay toward zero.
  - [ ] Multi-target prioritization tests asserting deterministic ordering with shared vision snapshots.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
