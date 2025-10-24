Gamename "FORD" 
Single-Player 2D-Dungeon-Crawler in Python mit der "arcade"-Engine. Stil: Roguelike-Pixel (16×16 skaliert auf 64px). Keine eigenen Texturen erstellen; nutze Platzhalter aus frei verfügbaren CC0-Assetpacks und strukturiere den Code so, dass Assets später leicht austauschbar sind.

Technische Leitplanken:
- Rundenbasierende Kämpfe (Angriff/Verteidigung/Effekte/etc. werden gewürfelt).
- Python 3.13.5+, arcade >= 3.x, strukturiertes Projekt mit Poetry.
- Auflösung 1920×1080, Pixel-Perfect (integer scale), Kamera folgt Spieler.
- Tilemaps: lade aus Tiled (.tmx) ODER erzeuge prozedural via BSP (Rooms + Corridors) in ein grid und konvertiere zu arcade.TileMap-Layern.
- Layers: ground, walls (collidable), decals, light-blockers, entities.
- Rendering: SpriteList pro Layer; nutze Light- und Particle-System von arcade (Fackeln, Trefferfunken, Staub).
- Physik/Kollision: AABB, Bewegung mit dt, Diagonalen erlauben, Slopes nicht nötig.
- UI: arcade.gui (Healthbar, Stamina/Mana, Hotbar 10 Slots, Tooltip bei Hover).
- Audio: Platzhalter-SFX (Schritt, Schlag, Treffer, Pickup).

Gameplay:
- Player: 8-Wege, Dodge-Roll (Invulnerability frames), Ausdauer.
- Combat: Nah (Schwert), Fern (Bogen + Pfeilverbrauch), Magie (Manakosten + Cast-Zeit). Crit-Chancen, iFrames, On-hit Partikel.
- Gegner: 3 Basistypen (Melee, Ranged, Caster), FSM (idle/patrol/chase/attack/flee).
- Skills (usage-based): swords, archery, sorcery, lockpicking, mining, woodcutting, alchemy, smithing, healing. Skill steigt beim Nutzen, mit Cap (z.B. 100).
- Berufe/Nodes: Erzadern, Bäume, Kräuter mit Respawn-Timer; Tool-Checks (Pickaxe, Axe).
- Crafting: an Stationen (Forge, Alchemy Table). Rezepte in JSON (input items + Mengen → output + Zeit; Skill-Mindestwerte).
- Loot: gewichtete Tabellen pro Gegnertyp/Tier, Seltenheit (common/rare/epic), Gold, Mats.
- Save/Load: Player-Stats, Skills, Inventar, aktiver Dungeon-Seed.

Daten-Driven:
- `data/items.json` (id, name, type, stack, rarity, dmg/armor/mods)
- `data/skills.json` (id, cap, xp_curve, decay?)
- `data/recipes.json` (inputs, tool, station, output, time, min_skill)
- `data/monsters.json` (hp, speed, ai, drops)
- `data/loot_tables.json` (table_id, entries[ item_id, weight, min/max ])

Projektstruktur:
- `game/`
  - `main.py` (App/Scenes bootstrap)
  - `scenes/` (MainMenu, Dungeon, Inventory/Crafting)
  - `ecs/` (optional, kleine Systems: movement, combat, ai)
  - `assets/` (fonts/sfx/temp tiles)
  - `data/` (json files)
  - `systems/` (skills.py, crafting.py, loot.py, save_load.py)
  - `entities/` (player.py, enemy.py, projectiles.py)
  - `util/` (rng, tilemap.py, lighting.py, particles.py)

Minimum Viable Milestones & Abnahmen:
M1 (Laufen & Licht):
- Prozeduraler Dungeon (BSP), Wände kollidieren, Spieler bewegt sich mit dt.
- Kamera, Light-Layer (Fackel um Spieler), 60 FPS bei 1280×720.
M2 (Kampf & Gegner):
- 3 Gegnertypen mit FSM, Hitboxes, Trefferfeedback (Particles, Screen-Shake).
M3 (Skills & Loot):
- usage-based Skills steigen, Loot-Tabellen greifen, Inventar/Hotbar funktionieren.
M4 (Berufe & Crafting):
- Sammeln an Nodes (Erz/Holz/Kräuter), Crafting an Stationen mit JSON-Rezepten.
M5 (Save/Load):
- Vollständiger Spielstand wird gespeichert/geladen.

Qualitätskriterien:
- Kein eigenes Artwork nötig, aber saubere Platzhalter & klare Abstraktionsschichten (Assets leicht austauschbar).
- 2000+ Entities im Dungeon sollen nicht die FPS unter 60 drücken (Culling, SpriteLists).
- Modularer Code, Type Hints, Docstrings, kleine Funktionen, keine God-Objects.
- Ein `make run`/`poetry run python -m game.main` startet das Spiel ohne Setup-Schmerz.

Bonus (optional):
- Shader-Vignette/Scanlines, Crit-Popup-Numbers, 