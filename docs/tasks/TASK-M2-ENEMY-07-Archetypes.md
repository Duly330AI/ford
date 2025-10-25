- [ ] ID: TASK-M2-07
  Title: Gegner-Archetypen & Daten
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/entities/enemy.py`, `data/monsters.json`, `tests/entities/test_enemy_data.py`
  DependsOn: TASK-M2-02
  Notes:
  Drei Archetypen:
        - **Melee**: hoher ATK/HP, Nahkampfreichweite 1, Faehigkeit "Guard".
        - **Ranged**: mittlerer ATK, Reichweite 6-8 Tiles, Faehigkeit "Kitedistance".
        - **Caster**: niedriger ATK, Zauber (DoT/Stun), Mana/Kosten.
  Acceptance:
  - [ ] Daten validieren gegen Schema (Stats, Resistenzen, Skills).
  Tests:
  - [ ] Laden & Instanziieren, Basiswerte korrekt, Resistenzen greifen.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
