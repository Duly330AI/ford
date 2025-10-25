- [ ] ID: TASK-M2-19
  Title: Encounter Bubble & Escape/Disengage Mechanics
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/engagement.py`, `tests/systems/test_engagement.py`
  DependsOn: TASK-M2-06, TASK-M2-08, TASK-M2-AI-06
  Notes:
  Implement encounter bubble detection with a default 12-tile radius, requiring line-of-sight to enlist actors into combat per GAMEPLAY_ADDENDUM_UO.md Section C and ARCHITECTURE_UO_ADDENDUM.md Section "Engagement & Zeit".
  Queue late entrants so enemies crossing into the bubble join at the next round start, maintaining deterministic initiative ordering.
  Add escape logic that checks for zero enemy LOS and a minimum `leash_break` distance (10 tiles default) for a full round, optionally boosted by a player Flee action that grants additional leash margin and evade%.
  Surface engagement state transitions to the overworld FSM (TASK-M2-AI-06) and combat systems so UI/AI can react to join/escape events.
  Acceptance:
  - [ ] Encounter bubble (12 tiles, LOS) correctly identifies combatants.
  - [ ] New enemies join at round start (not mid-round).
  - [ ] Escape countdown triggers correctly (LOS-free + distance).
  - [ ] Flee action grants +leash_margin, +evade%.
  Tests:
  - [ ] Bubble tests (LOS + radius).
  - [ ] Join timing tests (mid-round vs round-start).
  - [ ] Escape countdown tests (seeded, timekeeper mock).
  - [ ] Flee action tests (modifiers applied).
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
