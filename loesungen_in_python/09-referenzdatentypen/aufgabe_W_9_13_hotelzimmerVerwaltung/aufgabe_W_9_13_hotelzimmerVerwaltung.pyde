# Öffentliche Klasse zur Repräsentation eines Hotelzimmers
class Room:
    # Konstruktor, der vorschreibt, dass die Zimmer-
    # nummer angegeben wird
    def __init__(self, number):
        self.__number = number
        self.__available = True

    # Öffentliche Methode zur Prüfung, ob das Zimmer
    # noch frei ist.
    def is_available(self):
        return self.__available

    # Öffentliche Methode um den Status der Zimmer-
    # belegung zu ändern. Der zu setzende Status
    # wird der Methode übergeben.
    def set_is_available(self, available):
        self.__available = available

    # Methode, die die Zimmernummer zurückliefert.
    def get_number(self):
        return self.__number


# Öffentliche Klasse zur Zimmerverwaltung eines Hotels
class Hotel:
    # Öffentlicher Konstruktor, der den Hotelnamen, die
    # Anzahl der Sterne sowie die Räume übergeben bekommt
    def __init__(self, name, stars, rooms_list):
        self.__rooms = rooms_list
        self.__name = name
        self.__stars = stars

    # Öffentliche Methode, die den Index des nächsten freien Raums
    # zurückliefert
    def check_in(self):
        # Gehe Räume nacheinander durch
        for room in self.__rooms:
            # Sobald ein Raum frei ist
            if room.is_available():
                # Raum belegen
                room.set_is_available(False)
                # Aus der Funktion mit Nummer springen
                return room.get_number()
        return 0

    # Öffentliche Methode, die einen Checkout-Vorgang simuliert. Die
    # Zimmernummer, für die der Checkout-Vorgang durchgeführt werden
    # soll, wird an die Methode übergeben.
    def check_out(self, number):
        # Zähler außerhalb von for-Schleife definieren,
        # da wir sie danach noch brauchen könnten
        i = 0

        # Gehe Räume nacheinander durch
        for room in rooms:
            # Stimmt Raumnummer überein und ist Raum noch belegt
            if room.get_number() == number and room.is_available() is False:
                # Aus Schleife springen
                break
            # Zähler erhöhen
            i += 1

        # Sollten wir vor Array-Ende aus Schleife
        # gesprungen sein (= Raum gefunden + belegt),
        # dann Raum auf verfügbar stellen
        if i < len(rooms):
            rooms[i].set_is_available(True)


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

rooms = []

rooms.append(Room(101))
rooms.append(Room(102))
rooms.append(Room(103))
rooms.append(Room(201))
rooms.append(Room(202))
rooms.append(Room(203))
rooms.append(Room(301))
rooms.append(Room(302))
rooms.append(Room(303))

hotel = Hotel("Seeblick", 4, rooms)

print(hotel.check_in())
print(hotel.check_in())
print(hotel.check_in())
hotel.check_out(102)
print(hotel.check_in())
print(hotel.check_in())
