# Öffentliche Klasse zur Repräsentation einer Lampe
class Lamp(object):

    # Konstruktor, der die Angabe der Wattzahl verlangt.
    def __init__(self, watt):
        self.__watt = watt

    # Methode zur Berechnung des jährlichen Energieverbrauchs
    def annualPowerConsumption(self, hoursPerDay):
        # Formel aus Aufgabe
        return (self.__watt * hoursPerDay * 365) / 1000

    # Getter-Methode zur Rückgabe der Wattzahl
    def getWatt(self):
        return watt


# Öffentliche Klasse, die von der Klasse Lamp ableitet
class Bulb(Lamp):

    # Konstruktor verlangt ebenfalls die Angabe der Wattzahl
    def __init__(self, watt):
        # Aufruf des Basisklassenkonstruktors
        Lamp.__init__(self, watt)

    # Methode zur Rückgabe eines repräsentativen Strings
    def toString(self, hoursPerDay):
        output = "A bulb consumes "
        output += str(self.annualPowerConsumption(hoursPerDay))
        output += " KWh per year."
        return output


# Öffentliche Klasse, die von der Klasse Lamp ableitet
class LEDBulb(Lamp):

    # Konstruktor verlangt die Angabe der Wattzahl
    def __init__(self, watt):
        # Aufruf des Basisklassenkonstruktors
        Lamp.__init__(self, watt)

    # Methode zur Rückgabe eines repräsentativen Strings
    def toString(self, hoursPerDay):
        output = "A led bulb consumes "
        output += str(self.annualPowerConsumption(hoursPerDay))
        output += " KWh per year."
        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

b = Bulb(60)
l = LEDBulb(9)

print b.toString(10)
print l.toString(10)
