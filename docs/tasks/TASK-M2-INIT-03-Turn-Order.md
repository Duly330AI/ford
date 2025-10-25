- [ ] ID: TASK-M2-03
  Title: Initiative & Turn-Order
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/initiative.py`, `tests/systems/test_initiative.py`
  DependsOn: TASK-M2-01, TASK-M2-02
  Notes:
  `CombatState`: Teilnehmer, Runde, Zugindex. `roll_initiative()` mit Tie-Break (DEX, dann RNG).
  Acceptance:
  - [ ] Stabile Reihenfolge, Runde++ nach letztem Teilnehmer.
  Tests:
  - [ ] Ties korrekt; Wiederholbarkeit mit Seed.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
