# Zusätzliche Iteratorfunktion
import decimal


def drange(d_start, d_end, d_step):
    x = d_start
    while x < d_end:
        yield float(x)
        x += decimal.Decimal(d_step)


# Deklaration der Konstanten g für die Fallbeschleunigung
G = 9.81

# Funktion zum Zeichnen der Koordinaten der Wurfparabel für
# Anfangsgeschwindigkeit v_0 und -winkel beta, die als
# Fließkommazahl an die Funktion übergeben werden. Da die
# Funktion das Berechnen und Zeichnen übernimmt, hat sie
# keinen Rückgabewert.
def draw_trajectory(v_0, beta):
    # Umwandlung von Grad in Radians
    beta = radians(beta)
    # Berechne und zeichne in einer Skalierung von 0.25
    for t in drange(0, 20, 0.25):
        # Startpunkt für Zeichnung ist Fensterhöhe = unterer Rand
        yStart = height

        # Berechne Werte für x und y
        x = v_0 * t * cos(beta)
        y = v_0 * t * sin(beta) - (G / 2) * t * t

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
draw_trajectory(60, 45)
