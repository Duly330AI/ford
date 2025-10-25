- [ ] ID: TASK-M3-EXT-06
  Title: Ownership & Trespass System (Crime, Faction Reactions)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/ownership.py`, `tests/systems/test_ownership.py`
  DependsOn: TASK-M3-EXT-01, TASK-M2-AI-04
  Notes:
  Add ownership metadata to containers (`ownership.faction`, `ownership.trespass`) and enforce trespass checks before allowing interactions, referencing USABLES_AND_CONTAINERS.md Section 7.
  Generate crime events when trespass containers are opened or looted, and route reactions to the faction system (TASK-M2-AI-04) for future guard/AI responses.
  Display UI warnings indicating faction ownership so players understand consequences.
  Acceptance:
  - [ ] Ownership field checked on interact.
  - [ ] Crime events generated for trespass.
  - [ ] UI warning displays before opening.
  - [ ] Faction reactions stub (extensible for guards).
  Tests:
  - [ ] Ownership check tests.
  - [ ] Crime event generation tests.
  - [ ] UI warning tests (mock).
