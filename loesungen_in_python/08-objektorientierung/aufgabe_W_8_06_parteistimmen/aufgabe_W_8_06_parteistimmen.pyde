class Partei:
    # Konstruktor der Klasse, der die Objektgenerierung
    # nur unter der Angabe des Parteinamens als String,
    # der aktuellen Stimmenanzahl als Integer und der
    # vorherigen Stimmenanzahl als Integer ermöglicht
    def __init__(self, name, stimmen_vorher, stimmen_aktuell):
        self.__name = name
        self.__stimmen_aktuell = float(stimmen_aktuell)
        self.__stimmen_vorher = float(stimmen_vorher)

    # Berechnet, um wie viel Prozent sich die Parteistimmen
    # von der vorherigen zur aktuellen Wahl entwickelt haben
    def bestimme_entwicklung(self):
        # Berechne zunächst als absolute Zahl, wie sehr sich
        # die Stimmen verändert haben
        entwicklung_absolut = self.__stimmen_aktuell - self.__stimmen_vorher

        # Berechne jetzt in Prozent, wie sich Zuwachs/Abnahme
        # im Vergleich zur vorherigen Wahl entwickelt haben
        entwicklung_prozent = entwicklung_absolut / self.__stimmen_vorher * 100

        return entwicklung_prozent

    # Ermittle, ob Partei einen Zuwachs zur vorherigen Wahl
    # bekommen hat
    def ist_zuwachs(self):
        # Liegt die Prozentzahl über 0, haben wir einen Zuwachs
        return self.bestimme_entwicklung() > 0

    def __str__(self):
        # In diesem String speichern wir die Ausgabe
        output = "Die Partei '" + self.__name + "' hat einen"

        # Variiere den Text je nach Zuwachs oder Verlust
        if self.ist_zuwachs():
            output += " Zuwachs "
        else:
            output += " Verlust "

        # Füge den Rest vom Text an
        output += "von {}% bekommen".format(self.bestimme_entwicklung())

        # Gebe diesen String nun aus
        return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # Erstelle Parteien
    gewinnerPartei = Partei("Gewinnerpartei", 500, 600)
    verliererPartei = Partei("Verliererpartei", 600, 300)

    # Gebe die Statistik aus
    print(gewinnerPartei)
    print(verliererPartei)


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
