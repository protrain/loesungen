# Bei der Ausführung in einer reinen Python-Umgebung, kann die
# folgende Funktion die Processing-Funktion loadStrings ersetzen
# def load_strings(filename):
#     with open(filename, mode="r", encoding="utf-8", ) as f:
#         return f.read().splitlines()


# Funktion zum Einlesen eines Telefonbuchs in Form einer CSV-Datei
# Als Parameter wird die Angabe des Pfades zur Datei an die Funktion
# übergeben. Diese liefert den Inhalt der Datei als String-Array zurück.
def read_phonebook(filename):
    phonebook = loadStrings(filename)
    output = []

    # Telefonbuch einlesen
    for entry in phonebook:
        # Trenne CSV-Einträge
        entry_array = split(entry)

        # Ergänze Festnetznummer, wenn erste Ziffer = "0"

        # Wurde eine Nummer angegeben
        if entry_array[2] != '':
            # Beginnt die Nummer mit einer '0'
            if entry_array[2][0] == '0':
                # Tauschen
                entry_array[2] = '+49' + entry_array[2][1:]

        # Ergänze Handynummer, wenn erste Nummer "0"

        # Wurde eine Nummer angegeben
        if entry_array[3] != '':
            # Beginnt die Nummer mit einer '0'
            if entry_array[3][0] == '0':
                # Tauschen
                entry_array[3] = '+49' + entry_array[3][1:]

        # Füge Array an Ausgabe an
        output = output + [entry_array]

    return combine(output)


# Funktion zum Zerteilen eines Eingabestrings, der an
# die Funktion übergeben wird. Als Ergebnis wird ein
# Array mit den Teilstrings zurückgegeben.
def split(row_text):
    string_length = len(row_text)
    output = []
    word = ""  # Aktueller ausgelesener String (bis Semikolon)

    for i in range(0, string_length):
        # Semikolon entdeckt oder Ende des Strings
        if row_text[i] == ";":
            # Füge Wort hinzu
            output = output + [word]
            # Lösche aktuelles Wort
            word = ""
        # Letztes Element im String -> Wort ergänzen + hinzufügen
        elif i == string_length - 1:
            word = word + row_text[i]
            output = output + [word]
        # Sonst String um aktuellen Character ergänzen
        else:
            word = word + row_text[i]

    return output

# Funktion zum Zusammensetzen eines zweidimensionalen Arrays
# zurück in ein String-Array mit kommaseparierten Werten


def combine(input_array):
    output = []

    # Gehe jede Zeile durch
    for element in input_array:
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
phonebook = read_phonebook("telefonbuch.csv")
for elem in phonebook:
    print(elem)
