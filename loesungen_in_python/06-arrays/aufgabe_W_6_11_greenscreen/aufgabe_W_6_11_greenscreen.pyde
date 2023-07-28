size(800, 800)


# Funktion zum Verschmelzen zweier Bilder, die
# der Funktion als Parameter übergeben werden
def merge_images(greenscreen, scene):
    # Erzeuge leeres Ergebnisbild
    result_image = PImage(scene.width, scene.height)

    # Lade alle Bilder in den Speicher
    greenscreen.loadPixels()
    scene.loadPixels()
    result_image.loadPixels()

    # Gehe jedes Pixel einzeln durch
    for x in range(0, scene.width):
        for y in range(0, scene.height):
            # Position im Bild als fortlaufenden Index berechnen
            idx = y * greenscreen.width + x

            # Wenn Grün im Bild
            if red(greenscreen.pixels[idx]) == 0 \
                and green(greenscreen.pixels[idx]) == 255 \
                and blue(greenscreen.pixels[idx]) == 0:
                # Übernehme Pixel aus Hintergrund
                result_image.pixels[idx] = scene.pixels[idx]
            else:
                # Sonst übernehme Pixel aus Vordergrund
                result_image.pixels[idx] = greenscreen.pixels[idx]

    result_image.updatePixels()
    return result_image


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

# Lade Bild mit Greenscreen
gs = loadImage("green.png")

# Lade Bild mit Hintergrund
sc = loadImage("bg.png")

# Kombiniere beide Bilder
result = merge_images(gs, sc)

# Gebe kombiniertes Bild im Fenster aus
image(result, 0, 0)
