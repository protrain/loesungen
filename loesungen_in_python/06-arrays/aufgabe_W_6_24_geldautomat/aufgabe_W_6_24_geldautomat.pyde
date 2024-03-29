# Wir wollen 2305 Euro ausgeben
betrag = 2305

# Wir haben einen Kontostand von 500 Euro
kontostand = 5000

# Betrag muss größer als 0 Euro sein und darf maximal
# der Kontostand sein. Außerdem müssen wir den Beitrag in
# Fünf-Euro-Scheinen aufteilen können.
if betrag > 0 and betrag < kontostand and betrag % 5 == 0:
    # Liste der möglichen Scheinarten
    SCHEINE = [500, 200, 100, 50, 20, 10, 5]

    # Beitrag, den wir noch ausgeben müssen
    rest_betrag = betrag

    # Gehe alle Scheinarten durch
    for schein in SCHEINE:
        # Anzahl der Scheine, die wir für die aktuelle
        # Scheinart bekommen
        num_scheine = int(rest_betrag / schein)

        # Gebe die Anzahl der Scheine aus, wenn wir diese
        # Scheinart ausgeben können
        if num_scheine > 0:
            print('{}x{}'.format(num_scheine, schein))

        # Bestimme den Restbetrag, den wir mit der aktuellen
        # Scheinart nicht ausgeben konnten
        rest_betrag = rest_betrag % schein
