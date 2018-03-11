# Funktion zur Generierung der IBAN-Prüfziffer
# Die IBAN wird als String übergeben. Als Ergebnis
# wird die IBAN inklusive Prüfziffer als String
# zurückgegeben
def generateIBANChecksum(bigNum):
    # Berechne die Prüfziffer, indem die Nummer modulo 97
    # gerechnet wird.
    checksum = bigNum % 97

    # Subtrahiere von 98
    checksum = 98 - checksum
    # Ist Resultat kleiner 10, füge 0 voran
    if(checksum < 10):
        return "0" + str(checksum)
    # ansonsten gib das Resultat zurück
    else:
        return str(checksum)

# Funktion zum Generieren der IBAN
# Die Kontonummer und Bankleitzahl werden als Strings an die
# Funktion übergeben. Das Ergebnis wird als String
# zurückgegeben.
def generateGermanIBAN(kontonummer, blz):
    # Wandle Strings in große Zahl um
    bigNum = int(blz + kontonummer + "131400")

    # Generiere Checksumme, indem zunächst ein String, bestehend
    # aus Bankleitzahl, Kontonummer sowie der Zeichenfolge "131400",
    # aneinandergehängt werden, bevor die Prüfziffer hierfür
    # berechnet wird
    checksum = generateIBANChecksum(bigNum)

    # Gebe IBAN-Nummer zurück
    return "DE" + str(checksum) + str(blz) + str(kontonummer)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print generateGermanIBAN("1234567890", "70090100")

