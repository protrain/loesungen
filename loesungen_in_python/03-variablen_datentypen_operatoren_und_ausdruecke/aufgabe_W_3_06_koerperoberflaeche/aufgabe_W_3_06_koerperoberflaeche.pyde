# Körpergröße in cm
height = 180

# Körpergewicht in kg
weight = 58

# Berechnung der Körperoberfläche nach der Formel von Mosteller
# in Quadratmeter (m^2)
a = height * weight / 3600.0
b = sqrt(a)

# Ausgabe des Ergebnisses
output = "Ein " + str(height) + " cm großer und " + str(weight)
output += " kg schwerer Mensch verfügt über ca " + str(b) + " m^2 Haut."
print output

