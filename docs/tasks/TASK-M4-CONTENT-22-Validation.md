- [ ] ID: TASK-M4-22
  Title: Container Respawn System (Daily/Interval/None)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/container_respawn.py`, `tests/systems/test_container_respawn.py`
  DependsOn: TASK-M3-EXT-01, TASK-M3-08
  Notes:
  Implement respawn modes `none`, `daily`, and `interval` per USABLES_AND_CONTAINERS.md Section 5, starting timers on first open or when emptied based on configuration.
  Regenerate loot on respawn using the associated `loot_table`, supporting deterministic or re-seeded behavior.
  Respect the `preserve_unlooted` flag to carry over unclaimed items while adding newly rolled loot.
  Acceptance:
  - [ ] Respawn modes (none/daily/interval) work correctly.
  - [ ] Timer starts on first open or empty.
  - [ ] Loot regenerates from table on respawn.
  - [ ] `preserve_unlooted` works (old items + new items).
  Tests:
  - [ ] Respawn timing tests (timekeeper mock).
  - [ ] Loot regeneration tests (seeded).
  - [ ] Preserve_unlooted tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
  - docs/ITEMIZATION_DESIGN.md
