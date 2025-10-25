- [ ] ID: TASK-M3-EQUIPMENT-06-Slots
  Title: Skill-System (usage-based XP, Cap, Level-Boni)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/skills.py`, `data/skills.json`, `tests/systems/test_skills.py`
  DependsOn: TASK-M3-01
  Notes:
  Skills: `swords, archery, sorcery, lockpicking, mining, woodcutting, alchemy, smithing, healing`. XP-Kurven datengetrieben (z. B. `xp_for_level(n)`), Cap 100. **Hooks**: On-Hit (swords/archery/sorcery), On-Craft (alchemy/smithing), On-Gather (mining/woodcutting), On-Use (healing).
  Acceptance:
  - [ ] Nutzung erhoeht XP gemaess Kurve; Level-Up triggert Events.
  - [ ] Boni wirken auf Stats/Regeln (z. B. +ATK aus swords, +chance auf extra yield beim mining).
  Tests:
  - [ ] XP-Verteilung, Cap, Level-Boni, Hook-Aufrufe.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
