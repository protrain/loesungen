# Klasse zur Repräsentation eines Meeting-Protokolls
class MeetingMinutes:

    # Konstruktor, der die benötigten Daten per
    # Vorschrift beim Anlegen eines neuen Objekts
    # erforderlich macht
    def __init__(self, date, timeframe,
                 room, participants):
        self.__date = date
        self.__timeframe = timeframe
        self.__room = room
        self.__participants = participants

        # Leere Liste erzeugen
        self.__items = []

    # Methode zum Hinzufügen eines Item-Objekts
    def add(self, item):
        self.__items.append(item)

    # Methode zur Repräsentation eines Meetings
    def __str__(self):
        output = "Meeting: " + self.__date + \
            " (" + self.__timeframe + "), "
        output += self.__room + "\nParticipants: "

        # Gehe Teilnehmerliste durch
        for i in range(0, len(self.__participants)):
            output += self.__participants[i]

            # Komma bis zum letzten Element setzen
            if i < len(self.__participants) - 1:
                output += ", "

        output += "\n-----------\n"

        # Alle Diskussionspunkte durchgehen
        for item in self.__items:
            output += str(item) + "\n"

        return output


# Import spezieller Python-Funktionalitäten, damit abstrakte Methoden
# definiert werden können
from abc import ABCMeta, abstractmethod

# Abstrakte Klasse Item


class Item(object):

    # Definiere diese Klasse als abstrakte Klasse. Danach können
    # wir abstrakte Funktionen in dieser Klasse definieren (mit
    # @abstractclass).
    __metaclass__ = ABCMeta

    # Konstruktor, der den Content verlangt
    @abstractmethod
    def __init__(self, content):
        self.__content = content

    # Methode zur Repräsentation des Items
    def __str__(self):
        return self.__content


# Öffentliche Klasse zur Repräsentation eines Diskussionsbeitrags
# Es wird von der Klasse Item geerbt.
class DiscussionItem(Item):

    # Der Konstruktor erwartet den Inhalt.
    def __init__(self, content):
        Item.__init__(self, content)

    # Überschreiben der Repräsentation mit der spezifischen Version
    # für einen Diskussionsbeitrag
    def __str__(self):
        return "Discussion: " + Item.__str__(self)


# Klasse, die eine Entscheidung repräsentiert und von der Klasse
# Item erbt
class DecisionItem(Item):

    # Konstruktor, der den Content verlangt
    def __init__(self, content):
        # und die Basisklasse damit aufruft
        Item.__init__(self, content)

    # Überschreiben der Repräsentation mit der spezifischen Version
    # für einen Entscheidungsbeitrag
    def __str__(self):
        return "Decision: " + Item.__str__(self)


# Klasse zur Repräsentation einer Aktion, die von der Klasse
# Item ableitet.
class ActionItem(Item):

    # Öffentlicher Konstruktor, der zur Angabe des Inhalts
    # verpflichtet
    def __init__(self, content):
        Item.__init__(self, content)

    # Überschreiben der Repräsentation mit der spezifischen Version
    # für einen Aktionsbeitrag
    def __str__(self):
        return "Action: " + Item.__str__(self)


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

participants = ["Luigi Lo Iacono", "Michael Schneider",
                "Stephan Wiefling"]
meeting = MeetingMinutes("10.10.2017",
                         "10-12 Uhr", "R123", participants)

meeting.add(DiscussionItem("Veröffentlichung Buch"))
meeting.add(DecisionItem("Dem Antrag wurde einstimmig " +
                         "zugestimmt."))
meeting.add(ActionItem("Bis zum nächsten Meeting muss Kapitel 9" +
                       " fertiggestellt sein."))

print meeting
