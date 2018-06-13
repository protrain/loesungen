# Farben
weiss = color(255,255,255)
rot = color(255, 0, 0)

# Hauseigenschaften
hausX = 150
hausY = 200

# Höhe und Breite des Hauses
hausHoehe = 300
hausBreite = 300

# Höhe des Dachs, was auf das Haus gesetzt wird
dachHoehe = 100

# Definiere Eigenschaften der Garage
garagenHoehe = hausHoehe / 2
garagenBreite = hausBreite * 5/8
garageX = hausX + hausBreite
garageY = hausY + hausHoehe - garagenHoehe

# Setze Fenstergröße auf 600x600 Pixel
size(800, 800)

# Setze Hintergrund auf weiß
background(weiss)

# Setze Strichfarbe auf Rot
stroke(rot)

# Setze Strichdicke auf 20 Pixel
strokeWeight(2)

# Rechteck malen
rect(hausX, hausY, hausBreite, hausHoehe)

# Dreieck malen
triangle(hausX, hausY,
  hausX+hausBreite, hausY,
  hausBreite, hausY-dachHoehe)   # Y-Koordinatensystem geht nach unten,
                                 # daher hausY-dachHoehe

# Male die Garage rechts an das Haus
rect(garageX, garageY, garagenBreite, garagenHoehe)
