# Funktion zur Überprüfung eines Strings auf eine gültige
# E-Mail-Adresse. Die Funktion erhält die E-Mail-Adresse und
# liefert als Ergebnis einen Wahrheitswert zurück.
def isEmail(email):
    stage = 0
    cCount = 0              # gezählte Characters im Bereich

    # Gehe jedes Zeichen durch
    for c in email:
        if c == "@":
            # Nur erhöhen, wenn kein vorheriges @ erkannt wurde
            if stage == 0 and cCount > 0:
                stage = 1
                cCount = 0
            else:
                # Sonst ungültige Mail-Adresse
                return False
        elif c == ".":
            # Nur erhöhen, wenn bereits @ erkannt wurde
            if stage == 1 and cCount > 0:
                stage = 2
                cCount = 0
            else:
                # Sonst ungültige Mail-Adresse
                return False
        else:
            # Sonst Zeichenzähler erhöhen
            cCount += 1

    # Alle Zeichen durchgegangen
    # Endergebnis ist wahr, wenn Zeichen am Ende 2 oder 3 sind
    return cCount == 2 or cCount == 3


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print isEmail("john@doe.net")
print isEmail("john@doe.de")
print isEmail("john@doe.shop")
print isEmail("john@.net")
print isEmail("@.net")

