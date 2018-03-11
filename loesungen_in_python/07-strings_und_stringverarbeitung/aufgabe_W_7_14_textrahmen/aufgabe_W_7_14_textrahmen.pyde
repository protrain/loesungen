# Funktion zum Erzeugen eines umrahmten Texts.
# Die Funktion erhält den Text zeilenweise als Array
# vom Typ String. Der fertig gerahmte Text wird auf
# der Konsole ausgegeben.
def frameWordlist(wl):
    # Textzeile für Ausgabe
    output = ""

    # Maximale Textbreite
    maxWidth = 0

    # Bestimme maximale Textbreite
    # Gehe alle Wörter durch
    for word in wl:
        # Wenn die Länge des Wortes größer als bisheriges Maximum
        # ist, dann überschreiben
        if len(word) > maxWidth:
            maxWidth = len(word)

    # Schreibe oberen Rahmen
    # 2 Sternchen + 2 Leerzeichen länger als maximale Wortlänge
    for i in range(0, maxWidth + 4):
        output += "*"
    print output
    output = ""

    # Textzeilen
    # Gehe jedes Wort durch
    for word in wl:
        output += "* "
        output += word
        # Schreibe restliche Leerzeichen, je nach Wortlänge
        for j in range(0, maxWidth - len(word)):
            output += " "
        print output + " *"
        output = ""

    # Schreibe unteren Rahmenrand
    for i in range(0, maxWidth + 4):
        output += "*"
    print output
    output = ""


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
def setup():
    test = ["Rahmen", "sind", "toll!"]
    frameWordlist(test)

