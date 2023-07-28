size(400, 400)
background(0)
strokeWeight(4)

# Skalierungsfaktor
scale = 80

# Koordinatensystem verschieben
translate(width / 2 - 180, height / 2)

# Zeichne Linien bei 0, 90, 180, 270 und 360 Grad
stroke(125)
for x in range(0, 361, 90):
    line(x, -scale * 2, x, scale * 2)

# Zeichne horizontale Linie
stroke(255, 255, 0)
line(0, 0, 360, 0)

# Stelle Sinuskurve dar
stroke(255, 0, 0)
for x in range(0, 360):
    # Sinus aus Gradzahl berechnen (Zahl von -1 bis 1)
    y = sin(radians(x))

    # Punkt zeichnen
    point(x, -y * scale)

