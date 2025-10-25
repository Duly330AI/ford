Analyse von DUNGEON_GENERATOR.md
Gesamtstatus: Dieses Dokument beschreibt eine deutlich erweiterte und thematisch reichere Vision für die Dungeon-Generierung, die über die Grundlagen des ursprünglichen Milestone 1 hinausgeht.
Die grundlegende algorithmische Basis (BSP-Generator) ist abgedeckt.
Die weiterführenden Gameplay-Schichten (Biome, thematisches Tagging, Threat-Budget-Spawning) sind nicht in den aktuellen Tasks abgedeckt und stellen neue Anforderungen dar.
✅ Abgedeckte Aspekte
Die fundamentalen, strukturellen Teile des Generators sind durch bestehende Tasks gut abgedeckt:
BSP-Algorithmus (Splitting, Room-Carving, Corridors):
Dies ist die Kernimplementierung von TASK-M1-01 (BSP-Dungeon-Generator). Die Task fordert explizit einen rekursiven BSP-Generator, der Räume und Korridore aus einem Grid-Modell erstellt.
Die im DUNGEON_GENERATOR.md genannten Parameter (min_room_w, split_bias) wären die Konfigurationswerte für die in TASK-M1-01 zu implementierende Logik.
Reproduzierbarkeit (Seed-basiert):
Eine zentrale Anforderung in TASK-M1-01 ist die Verwendung eines injizierbaren, geseedeten RNG für deterministische Ergebnisse.
Validierung (Konnektivität):
TASK-M1-01 hat als explizites Akzeptanzkriterium einen "Connectivity-Test", der sicherstellt, dass alle Räume miteinander verbunden sind.
Basis-Parameter & Konfiguration:
Das Laden von Parametern aus JSON-Dateien wird durch TASK-M1-11 (Konfiguration & Seeds) abgedeckt.
Grundlegendes Debug-Overlay (F3):
TASK-M1-09 (Debug-Overlay (F3)) implementiert bereits die Anzeige von Seed und Koordinaten. Das Hinzufügen von "Depth" und "Threat" wäre eine Erweiterung dieser bestehenden Task.
❌ Lücken und fehlende Tasks
Das Dokument führt mehrere signifikante neue Konzepte ein, für die es derzeit keine entsprechenden Tasks gibt. Diese würden neue Features darstellen, die über M1-M4 hinausgehen oder diese erweitern müssten.
Thematische Generierung & Biome (data/biomes/*.json):
Lücke: Dies ist die größte und wichtigste neue Anforderung. Die Idee, dass ein "Biome" (crypt_undead) das Tileset, die Gegnerfraktionen, Reagenzien-Vorkommen, Loot-Tabellen und sogar Musik/Beleuchtung steuert, ist in keiner Task abgebildet. Die aktuelle M1-Generierung erzeugt nur eine generische, themenlose Struktur aus Wänden und Böden.
Benötigte Tasks: Hierfür wären neue Tasks erforderlich, z.B. "Implement Biome System", "Extend Tilemap Adapter to use Biome Tilesets", "Integrate Biome Faction data with Spawner".
Fortgeschrittenes Spawning (Threat-Budget & Encounter Tables):
Lücke: Das Dokument beschreibt einen detaillierten Algorithmus, der Gegner basierend auf einem "Threat-Budget" platziert, das mit der Tiefe skaliert. Es referenziert data/encounters/*.json. Die aktuellen Tasks definieren zwar Gegner (TASK-M2-07) und ihre KI (TASK-M2-AI), aber es gibt keine Task, die den Prozess des strategischen Platzierens dieser Gegner in einem prozedural generierten Level beschreibt.
Benötigte Task: Eine neue Task wie "Implement Threat-Budget Based Enemy Spawner" wäre notwendig.
Room Tagging:
Lücke: Das Konzept, Räume mit semantischen Tags wie altar, crypt, oder boss_antechamber zu versehen, um spezielle Features oder Begegnungen zu platzieren, ist eine neue Anforderung. Es gibt keine Task, die diese Funktionalität implementiert.
Erweiterte Debug-Tools:
Lücke: Die im Dokument geforderten Werkzeuge F4 (Reachability-Heatmap), F5 (Spawn-Overlay) und Ctrl+S (Map-Dump) sind spezifische neue Features, die in keiner bestehenden Debug- oder Tooling-Task geplant sind.
Fazit
Das DUNGEON_GENERATOR.md-Dokument dient als eine Art "Version 2.0" für die Level-Generierung.
Die in TASK-M1-01 geplante Arbeit liefert die strukturelle Grundlage (den "Rohbau" des Dungeons via BSP).
Dieses Spezifikationsdokument fügt jedoch entscheidende Gameplay- und Atmosphären-Schichten hinzu (den "Innenausbau" mit Themen, Biomen, strategischer Gegnerplatzierung und speziellen Räumen).
Um die Vision dieses Dokuments vollständig umzusetzen, müssten neue Tasks erstellt werden, die sich explizit mit dem Biome-System, dem Threat-Budget-Spawner, dem Room-Tagging und den erweiterten Debug-Tools befassen. Die aktuelle Task-Planung deckt diese fortgeschrittenen Konzepte nicht ab.
