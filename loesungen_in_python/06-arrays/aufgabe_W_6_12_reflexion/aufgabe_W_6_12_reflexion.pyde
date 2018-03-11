size(800, 800)

# Funktion zur Berechnung der angegebenen Reflexion
# An die Funktion wird das zu bearbeitende zwei-
# dimensionale Array übergeben. Das gespiegelte
# Ergebnis wird zurückgegeben.
def reflection(input):
    # Höhe des Eingabe-Arrays
    iHeight = len(input)

    # Kopie anlegen (ein Drittel größer)
    output = input

    # Gehe rückwärts das letzte Drittel des Arrays durch
    for i in range(0, iHeight / 3):
        # Füge Zeile dem Array hinzu
        output = output + [input[iHeight - 1 - i]]
    return output

# Funktion zur grafischen Darstellung eines zweidimensionalen
# Arrays
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


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
input = [[False, False, False, True, True],
         [False, False, False, True, True],
         [False, False, False, True, True],
         [True, True, False, False, False],
         [True, False, False, False, True],
         [False, False, False, True, True]]

# displayArray(input)
displayArray(reflection(input))

