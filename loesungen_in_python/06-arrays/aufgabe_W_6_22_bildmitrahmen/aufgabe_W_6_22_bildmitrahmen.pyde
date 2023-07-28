# Funktion zum Hinzufügen einer schwarzen Umrandung an ein Array.
# An die Funktion wird das zweidimensionale Quell-Array sowie die
# Zielgröße inkl. Rahmen übergeben. Die Funktion gibt das neu berechnete
# Array zurück.
def add_frame(input_data, f_width):
    out = create_array(len(input_data) + 2 * f_width,
                       len(input_data[0]) + 2 * f_width)

    # Setze zunächst alle Array-Werte auf false.
    # Damit wird das Array komplett "eingeschwärzt".
    for x in range(0, len(out)):
        for y in range(0, len(out[0])):
            out[x][y] = False

    # Kopiere die Array-Werte vom Quell-Array rüber in das
    # größere Array, beginnend ab Rand
    for x in range(0, len(input_data)):
        for y in range(0, len(input_data[0])):
            out[x + f_width][y + f_width] = input_data[x][y]

    return out


# Funktion zur grafischen Darstellung eines
# zweidimensionalen Arrays, welches an die
# Funktion übergeben wird
def display_array(input_data):
    # Höhe und Breite des Arrays bestimmen
    i_width = len(input_data[0])
    i_height = len(input_data)

    # Größe pro Rechteck, abhängig vom Bildschirmfenster
    xSize = width / i_width
    ySize = height / i_height

    # Gehe jede Zeile und Spalte durch
    for y in range(0, i_height):
        for x in range(0, i_width):
            # Bestimme Farbe
            # True = Setze Farbe auf Weiß
            if input_data[y][x]:
                fill(255)
            # Sonst setze Farbe auf Grau
            else:
                fill(125)

            # Male Kasten auf Bildschirm
            rect(x * xSize, y * ySize, xSize, ySize)


# Generiert leeres 2D-Array in den Dimensionen sizeX x sizeY
def create_array(sizeX, sizeY):
    print(sizeX, sizeY)
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

# display_array(input)
display_array(add_frame(input, 1))
