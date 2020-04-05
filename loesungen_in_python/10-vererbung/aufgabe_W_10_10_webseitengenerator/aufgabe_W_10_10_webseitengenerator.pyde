# Import spezieller Python-Funktionalitäten, damit Abstrakte Methoden
# definiert werden können
from abc import ABCMeta, abstractmethod

# Konstanten, mit denen wir die Wetterlage beschreiben
SONNE = 0,
BEWOELKT = 1
REGEN = 2

# Abstrakte Klasse zur Repräsentation einer Stadt.
# Von dieser Klasse kann keine Instanz (= Objekt) erzeugt werden.


class Stadt:
    # Definiere diese Klasse als abstrakte Klasse. Danach können
    # wir abstrakte Funktionen in dieser Klasse definieren (mit
    # @abstractclass).
    __metaclass__ = ABCMeta

    # Konstruktor, der zur Angabe eines Städtenamens und des
    # Wetters auffordert
    @abstractmethod
    def __init__(self, name, wetter):
        self.__name = name
        self.__wetter = wetter

    # Getter-Methode zur Rückgabe des Städtenamens
    def getName(self):
        return self.__name

    # Getter-Methode zur Rückgabe des Wetters als String
    def __getWetter(self):
        if self.__wetter == REGEN:
            return "regnerisch"
        elif self.__wetter == BEWOELKT:
            return "bewölkt"
        elif self.__wetter == SONNE:
            return "sonnig"

        # Unbekannter Wert
        return "Unbekannt"

    # Getter-Methode zur Rückgabe des Webseiten-Inhalts
    # für den Webseiten-Generator.
    def getContent(self):
        print "Stadt"
        output = "<p>In " + self.getName() + " ist es "
        output += self.__getWetter() + ".</p>"
        return output

    # Getter-Methode zur Rückgabe der URL zur Wetterseite
    def getURL(self):
        # Wandle Namen in Kleinbuchstaben um
        name = self.getName().lower()

        # Wandle Leerzeichen im Namen in Bindestriche um
        name = name.replace(" ", "-")

        # Wandle Umlaute um
        name = name.replace("ä", "ae")
        name = name.replace("ü", "ue")
        name = name.replace("ö", "oe")

        # Gebe umgewandelte URL zurück
        return name + ".html"


# Öffentliche Klasse für die Großstadt leitet
# von der Klasse Stadt ab.
class Grossstadt(Stadt):
    # Konstruktor erwartet ebenfalls einen Städtenamen und das
    # Wetter, aber zusätzlich noch Stadtteile
    def __init__(self, name, wetter, stadtteile):
        # Städtename und Wetter werden an die Basisklasse
        # übergeben
        Stadt.__init__(self, name, wetter)

        # Stadtteile werden noch gesetzt
        self.__stadtteile = stadtteile

    # Getter-Methode zur Rückgabe des Webseiten-Inhalts
    # für den Webseiten-Generator
    def getContent(self):
        # Hier speichern wir unsere Webseite als HTML-Code.
        # Wir übernehmen zunächst den Code von der Überklasse.
        output = Stadt.getContent(self)

        stadtteile = ""
        # Gehe die Stadtteile durch
        for i in range(0, len(self.__stadtteile)):
            if (i == (len(self.__stadtteile) - 1)):
                # Wir sind beim letzten Eintrag:
                # Füge "und" vor dem Stadtteilnamen hinzu
                stadtteile += " und "

            # Füge Namen des Stadtteils hinzu
            stadtteile += self.__stadtteile[i]

            # Wenn wir noch nicht am Ende sind
            if (i < (len(self.__stadtteile) - 2)):
                # Füge Komma und Leerzeichen hinzu
                stadtteile += ", "

        # Füge den Hinweis zu den Stadtteilen hinzu
        output += "<p>Dies trifft auch für die Stadtteile "
        output += stadtteile + " zu.</p>"

        # Gebe generierten HTML-Code zurück
        return output

    # Getter-Methode zur Rückgabe der URL zur Wetterseite
    def getURL(self):
        # Generiere URL und gebe sie zurück.
        # Rufe dabei die URL-Generierungsmethode aus der
        # Oberklasse auf.
        url = super(Grossstadt, self).getURL()
        return "wetter_grossstadt_{}".format(url)


