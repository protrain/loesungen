class Room:
    # Konstruktor, der den Namen des Raumes, die Nummer und
    # Anzahl der Sitze erwartet
    def __init__(self, name, number, seats):
        self.__name = name
        self.__number = number
        self.__seats = seats

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def __str__(self):
        # Gebe Raum als String zurück. Die Zeichen {} stehen hierbei
        # für Platzhalter, welche mit dem .format-Kommando mit den
        # Variableninhalten gefüllt werden
        return "Raum {} ({}, {} Sitze)".format(
            self.__number, self.__name, self.__seats)


class Occupancy:
    # Konstruktor, der den Raum, den Grund zur Raumbelegung sowie das
    # Start- und Enddatum erwartet
    def __init__(self, room, reason, begin, to):
        self.__reason = reason
        self.__room = room
        self.__begin = begin
        self.__to = to

    def getRoom(self):
        return self.__room

    def getFrom(self):
        return self.__begin

    def __str__(self):
        return self.__begin + " - " + \
            self.__to + " (" + self.__reason + ")"


class RoomOccupancyPlan:
    # Konstruktor, der den Raumbelegungsplan initialisiert
    def __init__(self):
        # Initialisiere neue Belegungsliste
        self.__occupancies = []

    # Zeige den Belegungsplan an
    def __str__(self):
        output = ""

        # Der Raum aus der letzten Iteration
        lastRoom = Room("", "", -1)
        for occupancy in self.__occupancies:
            # Aktueller Raum
            currentRoom = occupancy.getRoom()

            # Sollte der letzte Raum nicht identisch sein
            if lastRoom != currentRoom:
                # Gebe die Titelzeile für den neuen Raum aus
                output += str(currentRoom) + ":\n"

            # Gebe den Termin aus
            output += "* {}\n".format(occupancy)

            # Speichere Raum aus aktueller Iteration für
            # nächste Iteration
            lastRoom = currentRoom

        return output

    # Füge Eintrag hinzu, sortiert nach Raum
    def addOccupancy(self, room, reason, begin, to):
        # Erzeuge neue Raumbelegung basierend auf den Eingaben
        newOccupancy = Occupancy(room, reason, begin, to)

        # Erstelle neuen temporären Array, der um ein Element wachsen
        # wird
        occupanciesTemp = []

        # Füge den ersten Listeneintrag ohne Schleife hinzu
        if len(occupanciesTemp) == 1:
            occupanciesTemp[pos] = occupancy

        else:
            # Gehe Einträge durch
            for occupancy in self.__occupancies:
                # Raumnummer des neuen Eintrags
                numberNew = newOccupancy.getRoom().getNumber()

                # Belegungsbeginn des neuen Eintrags
                fromNew = newOccupancy.getFrom()

                # Raumnummer des Eintrags an der aktuellen Position
                numberCurrent = occupancy.getRoom().getNumber()

                # Belegungsbeginn des Eintrags an der aktuellen Position
                fromCurrent = occupancy.getFrom()

                # Wenn aktueller Eintrag alphabetisch größer oder gleich
                # dem hinzufügenden Eintrag ist
                if numberCurrent >= numberNew and fromCurrent >= fromNew:
                    # Haben Stelle gefunden
                    # Füge neuen Eintrag an dieser Stelle hinzu
                    occupanciesTemp.append(newOccupancy)

                # Füge aktuellen Eintrag an dieser Stelle hinzu
                occupanciesTemp.append(occupancy)

            # Haben wir das neue Element immer noch nicht hinzugefügt,
            # da es an die letzte Stelle hinzugefügt werden muss,
            # fügen wir dieses noch hinzu
            if len(occupanciesTemp) == len(self.__occupancies):
                occupanciesTemp.append(newOccupancy)

        # Setze temporären Array als neuen Array der Liste
        self.__occupancies = occupanciesTemp


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Definiere Räume
    usabilitylab = Room("Usability Lab", "A-W42", 2)
    besprechungsraum = Room("Besprechungsraum", "A-C33", 10)
    vorlesungssaal = Room("Vorlesungssaal", "A-T44", 140)

    # Erstelle Raumbelegungsplan
    plan = RoomOccupancyPlan()

    # Füge Einträge hinzu
    plan.addOccupancy(usabilitylab, "Studie zu Buchprojekt",
                      "2019-02-03", "2019-02-04")
    plan.addOccupancy(
        besprechungsraum,
        "Lagebesprechung zu den Programmieraufgaben",
        "2019-02-03",
        "2019-02-04")
    plan.addOccupancy(
        vorlesungssaal,
        "Vorlesung Informatik",
        "2019-02-03",
        "2019-02-04")
    plan.addOccupancy(
        usabilitylab,
        "Studie zu risikobasierter Authentifizierung",
        "2019-02-05",
        "2019-02-06")
    plan.addOccupancy(usabilitylab, "Testen der Programmieraufgaben",
                      "2019-02-04", "2019-02-05")

    # Gebe Belegungsplan aus
    print plan
