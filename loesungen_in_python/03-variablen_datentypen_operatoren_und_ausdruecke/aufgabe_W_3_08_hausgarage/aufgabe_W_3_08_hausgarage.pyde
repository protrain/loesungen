# Farben
weiss = color(255,255,255)
rot = color(255, 0, 0)

# Hauseigenschaften
haus_x = 150
haus_y = 200

# Höhe und Breite des Hauses
haus_hoehe = 300
haus_breite = 300

# Höhe des Dachs, welches auf das Haus gesetzt wird
dach_hoehe = 100

# Definiere Eigenschaften der Garage
garagen_hoehe = haus_hoehe / 2
garagen_breite = haus_breite * 5/8
garage_x = haus_x + haus_breite
garage_y = haus_y + haus_hoehe - garagen_hoehe

# Setze Fenstergröße auf 800x800 Pixel
size(800, 800)

# Setze Hintergrund auf weiß
background(weiss)

# Setze Strichfarbe auf Rot
stroke(rot)

# Setze Strichdicke auf 20 Pixel
strokeWeight(2)

# Rechteck malen
rect(haus_x, haus_y, haus_breite, haus_hoehe)

# Dreieck malen
triangle(haus_x, haus_y,
  haus_x+haus_breite, haus_y,
  haus_breite, haus_y-dach_hoehe) # Y-Koordinatensystem geht nach unten,
                                  # daher haus_y-dach_hoehe

# Male die Garage rechts an das Haus
rect(garage_x, garage_y, garagen_breite, garagen_hoehe)
