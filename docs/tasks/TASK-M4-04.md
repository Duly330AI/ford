- [ ] ID: TASK-M4-04
  Title: Node-Datenmodell (Depletion, Respawn, Yield)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/nodes.py`, `tests/systems/test_nodes_model.py`
  DependsOn: TASK-M4-01
  Notes:
  Node-State: `id`, `type`, `tier`, `pos(tile)`, `depleted(bool)`, `respawn_at(time)`. `gather(tool, skill, rng)` -> prueft Tool, wuerfelt yield gemaess Tabelle/Range, setzt Depletion + `respawn_at`.
  Acceptance:
  - [ ] Yield im Range, Depletion korrekt, respawn nach Zeit.
  Tests:
  - [ ] Tool-Fehlerfaelle, Skill-XP-Hooks, Respawn-Simulation.
