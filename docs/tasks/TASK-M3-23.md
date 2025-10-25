- [ ] ID: TASK-M3-23
  Title: Skill Lock System (Up/Down/Lock, Auto-Drop at Total Cap)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/skills.py`, `tests/systems/test_skill_locks.py`
  DependsOn: TASK-M3-06
  Notes:
  Introduce per-skill lock states (`UP`, `DOWN`, `LOCK`) persisted alongside skill ranks so players can control gain/drop behavior as outlined in GAMEPLAY.md Section 7 and UI_SPEC_UO_STYLE.md Section 4.
  Enforce the total skill cap from `progression_rules.json.caps.total_skills` (700.0 default), auto-dropping the lowest `DOWN` skill by 0.1 when a capped character gains on an `UP` skill.
  Provide safe handling for the edge case where no skills are set to `DOWN`, blocking the gain and surfacing a UI-friendly reason string for later UI tasks.
  Ensure lock icons or states remain accessible for UI rendering (cross-ref TASK-M6-UI-05) and persist through save/load.
  Acceptance:
  - [ ] Lock states (UP/DOWN/LOCK) stored per skill.
  - [ ] Total cap enforced (auto-drop on gain if at cap).
  - [ ] Lowest DOWN skill selected for drop.
  - [ ] Lock state persists in save/load.
  Tests:
  - [ ] Lock state CRUD tests.
  - [ ] Auto-drop logic tests (at cap, multiple DOWN skills).
  - [ ] Edge case: no DOWN skills (gain blocked).
