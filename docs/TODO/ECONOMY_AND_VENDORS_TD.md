Analyse von ECONOMY_AND_VENDORS.md
Gesamtstatus: Das Dokument beschreibt ein neues, eigenständiges Gameplay-System. Die Grundlagen dafür (Items mit Wert, eine Währung) sind vorhanden. Das System wird von einer UI-Task erwartet, aber die Kernlogik für Händler, Preisberechnung und Restocks ist nicht in den aktuellen Tasks abgedeckt. Es handelt sich hierbei um eine Spezifikation für ein neues Feature-Set.
✅ Abgedeckte Aspekte (Grundlagen)
Die fundamentalen Bausteine, auf denen dieses System aufbauen würde, sind in den bestehenden Tasks geplant:
Item-Basiswert (base_value):
TASK-M3-02 (Items-Datenmodell) definiert, dass Items ein value-Feld haben. Dies dient als base_value für die Preisformel.
Währung (Gold):
TASK-M3-13 (Waehrungsmodell) implementiert Gold als stackbares Item und stellt Komfort-APIs (add_gold/remove_gold) bereit. Damit existiert die Währung, mit der gehandelt werden kann.
UI-Schicht (Merchant/Trade UI):
TASK-M6-UI-11 (Merchant/Trade UI) ist die dedizierte Aufgabe zur Erstellung der Benutzeroberfläche für den Handel. Wichtig ist hier die Anmerkung in der Task: "Prepare hooks for dynamic pricing while shipping a static prototype." Dies zeigt, dass die UI-Task ein Backend-System erwartet, das die Preislogik liefert, aber die Implementierung dieses Backends ist nicht Teil der UI-Task selbst.
❌ Lücken und fehlende Tasks
Das Dokument beschreibt eine vollständige Systemlogik, für deren Implementierung es derzeit keine Tasks gibt.
Core Economy & Vendor System:
Lücke: Es gibt keine Task wie Implement Economy System oder systems/vendor.py. Die gesamte Kernlogik – insbesondere die Preisformel (base_value *rarity_factor* quality_mod * vendor_modifier) – ist nirgendwo zur Implementierung zugewiesen.
Händler-Daten & Validierung (data/vendors/*.json):
Lücke: Es gibt keine Task, die das Erstellen, Validieren und Laden von data/vendors/*.json beschreibt. Die bestehenden Validierungs-Tasks (TASK-M3-01, TASK-M4-01) decken Händler-Daten nicht ab.
Restock-Mechanik:
Lücke: Die Logik, dass das Inventar eines Händlers sich über Zeit (restock_turns) wieder auffüllt, ist ein neues Feature. Es erfordert eine Anbindung an den Timekeeper (TASK-M4-16) und eine Zustandsverwaltung pro Händler, was in keiner Task geplant ist.
Gold-Sinks (Reparatur & Reisen):
Lücke (Reparatur-Logik): Während die UI-Tasks TASK-M6-UI-04 und TASK-M6-UI-06 "repair"-Kontextmenüs und -Vorschauen erwähnen, gibt es keine Backend-Task, die die Reparatur-Mechanik selbst implementiert (z.B. Kostenberechnung, Erfolgschance, Haltbarkeits-Update).
Lücke (Reisen & Quests): Schnellreise-Gebühren und Quest-Gebühren sind völlig neue Gameplay-Systeme, die in den aktuellen Tasks nicht vorkommen.
Fazit
Das ECONOMY_AND_VENDORS.md-Dokument beschreibt im Wesentlichen ein neues Milestone-Paket.
Die aktuelle Task-Planung schafft die Voraussetzungen (Items haben einen Wert, es gibt Gold), aber nicht das Handelssystem selbst. Um die Vision dieses Dokuments umzusetzen, müssten neue Tasks erstellt werden, darunter mindestens:
Eine Task für das Core-Wirtschaftssystem (Implementierung der Preisformel).
Eine Task für das Händler-Datenmanagement (Laden/Validieren von vendors.json).
Eine Task für die Restock-Logik.
Separate Tasks für die Implementierung der Gold-Sink-Mechaniken (Reparatur, Reisen etc.).
Die bestehende Task TASK-M6-UI-11 kann erst dann vollständig umgesetzt werden, wenn diese Backend-Systeme existieren.
