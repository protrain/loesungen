# Variablen deklarieren und initialisieren
a = 1
b = 2
c = 3

# Variable deklarieren, die den maximalen Wert halten soll
maxi = -2147483648  # kleinste erlaubte Integer-Zahl

# Maximum bestimmen
if a > b:        # a > B
    if a > c:      # a > b > C
        maxi = a
    else:        # c > a > B
        maxi = c
else:          # b > A
    if b > c:      # b > a > C
        maxi = b
    else:        # c > b > A
        maxi = c

# Ausgabe des Maximums in der Konsole
output = "Der größte Wert in der Menge {" + str(a) + ", "
output += str(b) + ", " + str(c) + "} lautet: " + str(maxi)
print(output)
