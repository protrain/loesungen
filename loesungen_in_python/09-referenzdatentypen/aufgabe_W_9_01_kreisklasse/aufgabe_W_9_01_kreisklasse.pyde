# Öffentliche Klasse zur Repräsentation eines Kreises
class Circle:
    # Konstruktor, der die Position im Koordinatensystem
    # sowie den Radius erwartet
    def __init__(self, x, y, radius):
        self.position = Coordinate(x, y)
        self.radius = radius

    # Öffentliche Methode zur Berechnung des Flächeninhalts
    def area(self):
        # PI*r^2
        return PI * self.radius * self.radius

    # Methode zur Ausgabe
    def toConsole(self):
        area = str(self.area())
        output =  "Ich stehe bei " + str(self.position) + " und bin " + area
        output += " gross."
        print output


# Interne Klasse zur Repräsentation einer Koordinate
class Coordinate:
    # Konstruktor, der die Angabe von x- und y-Werten
    # übernimmt und intern speichert.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Öffentliche Methode zur Rückgabe einer generierten
    # Koordinaten - Angabe
    def __str__(self):
        # Zur besseren Lesbarkeit im Code werden hier die Variablen als
        # String umgewandelt und in einer lokalen Variable gespeichert
        x = str(self.x)
        y = str(self.y)

        return "(" + x + ", " + y + ")"


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
kreis = Circle(10, 43, 4)
kreis.toConsole()
