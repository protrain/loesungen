# Wurf und Visualisierung eines 6-seitigen Würfels
diceNumber = 1  # Würfelzahl, wird hier einmalig initialisiert

# Funktion zum Zeichnen einer gewürfelten Zahl, die als Integer-Wert
# übergeben wird.
def drawDice(number):
    # Größe des Würfelpunkts
    dotSize = 40

    # Zeichne Punkte in Abhängigkeit der Nummer
    if(number == 1):
        ellipse(200, 200, dotSize, dotSize)
    elif(number == 2):
        ellipse(100, 100, dotSize, dotSize)
        ellipse(300, 300, dotSize, dotSize)
    elif(number == 3):
        ellipse(100, 100, dotSize, dotSize)
        ellipse(200, 200, dotSize, dotSize)
        ellipse(300, 300, dotSize, dotSize)
    elif(number == 4):
        ellipse(100, 100, dotSize, dotSize)
        ellipse(300, 300, dotSize, dotSize)
        ellipse(300, 100, dotSize, dotSize)
        ellipse(100, 300, dotSize, dotSize)
    elif(number == 5):
        ellipse(100, 100, dotSize, dotSize)
        ellipse(300, 300, dotSize, dotSize)
        ellipse(300, 100, dotSize, dotSize)
        ellipse(100, 300, dotSize, dotSize)
        ellipse(200, 200, dotSize, dotSize)
    elif(number == 6):
        ellipse(100, 100, dotSize, dotSize)
        ellipse(300, 300, dotSize, dotSize)
        ellipse(300, 100, dotSize, dotSize)
        ellipse(100, 300, dotSize, dotSize)
        ellipse(100, 200, dotSize, dotSize)
        ellipse(300, 200, dotSize, dotSize)

# Funktion zum Generieren einer Zufallszahl
# die dann als Integer-Wert zurückgeliefert wird
def throwDice():
    return int(random(1, 7))

# Diese Funktion wird ausgeführt, wenn eine Taste
# gedrückt wurde
def keyPressed():
    global diceNumber
    diceNumber = throwDice()

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    size(400, 400)
    global diceNumber
    diceNumber = throwDice()  # Zur Initialisierung einmal werfen

# Funktion zum Zeichnen
def draw():
    clear()
    stroke(0)
    fill(0)
    background(255, 255, 255)
    drawDice(diceNumber)

