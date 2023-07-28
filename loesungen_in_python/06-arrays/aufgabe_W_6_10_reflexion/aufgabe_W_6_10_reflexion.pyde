size(800, 800)

# Funktion zur Berechnung der angegebenen Reflexion
# An die Funktion wird das zu bearbeitende zwei-
# dimensionale Array übergeben. Das gespiegelte
# Ergebnis wird zurückgegeben.
def reflection(input_data):
    # Höhe des Eingabe-Arrays
    i_height = len(input_data)

    # Kopie anlegen (ein Drittel größer)
    output = input_data

    # Gehe rückwärts das letzte Drittel des Arrays durch
    for i in range(0, i_height / 3):
        # Füge Zeile dem Array hinzu
        output = output + [input_data[i_height - 1 - i]]
    return output

# Funktion zur grafischen Darstellung eines zweidimensionalen
# Arrays
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


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
input = [[False, False, False, True, True],
         [False, False, False, True, True],
         [False, False, False, True, True],
         [True, True, False, False, False],
         [True, False, False, False, True],
         [False, False, False, True, True]]

# display_array(input)
display_array(reflection(input))
