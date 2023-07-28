# Öffentliche Klasse, die einen Punkt im Koordinatensystem
# repräsentiert
class Point:
    # Konstruktor, der die Angabe von x und y bei der Objekt-
    # generierung vorschreibt.
    def __init__(self, point_x, point_y):
        self.__x = point_x
        self.__y = point_y

    # Getter-Methode zur Rückgabe des X-Werts
    def get_x(self):
        return self.__x

    # Getter-Methode zur Rückgabe des Y-Werts
    def get_y(self):
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

        self.__next_free = 0

    # Öffentliche Methode zum Hinzufügen eines weiteren
    # Punkts in Form eines x- und  y-Werts
    def append(self, point_x, point_y):
        if self.__next_free < len(self.__points):
            self.__points[self.__next_free] = Point(point_x, point_y)
            self.__next_free += 1

    # Öffentliche Methode zum Hinzufügen eines weiteren
    # Punkts, der durch ein Point-Objekt repräsentiert
    # wird
    def append_point(self, point):
        self.append(point.get_x(), point.get_y())

    # Öffentliche Methode, die den Polygonzug in einem
    # String repräsentiert. Der erzeugte String wird
    # am Ende der Funktion zurückgegeben.
    def __str__(self):
        temp = "{ "
        for i in range(0, self.__next_free):
            temp += "(" + str(self.__points[i].get_x()) + \
                "," + str(self.__points[i].get_y()) + ")"

        return temp + " }"


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Neuen Polygonzug erzeugen
    poly = PolyLine(3)
    print(poly)

    # Füge Punkt hinzu
    poly.append(2, 4)
    print(poly)

    # Füge Punkt hinzu (andere Methode)
    poly.append_point(Point(10, 5))
    poly.append(4, 4)
    print(poly)

    # Füge ein Element zu viel hinzu
    poly.append(1, 1)
    print(poly)


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
