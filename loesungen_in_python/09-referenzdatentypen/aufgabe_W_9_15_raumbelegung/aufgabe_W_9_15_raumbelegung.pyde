class Room:
    # Konstruktor, der den Namen des Raumes, die Nummer und
    # Anzahl der Sitze erwartet
    def __init__(self, name, number, seats):
        self.__name = name
        self.__number = number
        self.__seats = seats

    def get_name(self):
        return self.__name

    def get_number(self):
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

    def get_room(self):
        return self.__room

    def get_from(self):
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
        last_room = Room("", "", -1)
        for occupancy in self.__occupancies:
            # Aktueller Raum
            current_room = occupancy.get_room()

            # Sollte der letzte Raum nicht identisch sein
            if last_room != current_room:
                # Gebe die Titelzeile für den neuen Raum aus
                output += str(current_room) + ":\n"

            # Gebe den Termin aus
            output += "* {}\n".format(occupancy)

            # Speichere Raum aus aktueller Iteration für
            # nächste Iteration
            last_room = current_room

        return output

    # Füge Eintrag hinzu, sortiert nach Raum
    def add_occupancy(self, room, reason, begin, to):
        # Erzeuge neue Raumbelegung basierend auf den Eingaben
        new_occupancy = Occupancy(room, reason, begin, to)

        # Erstelle neuen temporären Array, der um ein Element wachsen
        # wird
        occupancies_temp = []

        # Gehe Einträge durch
        for occupancy in self.__occupancies:
            # Raumnummer des neuen Eintrags
            number_new = new_occupancy.get_room().get_number()

            # Belegungsbeginn des neuen Eintrags
            from_new = new_occupancy.get_from()

            # Raumnummer des Eintrags an der aktuellen Position
            number_current = occupancy.get_room().get_number()

            # Belegungsbeginn des Eintrags an der aktuellen Position
            from_current = occupancy.get_from()

            # Wenn aktueller Eintrag alphabetisch größer oder gleich
            # dem hinzufügenden Eintrag ist
            if number_current >= number_new and from_current >= from_new:
                # Haben Stelle gefunden
                # Füge neuen Eintrag an dieser Stelle hinzu
                occupancies_temp.append(new_occupancy)

            # Füge aktuellen Eintrag an dieser Stelle hinzu
            occupancies_temp.append(occupancy)

        # Haben wir das neue Element immer noch nicht hinzugefügt,
        # da es an die letzte Stelle hinzugefügt werden muss,
        # fügen wir dieses noch hinzu
        if len(occupancies_temp) == len(self.__occupancies):
            occupancies_temp.append(new_occupancy)

        # Setze temporären Array als neuen Array der Liste
        self.__occupancies = occupancies_temp


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
    plan.add_occupancy(usabilitylab, "Studie zu Buchprojekt",
                       "2019-02-03", "2019-02-04")
    plan.add_occupancy(
        besprechungsraum,
        "Lagebesprechung zu den Programmieraufgaben",
        "2019-02-03",
        "2019-02-04")
    plan.add_occupancy(
        vorlesungssaal,
        "Vorlesung Informatik",
        "2019-02-03",
        "2019-02-04")
    plan.add_occupancy(
        usabilitylab,
        "Studie zu risikobasierter Authentifizierung",
        "2019-02-05",
        "2019-02-06")
    plan.add_occupancy(usabilitylab, "Testen der Programmieraufgaben",
                       "2019-02-04", "2019-02-05")

    # Gebe Belegungsplan aus
    print(plan)

# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
