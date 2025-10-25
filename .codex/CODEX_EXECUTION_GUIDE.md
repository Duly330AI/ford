# Codex Execution Guide: Task Generation

## Overview
This guide walks you through running Codex to generate **~47 missing TASK files** based on `CROSS_REFERENCE_ANALYSIS.md`.

**Estimated Total Time**: 2-3 hours (with review breaks)

---

## Prerequisites

### 1. Install Codex Extension (if not already installed)
```powershell
# Check if Codex is installed
code --list-extensions | Select-String "codex"

# If not installed, install from VS Code Marketplace
# Search: "Codex" or install via CLI (if available)
```

### 2. Verify Config Location
```powershell
# Config should be at:
C:\Users\duly3\.codex\config.toml

# Verify it exists:
Test-Path C:\Users\duly3\.codex\config.toml
```

### 3. Verify Prompt Files
```powershell
# Prompts should be at:
C:\noc_project\UNOC\ford\.codex\prompts\

# Verify all 4 exist:
ls C:\noc_project\UNOC\ford\.codex\prompts\
# Should show:
# - phase1_ai_tasks.md
# - phase2_mechanics_usables.md
# - phase3_ui_tasks.md
# - phase4_quality_validation.md
```

### 4. Ensure Clean Working Tree
```powershell
cd C:\noc_project\UNOC\ford
git status
# Should show: "nothing to commit, working tree clean"
# If not, commit or stash changes first
```

---

## Phase 0: Inventory & Analysis (10-15 min)

### Start Codex
```powershell
cd C:\noc_project\UNOC\ford
# Open VS Code in project root
code .
```

**In VS Code:**
1. Open Command Palette: `Ctrl+Shift+P`
2. Type: `Codex: Run`
3. Select your config: `C:\Users\duly3\.codex\config.toml`

### Phase 0 Execution
Codex will:
1. Read `docs/CROSS_REFERENCE_ANALYSIS.md`
2. Scan `docs/tasks/*.md` (95+ existing files)
3. Analyze task schema and numbering
4. Generate inventory report

**Output Files:**
- `codex_outputs/phase0_inventory.md`
- `codex_outputs/phase0_task_numbering_plan.md`

### Review Phase 0 Output
```powershell
cat codex_outputs/phase0_inventory.md
cat codex_outputs/phase0_task_numbering_plan.md
```

**Check:**
- [ ] Inventory correctly identifies existing tasks (should be ~95 tasks)
- [ ] Numbering plan shows:
  - M1 ends at TASK-M1-16
  - M2 ends at TASK-M2-18
  - M3 ends at TASK-M3-20
  - M4 ends at TASK-M4-20
  - M5 ends at TASK-M5-18
- [ ] Gap analysis matches CROSS_REFERENCE_ANALYSIS.md (47 missing tasks)

### Approve Phase 1
**In Codex UI (or VS Code):**
- Click "Approve" or confirm prompt: *"Review inventory report and task numbering plan. Approve to proceed with Phase 1?"*

---

## Phase 1: AI System Tasks (20-30 min)

### Phase 1 Execution
Codex will:
1. Read `docs/AI_DESIGN.md` (complete spec)
2. Read `data/behaviors.json`, `data/tactics.json`, `data/factions.json`, `data/blackboard_keys.json`
3. Read `.codex/prompts/phase1_ai_tasks.md`
4. Generate 8 task files (1 umbrella + 7 subtasks)

**Output Files:**
- `docs/tasks/TASK-M2-AI.md` (umbrella)
- `docs/tasks/TASK-M2-AI-01.md` (Perception & Threat)
- `docs/tasks/TASK-M2-AI-02.md` (Utility Scoring)
- `docs/tasks/TASK-M2-AI-03.md` (Tactics Integration)
- `docs/tasks/TASK-M2-AI-04.md` (Factions & Diplomacy)
- `docs/tasks/TASK-M2-AI-05.md` (Blackboard System)
- `docs/tasks/TASK-M2-AI-06.md` (Overworld AI FSM)
- `docs/tasks/TASK-M2-AI-07.md` (AI-vs-AI Combat)

