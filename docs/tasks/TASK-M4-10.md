- [ ] ID: TASK-M4-10
  Title: Crafting-Outcome-Qualitaet (Fail/Success/Crit + Returns)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/crafting.py` (Erweiterung)`, `tests/systems/test_crafting_outcomes.py`
  DependsOn: TASK-M4-02
  Notes:
  Qualitaet beeinflusst Output-Menge/Mods (z. B. "well-forged" Schwert). `fail_returns` gibt Teil-Inputs zurueck.
  Acceptance:
  - [ ] Verteilung gemaess Rezeptfeldern & Skill-Boni.
  Tests:
  - [ ] Monte-Carlo ueber 10k Crafts (Seed) -> erwartete Raten.
