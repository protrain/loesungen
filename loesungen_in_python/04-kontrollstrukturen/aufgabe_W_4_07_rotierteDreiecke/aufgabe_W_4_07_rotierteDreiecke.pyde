size(800, 800)
background(255)
smooth()

noFill()
strokeWeight(4)

# Verschiebe Nullpunkt des Koordinatensystems von der Ecke links oben des
# grafischen Ausgabefensters ins Zentrum.
translate(width / 2, height / 2)

# Halbe Größe des Dreiecks
size = 250

for i in range(0, 20):
    # Wähle zufällige Farbe
    stroke(random(0, 255), random(0, 255), random(0, 255))

    # Male Dreieck um die Mitte
    triangle(0, -size, size, size, -size, size)

    # Rotiere um 360/20 Grad
    rotate(2 * PI / 20)

