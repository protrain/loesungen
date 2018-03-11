# Klasse, die die Ansteuerung einer LED realisiert
class AmbiLight:

    # Konstruktor, der die Werte für Hue, Saturation und Lightness
    # erwartet.
    def __init__(self, h, s, l):
        self.__h = h
        self.__s = s
        self.__l = l

    # Öffentliche Methode zum Erhöhen der Farbsättigung
    def increaseSaturation(self):
        if self.__s < 100:
            self.__s += 1
        else:
            self.__s = 100

    # Öffentliche Methode zum Herabsetzen der Farbsättigung
    def decreaseSaturation(self):
        if self.__s > 0:
            self.__s -= 1
        else:
            self.__s = 0

    # Öffentliche Methode zur Erhöhung der Helligkeit
    def increaseLightness(self):
        if self.__l < 100:
            self.__l += 1
        else:
            self.__l = 100

    # Öffentliche Methode zum Herabsetzen der Helligkeit
    def decreaseLightness(self):
        if self.__l > 0:
            self.__l -= 1
        else:
            self.__l = 0

    # Öffentliche Methode, um die Werte für die nächstmögliche
    # Farbe zu generieren
    def getNextColor(self):
        # Erhöhe Farbwert
        self.__h += 1

        # Wenn Hue den maximalen Farbwert (360 Grad) überschreitet,
        # beginne bei 0 Grad.
        if self.__h > 360:
            self.__h = 0

        # Gebe Farbe als RGB-Farbwert zurück.
        return AmbiLight.hslToRgb(self.__h, self.__s, self.__l)

    # Öffentliche Methode zum Generieren einer Zufallsfarbe
    def getRandomColor(self):
        self.__h = int(random(0, 360))
        self.__s = int(random(0, 100))
        self.__l = int(random(0, 100))

        return AmbiLight.hslToRgb(self.__h, self.__s, self.__l)

    # Private Funktion zur Umrechnung von HSL nach RGB-Werten
    # An die Funktion werden die Werte für die Farbe, die
    # Sättigung und die Helligkeit übergeben.
    # Die Funktion liefert ein Array mit den RGB-Werten zurück.
    @staticmethod
    def hslToRgb(h, s, l):
        s = s / 100.0
        l = l / 100.0

        # Wenn keine Sättigung, dann ist es Grauwert
        if s == 0:
            r = 255 * l
            g = 255 * l
            b = 255 * l
        else:
            # Nutze temporäre Variablen zur Weiterberechnung
            if l < 0.5:
                temp1 = l * (1.0 + s)
            else:
                temp1 = l + s - (l * s)

            temp2 = 2 * l - temp1

            # Bringe Hue auf Werte zwischen 0 und 1
            h = h / 360.0

            # Nutze temporäre RGB-Variablen zur Weiterberechnung
            tempR = h + 0.333
            tempG = h
            tempB = h - 0.333

            # Sorge dafür, dass alle RGB-Werte zwischen 0 und 1 liegen
            tempR = AmbiLight.convertBetween0and1(tempR)
            tempG = AmbiLight.convertBetween0and1(tempG)
            tempB = AmbiLight.convertBetween0and1(tempB)

            # Berechne RGB-Werte
            r = AmbiLight.calculateColor(tempR, temp1, temp2)
            g = AmbiLight.calculateColor(tempG, temp1, temp2)
            b = AmbiLight.calculateColor(tempB, temp1, temp2)

            # Wandle in Werte von 0 bis 255 um
            r = int(round(r * 255))
            g = int(round(g * 255))
            b = int(round(b * 255))

        return [r, g, b]

    @staticmethod
    def convertBetween0and1(value):
        if value < 0:
            value = value + 1
        elif value > 1:
            value = value - 1
        return value

    # Finde korrekte Berechnungsformel
    # Hilfsfunktion, um Duplikate zu vermeiden
    @staticmethod
    def calculateColor(tempColor, temp1, temp2):
        if (6 * tempColor) < 1:
            c = temp2 + (temp1 - temp2) * 6 * tempColor
        elif (2 * tempColor) < 1:
            c = temp1
        elif (3 * tempColor) < 2:
            c = temp2 + (temp1 - temp2) * (0.666 - tempColor) * 6
        else:
            c = temp2
        if c > 1:
            c = 1
        return c


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
al = AmbiLight(0, 0, 50)
for i in range(0, 50):
    al.increaseLightness()
    print al.getNextColor()
