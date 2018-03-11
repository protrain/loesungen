# Funktion zur einfachen Komprimierung von Strings
# Als Eingabeparameter wird der zu komprimierende String
# übergeben. Die Funktion liefert das Ergebnis der Komprimierung
# zurück.
def simpleCompression(input):
    cCount = 0                          # Gezählte gleiche Zeichen
    lastChar = input[0]                 # Letztes Zeichen
    output = ""                         # Komprimierter String

    # Gehe alle Zeichen im String durch
    for currentChar in input:

        # Wenn Zeichen übereinstimmen:
        if currentChar == lastChar:
            # Erhöhe Zähler
            cCount += 1
        else:
            # Anzahl + Zeichen an Ausgabestring schreiben
            output += str(cCount) + lastChar

            # Zeichenzähler zurücksetzen
            cCount = 1

        # Letztes Zeichen aktualisieren
        lastChar = currentChar

    # Letztes Zeichen aktualisieren
    output += str(cCount) + lastChar

    return output

# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
def setup():
    bwImageStringA = "WWWWBBBWBBBBBBWW"  # compressed: "4W3B1W6B2W"
    bwImageStringB = "BBBBWWWWWWWWWB"    # compressed: "4B9W1B"
    bwImageStringC = "WBBBBWWWWWWB"      # compressed: "1W4B6W1B"

    print simpleCompression(bwImageStringA)
    print simpleCompression(bwImageStringB)
    print simpleCompression(bwImageStringC)

