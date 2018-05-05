class Room:
    """ Öffentliche Klasse zur Repräsentation eines Hotelzimmers """
    def __init__(self, number):
        """ Initialisierer, der vorschreibt, dass die Zimmer-
        nummer angegeben wird """
        self.number = number
        self.available = True

class Hotel:
    """ Öffentliche Klasse zur Zimmerverwaltung eines Hotels """
    def __init__(self, name, stars, rooms):
        """ Initialisierer, der den Hotelnamen, die
        Anzahl der Sterne sowie die Räume übergeben bekommt """
        self.rooms = rooms
        self.name = name
        self.stars = stars

    def check_in(self):
        """ Öffentliche Methode, die den Index des nächsten freien Raums
        zurückliefert """
        # Gehe Räume nacheinander durch
        for room in rooms:
            # Sobald ein Raum frei ist
            if room.available:
                # Raum belegen
                room.available = False
                # Aus der Funktion mit Nummer springen
                return room.number
        return None

    def check_out(self, number):
        """ Öffentliche Methode, die einen Checkout-Vorgang simuliert. Die
        Zimmernummer, für die der Checkout-Vorgang durchgeführt werden
        soll, wird an die Methode übergeben. """
        # Gehe Räume nacheinander durch
        for room in rooms:
            # Stimmt Raumnummer überein und ist Raum noch belegt
            if room.number == number and not room.available:
                # Aus Schleife springen
                room.available = True
                break


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

print hotel.check_in()
print hotel.check_in()
print hotel.check_in()
hotel.check_out(102)
print hotel.check_in()
print hotel.check_in()
