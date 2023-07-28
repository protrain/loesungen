# Funktion zum Umdrehen und Invertieren eines zwei-
# dimensionalen Arrays. An die Funktion wird das zu
# bearbeitende Array übergeben. Die Funktion selbst
# gibt das fertig bearbeitete Array zurück.
def flip_and_invert(input_data):
    # Ausgabe-Array mit gleicher Größe
    out = create_array(len(input_data), len(input_data[0]))

    # Gehe jede Zeile und Spalte durch
    for i in range(0, len(input_data)):
        for j in range(0, len(input_data[0])):
            # Oben wird unten hingeschrieben und umgekehrt
            # Inhalt wird invertiert
            if input_data[i][j]:
                content = False
            else:
                content = True
            out[len(input_data) - 1 - i][j] = content
    return out


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


# Generiert leeres 2D-Array in den Dimensionen size_x x size_y
def create_array(size_x, size_y):
    print(size_x, size_y)
    output = []
    for x in range(0, size_x):
        row = []
        for y in range(0, size_y):
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

# display_array(input_data)
display_array(flip_and_invert(input))
