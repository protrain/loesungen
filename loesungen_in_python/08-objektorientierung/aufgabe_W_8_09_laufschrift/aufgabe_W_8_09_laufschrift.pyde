# Klasse, welche die Laufschrift realisiert
class Ticker:
    # Konstuktor, welche den Text und die
    # Geschwindigkeit festlegt
    def __init__(self, text, speed_per_frame):
        # Processing kann im Python-Mode nicht auf die interne
        # height- und width-Variablen zugreifen, daher definieren
        # wir hier statische Werte.
        height = 100
        width = 100
        
        # Darzustellender Text
        self.text = text
        self.text_size = height / 4
        # Laufgeschwindigkeit pro Frame
        self.speed_per_frame = speed_per_frame
        
        # Position des Textes
        # Wir starten am Rand des Bildschirmfensters
        self.x = width
        self.y = height / 2
    
    # Funktion, welche den Text für den aktuellen Frame
    # nach links bewegt
    def move_text(self):
        # Wir müssen die Breite des Textes wissen, damit
        # wir wissen, wann der Text nicht mehr zu sehen ist.
        textSize(self.text_size)
        text_width = int(textWidth(self.text))
        
        if self.x < -text_width:
            # Text ist nicht mehr sichtbar, also bewegen
            # wir ihn wieder an den Anfang
            self.x = width
        else:
            self.x -= self.speed_per_frame
            
    # Funktion, welche den Text auf den Bildschirm zeichnet
    def draw_text(self):
        background(255)
        fill(0)
        textSize(self.text_size)
        textAlign(LEFT, CENTER)
        text(self.text, self.x, self.y)


ticker = Ticker("+++ Kaffee 1 Euro +++", 1)


def setup():
    size(100, 100)    


def draw():
    global ticker
    ticker.draw_text()
    ticker.move_text()
