# Klasse zur Realisierung eines Highscore-Eintrags
class HighscoreEntry:

    # Konstruktor, der als Eingabewerte den Nickname und
    # die erreichten Punkte erwartet
    def __init__(self, nickname, points):
        self.__nickname = nickname
        self.__points = points

    # Öffentliche Methode zur Ausgabe eines Strings mit der
    # Angabe von Nickname und erreichter Punkte
    def __str__(self):
        return self.__nickname + " - " + str(self.__points) + " Punkte"


# Klasse zur Realisierung einer Highscore-Tabelle
class HighscoreTable:

    # Konstruktor der Klasse, der die Initialisierung vornimmt
    def __init__(self):
        # Lege leere Highscore-Liste mit 10 Platzierungen an
        self.__entries = []
        for i in range(0, 10):
            self.__entries.append(HighscoreEntry("Name" + str(i), 0))

    # Öffentliche Methode zum Hinzufügen eines neuen Eintrags in die
    # Highscore-Liste. Übergeben werden der Nickname, die erreichten
    # Punkte sowie die Position innerhalb der Liste.
    def add_entry(self, nickname, points, position):
        # Nutze die HighscoreEntry-Klasse
        entry = HighscoreEntry(nickname, points)

        # Gehe alte Liste bis zur Position durch
        entries_temp = []
        for i in range(0, position - 1):
            # Füge altes Element hinzu
            entries_temp.append(self.__entries[i])

        # Füge jetzt neues Element hinzu
        entries_temp.append(entry)

        # Gehe Rest der Liste durch
        for i in range(position - 1, len(self.__entries)):
            # Füge altes Element hinzu
            entries_temp.append(self.__entries[i])

        # Setze temporäre Liste als neue Liste
        self.__entries = entries_temp

    # Öffentliche Methode zur Ausgabe der Highscore-Liste
    def print_list(self):
        pos = 1
        for entry in self.__entries:
            print("Platz " + str(pos) + ": " + str(entry))
            pos += 1


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
hs = HighscoreTable()
hs.add_entry("Dieter", 666, 1)
hs.add_entry("Thomas", 12, 6)
hs.print_list()
