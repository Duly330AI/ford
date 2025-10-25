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

- **Python**: 3.12+ (via Conda environment `ford`)
- **Arcade**: ≥ 3.x
- **Package**: Poetry
- **Resolution**: 1920×1080, integer scale (16px tiles upscale 4× → 64px).
- **Layers**: ground, walls (collidable), decals, light-blockers, entities.
- **Rendering**: SpriteList per layer + Arcade lights & particles.
- **Physics**: AABB, dt movement (8-way), no slopes.
- **Combat**: **Turn-based** resolution (formula-driven attack/defense/effects).
- **Systems**: skills (usage-based), professions/nodes, crafting (JSON recipes), loot tables, save/load.

---

## Codebase Architecture

### **Core Structure**

```
game/                      # Python package (bootstrap yet)
  main.py               # Entry point: init Arcade, load data, run MainLoop
  systems/              # Core logic (no Arcade deps)
    combat_system.py   # Turn-based formulas (hit_chance, damage, initiative)
    skill_system.py    # Skill tracking (usage-based progression)
    crafting_system.py # Recipe validation & output
    dungeon_gen.py     # Procedural generation (BSP, spawning)
  models/               # Data classes (actor, item, combat state)
  views/                # Arcade rendering (SpriteList per layer)

data/                    # JSON-driven content (VALIDATED at load)
  combat_rules.json     # All formulas: hit%, damage, movement, recovery
  items.json            # Item definitions (damage, armor, rarity, slots)
  monsters.json         # Mob templates (HP, loot, AI hints)
  recipes.json          # Crafting recipes (input → output)
  skills.json           # Skill metadata (names, affinity, caps)
  loot_tables.json      # Encounter rewards (weighted pools)
  factions.json         # NPC groups & reputation
  schemas/              # JSON Schema validation (.schema.json files)
```

### **Key Design Patterns**

**Data-Driven Everything:**
- Combat formulas live in `data/combat_rules.json`, not hardcoded
- Item/monster definitions are JSON; loaded + validated on startup
- Change `data/items.json` → restart game → new item available (no code rebuild)

**Testable Core:**
- `game/systems/*` must NOT import Arcade (no pygame/OpenGL)
- All formulas deterministic with seeded RNG (`PYTHONHASHSEED=0`)
- Tests import systems directly; mock models as needed

**Skill Usage-Based Progression:**
- Player gains exp in Swords by using sword attacks (not from kills)
- Skill `(0-100)` from usage count; caps per skill in `skills.json`
- Affects combat via `hit_chance = f(skill_diff)` per `combat_rules.json`

**Turn-Based Combat Resolution:**
- Overworld: realtime movement
- Encounter: initiative roll → turn order → each actor chooses action
- All damage/hit/parry calculated via formulas in `combat_rules.json`
- See `docs/COMBAT_RULES.md` for full math

---

## Local Workflow (VS Code + Conda)

- **Environment**: `conda activate ford` (Python 3.12 via Conda; auto-activates on terminal open)
- **Code Quality**: Black + Ruff on save; pre-commit hooks block commits on failures
- **Maps**: Tiled editor for `.tmx` (external tool; generates collision/spawn data)
- **Debug**: F3 overlay (FPS, seed, coords); F4/F5 heatmaps (reachability, spawns)

### 🎯 CRITICAL FOR AGENTS: Use Tasks + invoke-wait Wrapper

**NEVER use raw `run_in_terminal` for long-running commands.** Instead:

**Option A (Preferred): VS Code Tasks**
```
runTasks with label "pytest: run all"
runTasks with label "ruff: check all"
```

**Option B (Fallback): invoke-wait Wrapper**
```powershell
invoke-wait "conda run -n ford python -m pytest tests/"
invoke-wait "conda run -n ford poetry install --no-root"
```

Both ensure:
- ✅ Complete output capture (no truncation)
- ✅ Exit code guaranteed
- ✅ Clear START/END markers (agent sees completion)
- ✅ Timeout protection (`pytest-timeout`: 30s/test)

**WHY:** Raw `run_in_terminal` suffers from Shell Integration bugs (hangs, buffering, missed exit codes).

**Available Tasks:**
- `pytest: run all` — Full suite
- `pytest: run fast (no slow tests)` — Smoke tests only
- `pytest: run with coverage` — HTML report
- `ruff: check all` / `ruff: fix all` — Lint
- `black: format all` — Formatter
- `poetry: install` — Deps
- `run: FORD game` — Start game

**Do NOT use raw terminal for:**
- ❌ Tests (hanging issues, missing output)
- ❌ Linting/formatting (coverage/exit code tracking)
- ❌ Pre-commit hooks
- ❌ Long-running operations (poetry, builds)

### Commands (Poetry with Conda; for reference only—use Tasks instead!)
```bash
# Environment is auto-activated on terminal open
poetry install --no-root
poetry run python -m game.main          # run
poetry run pytest -q                    # tests
poetry run pytest -q -m "not slow"      # fast suite
poetry run ruff check . && poetry run ruff format .

---

## 📐 Critical Patterns & Conventions

### **JSON Data Validation (CRITICAL)**

All game data (items, monsters, skills, combat) is JSON. **MUST validate on load:**

```python
# game/systems/data_loader.py (pseudocode)
def load_items():
    with open("data/items.json") as f:
        raw = json.load(f)
    # Validate against schema
    validate(raw, load_schema("data/schemas/items.schema.json"))
    return [Item.from_dict(item) for item in raw]
