- [ ] ID: TASK-M4-ACCEPTANCE-24-Criteria
  Title: Crafting Queue Pause During Combat (Timekeeper Integration)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/util/timekeeper.py`, `tests/systems/test_crafting_pause.py`
  DependsOn: TASK-M4-02, TASK-M2-04
  Notes:
  Integrate combat state signals with the timekeeper so crafting queue ticks pause when combat begins and resume afterward, following ARCHITECTURE_UO_ADDENDUM.md Section Engagement & Zeit and GAMEPLAY_ADDENDUM_UO.md Section C.
  Mark completions that occur during combat without triggering UI spam, allowing players to collect items once combat ends.
  Ensure queue state persists and resumes accurately after pauses, respecting crafting duration progress.
  Acceptance:
  - [ ] Crafting pauses on combat start.
  - [ ] Crafting resumes on combat end.
  - [ ] Completions marked (no UI spam during combat).
  - [ ] Collectible items available post-combat.
  Tests:
  - [ ] Pause/resume tests (timekeeper mock).
  - [ ] Completion marking tests.
  - [ ] Post-combat collection tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
