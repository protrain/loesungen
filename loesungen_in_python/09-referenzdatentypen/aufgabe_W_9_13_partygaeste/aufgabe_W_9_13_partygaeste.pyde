# Öffentliche Klasse zur Repräsentation einer Partyverwaltung
class PartyInvitation:

    # Öffentlicher Konstruktor, der vorschreibt, dass Instanzen
    # dieser Klasse nur mit Angabe der Einladungen erfolgen kann
    def __init__(self, invitations):
        self.__invitations = List(invitations)
        self.__coming = List([])
        self.__notComing = List([])

    # Öffentliche Methode, die die Teilnahme einer eingeladenen
    # Person vermerkt. Der Name der eingeladenen Person wird
    # an die Funktion übergeben.
    def coming(self, name):
        # Wenn die Person unter den eingeladenen Personen
        # gefunden wird
        if self.__findAndRemove(self.__invitations, name):
            # vergrößere das Teilnehmer-Array, speichere
            # diesen Gast als Teilnehmer und ersetze die bisherige
            # Liste durch die um den gerade zugesagten Teilnehmer
            # erweiterten Liste
            grownArray = self.__growAndAdd(
                self.__coming.getArray(), name)

            # Setze Array im Referenzdatentyp (hier speziell in Python
            # notwendig)
            self.__coming.setArray(grownArray)

    # Öffentliche Methode, die die Nichtteilnahme einer
    # eingeladenen Person vermerkt. Der Name der eingeladenen
    # Person wird an die Funktion übergeben.
    def notComing(self, name):
        # Wenn die Person unter den eingeladenen Personen
        # gefunden wird
        if self.__findAndRemove(self.__invitations, name):
            # vergrößere das Nichtteilnehmer-Array, speichere
            # diesen Gast als Nichtteilnehmer und ersetze die
            # bisherige Liste durch die um den gerade zugesagten
            # Teilnehmer erweiterten Liste
            grownArray = self.__growAndAdd(
                self.__notComing.getArray(), name)

            # Setze Array im Referenzdatentyp (hier speziell in Python
            # notwendig)
            self.__notComing.setArray(grownArray)

    # Öffentliche Methode, die die Anzahl der Teilnehmer
    # zurückliefert.
    def numberOfComingGuests(self):
        return len(self.__coming.getArray())

    # Private Methode, die das übergebene Array um einen Teilnehmer
    # vergrößert und die an die Methode übergebene Person
    # dieser Liste hinzufügt
    def numberOfNotComingGuests(self):
        return len(self.__notComing.getArray())

    @staticmethod
    def __growAndAdd(array, item):
        array += [item]
        return array

    # Private Methode, die in der übergebenen Liste nach dem
    # ebenfalls übergebenen Namen sucht und zurückliefert, ob
    # der Name in der Liste gefunden wurde
    @staticmethod
    def __findAndRemove(liste, item):
        # Hole Array aus Referenzdatentyp. Hier in Python wird
        # dafür ein temporäres Array angelegt, welches am Ende
        # der Funktion übernommen wird.
        array = liste.getArray()

        # Gehe Liste durch
        for i in range(0, len(array)):
            # Wenn Inhalt mit Erwartung übereinstimmt,
            # setze auf null (None in Python)
            if array[i] == item:
                array[i] = None
                # setze geändertes Array in Hilfsklasse
                liste.setArray(array)
                return True

        # Wenn nichts gefunden, dann False zurückgeben
        return False

    # Öffentliche Testfunktion, um Array-Inhalt zu testen
    def getInvitationsArray(self):
        return self.__invitations.getArray()

# Hilfsklasse, um Array in Python als Referenzdatentyp nutzen zu können.
class List:
    def __init__(self, array):
        self.__array = array

    def setArray(self, array):
        self.__array = array

    def getArray(self):
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
invitations.notComing("Harry")

# Gebe kommende und nicht kommende Gäste aus
print invitations.numberOfComingGuests()
print invitations.numberOfNotComingGuests()

# Kontrolle, ob wirklich alle Elemente außer Harry mit None
# ersetzt wurden
print invitations.getInvitationsArray()