# Öffentliche Klasse für die Großstadt leitet
# von der Klasse Stadt ab.
class Kleinstadt(Stadt):
    # Konstruktor erwartet ebenfalls einen Städtenamen und das
    # Wetter
    def __init__(self, name, wetter):
        # Städtename und Wetter werden an die Basisklasse
        # übergeben
        Stadt.__init__(self, name, wetter)

    # Getter-Methode zur Rückgabe des Webseiten-Inhalts
    # für den Webseiten-Generator
    def getContent(self):
        return Stadt.getContent(self)

    # Getter-Methode zur Rückgabe der URL zur Wetterseite
    def getURL(self):
        # Generiere URL und gebe sie zurück.
        # Rufe dabei die URL-Generierungsmethode aus der
        # Oberklasse auf.
        url = super(Kleinstadt, self).getURL()
        return "wetter_kleinstadt_{}".format(url)


# Öffentliche Klasse für den Webseitengenerator
class WebseitenGenerator:
    # Anzahl der Einträge im Array
    numEntries = 0

    def __init__(self):
        self.__staedte = []

    # Methode zum Hinzufügen einer Stadt
    def addStadt(self, stadt):
        # Füge den neuen Eintrag an der letzten Position hinzu
        self.__staedte.append(stadt)

    # Methode zum Erstellen und Ausgeben der Navigationsleiste
    # unserer Wetterwebseite
    def getNavigation(self):
        # Hier speichern wir unsere Navigationsleiste als HTML-Code.
        # Wir beginnen mit dem Paragrafen-HTML-Tag
        output = "<h1>Die Wetter-Webseite</h1><p>"

        # Gehe alle Städte durch
        for i in range(0, len(self.__staedte)):
            # Hole die URL zur Datei
            url = self.__staedte[i].getURL()

            # Hole den Städtenamen
            name = self.__staedte[i].getName()

            # Füge HTML-Link zur Ausgabe hinzu
            output += "<a href='" + url + "'>" + name + "</a>"

            # Füge Trenner hinzu, wenn wir noch nicht am Ende der
            # Liste sind
            if i < (len(self.__staedte) - 1):
                output += " | "

        # Schließe den Paragrafen-Tag
        output += "</p>"

        # Gebe generierte Navigationsleiste zurück
        return output

    # Methode zum Erstellen und Ausgeben der HTML-Seite
    # für eine bestimmte Stadt
    def generatePage(self, index):
        # Hole die Stadt aus dem Array
        stadt = self.__staedte[index]

        # Hier speichern wir unsere Webseite als HTML-Code
        # Setze HTML-Kopf
        output = "<html><body>"

        # Füge Navigationsleiste hinzu
        output += self.getNavigation()

        # Füge Überschrift hinzu
        output += "<h2>Das Wetter für " + stadt.getName() + "</h2>"

        output += stadt.getContent()

        # Füge HTML-Fußzeile hinzu
        output += "</body></html>"

        # Gebe HTML-Code zurück
        return output

    # Methode zum Erstellen und Ausgeben der Wetterwebseite
    # mit allen Webseiten
    def generateWebsites(self):
        # Generiere Index-Dokument
        # Öffne Datei für die Hauptseite
        output = createWriter("index.html")

        # Generiere HTML-Code für Datei, in der Hauptseite nehmen
        # wir nur die Navigationsleiste
        htmlCode = self.getNavigation()

        # Speichere HTML-Code in Datei
        output.print(htmlCode)

        # Schließe Datei
        output.close()

        # Gehe alle Städte durch
        for i in range(0, len(self.__staedte)):
            # Öffne Datei mit URL-Dateinamen
            output = createWriter(self.__staedte[i].getURL())

            # Generiere HTML-Code für Datei
            htmlCode = self.generatePage(i)

            # Speichere HTML-Code in Datei
            output.print(htmlCode)

            # Schließe Datei
            output.close()

        println("Webseiten generiert")


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Definiere Köln
    stadtteileKoeln = ["Ehrenfeld", "Raderthal", "Nippes",
                       "Poll", "Esch", "Pesch", "Kalk"]
    koeln = Grossstadt("Köln", SONNE, stadtteileKoeln)

    # Definiere Daaden
    daaden = Kleinstadt("Daaden", BEWOELKT)

    # Definiere Bonn
    stadtteileBonn = ["Poppelsdorf", "Südstadt", "Beuel",
                      "Duisdorf", "Graurheindorf"]
    bonn = Grossstadt("Bonn", REGEN, stadtteileBonn)

    # Initialisiere den Webseitengenerator
    generator = WebseitenGenerator()

    # Füge die Städte hinzu
    generator.addStadt(koeln)
    generator.addStadt(daaden)
    generator.addStadt(bonn)

    # Generiere die Webseiten
    generator.generateWebsites()
