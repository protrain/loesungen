# Funktion zum Konvertieren eines IMDB-Texteintrags
# in eine tabellarische String-Array-Darstellung.
# An die Funktion wird ein eindimensionales String-Array
# mit den zeilenweisen IMDB-Einträgen übergeben. Als
# Ergebnis wird ein zweidimensionales Array mit Zeilen und
# Spalten für die Einträge generiert und zurückgegeben.
def to_table(imdb_list):
    # Leere Tabelle erzeugen mit
    # so vielen Zeilen wie im Eingabe-Array und mit je drei Spalten
    # für die Werte <Score><Filmtitel>(<Erscheinungsjahr>)
    t = []

    # Jede Zeile der Liste durchgehen
    for s in imdb_list:
        # Leere Tabellenzeile erzeugen
        row = []

        # Inhalte auslesen
        # das erste Leerzeichen trennt <Score> und <Filmtitel>
        score = s[0:s.index(' ')]

        # Die letzten 7 Zeichen eines IMDB-Eintrags bestehen aus
        # Leerzeichen + (<Erscheinungsjahr). Damit können wir den
        # <Filmtitel> ausschneiden, wenn wir bedenken, dass der Titel
        # nach dem <Score> angegeben wird:
        title = s[s.index(' ') + 1:len(s) - 7]

        # Ausschneiden des <Erscheinungsjahrs> ohne Klammern. Da der
        # IMDB-String zuletzt aus der Jahreszahl und einer schließenden
        # Klammer besteht...
        year = s[len(s) - 5:len(s) - 1]

        # Reihen der Zeile hinzufügen
        row.append(score)
        row.append(title)
        row.append(year)

        # Zeile der Tabelle hinzufügen
        t.append(row)

    return t


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
liste = ["8.7 The Lord of the Rings: The Fellowship of the Ring (2001)"]
liste_converted = to_table(liste)

output = ""
for spalte in liste_converted:
    for element in spalte:
        output += element + "\t"

print(output)
