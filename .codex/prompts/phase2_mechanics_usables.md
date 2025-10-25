# Phase 2 Prompt: UO Mechanics & Usables/Containers Tasks

## Context
You are creating **17 tasks** covering:
- **UO-specific skill progression mechanics** (5 tasks: M3-21..25)
- **Encounter & dodge mechanics** (2 tasks: M2-19, M2-20)
- **Usables & Containers system** (6 tasks: M3-EXT-01..06)
- **World interactions** (4 tasks: M4-21..24)

These tasks address **critical gaps** identified in `CROSS_REFERENCE_ANALYSIS.md`.

## Source Documents (READ THESE FIRST)
1. **`docs/CROSS_REFERENCE_ANALYSIS.md`** (Sections 7, 10: GAMEPLAY_ADDENDUM_UO, USABLES_AND_CONTAINERS)
2. **`docs/GAMEPLAY_ADDENDUM_UO.md`** (Skill progression formulas, engagement mechanics, dodge)
3. **`docs/USABLES_AND_CONTAINERS.md`** (Complete container/lock/trap/ownership system spec)
4. **`docs/ARCHITECTURE_UO_ADDENDUM.md`** (Dataflow: skills, combat, engagement)
5. **`data/progression_rules.json`** (Skill gain formulas, stat gains, caps)

## Existing Task Schema (FOLLOW EXACTLY)
[Same as Phase 1]

---

## Tasks to Create

### **UO Skill Progression Mechanics (M3-21..25)**

#### 1. **TASK-M3-21.md**: Stat Affinities System
- **Title**: "Stat Affinity System (STR/DEX/INT/STAM gains on skill gains)"
- **Priority**: P1
- **Artifacts**: `game/systems/stats.py` (extend), `tests/systems/test_stat_affinities.py`
- **DependsOn**: TASK-M3-06 (Skills System), TASK-M2-02 (Stats)
- **Notes**:
  - Each skill has stat affinities (STR/DEX/INT/STAM weights) in `skills.json`
  - On skill gain (+0.1), roll for **each stat** based on affinity
  - Formula: `P(stat_gain) = base_chance * affinity_weight * (1 - today_gains / daily_cap)`
  - Daily caps per stat (from `progression_rules.json.stats`): `str_daily_cap`, `dex_daily_cap`, `int_daily_cap`, `stam_daily_cap`
  - Stat gains are +0.1 increments (like skills)
  - Reference **GAMEPLAY.md § 4 (Stat-Affinitäten)**, **GAMEPLAY_ADDENDUM_UO.md § B**
- **Acceptance**:
  - [ ] Stat gain rolls fire on skill gains
  - [ ] Affinities from `skills.json` correctly weight rolls
  - [ ] Daily caps enforced (no gains if cap reached today)
  - [ ] Stat gains persist in save/load
- **Tests**:
  - [ ] Affinity weighting tests (seeded)
  - [ ] Daily cap enforcement tests
  - [ ] Multi-skill stat gain tests (cumulative)

#### 2. **TASK-M3-22.md**: Anti-Macro Penalty System
- **Title**: "Anti-Macro Penalty Detection & Application"
- **Priority**: P1
- **Artifacts**: `game/systems/skills.py` (extend), `tests/systems/test_anti_macro.py`
- **DependsOn**: TASK-M3-06 (Skills System), TASK-M3-24 (Skill Progression Formula)
- **Notes**:
  - Detect repeated actions: same skill + same target + same position within `repeat_window` (30s default)
  - Apply penalty: `gain_chance *= (1 - penalty)` (penalty = 0.2 default from `progression_rules.json.skill.anti_macro`)
  - Penalty decays after leaving `repeat_window`
  - Reference **GAMEPLAY_ADDENDUM_UO.md § B (Anti-Macro)**, **progression_rules.json**
- **Acceptance**:
  - [ ] Repeated actions detected correctly
  - [ ] Penalty applied to gain chance
  - [ ] Penalty decays after time window
