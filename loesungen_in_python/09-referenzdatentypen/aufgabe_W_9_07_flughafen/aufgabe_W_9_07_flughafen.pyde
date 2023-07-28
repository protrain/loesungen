# Öffentliche Klasse, die einen ReisendePerson repräsentiert
class ReisendePerson:

    # Konstruktor, der dafür sorgt, dass Objekte dieser Klasse nur
    # unter Angabe von Vor- und Zunamen sowie Titel angelegt werden
    # können
    def __init__(self, first_name, last_name, title):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__check_in = False

        # ist ReisendePerson am Gate
        self.__at_gate = False

    # Öffentliche Methode zum Durchführen des Check-ins
    def check_in(self):
        self.__check_in = True

    # Öffentliche Methode zur Prüfung, ob ReisendePerson bereits
    # eingecheckt ist
    def is_checked_in(self):
        return self.__check_in

    # Öffentliche Methode zum Setzen des Status: ReisendePerson am Gate
    def on_gate(self):
        self.__at_gate = True

    # Öffentliche Methode zur Ermittlung, ob ReisendePerson am Gate ist
    def is_at_gate(self):
        return self.__at_gate

    # Öffentliche Methode zum Generieren eines aussagekräftigen
    # Strings zur Repräsentation der reisenden Person
    def __str__(self):
        # Nur Titel ausgeben, wenn auch angegeben
        if self.__title == "":
            return self.__first_name + " " + self.__last_name
        else:
            output = self.__title + " " + self.__first_name
            output += " " + self.__last_name
            return output


# Öffentliche Klasse, die einen Flug repräsentieren soll
class Flug:

    # Öffentlicher Konstruktor, der die Daten vorgibt, die für
    # die Erzeugung eines Objekts dieser Klasse notwendig sind
    def __init__(
            self,
            flug_id,
            start_airport,
            end_airport,
            start_time,
            gate,
            passengers):
        self.__id = flug_id
        self.__start_airport = start_airport
        self.__end_airport = end_airport
        self.__start_time = start_time
        self.__gate = gate
        self.__passengers = passengers

    # Öffentliche Methode, die eine reisende Person aufruft, wenn
    # diese nicht am Gate ist.
    def ausrufen(self):
        # Gehe ReisendePersonliste durch
        for passenger in self.__passengers:
            # Wenn ReisendePerson eingecheckt und noch
            # nicht am Gate
            if passenger.is_checked_in() and passenger.is_at_gate() is False:
                # ausrufen
                print("Last call for passenger " + str(passenger))


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

reisende = [ReisendePerson("Martin", "Krause", "Dr."),
              ReisendePerson("Simone", "Krause", ""),
              ReisendePerson("Herr", "Kules", ""),
              ReisendePerson("Frau", "Kules", ""),
              ReisendePerson("Kranke", "Person", "")]

# Checke alle Fluggäste außer Kranke Person ein
for i in range(0, len(reisende)):
    reisende[i].check_in()
    # Außer den Krauses sind davon alle am Gate
    if i > 1:
        reisende[i].on_gate()

flug = Flug("MH123", "Köln-Bonn", "München", "9:10",
            "C12", reisende)
flug.ausrufen()
