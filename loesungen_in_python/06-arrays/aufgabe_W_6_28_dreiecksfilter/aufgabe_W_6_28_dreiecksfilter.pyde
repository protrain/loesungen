# Setze Fenstergröße
size(600, 600)

# Lade Bild
img = loadImage("bild.png")

# Lade Bilddaten in Array
img.loadPixels()

# Berechne Skalierungsfaktor in Abhängigkeit von der Fenstergröße
x_scale = width / img.width
y_scale = height / img.height

# Verschiebe das Koordinatensystem
translate(x_scale/2, y_scale)

# Bestimme zunächst die Hintergrundfarbe
bg_r = red(img.pixels[0])
bg_g = green(img.pixels[0])
bg_b = blue(img.pixels[0])

# Gehe alle Pixel nacheinander durch
for i in range(1, len(img.pixels)):
    # Addiere die einzelnen Farbbestandteile
    bg_r += red(img.pixels[i])
    bg_g += green(img.pixels[i])
    bg_b += blue(img.pixels[i])

    # Teile anschließend durch 2, womit wir den Durchschnitt
    # berechnen
    bg_r /= 2
    bg_g /= 2
    bg_b /= 2

# Setze Hintergrundfarbe auf die Durchschnittsfarbe
background(bg_r, bg_g, bg_b)

# Gehe alle Pixel nacheinander durch
for i in range(0, len(img.pixels)):
    # Hole den Pixel an der aktuellen Stelle
    pixel_color = img.pixels[i]

    # Berechne 1D- in 2D-Position um
    y = i / img.width
    x = i % img.width

    # Berechne aus Pixelposition die Koordinaten des Dreiecks
    if y % 2 == 0:
        # Wenn wir in einer geraden Zeile sind
        # Oben links
        x_1 = x * x_scale
        y_1 = y * y_scale - y_scale

        # Oben rechts
        x_2 = x_1 + x_scale
        y_2 = y_1

        # Unten links
        x_3 = x_1
        y_3 = y_1 + y_scale * 2
    else:
        # Wenn wir in einer ungeraden Zeile sind
        # Unten rechts
        x_1 = x * x_scale
        y_1 = y * y_scale

        # Oben rechts
        x_2 = x_1
        y_2 = y_1 - y_scale * 2

        # Unten links
        x_3 = x_1 - x_scale
        y_3 = y_1

    # Setze Farbe
    fill(pixel_color)
    stroke(pixel_color)

    # Male Pixel als Dreieck
    triangle(x_1, y_1, x_2, y_2, x_3, y_3)
