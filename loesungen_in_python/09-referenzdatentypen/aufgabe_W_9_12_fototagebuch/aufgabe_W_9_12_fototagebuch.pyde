# Import von Bibliotheksfunktionen für den Umgang
# mit dem Datum
import datetime

# Öffentliche Klasse, die ein Foto repräsentiert
class Photo:
    # Konstruktor, der vorschreibt, dass ein Foto
    # einen Namen haben muss
    def __init__(self, name):
        self.__name = name

    # Öffentliche Methode zum Generieren einer
    # geeigneten String-basierten Ausgabe.
    def __str__(self):
        return self.__name


# Öffentliche Hilfsklasse, die eine statische Methode
# enthält
class DateUtils:
    import datetime

    # Methode zur Überprüfung auf Gleichheit eines Tags
    @staticmethod
    def isSameDay(a, b):
        # Stimmen Tag, Jahr und Monat überein, ist es der gleiche Tag
        if a.year == b.year and a.month == b.month and a.year == b.year:
            return True
        else:
            return False


# Öffentliche Klasse, die ein Fototagebuch repräsentiert
class PhotoDiary:
    import datetime

    def __init__(self):
        self.__photos = []
        self.__dates = []

    # Erzeuge um ein Element größeres Array
    def addPhoto(self, p):
        # Setze letztes Photo mit neuem Foto
        self.__photos.append(p)

        # Setze letztes Datum mit aktueller Zeit
        self.__dates.append(datetime.date.today())

    # Öffentliche Methode, die alle Fotos eines Tages zurückliefert
    def getPhotosByDay(self, day):
        count = 0
        for date in self.__dates:
            if(DateUtils.isSameDay(date, day)):
                count += 1

        if count > 0:
            tPhotos = []
            i = 0

            # Alle Datumsangaben durchgehen
            for date in self.__dates:
                # Wenn Tag übereinstimmt
                if DateUtils.isSameDay(date, day):
                    # Foto anfügen
                    tPhotos.append(self.__photos[i])

                # immer Fotozähler erhöhen, damit richtiges
                # Foto hinzugefügt wird
                i += 1
            return tPhotos
        else:
            return None


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

pd = PhotoDiary()
pd.addPhoto(Photo("Foto 1"))
pd.addPhoto(Photo("Foto 2"))

# Heutiges Datum
today = datetime.date.today()

# Hole Fotos
photos = pd.getPhotosByDay(today)

# Gebe jedes Foto aus
for photo in photos:
    print photo
