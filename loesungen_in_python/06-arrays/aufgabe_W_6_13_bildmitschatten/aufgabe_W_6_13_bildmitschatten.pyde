# Funktion zum Erzeugen eines Schlagschattens in einem
# zweidimensionalen Array, welches an die Funktion
# übergeben wird. Als Ergebnis liefert die Funktion
# das Array mit dem erzeugten Schatten zurück
def add_shadow(input_data):
    # Vergrößere Ausgabebild um jeweils einen Pixel
    # nach rechts und unten
    t = create_array(len(input_data) + 1, len(input_data[0]) + 1)

    # Kopiere alle Elemente des Eingabe-Arrays.
    # Durchlaufe das Array für jede Zeile
    for i in range(0, len(input_data)):
        # und jede Spalte
        for j in range(0, len(input_data[i])):
            # kopiere Inhalt
            t[i][j] = input_data[i][j]

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
display_array(add_shadow(input))
