# Funktion zum Erzeugen eines Memory-Felds
# An die Funktion wird die zu erstellende
# Größe übergeben. Die Funktion gibt als Ergebnis
# das generierte Spielfeld als zweidimensionales Array
# zurück.
def generate_memory_field(field_size):
    # Anzahlnummer der Karten
    num_elements = field_size * field_size

    # Gültige Spielfeldgröße?
    if num_elements % 2 == 0 and num_elements > 0:
        # Erzeuge leeres Spielfeld (field_size x field_size)
        memory_field = create_array(field_size)
        num_paare = num_elements / 2

        # Belege Feld mit möglichen Zahlen
        for number in range(1, num_paare + 1):
            # Immer zweimal (= 1 Paar) durchführen
            for j in range(0, 2):
                # Wähle zufällige Position
                random_x = int(random(0, field_size))
                random_y = int(random(0, field_size))

                # Solange Position schon belegt, neue Position wählen
                while memory_field[random_x][random_y] != 0:
                    random_x = int(random(0, field_size))
                    random_y = int(random(0, field_size))

                # setze Zahl
                memory_field[random_x][random_y] = number

        return memory_field
    else:
        # ungültige Spielfeldgröße
        return []


# Funktion zur Visualisierung des berechneten Spielfelds
# An die Funktion wird das generierte Spielfeld als
# zweidimensionales Array übergeben.
def visualize_memory_field(memory_field):
    field_size = len(memory_field)
    if field_size == 0:
        return

    # Pixel pro Schritt
    step_size = width / field_size

    # Halbe Größe einer Karte
    step_middle = step_size / 2

    x = 0
    y = 0
    for row in memory_field:
        x = 0
        for element in row:

            # Karte als Rechteck zeichnen
            fill(255)
            stroke(0)
            rect(x, y, x + step_size, y + step_size)

            # Zahlen reinzeichnen
            fill(0)
            textSize(step_middle)
            text(
                element,
                x +
                step_middle /
                2,
                y +
                step_middle +
                step_middle /
                4)
            x = x + step_size
        y = y + step_size


# Generiert leeres 2D-Array in den Dimensionen array_size x array_size
def create_array(array_size):
    output = []
    for y in range(0, array_size):
        row = []
        for x in range(0, array_size):
            row = row + [0]
        output = output + [row]
    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
size(600, 600)
background(255, 255, 255)

memory_field = generate_memory_field(4)
visualize_memory_field(memory_field)
