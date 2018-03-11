# Funktion zur Bestimmung der minimalen Distanz zweier
# benachbarter Zahlen in einem eindimensionalen Array.
# Es wird das zu überprüfende Array in die Funktion hineingegeben,
# und der Index der ersten Zahl des Paares mit der "minimalsten"
# Distanz soll zurückgegeben werden.
def minDist(input):
    # Die kleinste Distanz mit der größten erlaubten Integer-Zahl
    # initialisieren
    smallestDist = 2147483647

    # Ein Zeiger auf die kleinste Distanz initialisieren, der
    # noch auf kein Array-Element zeigt.
    smallestDistPos = -1

    # Die aktuelle Array-Größe merken
    arraySize = len(input)

    # Gehe jedes Element durch
    for i in range(0, arraySize - 1):
        # Berechne Distanz zum Nachbarn
        distTemp = abs(input[i] - input[i + 1])

        # Wenn Distanz kleiner als aktuell kleinste Distanz
        if distTemp < smallestDist:
            # dann ersetzen
            smallestDist = distTemp

            # und die Position im Array merken
            smallestDistPos = i

    return smallestDistPos


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print minDist([4, 8, 6, 1, 2, 9, 4])

