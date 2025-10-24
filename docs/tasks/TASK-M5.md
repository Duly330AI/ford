- [ ] ID: TASK-M5
  Title: M5 — Save & Load
  Status: Proposed
  Milestone: M5
  Created: 2025-10-24
  Notes: Persist player stats, skills, inventory, current dungeon seed.
  Artifacts:
  - `game/systems/save_load.py`
  Acceptance:
  - Save file written and loaded with deterministic seed restoration
  - Backwards-compatible small-versioning in save format

  Subtasks:
  - Implement JSON-based save format and load routine
  - Add quick-save / auto-save hooks
