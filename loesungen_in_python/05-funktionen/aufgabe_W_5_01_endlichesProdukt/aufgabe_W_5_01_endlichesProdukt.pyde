# Die Funktion zur Berechnung endlicher Produkte erhält den
# Startwert s und den Endwert e als Integer-Werte und liefert
# als Ergebnis einen Integer-Wert zurück.
def product(s, e):
    if e < 0 or s < 0:          # ist einer der beiden Werte kleiner 0,
        return                  # wird 0 zurückgegeben

    elif e == 0 or s == 0:      # ist einer der beiden Werte gleich 0,
        return 0                # wird 0 zurückgegeben

    elif e < s:
        # Vertausche Werte, damit die for-Schleife
        # vom kleinsten zum größten Wert laufen kann
        eTemp = e
        e = s
        s = eTemp

    # Deklaration und Initialisierung der Variablen für das Ergebnis
    # Der Startwert muss 1 sein (wegen Multiplikation)
    result = 1
    for i in range(s, e + 1):  # Zähle vom Start- bis Endwert
        result *= i            # und multipliziere die Zahl mit dem
        # Ergebnis

    # Das Ergebnis zurückliefern
    return result


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    result = product(4, 3)
    print "Prod(4, 3): " + str(result)

