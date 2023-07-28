# Konstanten für die Antwort
NO_SOLUTION = -1

# Richtige Antwort
CORRECT = 1

# Falsche Antwort
WRONG = 0

# Noch keine Lösung angeklickt
solution = NO_SOLUTION

img_left, img_middle, img_right = (None, None, None)
img_width = 0

correct_x_1, correct_y_1, correct_x_2, correct_y_2 = (0, 0, 0, 0)


def setup():
    # Erlaube Zugriff auf globale Variablen
    global img_left, img_middle, img_right
    global img_width
    global solution
    global correct_x_1, correct_x_2, correct_y_1, correct_y_2

    # Definiere Fenstergröße
    size(600, 200)
    
    # Setze Hintergrundfarbe auf weiß
    background(255)
    
    # Lade CAPTCHA-Bild mit korrekter Lösung
    dog0 = loadImage("./dog0.png")
    dog90 = loadImage("./dog90.png")
    dog180 = loadImage("./dog180.png")
    dog270 = loadImage("./dog270.png")
    
    # Leite Höhe und Breite des Bildes ab
    img_width = dog0.width
    img_height = dog0.height
    
    # Wähle zufällig Bildposition (Stellen 0-2) aus
    # welche die Richtige ist
    correct_image = int(random(0, 3))
    
    # Berechne den Klickbereich, an dem wir mit einem
    # korrekt geratenen Bild rechnen
    
    # Oben links
    correct_x_1 = img_width * correct_image
    correct_y_1 = 0
    # Unten rechts
    correct_x_2 = img_width * (correct_image + 1)
    correct_y_2 = img_height
    
    # Setze die Bilder für die entsprechenden Positionen.
    if correct_image == 0:
        img_left = dog0
    else:
        # Wähle Zufallszahl und bestimme danach zufälliges
        # "falsches" Bild
        random_int = int(random(0, 3))
        if random_int == 0:
            img_left = dog90
        elif random_int == 1:
            img_left = dog180
        else:
            img_left = dog270
    
    if correct_image == 1:
        img_middle = dog0
    else:
        # Wähle Zufallszahl und bestimme danach zufälliges
        # "falsches" Bild
        random_int = int(random(0, 3))
        if random_int == 0:
            img_middle = dog90
        elif random_int == 1:
            img_middle = dog180
        else:
            img_middle = dog270

    if correct_image == 2:
        img_right = dog0
    else:
        # Wähle Zufallszahl und bestimme danach zufälliges
        # "falsches" Bild
        random_int = int(random(0, 3))
        if random_int == 0:
            img_right = dog90
        elif random_int == 1:
            img_right = dog180
        else:
            img_right = dog270


def draw():
    # Erlaube Zugriff auf globale Variablen
    global img_left, img_middle, img_right
    global img_width
    global solution
    
    if solution == WRONG:
        # Falsche Antwort
        # Zeichne roten Hintergrund
        background(255, 0, 0)
    elif solution == CORRECT:
        # Richtige Antwort
        # Zeichne blauen Hintergrund
        background(0, 0, 255)
    else:
        # Es wurde noch kein Bild angeklickt
        # Zeichne Bild
        image(img_left, 0, 0)
        image(img_middle, img_width, 0) 
        image(img_right, img_width*2, 0)


# Funktion, welche Mausklicks verarbeitet
def mouseClicked():
    # Erlaube Zugriff auf globale Variablen
    global correct_x_1, correct_x_2, correct_y_1, correct_y_2
    global solution
    
    # Prüfe, ob Position der Maus im korrekten
    # Klickbereich liegt
    if mouseX > correct_x_1 and mouseX < correct_x_2:
        if mouseY > correct_y_1 and mouseY < correct_y_2:
            solution = CORRECT
        else:
            solution = WRONG
    else:
        solution = WRONG
