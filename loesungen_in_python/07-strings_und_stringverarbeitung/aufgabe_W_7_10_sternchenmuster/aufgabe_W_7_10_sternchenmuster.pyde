# Funktion zum Zeichnen von Sternchenmuster in der Kommandozeile
# An die Funktion wird die Anzahl an Zeilen übergeben.
def draw_stars(rows):
    # Zeilen von oben bis Mitte
    for num_stars in range(1, rows):
        print_stars(num_stars)

    # In der Mitte werden (fast) doppelt so viele
    # ausgegeben
    print_stars(rows * 2 - 1)

    # Für die nachfolgenden Zeilen ...
    for i in range(1, rows):
        # ... immer ein Sternchen weniger ausgeben
        num_stars = rows - i
        # Aufruf mit zwei Parametern, damit die Leerzeichen
        # berücksichtigt werden
        print_stars(num_stars, rows)


# Zeichnet angegebene Nummer an Sternen in eine Reihe
# Funktion zum Zeichnen der Anzahl angegebener Sternchen
# mit Berücksichtigung von Leerzeichen.
# Die Funktion erhält die Anzahl der auszugebenden Sterne
# sowie die Anzahl von Leerzeichen.
def print_stars(num_stars, num_space=0):
    row = ""

    # Füge ggf. Leerzeichen hinzu
    for i in range(0, num_space):
        row += " "

    for i in range(0, num_stars):
        row += "*"

    print(row)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
draw_stars(4)
