- [ ] ID: TASK-M2-AI
  Title: AI System (Utility-AI, Factions, Behaviors, Overworld FSM)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `docs/AI_SYSTEM_OVERVIEW.md`
  DependsOn: TASK-M2-06, TASK-M2-09
  Notes:
  Reference AI_DESIGN.md Sections 1-14 and docs/CROSS_REFERENCE_ANALYSIS.md Section 1 to restate the intended AI pipeline, data flows, and QA hooks.
  Summarize how the Utility-AI approach replaces the behavior tree fallback discussed in AI_DESIGN.md Section 4 and call out key data providers (behaviors.json, tactics.json, factions.json, blackboard_keys.json).
  Break down the milestone into TASK-M2-AI-01..07 covering perception, utility scoring, tactics integration, faction diplomacy, blackboard state, overworld FSM, and AI-versus-AI encounters.
  Document coordination points with core gameplay milestones (TASK-M2-04 combat core, TASK-M2-06 overworld FSM, TASK-M2-09 combat AI integration) so contributors understand shared contracts.
  Acceptance:
  - [ ] TASK-M2-AI-01..07 reach Status: Done and are referenced from this milestone summary.
  - [ ] Utility-AI pipeline, diplomacy rules, and overworld FSM are documented in docs/AI_SYSTEM_OVERVIEW.md in line with AI_DESIGN.md Sections 3-9.
  - [ ] Seeded headless integration suites demonstrate working single-faction and multi-faction encounters.
  Tests:
  - [ ] `tests/integration/test_ai_system.py::test_single_faction_encounter` (seeded utility pipeline smoke).
  - [ ] `tests/integration/test_ai_system.py::test_multi_faction_battle` (seeded three-faction scenario).
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
