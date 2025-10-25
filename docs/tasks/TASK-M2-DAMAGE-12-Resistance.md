- [ ] ID: TASK-M2-12
  Title: Schadenstypen & Resistenzen
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/damage.py`, `data/combat_rules.json` (Erweiterung)`, `tests/systems/test_damage.py`
  DependsOn: TASK-M2-02, TASK-M2-05
  Notes:
  Typen: **physical**, **piercing**, **fire**, **ice**, **poison**, **arcane**. Resistenzen 0-1. Optional: Schwachstellen.
  Acceptance:
  - [ ] Resistenzen korrekt angewendet; min-Schaden 1.
  Tests:
  - [ ] Matrixtest ueber TypxResistenz; DoT + Resistenz-Kombinationen.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