### Review Phase 1 Output
```powershell
# Quick check: all files created?
ls docs/tasks/TASK-M2-AI*.md
# Should show 8 files

# Review umbrella task:
cat docs/tasks/TASK-M2-AI.md

# Spot-check one subtask:
cat docs/tasks/TASK-M2-AI-01.md
```

**Check:**
- [ ] All 8 files created
- [ ] Schema followed (ID, Title, Status, Priority, Owner, Created, Artifacts, DependsOn, Notes, Acceptance, Tests)
- [ ] Cross-references to AI_DESIGN.md present (e.g., "Reference AI_DESIGN.md § 3")
- [ ] Cross-references to data files (behaviors.json, tactics.json, factions.json, blackboard_keys.json)
- [ ] DependsOn chains logical (e.g., M2-AI-01 depends on M1-04, M2-11)
- [ ] Acceptance criteria concrete (3-5 items, testable)
- [ ] Tests specified (2-4 items, deterministic)

### Run Pre-Commit
```powershell
poetry run pre-commit run --files docs/tasks/TASK-M2-AI*.md
# Should pass (no errors)
```

**If errors:**
- Fix manually or ask Codex to regenerate
- Common issues: formatting, line length, trailing whitespace

### Approve Phase 2
**In Codex UI:**
- Click "Approve" or confirm: *"Review generated AI tasks. Approve to proceed with Phase 2?"*

---

## Phase 2: UO Mechanics & Usables Tasks (30-40 min)

### Phase 2 Execution
Codex will:
1. Read `docs/GAMEPLAY_ADDENDUM_UO.md`, `docs/USABLES_AND_CONTAINERS.md`, `docs/ARCHITECTURE_UO_ADDENDUM.md`
2. Read `data/progression_rules.json`
3. Read `.codex/prompts/phase2_mechanics_usables.md`
4. Generate 18 task files (1 umbrella + 17 subtasks)

**Output Files:**
- **Skill Progression (5)**: M3-21, M3-22, M3-23, M3-24, M3-25
- **Encounter & Dodge (2)**: M2-19, M2-20
- **Usables/Containers (7)**: TASK-M3-EXT.md (umbrella), M3-EXT-01..06
- **World Interactions (4)**: M4-21, M4-22, M4-23, M4-24

### Review Phase 2 Output
```powershell
# Check skill progression tasks:
ls docs/tasks/TASK-M3-2*.md
# Should show M3-21, M3-22, M3-23, M3-24, M3-25

# Check encounter/dodge tasks:
ls docs/tasks/TASK-M2-19.md docs/tasks/TASK-M2-20.md

# Check usables/containers:
ls docs/tasks/TASK-M3-EXT*.md
# Should show TASK-M3-EXT.md (umbrella) + M3-EXT-01..06

# Check world interactions:
ls docs/tasks/TASK-M4-2*.md
# Should show M4-21, M4-22, M4-23, M4-24

# Spot-check a few:
cat docs/tasks/TASK-M3-24.md   # Skill Progression Formula
cat docs/tasks/TASK-M3-EXT-02.md   # Locks & Lockpicking
cat docs/tasks/TASK-M4-21.md   # Levers/Buttons/Doors
```

**Check:**
- [ ] All 18 files created
- [ ] Schema followed
- [ ] Cross-references to GAMEPLAY_ADDENDUM_UO.md, USABLES_AND_CONTAINERS.md, progression_rules.json
- [ ] DependsOn chains logical (e.g., M3-24 depends on M3-06, M3-EXT-02 depends on M3-EXT-01)
- [ ] Acceptance criteria concrete
- [ ] Tests specified

### Run Pre-Commit
```powershell
poetry run pre-commit run --files docs/tasks/TASK-M3-2*.md docs/tasks/TASK-M2-19.md docs/tasks/TASK-M2-20.md docs/tasks/TASK-M3-EXT*.md docs/tasks/TASK-M4-2*.md
# Should pass
```

