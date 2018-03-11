# Funktion zum Erzeugen eines Schlagschattens in einem
# zweidimensionalen Array, welches an die Funktion
# übergeben wird. Als Ergebnis liefert die Funktion
# das Array mit dem erzeugten Schatten zurück
def addShadow(input):
    # Vergrößere Ausgabebild um jeweils einen Pixel
    # nach rechts und unten
    t = createArray(len(input) + 1, len(input[0]) + 1)

    # Kopiere alle Elemente des Eingabe-Arrays.
    # Durchlaufe das Array für jede Zeile
    for i in range(0, len(input)):
        # und jede Spalte
        for j in range(0, len(input[i])):
            # kopiere Inhalt
            t[i][j] = input[i][j]

    # Letzte Zeile: unten links auf Weiß
    t[len(t) - 1][0] = True

    # Setze den Rest der letzten Zeile auf Schwarz
    for i in range(1, len(t[len(t) - 1])):
        t[len(t) - 1][i] = False

    # Letzte Spalte: oben rechts auf Weiß
    t[0][len(t[0]) - 1] = True

    # Setze den Rest der letzten Spalte auf Schwarz
    for i in range(1, len(t)):
        t[i][len(t[i]) - 1] = False

    return t


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
displayArray(addShadow(input))

