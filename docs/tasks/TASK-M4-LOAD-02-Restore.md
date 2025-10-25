- [ ] ID: TASK-M4-02
  Title: Crafting-Core (Queue, Jobs, Zeit, Erfolg/Fail/Crit)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/crafting.py`, `tests/systems/test_crafting_core.py`
  DependsOn: TASK-M3-02, TASK-M3-03, TASK-M4-01
  Notes:
  Reines Logikmodul:
        - `CraftingStationState` (queue, active_job, progress).
        - `enqueue(recipe_id, count)` prueft **Inputs**, **Tools**, **Skill-Min**; Reservierung aus Inventar (atomar).
        - `tick(dt)` erhoeht Fortschritt, bei Abschluss: Outputs ins Inventar (oder World-Drop via Adapter), Skill-XP, Erfolg/Fail/Crit je Rezept-Regeln.
        - **Pause-Regeln**: laeuft im Overworld-Takt; **pausiert im Combat** (Signal aus Szene, Adapter-Flag).
  Acceptance:
  - [ ] Enqueue validiert sauber & ist atomar (Rollback bei Fehler).
  - [ ] tick liefert deterministische Ergebnisse bei fixem Seed.
  Tests:
  - [ ] Mehrfachjobs, Parallelflag, Fail/Success/Crit, Inventar-Reservierung/Rueckgabe.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/INPUT_AND_REBIND.md
