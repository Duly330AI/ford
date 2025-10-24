# FORD • Copilot Instructions

> Single-Player 2D Dungeon Crawler in **Python + Arcade** (Roguelike Pixel 16×16→64px).  
> Goal: **clean architecture**, **data-driven content**, **tests for everything**, **60 FPS feel**, **zero custom art** (CC0 placeholders only).

---

## TL;DR (Golden Rules)

1. **Always ship tests** with every code change (`pytest`). No tests → no merge.  
2. **Keep logic testable**: core systems (skills, loot, crafting, AI) must not depend on Arcade/OpenGL.  
3. **Follow style**: Ruff + Black clean; type hints everywhere; small functions; no God objects.  
4. **Data-driven**: JSON for items/skills/recipes/monsters/loot-tables must be validated at load time.  
5. **Pixel-perfect**: integer scaling, no sub-pixel movement; stable 60 FPS feel.  
6. **Git hygiene**: feature branches, Conventional Commits, small PRs, green CI before merge.  
7. **No new artwork**: use CC0 placeholders; record sources in `ATTRIBUTIONS.md`.  
8. **Determinism for tests**: use `PYTHONHASHSEED=0` and seeded RNG for logic.
9. **Document tasks**: keep `docs/task.md` updated with all active and completed tasks.

---

## Project Constraints (enforced by Copilot)

- **Python**: 3.13.5+  
- **Arcade**: ≥ 3.x  
- **Package**: Poetry  
- **Resolution**: 1920×1080, integer scale (16px tiles upscale 4× → 64px).  
- **Layers**: ground, walls (collidable), decals, light-blockers, entities.  
- **Rendering**: SpriteList per layer + Arcade lights & particles.  
- **Physics**: AABB, dt movement (8-way), no slopes.  
- **Combat**: **Turn-based** resolution (dice-driven attack/defense/effects).  
- **Systems**: skills (usage-based), professions/nodes, crafting (JSON recipes), loot tables, save/load.

---

## Local Workflow (VS Code)

- Use provided `.vscode`:
  - **Run**: `Run FORD` (launches `python -m game.main`)
  - **Tasks**: `poetry: install`, `run`, `tests`
- Formatter/linter run on save (Black + Ruff).
- Tiled is used to edit `.tmx` maps (external app).

### Commands (Poetry)
```bash
poetry install
poetry run python -m game.main          # run
poetry run pytest -q                    # tests
poetry run pytest -q -m "not slow"      # default fast suite
poetry run ruff check . && poetry run ruff format .
