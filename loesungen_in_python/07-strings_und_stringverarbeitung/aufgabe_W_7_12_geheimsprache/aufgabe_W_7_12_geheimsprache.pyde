# Statische Funktion zum Überführen eines englischen
# Texts in eine Geheimsprache. Der Text wird an die
# Funktion übergeben, und das überführte Ergebnis wird
# am Ende von der Funktion zurückgeliefert.
def pigLatin(text):
    # Packe jedes Wort in ein Array-Element
    words = text.split(" ")

    # Temporärer String zur Verarbeitung
    temp = ""

    # Jedes Wort durchgehen
    for word in words:
        # übernehme Wort ab dem 2. Buchstaben
        temp += word[1:]

        # Setze 1. Buchstaben ans Ende
        temp += word[0]

        # Füge "ay" hinzu
        temp += "ay "

    # Gebe Satz ohne letztes Leerzeichen zurück
    return temp[0:len(temp) - 1]


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print pigLatin("hello world")

