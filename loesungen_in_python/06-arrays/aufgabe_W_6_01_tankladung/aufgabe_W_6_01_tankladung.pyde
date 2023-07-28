# Funktion zur Berechnung des durchschnittlichen Verbrauchs
# An die Funktion wird ein Array mit Integer-Werten übergeben,
# die die gefahrenen Kilometer bis zum nächsten Tankstopp
# enthalten. Die Funktion gibt den Durchschnittswert als
# Fließkommazahl zurück.
def average_battery_consumption(kilometersPerTankful):
    # Initialisierung der Variablen
    average_consumption = 0.0
    sum_kilometers = 0

    # Summiere alle Kilometer
    for kilometer in kilometersPerTankful:
        sum_kilometers += kilometer

    # Teile durch Gesamtzahl
    average_consumption = float(sum_kilometers) / len(kilometersPerTankful)

    return average_consumption


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

kilometers = [123, 134, 120, 122]

print(average_battery_consumption(kilometers))
