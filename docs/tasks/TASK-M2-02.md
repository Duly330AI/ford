- [ ] ID: TASK-M2-02
  Title: Ableitbare Werte & Formeln (ATK/DEF/CRIT/EVA/RES)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/stats.py`, `data/combat_rules.json`, `tests/systems/test_stats.py`
  DependsOn: TASK-M2-01
  Notes:
  Datengetriebene Formeln:
        - **To-Hit** Standard: `d20 + ATK >= 10 + DEF` (konfigurierbar).
        - **Crit**: Basis 5% (nat20) + Mod; **Block/Parry**: DEF-basierter Wurf.
        - **Damage**: `(weapon dice + mods) * (1 - resist[type])`, min 1.
  Acceptance:
  - [ ] Regeln aus `data/combat_rules.json` ladbar/pruefbar.
  - [ ] Ableitungen reproduzierbar & ohne Arcade-Abhaengigkeit.
  Tests:
  - [ ] Beispielrechnungen (Hit/Miss/Crit/Block) gegen feste Seeds.
  - [ ] Grenzfaelle: volle Resistenz (100%), negative Mods.
