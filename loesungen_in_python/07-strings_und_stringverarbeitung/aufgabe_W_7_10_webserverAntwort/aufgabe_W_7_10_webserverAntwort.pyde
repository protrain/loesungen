# Funktion zum Filtern von Content-Type- und Content-Length-Werten
# in einer Webserver-Status-Nachricht. Die Status-Nachricht wird in
# einem String-Array an die Funktion übergeben und liefert die
# relevanten Informationen zurück.
def filterContentHeader(responses):
    type = None
    length = None

    # Gehe jede Response-Zeile durch
    for element in responses:
        # Trenne String nach Zeichenkette ": " in einzelne
        # Array-Elemente auf
        temp = element.split(": ")

        # Springe zu nächster For-Iteration, wenn mehr als 2x ": " in
        # einer Zeile (dann kann nichts gefunden werden)
        if len(temp) != 2:
            continue

        # Setze Variablen nach Werten
        # Springe aus Schleife, wenn beide Werte schon gesetzt sind
        if type is not None and length is not None:
            break
            # Setze Content-Type, wenn Wert in Zeile ist
        elif temp[0].lower() == "Content-Type".lower():
            type = temp[1]
            # Setze Content-Length, wenn Wert in Zeile ist
        elif temp[0].lower() == "Content-Length".lower():
            length = temp[1]

    # Erzeuge Ausgabe
    if type is not None and length is not None:
        return "The response contains: " + type + " (" + length + ")"
    else:
        return "The response does not contain any content."


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Stringverarbeitungsfunktion zu
# Demonstrations- und Testzwecken aufgerufen.
header = ["HTTP/1.1 200 OK",
          "Server: Apache",
          "Content-Length: 14188",
          "Connection: close",
          "Content-Type: image/jpg",
          "..."]
print filterContentHeader(header)