- **Tests**:
  - [ ] Repeat detection tests (seeded, timekeeper mock)
  - [ ] Penalty application tests (gain chance reduced)
  - [ ] Decay tests (penalty clears after window)

#### 3. **TASK-M3-23.md**: Skill Locks (Up/Down/Lock + Auto-Drop)
- **Title**: "Skill Lock System (Up/Down/Lock, Auto-Drop at Total Cap)"
- **Priority**: P1
- **Artifacts**: `game/systems/skills.py` (extend), `tests/systems/test_skill_locks.py`
- **DependsOn**: TASK-M3-06 (Skills System)
- **Notes**:
  - Each skill has lock state: `UP` (default, gains allowed), `DOWN` (auto-drop if total cap hit), `LOCK` (no gains/drops)
  - Total skill cap (700.0 default from `progression_rules.json.caps.total_skills`)
  - When total >= cap and skill with `UP` lock gains, find **lowest `DOWN` skill** and drop by 0.1
  - UI shows lock icons (▲ UP, ▼ DOWN, ■ LOCK) - cross-ref TASK-M6-UI-05
  - Reference **GAMEPLAY.md § 7 (Skills), § 20 (Beispielwerte)**, **UI_SPEC_UO_STYLE.md § 4**
- **Acceptance**:
  - [ ] Lock states (UP/DOWN/LOCK) stored per skill
  - [ ] Total cap enforced (auto-drop on gain if at cap)
  - [ ] Lowest DOWN skill selected for drop
  - [ ] Lock state persists in save/load
- **Tests**:
  - [ ] Lock state CRUD tests
  - [ ] Auto-drop logic tests (at cap, multiple DOWN skills)
  - [ ] Edge case: no DOWN skills (gain blocked)

#### 4. **TASK-M3-24.md**: Skill Progression Formula (Sweet-Spot, Slowdown)
- **Title**: "Skill Progression Formula (Sweet-Spot, Slowdown, progression_rules.json)"
- **Priority**: P0
- **Artifacts**: `game/systems/skills.py` (extend), `tests/systems/test_skill_progression.py`
- **DependsOn**: TASK-M3-06 (Skills System)
- **Notes**:
  - Implement UO-style gain formula:
    ```
    p_success = action success chance (hit/craft/gather/cast)
    sweet = 1.0 - abs(p_success - sweet_spot_center) / 0.5  # max gain at ~50% success
    slowdown = slowdown_fn(skill/cap, mode)  # quadratic/cubic/sqrt from curves
    anti_macro = antiMacroMultiplier(context)  # 1.0 or penalty
    P(gain) = clamp(min_gain, base * curve.base_mult * sweet * slowdown * anti_macro, max_gain)
    if roll() < P(gain): skill += increment  # +0.1
    ```
  - Load curves from `progression_rules.json.curves` (linked via `skills.json[id].xp_curve`)
  - Supported slowdown modes: `linear`, `quadratic`, `cubic`, `sqrt`
  - Reference **GAMEPLAY_ADDENDUM_UO.md § B**, **ARCHITECTURE_UO_ADDENDUM.md § Datenfluss (Skills)**
- **Acceptance**:
  - [ ] Sweet-spot formula works (max gain at p_success ~0.5)
  - [ ] Slowdown curves implemented (quadratic default)
  - [ ] Curves loaded from `progression_rules.json`
  - [ ] Gain increments are always +0.1
- **Tests**:
  - [ ] Sweet-spot tests (varying p_success)
  - [ ] Slowdown tests (skill 0/50/90 → different gains)
  - [ ] Curve profile tests (linear vs quadratic)
  - [ ] Deterministic gain tests (seeded)

