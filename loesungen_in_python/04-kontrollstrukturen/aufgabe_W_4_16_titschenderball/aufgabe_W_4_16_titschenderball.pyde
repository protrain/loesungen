# Zeitpunkt in unserer Simulation
t = 0

# Startposition unseres Balles
y = 10

# Position des Bodens
yBottom = 600

# Gravitationskraft, hier um ein Zehntel herunterskaliert
g = 9.81 / 10.0

# Wir haben die Gravitation als Anfangsgeschwindigkeit
v = g

# Geschwindigkeitsverlust nach Aufprall
cor = 0.7

# Berechne Zeitpunkt, an dem die Geschwindigkeit 0 wird
v1 = sqrt(v * v + 2 * g * (y - yBottom))
tBorder = 1 / g * (v + v1 * ((1 + cor) / (1 - cor)))


def setup():
    # Setze die Bildschirmgröße
    size(100, 630)


def draw():
    global t, y, yBottom, g, v, cor, v1, tBorder
    # Male den Hintergrund
    background(255)

    # Haben wir den Grenzzeitpunkt erreicht
    if t > tBorder:
        # Setze die Geschwindigkeit auf 0 und stoppe damit den Ball
        v = 0
    else:
        # Setze die Geschwindigkeit in Abhängigkeit von der Gravitation
        v = v + g

    # Berechne die neue Y-Position des Balles
    y = y + v

    # Berührt unser Ball den Boden
    if y >= yBottom:
        # Verändere Richtung und Geschwindigkeit des Balles
        v = v * -cor

        # Setze die Position auf den Boden
        y = yBottom

    # Setze die Linienfarbe auf Schwarz
    stroke(0)

    # Male den Boden
    line(0, yBottom, width, yBottom)

    # Setze die Ballfarbe auf Grau
    fill(125)

    # Zeichne den Ball
    ellipse(50, y, 30, 30)

    # Erhöhe die Zeitpunktzahl um Eins
    t += 1