### Approve Phase 3
**In Codex UI:**
- Click "Approve" or confirm: *"Review generated UO Mechanics & Usables tasks. Approve to proceed with Phase 3?"*

---

## Phase 3: UI System Tasks (40-60 min)

### Phase 3 Execution
Codex will:
1. Read `docs/UI_SPEC_UO_STYLE.md` (900+ lines)
2. Read `.codex/prompts/phase3_ui_tasks.md`
3. Generate 18 task files (1 umbrella + 17 subtasks)

**Output Files:**
- `docs/tasks/TASK-M6-UI.md` (umbrella)
- `docs/tasks/TASK-M6-UI-01.md..TASK-M6-UI-17.md` (UI Framework, HUD, Initiative Bar, Character Window, Skills Window, Inventory UI, Container UI, Tooltip System, Spellbook, Crafting UI, Merchant, Cursor, Keybinds, Window Management, Accessibility, Event Bus, Error Messages)

### Review Phase 3 Output
```powershell
# Check all UI tasks:
ls docs/tasks/TASK-M6-UI*.md
# Should show 18 files (umbrella + 17 subtasks)

# Spot-check key tasks:
cat docs/tasks/TASK-M6-UI.md        # Umbrella
cat docs/tasks/TASK-M6-UI-01.md     # Framework
cat docs/tasks/TASK-M6-UI-02.md     # HUD
cat docs/tasks/TASK-M6-UI-05.md     # Skills Window
cat docs/tasks/TASK-M6-UI-08.md     # Tooltip System
```

**Check:**
- [ ] All 18 files created
- [ ] Schema followed
- [ ] Cross-references to UI_SPEC_UO_STYLE.md extensive (§ 2, § 3, § 4, etc.)
- [ ] DependsOn chains reference M3/M4 systems (inventory, skills, crafting)
- [ ] Priority correct (P0 for core, P1 for extensions, P2 for nice-to-have)
- [ ] Acceptance criteria concrete
- [ ] Tests specified

### Run Pre-Commit
```powershell
poetry run pre-commit run --files docs/tasks/TASK-M6-UI*.md
# Should pass
```

### Approve Phase 4
**In Codex UI:**
- Click "Approve" or confirm: *"Review generated UI tasks. Approve to proceed with Phase 4?"*

---

## Phase 4: Quality & Validation Tasks (15-20 min)

### Phase 4 Execution
Codex will:
1. Read `docs/ARCHITECTURE.md`
2. Read `.codex/prompts/phase4_quality_validation.md`
3. Generate 4 task files

**Output Files:**
- `docs/tasks/TASK-QUALITY-2.md` (Architectural Compliance Tests)
- `docs/tasks/TASK-QUALITY-3.md` (Commit Message Linting)
- `docs/tasks/TASK-M2-23.md` (Combat Rules Validation)
- `docs/tasks/TASK-M2-24.md` (Monster AI Field Mapping Extension)

### Review Phase 4 Output
```powershell
# Check quality tasks:
ls docs/tasks/TASK-QUALITY*.md docs/tasks/TASK-M2-2*.md
# Should show 4 files

# Review:
cat docs/tasks/TASK-QUALITY-2.md
cat docs/tasks/TASK-M2-23.md
```

**Check:**
- [ ] All 4 files created
- [ ] Schema followed
- [ ] Cross-references to ARCHITECTURE.md, combat_rules.json, monsters.json
- [ ] DependsOn chains logical
- [ ] Acceptance criteria concrete
- [ ] Tests specified

### Run Pre-Commit
```powershell
poetry run pre-commit run --files docs/tasks/TASK-QUALITY*.md docs/tasks/TASK-M2-2*.md
# Should pass
```

### Approve Phase 5
**In Codex UI:**
- Click "Approve" or confirm: *"Review generated Quality tasks. Approve to proceed with Phase 5?"*

---

## Phase 5: Index Update & Final Validation (10-15 min)

### Phase 5 Execution
Codex will:
1. Read `docs/task.md` (current index)
2. Update index with all new tasks
3. Add sections for M2-AI, M3-EXT, M6-UI milestones
4. Run pre-commit on `docs/task.md`
5. Generate summary report

