# Öffentliche Klasse, die einen Punkt im Koordinatensystem
# repräsentiert
class Point:
    # Konstruktor, der die Angabe von x und y bei der Objekt-
    # generierung vorschreibt.
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Getter-Methode zur Rückgabe des X-Werts
    def getX(self):
        return self.__x

    # Getter-Methode zur Rückgabe des Y-Werts
    def getY(self):
        return self.__y


# Öffentliche Klasse, die einen Polygonzug repräsentiert
class PolyLine:

    # Öffentlicher Konstruktor, der bei der Objekterzeugung
    # zur Angabe der Größe des Polygonzugs benötigt wird
    def __init__(self, size):
        # Initialisiere leeres Array
        self.__points = []
        for i in range(0, size):
            self.__points.append(None)

        self.__nextFree = 0

    # Öffentliche Methode zum Hinzufügen eines weiteren
    # Punkts in Form eines x- und  y-Werts
    def append(self, x, y):
        if self.__nextFree < len(self.__points):
            self.__points[self.__nextFree] = Point(x, y)
            self.__nextFree += 1

    # Öffentliche Methode zum Hinzufügen eines weiteren
    # Punkts, der durch ein Point-Objekt repräsentiert
    # wird
    def appendPoint(self, p):
        self.append(p.getX(), p.getY())

    # Öffentliche Methode, die den Polygonzug in einem
    # String repräsentiert. Der erzeugte String wird
    # am Ende der Funktion zurückgegeben.
    def __str__(self):
        temp = "{ "
        for i in range(0, self.__nextFree):
            temp += "(" + str(self.__points[i].getX()) + \
                "," + str(self.__points[i].getY()) + ")"

        return temp + " }"


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Neuen Polygonzug erzeugen
    poly = PolyLine(3)
    print poly

    # Füge Punkt hinzu
    poly.append(2, 4)
    print poly

    # Füge Punkt hinzu (andere Methode)
    poly.appendPoint(Point(10, 5))
    poly.append(4, 4)
    print poly

    # Füge ein Element zu viel hinzu
    poly.append(1, 1)
    println(poly)
