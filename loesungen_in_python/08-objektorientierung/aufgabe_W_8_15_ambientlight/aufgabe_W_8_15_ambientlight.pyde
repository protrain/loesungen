# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# Library importiert werden
#from random import randint as random

import colorsys

# Klasse, die die Ansteuerung einer LED realisiert
class AmbiLight:

    # Konstruktor, der die Werte für Hue, Saturation und Brightness
    # erwartet.
    def __init__(self, h, s, b):
        self.__h = h
        self.__s = s
        self.__b = b

    # Öffentliche Methode zum Erhöhen der Farbsättigung
    def increase_saturation(self):
        if self.__s < 100:
            self.__s += 1
        else:
            self.__s = 100

    # Öffentliche Methode zum Herabsetzen der Farbsättigung
    def decrease_saturation(self):
        if self.__s > 0:
            self.__s -= 1
        else:
            self.__s = 0

    # Öffentliche Methode zur Erhöhung der Helligkeit
    def increase_brightness(self):
        if self.__b < 100:
            self.__b += 1
        else:
            self.__b = 100

    # Öffentliche Methode zum Herabsetzen der Helligkeit
    def decrease_brightness(self):
        if self.__b > 0:
            self.__b -= 1
        else:
            self.__b = 0

    # Öffentliche Methode, um die Werte für die nächstmögliche
    # Farbe zu generieren
    def get_next_color(self):
        # Erhöhe Farbwert
        self.__h += 1

        # Wenn Hue den maximalen Farbwert (360 Grad) überschreitet,
        # beginne bei 0 Grad.
        if self.__h > 360:
            self.__h = 0

        # Gebe Farbe als RGB-Farbwert zurück.
        return AmbiLight.hsb_to_rgb(self.__h, self.__s, self.__b)

    # Öffentliche Methode zum Generieren einer Zufallsfarbe
    def get_random_color(self):
        self.__h = int(random(0, 360))
        self.__s = int(random(0, 100))
        self.__b = int(random(0, 100))

        return AmbiLight.hsb_to_rgb(self.__h, self.__s, self.__b)


    # Statische Funktion zur Umrechnung von HSB nach RGB-Werten
    # An die Funktion werden die Werte für die Farbe, die
    # Sättigung und die Helligkeit übergeben.
    # Die Funktion liefert ein Array mit den RGB-Werten zurück.
    @staticmethod
    def hsb_to_rgb(h, s, b):
        # Konvertiere s und b zu Dezimalwert
        __s = s/100.0
        __b = b/100.0
        
        # Generiere RGB-Werte als Dezimalwert
        __r, __g, __b = colorsys.hsv_to_rgb(h, __s, __b)
        
        # Umwandeln in Integer-Wert zwischen 0 und 360
        __r = (__r * 360)//1
        __g = (__g * 360)//1
        __b = (__b * 360)//1
        
        return (__r, __g, __b)
        

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.
al = AmbiLight(0, 0, 50)
for i in range(0, 50):
    al.increase_brightness()
    print(al.get_next_color())
