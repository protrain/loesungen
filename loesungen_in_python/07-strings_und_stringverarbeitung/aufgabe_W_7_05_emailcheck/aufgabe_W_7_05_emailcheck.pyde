# Funktion zur Überprüfung eines Strings auf eine gültige
# E-Mail-Adresse. Die Funktion erhält die E-Mail-Adresse und
# liefert als Ergebnis einen Wahrheitswert zurück.
def is_email(email):
    stage = 0
    c_count = 0              # gezählte Characters im Bereich

    # Gehe jedes Zeichen durch
    for c in email:
        if c == "@":
            # Nur erhöhen, wenn kein vorheriges @ erkannt wurde
            if stage == 0 and c_count > 0:
                stage = 1
                c_count = 0
            else:
                # Sonst ungültige Mail-Adresse
                return False
        elif c == ".":
            # Nur erhöhen, wenn bereits @ erkannt wurde
            if stage == 1 and c_count > 0:
                stage = 2
                c_count = 0
            else:
                # Sonst ungültige Mail-Adresse
                return False
        else:
            # Sonst Zeichenzähler erhöhen
            c_count += 1

    # Alle Zeichen durchgegangen
    # Endergebnis ist wahr, wenn Zeichen am Ende 2 oder 3 sind
    return c_count in (2, 3)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print(is_email("john@doe.net"))
print(is_email("john@doe.de"))
print(is_email("john@doe.shop"))
print(is_email("john@.net"))
print(is_email("@.net"))
