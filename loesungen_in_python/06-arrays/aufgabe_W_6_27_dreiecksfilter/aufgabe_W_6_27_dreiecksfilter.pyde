# Setze Fenstergröße
size(600, 600)

# Lade Bild
img = loadImage("bild.png")

# Lade Bilddaten in Array
img.loadPixels()

# Berechne Skalierungsfaktor in Abhängigkeit von der Fenstergröße
xScale = width / img.width
yScale = height / img.height

# Verschiebe das Koordinatensystem
translate(xScale / 2, yScale)

# Bestimme zunächst die Hintergrundfarbe
bgR = red(img.pixels[0])
bgG = green(img.pixels[0])
bgB = blue(img.pixels[0])

# Gehe alle Pixel nacheinander durch
for i in range(1, len(img.pixels)):
    # Addiere die einzelnen Farbbestandteile
    bgR += red(img.pixels[i])
    bgG += green(img.pixels[i])
    bgB += blue(img.pixels[i])

    # Teile anschließend durch 2, womit wir den Durchschnitt
    # berechnen
    bgR /= 2
    bgG /= 2
    bgB /= 2

# Setze Hintergrundfarbe auf die Durchschnittsfarbe
background(bgR, bgG, bgB)

# Gehe alle Pixel nacheinander durch
for i in range(0, len(img.pixels)):
    # Hole den Pixel an der aktuellen Stelle
    pixelColor = img.pixels[i]

    # Berechne 1D- in 2D-Position um
    y = i / img.width
    x = i % img.width

    # Berechne aus Pixelposition die Koordinaten des Dreiecks
    if y % 2 == 0:
        # Wenn wir in einer geraden Zeile sind
        # Oben links
        x1 = x * xScale
        y1 = y * yScale - yScale

        # Oben rechts
        x2 = x1 + xScale
        y2 = y1

        # Unten links
        x3 = x1
        y3 = y1 + yScale * 2
    else:
        # Wenn wir in einer ungeraden Zeile sind
        # Unten rechts
        x1 = x * xScale
        y1 = y * yScale

        # Oben rechts
        x2 = x1
        y2 = y1 - yScale * 2

        # Unten links
        x3 = x1 - xScale
        y3 = y1

    # Setze Farbe
    fill(pixelColor)
    stroke(pixelColor)

    # Male Pixel als Dreieck
    triangle(x1, y1, x2, y2, x3, y3)
