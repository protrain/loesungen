# Funktion zum Vergrößern eines quadratisches Array um den Faktor f
# Eingabe ist ein zweidimensionales Array mit boolean-Werten sowie
# der Faktor, um den das Array vergrößert werden soll
def magnify(in_arr, f):
    # Die aktuelle Größe entspricht der Anzahl an Array-Elementen
    # einer Dimension
    in_arr_size = len(in_arr)

    # Berechnen der Ergebnisgröße des Arrays
    output_size = f * in_arr_size

    # Generiere leeren Output-Array in der neuen Größe
    output = create_array(output_size)

    # Gehe jedes Element in Input durch und schreibe es in die skalierten
    # Felder im Output
    for y in range(0, in_arr_size):       # Iteration durch Zeilen
        for x in range(0, in_arr_size):   # Iteration durch Spalten
            for j in range(0, f):       # Iteration für den Zeilenfaktor
                for i in range(
                        0, f):   # Iteration für den Spaltenfaktor
                    # Schreiben des Werts
                    output[x * f + j][y * f + i] = in_arr[x][y]

    return output


# Funktion, die ein leeres 2D-Array in den Dimensionen
# array_size x array_size erzeugt und zurückgibt
def create_array(array_size):
    output = []
    for y in range(0, array_size):
        row = []
        for x in range(0, array_size):
            row = row + [False]
        output = output + [row]
    return output


# Funktion, die das Array grafisch im Ausgabefenster darstellt
# Als Eingabe erfolgt das Array.
def draw_array(in_arr):
    # Array-Größe. Da das Array quadratisch sein soll, reicht die Höhe
    # des Arrays aus
    in_arr_size = len(in_arr)

    # Höhe und Breite jedes Rechtecks (definiert durch Fenstergröße)
    rect_width = width / in_arr_size
    rect_height = height / in_arr_size

    for y in range(0, in_arr_size):
        for x in range(0, in_arr_size):
            # Setze Farbe nach Array-Inhalt
            # Um einzelne Elemente sichtbar zu machen, ist Linienfarbe
            # stets das Gegenteil der Füllfarbe
            if in_arr[y][x] is False:
                stroke(0)
                fill(255)
            else:
                stroke(255)
                fill(0)

            # Zeichne Rechteck
            # start_x,start_y: obere linke Ecke des Rechtecks
            # start_x+rect_width, start_y+rect_height: untere linke Ecke
            # des Rechtecks
            start_x = x * rect_width
            start_y = y * rect_height
            rect(start_x, start_y, start_x + rect_width, start_y + rect_height)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

size(200, 200)
background(255)
eingabe = [[True, False], [False, False]]
draw_array(magnify(eingabe, 1))