**Output Files:**
- `docs/task.md` (updated)
- `codex_outputs/phase5_summary_report.md`

### Review Phase 5 Output
```powershell
# Check updated index:
cat docs/task.md

# Check for new sections:
# Should contain:
# - M2-AI milestone (7 tasks)
# - M3-EXT milestone (6 tasks)
# - M6-UI milestone (17 tasks)
# - Updated M2 section (M2-19, M2-20, M2-23, M2-24)
# - Updated M3 section (M3-21..25)
# - Updated M4 section (M4-21..24)

# Review summary report:
cat codex_outputs/phase5_summary_report.md
```

**Check:**
- [ ] All new task IDs present in index
- [ ] No duplicate IDs
- [ ] Milestone sections properly organized
- [ ] Summary report lists all 47 created tasks

### Run Pre-Commit
```powershell
poetry run pre-commit run --files docs/task.md
# Should pass
```

### Approve Final Commit
**In Codex UI:**
- Click "Approve" or confirm: *"Review updated task.md index and summary report. Ready to commit all changes?"*

---

## Final Steps: Commit & Push

### Review All Changes
```powershell
cd C:\noc_project\UNOC\ford
git status
# Should show:
# - 47 new TASK-*.md files
# - 1 modified docs/task.md
# - 2 new codex_outputs/*.md files (optional, can gitignore)
```

### Commit All Generated Tasks
```powershell
# Add all new task files:
git add docs/tasks/TASK-M2-AI*.md
git add docs/tasks/TASK-M3-2*.md docs/tasks/TASK-M2-19.md docs/tasks/TASK-M2-20.md
git add docs/tasks/TASK-M3-EXT*.md
git add docs/tasks/TASK-M4-2*.md
git add docs/tasks/TASK-M6-UI*.md
git add docs/tasks/TASK-QUALITY*.md
git add docs/task.md

# Add Codex outputs (optional):
git add codex_outputs/

# Commit:
git commit -m "feat(tasks): add 47 missing tasks from cross-reference analysis

Generated via Codex (5 phases, 3 hours):
- Phase 1: M2-AI milestone (7 AI system tasks)
- Phase 2: UO Mechanics & Usables (18 tasks: M3-21..25, M2-19/20, M3-EXT-01..06, M4-21..24)
- Phase 3: M6-UI milestone (17 complete UI tasks)
- Phase 4: Quality & Validation (4 tasks: QUALITY-2/3, M2-23/24)
- Phase 5: Index update (docs/task.md)

BREAKDOWN:
- AI System: 7 tasks (Perception, Utility Scoring, Tactics, Factions, Blackboard, Overworld FSM, AI-vs-AI)
- UO Skills Progression: 5 tasks (Stat Affinities, Anti-Macro, Skill Locks, Progression Formula, Stat Gains)
- Encounter & Dodge: 2 tasks (Encounter Bubble, Dodge Mechanics)
- Usables & Containers: 6 tasks (Container Core, Locks, Traps, Detect Hidden, Bash, Ownership)
- World Interactions: 4 tasks (Levers/Doors, Container Respawn, Reading/Lore, Crafting Pause)
- UI System: 17 tasks (Framework, HUD, Initiative Bar, Paperdoll, Skills UI, Inventory, Tooltips, Spellbook, Crafting UI, Merchant, Cursor, Keybinds, Window Mgmt, Accessibility, Event Bus, Messages)
- Quality: 4 tasks (Arch Compliance, Commit Linting, Combat Rules Validation, Monster AI Field Mapping)

Cross-references to:
- AI_DESIGN.md (7 tasks)
- GAMEPLAY_ADDENDUM_UO.md (7 tasks)
- USABLES_AND_CONTAINERS.md (6 tasks)
- UI_SPEC_UO_STYLE.md (17 tasks)
- progression_rules.json (5 tasks)
- behaviors.json, tactics.json, factions.json, blackboard_keys.json (7 tasks)

Coverage improvement: 45% → 95%

Closes gap identified in CROSS_REFERENCE_ANALYSIS.md.
Next step: Cross-reference injection (separate Codex run)."

# Push:
git push origin main
```

