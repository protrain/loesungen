size(800, 800)
noStroke()

# Soll aktueller Kasten schwarz sein?
black = True

# Größe pro Feldelement
size = 100

# Gehe jede Spalte durch
for y in range(0, height / size):
    # Gehe jede Zeile durch
    for x in range(0, width / size):
        # Male Farbe abhängig von Variable
        if black:
            # setze Farbe auf Schwarz
            fill(0)
        else:
            # setze Farbe auf Weiß
            fill(255)

        # Kehre Variable um
        if black:
            black = False
        else:
            black = True

        # Male Element
        rect(0, 0, size, size)

        # "Wandere" ein Feld nach rechts
        translate(size, 0)

    # Ende der Zeile erreicht
    # "Wandere" in nächste Zeile
    translate(-width, size)

    # Kehre Variable nochmals um, da Muster
    # immer mit letzter Farbe anfängt
    if black:
        black = False
    else:
        black = True

