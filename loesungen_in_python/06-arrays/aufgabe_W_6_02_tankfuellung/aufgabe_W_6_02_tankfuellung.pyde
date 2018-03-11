# Funktion zur Berechnung des durchschnittlichen Verbrauchs
# An die Funktion wird ein Array mit Integer-Werten übergeben,
# die die gefahrenen Kilometer bis zum nächsten Tankstopp
# enthalten. Die Funktion gibt den Durchschnittswert als
# Fließkommazahl zurück.
def averageFuelComsumption(kilometersPerTankful):
    # Initialisierung der Variablen
    averageConsumption = 0.0
    sumKilometers = 0

    # Summiere alle Kilometer
    for kilometer in kilometersPerTankful:
        sumKilometers += kilometer

    # Teile durch Gesamtzahl
    averageConsumption = float(sumKilometers) / len(kilometersPerTankful)

    return averageConsumption


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

kilometers = [123, 134, 120, 122]

print averageFuelComsumption(kilometers)

