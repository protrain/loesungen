# Öffentliche Klasse, die einen einzelnen Song repräsentiert
class Song:

    # Konstruktor, der die Angabe des Titelnamens
    # sowie eine Dauer erwartet
    def __init__(self, title, duration):
        self.__title = title
        self.__duration = duration

    # Öffentliche Methode, die den Titel mit der
    # Angabe der Dauer als String zurückliefert
    def __str__(self):
        return self.__title + " -- " + self.__duration


# Öffentliche Klasse für ein Musikalbum
class Album:

    # Konstruktor, der die Angabe des Künstlers,
    # das Land sowie den Albumtitel und die einzelnen
    # Songs erwartet
    def __init__(self, artist, country, album, songs):
        self.__artist = artist
        self.__country = country
        self.__album = album
        self.__songs = songs

    # Öffentliche Methode, die ein komplettes Album
    # mit allen nötigen Informationen zurückliefert
    def __str__(self):
        # Generiere Ausgabe
        output = "Künstler: " + self.__artist + "\n"
        output += "Land: " + self.__country + "\n"
        output += "Album: " + self.__album + "\n"
        output += "---------------------\n"

        # Gehe jeden Song durch
        tracknumber = 1  # Tracknummer
        for song in self.__songs:
            output += str(tracknumber) + ". " + str(song) + "\n"

            # Erhöhe Tracknummer um 1
            tracknumber += 1

        return output


# Öffentliche Klasse zur Verwaltung eines Music Store
class MusicStore:

    # Standardkonstruktor, der die Initialisierung
    # des Album-Arrays übernimmt.
    def __init__(self):
        self.__albums = []

    # Methode zum Hinzufügen eines Albums
    def addAlbum(self, album):
        self.__albums += [album]

    # Öffentliche Methode zur Ausgabe aller Alben
    # auf der Konsole
    def printAll(self):
        for album in self.__albums:
            print album


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

# Erstelle Album-Song-Array
fanta4Songs = [Song("Und Täglich Grüßen Fanta Vier / Romantic Fighters",
                    "1:23"),
               Song("30 Mark", "0:42"),
               Song("MfG", "3:35"),
               Song("Hammer", "4:59"),
               Song("Die Stadt Die Es Nicht Gibt", "4:29"),
               Song("0:29", "0:30"),
               Song("Alles Schon Gesehen", "4:25"),
               Song("Michi Beck In Hell", "5:12"),
               Song("Home Again", "0:44")]

# Erstelle Album
fanta4 = Album("Die Fantastischen Vier", "Deutschland", "4:99",
               fanta4Songs)

# Erstelle Album-Song-Array
astleySongs = [Song("Never Gonna Give You Up", "3:36"),
               Song("Whenever You Need Somebody", "3:56"),
               Song("Together Forever", "3:29"),
               Song("It Would Take A Strong Strong Man", "3:44"),
               Song("The Love Has Gone", "4:20"),
               Song("Don't Say Goodbye", "4:11"),
               Song("Slipping Away", "3:56"),
               Song("No More Looking For Love", "3:15"),
               Song("You Move Me", "3:45"),
               Song("When I Fall In Love", "3:03")]

# Erstelle Album
astley = Album("Rick Astley", "England", "Whenever You Need Somebody",
               astleySongs)

# Erstelle MusicStore und füge Alben hinzu
ms = MusicStore()
ms.addAlbum(fanta4)
ms.addAlbum(astley)

# Gebe kompletten Music-Store aus
ms.printAll()
