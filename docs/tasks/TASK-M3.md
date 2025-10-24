- [ ] ID: TASK-M3
  Title: M3 - Skills, Loot & Inventory/Hotbar
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Notes:
  **Scope:** Nutzungsbasierte **Skills** (Steigerung beim Verwenden), **Items** & **Inventory** (stackbar, equip/consume), **Hotbar** (10 Slots, Keybinds 1-0), **Loot-System** (gewichtete Tabellen, Raritaeten, Mengen, ggf. verschachtelte Tabellen), **Drops** (Monster-Death-Hooks), **Tooltips** & Basis-UI, Daten-Schemas + Validierung.  
  **Ziel:** Nach Abschluss von M3 besitzt FORD ein robustes, datengetriebenes Progressions- und Beutesystem. Spieler kann Items aufnehmen/ausruesten/verwenden, Skills steigen durch Nutzung, Gegner lassen loot gemaess Tabellen fallen. Alles ist **deterministisch testbar** und unabhaengig von Arcade render-logik.
  
  ---
  
  ## Leitplanken (M3-weit)
  - **Tests verpflichtend** fuer Kernlogik (skills, items, inv, loot, tables, validators).
  - **Determinismus**: RNG injizierbar (`random.Random(seed)`), `PYTHONHASHSEED=0`.
  - **Trennung**: `systems/*` & `util/*` **ohne Arcade**; UI/FX nur Adapter in `scenes/*`.
  - **Datengetrieben**: `data/*.json` strikt gegen Schemas validiert (IDs stabil).
  - **Performance**: 100k Loot-Rolls < **250 ms** in CI (reine Logik); Inventar-Operationen O(1) bis O(log n).
  
  ---
  Subtasks:
  - [TASK-M3-01](./TASK-M3-01.md) - Daten-Schemas & Validatoren (items/skills/loot_tables)
  - [TASK-M3-02](./TASK-M3-02.md) - Items-Datenmodell & Typen (weapon/armor/consumable/material/currency)
  - [TASK-M3-03](./TASK-M3-03.md) - Inventory-Kern (Slots, Stacks, Split/Merge, Capacity)
  - [TASK-M3-04](./TASK-M3-04.md) - Equipment-Slots & Stat-Aggregation (weapon/offhand/armor/accessory)
  - [TASK-M3-05](./TASK-M3-05.md) - Consumables & Use-Effects (Heiltrank, Buff, Cleanse)
  - [TASK-M3-06](./TASK-M3-06.md) - Skill-System (usage-based XP, Cap, Level-Boni)
  - [TASK-M3-07](./TASK-M3-07.md) - Skill-Hooks in Combat & Nodes (Integration)
  - [TASK-M3-08](./TASK-M3-08.md) - Loot-Tabellen (Gewichte, Mengen, Nested Tables)
  - [TASK-M3-09](./TASK-M3-09.md) - Drop-Hooks bei Gegner-Death (Integration mit M2)
  - [TASK-M3-10](./TASK-M3-10.md) - World-Drops & Pickup-Adapter (Scene-Stubs)
  - [TASK-M3-11](./TASK-M3-11.md) - Hotbar (10 Slots) & Keybinds (1-0) + Quick-Use
  - [TASK-M3-12](./TASK-M3-12.md) - Tooltips & Rarity-UI (Adapter)
  - [TASK-M3-13](./TASK-M3-13.md) - Waehrungsmodell (Gold als Item vs. Konto)
  - [TASK-M3-14](./TASK-M3-14.md) - Pfeilverbrauch & Munition-Handling (Archery)
  - [TASK-M3-15](./TASK-M3-15.md) - Loot-Rarity & Farbkonvention (+SFX Hooks)
  - [TASK-M3-16](./TASK-M3-16.md) - Persistenz-Vorbereitung (IDs stabil, Save-Hooks)
  - [TASK-M3-17](./TASK-M3-17.md) - Performance: Loot-Monte-Carlo & Inventory-Mikros
  - [TASK-M3-18](./TASK-M3-18.md) - Integrationsszenario "Kampf -> Drop -> Pickup -> Equip/Use"
  - [TASK-M3-19](./TASK-M3-19.md) - Daten-Basisbestand (10 Items, 2 Tabellen, Skills)
  - [TASK-M3-20](./TASK-M3-20.md) - Doku "Wie M3 pruefen" (README Abschnitt)
  Acceptance:
  - [ ] See docs/notes/milestone-acceptance.md#m3
  Tests:
  - [ ] Track per subtask
