# Die Funktion zur Berechnung endlicher Produkte erhält den
# Startwert s und den Endwert e als Integer-Werte und liefert
# als Ergebnis einen Integer-Wert zurück.
def product(s, e):
    if e < 0 or s < 0:          # ist einer der beiden Werte < 0,
        return 0                # wird 0 zurückgegeben

    elif e == 0 or s == 0:      # ist einer der beiden Werte = 0,
        return 0                # wird 0 zurückgegeben

    # Vertausche Werte, damit die for-Schleife vom kleinsten
    # zum größten Wert laufen kann
    elif e < s:
        # Vertausche Werte, damit die for-Schleife
        # vom kleinsten zum größten Wert laufen kann
        eTemp = e               # Temporäres Speichern von e
        e = s                   # Tauschen..
        s = eTemp

    # Deklaration und Initialisierung der Variablen für das Ergebnis
    # Der Startwert muss 1 sein (wegen Multiplikation)
    result = 1
    for i in range(s, e + 1):  # Zähle vom Start- bis Endwert
        result *= i            # und multipliziere die Zahl mit dem
        # Ergebnis

    # Das Ergebnis zurückliefern
    return result

# Die Funktion zur Berechnung der Fakultät
# verwendet die Funktion zur Berechnung endlicher Produkte.
# An die Funktion wird der Wert n übergeben, für die die
# Fakultät berechnet werden soll.
def factorial(n):
    return product(1, n)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print factorial(6)

