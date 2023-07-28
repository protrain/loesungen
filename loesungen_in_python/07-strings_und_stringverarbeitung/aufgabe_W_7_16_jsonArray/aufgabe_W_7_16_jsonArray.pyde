# Funktion zum Konvertieren eines JSON-Strings in ein
# Python-Array. Die Funktion erhält den JSON-String in der
# Übergabe und liefert das Ergebnis-Array zurück.
def to_string_array(json_array):
    string_array = []

    # Alle Leerzeichen entfernen
    json_array = json_array.replace(" ", "")

    # Sind wir gerade mitten in einem JSON-String?
    string_open = False

    word = ""

    # Gehe jedes Zeichen durch
    for c in json_array:
        # Sind wir jetzt bei einem Anführungsstrich
        if c == "'":
            # Waren wir in einem String, sind wir jetzt am Ende
            if string_open:
                # Füge hinzu
                string_array.append(word)

                # Word resetten
                word = ""
                string_open = False
            else:
                # Jetzt sind wir im JSON-String
                string_open = True

        # Ansonsten Zeichen hinzufügen, solange wir
        # im JSON-String sind
        elif string_open:
            word += c

    return string_array


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.

json_array = "[ 'Null', 'Eins', 'Zwei', 'Drei', 'Vier' ]"
string_array = to_string_array(json_array)

for element in string_array:
    print(element)
