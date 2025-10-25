- [ ] ID: TASK-M2-DICE-01-Dice-System
  Title: Wuerfelsystem (d20/dX, Advantage/Disadvantage, Tabellen)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/dice.py`, `tests/systems/test_dice.py`
  DependsOn: -
  Notes:
  Allgemeines Wuerfelmodul: `roll("1d20+3")`, Mehrfachwuerfe, Advantage/Disadvantage, Seedbarer RNG. Utility fuer Schwellen-Checks (z. B. `d20 + ATK >= TN`).
  Acceptance:
  - [ ] Parser fuer `NdM[+/-K]`, Advantage/Disadvantage.
  - [ ] Reine Funktion, injizierbarer RNG.
  Tests:
  - [ ] Determinismus: gleicher Seed -> gleiche Sequenz.
  - [ ] Verteilungen (Smoke): Mittelwert im erwarteten Bereich.
  References:
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
