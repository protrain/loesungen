# Klasse, die einen Besucher repräsentiert
class Visitor:

    # Konstruktor, der die Angabe eines Preises
    # erforderlich macht
    def __init__(self, prize):
        self.__prize = prize

    # Getter-Methode zur Abfrage des Preises
    def get_prize(self):
        return self.__prize

    # Getter-Methode zur Rückgabe der Anzahl von Personen
    def get_count(self):
        return 0


# Öffentliche Klasse, die eine Personengruppe repräsentiert
# und von der Klasse Visitor erbt
class Group(Visitor):

    # Konstruktor mit der Angabe der Gruppengröße
    def __init__(self, size):
        # Aufruf der Basisklasse
        Visitor.__init__(self, 50.0)

        # Speichern der Gruppengröße lokal
        self.__size = size

    # Getter-Methode zur Rückgabe der Gruppengröße
    def get_count(self):
        return self.__size


# Öffentliche Klasse, die ein Kind repräsentiert
# und von der Klasse Visitor erbt
class Child(Visitor):

    def __init__(self):
        # Aufruf der Basisklasse
        Visitor.__init__(self, 0.0)

    # Getter-Methode zur Rückgabe der Gruppengröße
    def get_count(self):
        return 1


# Öffentliche Klasse, die einen Erwachsenen repräsentiert
# und von der Klasse Visitor erbt
class Adult(Visitor):

    def __init__(self):
        # Aufruf der Basisklasse
        Visitor.__init__(self, 15.0)

    # Getter-Methode zur Rückgabe der Gruppengröße
    def get_count(self):
        return 1


# Öffentliche Klasse, die den Eingang repräsentiert
class Entrance:

    # Öffentlicher Konstruktor, der die Gesamtzahl an
    # Gästen erwartet
    def __init__(self, size):
        self.__visitors = []

        # Leeres Array fester Größe erzeugen
        for i in range(0, size):
            self.__visitors.append(None)

        self.__visitorCount = 0

    # Methode zum Hinzufügen von Besucher(n) vom
    # Typ 'Visitor'. Instanzen aller von Visitor abgeleiteten
    # Klassen können hier übergeben werden.
    def add_visitor(self, visitor):
        self.__visitors[self.__visitorCount] = visitor
        self.__visitorCount += 1

    # Methode zur Ermittlung der gesamten Einnahmen
    def compute_turnover(self):
        to = 0.0

        # Gehe jeden Besucher durch
        for i in range(0, self.__visitorCount):
            # Addiere Preis von Besucher zum Gesamtpreis
            to += self.__visitors[i].get_prize()

        return to

    # Methode, die die Gesamtzahl an Besuchern bestimmt
    # sowie zurückliefert
    def compute_visitors(self):
        v = 0

        # Gehe jeden Besucher durch
        for i in range(0, self.__visitorCount):
            # Addiere Besucheranzahl zur Gesamtzahl
            v += self.__visitors[i].get_count()

        return v


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

entrance = Entrance(100)
entrance.add_visitor(Group(6))
entrance.add_visitor(Adult())
entrance.add_visitor(Child())
entrance.add_visitor(Child())

print("Besucher: " + str(entrance.compute_visitors()))
print("Umsatz: " + str(entrance.compute_turnover()) + " Euro")
