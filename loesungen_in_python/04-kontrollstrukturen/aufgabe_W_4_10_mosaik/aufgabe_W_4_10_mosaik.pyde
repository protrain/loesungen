size(800, 800)
background(255)
noStroke()

# Größe pro Kästchen
size = 20

# Gehe alle Spalten durch
for y in range(0, height / size):
    # Gehe alle Zeilen durch
    for x in range(0, width / size):
        # Zufällige Füllfarbe
        fill(random(0, 255), random(0, 255), random(0, 255))

        # Zufälliger Rotationswinkel
        angle = random(-PI / 32, PI / 32)

        # Rotiere hin
        rotate(angle)

        # Zeichne Rechteck
        rect(0, 0, size, size)

        # Rotiere zurück
        rotate(-angle)

        # Bewege Koordinatensystem nach rechts
        translate(size, 0)

    # Bewege Koordinatensystem nach unten und ganz nach links
    translate(-height, size)

