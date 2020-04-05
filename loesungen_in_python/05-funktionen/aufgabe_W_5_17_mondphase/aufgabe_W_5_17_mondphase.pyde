# Gebe den angegebenen Tag als julianisches Datum zurück
def getJulianDate(year, month, day):
    if month < 2:
        year = year + 1
        month = month + 12

    b = 2 - (year / 100) + (year / 400)
    return (365.25 * (year + 4716) + (30.6001 * (month + 1))
            + day + b - 1524.5)

# Gebe die Mondphase als String zurück


def getMoonPhase(year, month, day):
    # Definiere den Mondzyklus in Tagen
    moonCyclus = 29.53

    # Definiere einen Tag, an dem Neumond war
    # Wir nehmen hier den 28.09.2019
    newMoon = getJulianDate(2019, 9, 28)

    # Definiere den Tag, für den wir die Mondphase berechnen wollen
    dateToday = getJulianDate(year, month, day)

    # Berechne die Tage seit dem letzten Neumond
    daysSinceLastNewMoon = int(dateToday - newMoon)

    # Berechne die Anzahl der Neumonde, die seit dem angegebenen
    # Neumond-Datum waren
    newMoonCount = daysSinceLastNewMoon / moonCyclus

    # Nehmen wir die Nachkommastelle, wissen wir, wo wir in
    # der Mondphase stehen
    moonPosition = newMoonCount % 1

    # Bei Werten kleiner als 0.5 haben wir einen zunehmenden Mond
    if moonPosition < 0.5:
        return "Zunehmender Mond"

    # Andernfalls haben wir einen abnehmenden Mond
    return "Abnehmender Mond"


# Jetzt folgen die Testbedingungen
print "11.11.2019: {}".format(getMoonPhase(2019, 11, 11))
print "12.11.2019: Vollmond"
print "13.11.2019: {}".format(getMoonPhase(2019, 11, 13))
print "25.11.2019: {}".format(getMoonPhase(2019, 11, 25))
print "26.11.2019: Neumond"
print "27.11.2019: {}".format(getMoonPhase(2019, 11, 27))
