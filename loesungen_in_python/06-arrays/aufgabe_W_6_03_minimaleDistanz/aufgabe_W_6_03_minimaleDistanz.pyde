# Funktion zur Bestimmung der minimalen Distanz zweier
# benachbarter Zahlen in einem eindimensionalen Array.
# Es wird das zu überprüfende Array in die Funktion hineingegeben,
# und der Index der ersten Zahl des Paares mit der "minimalsten"
# Distanz soll zurückgegeben werden.
def min_dist(input_data):
    # Die kleinste Distanz mit der größten erlaubten Integer-Zahl
    # initialisieren
    smallest_dist = 2147483647

    # Ein Zeiger auf die kleinste Distanz initialisieren, der
    # noch auf kein Array-Element zeigt.
    smallest_dist_pos = -1

    # Die aktuelle Array-Größe merken
    array_size = len(input_data)

    # Gehe jedes Element durch
    for i in range(0, array_size - 1):
        # Berechne Distanz zum Nachbarn
        dist_temp = abs(input_data[i] - input_data[i + 1])

        # Wenn Distanz kleiner als aktuell kleinste Distanz
        if dist_temp < smallest_dist:
            # dann ersetzen
            smallest_dist = dist_temp

            # und die Position im Array merken
            smallest_dist_pos = i

    return smallest_dist_pos


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print(min_dist([4, 8, 6, 1, 2, 9, 4]))
