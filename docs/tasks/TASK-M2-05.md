- [ ] ID: TASK-M2-05
  Title: Status-Effekte (Buffs/Debuffs/DoT/CC)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/effects.py`, `data/effects.json`, `tests/systems/test_effects.py`
  DependsOn: TASK-M2-04
  Notes:
  Generisches Effektmodell: `on_apply`, `on_tick`, `on_expire`, Stacks/MaxStacks, Dauer in **Runden**. Beispiele: **Bleed**, **Poison**, **Stun**, **Guard(+DEF)**, **Haste(+Move)**, **Evade(+Dodge)**.
  Acceptance:
  - [ ] Ticks am Rundenanfang/-ende (konfigurierbar).
  - [ ] Stacking-Regeln: additiv/refresh.
  Tests:
  - [ ] DoT-Stacks, Stun ueberspringt Aktionen, Buff wirkt auf Formeln.
