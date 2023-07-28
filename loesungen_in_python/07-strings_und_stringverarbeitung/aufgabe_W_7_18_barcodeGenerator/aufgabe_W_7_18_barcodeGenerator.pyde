size(400, 200)
stroke(0)
fill(0)
background(255, 255, 255)


# Funktion zum Zeichnen von Linien für ein übergebenes
# Ziffern-Array. Der Funktion wird die codierte String-
# sowie die Startkoordinate übergeben.
def draw_digit_lines(coding, start_x=20):
    # Variablen zum Zeichnen der Linien
    x = start_x
    y_1 = 10
    y_2 = 130
    line_width = 3           # Breite für eine Linie

    # Linienbreite festlegen
    strokeWeight(line_width)

    # Linientyp festlegen
    strokeCap(SQUARE)

    for code in coding:
        # Farbe setzen
        if code == 1:
            stroke(0)
        else:
            stroke(255)
        line(x, y_1, x, y_2)
        x = x + line_width   # Eine Linie weiterspringen


# Funktion, die eine codierte Nummer als Ziffern-Array zurück-
# gibt. Die Funktion erhält als Parameter den darzustellenden
# Zahlenwert sowie eine boolesche Variable für die Steuerung der
# Seitencodierung:
# leftside==true => linke Seite
# leftside==false => rechte Seite
def get_number_code(number, left_side=True):
    output = []
    # Generiere Nummern für rechte Seite
    if number == 0:
        output = [0, 0, 0, 1, 1, 0, 1]
    elif number == 1:
        output = [0, 0, 1, 1, 0, 0, 1]
    elif number == 2:
        output = [0, 0, 1, 0, 0, 1, 1]
    elif number == 3:
        output = [0, 1, 1, 1, 1, 0, 1]
    elif number == 4:
        output = [0, 1, 0, 0, 0, 1, 1]
    elif number == 5:
        output = [0, 1, 1, 0, 0, 0, 1]
    elif number == 6:
        output = [0, 1, 0, 1, 1, 1, 1]
    elif number == 7:
        output = [0, 1, 1, 1, 0, 1, 1]
    elif number == 8:
        output = [0, 1, 1, 0, 1, 1, 1]
    elif number == 9:
        output = [0, 0, 0, 1, 0, 1, 1]

    # Wenn für rechte Seite bestimmt, dann invertieren
    if not left_side:
        temp = []   # Temporärer Array

        # Gehe alle Array-Elemente durch
        for digit in output:
            if digit == 1:
                temp = temp + [0]
            else:
                temp = temp + [1]

        output = temp

    return output


# Funktion zum Generieren eines Barcodes aus 11 Ziffern.
# An die Funktion wird ein String mit den Nummern übergeben.
# Die Funktion liefert den Barcode als String zurück.
# Die Prüfziffer wird in der Funktion berechnet.
def get_barcode(numbers):
    quiet_zone = [0, 0, 0, 0, 0, 0, 0]
    start_end_pattern = [1, 0, 1]
    middle_pattern = [0, 1, 0, 1, 0]

    if len(numbers) != 11:
        print("Die angegebene Nummernfolge hat nicht genau 11 Zeichen.")
        print("Der Barcode ist daher nicht korrekt.")

    # Prüfziffer berechnen
    checksum = 0
    temp = 0
    for i in range(0, 10, 2):
        temp = temp + int(numbers[i])

    checksum = temp * 3
    temp = 0

    for i in range(1, 10, 2):
        temp = temp + int(numbers[i])

    checksum = checksum + temp
    checksum = checksum % 10

    if checksum > 0:
        checksum = 10 - checksum

    print("Code: " + numbers + str(checksum))

    # Generiere Barcode
    barcode = quiet_zone + start_end_pattern
    i = 1  # Anzahl bearbeiteter Ziffern
    left_side = True

    for number in numbers:
        if i == 12:
            break

        number = int(number)
        barcode = barcode + get_number_code(number, left_side)

        # Wenn an der Mitte angekommen, dann Mitte-Muster anfügen
        # und Codierung für rechte Seite aktivieren
        if i == 6:
            left_side = False
            barcode = barcode + middle_pattern

        i = i + 1

    # Zusammensetzen des Barcodes
    barcode = barcode + get_number_code(checksum, False)
    barcode += start_end_pattern + quiet_zone

    return barcode


# Funktion zum Zeichnen des Barcodes. Der Funktion wird
# die Nummer als String übergeben.
def draw_barcode(numbers):
    draw_digit_lines(get_barcode(numbers))


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
draw_barcode("98765432110")
