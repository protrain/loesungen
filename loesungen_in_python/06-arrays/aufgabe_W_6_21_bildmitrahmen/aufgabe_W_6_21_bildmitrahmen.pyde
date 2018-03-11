# Funktion zum Hinzufügen einer schwarzen Umrandung an ein Array.
# An die Funktion wird das zweidimensionale Quell-Array sowie die
# Zielgröße inkl. Rahmen übergeben. Die Funktion gibt das neu berechnete
# Array zurück.
def addFrame(input, fWidth):
    out = createArray(len(input) + 2 * fWidth,
                      len(input[0]) + 2 * fWidth)

    # Setze zunächst alle Array-Werte auf false.
    # Damit wird das Array komplett "eingeschwärzt".
    for x in range(0, len(out)):
        for y in range(0, len(out[0])):
            out[x][y] = False

    # Kopiere die Array-Werte vom Quell-Array rüber in das
    # größere Array, beginnend ab Rand
    for x in range(0, len(input)):
        for y in range(0, len(input[0])):
            out[x + fWidth][y + fWidth] = input[x][y]

    return out


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
    print sizeX, sizeY
    output = []
    for x in range(0, sizeX):
        row = []
        for y in range(0, sizeY):
            row = row + [False]
        output = output + [row]
    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(800, 800)
input = [[True, False, True],
         [False, False, True],
         [True, False, False],
         [False, False, True]]

# displayArray(input)
displayArray(addFrame(input, 1))

