# Tatsächliches Endergebnis des Spiels
home = 3
guest = 2

# Getipptes Endergebnis
betHome = 3
betGuest = 2

# Berechnete Punkte
points = 0

# Bestimme Punktzahl
if home == betHome and guest == betGuest: 	# exakter Tipp
    points = 3
elif home > betHome and guest > betGuest: 	# richtige Tendenz: Sieg Heim
    points = 1
elif home < betHome and guest < betGuest: 	# richtige Tendenz: Sieg Gast
    points = 1
elif home == betHome and guest == betGuest: # richtige Tendenz: Unentschieden
    points = 1
else:       								# falscher Tipp
    points = 0

# Gebe die durch den Tipp erreichte Punktzahl aus
output = "Ergebnis: " + str(home) + ":" + str(guest)
output += ", Tipp: " + str(betHome) + ":" + str(betGuest)
output += " -> Punkte: " + str(points)
print output

