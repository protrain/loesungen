# Klasse, die einen Post repräsentiert
class Post:
    # Öffentlicher Konstruktor, der vorschreibt, dass ein
    # Post zwangsläufig aus einem Anmeldenamen und dem
    # textuellen Inhalt besteht.
    def __init__(self, username, text):
        self.__username = username

        # Beschneide Post auf 140 Zeichen,
        # wenn er zu groß ist
        if len(text) > 140:
            text = text[0:140]
        self.__text = text

    # Öffentliche Methode, die den Post in geeigneter
    # Weise zurückliefert
    def __str__(self):
        return self.__username + ": " + self.__text


# Öffentliche Klasse, die eine Twitterwall repräsentiert
class SocialWall:
    # Konstruktor, der die Anzahl maximal zu verwaltender
    # Posts erwartet
    def __init__(self, max_posts):
        self.__posts = []
        for i in range(0, max_posts):
            self.__posts.append(None)
            # nächste Schreibposition im Array
            self.next_post = 0

    # Öffentliche Methode zum Hinzufügen eines Posts
    def add_post(self, post):
        # Wenn kein Platz im Array
        if self.next_post >= len(self.__posts):
            # umkopieren nach vorne
            for i in range(0, len(self.__posts) - 1):
                self.__posts[i] = self.__posts[i + 1]

                # Letzter Eintrag = neuer Post
                self.next_post = len(self.__posts) - 1

        # Füge Post hinzu
        self.__posts[self.next_post] = post

        # Erhöhe Zähler
        self.next_post += 1

    # Öffentliche Methode, die alle Posts in Form
    # eines Post-Arrays in der Reihenfolge der Erzeugung
    # zurückliefert
    def get_posts(self):
        output = []
        # Gehe bis letzten Eintrag durch
        for post in self.__posts:
            # Kopiere Einträge
            output.append(post)

        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

tw = SocialWall(2)

long_text = "Dies ist ein Post, der so viel Text enthält, dass er "
long_text += "über die erlaubten 140 Zeichen hinausragen wird. "
long_text += "Ehrlich wahr, so sollte es sein. #toomuchtext"
tw.add_post(Post("Bot1", long_text))
tw.add_post(Post("Bot2", "Auch Hallo"))
tw.add_post(Post("Bot3", "Wie geht's?"))

# Gebe alle Posts der Twitterwall untereinander aus.
for current_post in tw.get_posts():
    print(current_post)
