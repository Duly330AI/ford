- [ ] ID: TASK-M3-03
  Title: Inventory-Kern (Slots, Stacks, Split/Merge, Capacity)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/inventory.py`, `tests/systems/test_inventory.py`
  DependsOn: TASK-M3-02
  Notes:
  Gridloses Inventar mit **Slot-Anzahl** (z. B. 30) und optionalem **Gewichtslimit**. Funktionen: `add(item, qty)`, `remove(item_id, qty)`, `move(src,dst)`, `split_stack(src, qty)`, `merge(dst, src)`. Transaktionen **atomar** (all-or-nothing).
  Acceptance:
  - [ ] Stacks fuellen bis `max_stack`, Rest in naechste Slots.
  - [ ] Fehler bei ungenuegendem Platz oder Negativmengen.
  Tests:
  - [ ] Happy-Path, Volllauf, Splits/Merges, Kapazitaets-Fehler.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
