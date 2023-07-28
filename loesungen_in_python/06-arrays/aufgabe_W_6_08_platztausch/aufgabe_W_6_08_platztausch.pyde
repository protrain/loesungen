# Funktion zum Tauschen von Sitzplätzen
def switch_seats(seats):
    # Anzahl der Sitze ergibt sich aus Array-Größe
    num_seats = len(seats)

    # Gehe Array bis zur Hälfte durch (bei komplettem Durchgang
    # wäre die gleiche Reihenfolge wie vorher)
    for i in range(0, int(num_seats / 2)):
        # Hole zu tauschende Plätze
        seat_a = seats[i]
        seat_b = seats[num_seats - i - 1]

        # Vertausche beide Plätze
        seats[i] = seat_b
        seats[num_seats - i - 1] = seat_a

    return seats


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

seats = [0, 1, 2, 3, 4, 5, 6]
seat_switched = switch_seats(seats)
# Gebe Array aus
print(seat_switched)
