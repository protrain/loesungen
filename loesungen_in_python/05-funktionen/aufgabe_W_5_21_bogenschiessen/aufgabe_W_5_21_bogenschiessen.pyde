# Konstanten
G = 9.81
soil_y = 520             # Position, an dem der Boden beginnt
grass_y = 500            # Position, an dem die Wiese beginnt

angle = 1
speed = 1
arrow_x = 1
arrow_y = 1
arrow_fire = 1
arrow_time = False

# Pfeilstartposition
start_x = 60
start_y = grass_y - 40

aim_width = 30
aim_height = 70


# Funktion zum (Re-)Initialisieren von globalen Variablen
# Benötigt keinen Eingabewert und gibt auch keinen Wert
# zurück
def reset():
    global speed, angle, arrow_x, arrow_y, arrow_fire, arrow_time
    global arrowDegrees, aim_x, aim_y
    speed = 90
    angle = 45
    arrow_x = start_x
    arrow_y = start_y
    arrowDegrees = angle
    arrow_fire = False  # Ist Pfeil abgefeuert worden?
    arrow_time = 1
    aim_x = int(random(width - 300, width))
    aim_y = grass_y - aim_height


# Funktion zur Ausgabe von Koordinaten der Wurfparabel zum angeforderten
# Zeitpunkt
# An die Funktion wird die Geschwindigkeit als Integer-Wert sowie der
# Winkel und den Zeitpunkt je als Fließkommazahl gegeben. Die Rückgabe
# erfolgt als Fließkomma-Array.
def get_trajectory(v0, beta, t):
    beta = radians(beta)
    x = v0 * t * cos(beta)
    y = v0 * t * sin(beta) - (G / 2) * t * t
    return [x, y]


# Funktion zur Berechnung des Steigungswinkels des Pfeils (1. Ableitung)
# als Fließkommazahl zurück
def get_degrees(v0, beta, t):
    beta = radians(beta)
    x1 = v0 * cos(beta)
    y1 = v0 * sin(beta) - G * t
    winkel = atan(y1 / x1)
    return degrees(winkel)


# Funktion, die die Reaktion auf Tastatureingaben verarbeitet. Der
# keyCode ist in einer globalen Variable enthalten.
def keyPressed():
    if keyCode == RIGHT:
        increase_speed()
    elif keyCode == LEFT:
        decrease_Speed()
    elif keyCode == UP:
        increase_angle()
    elif keyCode == DOWN:
        decrease_angle()
    elif keyCode == 10:
        global arrow_fire
        arrow_fire = True
    elif key == "r":
        reset()


# Funktion zum Erhöhen der Geschwindigkeit ohne Ein- oder
# Ausgabeparameter
def increase_speed():
    global speed
    if not arrow_fire:
        speed = speed + 1


# Funktion zum Verringern der Geschwindigkeit ohne Ein- oder
# Ausgabeparameter
def decrease_Speed():
    global speed
    if speed > 0 and arrow_fire is False:
        speed = speed - 1


# Funktion zum Erhöhen der Winkels ohne Ein- oder Ausgabeparameter
def increase_angle():
    global angle, arrowDegrees
    if angle < 90 and arrow_fire is False:
        angle = angle + 1
        arrowDegrees = angle


# Funktion zum Verringern der Winkels ohne Ein- oder Ausgabeparameter
def decrease_angle():
    global angle, arrowDegrees
    if angle > -90 and arrow_fire is False:
        angle = angle - 1
        arrowDegrees = angle


# Aktualisiere Pfeilposition
def update_arrow():
    # Nur aktualisieren, wenn Pfeil abgefeuert wurde
    if arrow_fire:
        global arrow_x, arrow_y, arrow_xBefore, arrow_yBefore
        global arrow_time, arrowDegrees

        # Hole Wurfparabel
        new_pos = get_trajectory(speed, angle, arrow_time)
        arrowDegrees = get_degrees(speed, angle, arrow_time)

        # Berechne neue Pfeilposition mit Wurfparabel
        arrow_x = start_x + new_pos[0]
        arrow_y = start_y - new_pos[1]

        # Erhöhe Berechnungszeit der Wurfparabel
        arrow_time = arrow_time + 0.1
        check_collision()


# Funktion zur simplen Kollisionserkennung ohne Ein- und Ausgabeparameter
def check_collision():
    if is_in_bounds(arrow_x, arrow_y):
        global arrow_fire
        arrow_fire = False
        return


# Funktion zur Bestimmung, ob die aktuelle Koordinate im
# Kollisionsbereich liegt
def is_in_bounds(x, y):
    if y > soil_y or x > aim_x and x < aim_x + aim_width and y < aim_y + \
       aim_height and y > aim_y:
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
    check_collision()

    # Pfeil aktualisieren
    update_arrow()

    # Zeichne Wiese
    stroke(76, 178, 33)
    fill(76, 178, 33)
    rect(0, grass_y, width, soil_y - grass_y)

    # Zeichne Boden
    stroke(125, 67, 22)
    fill(125, 67, 22)
    rect(0, soil_y, width, width - soil_y)

    # Zeichne Zielscheibe
    stroke(125, 0, 0)
    fill(125, 0, 0)
    rect(aim_x, aim_y, aim_width, aim_height)

    # Zeichne Pfeil
    stroke(125)
    fill(125)
    radius = 80
    arch_w = cos(radians(arrowDegrees)) * radius
    arch_h = sin(radians(arrowDegrees)) * radius
    line(arrow_x, arrow_y, arrow_x - arch_w, arrow_y + arch_h)
