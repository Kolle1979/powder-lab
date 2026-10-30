# Änderungsprotokoll

## 1.2.0 – zur Veröffentlichung vorbereitet
- Einheitliches Malen/Radieren für Linksklick, Finger und Stift; Rechtsklick löscht immer.
- Sichtbarer Werkzeugstatus.
- Größere, gegliederte Kurzanleitung für Maus und iOS/Touch unter Sonstiges.
- Welt, Elemente, Physik und Rendering bleiben unverändert; nur Versionskonstante und gezielte Eingabe-/Hilfetextänderungen.
- Neuer ausführbarer Chromium-Test: 17 Checks bestanden. Die vorherige ausführlichere Entwicklungsprüfung meldete 29 bestandene Checks. Echtes iOS der neuen Fassung steht aus.
- Veröffentlichung als index.html unter demselben Spiel-Link vorgesehen; noch kein Deployment-Nachweis durch diesen Commit.
- Bisheriger Stand im Sicherungsbranch release/1.1.0 erhalten; kein Release-Tag angelegt.

## Dokumentation zu 1.1.0
README, Original-Startprompt, Architektur-/Codeanalyse, Elemente, Testplan, Roadmap, Beitragsregeln, KI-Arbeitsregeln und MIT-Lizenz ergänzt. Keine Änderung an index.html durch den damaligen Dokumentations-Commit.

## 1.1.0
Erster im Repository gespeicherter Spielstand; Erstveröffentlichungs-Commit: 47356ae9c8a54a4a22c317d224caca57778db327.

Gegenüber dem vorausgehenden Entwicklungsentwurf: vollständige Canvas-Hochskalierung und Fensteranpassung, Farbpalette und Pointer-Eingabe korrigiert; Lebensdauer und Tick-Markierungen erweitert; Chunk-Aktivierung, Flüssigkeitspfade, Wärmeleitung, Schießpulver und Bomben-Kettenreaktionen überarbeitet. Dunkle Oberfläche und Bedienkonzept beibehalten.
