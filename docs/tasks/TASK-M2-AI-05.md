- [ ] ID: TASK-M2-AI-05
  Title: AI Blackboard Context System
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/ai_blackboard.py`, `tests/systems/test_ai_blackboard.py`
  DependsOn: TASK-M2-AI-01
  Notes:
  Create a per-actor blackboard container aligned with data/blackboard_keys.json and AI_DESIGN.md Sections 7 and 8.
  Persist threat maps, focus targets, ally distress signals, last hurt sources, ammunition, mana, recovery timers, position, line-of-sight, cover scores, incoming threat, and boss phase markers.
  Provide deterministic update hooks each perception tick so utility scoring, tactics, and overworld FSM consume consistent snapshots.
  Offer lightweight query helpers (`get`, `set`, `has`) for AI components and debug tooling described in docs/CROSS_REFERENCE_ANALYSIS.md Section 1.
  Acceptance:
  - [ ] Blackboard keys mirror data/blackboard_keys.json, including optional boss phase markers.
  - [ ] Update cycle persists threat maps with decay while refreshing perception-driven fields each tick.
  - [ ] Utility scoring (TASK-M2-AI-02) and tactics (TASK-M2-AI-03) read from the blackboard without direct system coupling.
  Tests:
  - [ ] CRUD tests confirming default values, typed updates, and optional key handling.
  - [ ] Threat map update tests verifying decay and insertion order with seeded data.
  - [ ] Line-of-sight snapshot tests ensuring perception writes propagate correctly.
