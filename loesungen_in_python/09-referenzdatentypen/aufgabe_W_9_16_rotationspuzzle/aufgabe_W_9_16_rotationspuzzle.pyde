# Klasse die ein klickbares Puzzleteil repräsentiert
class PuzzlePiece:
    # Konstruktor, der ein Bild, die
    # Koordinaten und die Rotation erwartet
    def __init__(self, img, x, y, rotation, img_size):
        self.img = img
        self.x = x
        self.y = y
        self.rotation = rotation
        self.img_size = img.width
  
    # Funktion, welches das Bild auf den Bildschirm zeichnet
    def render(self):   
        # Bestimme den Mittelpunkt des Bildes
        x_center = self.x + self.img_size / 2
        y_center = self.y + self.img_size / 2
        
        # Bewege Mittelpunkt des Koordinatensystems in
        # die Mitte des Bildes. Wir müssen das machen,
        # damit wir das Bild in der Mitte drehen können.
        translate(x_center, y_center)
        
        # Drehe Koordinatensystem um angegebenen Rotationswinkel
        rotate(radians(self.rotation))
    
        # Setze das Koordinatensystem des Bildes auf die
        # Mitte, damit wir das Bild an der geplanten
        # Stelle malen können.
        imageMode(CENTER)
        
        # Male das Bild
        image(self.img, 0, 0, self.img_size, self.img_size)
        
        # Rotiere und bewege das Koordinatensystem zurück,
        # damit wir andere Elemente wieder malen können.
        rotate(radians(-self.rotation))
        translate(-x_center, -y_center)
  
    # Funktion, welche prüft, ob das Bild geklickt wurde
    def image_clicked(self, x, y):
        # Berechne den Bildbereich oben links und unten rechts.
        top_left_x = self.x
        top_left_y = self.y
        bottom_right_x = self.x + self.img_size
        bottom_right_y = self.y + self.img_size
        
        # Prüfe, ob Klick im Bildbereich erfolgt ist
        __check = x > top_left_x and x < bottom_right_x
        __check = __check and y > top_left_y and y < bottom_right_y
        return __check
    
    # Funktion, welche das Bild um 90 Grad nach rechts dreht
    def rotate_right(self):
        self.rotation = (self.rotation + 90) % 360
    
    # Funktion, welche eine Klickaktion verarbeitet.
    def handle_click(self):
        if self.image_clicked(mouseX, mouseY):
            # Rotiere Bild um 90 Grad
            self.rotate_right()
  
    # Funktion, welche die Bildrotation zurückgibt
    def get_rotation(self):
        return self.rotation

class RotationPuzzleGame:
    # Konstruktor, der die Puzzlegröße als Integer erwartet
    def __init__(self, puzzle_size):
        # Initialisiere das Spielfeld
        self.puzzle_field = []
        
        # Puzzle ist noch nicht gelöst
        self.solved = False
        
        # Lade das Hauptbild
        self.main_image = loadImage("dog.png")
        
        # Bestimme Größe der Bild-Einzelteile
        img_split_size_x = self.main_image.width / puzzle_size
        img_split_size_y = self.main_image.height / puzzle_size
        
        # Splitte das Bild in Einzelteile
        
        for y in range(0, puzzle_size):
            row = []
            for x in range(0, puzzle_size):
                # Erstelle neues Bildobjekt für Puzzleteil
                __parameters = []
                __parameters.append(img_split_size_x)
                __parameters.append(img_split_size_y)
                __parameters.append(RGB)
                puzzle_piece = createImage(*__parameters)
                
                # Startposition des Bildschnipsels im Hauptbild
                split_start_pos_x = img_split_size_x * x
                split_start_pos_y = img_split_size_y * y
                
                # Kopiere Bildbereich von großem Bild in das Puzzleteil
                __parameters = []
                __parameters.append(split_start_pos_x)
                __parameters.append(split_start_pos_y)
                __parameters.append(img_split_size_x)
                __parameters.append(img_split_size_y)
                puzzle_piece = self.main_image.get(*__parameters)
                        
                # Packe Puzzleteil in das Spielfeld
                __parameters = []
                __parameters.append(puzzle_piece)
                __parameters.append(split_start_pos_x)
                __parameters.append(split_start_pos_y)
                __parameters.append(self.get_random_rotation())
                __parameters.append(img_split_size_x)
                row.append(PuzzlePiece(*__parameters))
            self.puzzle_field.append(row)
            
    # Funktion, welche das Spielfeld darstellt
    def render(self):
        # Gehe alle Elemente des Spielfeldes einzeln durch
        for row in self.puzzle_field:
            for puzzle_piece in row:
                # Male Einzelbild auf Bildschirm
                puzzle_piece.render()
    
        # Prüfen, ob Puzzle gelöst ist
        self.check_status()
        
    # Funktion, welche die Clicks verarbeitet
    def handle_click(self):
        # Gehe alle Elemente des Spielfeldes einzeln durch
        for row in self.puzzle_field:
            for puzzle_piece in row:
                # Male Einzelbild auf Bildschirm
                puzzle_piece.handle_click()
  
    # Funktion, welche eine zufälligen Bildrotation in 90-Grad-
    # Winkeln zurückgibt
    def get_random_rotation(self):
        rotations = [0, 90, 180, 270]
        
        # Bestimme Zufallszahl zwischen 0 und 3
        random_number = int(random(0, 4))
        
        return rotations[random_number]
    
    # Funktion, welche prüft, ob das Spiel geschafft wurde
    def check_status(self):
        # Gehe alle Elemente des Spielfeldes einzeln durch
        for row in self.puzzle_field:
            for puzzle_piece in row:
                # Hole Rotation des Puzzleteils
                rotation = puzzle_piece.get_rotation()
            
                # Wir brechen ab, sofern nicht alle Spielfelder die
                # richtige Rotation von 0 Grad haben
                if rotation != 0:
                    return
                        
        # Wenn wir hier landen, ist das Puzzle gelöst. Nun können die
        # Puzzleteile nicht mehr bewegt werden.
        self.solved = True
        
        font_size = 39
        img_center_x = self.main_image.width / 2
        img_center_y = self.main_image.height + font_size
        
        fill(0, 0, 255)
        textAlign(CENTER)
        textSize(font_size)
        text("Puzzle geloest!",img_center_x, img_center_y)
    
game = None

# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    global game
    size(300, 350)
    game = RotationPuzzleGame(4)


def mouseClicked():
    global game
    game.handle_click()


def draw():
    global game
    if game.solved == False:
        game.render()
