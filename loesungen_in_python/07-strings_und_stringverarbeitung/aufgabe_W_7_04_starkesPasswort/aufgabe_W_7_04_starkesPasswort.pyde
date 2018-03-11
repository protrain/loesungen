# Funktion prüft, ob ein als String übergebenes Passwort
# die Regeln für ein starkes Passwort erfüllt. Die Funktion
# gibt einen Wahrheitswert mit dem Ergebnis der Prüfung zurück.
def isStrong(password):
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
        charCode = charToNumber(c)

        # ist ein Kleinbuchstabe
        if charCode >= charToNumber(
                "a") and charCode <= charToNumber("z"):
            lowercase += 1

        # ist ein Großbuchstabe
        elif charCode >= charToNumber("A") and charCode <= charToNumber("Z"):
            uppercase += 1

        # ist eine Ziffer
        elif charCode >= charToNumber("0") and charCode <= charToNumber("9"):
            number += 1

        # ist ein Sonderzeichen (! oder *)
        elif charCode == charToNumber("!") or charCode == charToNumber("*"):
            special += 1

    # Sind alle Zeichen gezählt, werte aus
    # Gebe True zurück, wenn alle Bedingungen erfüllt sind
    if lowercase > 0 and uppercase > 0 and number > 0 and special > 0:
        return True
    else:
        return False


# Funktion zum Konvertieren eines Buchstabens in Character-Code. Die
# Funktion erhält das Zeichen, für den der Code zurückgeliefert wird.
def charToNumber(c):
    return unhex(hex(c))


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print isStrong("eVJo2!8IrRo")
print isStrong("aH6*LauTp21u")
print isStrong("o1hKeaZG*!o")
print isStrong("Passwort123")
print isStrong("!2Bcv")

