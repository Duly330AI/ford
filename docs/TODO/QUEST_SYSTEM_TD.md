Analyse von QUEST_SYSTEM.md
Gesamtstatus: Das Dokument beschreibt ein gut strukturiertes, aber komplett neues Gameplay-System. Die aktuelle Task-Planung in den Milestones M1 bis M6 enthält keine Implementierung eines Quest-Systems. Die bestehende Architektur und die geplanten Systeme schaffen jedoch die notwendigen Grundlagen und Haken, an die ein solches System andocken könnte. Es handelt sich um eine Spezifikation für ein zukünftiges Feature.
✅ Abgedeckte Aspekte (Grundlagen & Haken)
Die bestehenden Tasks schaffen die Voraussetzungen, die ein Quest-System benötigen würde, um zu funktionieren:
Event-Quellen:
Das Quest-System ist event-getrieben. Die Systeme, die diese Events auslösen würden, sind in Planung:
onKill: Würde vom TASK-M2-04 (Combat-Core) ausgelöst, wenn ein Gegner stirbt.
onCollect: Würde vom TASK-M3-03 (Inventory-Kern) ausgelöst, wenn ein Item dem Inventar hinzugefügt wird.
onUseItem: Würde von TASK-M3-05 (Consumables & Use-Effects) ausgelöst.
Die Architektur ist also in der Lage, die nötigen Signale zu senden.
Anforderungen & Belohnungen:
Das Quest-System kann auf bestehende Systeme für Anforderungen und Belohnungen zurückgreifen:
level: Ein Level-System ist zwar nicht explizit in einer Task, aber die Skill- und Stat-Systeme bilden die Basis dafür.
skill: TASK-M3-06 (Skill-System) implementiert die Skills, deren Werte abgefragt werden können.
gold: TASK-M3-13 (Waehrungsmodell) implementiert die Gold-Währung.
item: TASK-M3-02 (Items-Datenmodell) implementiert die Items, die als Belohnung gegeben werden können.
UI-Platzhalter (Journal):
TASK-M6-UI-02 (HUD) plant die Implementierung eines "Journals". Aktuell ist es für das Loggen von Skill-Gains und Kampfergebnissen gedacht, aber es schafft den UI-Container, der später zu einem vollwertigen Quest-Journal erweitert werden könnte.
❌ Lücken und fehlende Tasks
Die gesamte Kernlogik und Datenverwaltung des Quest-Systems ist in keiner Task abgedeckt.
Core Quest Engine (systems/quests.py):
Lücke: Es gibt keine Task, die den zentralen "QuestEngine" implementiert. Dies beinhaltet die gesamte Logik zur Zustandsverwaltung (FSM: offered, active, succeeded), zur Verarbeitung der hooks und zur Aktualisierung des Quest-Fortschritts.
Quest-Daten & Schema (data/quests/*.json):
Lücke: Es gibt keine Task, die das Erstellen, Validieren und Laden von Quest-Definitionen aus data/quests/*.json beschreibt. Die bestehenden Validierungs-Tasks decken dieses neue Datenschema nicht ab.
Event-Listener-Implementierung:
Lücke: Während andere Systeme Events aussenden, gibt es keine Task, die die Quest-Engine als Empfänger dieser Events implementiert. Die Logik, die ein onKill-Event mit einem kill-Objective in einer aktiven Quest abgleicht, fehlt vollständig.
Persistenz des Quest-Status:
Lücke: Das Save/Load-System, das in Milestone M5 geplant ist, berücksichtigt den Quest-Fortschritt nicht. TASK-M5-01 (Save-Schema-Definition) und TASK-M5-02 (Save-Contract Implementierung) müssten erweitert werden, um den Zustand aller angenommenen, aktiven und abgeschlossenen Quests zu speichern und zu laden.
UI-Erweiterung für Quests:
Lücke: Das in TASK-M6-UI-02 geplante Journal ist nicht für die Anzeige von strukturierten Quest-Zielen, -Beschreibungen und -Belohnungen ausgelegt. Eine dedizierte Erweiterung oder eine neue UI-Task wäre erforderlich.
Fazit
Das QUEST_SYSTEM.md-Dokument beschreibt ein in sich geschlossenes, neues Feature, das perfekt in die geplante Architektur passt, aber dessen Implementierung nicht Teil der aktuellen Roadmap (M1-M6) ist.
Um die Vision dieses Dokuments umzusetzen, wäre ein neuer Milestone oder eine Epic-Task-Gruppe notwendig, die mindestens die folgenden Punkte abdeckt:
Implementierung des Core Quest Engine.
Erstellung des Daten-Schemas und Laders für quests.json.
Anbindung der Engine an den globalen Event-Bus.
Erweiterung des Save/Load-Systems um Quest-Daten.
Erweiterung der Journal-UI zu einem vollwertigen Quest-Log.
