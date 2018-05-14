def check_sudoku(sudoku):
    """ Funktion zur Überprüfung einer Sudoku-Lösung auf Korrektheit.
    Als Eingabe an die Funktion wird die Sudoku-Lösung in Form einer
    Liste von Listen übergeben. Die Funktion gibt als Ergebnis
    einen Wahrheitswert zurück. """

    # Prüfe Zeilen
    # Gehe jede Zeile durch
    for line in sudoku:
        occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Gehe jedes Element in der Zeile durch
        for number in line:
            # Erhöhe Zähler für Zahl um 1
            occurrences[number - 1] += 1

        # Wenn Zahl häufiger als einmal vorkommt
        # -> Keine gültige Lösung
        if max(occurences) > 1:
            return False

    # Prüfe Spalten
    # Gehe jede Spalte durch
    for column in range(8):
        occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Gehe jedes Element in der Spalte durch
        for line in sudoku:
            # Hole Zahl aus Position in Sudoku
            number = line[column]

            # Erhöhe Zähler für Zahl um 1
            occurrences[number - 1] += 1

        # Wenn Zahl häufiger als einmal vorkommt
        # -> Keine gültige Lösung
        if max(occurences) > 1:
            return False

    # Prüfe 3x3 Blöcke
    # Bestimme Blocknummer
    for i in range(3):     # Blocknummer in x-Richtung
        for j in range(3):  # Blocknummer in y-Richtung
            occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            # Gehe inneren Block durch
            for y in range(3):
                for x in range(3):
                    # Bestimme globale Position
                    pos_x = 3 * i + x
                    pos_y = 3 * j + y

                    # Bestimme Zahl
                    number = sudoku[pos_y][pos_x]

                    # Erhöhe Zähler für Zahl um 1
                    occurrences[number - 1] += 1

            # Wenn Zahl häufiger als einmal vorkommt
            # -> Keine gültige Lösung
            if max(occurences) > 1:
                return False

    # Wenn das Programm bis an diese Stelle kommt, wurde keine "return"-
    # Anweisung ausgeführt. Das bedeutet, die Prüfung ist erfolgreich!
    return True


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

# Test-Sudoku
sudoku = [[8, 3, 5, 4, 1, 6, 9, 2, 7],
          [2, 9, 6, 8, 5, 7, 4, 3, 1],
          [4, 1, 7, 2, 9, 3, 6, 5, 8],
          [5, 6, 9, 1, 3, 4, 7, 8, 2],
          [1, 2, 3, 6, 7, 8, 5, 4, 9],
          [7, 4, 8, 5, 2, 9, 1, 6, 3],
          [6, 5, 2, 7, 8, 1, 3, 9, 4],
          [9, 8, 1, 3, 4, 5, 2, 7, 6],
          [3, 7, 4, 9, 6, 2, 8, 1, 5]]

print check_sudoku(sudoku)

