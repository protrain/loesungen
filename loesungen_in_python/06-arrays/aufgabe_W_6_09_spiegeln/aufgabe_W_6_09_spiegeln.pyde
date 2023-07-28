size(800, 800)

# Funktion zum Spiegeln eines Arrays
# Erhält das ursprüngliche zweidimensionale Array
# und gibt das gespiegelte Array zurück.
def mirror(input_data):
    # Ausgabe-Array gespiegelt
    output = []

    # Gehe jede Zeile im Input-Array zeilenweise durch
    for y in input_data:
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
            # True = Setze Farbe auf Schwarz
            if input_data[y][x]:
                fill(0)

            # Sonst setze Farbe auf weiß
            else:
                fill(255)

            # Male Kasten auf Bildschirm
            rect(x * x_size, y * y_size, x_size, y_size)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
inhalt = [[False, False, False, False],
          [False, True, False, False],
          [False, True, False, True]]

display_array(mirror(inhalt))
