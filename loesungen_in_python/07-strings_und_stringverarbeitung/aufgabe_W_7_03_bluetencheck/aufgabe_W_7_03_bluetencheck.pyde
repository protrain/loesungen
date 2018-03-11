# Funktion, die die Position eines Buchstabens im Alphabet
# zurückliefert. An die Funktion wird der Buchstabe übergeben,
# für den die Position bestimmt und am Ende der Funktion
# zurückgeliefert wird.
def computeCheckDigit(serialnumber):
    letter = serialnumber[0]

    # Python-Dictionary zur Zuordnung von Buchstaben zu ihrer
    # Alphabetsposition
    letterPosition = {"A": 1,
                      "B": 2,
                      "C": 3,
                      "D": 4,
                      "E": 5,
                      "F": 6,
                      "G": 7,
                      "H": 8,
                      "I": 9,
                      "J": 10,
                      "K": 11,
                      "L": 12,
                      "M": 13,
                      "N": 14,
                      "O": 15,
                      "P": 16,
                      "Q": 17,
                      "R": 18,
                      "S": 19,
                      "T": 20,
                      "U": 21,
                      "V": 22,
                      "W": 23,
                      "X": 24,
                      "Y": 25,
                      "Z": 26,
                      }

    # Hole Position im lateinischen Alphabet
    posNumber = letterPosition[letter]

    # Berechne Summe
    sum = 0

    # Addiere Quersumme
    while posNumber != 0:
        sum = sum + posNumber % 10
        posNumber = posNumber / 10

    # Addiere restliche Ziffern
    # Wandle dabei die Ziffern in Integer-Werte um
    for i in range(1, 11):
        sum = sum + int(serialnumber[i])

    # Ganzzahligen Rest der Division durch 9 bestimmen (Modulo)
    rest = sum % 9

    # Berechne Prüfziffer
    # Subtrahiere Rest von 8
    checkDigit = 8 - rest

    # Wenn Ergebnis = 0, dann ist Prüfziffer = 9
    if rest == 0:
        checkDigit = 9

    return checkDigit

# Funktion, die die Prüfziffer einer Seriennummer
# eines Geldscheins zurückliefert. Die Seriennummer
# wird an die Funktion übergeben. Die Funktion liefert
# die Prüfziffer der Seriennummer zurück.
def getCheckDigit(serialnumber):
    return int(serialnumber[11])

# Funktion zur Überprüfung der Gültigkeit einer Seriennummer
# eines Geldscheins. Die Seriennummer wird als String an die
# Funktion übergeben und liefert einen Wahrheitswert zurück.
def isCheckDigitValid(serialnumber):
    return getCheckDigit(serialnumber) == computeCheckDigit(serialnumber)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print isCheckDigitValid("S00630387745")