---

## Troubleshooting

### Codex Fails to Start
```powershell
# Check config syntax:
cat C:\Users\duly3\.codex\config.toml | Select-String "error"

# Check prompts exist:
ls C:\noc_project\UNOC\ford\.codex\prompts\

# Check VS Code Codex extension installed:
code --list-extensions | Select-String "codex"
```

### Pre-Commit Fails
```powershell
# Install pre-commit:
pipx install pre-commit

# Install hooks:
cd C:\noc_project\UNOC\ford
pre-commit install

# Run manually:
poetry run pre-commit run --all-files
```

### Schema Validation Fails
- Check task files follow schema exactly (ID, Title, Status, Priority, Owner, Created, Artifacts, DependsOn, Notes, Acceptance, Tests)
- Check Created date is "2025-10-25"
- Check Owner is "Copilot Agent"
- Check Status is "Proposed"
- Check Priority is P0/P1/P2

### Codex Hallucinates/Wrong Output
- Review prompts in `.codex/prompts/*.md` - ensure they reference correct source docs
- Re-run phase with stricter prompt (add examples from existing tasks)
- Manually fix generated tasks

### Git Merge Conflicts
```powershell
# If docs/task.md has conflicts:
git status
# Fix conflicts manually in docs/task.md
git add docs/task.md
git commit -m "fix: resolve task.md merge conflicts"
```

---

## Post-Generation: Cross-Reference Injection (LATER)

**DO NOT DO THIS NOW** - separate Codex run after review & merge.

### Next Codex Run: Cross-Ref Injection
1. Create new config: `C:\Users\duly3\.codex\config_crossrefs.toml`
2. Create prompt: `.codex/prompts/crossref_injection.md`
3. Run Codex to:
   - Read all TASK-*.md files
   - Identify missing cross-references (e.g., TASK-M2-02 should reference combat_rules.json)
   - Inject references into existing tasks (bulk edit)
4. Review, commit, push

**Estimated Time**: 1-2 hours

---

## Success Criteria

✅ **Phase 0**: Inventory report generated, numbering plan approved
✅ **Phase 1**: 8 AI tasks created, pre-commit passes
✅ **Phase 2**: 18 UO/Usables tasks created, pre-commit passes
✅ **Phase 3**: 18 UI tasks created, pre-commit passes
✅ **Phase 4**: 4 Quality tasks created, pre-commit passes
✅ **Phase 5**: `docs/task.md` updated, summary report generated
✅ **Final**: All 47 tasks committed & pushed, CI passes

**Coverage Score**: 45% → 95% ✅

---

## Appendix: File Counts Summary

| Phase | Milestone | Tasks | Files Generated |
|-------|-----------|-------|-----------------|
| 1 | M2-AI | 7 | 8 (1 umbrella + 7 subtasks) |
| 2a | M3 Skills | 5 | 5 (M3-21..25) |
| 2b | M2 Encounter | 2 | 2 (M2-19, M2-20) |
| 2c | M3-EXT Usables | 6 | 7 (1 umbrella + 6 subtasks) |
| 2d | M4 World | 4 | 4 (M4-21..24) |
| 3 | M6-UI | 17 | 18 (1 umbrella + 17 subtasks) |
| 4 | Quality | 4 | 4 (QUALITY-2/3, M2-23/24) |
| **Total** | | **47** | **48 task files** |

Plus:
- 1 updated index file (`docs/task.md`)
- 2 reports (`codex_outputs/phase0_inventory.md`, `codex_outputs/phase5_summary_report.md`)

**Grand Total: 51 files modified/created**

---

## Questions?

If Codex behaves unexpectedly or you need clarification:
1. Check this guide's Troubleshooting section
2. Review prompt files in `.codex/prompts/*.md`
3. Check Codex logs (if available in VS Code)
4. Review CROSS_REFERENCE_ANALYSIS.md for context

**Good luck!** 🚀
