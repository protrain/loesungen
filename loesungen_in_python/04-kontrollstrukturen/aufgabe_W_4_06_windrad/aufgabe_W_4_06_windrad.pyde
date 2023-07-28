size(800, 800)
background(255)
smooth()

fill(86, 135, 174, 175)
noStroke()

# Verschiebe Nullpunkt des Koordinatensystems von der Ecke links oben des
# grafischen Ausgabefensters ins Zentrum.
translate(width / 2, height / 2)

radius = 350.0
for i in range(0, 8):
    arc(radius / 2, 0.0, radius, radius, 0, PI)
    rotate(PI / 4.0)

