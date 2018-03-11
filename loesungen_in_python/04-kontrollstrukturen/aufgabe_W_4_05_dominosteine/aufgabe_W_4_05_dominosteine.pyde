for i in range(0, 7):
    row = ""

    # Erzeuge Leerzeichen
    for j in range(0, i):
        row += "     "

    # Füge Dominosteine hinzu
    for j in range(i, 7):
        row += "(" + str(i) + "|" + str(j) + ")"

    # Gebe Zeile mit Dominosteinen aus
    print row

