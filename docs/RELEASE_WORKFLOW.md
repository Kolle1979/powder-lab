# Testseite und Freigabeprozess

## Feste Adressen
- Offiziell: https://kolle1979.github.io/powder-lab/
- Vorschau: https://kolle1979.github.io/powder-lab/test/

Die Vorschau ist öffentlich und ohne Anmeldung spielbar, nicht vertraulich. Die Adresse funktioniert erst nach erfolgreicher Pages-Bereitstellung. Dieser Commit allein bestätigt keinen erfolgreichen Live-Aufruf.

## Verbindlicher Ablauf
1. Im Entwicklungsstand nur beauftragte Änderungen durchführen.
2. Syntax, betroffene Funktionen und bestehende Bedienung lokal/automatisiert prüfen. Testskripte und tatsächliche Ergebnisse dokumentieren.
3. Geprüfte eigenständige HTML-Datei als test/index.html bereitstellen; offizielle index.html im Hauptordner unverändert lassen. Pages bleibt auf main / (root). Die Testdatei muss deshalb ebenfalls in der Veröffentlichungsquelle liegen.
4. Testlink am PC sowie auf echtem iPhone/iPad prüfen. RC-Versionsanzeige kontrollieren, damit nicht versehentlich die offizielle Fassung getestet wird. Simuliertes Touch ersetzt den Gerätetest nicht.
5. Ausdrückliche Freigabe des Nutzers für den getesteten Stand abwarten. Feedback oder Freigabe der Vorschau-Infrastruktur ist keine automatische offizielle Freigabe.
6. Vorherigen offiziellen Stand sichern. Geprüften Spielcode per Pull Request zur offiziellen index.html machen; Versionsmetadaten bewusst anpassen und die resultierende Datei erneut prüfen. Keine zusätzlichen ungetesteten Änderungen.
7. Nach erfolgreichem Deployment den unveränderten Hauptlink prüfen. Bei Problemen den vorherigen Stand mit einem neuen Commit wiederherstellen, nicht per Force-Push.

## Erste Vorschau: 1.2.1-rc.1
Basis: offizielle 1.2.0, index.html mit Git-Blob e14c145c8e3f26b9108bfc8f3bdbcb038af02b75. Entfernt wird nur das sichtbare div mit id=hint unten an der Spielfläche. Zusätzlich Versionskennzeichnung als 1.2.1-rc.1. Linke Anleitung, FPS-Anzeige, Eingabe, Physik, Rendering und Layout bleiben bestehen. Nicht mehr verwendete hint-CSS-Regeln bleiben absichtlich unangetastet.

Vor dem Upload: Node.js-Syntaxprüfung und 12 bestandene Checks mit tests/test_preview.py in Chromium: exakter Änderungsumfang, fehlende Hinweiszeile, erhaltene linke Anleitung, Versionsanzeige, Maus-/Touch-Malen/Radieren, drei Fenstergrößen, keine JavaScript-Fehler und unveränderte offizielle Datei. Kein echter iOS-Gerätetest; dieser folgt durch den Nutzer am Testlink. Keine CI-Prüfung oder erfolgreiche öffentliche Bereitstellung behauptet.

## Tests wiederholen
Nur für Entwicklung, nicht zum Spielen:
```sh
python -m pip install playwright
python -m playwright install chromium
python tests/test_preview.py
```
Der Test ist gezielt an den Vergleich 1.2.0 zu 1.2.1-rc.1 gebunden. Bei weiteren RCs den erwarteten Änderungsumfang bewusst aktualisieren und erneut ausführen; nicht bloß Assertions entfernen.

Noch offen: erfolgreicher Live-Aufruf der Testseite, echter iPhone-/iPad-Test und ausdrückliche Freigabe für eine offizielle 1.2.1. Die offizielle 1.2.0 wird durch diese Vorschau nicht ersetzt.
