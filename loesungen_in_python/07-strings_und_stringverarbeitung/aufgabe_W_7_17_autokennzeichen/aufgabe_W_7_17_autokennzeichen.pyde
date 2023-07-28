# Bei der Ausführung in einer reinen Python-Umgebung, kann die
# folgende Funktion die Processing-Funktion loadStrings ersetzen
# def load_strings(filename):
#     with open(filename, mode="r", encoding="utf-8", ) as f:
#         return f.read().splitlines()


# Importiere die Kennzeichen
def import_license_plates():
    # Lade CSV-Datei mit allen Kennzeichen
    license_plates_csv = loadStrings("kennzeichen.csv") 

    # Erstelle daraus zweispaltiges Array
    license_plates = []

    # Gehe alle Reihen der CSV-Datei durch
    for license_plate in license_plates_csv:
        # Unterteile Semikolons in Array-Elements
        license_plates.append(license_plate.split(";"))
            #split(license_plate, ";"))

    # Jetzt haben wir Liste mit allen KFZ-Kennzeichen importiert
    # Gebe diese Liste zurück
    return license_plates


# Bestimme Stadt/Landkreis basierend auf dem Kennzeichen
def get_location(identifier):
    # Extrahiere Ortskürzel aus Kennzeichen
    identifier = identifier.split("-")[0]

    # Importiere Liste der Autokennzeichen
    license_plates = import_license_plates()

    # Binäre Suche
    # Beginne bei gesamtem Array
    left = 0
    right = len(license_plates) - 1

    # Wiederhole solange, bis wir alle Werte im Array abgesucht haben
    while left <= right:
        # Bilde die Mitte zwischen den Bereichen links und rechts
        middle = left + int((right - left) / 2)

        # Haben wir das richtige Kennzeichenkürzel in der Mitte?
        if license_plates[middle][0] == identifier:
            # Gebe die Ortsbezeichnung zurück
            return license_plates[middle][1]
        else:
            # Kennzeichen ist nicht in der Mitte, daher prüfen wir jetzt
            # anhand der Buchstaben, in welchem Bereich wir weitersuchen
            # sollten

            # Wenn das gesuchte Kennzeichen alphabetisch größer ist
            if identifier > license_plates[middle][0]:
                # Suche rechts weiter
                left = middle + 1
            else:
                # Sonst auf der linken Seite
                right = middle - 1

    # Wir sind am Ende angekommen, also haben wir leider nichts
    # gefunden
    return "KENNZEICHEN NICHT GEFUNDEN"


print(get_location("K-TH-666"))
print(get_location("AB-CD-123"))
print(get_location("SRO-LI-7326"))
print(get_location("NON-EX-157"))
