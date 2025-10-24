# 🗂 FORD – Master Task Index

---

## 📜 Maintenance Guidelines

- New tasks: Add directly to the appropriate chunk and link here under “Active Tasks.”
- Completed tasks: Set to `Status: Done` and move to the bottom “Completed Tasks” section.
- Numbering: Sequential; do not fill gaps—IDs remain stable.
- Consistency: Make changes to titles or descriptions in the chunk, not here.

---


## 🔧 Task Management

## Critical: Use the templates below to ensure consistency.

## Mark [D] ID: TASK-### for done tasks.

## Mark [A] for active/in-progress tasks.

## Mark [D] for done subtasks.

## Move done tasks to the bottom of the list only if all subtasks are done.

## Completed Tasks



---

## Task Index

This file is an index. Detailed task descriptions live in `docs/tasks/*.md` per the repository pre-commit rules.

Active tasks (quick links):

- [TASK-M1 — M1: Prozeduraler Dungeon, Spielerbewegung & Licht](./tasks/TASK-M1.md)
- [TASK-M2 — M2: Gegner & Kampfgrundlagen](./tasks/TASK-M2.md)
- [TASK-M3 — M3: Skills, Loot & Inventory/Hotbar](./tasks/TASK-M3.md)
- [TASK-M4 — M4: Nodes, Berufe & Crafting](./tasks/TASK-M4.md)
- [TASK-M5 — M5: Save & Load](./tasks/TASK-M5.md)
- [TASK-DATA-1 — Create initial data schemas and sample files](./tasks/TASK-DATA-1.md)
- [TASK-SCAFFOLD-1 — Project scaffolding & run/test commands](./tasks/TASK-SCAFFOLD-1.md)
- [TASK-TOOLING-1 — Developer tooling (formatters, tests, CI)](./tasks/TASK-TOOLING-1.md)
- [TASK-QUALITY-1 — Performance budgeting & SpriteList culling](./tasks/TASK-QUALITY-1.md)
- [TASK-BONUS-1 — Visual polish (vignette, scanlines, crit popups)](./tasks/TASK-BONUS-1.md)

Completed tasks:

- [D] ID: TASK-DOC-AUDIT
                  Title: Documentation audit & recommendations
                  Status: Done
                  Created: 2025-10-24
                  Milestone: DOC - Quality Improvements
                  Commit: -
                  Notes: Reviewed docs/tasks/ inventory; captured findings and follow-up suggestions in Codex summary.
                  Artifacts: docs/tasks/*
                  - [D] Inventory existing TASK docs
                  - [D] Document findings & suggestions

- See individual task files and Git history for completed work.

Usage:

- Add new detailed tasks under `docs/tasks/` as `TASK-<id>.md` and link them here.


- Task Template (for done tasks):
- [D] ID: TASK-###
                  Title: Short descriptive title
                  Status: Proposed / In Progress / Blocked / Done
                  Created: 2025-10-24
                  Milestone: Mx – Milestone Name
                  Commit: <git-sha-if-applicable>
                  Notes: Detailed description, context, and any relevant links.
                  Artifacts: List of affected files or modules.
                  - [D] Subtask or checklist item 1
                  - [D] Subtask or checklist item 2

```
