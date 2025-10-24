- [ ] ID: TASK-M5
  Title: M5 - Save & Load
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Notes:
  **Scope:** Persistentes Speicher-/Ladesystem mit Versionierung & Migration, Save-Slots (manual/auto/quick), atomaren Writes, Integritaets-Checks und Wiederherstellung bei Korruption. Inklusive Autosave, QuickSave/Load-Adapter, Slot-UI und optionale Thumbnails.  
  **Ziel:** Vollstaendig deterministisches Save/Load, robust (<50 ms typische Saves), validiert & dokumentiert. Alle Kernsysteme (Combat, Loot, Crafting, Nodes, Skills) werden ueber Contract & Validator abgebildet.
  
  ---
  
  ## Leitplanken (M5-weit)
  - **Tests verpflichtend**: Unit + Integration + Korruption + Migration + Performance.
  - **Determinismus**: RNG-Streams & Timekeeper-State werden persistiert; `PYTHONHASHSEED=0`.
  - **Atomare Saves**: tmp -> rename() -> fsync; Manifest/Slots konsistent halten.
  - **Backward-Kompatibilitaet**: Versionierung + Migrationen (vN -> vN+1) mit Tests.
  - **Keine Arcade-Abhaengigkeit** in Serializer/Validator; UI nur ueber Adapter.
  
  ---
  Subtasks:
  - [TASK-M5-01](./TASK-M5-01.md) - Save-Schema-Definition & Validatoren (v1)
  - [TASK-M5-02](./TASK-M5-02.md) - Save-Contract Implementierung (to_dict/from_dict)
  - [TASK-M5-03](./TASK-M5-03.md) - Serializer (JSON/Gzip + MsgPack, Checksummen)
  - [TASK-M5-04](./TASK-M5-04.md) - Atomic File Writer (tmp -> rename -> fsync)
  - [TASK-M5-05](./TASK-M5-05.md) - Save-Metadaten & Manifest (Slots, Versions, History)
  - [TASK-M5-06](./TASK-M5-06.md) - Save-Slots Manager (create/list/load/delete)
  - [TASK-M5-07](./TASK-M5-07.md) - Save-Service/Fassade (sync/async Hooks, Signals)
  - [TASK-M5-08](./TASK-M5-08.md) - Autosave Scheduler & Rate Limiter
  - [TASK-M5-09](./TASK-M5-09.md) - QuickSave/QuickLoad UI Adapter
  - [TASK-M5-10](./TASK-M5-10.md) - Save-Policy Guard (verb. Phasen, Fehlermeldungen)
  - [TASK-M5-11](./TASK-M5-11.md) - Migration Framework (v1 -> v2)
  - [TASK-M5-12](./TASK-M5-12.md) - Save-Validator (Referenzen, Balancing)
  - [TASK-M5-13](./TASK-M5-13.md) - Korruptions-Recovery & Fallback
  - [TASK-M5-14](./TASK-M5-14.md) - Performance Benchmark (Dump + Write < 50 ms)
  - [TASK-M5-15](./TASK-M5-15.md) - E2E Save/Load Flow (Kampf -> Loot -> Craft -> Load)
  - [TASK-M5-16](./TASK-M5-16.md) - Slot-UI Erweiterung (Slotliste, Umbenennen, Loeschen)
  - [TASK-M5-17](./TASK-M5-17.md) - Thumbnail Adapter (optional)
  - [TASK-M5-18](./TASK-M5-18.md) - Dokumentation "Wie M5 pruefen" (README Abschnitt)
  Acceptance:
  - [ ] See docs/notes/milestone-acceptance.md#m5
  Tests:
  - [ ] Track per subtask
