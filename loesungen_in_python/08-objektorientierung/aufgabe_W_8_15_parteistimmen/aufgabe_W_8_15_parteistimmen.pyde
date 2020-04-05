class Partei:
    # Konstruktor der Klasse, der die Objektgenerierung
    # nur unter der Angabe des Parteinamens als String,
    # der aktuellen Stimmenanzahl als Integer und der
    # vorherigen Stimmenanzahl als Integer ermöglicht
    def __init__(self, name, stimmenVorher, stimmenAktuell):
        self.__name = name
        self.__stimmenAktuell = float(stimmenAktuell)
        self.__stimmenVorher = float(stimmenVorher)

    # Berechnet, um wie viel Prozent sich die Parteistimmen
    # von der vorherigen zur aktuellen Wahl entwickelt haben
    def bestimmeEntwicklung(self):
        # Berechne zunächst als absolute Zahl, wie sehr sich
        # die Stimmen verändert haben
        entwicklungAbsolut = self.__stimmenAktuell - self.__stimmenVorher

        # Berechne jetzt in Prozent, wie sich Zuwachs/Abnahme
        # im Vergleich zur vorherigen Wahl entwickelt haben
        entwicklungProzent = entwicklungAbsolut / self.__stimmenVorher * 100

        return entwicklungProzent

    # Ermittle, ob Partei einen Zuwachs zur vorherigen Wahl
    # bekommen hat
    def istZuwachs(self):
        # Liegt die Prozentzahl über 0, haben wir einen Zuwachs
        return self.bestimmeEntwicklung() > 0

    def __str__(self):
        # In diesem String speichern wir die Ausgabe
        output = "Die Partei '" + self.__name + "' hat einen"

        # Variiere den Text je nach Zuwachs oder Verlust
        if (self.istZuwachs()):
            output += " Zuwachs "
        else:
            output += " Verlust "

        # Füge den Rest vom Text an
        output += "von {}% bekommen".format(self.bestimmeEntwicklung())

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
    println(gewinnerPartei)
    println(verliererPartei)
