# Funktion zum Verkleinern eines quadratischen
# Arrays. Das zu verkleinernde Array wird an die
# Funktion übergeben. Als Ergebnis wird das
# verkleinerte Array zurückgegeben.
def shrink(input_data):
    # Nur gültige Größen (gerade Anzahl an Feldern
    # und quadratisch) akzeptieren
    if len(input_data) % 2 != 0 and len(input_data) != len(input_data[0]):
        return None

    # Ausgabe-Array (halb so groß wie die Eingabe)
    out = create_array(len(input_data) / 2, len(input_data) / 2)

    # Zähler, wie viele Schwarzwerte in dem 2x2-Element sind
    num_black = 0

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
                    if input_data[k + i * 2][l + j * 2] is False:
                        num_black += 1

            # Wenn mindestens zweimal schwarz vorkommt
            # schwarz im Ausgabe-Array speichern
            if num_black > 1:
                out[i][j] = False
            # sonst weiß
            else:
                out[i][j] = True

            # Zähler resetten für nächstes 2x2-Element
            num_black = 0

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
input = [[False, True, False, False, True, False],
         [True, True, False, False, True, True],
         [True, False, True, True, False, True],
         [True, True, True, True, True, True],
         [False, True, False, False, True, False],
         [True, False, False, False, False, True]]

# display_array(input)
display_array(shrink(input))