#### 5. **TASK-M3-25.md**: Stat Gain System (Affinities, Daily Caps)
- **Title**: "Stat Gain System (on Skill Gain, Affinities, Daily Caps)"
- **Priority**: P1
- **Artifacts**: `game/systems/stats.py` (extend), `tests/systems/test_stat_gains.py`
- **DependsOn**: TASK-M3-21 (Stat Affinities), TASK-M3-24 (Skill Progression)
- **Notes**:
  - Triggered on skill gain events
  - Roll for **each stat** (STR/DEX/INT/STAM) based on `skills.json[id].stats` affinities
  - Formula: `P(stat_gain) = gain_on_skill_gain * affinity * (1 - daily_gains / daily_cap)`
  - `gain_on_skill_gain` = 0.15 default (from `progression_rules.json.stats`)
  - Daily caps: `str_daily_cap=2.0`, `dex_daily_cap=2.0`, etc.
  - Reset daily counters at midnight (game time or real time, configurable)
  - Reference **GAMEPLAY_ADDENDUM_UO.md § B**, **progression_rules.json**
- **Acceptance**:
  - [ ] Stat gain rolls fire on skill gain
  - [ ] Affinities correctly weight rolls
  - [ ] Daily caps enforced (soft cap, no gains if exceeded)
  - [ ] Daily counters reset at midnight
- **Tests**:
  - [ ] Stat gain roll tests (seeded)
  - [ ] Daily cap enforcement tests
  - [ ] Reset tests (timekeeper mock)

---

### **Encounter & Dodge Mechanics (M2-19, M2-20)**

#### 6. **TASK-M2-19.md**: Encounter Bubble & Escape Mechanics
- **Title**: "Encounter Bubble & Escape/Disengage Mechanics"
- **Priority**: P1
- **Artifacts**: `game/systems/engagement.py`, `tests/systems/test_engagement.py`
- **DependsOn**: TASK-M2-06 (Overworld FSM), TASK-M2-08 (Initiative), TASK-M2-AI-06 (Overworld AI FSM)
- **Notes**:
  - **Encounter Bubble**: 12-tile radius from player (configurable)
  - All enemies with **LOS to player** within bubble **join combat**
  - New enemies entering bubble join at **next round start**
  - **Escape conditions**:
    - No enemy has LOS **AND** all enemies > `leash_break` distance (10 tiles)
    - Condition must hold for **1 full round**
    - Player can use **Flee action** (main action) for +leash_margin, +evade%
  - **Rundenzeit**: 1 round = 3 seconds simulation time
  - Reference **GAMEPLAY_ADDENDUM_UO.md § C**, **ARCHITECTURE_UO_ADDENDUM.md § Engagement & Zeit**
- **Acceptance**:
  - [ ] Encounter bubble (12 tiles, LOS) correctly identifies combatants
  - [ ] New enemies join at round start (not mid-round)
  - [ ] Escape countdown triggers correctly (LOS-free + distance)
  - [ ] Flee action grants +leash_margin, +evade%
- **Tests**:
  - [ ] Bubble tests (LOS + radius)
  - [ ] Join timing tests (mid-round vs round-start)
  - [ ] Escape countdown tests (seeded, timekeeper mock)
  - [ ] Flee action tests (modifiers applied)

#### 7. **TASK-M2-20.md**: Dodge Mechanics (Overworld iFrames vs Combat Dash)
- **Title**: "Dodge Mechanics (Overworld iFrames vs Combat Dash+Evade)"
- **Priority**: P1
- **Artifacts**: `game/systems/dodge.py`, `tests/systems/test_dodge.py`
- **DependsOn**: TASK-M1-05 (Player Controller), TASK-M2-04 (Combat Resolution)
- **Notes**:
  - **Overworld Dodge-Roll** (Space):
    - Costs Stamina (configurable in `combat_rules.json.dodge`)
    - Grants iFrames (0.35s default)
    - Dash distance: 1 tile
    - Cooldown: short (1-2s)
  - **Combat Dodge Action** (Space):
    - **Main Action** (blocks Attack/Cast/Use)
    - Dash distance: 1 tile (any direction)
    - Grants `+evade%` until **end of turn** (not full round)
    - Costs Stamina, checks `recovery` and `immobilized` status
  - Reference **GAMEPLAY_ADDENDUM_UO.md § D**, **combat_rules.json.dodge**
