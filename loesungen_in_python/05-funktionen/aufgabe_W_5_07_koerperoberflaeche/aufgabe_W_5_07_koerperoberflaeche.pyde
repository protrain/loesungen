# Funktion zur Berechnung der Körperoberfläche
# Das Gewicht und die Größe werden als Integer-Werte an die Funktion
# übergeben, die das Ergebnis der Berechnung als Fließkommazahl
# zurückliefert

# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# Library importiert werden
#from math import sqrt


def kof(height, weight):
    a = height * weight / 3600.0
    b = sqrt(a)                 # Berechnung der Wurzel von a
    return b


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print(kof(180, 58))
