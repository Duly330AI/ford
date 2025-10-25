# Phase 4 Prompt: Quality Assurance & Validation Tasks

## Context
You are creating **4 quality/validation tasks** identified in `CROSS_REFERENCE_ANALYSIS.md`.

## Source Documents (READ THESE FIRST)
1. **`docs/CROSS_REFERENCE_ANALYSIS.md`** (Section 2, 14: ARCHITECTURE, combat_rules.json, monsters.json analysis)
2. **`docs/ARCHITECTURE.md`** (Section 21: Testpyramide & Headless-Strategie)

## Existing Task Schema (FOLLOW EXACTLY)
[Same as previous phases]

---

## Tasks to Create

### 1. **TASK-QUALITY-2.md**: Architectural Compliance Tests
- **Title**: "Architectural Compliance Tests (systems/* Zero Arcade Imports)"
- **Status**: Proposed
- **Priority**: P1
- **Owner**: Copilot Agent
- **Created**: 2025-10-25
- **Artifacts**: `tests/architecture/test_compliance.py`, `.github/workflows/ci.yml` (extend)
- **DependsOn**: TASK-M1-01..16 (all M1 tasks), TASK-M2-01..18 (all M2 tasks)
- **Notes**:
  - Validate **all files in `game/systems/*` have ZERO imports from `arcade`, `pyglet`, `game/scenes/*`**
  - Validate **all files in `game/util/*` (except `util/camera.py`, `util/feedback.py` which are adapter stubs) have ZERO Arcade imports**
  - Validate **all test files in `tests/systems/*` and `tests/util/*` have ZERO Arcade imports**
  - Enforce via AST parsing (not regex) to catch `import arcade`, `from arcade import X`, `import game.scenes.Y`
  - Add to CI (`ci.yml`): run compliance tests before running unit tests
  - Reference **ARCHITECTURE.md § 1 (Trennung von Zuständigkeiten), § 21 (Testpyramide & Headless-Strategie)**
- **Acceptance**:
  - [ ] Compliance tests scan `game/systems/*` and fail if Arcade imports detected
  - [ ] Compliance tests scan `game/util/*` (exclude adapters) and fail if Arcade imports detected
  - [ ] CI runs compliance tests and blocks merge on failure
  - [ ] README or ARCHITECTURE.md updated with compliance rules
- **Tests**:
  - [ ] Compliance test itself (unit test for AST parser)
  - [ ] False positive tests (adapter files excluded correctly)
  - [ ] CI integration test (run in GH Actions)

---

### 2. **TASK-QUALITY-3.md**: Commit Message Linting
- **Title**: "Commit Message Linting (Conventional Commits Enforcement)"
- **Status**: Proposed
- **Priority**: P2
- **Owner**: Copilot Agent
- **Created**: 2025-10-25
- **Artifacts**: `.github/workflows/commitlint.yml`, `.commitlintrc.json`, `docs/CONTRIBUTING.md` (update)
- **DependsOn**: None
- **Notes**:
  - Enforce **Conventional Commits** format: `type(scope): subject`
  - Allowed types: `feat`, `fix`, `test`, `refactor`, `chore`, `docs`, `style`, `perf`, `ci`, `build`
  - Examples (from existing commits):
    - ✅ `feat: add initiative order`
    - ✅ `fix: correct loot roll`
    - ✅ `test: add crafting failure cases`
    - ✅ `refactor: split combat`
    - ✅ `docs(analysis): add cross-reference analysis`
    - ❌ `added some stuff`
    - ❌ `WIP`
  - Tools: `commitlint` + `husky` (or Python equivalent like `gitlint`)
  - Add to pre-commit hook (optional, can be skipped with `--no-verify`)
  - Add to CI: validate PR title and all commits
  - Reference **CONTRIBUTING.md § Git-Workflow & Commits**
- **Acceptance**:
  - [ ] Commit message linter configured (commitlint or gitlint)
  - [ ] Pre-commit hook warns on invalid messages (non-blocking, skippable)
  - [ ] CI fails on invalid commit messages in PR
  - [ ] CONTRIBUTING.md updated with examples
- **Tests**:
  - [ ] Linter config tests (valid/invalid messages)
  - [ ] CI integration test

---

