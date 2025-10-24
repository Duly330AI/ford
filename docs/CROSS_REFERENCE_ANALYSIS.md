# Cross-Reference Analysis: Documentation & Data Files vs. Tasks

**Date:** 2025-10-24  
**Purpose:** Systematic review of all 22 specified files (11 docs + 11 data JSONs) against all TASK-*.md files to identify missing cross-references and gaps in task coverage.

---

## Executive Summary

**Key Findings:**
1. **10/22 files have ZERO or minimal task references** (critical gap)
2. **AI system design completely unaddressed** in M2 tasks
3. **UO-specific mechanics** (progression, engagement, dodge) lack dedicated tasks
4. **UI specification** has no implementation tasks
5. **Usables/Containers system** (lockpicking, traps, ownership) missing entirely
6. **Data files** like `progression_rules.json`, `monsters_ai_overrides.json`, `factions.json`, `behaviors.json`, `tactics.json`, `blackboard_keys.json` are **not mentioned in any task**

---

## File-by-File Analysis

### 1. **AI_DESIGN.md** ⚠️ **CRITICAL GAP**
- **Current Task Coverage:** NONE
- **Content:** Utility-AI, faction diplomacy, behaviors, tactics, blackboard, overworld FSM, combat AI, AI-vs-AI, pathfinding, leashing
- **Missing Tasks:**
  - AI architecture implementation (Perception, Intent, Tactic scoring)
  - Faction/diplomacy system (`factions.json` integration)
  - Behavior archetypes (`behaviors.json` → melee/ranged/caster/scout/guardian/boss)
  - Tactics implementation (`tactics.json` → utility scoring per role)
  - Blackboard system (`blackboard_keys.json`)
  - AI-vs-AI combat (multi-faction encounters)
  - Overworld AI FSM (idle/patrol/chase/engage/leash)
  - Call-for-help & pack tactics
  - Boss phase logic
  
**Recommended Actions:**
- Create **TASK-M2-AI** umbrella covering AI Design
- Add subtasks: TASK-M2-AI-01 (Perception/Threat), TASK-M2-AI-02 (Utility Scoring), TASK-M2-AI-03 (Tactics Integration), TASK-M2-AI-04 (Factions/Diplomacy), TASK-M2-AI-05 (Blackboard), TASK-M2-AI-06 (Overworld FSM), TASK-M2-AI-07 (AI-vs-AI)

---

### 2. **ARCHITECTURE.md** ✅ **GOOD COVERAGE**
- **Current Task Coverage:** Referenced in TASK-M1-01..16 (implicit), mentioned in M2/M3/M4/M5 umbrella tasks
- **Content:** Systems separation, data-driven principles, determinism, testability, layers, coordinates, RNG, event flow
- **Cross-References Found:**
  - M1 tasks follow architecture (BSP, TileMap, Collision, Movement all separated)
  - M2-M5 tasks respect `systems/*` vs `scenes/*` separation
  - RNG streams mentioned (M5)
  
**Gaps:**
- No explicit task validates "all systems/* have zero Arcade imports" (architectural test)
- Missing: TASK-ARCH-01 "Validate architecture compliance (imports, separation, determinism tests)"

**Recommended Actions:**
- Add **TASK-QUALITY-2**: Architectural Compliance Tests

---

### 3. **ARCHITECTURE_UO_ADDENDUM.md** ⚠️ **PARTIAL GAP**
- **Current Task Coverage:** Skills/Stats mentioned in M3, Combat in M2, Engagement hinted
- **Content:** Skill progression dataflow, combat dataflow, engagement rules (encounter bubble, escape, rundenzeit), dodge mechanics
- **Missing Tasks:**
  - Explicit "Encounter Bubble" implementation (12-tile radius, LOS joining, leash-break mechanics)
  - Dodge mechanics in combat (Space = dash + evade bonus)
  - Crafting pause during combat
  - Node respawn pause policy
  
**Recommended Actions:**
- Add **TASK-M2-19**: Encounter Bubble & Escape Mechanics
- Add **TASK-M2-20**: Dodge Action (Combat)
- Add **TASK-M4-21**: Crafting/Node Pause During Combat

