size(800, 800)

# Funktion zum Spiegeln eines Arrays
# Erhält das ursprüngliche zweidimensionale Array
# und gibt das gespiegelte Array zurück.
def mirror(input):
    # Ausgabe-Array gespiegelt
    output = []

    # Gehe jede Zeile im Input-Array zeilenweise durch
    for y in input:
        # Temporäres Zeilen-Array
        row = []

        # Gehe jedes Element spaltenweise durch
        for x in y:
            # Schreibe Elemente umgekehrt in das Array
            row = [x] + row

        # Füge gespiegelte Reihe dem Ausgabe-Array hinzu
        output = output + [row]

    return output

# Stellt Array grafisch dar
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
            # True = Setze Farbe auf Schwarz
            if input[y][x]:
                fill(0)

            # Sonst setze Farbe auf weiß
            else:
                fill(255)

            # Male Kasten auf Bildschirm
            rect(x * xSize, y * ySize, xSize, ySize)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
inhalt = [[False, False, False, False],
          [False, True, False, False],
          [False, True, False, True]]

displayArray(mirror(inhalt))

