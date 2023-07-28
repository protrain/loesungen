# Öffentliche Klasse zur Repräsentation einer Partyverwaltung
class PartyInvitation:

    # Öffentlicher Konstruktor, der vorschreibt, dass Instanzen
    # dieser Klasse nur mit Angabe der Einladungen erfolgen kann
    def __init__(self, invitations):
        self.__invitations = List(invitations)
        self.__coming = List([])
        self.__not_coming = List([])

    # Öffentliche Methode, die die Teilnahme einer eingeladenen
    # Person vermerkt. Der Name der eingeladenen Person wird
    # an die Funktion übergeben.
    def coming(self, name):
        # Wenn die Person unter den eingeladenen Personen
        # gefunden wird
        if self.__find_and_remove(self.__invitations, name):
            # vergrößere das Teilnehmer-Array, speichere
            # diesen Gast als Teilnehmer und ersetze die bisherige
            # Liste durch die um den gerade zugesagten Teilnehmer
            # erweiterten Liste
            grown_array = self.__grown_and_add(
                self.__coming.get_array(), name)

            # Setze Array im Referenzdatentyp (hier speziell in Python
            # notwendig)
            self.__coming.set_array(grown_array)

    # Öffentliche Methode, die die Nichtteilnahme einer
    # eingeladenen Person vermerkt. Der Name der eingeladenen
    # Person wird an die Funktion übergeben.
    def not_coming(self, name):
        # Wenn die Person unter den eingeladenen Personen
        # gefunden wird
        if self.__find_and_remove(self.__invitations, name):
            # vergrößere das Nichtteilnehmer-Array, speichere
            # diesen Gast als Nichtteilnehmer und ersetze die
            # bisherige Liste durch die um den gerade zugesagten
            # Teilnehmer erweiterten Liste
            grown_array = self.__grown_and_add(
                self.__not_coming.get_array(), name)

            # Setze Array im Referenzdatentyp (hier speziell in Python
            # notwendig)
            self.__not_coming.set_array(grown_array)

    # Öffentliche Methode, die die Anzahl der Teilnehmer
    # zurückliefert.
    def number_of_coming_guests(self):
        return len(self.__coming.get_array())

    # Private Methode, die das übergebene Array um einen Teilnehmer
    # vergrößert und die an die Methode übergebene Person
    # dieser Liste hinzufügt
    def number_of_not_coming_guests(self):
        return len(self.__not_coming.get_array())

    @staticmethod
    def __grown_and_add(array, item):
        array += [item]
        return array

    # Private Methode, die in der übergebenen Liste nach dem
    # ebenfalls übergebenen Namen sucht und zurückliefert, ob
    # der Name in der Liste gefunden wurde
    @staticmethod
    def __find_and_remove(liste, item):
        # Hole Array aus Referenzdatentyp. Hier in Python wird
        # dafür ein temporäres Array angelegt, welches am Ende
        # der Funktion übernommen wird.
        array = liste.get_array()

        # Gehe Liste durch
        for i in range(0, len(array)):
            # Wenn Inhalt mit Erwartung übereinstimmt,
            # setze auf null (None in Python)
            if array[i] == item:
                array[i] = None
                # setze geändertes Array in Hilfsklasse
                liste.set_array(array)
                return True

        # Wenn nichts gefunden, dann False zurückgeben
        return False

    # Öffentliche Testfunktion, um Array-Inhalt zu testen
    def get_invitations_array(self):
        return self.__invitations.get_array()


# Hilfsklasse, um Array in Python als Referenzdatentyp nutzen zu können.
class List:
    def __init__(self, array):
        self.__array = array

    def set_array(self, array):
        self.__array = array

    def get_array(self):
        return self.__array


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

gaesteliste = ["Hinz", "Kunz", "Dirty", "Harry"]
invitations = PartyInvitation(gaesteliste)

# Hinz und Kunz kommen
invitations.coming("Hinz")
invitations.coming("Kunz")

# Harry kommt nicht
invitations.not_coming("Harry")

# Gebe kommende und nicht kommende Gäste aus
print(invitations.number_of_coming_guests())
print(invitations.number_of_not_coming_guests())

# Kontrolle, ob wirklich alle Elemente außer Harry mit None
# ersetzt wurden
print(invitations.get_invitations_array())
