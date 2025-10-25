- [ ] ID: TASK-M3-EXT-01
  Title: Container System Core (Data Model, State Machine, Interactions)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/containers.py`, `data/usables/*.json`, `tests/systems/test_containers.py`
  DependsOn: TASK-M3-02, TASK-M3-08
  Notes:
  Implement the container data schema from USABLES_AND_CONTAINERS.md Sections 1-2, including fields such as `id`, `type`, `name`, `sprite`, `placement`, `interact`, `ownership`, `durability`, and `fx`, with placement IDs (e.g., `map_x_y`) used for deterministic loot seeding.
  Build the container state machine tracking `locked`, `open`, `armed_trap`, `durability`, and `spawn_epoch`, with capacity constraints (`capacity`, `weight_max`, `allowed_tags`) enforced on inventory interactions.
  Provide serialization hooks for the new `data/usables/*.json` resources so pipelines can register container archetypes and map placements.
  Expose interaction entry points (open, close, inspect) for subsequent lock, trap, and ownership tasks to consume.
  Acceptance:
  - [ ] Container data model matches schema.
  - [ ] State machine transitions (locked->unlocked, closed->open).
  - [ ] Placement IDs used for deterministic loot.
  - [ ] Capacity/weight limits enforced.
  Tests:
  - [ ] State transition tests.
  - [ ] Capacity tests (slot/weight limits).
  - [ ] Placement ID seeding tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
  - docs/ITEMIZATION_DESIGN.md
