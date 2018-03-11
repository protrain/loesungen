# Öffentliche Klasse zur Repräsentation eines Bruchs
class Fraction:
    # Konstruktor, der Zähler und Nenner eines Bruchs
    # anfordert
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Öffentliche Methode zum Addieren eines Bruchs
    # Zum aktuellen Bruch wird der an die Methode über-
    # gebene Bruch addiert und als eigenständiges Objekt
    # zurückgegeben.
    def add(self, f):
        z1 = self.numerator * f.getDenominator()
        z2 = self.denominator * f.getNumerator()
        return Fraction(z1 + z2, self.denominator * f.getDenominator())

    # Öffentliche Methode zum Multiplizieren eines Bruchs.
    # Der aktuelle Bruch wird mit dem an die Methode über-
    # gebenen Bruch multipliziert und als eigenständiges
    # Objekt zurückgegeben.
    def multiply(self, f):
        return Fraction(self.numerator * f.getNumerator(),
                        self.denominator * f.getDenominator())

    # Öffentliche Methode, die den Zähler zurückliefert
    def getNumerator(self):
        return self.numerator

    # Öffentliche Methode, die den Nenner zurückliefert
    def getDenominator(self):
        return self.denominator

    # Öffentliche Methode zur Ausgabe eines Bruchs
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

# 1/2
f1 = Fraction(1, 2)
# 1/4
f2 = Fraction(1, 4)

# 1/2 + 1/4 = 6/8
sum = f1.add(f2)
print str(f1) + " + " + str(f2) + " = " + str(sum)

# 1/2 + 1/4 = 1/8
mult = f1.multiply(f2)
print str(f1) + " * " + str(f2) + " = " + str(mult)
