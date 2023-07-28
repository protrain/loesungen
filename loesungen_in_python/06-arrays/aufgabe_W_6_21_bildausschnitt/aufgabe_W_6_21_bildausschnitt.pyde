# Funktion zum Heraustrennen eines Teilbereichs aus
# einem Array. An die Funktion werden ein zweidimensionales
# Array sowie Ausschnitthöhe und -weite übergeben.
def extract_center(input_data, w, h):
    # Startreihe im Array
    # Gehe von Mitte h/2-Schritte zurück
    start_row = (len(input_data) - h) / 2

    # Startspalte im Array
    # Gehe von Mitte w/2-Schritte zurück
    start_column = (len(input_data) - w) / 2

    # Generiere Ausgabe-Array
    output = create_array(w, h)

    # Gehe jede Spalte im Ziel-Array durch
    for y in range(0, h):
        # pro Zeile
        for x in range(0, w):
            # pro Spalte
            # kopiere Elemente aus Quellbereich
            output[y][x] = input_data[start_row + y][start_column + x]

    # Gebe Bildausschnitt zurück
    return output


# Funktion zur grafischen Darstellung eines
# zweidimensionalen Arrays, welches an die
# Funktion übergeben wird
def display_array(input_data):
    # Höhe und Breite des Arrays bestimmen
    i_width = len(input_data[0])
    i_height = len(input_data)

    # Größe pro Rechteck, abhängig vom Bildschirmfenster
    x_size = width / i_width
    y_size = height / i_height

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
            rect(x * x_size, y * y_size, x_size, y_size)


# Generiert leeres 2D-Array in den Dimensionen sizeX x sizeY
def create_array(sizeX, sizeY):
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

# display_array(input)
display_array(extract_center(input, 3, 2))
