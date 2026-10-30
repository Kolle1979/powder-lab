# Testplan und Prüfstatus

## Transparenter Stand
In der Entwicklung wurden 30 bestandene automatisierte Chromium-Prüfungen und eine JavaScript-Syntaxprüfung gemeldet. Die dazugehörigen Testskripte sind in diesem Dokumentationsstand nicht im Repository archiviert. Das ist kein reproduzierbarer CI-Nachweis. Dieses Dokumentations-Update führt die damaligen Tests nicht erneut aus.

Die damalige Leistungs-Stichprobe meldete 120 Simulations-/Renderdurchläufe mit 20.596 belegten Zellen in rund 454 ms in einer Headless-Testumgebung. Keine garantierte Bildrate auf Nutzergeräten.

Nicht bestätigt: vollständige Windows-Browsermatrix, echtes iPhone/iPad, Safari-Gerätetest, alle Materialkombinationen. Ein GitHub-Pages-Deployment ist separat am öffentlichen Link zu prüfen.

## Manuelle Regression vor Spieländerungen
1. Start: korrekte Farben, sichtbare Welt, keine Konsolenfehler.
2. Fenster: 2489×1047, 1280×720, 800×600, 390×844; Canvas darf nicht über die Bühne hinausragen.
3. Eingabe: links platzieren, rechts löschen, halten, schnelle Linien, Rad, 1–9, Pause, Fokusverlust.
4. Sand über mehrere Chunkgrenzen fallen lassen; Stütze entfernen und Wiederaktivierung prüfen.
5. Sand in Wasser; Wasserbecken mit dünnen Wänden; keine unerwarteten Wanddurchtritte.
6. Feuer + Wasser, Lava + Wasser, Lava + Eis, Dampf-Ablauf, Rauch- und Feuer-Ablauf auch nach mehr als 255 Ticks.
7. Säure auf Stein/Holz und in Glas; Bombe und Schießpulverkette neben Wand.
8. Wärmeleitung durch Metall; Pflanzen an feuchter Erde.
9. Partikelzähler, Leeren und Reset; leerer Ausgangsrand enthält 996 belegte Zellen.
10. 10/100/300 % Geschwindigkeit und Pause vergleichen; über mehrere Minuten testen.

Pro Test Version, Commit, Browser/Version, Betriebssystem, Geräteklasse, Schritte, Soll/Ist und Ergebnis notieren. Zufallsabhängige Tests brauchen Wiederholungen bzw. künftig einen kontrollierten Zufallsstartwert.

## Noch aufzubauen
- Versionierte Browser-Testskripte, z. B. mit Playwright, ohne Abhängigkeiten in das Spiel selbst einzubauen.
- Automatische Syntax-/Smoke-Tests bei Pull Requests.
- Reproduzierbare Physiktests und Belastungsszenarien.
- Echter iOS-/Safari-Test einschließlich Touch, Radieren, Drehen und kleiner Displays.
- Prüfung des ausgelieferten Pages-Spiels statt nur lokaler Dateien.
