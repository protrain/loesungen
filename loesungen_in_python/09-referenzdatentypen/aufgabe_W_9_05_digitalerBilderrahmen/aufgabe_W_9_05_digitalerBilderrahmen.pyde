from random import randint as random


class DigitalPictureFrame:

    # Klasse, die einen digitalen Bilderrahmen darstellt
    def __init__(self, size):
        # Array mit fester Größe erzeugen
        self.pics = []
        for i in range(0, size):
            self.pics.append(None)

        self.amount = 0
        self.current = 0

    # Öffentliche Methode zum Hinzufügen eines neuen Bilds
    # Das Bild wird der Methode übergeben.
    def add_picture(self, pic):
        # Sind noch Speicherplätze frei, dann hinzufügen
        if self.amount < len(self.pics):
            self.pics[self.amount] = pic

            # Erhöhe Zähler
            self.amount += 1

    # Methode zum Löschen eines Bilds aus dem Bilderrahmen.
    # Der Index des Bilds im Rahmen wird der Methode über-
    # geben.
    def delete_picture(self, index):
        # Nur arbeiten, wenn angegebener Index im
        # gültigen Bereich
        if index >= 0 and index <= self.amount:
            # Kopiere nachfolgende Bilder nach vorne
            for i in range(index, self.amount - 1):
                self.pics[i] = self.pics[i + 1]

            # Reduziere Zähler, da Bild gelöscht
            self.amount -= 1

    # Öffentliche Methode zum Abholen des nächsten Bilds.
    def get_next(self):
        pos = self.current

        # Sorge mit Modulo dafür, dass maximale Anzahl nicht über-
        # schritten werden kann (erspart if-else-Anweisungen)
        self.current = (self.current + 1) % self.amount
        return self.pics[pos]

    # Öffentliche Methode, die ein Zufallsbild aus der
    # Menge der im Rahmen enthaltenen Bilder auswählt
    # und zurückliefert.
    def get_next_random(self):
        return self.pics[int(random(0, self.amount - 1))]


# Öffentliche Klasse Picture, die ein Bild repräsentiert.
class Picture:

    # Konstruktor, der erzwingt, dass bei der Objektgenerierung
    # der Name des Bilds angegeben werden muss
    def __init__(self, name):
        self.name = name

    # Öffentliche Methode, die einen String (in diesem Fall
    # den intern gespeicherten Namen) zurückliefert
    def __str__(self):
        return self.name


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.

dpf = DigitalPictureFrame(3)
dpf.add_picture(Picture("Bild 1"))
dpf.add_picture(Picture("Bild 2"))
dpf.add_picture(Picture("Bild 3"))

# Gebe alle Bilder aus
print(dpf.get_next())

print(dpf.get_next())
print(dpf.get_next())
print()
print(dpf.get_next_random())
dpf.delete_picture(3)

# Hier darf kein Bild 3 auftauchen
print(dpf.get_next_random())
