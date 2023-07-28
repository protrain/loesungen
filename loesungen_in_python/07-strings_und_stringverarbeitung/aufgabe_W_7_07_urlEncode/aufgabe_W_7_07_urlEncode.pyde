# Funktion zum Durchführen eines URL-Encodings.
# An die Funktion wird der Originalstring eingegeben.
# Der konvertierte String wird von der Funktion
# zurückgeliefert.
def url_encode(s):
    encoded = ""

    # Alle Zeichen im String durchgehen
    for c in s:
        # Schreibe Zeichen in Ausgabestring
        if c == ' ':
            encoded += "%20"
        elif c == '*':
            encoded += "%2A"
        elif c == '+':
            encoded += "%2B"
        elif c == ',':
            encoded += "%2C"
        elif c == '/':
            encoded += "%2F"
        elif c == ':':
            encoded += "%3A"
        elif c == '':
            encoded += "%3B"
        elif c == '=':
            encoded += "%3D"
        elif c == '?':
            encoded += "%3F"
        else:
            encoded += c

    return encoded


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
print(url_encode("http://www.hanser-fachbuch.de/buch/"
                 + "WebSockets/9783446443716"))
