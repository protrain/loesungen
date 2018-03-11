# Funktion zum Zeichnen von Kreisausschnitten. Die
# Anzahl an Kreisen(= Spalten) wird als ganzzahliger
# Wert an die Funktion übergeben.
def drawArcs(numArcsPerRow):
    # Setze Radius für jeden Kreis,
    # nutze dabei gegebenen Platz bestmöglich aus

    # Den kleineren Wert des Ausgabebereichs bestimmen
    # und für diesen den Radius bestimmen
    if width > height:
        radius = height / numArcsPerRow
    else:
        radius = width / numArcsPerRow

    # Winkelschritt pro Kreis (360 Grad entspricht 2*PI)
    winkelStep = 2 * PI / (numArcsPerRow * numArcsPerRow)
    winkel = 0  # Startwert

    # Durchlaufe nun alle Zeilen
    for y in range(0, numArcsPerRow):
        # und pro Zeile für alle Spalten
        for x in range(0, numArcsPerRow):
            # Setze zufällige Farbe
            colorR = int(random(0, 255))
            colorG = int(random(0, 255))
            colorB = int(random(0, 255))
            fill(colorR, colorG, colorB)
            stroke(colorR, colorG, colorB)

            # Erhöhe Kreiswinkel um Winkelschritt
            winkel = winkel + winkelStep

            # Zeichne Kreis
            arc(radius * x + (radius / 2), radius * y +
                (radius / 2), radius, radius, 0, winkel)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

size(600, 600)
background(255, 255, 255)
drawArcs(16)

