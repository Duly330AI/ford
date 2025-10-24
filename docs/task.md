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

## Move done tasks to COMPLETED_TASKS.md only if all subtasks are done.

- Task Template (copy-paste for new tasks):


```
- [ ] ID: TASK-###
                  Title: Short descriptive title
                  Status: Proposed / In Progress / Blocked / Done
                  Created: YYYY-MM-DD
                  Milestone: Mx – Milestone Name
                  Commit: <git-sha-if-applicable>
                  Notes: Detailed description, context, and any relevant links.
                  Artifacts: List of affected files or modules.
                  - [ ] Subtask or checklist item 1
                  - [ ] Subtask or checklist item 2

```
## Completed Tasks


---

## 🏁 Active Project Tasks (derived from docs/start.md)

Note: IDs are stable tokens for cross-references. Each task includes minimal acceptance criteria.

- [ ] ID: TASK-M1
    Title: M1 — Prozeduraler Dungeon, Spielerbewegung & Licht
    Status: Proposed
    Milestone: M1
    Created: 2025-10-24
    Notes: Implement BSP-based dungeon generation, collision for walls, player movement with dt and camera + light layer.
    Artifacts:
    - `game/main.py` (bootstrap)
    - `game/scenes/dungeon.py`
    - `game/util/tilemap.py`
    - `game/util/lighting.py`
    Acceptance:
    - [ ] BSP generator produces rooms+corridors saved to `data/maps/*.tmx` or an in-memory TileMap
    - [ ] Player moves 8-way using dt; collisions with walls (AABB) block movement
    - [ ] Camera follows player and light (torch) renders via Arcade lights
    - [ ] 60 FPS sustained at 1280×720 for a mid-size test map

    Subtasks:
    - [ ] Implement BSP dungeon generator (unit test: map connectivity)
    - [ ] Implement TileMap <-> Arcade TileLayer adapter
    - [ ] Player movement system (dt-based) + wall collisions
    - [ ] Light layer around player (torch) using Arcade lights

- [ ] ID: TASK-M2
    Title: M2 — Gegner & Kampfgrundlagen
    Status: Proposed
    Milestone: M2
    Created: 2025-10-24
    Notes: Implement three base enemy types with small FSMs, hitboxes, and feedback (particles/shake).
    Artifacts:
    - `game/entities/enemy.py`
    - `game/ecs/ai.py` or `game/systems/ai.py`
    Acceptance:
    - [ ] Three enemy archetypes (Melee, Ranged, Caster) with simple FSM states (idle/patrol/chase/attack)
    - [ ] Combat resolves hit/damage with particles and optional screen shake
    - [ ] Basic projectile entity for Ranged

    Subtasks:
    - [ ] Define enemy data entries in `data/monsters.json` (hp, speed, ai type, drops)
    - [ ] Implement FSM and simple pathing (grid-based or vector)
    - [ ] Implement hit/damage event + particle effect

- [ ] ID: TASK-M3
    Title: M3 — Skills, Loot & Inventory/Hotbar
    Status: Proposed
    Milestone: M3
    Created: 2025-10-24
    Notes: Usage-based skills, loot tables and working hotbar/inventory.
    Artifacts:
    - `game/systems/skills.py`
    - `data/loot_tables.json`, `data/items.json`, `data/skills.json`
    Acceptance:
    - [ ] Skills gain XP on usage and persist
    - [ ] Loot tables produce drops according to weights
    - [ ] Inventory + Hotbar (10 slots) with UI tooltips

    Subtasks:
    - [ ] Create `data/items.json` schema and sample items
    - [ ] Implement skill XP curve and cap (e.g., 100)
    - [ ] Implement inventory data model + hotbar UI

