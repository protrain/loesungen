# Definiere globale Variablen

# Anzahl der gespeicherten PLZ-Orte im Array
placeCount = 0

# Maximale Werte der x-und y-Koordinaten
minX = 0
maxX = 0
minY = 0
maxY = 0

# Zeichenbereich-Abmessungen der Karte
mapX1 = 0
mapY1 = 0
mapX2 = 0
mapY2 = 0

# Array, in dem wir die x- und y-Koordinaten
# speichern werden
x = []
y = []


def setup():
    # Lade globale Variablen, damit wir die Werte ändern können
    global placeCount, minX, maxX, minY, maxY, mapX1, mapY1, mapX2
    global mapY2, x, y

    # Setze Fenstergröße
    size(380, 450)

    # Setze Zeichenbereich für die Karte
    # Zeichenbereich-Abmessungen der Karte
    # Obere linke Ecke
    mapX1 = 30
    mapY1 = 20
    # Untere rechte Ecke
    mapX2 = width - mapX1
    mapY2 = height - mapY1

    # Lese die Koordinaten ein
    readData()


def draw():
    # Lade globale Variablen, damit wir die Werte ändern können
    global placeCount, minX, maxX, minY, maxY, mapX1, mapY1, mapX2
    global mapY2, x, y

    # Setze schwarzen Hintergrund
    background(0)

    # Setze weiße Kreisfarbe
    stroke(255)
    fill(255)
    for i in range(0, len(x)):
        # Setze x- und y-Koordinaten in Abhängigkeit vom
        # Zeichenbereich
        xDraw = map(x[i], minX, maxX, mapX1, mapX2)

        # Koordinatensystem bei Y ist umgekehrt, daher sind
        # Y2 und Y1 vertauscht
        yDraw = map(y[i], minY, maxY, mapY2, mapY1)

        # Male Kreis
        ellipse(xDraw, yDraw, 1, 1)

# Funktion, die die Postleitzahldaten und 2D-Koordinaten
# aus einer CSV-Datei einliest und in einem Array speichert


def readData():
    # Lade globale Variablen, damit wir die Werte ändern können
    global placeCount, minX, maxX, minY, maxY, mapX1, mapY1, mapX2
    global mapY2, x, y

    # Lese die CSV-Datei ein
    lines = loadStrings("zip_de_prep.csv")

    # Setze die Minimal- und Maximalwerte der Koordinaten in
    # der CSV-Datei
    minX = -0.056436524
    maxX = 0.044636916
    minY = 0.7982389
    maxY = 0.9287888

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
        if len(pieces) > 1:
            # Dann lesen wir die Koordinaten ein, die
            # in der 2. und 3. Spalte der Zeile gespeichert
            # sind
            x.append(float(pieces[1]))
            y.append(float(pieces[2]))

        # Erhöhe die Anzahl der gespeicherten Orte um 1
        placeCount += 1
