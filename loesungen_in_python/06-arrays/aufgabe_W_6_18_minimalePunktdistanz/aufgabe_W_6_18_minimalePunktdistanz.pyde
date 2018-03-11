# Funktion zur Ermittlung der minimalen Distanz
# zwischen zwei Punkten. An die Funktion wird ein
# zweidimensionales Array mit Koordinaten übergeben.
# Als Ergebnis liefert die Funktion ein eindimensionales
# Array mit der Angabe der Indizes der kleinsten Distanz.
def minDistance(c):
    # Ergebnis-Array für zwei Elemente initialisieren
    result = [0, 0]

    # Minimale Distanz soll hier am Ende stehen.
    minD = sqrt(pow(c[0][0] - c[1][0], 2) + pow(c[0][1] - c[1][1], 2))

    # Gehe jede Spalte durch (Referenzpunkt)
    for i in range(0, len(c)):
        # Gehe jede Spalte durch ab dem Referenzpunkt (Vergleichspunkt)
        for j in range(i + 1, len(c)):
            # Berechne Distanz dieser Spalte
            d = sqrt(pow(c[i][0] - c[j][0], 2) +
                     pow(c[i][1] - c[j][1], 2))

            # Wenn kleiner als aktuell minimale Distanz, dann übernehmen
            if d < minD:
                # Speichere Distanz
                minD = d

                # Speichere Referenzpunkt
                result[0] = i

                # Speichere Vergleichspunkt
                result[1] = j

    return result


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
c = [[3, 7],
     [30, 80],
     [80, 320],
     [15, 276],
     [84, 298],
     [19, 29],
     [200, 200],
     [191, 919]]

print minDistance(c)

