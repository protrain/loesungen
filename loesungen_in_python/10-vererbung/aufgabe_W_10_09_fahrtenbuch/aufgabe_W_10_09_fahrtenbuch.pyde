# Basisklasse für alle Fahrzeuge
class Fahrzeug(object):

    # Konstruktor, der vorgibt, dass ein
    # Kilometersatz angegeben werden muss
    def __init__(self, kmSatz):
        self.__kmSatz = kmSatz

    # Getter zur Rückgabe des Kilometersatzes
    def getKmSatz(self):
        return self.__kmSatz


# Klasse Fahrrad, die von der Klasse Fahrzeug erbt
class Fahrrad(Fahrzeug):

    # Rufe Superklasse auf und setze Fahrpreis auf 1,00 EUR fest
    def __init__(self):
        Fahrzeug.__init__(self, 1.00)


class Motorroller(Fahrzeug):

    # Rufe Superklasse auf und setze Fahrpreis auf 2,00 EUR fest
    def __init__(self):
        Fahrzeug.__init__(self, 2.00)


class Kleintransporter(Fahrzeug):

    # Rufe Superklasse auf und setze Fahrpreis auf 5,50 EUR fest
    def __init__(self):
        Fahrzeug.__init__(self, 5.50)


# Klasse, die eine Fahrt repräsentiert
class Fahrt:

    # Konstruktor der die Angabe eines Fahrzeugs
    # und die gefahrenen Kilometer vorschreibt
    def __init__(self, fahrzeug, km):
        self.__fahrzeug = fahrzeug
        self.__km = km

    # Methode zur Berechnung des Fahrpreises
    # (Kilometersatz * Kilometer)
    def getPrice(self):
        return self.__fahrzeug.getKmSatz() * self.__km


# Klasse, die ein Fahrtenbuch repräsentiert
class Fahrtenbuch:

    # Konstruktor, der die Fahrten initialisiert
    def __init__(self):
        self.__fahrten = []

    # Öffentliche Methode zum Hinzufügen einer Fahrt,
    # die als Fahrtobjekt an die Methode übergeben wird
    def addFahrt(self, fahrt):
        self.__fahrten.append(fahrt)

    # Getter-Methode, die den Preis zurückliefert
    def getPrice(self):
        # Gesamtpreis
        price = 0.0

        # Gehe jede Fahrt durch.
        for fahrt in self.__fahrten:
            # Berechne Preis
            price += fahrt.getPrice()

        return price


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

# Erstelle Fahrtenbuch
fb = Fahrtenbuch()

# Füge Fahrten hinzu
fb.addFahrt(Fahrt(Fahrrad(), 3))
fb.addFahrt(Fahrt(Motorroller(), 7.12))
fb.addFahrt(Fahrt(Kleintransporter(), 56.11))

# Berechne Gesamtpreis
print fb.getPrice()
