# Funktion zum Einlesen eines Telefonbuchs in Form einer CSV-Datei
# Als Parameter wird die Angabe des Pfades zur Datei an die Funktion
# übergeben. Diese liefert den Inhalt der Datei als String-Array zurück.
def readPhonebook(filename):
    phonebook = loadStrings(filename)
    output = []

    # Telefonbuch einlesen
    for entry in phonebook:
        # Trenne CSV-Einträge
        entryArray = split(entry)

        # Ergänze Festnetznummer, wenn erste Ziffer = "0"

        # Wurde eine Nummer angegeben
        if entryArray[2] != '':
            # Beginnt die Nummer mit einer '0'
            if entryArray[2][0] == '0':
                # Tauschen
                entryArray[2] = '+49' + entryArray[2][1:]

        # Ergänze Handynummer, wenn erste Nummer "0"

        # Wurde eine Nummer angegeben
        if entryArray[3] != '':
            # Beginnt die Nummer mit einer '0'
            if entryArray[3][0] == '0':
                # Tauschen
                entryArray[3] = '+49' + entryArray[3][1:]

        # Füge Array an Ausgabe an
        output = output + [entryArray]

    return combine(output)

# Funktion zum Zerteilen eines Eingabestrings, der an
# die Funktion übergeben wird. Als Ergebnis wird ein
# Array mit den Teilstrings zurückgegeben.
def split(input):
    stringLength = len(input)
    output = []
    word = ""  # Aktueller ausgelesener String (bis Semikolon)

    for i in range(0, stringLength):
        # Semikolon entdeckt oder Ende des Strings
        if input[i] == ";":
            # Füge Wort hinzu
            output = output + [word]
            # Lösche aktuelles Wort
            word = ""
        # Letztes Element im String -> Wort ergänzen + hinzufügen
        elif i == stringLength - 1:
            word = word + input[i]
            output = output + [word]
        # Sonst String um aktuellen Character ergänzen
        else:
            word = word + input[i]

    return output

# Funktion zum Zusammensetzen eines zweidimensionalen Arrays
# zurück in ein String-Array mit kommaseparierten Werten


def combine(inputArray):
    output = []

    # Gehe jede Zeile durch
    for element in inputArray:
        # Erstes Element bereits übernehmen
        row = element[0]

        # Zähler für aktuelle Spalte
        # Jedes Element in der Zeile durchgehen
        for i in range(1, len(element)):
            row = row + ";" + element[i]
        output = output + [row]

    return output


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.

# Array ausgeben. Datei telefonbuch.csv im Projektordner wird
# dabei eingelesen.
phonebook = readPhonebook("telefonbuch.csv")
for element in phonebook:
    print element



