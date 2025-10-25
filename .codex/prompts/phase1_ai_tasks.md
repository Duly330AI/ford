# Phase 1 Prompt: AI System Tasks (M2-AI Milestone)

## Context
You are creating **7 AI system tasks** for the FORD project based on `docs/CROSS_REFERENCE_ANALYSIS.md` findings. The AI system is currently **completely unimplemented** and has **zero task coverage**. These tasks form a new milestone **M2-AI** (AI Design & Implementation).

## Source Documents (READ THESE FIRST)
1. **`docs/CROSS_REFERENCE_ANALYSIS.md`** (Section 1: AI_DESIGN.md analysis)
2. **`docs/AI_DESIGN.md`** (Complete AI architecture spec - 800+ lines)
3. **`data/behaviors.json`** (AI archetypes: melee/ranged/caster/scout/guardian/boss/brute)
4. **`data/tactics.json`** (Utility-AI action scoring per archetype)
5. **`data/factions.json`** (Diplomacy matrix for 12 factions, AI-vs-AI combat)
6. **`data/blackboard_keys.json`** (AI context data schema)

## Existing Task Schema (FOLLOW EXACTLY)
```markdown
- [ ] ID: TASK-XXX
  Title: ...
  Status: Proposed
  Priority: P0/P1/P2
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `path/to/file.py`, `path/to/test.py`
  DependsOn: TASK-XXX, TASK-YYY
  Notes:
  [Detailed implementation notes with specific references to source docs]
  Acceptance:
  - [ ] Criterion 1 (concrete, testable)
  - [ ] Criterion 2
  Tests:
  - [ ] Test 1 (deterministic, headless where possible)
  - [ ] Test 2
```

## Tasks to Create

### 1. **TASK-M2-AI.md** (Umbrella Task)
- **Title**: "AI System (Utility-AI, Factions, Behaviors, Overworld FSM)"
- **Status**: Proposed
- **Priority**: P0
- **Artifacts**: Overview document
- **DependsOn**: TASK-M2-06 (Overworld FSM), TASK-M2-09 (Combat KI basics)
- **Notes**:
  - Reference **AI_DESIGN.md** sections 1-14
  - Explain Utility-AI approach (vs behavior trees)
  - List 7 subtasks (M2-AI-01..07)
  - Cross-ref to `behaviors.json`, `tactics.json`, `factions.json`, `blackboard_keys.json`
- **Acceptance**: All 7 subtasks completed, AI system operational for single-faction and multi-faction encounters
- **Tests**: Integration tests for AI-vs-AI scenarios

### 2. **TASK-M2-AI-01.md**: Perception & Threat System
- **Title**: "Perception & Threat Memory System"
- **Artifacts**: `game/systems/ai_perception.py`, `tests/systems/test_ai_perception.py`
- **DependsOn**: TASK-M1-04 (Collision/LOS), TASK-M2-11 (Enemy tracking)
- **Notes**:
  - Implement LOS-based perception (Bresenham-Ray)
  - Threat memory per actor (decay over time, cap, prioritization)
  - Visibility/noise scoring (0..1)
  - Last-seen tracking for "Investigate" behavior
  - Reference **AI_DESIGN.md § 3 (Perception & Threat-Memory)**
- **Acceptance**:
  - [ ] LOS checks respect wall-blocking
  - [ ] Threat decays correctly over time (no flip-flop)
  - [ ] Last-seen positions tracked for N turns
- **Tests**:
  - [ ] LOS unit tests (various geometries)
  - [ ] Threat decay tests (seeded)
  - [ ] Multi-target priority tests

### 3. **TASK-M2-AI-02.md**: Utility Scoring Engine
- **Title**: "Utility-AI Scoring Engine (Target & Action Selection)"
- **Artifacts**: `game/systems/ai_utility.py`, `tests/systems/test_ai_utility.py`
- **DependsOn**: TASK-M2-AI-01 (Perception)
- **Notes**:
  - Implement target scoring: `w_threat * Threat + w_dist * fDist + w_hp * (1-HP%) + w_role * RoleBias + w_mutual * MutualEnemy`
  - Action scoring per tactics.json rules
  - ε-greedy selection (5-10% randomness to avoid deterministic loops)
  - Reference **AI_DESIGN.md § 4 (Utility-AI), § 5 (Kampf Entscheidungsablauf)**
- **Acceptance**:
  - [ ] Target selection prioritizes correctly (threat, distance, HP, role)
  - [ ] Action scores computed from `tactics.json`
  - [ ] ε-greedy prevents predictable patterns
- **Tests**:
  - [ ] Scoring unit tests (known weights, expected outcomes)
  - [ ] ε-greedy randomness tests (seeded)
  - [ ] Deterministic scenarios (fixed inputs → known target/action)

