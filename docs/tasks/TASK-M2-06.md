- [ ] ID: TASK-M2-06
  Title: Overworld-FSM (idle/patrol/chase/attack) & Engagement
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/ai_overworld.py`, `tests/systems/test_ai_overworld.py`
  DependsOn: TASK-M1-04, TASK-M1-05, TASK-M2-11
  Notes:
  Gegner patrouillieren (Waypoints), entdecken den Spieler via **Sichtkegel/Radius + LOS**. Engagement-Trigger: Wechsel in **CombatState** mit Initiative-Roll.
  Acceptance:
  - [ ] Verlaesslicher Wechsel in Kampfmodus bei Sichtkontakt.
  - [ ] Kein "Durch-Waende-Erkennen" (LOS prueft `walls`).
  Tests:
  - [ ] Entdeckt ja/nein fuer Geometrien, deterministische Pfade.
