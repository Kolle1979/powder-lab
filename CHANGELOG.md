# Änderungsprotokoll

## 1.2.3 – freigegebene Feuer-Korrektur
- Gemaltes Feuer in freier Luft verglüht kurz nach dem Setzen.
- Holz und Öl entzünden sich bei Kontakt mit Feuer und brennen weiter.
- Pause hält die Simulation an; nach dem Fortsetzen brennt Feuer weiter.
- Die getestete 1.2.3-rc.1 aus test/index.html wurde unverändert übernommen; ausschließlich die Versionskennzeichnung wurde auf 1.2.3 angehoben.

## 1.2.2 – freigegebene Bomben-Korrektur
- Bombe statisch wie Stein; Feuer/Lava zünden ohne Zufallsverzögerung.
- Zusammenhängende Flächen und Bomben im Explosionsradius explodieren im selben Simulationsschritt, ohne verzögerte Bombenreste. Entfernte Bomben außerhalb bleiben stehen. Schießpulver unverändert.
- Nutzer bestätigte am 31.10.2026 um 09:25 CET den Test und gab 1.2.2 offiziell frei.
- Exakt die freigegebene 1.2.2-rc.1 übernommen; ausschließlich Versionskennzeichnung geändert. Testseite unverändert erhalten.
- Finale Syntaxprüfung und 21 Release-Checks bestanden; die Vorschau hatte zuvor 34 Checks bestanden. Kein Live-Deployment- oder CI-Nachweis durch diesen Commit.
- Direkte Übernahme auf main ohne zusätzliche Branches. Rückweg: 5ecd1345bd35730a2644482f4a49c7578b82824a:index.html (1.2.1). Keine Branch-Löschung und kein Release-Tag in diesem Upload.

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
