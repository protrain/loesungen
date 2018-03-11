# Zusätzliche Iteratorfunktion
import decimal


def drange(dStart, dEnd, dStep):
    x = dStart
    while x < dEnd:
        yield float(x)
        x += decimal.Decimal(dStep)


# Deklaration der Konstanten g für die Fallbeschleunigung
g = 9.81

# Funktion zum Zeichnen der Koordinaten der Wurfparabel für
# Anfangsgeschwindigkeit v0 und -winkel beta, die als
# Fließkommazahl an die Funktion übergeben werden. Da die
# Funktion das Berechnen und Zeichnen übernimmt, hat sie
# keinen Rückgabewert.
def drawTrajectory(v0, beta):
    # Umwandlung von Grad in Radians
    beta = radians(beta)
    # Berechne und zeichne in einer Skalierung von 0.25
    for t in drange(0, 20, 0.25):
        # Startpunkt für Zeichnung ist Fensterhöhe = unterer Rand
        yStart = height

        # Berechne Werte für x und y
        x = v0 * t * cos(beta)
        y = v0 * t * sin(beta) - (g / 2) * t * t

        # Zeichne Parabelpunkte
        # y muss horizontal gedreht werden (s. Hinweise)
        ellipse(x, -y + yStart, 2, 2)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

size(400, 400)
stroke(255, 0, 0)
fill(255, 0, 0)
background(0, 0, 0)
drawTrajectory(60, 45)

