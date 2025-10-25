- [ ] ID: TASK-M2-09
  Title: Combat-KI (Heuristiken fuer Melee/Ranged/Caster)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/ai_combat.py`, `tests/systems/test_ai_combat.py`
  DependsOn: TASK-M2-04, TASK-M2-08
  Notes:
  Einfache turn-basierte Entscheidung:
        - **Melee**: gehe zu Melee-Range, `Attack`; nutze `Guard`, wenn HP niedrig.
        - **Ranged**: halte Abstand (kitedistance), `Shoot`; reposition wenn zu nah.
        - **Caster**: `Cast` (Stun/DoT) nach Prioritaet; Mana-Verwaltung; fallback `Attack`.
  Acceptance:
  - [ ] Entscheidungen liefern gueltige Intents (Reichweite/LOS geprueft).
  Tests:
  - [ ] Szenarien pro Archetyp (seeded): erwartete Intent-Sequenzen.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