```

**Validation happens at:**
- Startup in `game/main.py`
- Test fixtures must mock or use real `data/` files
- Schema files are source of truth for data structure

**Common JSON Files:**
- `combat_rules.json` → Formulas (hit%, damage, recovery, movement)
- `items.json` → Weapons/armor/consumables (damage, armor, slots, rarity)
- `skills.json` → Skill caps, affinities (STR/DEX/INT/STAM), progression rates
- `monsters.json` → Mob stats (HP, loot_table_id, faction, threat_rating)
- `recipes.json` → Crafting (input items → output + skill check)

### **Combat Formula Pattern**

All combat calculations reference `data/combat_rules.json` **parameters**:

```python
# Example: Hit Chance Formula
# From: docs/COMBAT_RULES.md (lines 33-63)
def calculate_hit_chance(attacker, defender, combat_rules):
    base = combat_rules["hit_chance"]["base"]
    skill_diff = (attacker.weapon_skill - defender.weapon_skill)
    skill_contrib = skill_diff / combat_rules["hit_chance"]["skill_scale"]
    stat_diff = (attacker.str - defender.dex)
    stat_contrib = stat_diff / combat_rules["hit_chance"]["atkdef_scale"]

    chance = base + skill_contrib + stat_contrib
    min_val = combat_rules["hit_chance"]["min"]
    max_val = combat_rules["hit_chance"]["max"]
    return clamp(chance, min_val, max_val)
```

**Key Rules:**
- All damage/hit/parry/recovery calculations are **deterministic** with seeded RNG
- Formulas use `combat_rules.json` parameters (never hardcode numbers)
- Tests seed RNG with `PYTHONHASHSEED=0` for reproducibility
- See `docs/COMBAT_RULES.md` for complete mathematical specifications

### **Skill System (Usage-Based)**

Skills (Swords, Archery, Anatomy, Tactics, etc.) progress from **usage**, not kills:

```python
# When player uses a sword attack:
player.skills["Swords"].add_usage()  # Increment usage count

# Skill level = f(usage_count) from skills.json
# At level 100, no more progression (cap per skill.json)
```

**Skill Affinities** (from `skills.json`):
- Each skill has primary stat: STR, DEX, INT, STAM
- Affects skill cap (e.g., Swords 120 max with STR bonus)
- Used in formulas: `hit_chance += (skill_level / 200)`

### **Testable Core Systems**

**`game/systems/*.py` must NOT import Arcade/rendering:**
- ✅ OK: import from `game/models/`, `data`, `math`, `json`
- ❌ NOT OK: `import arcade`, `import pygame`, `from game.views`

**Tests MUST:**
- Run with `pytest` + timeout (30s per test)
- Use seeded RNG: `PYTHONHASHSEED=0` in environment
- Mock or use real `data/` files (not in-memory dicts)
- Validate JSON loading separately from system logic

### **Data-Driven Configuration**

**Modding-Ready:**
- Items: Change `data/items.json` → Restart → New item in game
- Formulas: Tweak `data/combat_rules.json` multipliers → Restart → New difficulty
- Monsters: Adjust `data/monsters.json` loot/threat → Restart → New economy

**Never hardcode:**
- ❌ Item stats (use `data/items.json`)
- ❌ Combat multipliers (use `data/combat_rules.json`)
- ❌ Skill caps (use `data/skills.json`)
- ❌ Monster templates (use `data/monsters.json`)

### **Git & Task Workflow**

- **Keep `/docs/task.md` updated** with all active + completed tasks
- **Conventional Commits**: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`
- **Feature branches**: Create for non-trivial changes
- **Small PRs**: One feature per branch; green CI before merge
- **Move tasks:** When done, move task to "Completed Tasks" section

---

## 🔧 Testing & Validation

### **Test Organization**

```
tests/
  test_smoke.py              # Imports all systems (validates no missing deps)
  systems/
    test_combat_system.py    # Combat formulas + edge cases
    test_skill_system.py     # Skill progression, caps
    test_crafting_system.py  # Recipe validation, output
    test_dungeon_gen.py      # Procedural generation, seed reproducibility
```

### **Validation Checklist Before Merge**

- [ ] All tests pass: `pytest: run all`
- [ ] No lint errors: `ruff: check all`
- [ ] Code formatted: `black: format all`
- [ ] Imports organized: pre-commit hooks run clean
- [ ] JSON schemas validated: `data/schemas/*.schema.json` match actual data
- [ ] Documentation updated: `docs/task.md`, code comments
- [ ] Determinism verified: Tests re-run with `PYTHONHASHSEED=0`

---

## 📚 Documentation Reference

- **Gameplay**: `docs/GAMEPLAY.md` — Core loop, UI, movement, combat UI
- **Combat Rules**: `docs/COMBAT_RULES.md` — Mathematical formulas, examples
- **Dungeon Generator**: `docs/DUNGEON_GENERATOR.md` — BSP, spawn algorithm, seeding
- **Task Tracking**: `docs/task.md` — Active + completed tasks (UPDATE THIS)
- **Architecture**: `docs/ARCHITECTURE_UO_ADDENDUM.md` — System boundaries
- **Attributions**: `ATTRIBUTIONS.md` — CC0 asset sources
