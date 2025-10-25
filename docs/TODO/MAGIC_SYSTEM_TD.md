Analyse von MAGIC_SYSTEM.md
Gesamtstatus: Das Dokument beschreibt ein detailliertes und tiefgehendes Magiesystem, das dem UO-Vorbild folgt. Die Architektur und die bestehenden Tasks sind darauf vorbereitet, ein solches System aufzunehmen, aber die spezifische Implementierung der hier beschriebenen Kernmechaniken (Fizzle, Resist-Formeln, spells.json) ist nicht in den aktuellen Tasks abgedeckt. Es handelt sich um eine Spezifikation für ein neues, großes Feature-Set.
✅ Abgedeckte Aspekte (Grundlagen & Vorbereitung)
Die bestehenden Tasks schaffen die notwendigen Haken und die grundlegende Infrastruktur, auf der dieses Magiesystem aufbauen kann:
Casting als grundlegende Aktion:
TASK-M2-04 (Combat-Core) definiert Cast(spell,target) als einen der grundlegenden "Intents", die das Kampfsystem verarbeiten kann. Die Architektur hat also bereits einen Platz für die Magie-Aktion.
Existenz der Kernskills:
TASK-M3-06 (Skill-System) plant die Implementierung der Skills. Magery (als sorcery erwähnt), Meditation und Resist Spells würden als Teil dieses Systems angelegt. Die Task schafft die Grundlage, dass Charaktere diese Skill-Werte besitzen und steigern können.
Reagenzien als Items:
TASK-M3-02 (Items-Datenmodell) definiert, wie Items (einschließlich Reagenzien) strukturiert sind. Die in der Spezifikation genannten Reagenzien (Bloodmoss etc.) können als Items im Inventar (TASK-M3-03) existieren.
Schadens- und Stat-System-Integration:
Die Skalierung von Zauberschaden mit INT würde auf das in TASK-M2-02 definierte System für abgeleitete Werte zurückgreifen.
Element-Resistenzen sind Teil von TASK-M2-12 (Schadenstypen & Resistenzen).
Spellbook UI:
TASK-M6-UI-09 (Spellbook UI) ist die dedizierte Task für die Erstellung der Benutzeroberfläche des Magiesystems. Sie erwartet explizit, dass Daten wie Manakosten, Reagenzien und Wirkungsrunden aus einem Backend-System kommen, was die Notwendigkeit der hier beschriebenen Logik unterstreicht.
❌ Lücken und fehlende Tasks
Die gesamte Kernlogik, die das Magiesystem einzigartig macht, ist in keiner Task abgedeckt.
Core Magic System (systems/magic.py):
Lücke: Es gibt keine zentrale Task, die die Implementierung des Magiesystems selbst beschreibt. Dies würde die Logik umfassen, die einen Cast-Intent entgegennimmt und die folgenden Schritte durchführt.
Zauber-Daten & Schema (spells.json):
Lücke: Es gibt keine Task, die das Erstellen, Validieren und Laden von data/spells.json beschreibt. Die bestehenden Validierungs-Tasks (TASK-M3-01, TASK-M4-01) decken Zauber nicht ab.
Implementierung der Magie-Formeln (Fizzle & Resist):
Lücke: Die spezifischen und entscheidenden Formeln für Fizzle und Spell Resist (resist_spells vs. magery) sind in keiner Task zur Implementierung vorgesehen. TASK-M2-02 konzentriert sich auf physische Kampfattribute.
Verbrauch von Mana & Reagenzien:
Lücke: Während Mana als Ressource und Reagenzien als Items existieren können, gibt es keine Task, die die Logik implementiert, diese Ressourcen beim Zaubern tatsächlich aus den Pools des Charakters zu verbrauchen.
Cast Rounds & Meditation-Bonus:
Lücke: Das Konzept, dass Zauber mehrere Runden zum Wirken benötigen (cast_rounds) und dass dieser Wert durch Meditation beeinflusst werden kann, ist eine neue Mechanik, die in keiner Task geplant ist.
Fazit
Das MAGIC_SYSTEM.md-Dokument ist eine hervorragende Spezifikation für ein Feature, das derzeit nur in seinen Grundfesten geplant ist. Die bestehenden Tasks schaffen die "Anschlüsse" (ein Cast-Intent, Skills, Items), aber die "Maschine" selbst – die Kernlogik des Magiesystems – fehlt.
Um die Vision dieses Dokuments umzusetzen, wären mehrere neue Tasks erforderlich, darunter mindestens:
Implement Core Magic System (Casting, Fizzle, Cost Consumption)
Create and Validate data/spells.json and Schema
Extend Combat Formulas (TASK-M2-02) to include Magic Resist
Integrate Cast Rounds into Combat Turn Manager (TASK-M2-04)
Die UI-Task TASK-M6-UI-09 kann erst sinnvoll umgesetzt werden, wenn dieses Backend-System existiert.
