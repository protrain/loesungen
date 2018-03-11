# Funktion zum Erzeugen eines Memory-Felds
# An die Funktion wird die zu erstellende
# Größe übergeben. Die Funktion gibt als Ergebnis
# das generierte Spielfeld als zweidimensionales Array
# zurück.
def generateMemoryField(fieldSize):
    # Anzahlnummer der Karten
    numElements = fieldSize * fieldSize

    # Gültige Spielfeldgröße?
    if numElements % 2 == 0 and numElements > 0:
        # Erzeuge leeres Spielfeld (fieldSize x fieldSize)
        memoryField = createArray(fieldSize)

        numPaare = numElements / 2

        # Belege Feld mit möglichen Zahlen
        for number in range(1, numPaare + 1):
            # Immer zweimal (= 1 Paar) durchführen
            for j in range(0, 2):
                # Wähle zufällige Position
                randomX = int(random(0, fieldSize))
                randomY = int(random(0, fieldSize))

                # Solange Position schon belegt, neue Position wählen
                while memoryField[randomX][randomY] != 0:
                    randomX = int(random(0, fieldSize))
                    randomY = int(random(0, fieldSize))

                # setze Zahl
                memoryField[randomX][randomY] = number

        return memoryField
    else:
        # ungültige Spielfeldgröße
        return []


# Funktion zur Visualisierung des berechneten Spielfelds
# An die Funktion wird das generierte Spielfeld als
# zweidimensionales Array übergeben.
def visualizeMemoryField(memoryField):
    fieldSize = len(memoryField)
    if fieldSize == 0:
        return

    # Pixel pro Schritt
    stepSize = width / fieldSize

    # Halbe Größe einer Karte
    stepMiddle = stepSize / 2

    x = 0
    y = 0
    for row in memoryField:
        x = 0
        for element in row:

            # Karte als Rechteck zeichnen
            fill(255)
            stroke(0)
            rect(x, y, x + stepSize, y + stepSize)

            # Zahlen reinzeichnen
            fill(0)
            textSize(stepMiddle)
            text(
                element,
                x +
                stepMiddle /
                2,
                y +
                stepMiddle +
                stepMiddle /
                4)
            x = x + stepSize
        y = y + stepSize

# Generiert leeres 2D-Array in den Dimensionen arraySize x arraySize
def createArray(arraySize):
    output = []
    for y in range(0, arraySize):
        row = []
        for x in range(0, arraySize):
            row = row + [0]
        output = output + [row]
    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(600, 600)
background(255, 255, 255)

memoryField = generateMemoryField(4)
visualizeMemoryField(memoryField)