---

### 4. **ATTRIBUTIONS.md** ✅ **COVERED**
- **Current Task Coverage:** TASK-M1-12 mentions `ATTRIBUTIONS.md`
- **Content:** Placeholder for CC0/CC-BY asset sources
- **Status:** Adequate (M1-12 enforces presence)

---

### 5. **CONTRIBUTING.md** ✅ **PARTIAL COVERAGE**
- **Current Task Coverage:** Implied by TASK-TOOLING-1, pre-commit config, CI workflows
- **Content:** Setup, coding standards, PR process, branch strategy, conventional commits
- **Gaps:**
  - No explicit task for "Enforce CONTRIBUTING.md compliance in CI" (e.g., commit message linting)
  
**Recommended Actions:**
- Optional: TASK-QUALITY-3 "Commit Message Linting (Conventional Commits)"

---

### 6. **GAMEPLAY.md** ✅ **GOOD COVERAGE**
- **Current Task Coverage:** M2 (combat), M3 (skills/inventory/loot), M4 (crafting/nodes), M5 (save/load)
- **Content:** Core loop, controls, world/light, attributes (UO-style), combat (UO hit/parry/damage), DEX/speed, skill progression (0.1 increments, sweet-spot), movement, nodes, crafting, items, loot, enemies, balance
- **Cross-References Found:**
  - M2: Combat formulas match GAMEPLAY
  - M3: Skills/Inventory/Loot align
  - M4: Crafting/Nodes align
  - M5: Save/Load policy aligns
  
**Gaps:**
- Missing: **Stat-Affinities** system (STR/DEX/INT/STAM gains on skill gains) — hinted in GAMEPLAY.md but no dedicated task
- Missing: **Anti-Macro** penalty implementation
- Missing: **Skill-Locks** (Up/Down/Lock UI + auto-drop logic when hitting total cap)

**Recommended Actions:**
- Add **TASK-M3-21**: Stat-Affinities & Stat Gains (on Skill Gain)
- Add **TASK-M3-22**: Anti-Macro Penalty System
- Add **TASK-M3-23**: Skill Locks (Up/Down/Lock + Auto-Drop)

---

### 7. **GAMEPLAY_ADDENDUM_UO.md** ⚠️ **CRITICAL GAP**
- **Current Task Coverage:** NONE (completely unaddressed)
- **Content:** 
  - **Skill progression mechanics** (0.1 increments, sweet-spot formula, slowdown, anti-macro, curves)
  - **Engagement & Zeit** (encounter bubble, rundenzeit=3s, escape conditions, flee action)
  - **Dodge-Roll** (overworld iFrames vs combat dash+evade)
- **Missing Tasks:**
  - Skill progression formula implementation (`progression_rules.json` + `skills.json` integration)
  - Sweet-spot gain calculation
  - Slowdown curves (quadratic/cubic/sqrt modes)
  - Anti-macro detection & penalty
  - Stat gain on skill gain (STR/DEX/INT/STAM daily caps)
  - Encounter bubble mechanics
  - Escape/disengage countdown
  - Flee action (+leash_margin, +evade%)
  - Dodge mechanics differentiation (overworld vs combat)

**Recommended Actions:**
- Add **TASK-M3-24**: Skill Progression Formula (Sweet-Spot, Slowdown, Anti-Macro)
- Add **TASK-M3-25**: Stat Gain System (Affinities, Daily Caps)
- Add **TASK-M2-21**: Encounter Bubble & Escape Mechanics (cross-ref with ARCHITECTURE_UO_ADDENDUM)
- Add **TASK-M2-22**: Dodge Mechanics (Overworld iFrames vs Combat Dash)

---

### 8. **SAVELOAD.md** ✅ **COVERED**
- **Current Task Coverage:** M5 tasks (TASK-M5-01..18) address save/load comprehensively
- **Content:** Format (JSON/gzip/MsgPack), schema_version, slots, policy, migration
- **Status:** Well-covered

---

