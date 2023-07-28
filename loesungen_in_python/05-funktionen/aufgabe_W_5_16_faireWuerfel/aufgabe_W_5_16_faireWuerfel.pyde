# Wurf und Visualisierung eines 6-seitigen Würfels
dice_number = 1  # Würfelzahl, wird hier einmalig initialisiert

# Funktion zum Zeichnen einer gewürfelten Zahl, die als Integer-Wert
# übergeben wird.
def draw_dice(number):
    # Größe des Würfelpunkts
    dot_size = 40

    # Zeichne Punkte in Abhängigkeit der Nummer
    if(number == 1):
        ellipse(200, 200, dot_size, dot_size)
    elif(number == 2):
        ellipse(100, 100, dot_size, dot_size)
        ellipse(300, 300, dot_size, dot_size)
    elif(number == 3):
        ellipse(100, 100, dot_size, dot_size)
        ellipse(200, 200, dot_size, dot_size)
        ellipse(300, 300, dot_size, dot_size)
    elif(number == 4):
        ellipse(100, 100, dot_size, dot_size)
        ellipse(300, 300, dot_size, dot_size)
        ellipse(300, 100, dot_size, dot_size)
        ellipse(100, 300, dot_size, dot_size)
    elif(number == 5):
        ellipse(100, 100, dot_size, dot_size)
        ellipse(300, 300, dot_size, dot_size)
        ellipse(300, 100, dot_size, dot_size)
        ellipse(100, 300, dot_size, dot_size)
        ellipse(200, 200, dot_size, dot_size)
    elif(number == 6):
        ellipse(100, 100, dot_size, dot_size)
        ellipse(300, 300, dot_size, dot_size)
        ellipse(300, 100, dot_size, dot_size)
        ellipse(100, 300, dot_size, dot_size)
        ellipse(100, 200, dot_size, dot_size)
        ellipse(300, 200, dot_size, dot_size)

# Funktion zum Generieren einer Zufallszahl
# die dann als Integer-Wert zurückgeliefert wird
def throw_dice():
    return int(random(1, 7))

# Diese Funktion wird ausgeführt, wenn eine Taste
# gedrückt wurde
def keyPressed():
    global dice_number
    dice_number = throw_dice()

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    size(400, 400)
    global dice_number
    dice_number = throw_dice()  # Zur Initialisierung einmal werfen

# Funktion zum Zeichnen
def draw():
    clear()
    stroke(0)
    fill(0)
    background(255, 255, 255)
    draw_dice(dice_number)
