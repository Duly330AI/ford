# Phase 0 Dependency Graph

```mermaid
graph TD
  G1[Magic System Backend]
  G2[Dungeon Biome System]
  G3[Economy Core]
  G4[Procedural Itemization]
  G5[Quest Engine]
  G6[Advanced Input]
  G7[Audio Mixer]
  G8[Tutorial / FTUE]
  G9[Localization]
  G10[Art Style Guide]
  G11[World Bible Alignment]

  G1 --> TASKM6UI09(Spellbook UI readiness)
  G1 --> G5
  G2 --> G4
  G2 --> G11
  G2 --> G3
  G3 --> TASKM6UI11(Merchant UI)
  G3 --> G4
  G4 --> TASKM3O8(Loot Tables)
  G5 --> G8
  G5 --> TASKM5O1(Save Schema)
  G6 --> TASKM6UIINPUT(Rebinding UI)
  G6 --> G8
  G7 --> TASKM4_15(Audio Hooks)
  G7 --> G8
  G8 --> TASKM5O1
  G8 --> G9
  G9 --> TASKM6UI(All UI tasks)
  G10 --> G2
  G10 --> G8
  G11 --> G2
```

## Sequencing Notes

- Ensure G1 and G2 complete before downstream High priority systems start.
- G3 and G4 can iterate in parallel once biome-driven loot tables exist.
- G5 must be operational before FTUE content to avoid duplicate quest scaffolding.
- G6 precedes any UI/UX work that consumes rebinding or gamepad support.
- G7 depends only on audio hooks; schedule alongside G6 for UX coherence.
- G9 blocks final polish for tutorial, quest journal, and UI copy.
- Documentation gaps (G10, G11) guide content production parallel to system work.
