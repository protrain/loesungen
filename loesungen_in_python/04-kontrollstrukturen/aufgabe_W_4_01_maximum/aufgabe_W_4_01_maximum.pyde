# Variablen deklarieren und initialisieren
a = 1
b = 2
c = 3

# Variable deklarieren, die den maximalen Wert halten soll
maxi = -2147483648  # kleinste erlaubte Integer-Zahl

# Maximum bestimmen
if a > b:  			# a > b
    if a > c:  		# a > b > c
        maxi = a
    else:  			# c > a > b
        maxi = c
else:  				# b > a
    if b > c:  		# b > a > c
        maxi = b
    else:  			# c > b > a
        maxi = c

# Ausgabe des Maximums in der Konsole
output = "Der größte Wert in der Menge {" + str(a) + ", "
output += str(b) + ", " + str(c) + "} lautet: " + str(maxi)
print output

