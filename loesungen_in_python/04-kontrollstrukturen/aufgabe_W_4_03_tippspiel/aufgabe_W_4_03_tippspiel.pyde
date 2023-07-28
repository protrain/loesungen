# Tatsächliches Endergebnis des Spiels
home = 3
guest = 2

# Getipptes Endergebnis
bet_home = 3
bet_guest = 2

# Berechnete Punkte
points = 0

# Bestimme Punktzahl
if home == bet_home and guest == bet_guest:   # exakter Tipp
    points = 3
elif home > bet_home and guest > bet_guest:   # richtige Tendenz: Sieg Heim
    points = 1
elif home < bet_home and guest < bet_guest:   # richtige Tendenz: Sieg Gast
    points = 1
elif home == bet_home and guest == bet_guest:  # richtige Tendenz: Unentschieden
    points = 1
else:                       # falscher Tipp
    points = 0

# Gebe die durch den Tipp erreichte Punktzahl aus
output = "Ergebnis: " + str(home) + ":" + str(guest)
output += ", Tipp: " + str(bet_home) + ":" + str(bet_guest)
output += " -> Punkte: " + str(points)
print(output)