### 4. **TASK-M2-AI-03.md**: Tactics Integration (behaviors.json, tactics.json)
- **Title**: "Tactics & Behavior Archetypes Integration"
- **Artifacts**: `game/systems/ai_tactics.py`, `tests/systems/test_ai_tactics.py`
- **DependsOn**: TASK-M2-AI-02 (Utility Scoring), TASK-M2-07 (Enemy data with ai field)
- **Notes**:
  - Load `behaviors.json` (engage_range, base_delay_class, kite settings, flee_hp_pct, taunt, body_block, call_for_help, berserk, phase_logic)
  - Load `tactics.json` (action base scores, dist_pref, ally_role, radius, threat_pct, hp_threshold)
  - Implement archetype-specific logic:
    - **Melee**: guard_ally (caster), chase, flee at HP threshold
    - **Ranged**: kite (min/max dist), switch_when_ammo_low
    - **Caster**: debuff (if target def high), nuke, fear (if outnumbered)
    - **Guardian**: body_block, taunt, guard_ally priority
    - **Brute**: berserk at HP threshold, smash (armor break), throw_rock
    - **Scout**: call_for_help, avoid_stronger
    - **Boss**: phase_ability, summon_adds
  - Reference **AI_DESIGN.md § 4 (Taktik-Score), § 7 (Beispiel-Daten & Mapping)**
- **Acceptance**:
  - [ ] All 7 archetypes implement correct tactics
  - [ ] Kiting behavior works (ranged maintains 3-5 tile distance)
  - [ ] Guard/Body-block positions correctly (within radius of caster ally)
  - [ ] Call-for-help triggers faction rally (cross-ref TASK-M2-AI-04)
- **Tests**:
  - [ ] Archetype tactic tests (seeded scenarios)
  - [ ] Kiting pathfinding tests
  - [ ] Guard positioning tests

### 5. **TASK-M2-AI-04.md**: Factions & Diplomacy (factions.json)
- **Title**: "Faction System & AI-vs-AI Diplomacy"
- **Artifacts**: `game/systems/factions.py`, `tests/systems/test_factions.py`
- **DependsOn**: TASK-M2-AI-01 (Perception), TASK-M2-07 (Enemy with faction field)
- **Notes**:
  - Load `factions.json` (12 factions: player, goblin, orc, undead, wildlife, daemon, elemental, gargoyle, ratman, lizardman, troll_ogre, dragonkind)
  - Relation matrix (-1 = hostile, 0 = neutral, +1 = ally, 0.5 = tentative ally)
  - Implement diplomacy checks:
    - `relation(actor.faction, target.faction) < 0` → hostile
    - AI actors engage enemies of their faction **automatically**
    - Multi-faction encounters (e.g., Orcs vs Undead vs Player)
  - Call-for-help: `aggro_radius_tiles`, `call_for_help_radius`, `mutual_enemy_bias`, `help_allies_threshold`
  - Reference **AI_DESIGN.md § 2 (Faktionen & Diplomatie)**
- **Acceptance**:
  - [ ] Faction relations loaded correctly from `factions.json`
  - [ ] AI-vs-AI combat triggers for hostile factions
  - [ ] Call-for-help rallies same-faction actors within radius
  - [ ] Mutual enemy bias prioritizes shared threats
- **Tests**:
  - [ ] Relation lookup tests (all 12×12 matrix entries)
  - [ ] AI-vs-AI engagement tests (Orc encounters Undead → combat)
  - [ ] Call-for-help tests (seeded scenarios)
  - [ ] 3-way fight tests (Player + Orc + Undead)

### 6. **TASK-M2-AI-05.md**: Blackboard System (blackboard_keys.json)
- **Title**: "AI Blackboard Context System"
- **Artifacts**: `game/systems/ai_blackboard.py`, `tests/systems/test_ai_blackboard.py`
- **DependsOn**: TASK-M2-AI-01 (Perception)
- **Notes**:
  - Implement blackboard per actor: `threat` (map<entityId, number>), `focusTarget` (entityId|null), `allyInNeed` (entityId|null), `lastHurtBy` (entityId|null), `ammo` (number), `mana` (number), `recovery` (number), `position` (tile), `los` (map<entityId, bool>), `coverScore` (number), `incomingThreat` (number), `phase` (number|undefined for boss mechanics)
  - Update blackboard each turn (perception phase)
  - Access via `actor.blackboard.get(key)`
  - Reference **AI_DESIGN.md § 7 (blackboard_keys.json), § 8 (Implementierung Pseudocode)**
- **Acceptance**:
  - [ ] Blackboard keys match `blackboard_keys.json` schema
  - [ ] Blackboard updates correctly each AI turn
  - [ ] Threat map persists across turns (with decay)
- **Tests**:
  - [ ] Blackboard CRUD tests
  - [ ] Threat map update tests
  - [ ] LOS map update tests

