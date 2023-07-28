# Funktion zur Prüfung, ob ein angegebenen Jahr ein Schaltjahr ist
# Die Funktion erhält die Jahreszahl als Integer-Wert und gibt
# einen Wahrheitswert {True || False} als Ergebnis zurück.
def check_leap_year(year_input):
    if year_input % 400 == 0:  # Jahreszahl glatt durch 400 teilbar?
        return True       # Rückgabe: es ist ein Schaltjahr!

        # sonst prüfe, ob Jahreszahl glatt durch 4, aber nicht durch
        # 100 teilbar
    elif year_input % 4 == 0 and year_input % 100 != 0:
        return True

    # ansonsten Rückgabe: kein Schaltjahr!
    else:
        return False


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print("War 1800 ein Schaltjahr? -> " + str(check_leap_year(1800)))
print("War 2016 ein Schaltjahr? -> " + str(check_leap_year(2016)))
print("Wird 2020 ein Schaltjahr sein? -> " + str(check_leap_year(2020)))
