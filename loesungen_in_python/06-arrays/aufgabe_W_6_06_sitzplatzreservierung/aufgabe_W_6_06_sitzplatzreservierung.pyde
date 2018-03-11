# Globale Symbolkonstanten
FREE = '_'     # Freier Sitz
TAKEN = '#'    # Belegter Sitz

# Globale Arena
arena = []
minSeats = 3   # Anzahl der Sitze in der letzten Reihe

# Funktion zum Generieren einer neuen Arena. Als
# Eingabewert dient die Anzahl an Zeilen. Die Arena
# wird in einem Array von Chars zurückgegeben
def createArena(numRows):
    # zu befüllendes Gesamt-Array
    arena = []

    # Gehe numerisch jede zu erzeugende Reihe durch
    for i in range(0, numRows):
        # Anzahl der Sitze in aktueller Reihe
        numSeats = numRows - i + (minSeats - 1)

        # Einzelne Reihe
        row = []
        # Gehe numerisch jeden zu erzeugenden Sitz durch
        for x in range(0, numSeats):
            # Füge Array-Element hinzu
            row.append(FREE)
        # Füge Reihe in Arena hinzu
        arena.append(row)

    return arena

# Funktion, die die Arena grafisch darstellt
# Erhält ein zweidimensionales Char-Array
def visualizeArena(arena):
    # Gehe jede Reihe durch
    for y in arena:
        # leeres Stringobjekt erzeugen, dient zur Ausgabe
        # in der Konsole
        row = ""

        # Gehe jeden Sitz durch
        for x in y:
            # Füge Character in Reihe dem Reihenstring hinzu
            row = row + x

        # gebe String mit Sitzreihe aus und mache Zeilenumbruch
        # (für die nächste Reihe)
        print row

# Funktion zum Buchen eines einzelnen Sitzplatzes
# Als Eingabe wird die Reihe und der Platz angegeben
def bookSeat(row, seat):
    # Das globale Arena-Array holen
    global arena

    # Zur Änderung der Reihe wird temporäre Reihe angelegt
    rowTemp = arena[row]

    # Setze Sitzplaz auf Belegt
    rowTemp[seat] = TAKEN

    # Ersetze Reihe mit geänderter Reihe
    arena[row] = rowTemp

# Funktion zum zufälligen Buchen von Sitzplätzen
# in der gesamten Arena
def fillSeats():
    # Das globale Arena-Array holen
    global arena

    # Anzahl der Reihen
    numRows = len(arena)

    # Gehe jede Reihe durch (von Reihe 0 bis Gesamtzahl)
    for y in range(0, numRows):
        # Stuhlanzahl in einer Reihe
        numSeats = numRows - y + (minSeats - 1)
        # Gehe jeden Sitz durch
        for x in range(0, numSeats):
            # Zufallszahl zwischen 0 und 1 (Random ist Zahl
            # von 0 bis 1,9999999...)
            randomNumber = int(random(0, 2))
            # Wenn Zufallszahl eine 1 ist, soll Sitz gebucht
            # werden
            if randomNumber == 1:
                bookSeat(y, x)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

arena = createArena(10)
fillSeats()
visualizeArena(arena)

