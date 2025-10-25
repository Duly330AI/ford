- [ ] ID: TASK-M2-AI-03
  Title: Tactics & Behavior Archetypes Integration
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/ai_tactics.py`, `tests/systems/test_ai_tactics.py`
  DependsOn: TASK-M2-AI-02, TASK-M2-07
  Notes:
  Load archetype definitions from data/behaviors.json and action modifiers from data/tactics.json as prescribed in AI_DESIGN.md Sections 4 and 7.
  Implement behavior adapters for melee, ranged, caster, guardian, brute, scout, and boss archetypes so their guard, kite, call-for-help, berserk, and phase logic match the design document.
  Integrate guard radius checks, flee thresholds, ammo-aware swaps, and phase triggers, ensuring outputs feed utility scores and overworld FSM hooks.
  Coordinate with TASK-M2-AI-04 for call-for-help diplomacy and with TASK-M2-AI-06 for overworld engage state transitions.
  Acceptance:
  - [ ] All seven archetypes execute their prescribed tactic branches using behaviors.json and tactics.json inputs.
  - [ ] Ranged archetypes maintain configured kite distances and swap behavior when ammo is low.
  - [ ] Guardian and melee archetypes guard allies within the specified radius and respect body block flags.
  - [ ] Call-for-help signals propagate to the faction system specified in TASK-M2-AI-04.
  Tests:
  - [ ] Archetype tactic fixtures validating melee, ranged, caster, guardian, brute, scout, and boss flows.
  - [ ] Kiting and flee behavior tests covering distance thresholds and stamina edges.
  - [ ] Guard and call-for-help regression tests verifying ally selection and signal emission.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/INPUT_AND_REBIND.md