- **Acceptance**:
  - [ ] Overworld dodge grants iFrames (brief invincibility)
  - [ ] Combat dodge grants +evade% until turn end
  - [ ] Both cost Stamina correctly
  - [ ] Combat dodge is main action (blocks other actions)
- **Tests**:
  - [ ] Overworld dodge iFrames tests (collision immunity)
  - [ ] Combat dodge evade bonus tests
  - [ ] Stamina cost tests
  - [ ] Action blocking tests (combat dodge)

---

### **Usables & Containers (M3-EXT-01..06)**

#### 8. **TASK-M3-EXT.md** (Umbrella Task)
- **Title**: "Usables & Containers System (Locks, Traps, Ownership, Interactions)"
- **Status**: Proposed
- **Priority**: P0
- **Artifacts**: Overview document
- **DependsOn**: TASK-M3-02 (Items), TASK-M3-06 (Skills), TASK-M3-08 (Loot Tables)
- **Notes**:
  - Reference **USABLES_AND_CONTAINERS.md** (complete spec)
  - Container types: chest, barrel, bookshelf, cabinet, wardrobe, crate, basket, desk
  - Systems: locks, traps, detect hidden, bash, ownership/trespass, respawn
  - Interactions: open, lockpick, disarm, search, inspect, read, bash
  - Cross-ref to `data/loot_tables.json` (container contents)
  - List 6 subtasks (M3-EXT-01..06)
- **Acceptance**: All 6 subtasks completed, container system operational
- **Tests**: Integration tests for lock→disarm→loot workflow

#### 9. **TASK-M3-EXT-01.md**: Container System Core
- **Title**: "Container System Core (Data Model, State Machine, Interactions)"
- **Priority**: P0
- **Artifacts**: `game/systems/containers.py`, `data/usables/*.json`, `tests/systems/test_containers.py`
- **DependsOn**: TASK-M3-02 (Items), TASK-M3-08 (Loot Tables)
- **Notes**:
  - Data schema from **USABLES_AND_CONTAINERS.md § 2**:
    - Fields: `id`, `type`, `name`, `sprite`, `placement`, `interact`, `ownership`, `durability`, `fx`
    - `interact`: `open`, `lock`, `trap`, `container`, `toggle`, `pressure_plate`, `readable`, `movable`
  - State machine: `locked`, `open`, `armed_trap`, `durability`, `spawn_epoch`
  - Placement IDs (deterministic loot seeding): `placement_id = "map_x_y"`
  - Container capacity: `capacity` (slots), `weight_max` (kg), `allowed_tags`
  - Reference **USABLES_AND_CONTAINERS.md § 1-2**
- **Acceptance**:
  - [ ] Container data model matches schema
  - [ ] State machine transitions (locked→unlocked, closed→open)
  - [ ] Placement IDs used for deterministic loot
  - [ ] Capacity/weight limits enforced
- **Tests**:
  - [ ] State transition tests
  - [ ] Capacity tests (slot/weight limits)
  - [ ] Placement ID seeding tests

