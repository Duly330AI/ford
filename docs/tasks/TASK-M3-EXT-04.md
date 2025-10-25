- [ ] ID: TASK-M3-EXT-04
  Title: Detect Hidden Skill (Passive & Active Search)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/detect_hidden.py`, `tests/systems/test_detect_hidden.py`
  DependsOn: TASK-M3-06, TASK-M3-EXT-01
  Notes:
  Implement passive detect hidden checks during container inspection, rolling based on the actor's detect_hidden skill to surface hints such as "scratches near lock" per USABLES_AND_CONTAINERS.md Section 3-4.
  Provide an Active Search main action that boosts detection for N turns, raising disarm success chances by +0.05 to +0.15 as specified and revealing hidden compartments when successful.
  Feed detection results into trap and lock workflows so TASK-M3-EXT-03 can adjust disarm probabilities and containers can expose hidden loot pools.
  Acceptance:
  - [ ] Passive detection rolls on inspect (skill-based).
  - [ ] Active Search grants detection bonus for N turns.
  - [ ] Hints displayed in tooltips.
  - [ ] Hidden compartments revealed (extra loot).
  Tests:
  - [ ] Passive detection tests (seeded).
  - [ ] Active Search duration tests.
  - [ ] Bonus application tests (disarm chance).
