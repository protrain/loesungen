# Öffentliche Klasse, die einen Passagier repräsentiert
class Passagier:

    # Konstruktor, der dafür sorgt, dass Objekte dieser Klasse nur
    # unter Angabe von Vor- und Zunamen sowie Titel angelegt werden
    # können
    def __init__(self, firstname, lastname, title):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__title = title
        self.__checkIn = False

        # ist Passagier am Gate
        self.__atGate = False

    # Öffentliche Methode zum Durchführen des Check-ins
    def checkIn(self):
        self.__checkIn = True

    # Öffentliche Methode zur Prüfung, ob dieser Passagier bereits
    # eingecheckt ist
    def isCheckedIn(self):
        return self.__checkIn

    # Öffentliche Methode zum Setzen des Status: Passagier am Gate
    def onGate(self):
        self.__atGate = True

    # Öffentliche Methode zur Ermittlung, ob der Passagier am Gate ist
    def isAtGate(self):
        return self.__atGate

    # Öffentliche Methode zum Generieren eines aussagekräftigen
    # Strings zur Repräsentation des Passagiers
    def __str__(self):
        # Nur Titel ausgeben, wenn auch angegeben
        if self.__title == "":
            return self.__firstname + " " + self.__lastname
        else:
            output =  self.__title + " " + self.__firstname
            output += " " + self.__lastname
            return output


# Öffentliche Klasse, die einen Flug repräsentieren soll
class Flug:

    # Öffentlicher Konstruktor, der die Daten vorgibt, die für
    # die Erzeugung eines Objekts dieser Klasse notwendig sind
    def __init__(
            self,
            id,
            startAirport,
            endAirport,
            startTime,
            gate,
            passengers):
        self.__id = id
        self.__startAirport = startAirport
        self.__endAirport = endAirport
        self.__startTime = startTime
        self.__gate = gate
        self.__passengers = passengers

    # Öffentliche Methode, die einen Passagier aufruft, wenn
    # dieser nicht am Gate ist.
    def ausrufen(self):
        # Gehe Passagierliste durch
        for passenger in self.__passengers:
            # Wenn Passagier eingecheckt und noch
            # nicht am Gate
            if passenger.isCheckedIn() and passenger.isAtGate() == False:
                # ausrufen
                print "Last call for passenger " + str(passenger)


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

passagiere = [Passagier("Martin", "Krause", "Dr."),
              Passagier("Simone", "Krause", ""),
              Passagier("Herr", "Kules", ""),
              Passagier("Frau", "Kules", ""),
              Passagier("Kranke", "Person", "")]

# Checke alle Fluggäste außer Kranke Person ein
for i in range(0, len(passagiere)):
    passagiere[i].checkIn()
    # Außer den Krauses sind davon alle am Gate
    if i > 1:
        passagiere[i].onGate()

flug = Flug("MH123", "Köln-Bonn", "München", "9:10",
            "C12", passagiere)
flug.ausrufen()
