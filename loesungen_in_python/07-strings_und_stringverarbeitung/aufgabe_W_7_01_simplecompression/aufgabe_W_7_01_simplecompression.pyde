# Funktion zur einfachen Komprimierung von Strings
# Als Eingabeparameter wird der zu komprimierende String
# übergeben. Die Funktion liefert das Ergebnis der Komprimierung
# zurück.
def simple_compression(input_data):
    c_count = 0                          # Gezählte gleiche Zeichen
    last_char = input_data[0]                 # Letztes Zeichen
    output = ""                         # Komprimierter String

    # Gehe alle Zeichen im String durch
    for current_char in input_data:

        # Wenn Zeichen übereinstimmen:
        if current_char == last_char:
            # Erhöhe Zähler
            c_count += 1
        else:
            # Anzahl + Zeichen an Ausgabestring schreiben
            output += str(c_count) + last_char

            # Zeichenzähler zurücksetzen
            c_count = 1

        # Letztes Zeichen aktualisieren
        last_char = current_char

    # Letztes Zeichen aktualisieren
    output += str(c_count) + last_char

    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    bw_image_string_a = "WWWWBBBWBBBBBBWW"  # compressed: "4W3B1W6B2W"
    bw_image_string_b = "BBBBWWWWWWWWWB"    # compressed: "4B9W1B"
    bw_image_string_c = "WBBBBWWWWWWB"      # compressed: "1W4B6W1B"

    print(simple_compression(bw_image_string_a))
    print(simple_compression(bw_image_string_b))
    print(simple_compression(bw_image_string_c))

# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