#### 10. **TASK-M3-EXT-02.md**: Locks & Lockpicking
- **Title**: "Locks & Lockpicking System (Skill Checks, Keys, Failure)"
- **Priority**: P0
- **Artifacts**: `game/systems/locks.py`, `tests/systems/test_locks.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core), TASK-M3-06 (Skills - lockpicking)
- **Notes**:
  - Lock fields: `locked` (bool), `difficulty` (0-100), `key_id` (optional bypass)
  - Lockpick formula: `P = clamp(0.02, 0.5 + (lockpicking - difficulty)/200, 0.98)`
  - On success: `locked = false`
  - On failure: optional anti-tamper (trigger trap, break pick, alert guards)
  - Skill gain: roll on **every attempt** (success or failure)
  - **Main Action** in combat (1 action)
  - Reference **USABLES_AND_CONTAINERS.md § 3-4**
- **Acceptance**:
  - [ ] Lockpick checks use skill vs difficulty
  - [ ] Keys bypass lockpick check
  - [ ] Skill gains on attempts (success/fail)
  - [ ] Anti-tamper triggers (optional, configurable)
- **Tests**:
  - [ ] Lockpick success/fail tests (seeded)
  - [ ] Key bypass tests
  - [ ] Skill gain tests
  - [ ] Anti-tamper tests

#### 11. **TASK-M3-EXT-03.md**: Traps & Disarm (Tinkering)
- **Title**: "Trap System & Disarm Mechanics (Tinkering + Detect Hidden)"
- **Priority**: P0
- **Artifacts**: `game/systems/traps.py`, `tests/systems/test_traps.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core), TASK-M3-EXT-04 (Detect Hidden), TASK-M3-06 (Skills - tinkering)
- **Notes**:
  - Trap fields: `armed` (bool), `type` (needle/poison_gas/explosion/dart/fireburst), `difficulty` (0-100), `power` (damage), `radius` (tiles), `on_open` (bool), `on_fail_disarm` (bool)
  - Disarm formula: `skill = 0.7*tinkering + 0.3*detect_hidden`, `P = clamp(0.02, 0.5 + (skill - difficulty)/200, 0.98)`
  - On success: `armed = false`
  - On failure + `on_fail_disarm==true`: trigger trap
  - Trap damage uses `combat_rules.json` (resist mitigation)
  - **Main Action** in combat
  - Reference **USABLES_AND_CONTAINERS.md § 3-4**
- **Acceptance**:
  - [ ] Trap types implemented (needle, poison, explosion, dart, fire)
  - [ ] Disarm checks use tinkering + detect_hidden
  - [ ] Trap damage respects resists (from combat_rules.json)
  - [ ] Failure can trigger trap (configurable)
- **Tests**:
  - [ ] Disarm success/fail tests (seeded)
  - [ ] Trap damage tests (resists applied)
  - [ ] On-failure trigger tests

#### 12. **TASK-M3-EXT-04.md**: Detect Hidden Skill
- **Title**: "Detect Hidden Skill (Passive & Active Search)"
- **Priority**: P1
- **Artifacts**: `game/systems/detect_hidden.py`, `tests/systems/test_detect_hidden.py`
- **DependsOn**: TASK-M3-06 (Skills), TASK-M3-EXT-01 (Container Core)
- **Notes**:
  - **Passive**: Skill level gives chance to auto-detect traps on inspect
  - **Active Search** (Main Action): Raises detection level for N turns
  - Detection hints: tooltips show "Scratches near lock", "Faint hissing sound", "Tripwire visible"
  - Detection bonus: +0.05..+0.15 to disarm chance (from detect_hidden skill)
  - Can reveal **hidden compartments** (extra loot in containers)
  - Reference **USABLES_AND_CONTAINERS.md § 3-4**
- **Acceptance**:
  - [ ] Passive detection rolls on inspect (skill-based)
  - [ ] Active Search grants detection bonus for N turns
  - [ ] Hints displayed in tooltips
  - [ ] Hidden compartments revealed (extra loot)
- **Tests**:
  - [ ] Passive detection tests (seeded)
  - [ ] Active Search duration tests
  - [ ] Bonus application tests (disarm chance)

#### 13. **TASK-M3-EXT-05.md**: Bash Mechanics (STR vs bash_dc)
- **Title**: "Bash Mechanics (STR Check, Durability, Noise)"
- **Priority**: P1
- **Artifacts**: `game/systems/bash.py`, `tests/systems/test_bash.py`
- **DependsOn**: TASK-M2-02 (Stats), TASK-M3-EXT-01 (Container Core)
- **Notes**:
  - Bash formula: `atk = STR + weapon_dmg + tactics*0.2`, `P = clamp(0.02, 0.5 + (atk - bash_dc)/200, 0.95)`
  - On success: `durability.hp -= roll(5..10)`
  - On failure: `noise += 0.2` (can alert enemies)
  - Durability reaches 0 → container breaks (loot spills, ownership violated if applicable)
  - **Main Action** in combat
  - Reference **USABLES_AND_CONTAINERS.md § 3-4**
