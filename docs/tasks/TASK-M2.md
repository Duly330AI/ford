- [ ] ID: TASK-M2
  Title: M2 — Gegner & Kampfgrundlagen
  Status: Proposed
  Milestone: M2
  Created: 2025-10-24
  Notes: Implement three base enemy types with small FSMs, hitboxes, and feedback (particles/shake).
  Artifacts:
  - `game/entities/enemy.py`
  - `game/ecs/ai.py` or `game/systems/ai.py`
  Acceptance:
  - [ ] Three enemy archetypes (Melee, Ranged, Caster) with simple FSM states (idle/patrol/chase/attack)
  - [ ] Combat resolves hit/damage with particles and optional screen shake
  - [ ] Basic projectile entity for Ranged

  Subtasks:
  - [ ] Define enemy data entries in `data/monsters.json` (hp, speed, ai type, drops)
  - [ ] Implement FSM and simple pathing (grid-based or vector)
  - [ ] Implement hit/damage event + particle effect
