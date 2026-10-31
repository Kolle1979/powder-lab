# Elemente und Experimente – v1.2.2

| Material | Implementiertes Verhalten |
|---|---|
| Sand | Fällt, bildet Haufen, sinkt in weniger dichten Flüssigkeiten. |
| Wasser | Fließt, löscht Feuer/Glut, reagiert mit Lava zu Stein und Dampf, verdampft bei hoher Wärme. |
| Stein | Statisch, leitet Wärme schwach, säurelöslich und durch Explosionen zerstörbar. |
| Erde | Fällt; neben Wasser kann oberhalb eine Pflanze entstehen. |
| Holz | Statisch, brennbar und säurelöslich. |
| Feuer | Steigt auf, entzündet Brennbares und wird nach Ablauf Rauch; Wasser löscht es. |
| Rauch | Steigt auf und verschwindet nach begrenzter Lebensdauer. |
| Dampf | Steigt auf und wird nach Ablauf wieder Wasser. |
| Lava | Fließt langsam, erhitzt Nachbarn, zündet Brennbares, schmilzt Eis; Wasser macht Stein daraus. |
| Öl | Fließt, ist leichter als Wasser und brennt. |
| Schießpulver | Fällt und explodiert bei Zündung mit Radius 5. |
| Säure | Löst Stein, Erde, Holz, Pflanzen, Metall, Sand und Eis probabilistisch; kann dabei selbst zu Rauch werden. Glas und Wand sind säurefest. |
| Glas | Statisch, säurefest, durch Explosionen zerstörbar; optisch durchscheinend eingefärbt. |
| Pflanze | Statisch, wächst langsam bei Anschluss an Erde/Pflanzen nach oben in Luft/Wasser; brennbar. |
| Eis | Statisch, schmilzt durch Wärme oder heißen Kontakt zu Wasser. |
| Metall | Statisch, leitet Wärme und wird bei hoher Wärme zu Lava. |
| Bombe | Statisch wie Stein. Feuer/Lava zünden sofort; verbundene Bombenzellen und weitere Bomben im Explosionsradius explodieren gemeinsam in einem Simulationsschritt. Kreisradius 13 je Bombenzelle, überlappende Flächen vereinigt. Keine verzögerten Bombenreste; entfernte Bomben außerhalb bleiben stehen. |
| Wand | Statisch, säure- und explosionsfest; per Radierer weiterhin löschbar. |

Luft ist der leere Zustand. Glut ist eine zusätzliche interne Material-ID und kein auswählbares Element. Zufall, Nachbarschaft und Scanreihenfolge beeinflussen den Ablauf; der direkte Bombenkontakt mit Feuer/Lava ist nicht zufallsabhängig.

## Fünf Experimente
1. Glasbecken mit Wasser füllen, Öl hinzufügen und die obere Schicht entzünden.
2. Vulkan aus Stein/Wand bauen, Lava einfüllen und oben Wasser hinzugeben.
3. Erde neben Wasser legen, auf Pflanzen warten und daneben eine Holzwand anzünden.
4. Bomben und Schießpulver neben Glas und Wand zünden; Schäden vergleichen.
5. Metall an Lava legen und Eis am anderen Ende platzieren; Erwärmung beobachten.