### 9. **TOOLING.md** ✅ **COVERED**
- **Current Task Coverage:** TASK-TOOLING-1, implied by CI/Makefile/pre-commit setup
- **Content:** Dependencies, setup, VS Code config, Makefile, linting, tests, pre-commit, data validation, CI workflows, headless strategy
- **Status:** Adequate

---

### 10. **USABLES_AND_CONTAINERS.md** 🔴 **MASSIVE GAP**
- **Current Task Coverage:** **ZERO** (completely unaddressed)
- **Content:**
  - Container types (chest/barrel/bookshelf/cabinet/wardrobe/crate/basket)
  - Locks & lockpicking (difficulty, keys, skill checks)
  - Traps (types: needle/poison/explosion/dart/fire, difficulty, disarm, on_open/on_fail)
  - Ownership & trespass (crime system)
  - Detect Hidden skill
  - Bash (STR vs bash_dc, durability)
  - Levers, buttons, doors, pressure plates
  - Container respawn (daily/interval/none)
  - Loot table integration
  - Search action (main action in combat)
  - Movable/pickup containers
  - Reading (books/notes, lore_id)
  
**Missing Tasks (ENTIRE SYSTEM):**
- Container system architecture
- Lock/Key mechanics
- Lockpicking skill implementation
- Trap system (types, triggers, disarm)
- Detect Hidden skill
- Tinkering skill (disarm synergy)
- Bash mechanics
- Ownership/Trespass system
- Lever/Button/Door/Pressure Plate interactions
- Toggle groups
- Container respawn logic
- Movable containers
- Reading/Lore system

**Recommended Actions:**
- Create **TASK-M3-USABLES** umbrella (or integrate into M4)
- Add subtasks:
  - **TASK-M3-26** or **TASK-M4-22**: Container System (Core)
  - **TASK-M3-27** or **TASK-M4-23**: Locks & Lockpicking
  - **TASK-M3-28** or **TASK-M4-24**: Traps & Disarm
  - **TASK-M3-29** or **TASK-M4-25**: Detect Hidden Skill
  - **TASK-M3-30** or **TASK-M4-26**: Bash Mechanics
  - **TASK-M3-31** or **TASK-M4-27**: Ownership & Trespass
  - **TASK-M4-28**: Levers/Buttons/Doors/Pressure Plates
  - **TASK-M4-29**: Container Respawn
  - **TASK-M4-30**: Reading/Lore System

---

### 11. **UI_SPEC_UO_STYLE.md** 🔴 **MASSIVE GAP**
- **Current Task Coverage:** **ZERO** (completely unaddressed)
- **Content:**
  - HUD (HP/Mana/Stamina bars, buff/debuff pips, hotbar, journal/combat-log, minimap, initiative bar)
  - Character window (paperdoll, stats tabs, resistances, weight/encumbrance)
  - Skills window (0.1 resolution, skill locks, cap display, curves, last actions, train/use)
  - Inventory (grid vs UO-freeform, stack-split, drag-drop, repair, filters)
  - Container windows (lock/trap status, take all, sort, respawn timer)
  - Item tooltips (name, rarity, weight, value, weapon stats, durability, skill req, set/unique)
  - Spellbook
  - Crafting UI (recipe list, detail panel, queue with priorities, success chance tooltip)
  - Merchant/Trade
  - Interaction & targeting (double-click, right-click context, use-target cursor, hover LOS)
  - Shortcuts (QWERTZ)
  - Window management (docking, scaling, layouts)
  - Accessibility (font scaling, colorblind modes, contrast, labeled icons)
  - Data bindings & events
  - Error/state messages
  
**Missing Tasks (ENTIRE UI SYSTEM):**
- UI architecture & framework setup
- HUD components (all of them)
- Paperdoll system
- Skills UI (with locks, curves, tooltips)
- Inventory UI (grid vs freeform modes)
- Container UI
- Tooltip system (data-driven, formula hints)
- Spellbook UI
- Crafting UI
- Merchant/Trade UI
- Interaction cursor system
- Hotkey/Keybind system
- Window management system
- Accessibility features
- UI event bus
- UI localization framework

