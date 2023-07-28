# Funktion, die ein zweidimensionales rechteckiges
# boolean-Array um 90 Grad nach links dreht. An die
# Funktion wird das zu bearbeitende Array übergeben.
# Zum Schluss gibt die Funktion das gedrehte Array
# zurück.
def negative_rotation(bw_image):
    # Neues Array anlegen (Höhe und Breite vertauscht)
    rotated_image = create_array(len(bw_image[0]), len(bw_image))

    # Gehe jedes Element durch
    # Zunächst in der Zeile
    for i in range(0, len(bw_image)):
        # dann in der Spalte
        for j in range(0, len(bw_image[i])):
            # Kopiere Quellinhalt der Zelle [i,j]
            # an die gedrehte Position
            rotated_image[len(bw_image[i]) - 1 - j][i] = bw_image[i][j]

    return rotated_image


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
display_array(negative_rotation(input))