- [ ] ID: TASK-M4
    Title: M4 — Nodes, Berufe & Crafting
    Status: Proposed
    Milestone: M4
    Created: 2025-10-24
    Notes: Nodes (ore/trees/herbs) with respawn, tool checks, and JSON-based crafting stations.
    Artifacts:
    - `data/recipes.json`
    - `game/systems/crafting.py`
    Acceptance:
    - [ ] Nodes spawn with respawn timers and drop expected materials
    - [ ] Crafting UI for Forge / Alchemy Table that consumes inputs and time

    Subtasks:
    - [ ] Define `data/recipes.json` schema and sample recipes
    - [ ] Implement node interactions and toolchecks
    - [ ] Crafting station UI + workflow (queue/timers)

- [ ] ID: TASK-M5
    Title: M5 — Save & Load
    Status: Proposed
    Milestone: M5
    Created: 2025-10-24
    Notes: Persist player stats, skills, inventory, current dungeon seed.
    Artifacts:
    - `game/systems/save_load.py`
    Acceptance:
    - [ ] Save file written and loaded with deterministic seed restoration
    - [ ] Backwards-compatible small-versioning in save format

    Subtasks:
    - [ ] Implement JSON-based save format and load routine
    - [ ] Add quick-save / auto-save hooks

## 🔢 Data & Schema Tasks

- [ ] ID: TASK-DATA-1
    Title: Create initial data schemas and sample files
    Status: Proposed
    Notes: data/items.json, data/skills.json, data/recipes.json, data/monsters.json, data/loot_tables.json
    Subtasks:
    - [ ] Add `data/items.json` with 10 sample items (weapons, materials)
    - [ ] Add `data/skills.json` with skill definitions and XP curves
    - [ ] Add `data/recipes.json` sample recipes for Forge and Alchemy
    - [ ] Add `data/monsters.json` with 3 archetypes
    - [ ] Add `data/loot_tables.json` with at least 2 tables

## 🧱 Project scaffold & developer workflow

- [ ] ID: TASK-SCAFFOLD-1
    Title: Project scaffolding & run/test commands
    Status: Proposed
    Notes: Provide developer convenience files and commands so `poetry run python -m game.main` works per docs.
    Subtasks:
    - [ ] Add `pyproject.toml` with project metadata and dependencies (Python 3.13.5+, arcade>=3.x)
    - [ ] Add `README.md` with run instructions: `poetry install` and `poetry run python -m game.main` or `make run`
    - [ ] Add `Makefile` or `.venv`-aware run scripts if desired
    - [ ] Add `tests/` skeleton and a smoke test that imports `game.main`

## ⚙️ Tooling, linting & CI

- [ ] ID: TASK-TOOLING-1
    Title: Developer tooling (formatters, tests, CI)
    Status: Proposed
    Notes: Minimal recommended tools: `black`, `ruff`, `pytest`, `pre-commit`, GitHub Actions workflow.
    Subtasks:
    - [ ] Add `requirements-dev.txt` or `[tool.poetry.dev-dependencies]` entries
    - [ ] Add pre-commit config + sample hooks (black, ruff)
    - [ ] Add GitHub Actions workflow: `ci.yml` that runs tests and lint

## ✅ Quality tasks & performance

- [ ] ID: TASK-QUALITY-1
    Title: Performance budgeting & SpriteList culling
    Status: Proposed
    Notes: Ensure 2000+ entities doesn't drop FPS below 60 using culling & SpriteList
    Subtasks:
    - [ ] Create a performance test map that spawns 2000 entities and measure FPS
    - [ ] Implement and benchmark SpriteList culling strategy

## ✨ Bonus / Nice-to-have

- [ ] ID: TASK-BONUS-1
    Title: Visual polish (vignette, scanlines, crit popups)
    Status: Proposed
    Subtasks:
    - [ ] Add shader vignette / scanline post-process effect
    - [ ] Add floating crit number popups with small pooling system

---

## How to use this file
- Add new tasks under the appropriate section. Keep IDs unique and stable.
- Move fully completed tasks to the Completed Tasks section (bottom) and set `Status: Done`.

```