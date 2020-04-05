# Importiere die Kennzeichen
def importLicensePlates():
    # Lade CSV-Datei mit allen Kennzeichen
    licensePlatesCSV = loadStrings("kennzeichen.csv")

    # Erstelle daraus zweispaltiges Array
    licensePlates = []

    # Gehe alle Reihen der CSV-Datei durch
    for licensePlate in licensePlatesCSV:
        # Unterteile Semikolons in Array-Elements
        licensePlates.append(split(licensePlate, ";"))

    # Jetzt haben wir Liste mit allen KFZ-Kennzeichen importiert
    # Gebe diese Liste zurück
    return licensePlates

# Bestimme Stadt/Landkreis basierend auf dem Kennzeichen


def getLocation(identifier):
    # Extrahiere Ortskürzel aus Kennzeichen
    identifier = identifier.split("-")[0]

    # Importiere Liste der Autokennzeichen
    licensePlates = importLicensePlates()

    # Binäre Suche

    # Beginne bei gesamtem Array
    left = 0
    right = len(licensePlates) - 1

    # Wiederhole solange, bis wir alle Werte im Array abgesucht haben
    while left <= right:
        # Bilde die Mitte zwischen den Bereichen links und rechts
        middle = left + ((right - left) / 2)

        # Haben wir das richtige Kennzeichenkürzel in der Mitte?
        if licensePlates[middle][0] == identifier:
            # Gebe die Ortsbezeichnung zurück
            return licensePlates[middle][1]
        else:
            # Kennzeichen ist nicht in der Mitte, daher prüfen wir jetzt
            # anhand der Buchstaben, in welchem Bereich wir weitersuchen
            # sollten

            # Wenn das gesuchte Kennzeichen alphabetisch größer ist
            if identifier > licensePlates[middle][0]:
                # Suche rechts weiter
                left = middle + 1
            else:
                # Sonst auf der linken Seite
                right = middle - 1

    # Wir sind am Ende angekommen, also haben wir leider nichts
    # gefunden
    return "KENNZEICHEN NICHT GEFUNDEN"


print getLocation("K-TH-666")
print getLocation("AB-CD-123")
print getLocation("SRO-LI-7326")
print getLocation("NON-EX-157")
