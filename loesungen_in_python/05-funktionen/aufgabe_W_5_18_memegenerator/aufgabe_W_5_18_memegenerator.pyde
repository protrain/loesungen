# Funktion, welche die passende Schriftgröße
# für einen Text bestimmt und setzt.
def get_font_size(text, max_font_size, img_width):
    # Starte zunächst bei der maximal gewollten
    # Schriftgröße
    font_size = max_font_size
    
    # Gehe so lange die Schrifgröße herunter
    # bis die Schrift in das Fenster passt
    textSize(font_size)
    while textWidth(text) > img_width:
        if (font_size <= 0):
            # Wir brechen ab, wenn da wir eine ungültige
            # Schriftgröße bekommen
            break
        
        # Reduziere Schriftgröße um 5 Pixel
        font_size -= 5
        textSize(font_size)
    
    return font_size
    

def generate_meme(image_path, text_top, text_bottom):
    # Lade Bild
    img = loadImage(image_path)
    
    # Abmessungen des Eingabebilds
    img_width = img.width
    img_height = img.height
    
    # Die Schriftart muss noch in den externe_daten-Ordner
    # gestellt werden, damit der Code ausgeführt wird.
    font_path = "../../../externe_daten/anton-font/"
    font_path += "data/Anton-Regular.ttf"
    anton = createFont(font_path, 200)
    
    # Setze Schriftart
    textFont(anton)
    
    # Zentriere Text
    textAlign(CENTER)
    
    # Weiße Schrift
    fill(255)
        
    # Zeichne schwarzen Hintergrund
    background(0)
    
    # Zeichne Bild
    image(img, 0, 0)
    
    # Setze Text oben
    font_size = get_font_size(text_top, 80, img_width)
    textSize(font_size)
    text(text_top, img_width/2, font_size)
    
    # Setze Text unten
    font_size = get_font_size(text_bottom, 80, img_width)
    textSize(font_size)
    text(text_bottom, img_width/2, img_height - 10)
    
    # Speichere Bild als JPG-Datei
    save("meme.jpg")


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # Setze die Fenstergröße
    size(510, 340)
    image_path = "./bild.jpg";
    generate_meme(image_path, "MY REACTION", "WHEN I SEE GOOD JAVA CODE")    
    # generate_meme(image_path, "WHEN I SEE YOU", "I GO NUTS")
