# Funktion prüft, ob ein als String übergebenes Passwort
# die Regeln für ein starkes Passwort erfüllt. Die Funktion
# gibt einen Wahrheitswert mit dem Ergebnis der Prüfung zurück.
def is_strong(password):
    # Enthält mindestens acht Zeichen
    if len(password) < 8:
        return False

    # Zähle einzelne Zeichentypen
    lowercase = 0
    uppercase = 0
    number = 0
    special = 0

    # Gehe String durch
    for c in password:
        # Bestimme Character-Code
        char_code = char_to_number(c)

        # ist ein Kleinbuchstabe
        if char_code >= char_to_number(
                "a") and char_code <= char_to_number("z"):
            lowercase += 1

        # ist ein Großbuchstabe
        elif (char_code >= char_to_number("A") and
              char_code <= char_to_number("Z")):
            uppercase += 1

        # ist eine Ziffer
        elif (char_code >= char_to_number("0") and
              char_code <= char_to_number("9")):
            number += 1

        # ist ein Sonderzeichen (! oder *)
        elif (char_code == char_to_number("!") or
              char_code == char_to_number("*")):
            special += 1

    # Sind alle Zeichen gezählt, werte aus
    # Gebe True zurück, wenn alle Bedingungen erfüllt sind
    if lowercase > 0 and uppercase > 0 and number > 0 and special > 0:
        return True
    else:
        return False


# Funktion zum Konvertieren eines Buchstabens in Character-Code. Die
# Funktion erhält das Zeichen, für den der Code zurückgeliefert wird.
def char_to_number(c):
    return ord(c)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print(is_strong("eVJo2!8IrRo"))
print(is_strong("aH6*LauTp21u"))
print(is_strong("o1hKeaZG*!o"))
print(is_strong("Passwort123"))
print(is_strong("!2Bcv"))
