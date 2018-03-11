# Klasse, die einen Tweet repräsentiert
class Tweet:
    # Öffentlicher Konstruktor, der vorschreibt, dass ein
    # Tweet zwangsläufig aus einem Benutzernamen und dem
    # textuellen Inhalt besteht.
    def __init__(self, username, text):
        self.__username = username

        # Beschneide Tweet auf 140 Zeichen,
        # wenn er zu groß ist
        if len(text) > 140:
            text = text[0:140]
        self.__text = text

    # Öffentliche Methode, die den Tweet in geeigneter
    # Weise zurückliefert
    def __str__(self):
        return self.__username + ": " + self.__text


# Öffentliche Klasse, die eine Twitterwall repräsentiert
class TwitterWall:
    # Konstruktor, der die Anzahl maximal zu verwaltender
    # Tweets erwartet
    def __init__(self, maxTweets):
        self.__tweets = []
        for i in range(0, maxTweets):
            self.__tweets.append(None)
            # nächste Schreibposition im Array
            self.__nextTweet = 0

    # Öffentliche Methode zum Hinzufügen eines Tweets
    def addTweet(self, tweet):
        # Wenn kein Platz im Array
        if self.__nextTweet >= len(self.__tweets):
            # umkopieren nach vorne
            for i in range(0, len(self.__tweets) - 1):
                self.__tweets[i] = self.__tweets[i + 1]

                # Letzter Eintrag = neuer Tweet
                self.__nextTweet = len(self.__tweets) - 1

        # Füge Tweet hinzu
        self.__tweets[self.__nextTweet] = tweet

        # Erhöhe Zähler
        self.__nextTweet += 1

    # Öffentliche Methode, die alle Tweets in Form
    # eines Tweet-Arrays in der Reihenfolge der Erzeugung
    # zurückliefert
    def getTweets(self):
        output = []
        # Gehe bis letzten Eintrag durch
        for tweet in self.__tweets:
            # Kopiere Einträge
            output.append(tweet)

        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

tw = TwitterWall(2)

longText = "Dies ist ein Tweet, der so viel Text enthält, dass er "
longText += "über die erlaubten 140 Zeichen hinausragen wird. "
longText += "Ehrlich wahr, so sollte es sein. #toomuchtext"
tw.addTweet(Tweet("Bot1", longText))
tw.addTweet(Tweet("Bot2", "Auch Hallo"))
tw.addTweet(Tweet("Bot3", "Wie geht's?"))

# Gebe alle Tweets der Twitterwall untereinander aus.
for tweet in tw.getTweets():
    print tweet
