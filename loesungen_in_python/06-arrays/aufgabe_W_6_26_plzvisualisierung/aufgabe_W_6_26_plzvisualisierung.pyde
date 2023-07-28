# Definiere globale Variablen
# Anzahl der gespeicherten PLZ-Orte im Array
place_count = 0

# Maximale Werte der x-und y-Koordinaten
min_X = 0
max_X = 0
min_Y = 0
max_Y = 0

# Zeichenbereich-Abmessungen der Karte
map_x_1 = 0
map_y_1 = 0
map_x_2 = 0
map_y_2 = 0

# Array, in dem wir die x- und y-Koordinaten
# speichern werden
x = []
y = []


def setup():
    # Lade globale Variablen, damit wir die Werte ändern können
    global place_count, min_X, max_X, min_Y, max_Y, map_x_1, map_y_1, map_x_2
    global map_y_2, x, y

    # Setze Fenstergröße
    size(380, 450)

    # Setze Zeichenbereich für die Karte
    # Zeichenbereich-Abmessungen der Karte
    # Obere linke Ecke
    map_x_1 = 30
    map_y_1 = 20
    # Untere rechte Ecke
    map_x_2 = width - map_x_1
    map_y_2 = height - map_y_1

    # Lese die Koordinaten ein
    read_data()


def draw():
    # Lade globale Variablen, damit wir die Werte ändern können
    global place_count, min_X, max_X, min_Y, max_Y, map_x_1, map_y_1, map_x_2
    global map_y_2, x, y

    # Setze schwarzen Hintergrund
    background(0)

    # Setze weiße Kreisfarbe
    stroke(255)
    fill(255)

    for i in range(0, len(x)):
        # Setze x- und y-Koordinaten in Abhängigkeit vom
        # Zeichenbereich
        x_draw = map(x[i], min_X, max_X, map_x_1, map_x_2)

        # Koordinatensystem bei Y ist umgekehrt, daher sind
        # Y2 und Y1 vertauscht
        y_draw = map(y[i], min_Y, max_Y, map_y_2, map_y_1)

        # Male Kreis
        ellipse(x_draw, y_draw, 1, 1)


# Funktion, die die Postleitzahldaten und 2D-Koordinaten
# aus einer CSV-Datei einliest und in einem Array speichert
def read_data():
    # Lade globale Variablen, damit wir die Werte ändern können
    global place_count, min_X, max_X, min_Y, max_Y
    global map_y_2, x, y

    # Lese die CSV-Datei ein
    lines = loadStrings("zip_de_prep.csv")

    # Setze die Minimal- und Maximalwerte der Koordinaten in
    # der CSV-Datei
    min_X = -0.056436524
    max_X = 0.044636916
    min_Y = 0.7982389
    max_Y = 0.9287888

    # Jetzt lesen wir die x- und y-Koordinaten
    # aller Postleitzahlen ein
    x = []
    y = []

    # Gehe alle Zeilen durch
    for a_line in lines:
        # Trenne die Werte bei jedem Tabulatorwert ab
        # und füge sie in einen Array ein
        pieces = split(a_line, TAB)

        # Haben wir Werte in der Zeile?
        if len(pieces) > 1 :
            # Dann lesen wir die Koordinaten ein, die
            # in der 2. und 3. Spalte der Zeile gespeichert
            # sind
            x.append(float(pieces[1]))
            y.append(float(pieces[2]))

        # Erhöhe die Anzahl der gespeicherten Orte um 1
        place_count += 1
