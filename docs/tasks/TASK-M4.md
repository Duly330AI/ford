- [ ] ID: TASK-M4
  Title: M4 — Nodes, Berufe & Crafting
  Status: Proposed
  Milestone: M4
  Created: 2025-10-24
  Notes: Nodes (ore/trees/herbs) with respawn, tool checks, and JSON-based crafting stations.
  Artifacts:
  - `data/recipes.json`
  - `game/systems/crafting.py`
  Acceptance:
  - [ ] Nodes spawn with respawn timers and drop expected materials
  - [ ] Crafting UI for Forge / Alchemy Table that consumes inputs and time

  Subtasks:
  - [ ] Define `data/recipes.json` schema and sample recipes
  - [ ] Implement node interactions and toolchecks
  - [ ] Crafting station UI + workflow (queue/timers)
