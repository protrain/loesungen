# Setze das Geburtsdatum in Form von drei Integerzahlen
# (Tag, Monat, Jahr)
day = 21
month = 6
year = 1970

# Bestimme Sternzeichen
if month == 1:
    # Entweder Steinbock oder Wassermann
    if day < 20:
        print("Steinbock")
    else:
        print("Wassermann")
elif month == 2:
    # Entweder Wassermann oder Fische
    if day < 19:
        print("Wassermann")
    else:
        print("Fische")
elif month == 3:
     # Entweder Fische oder Widder
    if day < 21:
        print("Fische")
    else:
        print("Widder")
elif month == 4:
    # Entweder Widder oder Stier
    if day < 21:
        print("Widder")
    else:
        print("Stier")
elif month == 5:
    # Entweder Stier oder Zwillinge
    if day < 22:
        print("Stier")
    else:
        print("Zwillinge")
elif month == 6:
    # Entweder Zwillinge oder Krebs
    if day < 22:
        print("Zwillinge")
    else:
        print("Krebs")
elif month == 7:
    # Entweder Krebs oder Löwe
    if day < 23:
        print("Krebs")
    else:
        print("Löwe")
elif month == 8:
    # Entweder Löwe oder Jungfrau
    if day < 23:
        print("Löwe")
    else:
        print("Jungfrau")
elif month == 9:
    # Entweder Jungfrau oder Waage
    if day < 23:
        print("Jungfrau")
    else:
        print("Waage")
elif month == 10:
    # Entweder Waage oder Skorpion
    if day < 23:
        print("Waage")
    else:
        print("Skorpion")
elif month == 11:
    # Entweder Skorpion oder Schütze
    if day < 23:
        print("Skorpion")
    else:
        print("Schütze")
elif month == 12:
    # Entweder Schütze oder Steinbock
    if day < 21:
        print("Schütze")
    else:
        print("Steinbock")
else:
     print("Ungültig")
