- [ ] ID: TASK-M3-07
  Title: Skill-Hooks in Combat & Nodes (Integration)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/combat.py` (Erweiterung Hooks)`, `game/systems/skills.py`, `tests/integration/test_skill_hooks.py`
  DependsOn: TASK-M2-04, TASK-M3-06
  Notes:
  Bindung: bei erfolgreichem **Attack/Shoot/Cast** -> XP fuer passendes Skill; bei **Node-Gather** (kommt in M4) bereits Hooks vorsehen (No-op-Adapter).
  Acceptance:
  - [ ] Combat ruft Skill-Hooks mit deterministischem RNG auf.
  Tests:
  - [ ] Kampfsequenzen steigern erwartete Skills; keine Doppelcounts.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
