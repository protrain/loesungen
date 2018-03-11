# Funktion zum Vergrößern eines quadratisches Array um den Faktor f
# Eingabe ist ein zweidimensionales Array mit boolean-Werten sowie
# der Faktor, um den das Array vergrößert werden soll
def magnify(input, f):
    # Die aktuelle Größe entspricht der Anzahl an Array-Elementen
    # einer Dimension
    inputSize = len(input)

    # Berechnen der Ergebnisgröße des Arrays
    outputSize = f * inputSize

    # Generiere leeren Output-Array in der neuen Größe
    output = createArray(outputSize)

  # Gehe jedes Element in Input durch und schreibe es in die skalierten
  # Felder im Output
    for y in range(0, inputSize):       # Iteration durch Zeilen
        for x in range(0, inputSize):   # Iteration durch Spalten
            for j in range(0, f):       # Iteration für den Zeilenfaktor
                for i in range(
                        0, f):   # Iteration für den Spaltenfaktor
                    # Schreiben des Werts
                    output[x * f + j][y * f + i] = input[x][y]

    return output

# Funktion, die ein leeres 2D-Array in den Dimensionen
# arraySize x arraySize erzeugt und zurückgibt
def createArray(arraySize):
    output = []
    for y in range(0, arraySize):
        row = []
        for x in range(0, arraySize):
            row = row + [False]
        output = output + [row]
    return output

# Funktion, die das Array grafisch im Ausgabefenster darstellt
# Als Eingabe erfolgt das Array.
def drawArray(input):
    # Array-Größe. Da das Array quadratisch sein soll, reicht die Höhe
    # des Arrays aus
    inputSize = len(input)

    # Höhe und Breite jedes Rechtecks (definiert durch Fenstergröße)
    rectWidth = width / inputSize
    rectHeight = height / inputSize

    for y in range(0, inputSize):
        for x in range(0, inputSize):
            # Setze Farbe nach Array-Inhalt
            # Um einzelne Elemente sichtbar zu machen, ist Linienfarbe
            # stets das Gegenteil der Füllfarbe
            if input[y][x] == False:
                stroke(0)
                fill(255)
            else:
                stroke(255)
                fill(0)

            # Zeichne Rechteck
            # startX,startY: obere linke Ecke des Rechtecks
            # startX+rectWidth, startY+rectHeight: untere linke Ecke
            # des Rechtecks
            startX = x * rectWidth
            startY = y * rectHeight
            rect(startX, startY, startX + rectWidth, startY + rectHeight)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

size(200, 200)
background(255)
eingabe = [[True, False], [False, False]]
drawArray(magnify(eingabe, 1))

