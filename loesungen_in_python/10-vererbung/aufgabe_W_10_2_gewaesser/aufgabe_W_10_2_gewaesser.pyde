# Import spezieller Python-Funktionalitäten, damit Abstrakte Methoden
# definiert werden können
from abc import ABCMeta, abstractmethod

# Öffentliche, abstrakte Klasse zur Basisimplementierung eines
# Gewässers. Die Klasse ist nicht instanziierbar; es können also
# keine Objekte dieser Klasse direkt erzeugt werden.
class Gewaesser(object):

    # Definiere diese Klasse als abstrakte Klasse. Danach können
    # wir abstrakte Funktionen in dieser Klasse definieren (mit
    # @abstractclass).
    __metaclass__ = ABCMeta

    # Öffentlicher Konstruktor, der die Angabe des Namens,
    # der Schiffbarkeit sowie der Schadstoffbelastung erfordert
    @abstractmethod
    def __init__(self, name, schiffbar, schadstoffbelastung):
        self.__name = name
        self.__schiffbar = schiffbar
        self.__schadstoffbelastung = schadstoffbelastung

    # Getter-Methode zum Abfragen, in welches andere Gewässer
    # dieses mündet. Diese Methode wird in ableitenden Klassen
    # überschrieben.
    def getMuendetIn(self):
        return None

    # Getter-Methode zur Rückgabe des Gewässernamens
    def getName(self):
        return self.__name

    # Öffentliche Methode zum Generieren eines repräsentativen
    # Strings
    def __str__(self):
        return self.__name


# Öffentliche Klasse, die ein Meer repräsentiert und dazu von
# der abstrakten Klasse Gewässer ableitet.
class Meer(Gewaesser):

    # Konstruktor, der Name, Schadstoffbelastung sowie Fläche
    # einfordert
    def __init__(self, name, schadstoffbelastung, flaeche):
        # und damit den Konstruktor der Basisklasse (Gewaesser) aufruft.
        # Da ein Meer immer schiffbar ist, wird beim Aufruf des Basis-
        # klassenkonstruktors für schiffbar direkt der Wert 'True'
        # gesetzt
        Gewaesser.__init__(self, name, True, schadstoffbelastung)

        # und zusätzlich noch die Fläche in der selbst erzeugten
        # Variablen gespeichert. Denn die Basisklasse hat hierfür keine
        # Variable vorgesehen.
        self.__flaeche = flaeche


# Klasse, die einen Fluss repräsentiert und von der Klasse Gewaesser
# ableitet.
class Fluss(Gewaesser):

    # Öffentlicher Konstruktor, der die benötigten Werte
    # entgegennimmt. Ein Fluss mündet in ein anderes
    # Gewässer und wird zusätzlich verlangt.
    def __init__(self, name, schiffbar, schadstoffbelastung,
                 laenge, muendetIn):
        # Aufruf und Übergabe der Werte an den Konstruktor der
        # Basisklasse Gewaesser
        Gewaesser.__init__(self, name, schiffbar,
                           schadstoffbelastung)

        # Speichern der zusätzlichen Parameter, die für einen
        # Fluss charakteristisch sind.
        self.__laenge = laenge
        self.__muendetIn = muendetIn

    # Öffentliche Methode, um das nächste erreichbare Meer
    # zu bestimmen.
    def bestimmeMeer(self):
        # Gehe ins nächste Gewässer
        gewaesser = self.__muendetIn

        # Solange wir noch weitere Gewässer haben
        while gewaesser.getMuendetIn() is not None:
            # Gehe Gewässerkette solange durch, bis wir auf Meer stoßen
            # (also kein muendetIn mehr vorhanden ist)
            gewaesser = gewaesser.getMuendetIn()

        return gewaesser

    # Überschreiben der Basisklassenmethode, die
    # hier aber einen konkreten Wert zurückliefert
    def getMuendetIn(self):
        return self.__muendetIn

    # Öffentliche Methode zur Repräsentation eines Flusses
    def __str__(self):
        output = self.getName() + ", mündet in "
        output += self.getMuendetIn().getName()
        output += ", endet in " + str(self.bestimmeMeer())
        return output


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

nordsee = Meer("Nordsee", 12.2, 842000)
elbe = Fluss("Elbe", True, 12.3, 1094, nordsee)
moldau = Fluss("Moldau", True, 12.3, 430, elbe)
berounka = Fluss("Berounka", False, 12.3, 138, moldau)
havel = Fluss("Havel", True, 12.3, 334, elbe)

print berounka
print moldau
print havel
