Analyse von LOCALIZATION.md
Gesamtstatus: Das Dokument beschreibt ein klares und professionelles System zur Internationalisierung (i18n). Die Architektur und die Konventionen des Projekts sind darauf vorbereitet, dieses System zu integrieren. Allerdings ist die tatsächliche Implementierung dieses Systems nicht Teil der aktuellen Task-Planung und wird in anderen Dokumenten explizit als zukünftige Arbeit ("Phase 3") deklariert.
✅ Abgedeckte Aspekte (Vorbereitung)
Die bestehenden Tasks und Konventionen schaffen die perfekten Voraussetzungen für die spätere Implementierung dieses Systems:
Architektonische Vorbereitung:
Das Dokument CONVENTIONS.md ist hier der entscheidende Punkt. Es legt bereits fest:
Die exakte Dateistruktur (/i18n/en.json, de.json).
Die Regel, dass Display-Namen aus Lokalisierungsdateien kommen sollen und IDs in den Daten-JSONs verwendet werden.
Es deklariert diese Arbeit explizit als "Future Phase 3", was erklärt, warum es keine Implementierungs-Tasks in den aktuellen Meilensteinen gibt.
UI-System-Design:
TASK-M6-UI und seine Sub-Tasks sind darauf ausgelegt, mit Lokalisierungs-Keys zu arbeiten. In TASK-M6-UI-01 wird "localization keys" als eines der Leitprinzipien für das UI-System genannt. Das bedeutet, die UI wird so gebaut, dass sie eine Funktion wie translate("ui.inventory.title") aufrufen kann, anstatt einen fest codierten String zu verwenden.
❌ Lücken und fehlende Tasks
Da es sich um ein zukünftiges Feature handelt, gibt es erwartungsgemäß keine Tasks für die Implementierung der Kernkomponenten.
Core Localization Service:
Lücke: Es gibt keine Task zur Erstellung eines zentralen Systems oder einer Klasse (z.B. LocalizationManager), die zur Laufzeit die *.json-Dateien lädt, die aktuelle Sprache verwaltet und eine Funktion wie translate(key, params) für den Rest des Spiels bereitstellt.
i18n Validierungs-Tooling:
Lücke: Es gibt keine Task, die die Erstellung des in der Spezifikation genannten Skripts tools/i18n/check_missing_keys.py beschreibt. Die bestehende Task TASK-TOOLING-1 richtet allgemeine Linter und Formatierer ein, aber nicht dieses projektspezifische Validierungswerkzeug.
CI-Integration der Validierung:
Lücke: Es gibt keine Task, die den CI-Workflow (.github/workflows/ci.yml) erweitert, um das check_missing_keys.py-Skript auszuführen und den Build bei fehlenden Schlüsseln abzubrechen.
