- [ ] ID: TASK-M2-20
  Title: Dodge Mechanics (Overworld iFrames vs Combat Dash+Evade)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/dodge.py`, `tests/systems/test_dodge.py`
  DependsOn: TASK-M1-05, TASK-M2-04
  Notes:
  Implement overworld dodge rolls triggered via the player controller (spacebar), consuming stamina defined in `combat_rules.json.dodge`, granting 0.35s invulnerability frames, moving one tile, and enforcing a short cooldown.
  Add a combat dodge main action that consumes the actor's turn, checks recovery/immobilized status, applies a one-tile dash, and grants an evade% buff lasting until the actor's turn ends as detailed in GAMEPLAY_ADDENDUM_UO.md Section D.
  Share cooldown and stamina logic between overworld and combat contexts where appropriate while keeping separate timing and buff application.
  Provide hooks so AI or scripted encounters can reference dodge availability and cooldown state.
  Acceptance:
  - [ ] Overworld dodge grants iFrames (brief invincibility).
  - [ ] Combat dodge grants +evade% until turn end.
  - [ ] Both cost Stamina correctly.
  - [ ] Combat dodge is main action (blocks other actions).
  Tests:
  - [ ] Overworld dodge iFrames tests (collision immunity).
  - [ ] Combat dodge evade bonus tests.
  - [ ] Stamina cost tests.
  - [ ] Action blocking tests (combat dodge).
