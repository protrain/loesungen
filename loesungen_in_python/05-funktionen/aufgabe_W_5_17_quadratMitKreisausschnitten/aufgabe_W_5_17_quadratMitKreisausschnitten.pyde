# Funktion zum Zeichnen von Kreisausschnitten. Die
# Anzahl an Kreisen(= Spalten) wird als ganzzahliger
# Wert an die Funktion übergeben.
def draw_arcs(num_arcs_per_row):
    # Setze Radius für jeden Kreis,
    # nutze dabei gegebenen Platz bestmöglich aus

    # Den kleineren Wert des Ausgabebereichs bestimmen
    # und für diesen den Radius bestimmen
    if width > height:
        radius = height / num_arcs_per_row
    else:
        radius = width / num_arcs_per_row

    # Winkelschritt pro Kreis (360 Grad entspricht 2*PI)
    winkel_step = 2 * PI / (num_arcs_per_row * num_arcs_per_row)
    winkel = 0  # Startwert

    # Durchlaufe nun alle Zeilen
    for y in range(0, num_arcs_per_row):
        # und pro Zeile für alle Spalten
        for x in range(0, num_arcs_per_row):
            # Setze zufällige Farbe
            color_r = int(random(0, 255))
            color_g = int(random(0, 255))
            color_b = int(random(0, 255))
            fill(color_r, color_g, color_b)
            stroke(color_r, color_g, color_b)

            # Erhöhe Kreiswinkel um Winkelschritt
            winkel = winkel + winkel_step

            # Zeichne Kreis
            arc(radius * x + (radius / 2), radius * y +
                (radius / 2), radius, radius, 0, winkel)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

size(600, 600)
background(255, 255, 255)
draw_arcs(16)