**Recommended Actions:**
- Create **TASK-M6** (UI Milestone) or integrate into existing milestones
- Add umbrella **TASK-UI**:
  - **TASK-UI-01**: UI Framework & Architecture
  - **TASK-UI-02**: HUD (HP/Mana/Stamina/Buffs/Hotbar/Journal/Minimap)
  - **TASK-UI-03**: Initiative Bar (Combat)
  - **TASK-UI-04**: Character Window (Paperdoll + Stats)
  - **TASK-UI-05**: Skills Window (Locks, Caps, Curves, Train/Use)
  - **TASK-UI-06**: Inventory UI (Grid + Freeform Modes)
  - **TASK-UI-07**: Container UI (Lock/Trap Status, Interactions)
  - **TASK-UI-08**: Tooltip System (Data-Driven, Formula Hints)
  - **TASK-UI-09**: Spellbook UI
  - **TASK-UI-10**: Crafting UI (Recipe List, Queue, Success Tooltip)
  - **TASK-UI-11**: Merchant/Trade UI
  - **TASK-UI-12**: Interaction Cursor & Targeting
  - **TASK-UI-13**: Hotkey/Keybind System
  - **TASK-UI-14**: Window Management (Docking, Scaling, Layouts)
  - **TASK-UI-15**: Accessibility (Fonts, Colorblind, Contrast)
  - **TASK-UI-16**: UI Event Bus & Data Bindings
  - **TASK-UI-17**: Error/State Messages

---

## Data Files Analysis