- **Acceptance**:
  - [ ] Bash checks use STR + weapon + tactics
  - [ ] Durability decreases on success
  - [ ] Noise raises on failure (can trigger enemy aggro)
  - [ ] Container breaks at 0 durability
- **Tests**:
  - [ ] Bash success/fail tests (seeded)
  - [ ] Durability reduction tests
  - [ ] Noise tests (aggro trigger cross-ref TASK-M2-AI-06)

#### 14. **TASK-M3-EXT-06.md**: Ownership & Trespass System
- **Title**: "Ownership & Trespass System (Crime, Faction Reactions)"
- **Priority**: P1
- **Artifacts**: `game/systems/ownership.py`, `tests/systems/test_ownership.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core), TASK-M2-AI-04 (Factions)
- **Notes**:
  - Ownership fields: `faction` (owner), `trespass` (bool, marks as "stealing if opened")
  - Opening/looting `trespass==true` container generates **Crime Event**
  - Faction reactions:
    - Guards/NPCs turn hostile (later feature, stub for now)
    - Call-for-help triggers (cross-ref TASK-M2-AI-04)
  - UI shows warning: "This container belongs to [faction]. Opening it is theft."
  - Reference **USABLES_AND_CONTAINERS.md § 7**
- **Acceptance**:
  - [ ] Ownership field checked on interact
  - [ ] Crime events generated for trespass
  - [ ] UI warning displays before opening
  - [ ] Faction reactions stub (extensible for guards)
- **Tests**:
  - [ ] Ownership check tests
  - [ ] Crime event generation tests
  - [ ] UI warning tests (mock)

---

### **World Interactions (M4-21..24)**

#### 15. **TASK-M4-21.md**: Levers/Buttons/Doors/Pressure Plates
- **Title**: "Levers, Buttons, Doors, Pressure Plates (Toggle Groups)"
- **Priority**: P1
- **Artifacts**: `game/systems/toggles.py`, `tests/systems/test_toggles.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core)
- **Notes**:
  - Toggle types: lever (flip), button (press), door (open/close), pressure_plate (weight trigger)
  - Toggle groups: `group_id` links multiple targets (e.g., lever "A" opens doors "A1", "A2", disarms trap "A3")
  - Toggle modes: `flip` (toggle state), `momentary` (hold while pressed), `permanent` (one-time)
  - Pressure plates: `weight_min` (kg), `hold_to_activate` (bool)
  - Reference **USABLES_AND_CONTAINERS.md § 2 (toggle), § 6 (Examples)**
- **Acceptance**:
  - [ ] Toggle groups work (one lever affects multiple targets)
  - [ ] Modes implemented (flip, momentary, permanent)
  - [ ] Pressure plates trigger on weight threshold
  - [ ] Doors open/close correctly
- **Tests**:
  - [ ] Toggle group tests (1→N targets)
  - [ ] Mode tests (flip vs momentary)
  - [ ] Pressure plate weight tests

