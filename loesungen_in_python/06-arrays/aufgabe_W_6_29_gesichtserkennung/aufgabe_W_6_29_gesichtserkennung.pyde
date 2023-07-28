# Funktion, welche ein 3x3 Pixel großen
# Bildarray in Binärwerte umwandelt.
#
# Als Ergebnis liefert die Funktion
# das Array mit den Binärwerten zurück.
def convert_image_to_binary_array(image_pixels):
    # Das reduzierte Bild muss genau drei Pixel hoch und
    # drei Pixel breit sein, ansonsten brechen wir die
    # Berechnung ab.
    image_height = len(image_pixels)
    if image_height != 3:
        return
    image_width = len(image_pixels[0])
    if image_width != 3:
        return

    # Extrahiere mittleres Pixel
    center_pixel = image_pixels[1][1]

    # Definiere Vergleichs-Array. Hier werden wir die Bild-Pixel
    # in binäre Werte umwandeln. Der binäre Wert gibt dabei an,
    # ob der Pixelwert kleiner oder größer gleich dem mittleren
    # Pixel ist.
    binary_pixels = []

    # Vergleiche mittleres Pixel mit den umliegenden Pixeln
    for y in range(0, image_height):
        # Definiere Array für die neue Array-Spalte
        row = []

        for x in range(0, image_width):

            # Hole Pixel an aktueller Position
            current_pixel = image_pixels[y][x]

            # Setze die binären Werte
            if current_pixel < center_pixel:
                # Pixel hat kleineren Wert, daher ist der Binär-
                # Wert gleich 0
                row.append(0)
            else:
                # current_pixel muss an dieser Stelle größer gleich
                # center_pixel sein, daher können wir den Binär-
                # Wert auf 1 setzen
                row.append(1)

        # Füge erstellte Reihe in den Gesamtarray ein
        binary_pixels.append(row)

    return binary_pixels


# Funktion, welche überprüft, ob sich ein Gesicht im Bild-
# Array befindet.
#
# Als Ergebnis liefert die Funktion True (Gesicht erkannt)
# oder False (kein Gesicht erkannt) zurück
def contains_face(image_pixels):
    # Wandle Bild in Binärwerte um
    binary_pixels = convert_image_to_binary_array(image_pixels)

    # Detektiere geforderte Binärpixelreihen
    if binary_pixels[0] == [0, 0, 0] and binary_pixels[1] == [0, 1, 0]:
        return True
    return False


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

# Definiere die Pixel vom Eingangsbild
# Person mit dunkler Haut
image_1 = [[53, 174, 89],
           [93, 190, 33],
           [195, 170, 213]]

# Person mit heller Haut
image_2 = [[83, 191, 102],
           [150, 193, 177],
           [202, 198, 212]]

# Landschaft
image_3 = [[143, 82, 122],
           [167, 137, 35],
           [126, 154, 151]]

print(contains_face(image_1))
print(contains_face(image_2))
print(contains_face(image_3))
