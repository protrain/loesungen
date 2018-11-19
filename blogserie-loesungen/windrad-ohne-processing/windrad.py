#!/usr/bin/env python3
# coding=utf-8
import sys, pygame

# Starte Pygame
pygame.init()

# Definiere Fenstergröße
width = 800
height = 800

# Setze Abmaße für Bildschirmfenster
screen = pygame.display.set_mode((width, height))

# Definiere Farben:
# Weiß
white = 255, 255, 255

# Windrad-Farbe
windrad_farbe = 86, 135, 174, 175


# Endlos-Schleife (Inhalt darin entspricht draw()-Funktion in Processing)
while 1:
    # Arbeite alle Events ab, die pygame erzeugt
    for event in pygame.event.get():
        # Beende Programm, wenn das QUIT-Event gestartet wurde
        # (z.B. durch Klick auf den Schließen-Button im Programmfenster))
        if event.type == pygame.QUIT:
            sys.exit()

    # Ab hier zeichnen wir das Bild
    ###############################

    # Setze Hintergrund auf Weiß
    screen.fill(white)

    # Definiere Radius des Windrades
    radius = 350

    # Definiere Höhe des Windrad-Flügels
    hoehe = 10

    # Definiere Eigenschaften eines Windrad-Flügels
    # (x,y) = (0, 0), Breite = Radius, Höhe
    windrad_abmasse = pygame.Rect(0, 0, radius, hoehe)

    # Definiere Mitte des Bildes
    mitte = width/2, height/2

    # Erzeuge Einzelteile des Windrades
    for i in range(0, 8):
        # Erzeuge neue Zeichenfläche für Windrad-Element (radius x radius)
        surface = pygame.Surface(((radius, hoehe)))

        # Setze Hintergrund der Zeichenfläche auf Transparent (blende weiße Farbe aus)
        surface.fill(white)
        surface.set_colorkey(white)

        # Male Rechteck auf die Zeichenfläche
        pygame.draw.rect(surface, windrad_farbe, windrad_abmasse)

        # Rotiere den Bogen um entsprechende Gradzahl
        winkel = -45*i

        # Einfache Rotation durchführen
        # Achtung: Ab 90 Grad Rotation verändert pygame die Abmaße unserer
        # Zeichenfläche
        surface = pygame.transform.rotate(surface, winkel)

        # Berechne Position der gedrehten Zeichenfläche.
        if i<3:
            # Zeichne unten rechts
            # (obere linke Ecke der Zeichenfläche in der Mitte des Bildes)
            position = surface.get_rect(topleft = mitte)
        elif i<5:
            # Zeichne unten links
            # (obere rechte Ecke der Zeichenfläche in der Mitte des Bildes)
            position = surface.get_rect(topright = mitte)
        elif i<7:
            # Zeichne oben links
            # (untere rechte Ecke der Zeichenfläche in der Mitte des Bildes)
            # Wir müssen dabei die Y-Position um die Hälfte der Höhe verschieben, damit
            # wir in der Mitte des Windradflügels sind
            position = surface.get_rect(bottomright = (mitte[0], mitte[1]+hoehe/2))
        else:
            # Zeichne oben rechts
            # (untere linke Ecke der Zeichenfläche in der Mitte des Bildes)
            # Wir müssen dabei die Y-Position um die Hälfte der Höhe verschieben, damit
            # wir in der Mitte des Windradflügels sind
            position = surface.get_rect(bottomleft = (mitte[0], mitte[1]+hoehe/2))

        # Zeichne Fläche in das Bildschirmfenster
        screen.blit(surface, position)

    # Zeige alle gezeichneten Elemente im Fenster an
    pygame.display.flip()