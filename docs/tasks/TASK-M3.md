- [ ] ID: TASK-M3
  Title: M3 — Skills, Loot & Inventory/Hotbar
  Status: Proposed
  Milestone: M3
  Created: 2025-10-24
  Notes: Usage-based skills, loot tables and working hotbar/inventory.
  Artifacts:
  - `game/systems/skills.py`
  - `data/loot_tables.json`, `data/items.json`, `data/skills.json`
  Acceptance:
  - [ ] Skills gain XP on usage and persist
  - [ ] Loot tables produce drops according to weights
  - [ ] Inventory + Hotbar (10 slots) with UI tooltips

  Subtasks:
  - [ ] Create `data/items.json` schema and sample items
  - [ ] Implement skill XP curve and cap (e.g., 100)
  - [ ] Implement inventory data model + hotbar UI
