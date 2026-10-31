# Testseite und Freigabeprozess

## Adressen
- Offiziell: https://kolle1979.github.io/powder-lab/
- Vorschau: https://kolle1979.github.io/powder-lab/test/
Beide Seiten sind öffentlich und ohne Anmeldung spielbar. Ein Entwicklungscommit allein ist kein erfolgreicher Pages-Deployment-Nachweis.

## Verbindlicher Ablauf
1. Im Entwicklungsstand nur beauftragte Änderungen durchführen.
2. Syntax, neue und bestehende Funktionen lokal/automatisiert prüfen; tatsächliche Ergebnisse dokumentieren.
3. Geprüfte eigenständige HTML-Datei unter test/index.html bereitstellen, offizielle index.html unverändert lassen. Pages nutzt main / (root); die Vorschau muss in dieser Veröffentlichungsquelle liegen. Ein Branch allein erzeugt keinen Testlink.
4. Nutzer prüft am PC und auf echtem iPhone/iPad. RC-Kennzeichnung kontrollieren; simuliertes Touch ist kein Gerätetest. Ausstehende Prüfungen offen nennen.
5. Ausdrückliche Freigabe für den getesteten Stand abwarten. Testveröffentlichung ist keine offizielle Freigabe.
6. Rückweg sichern; nur freigegebenen Spielcode per Pull Request zur offiziellen index.html machen. Versionsmetadaten bewusst anpassen, die resultierende Datei erneut testen. Keine zusätzlichen ungetesteten Änderungen.
7. Nach Merge und erfolgreichem Deployment Hauptlink kontrollieren. Bei Problemen vorherigen Stand per neuem Commit wiederherstellen, kein Force-Push.

## Vorschau 1.2.1-rc.1
Basis 1.2.0: Git-Blob e14c145c8e3f26b9108bfc8f3bdbcb038af02b75. Nur sichtbares div mit id=hint entfernt und Versionskennzeichnung geändert. Linke Anleitung, FPS, Eingabe, Physik, Rendering und Layout unverändert. Ungenutzte hint-CSS-Regeln absichtlich nicht angefasst. Vor Vorschau-Upload: Syntaxprüfung und 12 Chromium-Checks bestanden.

## Freigabe für 1.2.1
Nutzer erklärte am 31.10.2026 um 08:41 CET, alles getestet zu haben, und erteilte die offizielle Freigabe. Einzelne Geräte-/Browser-Versionen wurden nicht genannt. Dies wird als Nutzerbericht dokumentiert, nicht als unabhängige Geräte-Zertifizierung.

Freigegebener Vorschau-Blob: 7dd804c66dd240e4529d722f11d88d1967c82c10. Finaler 1.2.1-Blob: 705003e3e506826edc81505c61e3b8d783e33e39. Exakter Vergleich bestätigt ausschließlich den Ersatz 1.2.1-rc.1 durch 1.2.1. Testdatei bleibt unverändert erhalten.

Finale Prüfung vor Release-Commit: Node.js-Syntaxprüfung plus 29 bestandene Chromium-Checks (17 offizielle Datei, 12 Vorschau/Vergleich). Kein CI-Lauf behauptet. Veröffentlichung nach main und erfolgreicher offizieller Live-Aufruf müssen anschließend separat bestätigt werden.

Rücksetzpunkt der bisherigen 1.2.0: a73d7f4424519856836903bbb639ababeac9932f:index.html. Bisheriger Spielstand zusätzlich in version/1.2.0; release/1.1.0 bleibt erhalten.

## Wiederholen
```sh
python -m pip install playwright
python -m playwright install chromium
python tests/test_v120.py
python tests/test_preview.py
```
Historischer Dateiname test_v120.py prüft nun Release 1.2.1. test_preview.py prüft erhaltene Vorschau und Gleichheit mit dem Release nach Normalisierung der Versionskennzeichnung. Bei neuen Kandidaten Erwartungen bewusst anpassen und erneut prüfen; Assertions nicht bloß entfernen.
