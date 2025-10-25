- [ ] ID: TASK-M3-13
  Title: Waehrungsmodell (Gold als Item vs. Konto)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/currency.py`, `tests/systems/test_currency.py`
  DependsOn: TASK-M3-03
  Notes:
  Implementiere **Gold als Item** (stackbar, `value` dient Handel spaeter). Biete Wrapper-API `add_gold(n)`, `remove_gold(n)` als Komfort ueber Inventory.
  Acceptance:
  - [ ] Atomare Operationen; negativer Kontostand verhindert Transaktion.
  Tests:
  - [ ] Add/Remove, Fehlerfaelle, Zusammenspiel Inventar.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
