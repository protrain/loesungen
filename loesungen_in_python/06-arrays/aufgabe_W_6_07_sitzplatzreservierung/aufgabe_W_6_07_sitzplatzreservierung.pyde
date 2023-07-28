# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# Library importiert werden
from random import randint as random

# Globale Symbolkonstanten
FREE = '_'     # Freier Sitz
TAKEN = '#'    # Belegter Sitz

# Globale Arena
arena = []
min_seats = 3   # Anzahl der Sitze in der letzten Reihe


# Funktion zum Generieren einer neuen Arena. Als
# Eingabewert dient die Anzahl an Zeilen. Die Arena
# wird in einem Array von Chars zurückgegeben
def create_arena(num_rows):
    # zu befüllendes Gesamt-Array
    arena = []

    # Gehe numerisch jede zu erzeugende Reihe durch
    for i in range(0, num_rows):
        # Anzahl der Sitze in aktueller Reihe
        num_seats = num_rows - i + (min_seats - 1)

        # Einzelne Reihe
        row = []
        # Gehe numerisch jeden zu erzeugenden Sitz durch
        for x in range(0, num_seats):
            # Füge Array-Element hinzu
            row.append(FREE)
        # Füge Reihe in Arena hinzu
        arena.append(row)

    return arena


# Funktion, die die Arena grafisch darstellt
# Erhält ein zweidimensionales Char-Array
def visualize_arena(arena):
    # Gehe jede Reihe durch
    for y in arena:
        # leeres Stringobjekt erzeugen, dient zur Ausgabe
        # in der Konsole
        row = ""

        # Gehe jeden Sitz durch
        for x in y:
            # Füge Character in Reihe dem Reihenstring hinzu
            row = row + x

        # gebe String mit Sitzreihe aus und mache Zeilenumbruch
        # (für die nächste Reihe)
        print(row)


# Funktion zum Buchen eines einzelnen Sitzplatzes
# Als Eingabe wird die Reihe und der Platz angegeben
def book_seat(row, seat):
    # Das globale Arena-Array holen
    global arena

    # Zur Änderung der Reihe wird temporäre Reihe angelegt
    row_temp = arena[row]

    # Setze Sitzplaz auf Belegt
    row_temp[seat] = TAKEN

    # Ersetze Reihe mit geänderter Reihe
    arena[row] = row_temp


# Funktion zum zufälligen Buchen von Sitzplätzen
# in der gesamten Arena
def fill_seats():
    # Das globale Arena-Array holen
    global arena

    # Anzahl der Reihen
    num_rows = len(arena)

    # Gehe jede Reihe durch (von Reihe 0 bis Gesamtzahl)
    for y in range(0, num_rows):
        # Stuhlanzahl in einer Reihe
        num_seats = num_rows - y + (min_seats - 1)
        # Gehe jeden Sitz durch
        for x in range(0, num_seats):
            # Zufallszahl zwischen 0 und 1 (Random ist Zahl
            # von 0 bis 1,9999999...)
            random_number = int(random(0, 2))
            # Wenn Zufallszahl eine 1 ist, soll Sitz gebucht
            # werden
            if random_number == 1:
                book_seat(y, x)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

arena = create_arena(10)
fill_seats()
visualize_arena(arena)
