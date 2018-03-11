# Funktion zur Berechnung des Wochentags
# Erhält als Eingabeparameter ganzzahlige Werte für
# den Tag, den Montag und das Jahr
def calcDayOfWeek(inputDay, inputMonth, inputYear):
    # Letzte zwei Ziffern bestimmen, indem der Modulo-Operator ein-
    # gesetzt wird, um den Rest zu berechnen.
    dayOfWeek = inputYear % 100

    # Ganzzahliger Anteil eines Viertels dazu addieren
    # Das Ergebnis einer Division mit Integer-Zahlen liefert
    # den ganzzahligen Wert der Division.
    dayOfWeek = dayOfWeek + (dayOfWeek / 4)

    # Zuweisung Additionswerte für Monat
    monthAdd = {1: 1,
                2: 4,
                3: 4,
                4: 0,
                5: 2,
                6: 5,
                7: 0,
                8: 3,
                9: 6,
                10: 1,
                11: 4,
                12: 6}

    # Werte entsprechend des Monats addieren
    dayOfWeek = dayOfWeek + monthAdd[inputMonth]

    # Tag addieren
    dayOfWeek = dayOfWeek + inputDay

    # Zuweisung Jahrzehnt zu Offset
    centuryAdd = {18: 2,
                  19: 0,
                  20: 6,
                  21: 4}

    # Addiere Offset
    century = inputYear / 100
    dayOfWeek = dayOfWeek + centuryAdd[century]

    # Bei Schaltjahr wird für Januar und Februar 1 subtrahiert
    if checkLeapYear(inputYear):
        if inputMonth == 1 or inputMonth == 2:
            dayOfWeek -= 1

    # Wochentag ergibt sich aus Reduzieren Modulo 7
    dayOfWeek = dayOfWeek % 7

    # Array mit Wochentagen
    dayOfWeekNames = ["Samstag", "Sonntag", "Montag",
                      "Dienstag", "Mittwoch", "Donnerstag",
                      "Freitag"]

    # gebe Wochentag aus
    print dayOfWeekNames[dayOfWeek]

# Funktion zur Schaltjahrprüfung (aus vorheriger Aufgabe)
def checkLeapYear(yearInput):
    # Ist Jahreszahl durch 400 teilbar?
    if yearInput % 400 == 0:
        return True
    # sonst prüfe, ob Jahreszahl durch 4, aber nicht durch 100
    # teilbar ist
    elif yearInput % 4 == 0 and yearInput % 100 != 0:
        return True
    # Wenn keine Bedingung zutrifft
    else:
        return False


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.

calcDayOfWeek(1, 1, 1817)

