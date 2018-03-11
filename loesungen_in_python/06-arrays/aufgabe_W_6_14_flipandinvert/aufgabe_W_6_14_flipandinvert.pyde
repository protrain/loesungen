# Funktion zum Umdrehen und Invertieren eines zwei-
# dimensionalen Arrays. An die Funktion wird das zu
# bearbeitende Array übergeben. Die Funktion selbst
# gibt das fertig bearbeitete Array zurück.
def flipAndInvert(input):
    # Ausgabe-Array mit gleicher Größe
    out = createArray(len(input), len(input[0]))

    # Gehe jede Zeile und Spalte durch
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            # Oben wird unten hingeschrieben und umgekehrt
            # Inhalt wird invertiert
            if input[i][j]:
                content = False
            else:
                content = True
            out[len(input) - 1 - i][j] = content
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
input = [[False, True, True],
         [True, False, True],
         [True, True, False],
         [True, False, True]]

# displayArray(input)
displayArray(flipAndInvert(input))

