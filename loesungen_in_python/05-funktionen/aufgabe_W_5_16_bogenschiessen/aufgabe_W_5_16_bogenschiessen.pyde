# Konstanten
g = 9.81
soilY = 520             # Position, an dem der Boden beginnt
grassY = 500            # Position, an dem die Wiese beginnt

# Pfeilstartposition
startX = 60
startY = grassY - 40

aimWidth = 30
aimHeight = 70

# Funktion zum (Re-)Initialisieren von globalen Variablen
# Benötigt keinen Eingabewert und gibt auch keinen Wert
# zurück
def reset():
    global speed, angle, arrowX, arrowY, arrowFire, arrowTime
    global arrowDegrees, aimX, aimY
    speed = 90
    angle = 45
    arrowX = startX
    arrowY = startY
    arrowDegrees = angle
    arrowFire = False  # Ist Pfeil abgefeuert worden?
    arrowTime = 1
    aimX = int(random(width - 300, width))
    aimY = grassY - aimHeight

# Funktion zur Ausgabe von Koordinaten der Wurfparabel zum angeforderten
# Zeitpunkt
# An die Funktion wird die Geschwindigkeit als Integer-Wert sowie der
# Winkel und den Zeitpunkt je als Fließkommazahl gegeben. Die Rückgabe
# erfolgt als Fließkomma-Array.
def getTrajectory(v0, beta, t):
    beta = radians(beta)
    x = v0 * t * cos(beta)
    y = v0 * t * sin(beta) - (g / 2) * t * t
    return [x, y]

# Funktion zur Berechnung des Steigungswinkels des Pfeils (1. Ableitung)
# als Fließkommazahl zurück
def getDegrees(v0, beta, t):
    beta = radians(beta)
    x1 = v0 * cos(beta)
    y1 = v0 * sin(beta) - g * t
    winkel = atan(y1 / x1)
    return degrees(winkel)

# Funktion, die die Reaktion auf Tastatureingaben verarbeitet. Der
# keyCode ist in einer globalen Variable enthalten.
def keyPressed():
    if keyCode == RIGHT:
        increaseSpeed()
    elif keyCode == LEFT:
        decreaseSpeed()
    elif keyCode == UP:
        increaseAngle()
    elif keyCode == DOWN:
        decreaseAngle()
    elif keyCode == 10:
        global arrowFire
        arrowFire = True
    elif key == "r":
        reset()

# Funktion zum Erhöhen der Geschwindigkeit ohne Ein- oder
# Ausgabeparameter
def increaseSpeed():
    global speed
    if not arrowFire:
        speed = speed + 1

# Funktion zum Verringern der Geschwindigkeit ohne Ein- oder
# Ausgabeparameter
def decreaseSpeed():
    global speed
    if speed > 0 and arrowFire == False:
        speed = speed - 1

# Funktion zum Erhöhen der Winkels ohne Ein- oder Ausgabeparameter
def increaseAngle():
    global angle, arrowDegrees
    if angle < 90 and arrowFire == False:
        angle = angle + 1
        arrowDegrees = angle

# Funktion zum Verringern der Winkels ohne Ein- oder Ausgabeparameter
def decreaseAngle():
    global angle, arrowDegrees
    if angle > -90 and arrowFire == False:
        angle = angle - 1
        arrowDegrees = angle

# Aktualisiere Pfeilposition
def updateArrow():
    # Nur aktualisieren, wenn Pfeil abgefeuert wurde
    if arrowFire:
        global arrowX, arrowY, arrowXBefore, arrowYBefore
        global arrowTime, arrowDegrees

        # Hole Wurfparabel
        newPos = getTrajectory(speed, angle, arrowTime)
        arrowDegrees = getDegrees(speed, angle, arrowTime)

        # Berechne neue Pfeilposition mit Wurfparabel
        arrowX = startX + newPos[0]
        arrowY = startY - newPos[1]

        # Erhöhe Berechnungszeit der Wurfparabel
        arrowTime = arrowTime + 0.1
        checkCollision()

# Funktion zur simplen Kollisionserkennung ohne Ein- und Ausgabeparameter
def checkCollision():
    if isInBounds(arrowX, arrowY):
        global arrowFire
        arrowFire = False
        return

# Funktion zur Bestimmung, ob die aktuelle Koordinate im
# Kollisionsbereich liegt
def isInBounds(x, y):
    if y > soilY or x > aimX and x < aimX + aimWidth and
        y < aimY + aimHeight and y > aimY:
        return True
    else:
        return False

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    size(1200, 600)
    reset()

# Funktion, die immer wieder zum (Neu-)Zeichnen des Bildschirminhalts
# aufgerufen wird
def draw():
    # zunächst Löschen des Bildschirms
    clear()
    # Hintergrundfarbe setzen
    background(255)
    # mit gesetzter Farbe füllen
    fill(0)
    # Textgröße setzen
    textSize(20)
    # zeichne Variablenangaben
    text("speed: " + str(speed), 5, 25)
    text("angle: " + str(angle), 5, 50)

    # Auf Kollision prüfen
    checkCollision()

    # Pfeil aktualisieren
    updateArrow()

    # Zeichne Wiese
    stroke(76, 178, 33)
    fill(76, 178, 33)
    rect(0, grassY, width, soilY - grassY)

    # Zeichne Boden
    stroke(125, 67, 22)
    fill(125, 67, 22)
    rect(0, soilY, width, width - soilY)

    # Zeichne Zielscheibe
    stroke(125, 0, 0)
    fill(125, 0, 0)
    rect(aimX, aimY, aimWidth, aimHeight)

    # Zeichne Pfeil
    stroke(125)
    fill(125)
    radius = 80
    archW = cos(radians(arrowDegrees)) * radius
    archH = sin(radians(arrowDegrees)) * radius
    line(arrowX, arrowY, arrowX - archW, arrowY + archH)

