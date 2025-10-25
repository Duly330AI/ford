- [ ] ID: TASK-M3-EXT-05-Bash-Mechanics
  Title: Bash Mechanics (STR Check, Durability, Noise)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/bash.py`, `tests/systems/test_bash.py`
  DependsOn: TASK-M2-02, TASK-M3-EXT-01
  Notes:
  Implement bash checks using the formula `atk = STR + weapon_dmg + tactics * 0.2` and `P = clamp(0.02, 0.5 + (atk - bash_dc)/200, 0.95)` from USABLES_AND_CONTAINERS.md Section 3-4, consuming a Main Action in combat.
  Reduce container durability (`durability.hp`) on success and spill loot when durability reaches zero.
  Generate noise on failure (e.g., `noise += 0.2`) that can alert nearby enemies via the overworld AI (TASK-M2-AI-06).
  Acceptance:
  - [ ] Bash checks use STR + weapon + tactics.
  - [ ] Durability decreases on success.
  - [ ] Noise raises on failure (can trigger enemy aggro).
  - [ ] Container breaks at 0 durability.
  Tests:
  - [ ] Bash success/fail tests (seeded).
  - [ ] Durability reduction tests.
  - [ ] Noise tests (aggro trigger cross-ref TASK-M2-AI-06).
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
