# Funktion, welche ein Bild in Pixelart umwandelt
def generate_pixelart(image_path, scale_factor):
    # Lade Bild in das Fenster
    img = loadImage(image_path)
    image(img, 0, 0)
    
    # Bestimme Bildhöhe und -breite
    img_height = img.height
    img_width = img.width
        
    # Für jeden Pixel nach der Skalierschrittweite
    for y in range(0, img_height, scale_factor):
        for x in range(0, img_width, scale_factor):
            # Hole Pixelfarbe an Stelle (x, y)
            pixel_color = get(x, y)
                    
            # Male Viereck der Größe scale_factor x scale_factor
            fill(pixel_color)
            # Deaktiviere 
            noStroke()
            rect(x, y, scale_factor, scale_factor)
            
            
# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    # Setze die Fenstergröße
    size(510, 340)
    
    # Lade Bild
    generate_pixelart("./bild.jpg", 10)
    #generate_pixelart("./bild.jpg", 20)
