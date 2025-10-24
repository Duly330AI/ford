- [ ] ID: TASK-M4-07
  Title: Beruf-Skill-Hooks & Boni (mining/woodcutting/alchemy/smithing)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/skills.py` (Erweiterung)`, `tests/integration/test_profession_hooks.py`
  DependsOn: TASK-M3-06, TASK-M3-07, TASK-M4-02, TASK-M4-06
  Notes:
  Beispiele (datengetrieben):
        - mining/woodcutting: **extra_yield_chance** pro 10 Skill, **reduced_time%**.
        - smithing: **success_bonus**, **crit_bonus** beim Craften.
        - alchemy: **potion_potency%**, **fail_returns**-Bonus.
  Acceptance:
  - [ ] Hooks feuern deterministisch bei Gather/Craft.
  Tests:
  - [ ] Seeds: Erwartete Bonus-Ereignisse/Skalierung.
