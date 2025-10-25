- [ ] ID: TASK-M2-AI-02-Utility-Scoring
  Title: Utility-AI Scoring Engine (Target & Action Selection)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/ai_utility.py`, `tests/systems/test_ai_utility.py`
  DependsOn: TASK-M2-AI-01
  Notes:
  Build the utility-scoring pipeline described in AI_DESIGN.md Sections 4 and 5, combining threat, distance, health, role bias, and mutual enemy weighting into a composite target score.
  Consume data/tactics.json to compute action utilities per archetype, including distance preferences, ally role modifiers, and hit point thresholds highlighted in docs/CROSS_REFERENCE_ANALYSIS.md Section 1.
  Introduce an e-greedy action picker (5 to 10 percent exploration) to avoid deterministic loops while respecting seeded RNG.
  Emit scoring telemetry hooks so downstream tactics and QA harnesses can assert rankings during tests.
  Acceptance:
  - [ ] Target selection reflects threat, distance, health, role, and mutual enemy weights from AI_DESIGN.md Section 4.
  - [ ] Action scores load from data/tactics.json and respect per-action modifiers.
  - [ ] E-greedy exploration uses seeded RNG and avoids repeating the same decision loop endlessly.
  - [ ] Scoring telemetry exposes the ranked list for debugging and QA harnesses.
  Tests:
  - [ ] Deterministic scoring tests comparing computed weights against known fixtures.
  - [ ] E-greedy randomness tests verifying exploration frequency with fixed seeds.
  - [ ] Scenario regression tests ensuring consistent target and action ordering for archived battle states.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
