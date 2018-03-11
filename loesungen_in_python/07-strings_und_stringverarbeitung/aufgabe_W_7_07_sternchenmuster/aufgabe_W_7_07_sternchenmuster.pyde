# Funktion zum Zeichnen von Sternchenmuster in der Kommandozeile
# An die Funktion wird die Anzahl an Zeilen übergeben.
def drawStars(rows):
    # Zeilen von oben bis Mitte
    for numStars in range(1, rows):
        printStars(numStars)

    # In der Mitte werden (fast) doppelt so viele
    # ausgegeben
    printStars(rows * 2 - 1)

    # Für die nachfolgenden Zeilen ...
    for i in range(1, rows):
        # ... immer ein Sternchen weniger ausgeben
        numStars = rows - i
        # Aufruf mit zwei Parametern, damit die Leerzeichen
        # berücksichtigt werden
        printStars(numStars, rows)

# Zeichnet angegebene Nummer an Sternen in eine Reihe
# Funktion zum Zeichnen der Anzahl angegebener Sternchen
# mit Berücksichtigung von Leerzeichen.
# Die Funktion erhält die Anzahl der auszugebenden Sterne
# sowie die Anzahl von Leerzeichen.
def printStars(numStars, numSpace=0):
    row = ""

    # Füge ggf. Leerzeichen hinzu
    for i in range(0, numSpace):
        row += " "

    for i in range(0, numStars):
        row += "*"

    print row


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
drawStars(4)

