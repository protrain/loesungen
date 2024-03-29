# Funktion zur Anwendung eines Medianfilters
# auf ein übergebenes Bild. Das Ergebnisbild
# wird von der Funktion zurückgegeben.
def median_filter(input_data):
    # Bildausschnittsarray mit 9 Werten
    area = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    grey = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    output = PImage(input_data.width, input_data.height)

    # Gehe für jedes Pixel einzeln durch
    for y in range(1, input_data.height - 1):
        for x in range(1, input_data.width - 1):
            # Hole Ausschnitt aus Input
            num = 0

            # x,y-Zähler für 3x3-Block
            for j in range(-1, 2):
                for k in range(-1, 2):
                    # Speichere die umliegenden Elemente
                    # im area-Array
                    area[num] = input_data.get(x + k, y + j)
                    num += 1

            # Berechne Grauwerte aus den extrahierten
            # umliegenden Punkten (area-Array)
            for i in range(0, len(area)):
                grey[i] = red(area[i]) * 0.299 + green(area[i]) * 0.581
                + blue(area[i]) * 0.114

            # Sortiere Pixel
            grey = sort(grey)

            # Nehme mittleren Wert
            median = grey[4]

            # Schreibe Median in Ausgangspixel
            output.set(x, y, color(median, median, median))

    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(1000, 1000)
bild = loadImage("image.png")
image_filtered = median_filter(bild)
image(image_filtered, 0, 0)
