# CODEX Configuration - FORD Project Gap Filling

## Location
**Full config:** `C:\Users\duly3\.codex\config.toml`

## Mission
Fill all 11 documentation gaps identified in `/docs/TODO/` by creating new task files in `/docs/tasks/`.

## Gap Categories

### Critical Gaps
1. **Magic System** - Core spell casting, fizzle, resist mechanics
2. **Dungeon Biomes** - Themed generation, room tagging, threat-budget spawning

### High Priority Gaps
3. **Economy & Vendors** - Price formulas, restock mechanics
4. **Procedural Itemization** - ARPG-style affix generation
5. **Quest System** - Event-driven quest engine

### Medium Priority Gaps
6. **Advanced Input** - Context-aware input, rebinding UI, gamepad
7. **Audio System** - Mixer buses, 3D sound, context-based selection
8. **Tutorial/FTUE** - Character creation, scripted events, tutorial manager

### Low Priority Gaps
9. **Localization** - i18n service, validation tooling
10. **Documentation** - Art style guide, world bible integration
11. **Master Summary** - Integration report, roadmap

## Execution Flow
1. Run `codex` from project root
2. Phases execute sequentially with approval gates
3. Each phase creates task files in `/docs/tasks/`
4. Final master report in `codex_outputs/phase11_master_task_report.md`

## Output
- **40+ new task files** in `/docs/tasks/` following TASK-*.md convention
- **11 phase summaries** in `codex_outputs/`
- **Master integration report** with dependency graph and roadmap

## Design Constraints
- All systems data-driven (parameterized in JSON)
- Core systems testable without Arcade (no rendering deps)
- Usage-based skill progression
- Seeded RNG for deterministic tests
- Follow existing M1-M6 milestone structure
