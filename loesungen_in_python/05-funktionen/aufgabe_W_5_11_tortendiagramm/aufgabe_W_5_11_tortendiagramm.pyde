# Funktion zum Zeichnen eines Tortendiagramms mit den abgegebenen
# Stimmen und den Farben als optionale Eingabe
def draw_pie_chart(numbers, colors=[]):
    # Wenn die Farben noch nicht übergeben wurden
    if len(colors) == 0:
        # Generiere Farben
        for i in range(0, len(numbers)):
            # Generiere die Farben für Rot, Grün und Blau.
            value_r = int(random(0, 255))
            value_g = int(random(0, 255))
            value_b = int(random(0, 255))

            # Setze die Farben für Rot, Grün und Blau.
            colors.append(color(value_r, value_g, value_b))

    # Berechne zunächst die Summe der Einzelelemente
    total_sum = 0.0
    for number in numbers:
        total_sum += number

    # Berechne danach die Prozente
    percentages = []
    for i in range(0, len(numbers)):
        percentages.append(numbers[i] / total_sum * 100)

    # Setze Startposition im Kreis. Wir beginnen am Anfang.
    start = 0.0

    # Gehe nun die Prozente durch
    for i in range(0, len(percentages)):
        percent = percentages[i]

        # Bestimme Endposition in Abhängigkeit vom Prozentsatz
        end = start + 2 * PI / 100 * percent

        # Setze neue Füllfarbe
        fill(colors[i])

        # Male Tortenabschnitt in vordefinierter Farbe
        arc(width / 2, height / 2, 300, 300, start, end)

        # Setze Füllfarbe für den Text
        fill(0)

        # Setze Textgröße
        textSize(30)

        # Setze neue Startposition ans Ende
        start = end


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Setze die Fenstergröße auf 400x400 Pixel
    size(400, 400)

    # Setze weißen Hintergrund
    background(255)

    # Array, in dem wir die absoluten Zahlen für unser
    # Tortendiagramm speichern
    numbers = [900, 1200, 122, 567]

    # Array, in dem wir die Farben für das Tortendiagramm
    # speichern
    colors = [color(32, 39, 56), color(75, 101, 0),
              color(185, 104, 47), color(172, 58, 82)]

    # Zeichne Tortendiagramm mit Farben als Parameter
    draw_pie_chart(numbers, colors)

    # Zeichne Tortendiagramm ohne Farben als Parameter
    #draw_pie_chart(numbers)
