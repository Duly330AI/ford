- [ ] ID: TASK-M2-FEEDBACK-13-Adapter
  Title: Trefferfeedback-Adapter (Particles/Shake Hook)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/feedback.py`, `game/scenes/dungeon.py`, `tests/smoke/test_feedback_import.py`
  DependsOn: TASK-M2-04
  Notes:
  Kleine Adapter-API: `emit_hit_particles(pos, type)`, `screen_shake(intensity, ms)`. Scene implementiert visuell, Systems rufen **nur** Adapter auf.
  Acceptance:
  - [ ] Systems-Calls sind No-ops in Tests (kein GL).
  Tests:
  - [ ] Importierbar; Adapter funktionsfaehig als Stub.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