#### 16. **TASK-M4-22.md**: Container Respawn (daily/interval/none)
- **Title**: "Container Respawn System (Daily/Interval/None)"
- **Priority**: P1
- **Artifacts**: `game/systems/container_respawn.py`, `tests/systems/test_container_respawn.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core), TASK-M3-08 (Loot Tables)
- **Notes**:
  - Respawn modes: `none` (one-time loot), `daily` (24h reset), `interval` (configurable hours)
  - Timer starts: on **first open** or **after emptied** (configurable)
  - On respawn: regenerate loot from `loot_table` (new seed or same seed, configurable)
  - `preserve_unlooted` flag: keep old items if container not fully looted
  - Reference **USABLES_AND_CONTAINERS.md § 5**
- **Acceptance**:
  - [ ] Respawn modes (none/daily/interval) work correctly
  - [ ] Timer starts on first open or empty
  - [ ] Loot regenerates from table on respawn
  - [ ] `preserve_unlooted` works (old items + new items)
- **Tests**:
  - [ ] Respawn timing tests (timekeeper mock)
  - [ ] Loot regeneration tests (seeded)
  - [ ] Preserve_unlooted tests

#### 17. **TASK-M4-23.md**: Reading/Lore System (books, scrolls, lore_id)
- **Title**: "Reading & Lore System (Books, Scrolls, Notes, Lore Flags)"
- **Priority**: P2
- **Artifacts**: `game/systems/lore.py`, `tests/systems/test_lore.py`
- **DependsOn**: TASK-M3-EXT-01 (Container Core)
- **Notes**:
  - Readable objects: books, scrolls, notes (field: `readable.pages`, `readable.lore_id`)
  - Reading action: **Main Action** in combat, instant in overworld
  - Lore flags: `lore_id` sets flag on read (e.g., "bandit_notes_01" → quest trigger)
  - Multi-page support: `pages` field, UI shows page navigation
  - Reference **USABLES_AND_CONTAINERS.md § 6.3**
- **Acceptance**:
  - [ ] Reading action works (main action in combat)
  - [ ] Lore flags set on read
  - [ ] Multi-page support (UI shows pages)
  - [ ] Lore IDs persist in save/load
- **Tests**:
  - [ ] Reading tests (lore flag set)
  - [ ] Multi-page tests (navigation)
  - [ ] Persistence tests

#### 18. **TASK-M4-24.md**: Crafting Pause During Combat
- **Title**: "Crafting Queue Pause During Combat (Timekeeper Integration)"
- **Priority**: P1
- **Artifacts**: `game/util/timekeeper.py` (extend), `tests/systems/test_crafting_pause.py`
- **DependsOn**: TASK-M4-02 (Crafting System), TASK-M2-04 (Combat Resolution)
- **Notes**:
  - When combat starts: pause crafting queue ticks
  - When combat ends: resume crafting queue
  - Crafting completions during combat are **marked** but not UI-spammed
  - Player can collect completed items after combat ends
  - Reference **ARCHITECTURE_UO_ADDENDUM.md § Engagement & Zeit**, **GAMEPLAY_ADDENDUM_UO.md § C**
- **Acceptance**:
  - [ ] Crafting pauses on combat start
  - [ ] Crafting resumes on combat end
  - [ ] Completions marked (no UI spam during combat)
  - [ ] Collectible items available post-combat
- **Tests**:
  - [ ] Pause/resume tests (timekeeper mock)
  - [ ] Completion marking tests
  - [ ] Post-combat collection tests

---

## Critical Requirements
[Same as Phase 1: follow schema, Created: 2025-10-25, Owner: Copilot Agent, cross-references, etc.]

---

## Output Format
Generate **18 separate Markdown files**:
- M3-21..25 (skill progression)
- M2-19, M2-20 (encounter, dodge)
- TASK-M3-EXT.md (umbrella)
- M3-EXT-01..06 (usables/containers)
- M4-21..24 (world interactions)

---

## Validation Checklist (Run After Generation)
- [ ] All 18 files created
- [ ] All files follow schema
- [ ] Cross-references to GAMEPLAY_ADDENDUM_UO.md, USABLES_AND_CONTAINERS.md, progression_rules.json correct
- [ ] DependsOn chains logical
- [ ] Run `pre-commit run --files docs/tasks/TASK-M3-2*.md docs/tasks/TASK-M2-1*.md docs/tasks/TASK-M2-20.md docs/tasks/TASK-M3-EXT*.md docs/tasks/TASK-M4-2*.md`
