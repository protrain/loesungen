# Funktion zum Tauschen von Sitzplätzen
def switchSeats(seats):
    # Anzahl der Sitze ergibt sich aus Array-Größe
    numSeats = len(seats)

    # Gehe Array bis zur Hälfte durch (bei komplettem Durchgang
    # wäre die gleiche Reihenfolge wie vorher)
    for i in range(0, numSeats / 2):
        # Hole zu tauschende Plätze
        seatA = seats[i]
        seatB = seats[numSeats - i - 1]

        # Vertausche beide Plätze
        seats[i] = seatB
        seats[numSeats - i - 1] = seatA

    return seats


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

seats = [0, 1, 2, 3, 4, 5, 6]
seatSwitched = switchSeats(seats)
# Gebe Array aus
print seatSwitched

