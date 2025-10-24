- [ ] ID: TASK-M4
  Title: M4 - Nodes, Berufe & Crafting
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Notes:
  **Scope:** Sammelbare **Nodes** (Erz, Baeume, Kraeuter) mit Respawn, **Berufe** (mining, woodcutting, alchemy, smithing) inkl. Skill-Hooks & Boni, **Crafting an Stationen** (Forge, Alchemy Table) mit Rezept-JSON, Queue & Produktionszeit, **Tool-Checks**, UI fuer Stationen & Fortschritt, Audio-Hooks.
  **Ziel:** Spieler kann Ressourcen sammeln -> verarbeiten -> Items craften. Alles ist **datengetrieben**, deterministisch testbar (Kernlogik ohne Arcade) und integriert sich in M2 (Combat) + M3 (Items/Inventory/Skills/Loot).

  ---

  ## Leitplanken (M4-weit)
  - **Tests verpflichtend** fuer Kernlogik (spawn, respawn, gather, tools, crafting, queue, recipes).
  - **Determinismus**: injizierbarer RNG (`random.Random(seed)`); `PYTHONHASHSEED=0`.
  - **Trennung**: `systems/*`, `util/*` **ohne Arcade** (reine Logik). Szenen/FX via duenne Adapter.
  - **Datengetrieben**: `data/recipes.json`, `data/nodes.json`, optional `data/stations.json` strikt validiert.
  - **Performance**: 2 000 Nodes tick/respawn-Check < **1 ms** reine Logik (CI-Richtwert).

  ---
  Subtasks:
  - [TASK-M4-01](./TASK-M4-01.md) - Rezept- & Node-Schemas + Validatoren
  - [TASK-M4-02](./TASK-M4-02.md) - Crafting-Core (Queue, Jobs, Zeit, Erfolg/Fail/Crit)
  - [TASK-M4-03](./TASK-M4-03.md) - Stationen-Registry & Scene-Adapter (Forge, Alchemy)
  - [TASK-M4-04](./TASK-M4-04.md) - Node-Datenmodell (Depletion, Respawn, Yield)
  - [TASK-M4-05](./TASK-M4-05.md) - Node-Spawner (Platzierung, Seeds, Distanzen, Biome)
  - [TASK-M4-06](./TASK-M4-06.md) - Gather-Interaktion (Tool-Checks, Dauer, Stamina, Yield)
  - [TASK-M4-07](./TASK-M4-07.md) - Beruf-Skill-Hooks & Boni (mining/woodcutting/alchemy/smithing)
  - [TASK-M4-08](./TASK-M4-08.md) - Crafting-UI (Queue, Progress, Input/Output, Fehlerfaelle)
  - [TASK-M4-09](./TASK-M4-09.md) - Blueprint-/Rezept-Entdeckung (Drops/Scrolls)
  - [TASK-M4-10](./TASK-M4-10.md) - Crafting-Outcome-Qualitaet (Fail/Success/Crit + Returns)
  - [TASK-M4-11](./TASK-M4-11.md) - Persistenz-Hooks (Queues, Node-State) - Vorbereitung M5
  - [TASK-M4-12](./TASK-M4-12.md) - E2E "Erz -> Barren -> Schwert craften -> Equip"
  - [TASK-M4-13](./TASK-M4-13.md) - Performance: 2 000 Nodes Tick/Respawn + Gather-Load
  - [TASK-M4-14](./TASK-M4-14.md) - World-Adapter fuer Nodes (Spawn/Despawn, Hitbox, Label)
  - [TASK-M4-15](./TASK-M4-15.md) - Audio-Hooks (Gather-Start/Success/Fail, Craft-Complete)
  - [TASK-M4-16](./TASK-M4-16.md) - Zeit- & Takt-Adapter (Overworld vs. Combat)
  - [TASK-M4-17](./TASK-M4-17.md) - Daten-Basis: Nodes & Rezepte (Startbestand)
  - [TASK-M4-18](./TASK-M4-18.md) - Balance-Konfig (Zeiten, Yields, Tool-Tiers)
  - [TASK-M4-19](./TASK-M4-19.md) - Fehlerfaelle & Rollbacks (Transaktionen hart absichern)
  - [TASK-M4-20](./TASK-M4-20.md) - Doku "Wie M4 pruefen" (README Abschnitt)
  Acceptance:
  - [ ] See docs/notes/milestone-acceptance.md#m4
  Tests:
  - [ ] Track per subtask
