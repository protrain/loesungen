# Klasse, die eine Zwischenablage repräsentiert
class Clipboard:

    # Konstruktor, der die internen Werte initialisiert
    # Um eine Instanz dieser Klasse erzeugen zu können, muss
    # die Größe angegeben werden.
    def __init__(self, size):
        # Initialisiere mit n Speicherplätzen
        self.__clipboard = []
        for i in range(0, size):
            self.__clipboard += [None]

        # Aktuelle Schreibposition.
        # Mit erster Erhöhung wird an Position 0 gestartet, daher -1
        self.__position = -1

    def copy(self, string):
        # Wenn Schreibposition noch innerhalb der
        # Speichergröße
        if self.__position < len(self.__clipboard) - 1:
            # Erhöhe Positionszähler
            self.__position += 1

            # Schreibe String an aktuelle Position
            self.__clipboard[self.__position] = string

        # Wenn keine freie Stelle gefunden
        else:
            # Lösche ältesten Eintrag (= erster Eintrag)
            self.__clipboard[0] = None

            # Kopiere um
            # gehe Einträge von 1 bis Ende durch
            for i in range(1, len(self.__clipboard)):
                # Kopiere Eintrag eine Stelle nach vorne
                self.__clipboard[i - 1] = self.__clipboard[i]

            # setze String ans Ende
            self.__clipboard[self.__position] = string

    # Methode zum Einfügen (Rückgabe) des letzten Eintrags
    # aus der Zwischenablage. Die Methode benötigt keine
    # Parametereingabe und gibt den letzten Eintrag wieder
    # zurück.
    def paste(self):
        # Nehme Eintrag von letzter Schreibposition
        string = self.__clipboard[self.__position]

        # Lösche Eintrag an der Stelle
        self.__clipboard[self.__position] = None

        # Reduziere Zähler
        if self.__position > 0:
            self.__position -= 1
        # Wenn negative Position, dann wieder zurücksetzen
        else:
            self.__position = 0

        return string

    # Methode zur Ausgabe der aktuellen Zwischenablage
    def __str__(self):
        return str(self.__clipboard)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
cb = Clipboard(2)

# Schreibe in Zwischenablage absichtlich mehr Inhalt als möglich.
cb.copy("Hallo")
cb.copy("Wie")
cb.copy("Geht")
cb.copy("Es")

# Leere Zwischenablageninhalt
print cb.paste()
print cb.paste()
print cb.paste()
print cb.paste()

print cb
