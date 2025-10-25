- [ ] ID: TASK-M3-CRAFTING-15-Recipes
  Title: Loot-Rarity & Farbkonvention (+SFX Hooks)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `data/combat_rules.json` (oder `data/ui.json`)`, `game/util/feedback.py` (Ergaenzung)`, `tests/systems/test_rarity_map.py`
  DependsOn: TASK-M3-08
  Notes:
  Mappe Rarity -> Farbcode/Tooltip/optional SFX. Systems liefert nur Signale (Adapter), Scene spielt Effekte.
  Acceptance:
  - [ ] Konsistente Farb-Strings; keine GL-Abhaengigkeit.
  Tests:
  - [ ] Mapping/Defaults, fehlende Rarity -> Fallback.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
