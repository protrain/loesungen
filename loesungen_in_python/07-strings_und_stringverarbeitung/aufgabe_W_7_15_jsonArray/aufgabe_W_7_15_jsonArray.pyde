# Funktion zum Konvertieren eines JSON-Strings in ein
# Python-Array. Die Funktion erhält den JSON-String in der
# Übergabe und liefert das Ergebnis-Array zurück.
def toStringArray(jsonArray):
    stringArray = []

    # Alle Leerzeichen entfernen
    jsonArray = jsonArray.replace(" ", "")

    # Sind wir gerade mitten in einem JSON-String?
    stringOpen = False

    word = ""

    # Gehe jedes Zeichen durch
    for c in jsonArray:
        # Sind wir jetzt bei einem Anführungsstrich
        if c == "'":
            # Waren wir in einem String, sind wir jetzt am Ende
            if stringOpen:
                # Füge hinzu
                stringArray.append(word)

                # Word resetten
                word = ""
                stringOpen = False
            else:
                # Jetzt sind wir im JSON-String
                stringOpen = True

        # Ansonsten Zeichen hinzufügen, solange wir
        # im JSON-String sind
        elif stringOpen:
            word += c

    return stringArray


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.

jsonArray = "[ 'Null', 'Eins', 'Zwei', 'Drei', 'Vier' ]"
stringArray = toStringArray(jsonArray)

for element in stringArray:
    print element

