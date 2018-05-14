# Funktion zur Überprüfung einer Sudoku-Lösung auf Korrektheit.
# Als Eingabe an die Funktion wird die Sudoku-Lösung in Form eines
# zweidimensionalen Arrays übergeben. Die Funktion gibt als Ergebnis
# einen Wahrheitswert zurück.
def checkSudoku(sudoku):
    # Array, das die Anzahl der Vorkommnisse jeder Zahl aufschreibt
    # Position: Zahl
    # Inhalt an Position: Anzahl der Zahl
    occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Prüfe Zeilen
    # Gehe jede Zeile durch
    for y in sudoku:
        # Gehe jedes Element in der Zeile durch
        for x in y:
            # Erhöhe Zähler für Zahl um 1
            occurrences[x] += 1

        # Gehe Zähler-Array durch
        for i in occurrences:
            # Wenn Zahl häufiger als einmal vorkommt
            # -> Keine gültige Lösung
            if i > 1 and i != 0:
                return False

        # Zähler-Array wieder auf 0 setzen
        occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Prüfe Spalten
    # Gehe jede Spalte durch
    for x in range(0, 8):
        # Gehe jedes Element in der Spalte durch
        for y in range(0, 8):
            # Hole Zahl aus Position in Sudoku
            number = sudoku[y][x]

            # Erhöhe Zähler für Zahl um 1
            occurrences[number] += 1

        # Gehe Zähler-Array durch
        for i in occurrences:
            # Wenn Zahl häufiger als einmal vorkommt
            # -> Keine gültige Lösung
            if i > 1 and i != 0:
                return False

        # Zähler-Array wieder auf 0 setzen
        occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Prüfe 3x3 Blöcke
    # Bestimme Blocknummer
    for i in range(0, 3):     # Blocknummer in x-Richtung
        for j in range(0, 3):  # Blocknummer in y-Richtung
            # Gehe inneren Block durch
            for y in range(0, 3):
                for x in range(0, 3):
                    # Bestimme globale Position
                    posX = 3 * i + x
                    posY = 3 * j + y

                    # Bestimme Zahl
                    number = sudoku[posY][posX]

                    # Erhöhe Zähler für Zahl um 1
                    occurrences[number] += 1

            # Gehe Zähler-Array durch
            for k in occurrences:
                # Wenn Zahl häufiger als einmal vorkommt
                # -> Keine gültige Lösung
                if k > 1 and k != 0:
                    return False

            # Zähler-Array wieder auf 0 setzen
            occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

print checkSudoku(sudoku)

