- [ ] ID: TASK-M2-AI-04
  Title: Faction System & AI-vs-AI Diplomacy
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/factions.py`, `tests/systems/test_factions.py`
  DependsOn: TASK-M2-AI-01, TASK-M2-07
  Notes:
  Load faction metadata and the diplomacy matrix from data/factions.json, covering all twelve factions listed in AI_DESIGN.md Section 2.
  Implement relation lookups so actors auto-engage hostile factions, respect tentative allies, and bias toward mutual enemies as detailed in docs/CROSS_REFERENCE_ANALYSIS.md Section 1.
  Wire call-for-help radii, aggro defaults, and mutual enemy bias hooks so guard and scout archetypes (TASK-M2-AI-03) can summon allies.
  Expose APIs for overworld FSM (TASK-M2-AI-06) and AI-versus-AI combat (TASK-M2-AI-07) to query faction stance, join encounters, and record aid.
  Acceptance:
  - [ ] Faction relations load and cache correctly from data/factions.json, including defaults and overrides.
  - [ ] Hostile relations trigger AI-versus-AI combat without player involvement.
  - [ ] Call-for-help pulls in same-faction allies within configured radius and respects mutual enemy bias.
  - [ ] Public API provides relation, hostility, and allegiance checks for other systems.
  Tests:
  - [ ] Relation lookup tests covering representative combinations across the 12 by 12 matrix.
  - [ ] AI-versus-AI engagement tests where Orc and Undead actors enter combat automatically.
  - [ ] Call-for-help regression tests ensuring ally enlistment follows radius and bias rules.