### 3. **TASK-M2-23.md**: Combat Rules Validation
- **Title**: "Combat Rules Validation (Load & Validate combat_rules.json at Startup)"
- **Status**: Proposed
- **Priority**: P1
- **Owner**: Copilot Agent
- **Created**: 2025-10-25
- **Artifacts**: `game/util/data_loader.py` (extend), `data/schemas/combat_rules.schema.json`, `tests/util/test_combat_rules_validation.py`
- **DependsOn**: TASK-M2-02 (Stats), TASK-M2-12 (Damage System)
- **Notes**:
  - Load `combat_rules.json` at startup and validate against schema
  - Schema checks:
    - All required keys present (`hit_chance`, `parry`, `damage`, `movement`, `recovery`, `ranged`, `initiative`, `dodge`)
    - Numeric ranges valid (e.g., `hit_chance.min` <= `hit_chance.max`, `hit_chance.base` in [0,1])
    - Weapon delay map (`recovery.weapon_base_delay`) has valid keys (weapon types)
  - If validation fails: **abort startup** with clear error message (file path, key, expected range)
  - Reference **CROSS_REFERENCE_ANALYSIS.md § 14 (combat_rules.json)**, **combat_rules.json**
- **Acceptance**:
  - [ ] Schema file `combat_rules.schema.json` created (JSON Schema Draft-07)
  - [ ] Validation runs at startup (before game loop)
  - [ ] Invalid JSON aborts with clear error message
  - [ ] All keys validated (presence, types, ranges)
- **Tests**:
  - [ ] Valid combat_rules.json passes
  - [ ] Invalid JSON (missing keys, wrong types, out-of-range) fails with correct error
  - [ ] Schema tests (all constraints checked)

---

### 4. **TASK-M2-24.md**: Monster AI Field Mapping Extension
- **Title**: "Monster AI Field Mapping Extension (Extend M2-07 with ai/faction Fields)"
- **Status**: Proposed
- **Priority**: P1
- **Owner**: Copilot Agent
- **Created**: 2025-10-25
- **Artifacts**: `data/monsters.json` (extend), `game/systems/enemies.py` (extend), `tests/systems/test_enemies.py` (extend)
- **DependsOn**: TASK-M2-07 (Enemy Data), TASK-M2-AI-03 (Tactics), TASK-M2-AI-04 (Factions)
- **Notes**:
  - Extend `monsters.json` schema with AI fields (from **AI_DESIGN.md § 7**):
    - `ai`: archetype (melee/ranged/caster/scout/guardian/brute/boss) - links to `behaviors.json`
    - `faction`: faction ID (player/goblin/orc/undead/wildlife/daemon/elemental/gargoyle/ratman/lizardman/troll_ogre/dragonkind)
    - `ai_tags`: optional array (e.g., ["aggressive", "pack_hunter"])
    - `ai_overworld`: object (`patrol` bool, `leash` distance, `aggro_radius`)
    - `ai_combat`: object (`role` (melee/ranged/caster), `preferred_target` (lowest_armor/highest_threat/etc.))
  - Update `enemies.py` to load and use these fields
  - Map AI fields to behaviors/tactics (cross-ref TASK-M2-AI-03)
  - Reference **CROSS_REFERENCE_ANALYSIS.md § 18 (monsters.json)**, **AI_DESIGN.md § 7**
- **Acceptance**:
  - [ ] `monsters.json` schema extended with AI fields
  - [ ] All existing monsters have `ai` and `faction` fields populated
  - [ ] `enemies.py` loads AI fields correctly
  - [ ] AI fields used in TASK-M2-AI-03/04 integration
- **Tests**:
  - [ ] Schema validation tests (AI fields required, valid values)
  - [ ] Enemy loading tests (AI fields parsed)
  - [ ] Integration tests (AI archetype → tactics lookup)

---

## Critical Requirements
[Same as previous phases: follow schema, Created: 2025-10-25, Owner: Copilot Agent, cross-references, etc.]

**Special Notes:**
- TASK-QUALITY-2/3: These are **meta-tasks** (enforce project standards), not feature tasks
- TASK-M2-23: This is a **validation task** (data integrity), critical for stability
- TASK-M2-24: This is an **extension task** (augments existing M2-07), bridges to AI system

---

## Output Format
Generate **4 separate Markdown files**:
- `docs/tasks/TASK-QUALITY-2.md`
- `docs/tasks/TASK-QUALITY-3.md`
- `docs/tasks/TASK-M2-23.md`
- `docs/tasks/TASK-M2-24.md`

---

## Validation Checklist (Run After Generation)
- [ ] All 4 files created
- [ ] All files follow schema
- [ ] Cross-references to ARCHITECTURE.md, combat_rules.json, monsters.json correct
- [ ] DependsOn chains logical
- [ ] Run `pre-commit run --files docs/tasks/TASK-QUALITY*.md docs/tasks/TASK-M2-2*.md`
