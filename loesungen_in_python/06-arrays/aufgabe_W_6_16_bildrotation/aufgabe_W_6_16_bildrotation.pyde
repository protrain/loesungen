# Funktion, die ein zweidimensionales rechteckiges
# boolean-Array um 90 Grad nach links dreht. An die
# Funktion wird das zu bearbeitende Array übergeben.
# Zum Schluss gibt die Funktion das gedrehte Array
# zurück.
def negativeRotation(bwImage):
    # Neues Array anlegen (Höhe und Breite vertauscht)
    rotatedImage = createArray(len(bwImage[0]), len(bwImage))

    # Gehe jedes Element durch
    # Zunächst in der Zeile
    for i in range(0, len(bwImage)):
        # dann in der Spalte
        for j in range(0, len(bwImage[i])):
            # Kopiere Quellinhalt der Zelle [i,j]
            # an die gedrehte Position
            rotatedImage[len(bwImage[i]) - 1 - j][i] = bwImage[i][j]

    return rotatedImage


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
input = [[False, True, True],
         [True, False, True],
         [True, True, False],
         [True, False, True]]

# displayArray(input)
displayArray(negativeRotation(input))

