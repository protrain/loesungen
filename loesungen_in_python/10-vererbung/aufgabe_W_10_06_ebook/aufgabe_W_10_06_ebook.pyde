# Öffentliche Klasse zur Repräsentation eines E-Books
class Ebook:

    # Öffentlicher Konstruktor, der zur Angabe von
    # Autor und Jahreszahl verpflichtet
    def __init__(self, author, year):
        self.__assets = []
        for i in range(0, 100):
            self.__assets.append(None)

        self.__author = author
        self.__year = year

    # Getter-Methode zur Rückgabe der Seitenanzahl
    def numPages(self):
        sum = 0.0

        # Gehe Assets-Array durch
        for asset in self.__assets:
            # Ist Eintrag in Array vorhanden, dann Summe errechnen
            if asset is not None:
                sum += asset.numPages()

        return round(sum)

    # Methode, über die ein MediaAsset hinzugefügt werden kann
    # Das Asset muss an die Methode übergeben werden.
    def addAsset(self, asset):
        # Gehe Assets-Array durch
        for i in range(0, len(self.__assets)):
            # Ist kein Eintrag in Array vorhanden, dann einmal hinzufügen
            if self.__assets[i] is None:
                self.__assets[i] = asset

                # Springe aus Schleife
                break

    # Methode, die eine String-Repräsentation dieses
    # E-Books zurückliefert.
    def __str__(self):
        output = "Ebook: " + self.__author + \
            " (" + str(self.__year) + ")\n"
        output += "Seiten: " + str(self.numPages()) + "\n"
        output += "-------\n"

        # Gehe Array-Inhalte durch
        for asset in self.__assets:
            # Füge toString-Ausgabe hinzu
            if asset is not None:
                output += str(asset)

        return output


# Klasse zur Beschreibung eines MediaAssets
class MediaAsset(object):

    # Konstruktor, der zur Angabe diverser Informationen verpflichtet
    def __init__(self, file, size, language):
        self.__file = file
        self.__size = size
        self.__language = language

    # Methode zur Rückgabe der Seitenanzahl ist hierbei nicht möglich
    def numPages(self):
        # Ein undefiniertes Asset trägt nicht zur Seitenzahl bei.
        return 0.0

    # Methode zur Repräsentation des Assets
    def __str__(self):
        return self.__file + " (" + str(self.numPages()) + " Seiten)\n"


# Öffentliche Klasse zur Repräsentation eines TextAssets, die
# von der Klasse MediaAsset ableitet.
class TextAsset(MediaAsset):

    # Konstruktor, der zur Angabe von Werten für Dateinamen, -größe,
    # Sprache sowie Anzahl an Zeichen verpflichtet
    def __init__(self, file, size, language, numChars):
        # Aufruf der Basisklasse und Übergabe der Werte
        MediaAsset.__init__(self, file, size, language)

        # Spezifische Werte werden lokal gespeichert.
        self.__numChars = numChars

    # Methode zur Abfrage der Anzahl an Seiten
    def numPages(self):
        return self.__numChars / 2000.0


# Öffentliche Klasse zur Repräsentation eines PictureAssets, die
# von der Klasse MediaAsset ableitet.
class PictureAsset(MediaAsset):

    # Öffentlicher Konstruktor, der zur Angabe der folgenden Werte
    # verpflichtet
    def __init__(self, file, size, language, w, h):
        # Aufruf und Übergabe der von der Basisklasse verwalteten Werte
        MediaAsset.__init__(self, file, size, language)

        # Übrige Werte werden lokal festgehalten.
        self.__w = w
        self.__h = h

    # Methode zur Berechnung und Rückgabe der Anzahl von Seiten
    def numPages(self):
        height = self.__h * (960 / float(self.__w))
        if height > 600:
            return 1.0
        else:
            return 0.5


# Öffentliche Klasse zur Repräsentation eines PictureAssets, die
# von der Klasse MediaAsset ableitet
class AudioAsset(MediaAsset):

    # Öffentlicher Konstruktor, der zur Angabe der folgenden Werte
    # verpflichtet
    def __init__(self, file, size, language, duration):
        # Aufruf und Übergabe der von der Basisklasse verwalteten Werte
        MediaAsset.__init__(self, file, size, language)

        # Übrige Werte werden lokal festgehalten.
        self.__duration = duration

    # Methode zur Berechnung und Rückgabe der Anzahl von Seiten
    def numPages(self):
        return 0.0


# Öffentliche Klasse zur Repräsentation eines VideoAssets, die
# von der Klasse MediaAsset ableitet
class VideoAsset(MediaAsset):

    # Konstruktor, der zur Angabe der folgenden Werte verpflichtet
    def __init__(self, file, size, language, duration,
                 w, h):
        # Aufruf und Übergabe der von der Basisklasse verwalteten Werte
        MediaAsset.__init__(self, file, size, language)

        # Übrige Werte werden lokal festgehalten.
        self.__duration = duration
        self.__w = w
        self.__h = h

    # Methode zur Berechnung und Rückgabe der Anzahl von Seiten
    def numPages(self):
        height = self.__h * (960 / float(self.__w))
        if height > 600:
            return 1.0
        else:
            return 0.5


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

testBook = Ebook("Stephan Wiefling", 2017)
testBook.addAsset(TextAsset("Aufgabe 1", 12, "Deutsch", 3444))
testBook.addAsset(AudioAsset("Audio 1", 12, "Deutsch", 95))
testBook.addAsset(VideoAsset("Video 1", 12, "Deutsch", 95, 800, 800))
testBook.addAsset(PictureAsset("Bild 1", 12, "Deutsch", 2000, 600))
testBook.addAsset(TextAsset("Aufgabe 2", 12, "Deutsch", 7655))
print testBook
