# Feuer-Testfassung 1.2.3-rc.1

Nur test/index.html aktualisieren. Offizielle 1.2.2 und deren Startdatei bleiben unverändert. Keine neuen Branches und keine offizielle Freigabe durch diesen Vorschau-Upload.

Gemaltes Feuer wird zum kurzen Funken: sechs Simulationsschritte, ungefähr 0,1 Sekunden bei 100 Prozent Tempo. Nach Loslassen verschwindet es in freier Luft ohne Rest-Rauch. Gedrückthalten erzeugt weiterhin neue Funken. Die Pause hält auch die Lebensdauer an.

Bei direktem Kontakt mit Holz oder Öl entzündet der gemalte Funke das Material zuverlässig. Die Kontaktprüfung gilt auf beiden Seiten, damit fließendes Öl nicht vor der Prüfung wegfließt. Danach gelten die bisherigen längeren Brennzeiten und die bisherige Ausbreitung für normales Feuer. Bereits brennende Flammen werden durch Nachmalen nicht künstlich verkürzt. Explosionsfeuer, Bomben, sonstige Materialien, Oberfläche und Rendering bleiben wie zuvor.

Technik: Markierung im bestehenden Uint16-Lebensdauerwert, keine neuen Partikelobjekte oder externen Laufzeitabhängigkeiten. PAINT_FIRE_FLAG=512 und PAINT_FIRE_TICKS=6. Normal erzeugtes Feuer behält die bisherige Lebensdauer.

Vor Upload: Node.js-Syntaxprüfung und 15 bestandene Chromium-Prüfungen mit tests/test_fire.py, inklusive direkter Funken, Maus/Touch, Holz/Öl, Pause, nicht verkürztem normalen Feuer, Bombenzündung, fehlenden Laufzeitfehlern, keiner beobachteten HTTP/HTTPS-Verbindung und unveränderter offizieller Datei. Statische Durchsicht fand keine neuen externen Skripte, Netzwerkaufrufe, eval/new Function oder document.write. Vorhandene innerHTML-Nutzung für fest definierte Elementknöpfe bleibt unverändert; keine neuen fremden Eingaben. Kein vollständiger Sicherheitsaudit, kein echter iOS-Test, kein CI- oder Live-Deployment-Nachweis.

Nur für Entwicklung: python -m pip install playwright; python -m playwright install chromium; python tests/test_fire.py. Die vorhandenen Bombentests bleiben erhalten. Testlink nach erfolgreicher Bereitstellung: https://kolle1979.github.io/powder-lab/test/ . Erst nach Rückmeldung und ausdrücklicher Elternfreigabe die offizielle Spielversion ändern. Es werden keine persönlichen Daten in Spiel oder Testdaten übernommen.
