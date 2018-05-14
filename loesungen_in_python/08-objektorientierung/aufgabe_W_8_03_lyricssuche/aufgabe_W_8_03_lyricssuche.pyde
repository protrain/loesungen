from urllib import urlencode

# Statische Klasse, die nur aus statischen Methoden besteht
class Lyrics:
    @staticmethod
    def get_lyrics_url(artist, title):
        """ Statische Methode, die die URL zu einem Songtext aufbaut.
        Als Eingabewerte werden Musiker und Titel an die Methode
        übergeben. Als Ergebnis wird der generierte URL zurückgegeben
        """
        # Konvertiere artist und title in Kleinschreibung
        # und ersetze Leerzeichen mit Unterstrich
        params = {
            'func': 'getSong',
            'artist': artist.lower().replace(' ', '_'),
            'song': title.lower().replace(' ', '_'),
        }

        # Baue URL
        return "http://lyrics.wikia.com/api.php?%s" % urlencode(params)


# Startpunkt des Hauptprogramms
# Zu Demonstrations- und Testzwecken wird die oben programmierte
# statische Klassenmethode verwendet.

# Lese Interpret und Titel ein
interpret = "Die Fantastischen Vier"
titel = "MFG"

print Lyrics.getLyricsURL(interpret, titel)



