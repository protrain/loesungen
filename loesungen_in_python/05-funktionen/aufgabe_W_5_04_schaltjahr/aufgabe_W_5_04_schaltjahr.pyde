def check_leapyear(year):
    """ Funktion zur Prüfung, ob ein angegebenen Jahr ein Schaltjahr ist
    Die Funktion erhält die Jahreszahl als Integer-Wert und gibt
    einen Wahrheitswert {True || False} als Ergebnis zurück. """
    return (year % 4 == 0 # zuerst die Prüfung, die am stärksten diskriminiert
            and (year % 100 != 0 or year % 400 == 0)) # dann die Sonderfälle


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
print "War 1800 ein Schaltjahr? -> %s" % check_leapyear(1800)
print "War 2016 ein Schaltjahr? -> %s" % check_leapyear(2016)
print "Wird 2020 ein Schaltjahr sein? -> %s" % check_leapyear(2020)

