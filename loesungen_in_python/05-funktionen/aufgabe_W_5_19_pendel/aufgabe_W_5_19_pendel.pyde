angle = 0
velocity = 0

# Länge des Pendelfadens
length_m = 1

# Gravitationskonstante
gravity_mps2 = 9.80665

# Definiere rücktreibende Kraft
k = -gravity_mps2 / length_m

# Schrittweite bei jedem Zeichenvorgang in Sekunden
timestep_s = 0.01


def setup():
    # Lade globale Variablen
    global angle, velocity

    # Setze die Fenstergröße auf 600x600 Pixel
    size(600, 600)

    # Setze Startgeschwindigkeit auf 0
    velocity = 0

    # Setze Startwinkel des Pendels auf PI/3
    angle = PI / 3


def draw():
    # Lade globale Variablen
    global acceleration, velocity, angle

    # Male den Hintergrund
    background(255)

    # Berechne die Beschleunigung
    acceleration = k * sin(angle)

    # Berechne damit die neue Geschwindigkeit
    velocity += acceleration * timestep_s

    # Berechne damit den neuen Winkel des Pendels
    angle += velocity * timestep_s

    # Zeichne anschließend die Schwingung
    drawSwing(angle)


# Funktion, die die Schwingung im angegebenen
# Winkel zeichnet
def drawSwing(angle):
    # Radius des Pendels, also die Länge des
    # Pendelfadens
    rPend = min(width, height) * 0.47

    # Radius der Pendelkugel
    rBall = min(width, height) * 0.05

    # Setze Füllfarbe auf Schwarz
    fill(0)

    # Verschiebe das Koordinatensystem in die Fenstermitte
    translate(width / 2, height / 2)

    # Rotiere um den angegebenen Winkel
    rotate(angle)

    # Zeichne den Pendelfaden
    line(0, 0, 0, rPend * length_m)

    # Zeichne den Pendelkörper
    ellipse(0, rPend * length_m, rBall, rBall)
