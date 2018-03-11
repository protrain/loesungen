# Funktion zum Heraustrennen eines Teilbereichs aus
# einem Array. An die Funktion werden ein zweidimensionales
# Array sowie Ausschnitthöhe und -weite übergeben.
def extractCenter(input, w, h):
    # Startreihe im Array
    # Gehe von Mitte h/2-Schritte zurück
    startRow = (len(input) - h) / 2

    # Startspalte im Array
    # Gehe von Mitte w/2-Schritte zurück
    startColumn = (len(input) - w) / 2

    # Generiere Ausgabe-Array
    output = createArray(w, h)

    # Gehe jede Spalte im Ziel-Array durch
    for y in range(0, h):
        # pro Zeile
        for x in range(0, w):
            # pro Spalte
            # kopiere Elemente aus Quellbereich
            output[y][x] = input[startRow + y][startColumn + x]

    # Gebe Bildausschnitt zurück
    return output

# Funktion zur grafischen Darstellung eines
# zweidimensionalen Arrays, welches an die
# Funktion übergeben wird
def displayArray(input):
    # Höhe und Breite des Arrays bestimmen
    iWidth = len(input[0])
    iHeight = len(input)

    # Größe pro Rechteck, abhängig vom Bildschirmfenster
    xSize = width / iWidth
    ySize = height / iHeight

    # Gehe jede Zeile und Spalte durch
    for y in range(0, iHeight):
        for x in range(0, iWidth):
            # Bestimme Farbe
            # True = Setze Farbe auf Weiß
            if input[y][x]:
                fill(255)
            # Sonst setze Farbe auf Grau
            else:
                fill(125)

            # Male Kasten auf Bildschirm
            rect(x * xSize, y * ySize, xSize, ySize)

# Generiert leeres 2D-Array in den Dimensionen sizeX x sizeY
def createArray(sizeX, sizeY):
    output = []
    for y in range(0, sizeY):
        row = []
        for x in range(0, sizeX):
            row = row + [False]
        output = output + [row]
    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(800, 800)
input = [[False, False, False, True, True],
         [False, False, False, True, True],
         [False, False, False, True, True],
         [True, True, False, False, False],
         [True, False, False, False, True],
         [False, False, False, True, True]]

# displayArray(input)
displayArray(extractCenter(input, 3, 2))

