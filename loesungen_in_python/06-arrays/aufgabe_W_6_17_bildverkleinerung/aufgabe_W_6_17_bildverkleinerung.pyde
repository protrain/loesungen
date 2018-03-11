# Funktion zum Verkleinern eines quadratischen
# Arrays. Das zu verkleinernde Array wird an die
# Funktion übergeben. Als Ergebnis wird das
# verkleinerte Array zurückgegeben.
def shrink(input):
    # Nur gültige Größen (gerade Anzahl an Feldern
    # und quadratisch) akzeptieren
    if len(input) % 2 != 0 and len(input) != len(input[0]):
        return null

    # Ausgabe-Array (halb so groß wie die Eingabe)
    out = createArray(len(input) / 2, len(input) / 2)

    # Zähler, wie viele Schwarzwerte in dem 2x2-Element sind
    numBlack = 0

    # Für jedes Feld im Ausgabe-Array
    for i in range(0, len(out)):
        for j in range(0, len(out)):
          # Analyse: Gehe in Form von 2x2-Elementen das
          # Eingabe-Array durch und bestimme die Anzahl
          # an Schwarzwerten
            for k in range(0, 2):
                for l in range(0, 2):
                    # Wenn kein Weißwert vorliegt,
                    # dann Schwarzzähler erhöhen
                    if input[k + i * 2][l + j * 2] == False:
                        numBlack += 1

            # Wenn mindestens zweimal schwarz vorkommt
            # schwarz im Ausgabe-Array speichern
            if numBlack > 1:
                out[i][j] = False
            # sonst weiß
            else:
                out[i][j] = True

            # Zähler resetten für nächstes 2x2-Element
            numBlack = 0

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
input = [[False, True, False, False, True, False],
         [True, True, False, False, True, True],
         [True, False, True, True, False, True],
         [True, True, True, True, True, True],
         [False, True, False, False, True, False],
         [True, False, False, False, False, True]]

# displayArray(input)
displayArray(shrink(input))

