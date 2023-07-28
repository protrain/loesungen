# Öffentliche Klasse zur Repräsentation einer Lampe
class Lamp(object):

    # Konstruktor, der die Angabe der Wattzahl verlangt.
    def __init__(self, watt):
        self.__watt = watt

    # Methode zur Berechnung des jährlichen Energieverbrauchs
    def annual_power_consumption(self, hours_per_day):
        # Formel aus Aufgabe
        return (self.__watt * hours_per_day * 365) / 1000

    # Getter-Methode zur Rückgabe der Wattzahl
    def get_watt(self):
        return self.__watt


# Öffentliche Klasse, die von der Klasse Lamp ableitet
class Bulb(Lamp):

    # Konstruktor verlangt ebenfalls die Angabe der Wattzahl
    def __init__(self, watt):
        # Aufruf des Basisklassenkonstruktors
        Lamp.__init__(self, watt)

    # Methode zur Rückgabe eines repräsentativen Strings
    def to_string(self, hours_per_day):
        output = "A bulb consumes "
        output += str(int(self.annual_power_consumption(hours_per_day)))
        output += " KWh per year."
        return output


# Öffentliche Klasse, die von der Klasse Lamp ableitet
class LEDBulb(Lamp):

    # Konstruktor verlangt die Angabe der Wattzahl
    def __init__(self, watt):
        # Aufruf des Basisklassenkonstruktors
        Lamp.__init__(self, watt)

    # Methode zur Rückgabe eines repräsentativen Strings
    def to_string(self, hours_per_day):
        output = "A led bulb consumes "
        output += str(int(self.annual_power_consumption(hours_per_day)))
        output += " KWh per year."
        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

b = Bulb(60)
led = LEDBulb(9)

print(b.to_string(10))
print(led.to_string(10))