### 7. **TASK-M2-AI-06.md**: Overworld AI FSM (idle/patrol/chase/engage/leash)
- **Title**: "Overworld AI State Machine (idle→patrol→chase→engage→leash)"
- **Artifacts**: `game/systems/ai_overworld.py`, `tests/systems/test_ai_overworld.py`
- **DependsOn**: TASK-M2-06 (Overworld FSM basics), TASK-M2-AI-01 (Perception), TASK-M2-AI-04 (Factions)
- **Notes**:
  - States: `Idle`, `Patrol` (waypoints), `Investigate` (noise/last-seen), `Chase` (player or hostile), `Engage` (switch to combat mode), `LeashReturn` (return to spawn zone)
  - Engagement trigger: LOS + radius (from `factions.json.defaults.aggro_radius_tiles`)
  - Leash mechanics: If distance > `leash_distance` (12 tiles default), enter LeashReturn state
  - Encounter bubble: All enemies with LOS within 12-tile radius join combat
  - Reference **AI_DESIGN.md § 9 (Overworld-AI), § 2 (Factions defaults)**
- **Acceptance**:
  - [ ] FSM transitions correctly (idle→patrol→chase→engage)
  - [ ] Leash returns AI to spawn zone if pulled too far
  - [ ] Encounter bubble includes all nearby hostiles with LOS
- **Tests**:
  - [ ] FSM state transition tests
  - [ ] Leash return tests (distance checks)
  - [ ] Encounter bubble tests (LOS + radius)

### 8. **TASK-M2-AI-07.md**: AI-vs-AI Combat (Multi-Faction Encounters)
- **Title**: "AI-vs-AI Combat & Multi-Faction Encounters"
- **Artifacts**: `game/systems/ai_vs_ai.py`, `tests/systems/test_ai_vs_ai.py`
- **DependsOn**: TASK-M2-AI-03 (Tactics), TASK-M2-AI-04 (Factions), TASK-M2-09 (Combat KI)
- **Notes**:
  - Enable AI actors to target **any hostile faction** (not just player)
  - Combat resolution uses same systems (TASK-M2-04, M2-08, M2-09)
  - Handle 3+ way fights (e.g., Player + Orcs + Undead):
    - Each actor picks target via utility scoring (threat, mutual enemy bias)
    - Turn order respects initiative
  - Loot from AI-killed enemies goes to "world drops" (player can loot corpses)
  - Reference **AI_DESIGN.md § 2 (AI-vs-AI), § 12 (QA-Szenarien #1: 3-Wege-Fight)**
- **Acceptance**:
  - [ ] AI actors correctly target hostile factions (not just player)
  - [ ] 3-way fights resolve correctly (all actors get turns)
  - [ ] Loot drops are accessible to player after AI-vs-AI kills
- **Tests**:
  - [ ] AI-vs-AI unit tests (Orc kills Undead)
  - [ ] 3-way fight integration tests (seeded)
  - [ ] Loot drop tests (AI kill → world drop → player loot)

---

## Critical Requirements
1. **Follow existing task schema EXACTLY** (see TASK-M1-01.md, TASK-M2-01.md as examples)
2. **Created date**: 2025-10-25
3. **Owner**: Copilot Agent
4. **Status**: Proposed
5. **Priority**: P0 for core tasks (M2-AI-01, 02, 03, 04), P1 for extensions (05, 06, 07)
6. **Cross-references**:
   - Link to **AI_DESIGN.md** sections explicitly (e.g., "Reference AI_DESIGN.md § 3")
   - Link to data files (e.g., "Load behaviors.json, tactics.json")
   - Link to existing tasks (e.g., "DependsOn: TASK-M2-06")
7. **Artifacts**:
   - Always include implementation file (`game/systems/ai_*.py`)
   - Always include test file (`tests/systems/test_ai_*.py`)
8. **Acceptance criteria**: Concrete, testable, no vague language
9. **Tests**: Emphasize determinism (seeded RNG), headless (no Arcade/GL)

---

## Output Format
Generate **8 separate Markdown files**:
- `docs/tasks/TASK-M2-AI.md` (umbrella)
- `docs/tasks/TASK-M2-AI-01.md`
- `docs/tasks/TASK-M2-AI-02.md`
- `docs/tasks/TASK-M2-AI-03.md`
- `docs/tasks/TASK-M2-AI-04.md`
- `docs/tasks/TASK-M2-AI-05.md`
- `docs/tasks/TASK-M2-AI-06.md`
- `docs/tasks/TASK-M2-AI-07.md`

Each file must:
- Start with `- [ ] ID: TASK-M2-AI-XX`
- Follow schema exactly
- Include all required fields
- Have 3-5 concrete Acceptance criteria
- Have 2-4 deterministic Tests

---

## Validation Checklist (Run After Generation)
- [ ] All 8 files created
- [ ] All files follow schema (ID, Title, Status, Priority, Owner, Created, Artifacts, DependsOn, Notes, Acceptance, Tests)
- [ ] All cross-references to AI_DESIGN.md are correct
- [ ] All data file references (behaviors.json, tactics.json, factions.json, blackboard_keys.json) are present
- [ ] DependsOn chains are logical (no circular deps, no missing prerequisites)
- [ ] Run `pre-commit run --files docs/tasks/TASK-M2-AI*.md` (should pass)