### 12. **behaviors.json** ⚠️ **ZERO COVERAGE**
- **Content:** AI behavior archetypes (melee, ranged, caster, guardian, brute, scout, boss) with engage_range, base_delay_class, kite settings, flee thresholds, taunt, body_block, call_for_help, berserk
- **Current Task Coverage:** NONE (M2-09 mentions "Heuristiken" but doesn't reference `behaviors.json`)
- **Recommended Action:** Add cross-ref in **TASK-M2-AI-03** (Behaviors Integration)

---

### 13. **blackboard_keys.json** ⚠️ **ZERO COVERAGE**
- **Content:** AI blackboard schema (threat map, focusTarget, allyInNeed, lastHurtBy, ammo, mana, recovery, position, los, coverScore, incomingThreat, phase)
- **Current Task Coverage:** NONE
- **Recommended Action:** Add cross-ref in **TASK-M2-AI-05** (Blackboard System)

---

### 14. **combat_rules.json** ✅ **PARTIAL COVERAGE**
- **Content:** hit_chance, parry, damage, movement, recovery, ranged, initiative, crit, dodge
- **Current Task Coverage:** M2-02 (Stats), M2-12 (Damage), M3-14 (Ammo), M3-15 (Rarity tooltips hint at rules)
- **Gaps:** No explicit task for "Load & Validate combat_rules.json at startup", dodge mechanics
- **Recommended Action:** Add validation task, cross-ref dodge in **TASK-M2-22**

---

### 15. **factions.json** ⚠️ **ZERO COVERAGE**
- **Content:** Diplomacy matrix (12 factions), relation values (-1 to +1), defaults (aggro_radius, call_for_help_radius, mutual_enemy_bias, help_allies)
- **Current Task Coverage:** NONE
- **Recommended Action:** Add **TASK-M2-AI-04** (Factions & Diplomacy System)

---

### 16. **items.json** ✅ **COVERED**
- **Current Task Coverage:** M3-02 (Items Model), M3-19 (Data Samples), TASK-DATA-1
- **Status:** Adequate

---

### 17. **loot_tables.json** ✅ **COVERED**
- **Current Task Coverage:** M3-08 (Loot System), M3-09 (Drop Resolution), M3-19 (Data Samples), TASK-DATA-1
- **Status:** Adequate

---

### 18. **monsters.json** ✅ **PARTIAL COVERAGE**
- **Content:** Monster archetypes (hp, atk, def, speed, resist, drop_table, ai role, faction)
- **Current Task Coverage:** M2-07 (Enemy Data)
- **Gaps:** No task for AI field integration (`ai`, `faction`, `ai_overworld`, `ai_combat` extensions suggested in AI_DESIGN.md)
- **Recommended Action:** Extend **TASK-M2-07** or add **TASK-M2-08-EXT** (Monster AI Field Mapping)

---

### 19. **monsters_ai_overrides.json** ⚠️ **ZERO COVERAGE**
- **Content:** Currently empty `[]`, intended for per-monster AI overrides
- **Current Task Coverage:** NONE
- **Recommended Action:** Document in **TASK-M2-AI-06** (AI Overrides System)

---

### 20. **recipes.json** ✅ **COVERED**
- **Current Task Coverage:** M4-01 (Schema), M4-02 (Craft System), M4-17 (Data Samples)
- **Status:** Adequate

---

### 21. **skills.json** ✅ **PARTIAL COVERAGE**
- **Content:** Skill IDs, caps, xp_curve (curve profile keys), stats affinities (STR/DEX/INT/STAM)
- **Current Task Coverage:** M3-06 (Skills System), M3-19 (Data Samples)
- **Gaps:** `xp_curve` linkage to `progression_rules.json.curves` not explained in tasks, stat affinities implementation missing
- **Recommended Action:** Cross-ref in **TASK-M3-24** (Progression Formula), **TASK-M3-25** (Stat Gains)

---

### 22. **tactics.json** ⚠️ **ZERO COVERAGE**
- **Content:** Utility-AI action scoring per archetype (base scores, dist_pref, ally_role, radius, threat_pct, hp_threshold, ammo_low, etc.)
- **Current Task Coverage:** NONE
- **Recommended Action:** Add **TASK-M2-AI-03** (Tactics & Utility Scoring Integration)

---

## Missing Data File

### **progression_rules.json** ⚠️ **ZERO COVERAGE** (not in original 22 list but critical)
- **Content:** skill gain formula (increment, base, min_gain, max_gain, sweet_spot_center, slowdown_mode, anti_macro), stats gain (daily_caps, gain_on_skill_gain), caps (per_skill, total_skills, per_stat), curves profiles
- **Current Task Coverage:** NONE (hinted in M3-06 but not explicitly referenced)
- **Recommended Action:** Add **TASK-M3-24** (Skill Progression Formula using progression_rules.json)

---

## Summary Tables

### Files with ZERO Task Coverage (Critical Gaps)
| # | File | Type | Severity | Recommended Tasks |
|---|------|------|----------|-------------------|
| 1 | AI_DESIGN.md | Doc | 🔴 CRITICAL | TASK-M2-AI-01..07 (7 tasks) |
| 7 | GAMEPLAY_ADDENDUM_UO.md | Doc | 🔴 CRITICAL | TASK-M3-24, M3-25, M2-21, M2-22 (4 tasks) |
| 10 | USABLES_AND_CONTAINERS.md | Doc | 🔴 CRITICAL | TASK-M3-26..31, M4-22..30 (11 tasks) |
| 11 | UI_SPEC_UO_STYLE.md | Doc | 🔴 CRITICAL | TASK-UI-01..17 (17 tasks) |
| 12 | behaviors.json | Data | ⚠️ HIGH | TASK-M2-AI-03 cross-ref |
| 13 | blackboard_keys.json | Data | ⚠️ HIGH | TASK-M2-AI-05 cross-ref |
| 15 | factions.json | Data | ⚠️ HIGH | TASK-M2-AI-04 (1 task) |
| 19 | monsters_ai_overrides.json | Data | ⚠️ MEDIUM | TASK-M2-AI-06 cross-ref |
| 22 | tactics.json | Data | ⚠️ HIGH | TASK-M2-AI-03 cross-ref |
| — | progression_rules.json | Data | ⚠️ HIGH | TASK-M3-24, M3-25 cross-ref |

**Total Missing Tasks: ~45+** (including subtasks)

---

### Files with Partial Coverage (Need Cross-References)
| # | File | Current Coverage | Missing Cross-Refs |
|---|------|------------------|--------------------|
| 2 | ARCHITECTURE.md | Implicit in M1-M5 | Architectural compliance test task |
| 3 | ARCHITECTURE_UO_ADDENDUM.md | Partial (skills, combat) | Encounter bubble, dodge, crafting pause |
| 6 | GAMEPLAY.md | Good (M2-M5) | Stat affinities, anti-macro, skill locks |
| 14 | combat_rules.json | M2-02, M2-12 | Dodge mechanics, validation task |
| 18 | monsters.json | M2-07 | AI field mapping extension |
| 21 | skills.json | M3-06, M3-19 | xp_curve → progression_rules link, stat affinities |

---

### Files with Adequate Coverage ✅
| # | File | Notes |
|---|------|-------|
| 4 | ATTRIBUTIONS.md | M1-12 enforces |
| 5 | CONTRIBUTING.md | TASK-TOOLING-1, CI |
| 8 | SAVELOAD.md | M5 comprehensive |
| 9 | TOOLING.md | TASK-TOOLING-1 |
| 16 | items.json | M3-02, M3-19, TASK-DATA-1 |
| 17 | loot_tables.json | M3-08, M3-09, M3-19 |
| 20 | recipes.json | M4-01, M4-02, M4-17 |

---

## Recommendations

### Immediate Actions (Critical)
1. **Create TASK-M2-AI umbrella** (AI Design) with 7 subtasks (Perception, Utility, Tactics, Factions, Blackboard, Overworld FSM, AI-vs-AI)
2. **Create TASK-M3-USABLES umbrella** (Usables & Containers) with 11 subtasks
3. **Create TASK-UI umbrella** (or M6) with 17 subtasks covering full UI spec
4. **Add TASK-M3-24, M3-25** (Skill Progression Formula, Stat Gains from GAMEPLAY_ADDENDUM_UO)
5. **Add TASK-M2-21, M2-22** (Encounter Bubble, Dodge Mechanics)

### Short-Term Actions (High Priority)
6. Add cross-references to `behaviors.json`, `tactics.json`, `blackboard_keys.json`, `factions.json` in AI tasks
7. Add `progression_rules.json` cross-refs in skill progression tasks
8. Extend M2-07 (monsters.json) with AI field mapping
9. Add combat_rules.json validation task
10. Add skill locks, anti-macro, stat affinities tasks to M3

### Long-Term Actions (Medium Priority)
11. Add architectural compliance test task (TASK-QUALITY-2)
12. Add commit message linting task (TASK-QUALITY-3)
13. Document `monsters_ai_overrides.json` usage in AI tasks
14. Add encounter bubble & crafting pause tasks to M2/M4

---

## Conclusion

**Coverage Score: 45% (10/22 files adequately covered)**

The current task structure provides excellent coverage for:
- Core gameplay loop (M1-M5)
- Combat basics (M2)
- Items/Inventory/Loot (M3)
- Crafting/Nodes (M4)
- Save/Load (M5)

**Critical gaps exist in:**
- **AI systems** (behaviors, tactics, factions, blackboard, pathfinding, AI-vs-AI)
- **UO-specific progression mechanics** (sweet-spot gains, slowdown, anti-macro, stat affinities)
- **Usables/Containers** (locks, traps, detect hidden, bash, ownership, levers/doors)
- **Complete UI implementation** (17+ UI tasks missing)
- **Data file integration** (8 data files not referenced in tasks)

**Estimated Work:**
- **~45 new tasks** required to reach 95% coverage
- **~200-300 cross-references** to add to existing tasks
- **Priority:** AI (7 tasks), Usables (11 tasks), UI (17 tasks), UO Mechanics (4 tasks), Data Integration (6 tasks)

---

**Next Steps:**
1. Review this analysis with team
2. Prioritize missing tasks by milestone
3. Create new TASK-*.md files for gaps
4. Update existing tasks with cross-references
5. Update `docs/task.md` index with new tasks
6. Run validation: `python -m game.tools.validate_tasks` (if tool exists)
