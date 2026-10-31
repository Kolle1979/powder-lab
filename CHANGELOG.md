# Änderungsprotokoll

## 1.2.1 – Nutzerfreigabe erhalten, Veröffentlichung vorbereitet
- Untere Hinweiszeile an der Spielfläche entfernt; linke Anleitung bleibt erhalten.
- Freigegebene Vorschau 1.2.1-rc.1 unverändert übernommen, abgesehen von der Versionskennzeichnung 1.2.1. Kein zusätzlicher Spielcode.
- Nutzer bestätigte am 31.10.2026 den Test und die offizielle Freigabe. Einzelne Geräte-/Browser-Versionen sind nicht protokolliert.
- Finale Datei: Syntaxprüfung bestanden; 17 Release- und 12 Vorschau-Checks in Chromium bestanden.
- Testseite bleibt separat erhalten. Testregeln gelten weiter.
- Rücksetzpunkt 1.2.0: a73d7f4424519856836903bbb639ababeac9932f:index.html.
- Dieser Entwicklungscommit bestätigt noch keinen erfolgreichen offiziellen Pages-Aufruf und erstellt keinen Release-Tag.

## 1.2.1-rc.1
Öffentliche Testseite unter /test/ eingeführt, Hinweiszeile dort entfernt und Test-vor-Freigabe-Regeln in AGENTS.md sowie docs/RELEASE_WORKFLOW.md gespeichert. Offizielle 1.2.0 blieb dabei unverändert.

## 1.2.0
- Einheitliches Malen/Radieren für Linksklick, Finger und Stift; Rechtsklick löscht immer.
- Werkzeugstatus und größere, gegliederte linke Anleitung.
- Welt, Elemente, Physik und Rendering gegenüber 1.1.0 unverändert; gezielte Eingabe-/Hilfetextänderungen.
- Damals 17 kompakte sowie zuvor 29 ausführlichere Entwicklungschecks gemeldet.
- Über Pull Request #1 nach main übernommen; Nutzer bestätigte Funktion. Sicherungsbranch release/1.1.0 erhalten.

## Dokumentation zu 1.1.0
README, Startprompt, Architektur, Elemente, Testplan, Roadmap, Beitragsregeln, KI-Regeln und MIT-Lizenz ergänzt; keine damalige Spieländerung.

## 1.1.0
Erster gespeicherter Spielstand: 47356ae9c8a54a4a22c317d224caca57778db327.
Canvas-Skalierung, Fensteranpassung, Farbpalette, Pointer-Eingabe, Lebensdauer, Tick-Markierungen, Chunk-Aktivierung, Flüssigkeitspfade, Wärmeleitung und Explosionsketten gegenüber dem Entwicklungsentwurf korrigiert. Dunkle Oberfläche und Bedienkonzept beibehalten.
