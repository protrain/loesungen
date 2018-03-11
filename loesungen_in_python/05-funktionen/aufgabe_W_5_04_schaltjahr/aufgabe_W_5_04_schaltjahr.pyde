# Funktion zur Prüfung, ob ein angegebenen Jahr ein Schaltjahr ist
# Die Funktion erhält die Jahreszahl als Integer-Wert und gibt
# einen Wahrheitswert {True || False} als Ergebnis zurück.
def checkLeapYear(yearInput):
    if yearInput % 400 == 0:  # Jahreszahl glatt durch 400 teilbar?
        return True   		# Rückgabe: es ist ein Schaltjahr!

        # sonst prüfe, ob Jahreszahl glatt durch 4, aber nicht durch
        # 100 teilbar
    elif yearInput % 4 == 0 and yearInput % 100 != 0:
        return True

    # ansonsten Rückgabe: kein Schaltjahr!
    else:
        return False


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

print "War 1800 ein Schaltjahr? -> " + str(checkLeapYear(1800))
print "War 2016 ein Schaltjahr? -> " + str(checkLeapYear(2016))
print "Wird 2020 ein Schaltjahr sein? -> " + str(checkLeapYear(2020))

