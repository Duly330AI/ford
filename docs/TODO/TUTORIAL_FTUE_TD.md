Analyse von TUTORIAL_FTUE.md
Gesamtstatus: Das Dokument beschreibt ein umfangreiches, gut durchdachtes und komplett neues Feature-Set, das die "First Time User Experience" (FTUE) abdeckt. Die aktuelle Task-Planung in den Milestones M1 bis M6 enthält keine der für dieses Tutorial notwendigen Implementierungen.
Die bestehenden Tasks schaffen die einzelnen Gameplay-Mechaniken (Bewegung, Kampf, Inventar), aber das Tutorial-System, das diese Mechaniken dem Spieler gezielt beibringt (durch Prompts, geskriptete Events, einen dedizierten Quest-Flow), ist vollständig neu.
✅ Abgedeckte Aspekte (Die zu lehrenden Mechaniken)
Die TASK-Dateien implementieren die Gameplay-Systeme, die im Tutorial gelehrt werden sollen. Das Tutorial-System würde also auf eine solide Basis aufbauen.
Phase 1: Character Creation: Die Grundlagen (Skills, Stats) werden in M2 und M3 geschaffen. Eine dedizierte "Character Creation Screen"-Task fehlt jedoch.
Phase 3: Movement & Interaction: Bewegung wird in TASK-M1-04 und TASK-M1-05 implementiert. Interaktion (E-Taste) ist Teil von M3-EXT und M4.
Phase 4: Inventory & UI: Inventar wird in TASK-M3-03 implementiert, die UI in TASK-M6-UI-06.
Phase 5: First Combat: Das Kampfsystem wird vollständig in Milestone M2 implementiert.
Phase 6: Quest Intro: Das Konzept von Quests wird im QUEST_SYSTEM.md beschrieben, aber wie dort analysiert, gibt es keine Implementierungs-Tasks dafür.
❌ Lücken und fehlende Tasks
Die gesamte Infrastruktur und Logik des Tutorials selbst ist in keiner Task abgedeckt.
Core Tutorial Manager (tutorial_manager.py):
Lücke: Es gibt keine Task, die ein zentrales System zur Verwaltung des Tutorial-Zustands implementiert. Dieses System müsste den Fortschritt des Spielers durch die Phasen verfolgen, kontextsensitive Prompts auslösen und den Zustand "Tutorial abgeschlossen" speichern.
Tutorial UI-Layer (tutorial_overlay.py):
Lücke: Es gibt keine UI-Task zur Erstellung des spezifischen Tutorial-Overlays (goldene Boxen, animierte Pfeile etc.). Die bestehenden UI-Tasks in M6 konzentrieren sich auf die regulären Spiel-Interfaces (Inventar, HUD etc.).
Geskriptete Events & Sequenzen:
Lücke: Das Tutorial erfordert eine Kette von geskripteten Ereignissen (z.B. "Spieler wacht im Bett auf", "NPC gibt dem Spieler ein Item", "spezieller Tutorial-Gegner spawnt"). Es gibt kein System oder eine Task, die eine solche Ereigniskette implementiert.
Character Creation Screen:
Lücke: Es gibt keine Task zur Implementierung eines Charaktererstellungs-Bildschirms, einschließlich der Logik für die Auswahl von Vorlagen oder die benutzerdefinierte Verteilung von Punkten.
Tutorial-spezifische Inhalte:
Lücke: Es gibt keine Task, die das Erstellen der spezifischen Inhalte für das Tutorial abdeckt, wie tutorial_quests.json oder die Dialoge und Platzierungen der abbey_npcs.json.
FTUE-Telemetrie:
Lücke: Es gibt keine Task, die ein Telemetrie-System implementiert, um die im Dokument genannten Metriken zu erfassen.
Fazit
Das TUTORIAL_FTUE.md-Dokument beschreibt ein neues, in sich geschlossenes Projekt, das auf den fertigen Gameplay-Systemen der Milestones M1-M6 aufbaut.
Es ist kein Versehen, dass diese Tasks fehlen; ein Tutorial ist typischerweise eine der letzten Komponenten, die entwickelt werden, da es auf stabilen Kernmechaniken aufbauen muss.
Um die Vision dieses Dokuments umzusetzen, wäre ein eigener, neuer Milestone (z.B. "M7 - New Player Experience") erforderlich, der die folgenden Hauptkomponenten umfasst:
Implementierung des Character Creation Screens.
Implementierung des Tutorial Managers (State-Tracking, Event-Scripting).
Implementierung des Tutorial UI-Overlays.
Erstellung aller benötigten Tutorial-spezifischen Daten (Quests, NPCs, Dialoge).
Optional: Implementierung eines Telemetrie-Systems.
Die aktuelle Task-Planung deckt keine dieser Anforderungen ab.
