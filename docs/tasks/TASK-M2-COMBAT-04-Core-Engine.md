- [ ] ID: TASK-M2-COMBAT-04-Core-Engine
  Title: Combat-Core (Intents -> Outcomes)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/combat.py`, `tests/systems/test_combat_core.py`
  DependsOn: TASK-M2-01, TASK-M2-02, TASK-M2-03
  Notes:
  Reine Logik, keine Arcade:
        - **Intents**: `Move(tile)`, `Attack(target)`, `Shoot(target)`, `Cast(spell,target)`, `UseItem`, `Wait`.
        - **Kosten**: 1 **Hauptaktion** + **Schritte** (z. B. 3 Tiles) pro Zug.
        - **Output**: `Outcome`-Events (Hit/Miss/Crit/Block, Damage, ApplyEffect, Death, Log).
        - **Death Handling**: Entfernt Entity, triggert Loot-Hooks (M3 vorbereitend).
  Acceptance:
  - [ ] Eine komplette Runde sequenziell abbildbar (Spieler+3 Gegner).
  - [ ] Ungueltige Intents werden abgewiesen (out-of-range, OOA, OOM).
  Tests:
  - [ ] Simulierter Kampf (Player vs. 3 Archetypen) deterministisch.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/QUEST_SYSTEM.md
