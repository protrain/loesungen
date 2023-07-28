###
# Variablen setzen
###

# Farben setzen
wiese = color(42, 211, 50)
himmel = color(227, 248, 252)
torpfosten = color(0, 0, 0)
torkasten = color(255, 255, 255, 100)

# Höhe und Breite des Tors festlegen
hoehe = 300
breite = 2.5 * hoehe

# Torposition
tor_x = 100
tor_y = 100

# Oberer linker Eckpunkt des inneren Torkastens
kasten_x = breite * 1 / 8
kasten_y = hoehe * 1 / 8
kasten_breite = breite * 3 / 4
kasten_hoehe = hoehe * 5 / 8

size(1000, 500)

###
# Hintergrund malen
###

# Hintergrundfarbe auf Himmelfarbe setzen
background(himmel)

# Wiesenfarbe setzen
stroke(wiese)
fill(wiese)

# Wiese ab halber Torhöhe zeichnen
rect(0, tor_y + hoehe / 2, 1000, 500)

###
# Tornetz zeichnen
###

strokeWeight(3)

# Setze volle Transparenz (vierter Parameter Alpha=0)
stroke(torkasten)
fill(torkasten)


# Verschiebe Nullpunkt in den Kasten
translate(tor_x + kasten_x, tor_y + kasten_y)

# Male inneren Torkasten
rect(0, 0, kasten_breite, kasten_hoehe)

# Male obere Benetzung
quad(0, 0,
     -kasten_x, -kasten_y,
     breite - kasten_x, -kasten_y,
     kasten_breite, 0)

# Male Benetzung links
quad(0, 0,
     -kasten_x, -kasten_y,
     -kasten_x, hoehe - kasten_y,
     0, kasten_hoehe)

# Verschiebe Koordinatensystem an den rechten Kasten
translate(kasten_breite, 0)

# Male Benetzung rechts
quad(0, 0,
     kasten_x, -kasten_y,
     kasten_x, hoehe - kasten_y,
     0, kasten_hoehe)

translate(-kasten_breite, 0)


###
# Torpfosten malen
###

# Linienfarbe auf Pfostenfarbe setzen
stroke(torpfosten)

# Liniendicke auf 10 Pixel setzen
strokeWeight(10)

# Transformiere Koordinatensystem auf Pfosten
translate(-kasten_x, -kasten_y)

# Pfosten oben
line(0, 0, breite, 0)

# Pfosten links
line(0, 0, 0, hoehe)

# Gehe mit Koordinatensystem die Breite des Pfosten nach rechts
# womit wir an der rechten Pfostenposition sind
translate(breite, 0)

# Pfosten rechts
line(0, 0, 0, hoehe)
