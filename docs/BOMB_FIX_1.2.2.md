# Bomben-Testfassung 1.2.2-rc.1

Direkt auf main ausschließlich die Vorschau test/index.html aktualisieren, zusammen mit Tests und Hinweisen. Die offizielle index.html / Version 1.2.1 bleibt unverändert. Keine neuen Korrekturbranches und keine weitere Aufteilung in Test- und Spiel-Uploads. fix/bomb-1.2.2 wird nicht weiter benutzt und in diesem Commit nicht gelöscht.

Bombe statisch wie Stein. Feuer/Lava zünden ohne Zufallsverzögerung, auch diagonal. Zusammenhängende Bombenzellen explodieren gemeinsam in einem Simulationsschritt; Bomben innerhalb des Explosionsradius werden sofort einbezogen, entfernte außerhalb bleiben stehen. Jede Zelle wird einmal verbraucht, überlappende Kreisflächen vereinigt. Keine zeitversetzten Bombenreste. Frisch nachgemalte Bomben können erneut zünden. Feuer/Rauch dürfen normal aufsteigen. Schießpulver bleibt Pulver mit Radius 5 und bisheriger Warteschlange; Wand bleibt unzerstörbar. Oberfläche, Eingabe und Rendering bleiben bis auf Versionsanzeige unverändert. Druck bleibt vereinfacht.

Prüfung vor Upload: Node.js-Syntaxprüfung sowie 34 bestandene Chromium-Checks mit tests/test_bombs.py. Darunter 1600 Bombenzellen in einem Tick, feste Position, Feuer-/Lava-Richtungen, entfernte Bombe, Wasser/Wand, Pulver, Zähler, Rand, Wiederholung, Maus/Touch und Layout. Deterministischer Materialmix ohne Bomben erzeugt nach 60 Schritten identische Zell-, Lebensdauer- und Wärmedaten wie die offizielle 1.2.1. Kein echter iPhone-/Safari-Test und kein CI- oder erfolgreicher Live-Deployment-Nachweis.

Zum Wiederholen: python -m pip install playwright; python -m playwright install chromium; python tests/test_bombs.py. Der bisherige Einstieg tests/test_preview.py startet jetzt ebenfalls diese aktuelle Vorschau-Prüfung. tests/test_v120.py bleibt unverändert für die offizielle 1.2.1.

Testlink nach erfolgreichem Deployment: https://kolle1979.github.io/powder-lab/test/ . Erst nach Nutzertest und ausdrücklicher Freigabe offiziell übernehmen. Hauptlink bis dahin unverändert. Der Nutzer wünscht keine zusätzlichen Branches ohne vorherige Absprache.
