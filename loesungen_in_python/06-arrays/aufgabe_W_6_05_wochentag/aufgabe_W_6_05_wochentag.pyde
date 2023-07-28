# Funktion zur Berechnung des Wochentags
# Erhält als Eingabeparameter ganzzahlige Werte für
# den Tag, den Montag und das Jahr
def calc_day_of_week(input_day, input_month, input_year):
    # Letzte zwei Ziffern bestimmen, indem der Modulo-Operator ein-
    # gesetzt wird, um den Rest zu berechnen.
    day_of_week = input_year % 100

    # Ganzzahliger Anteil eines Viertels dazu addieren
    # Das Ergebnis einer Division mit Integer-Zahlen liefert
    # den ganzzahligen Wert der Division.
    day_of_week = day_of_week + int(day_of_week / 4)

    # Zuweisung Additionswerte für Monat
    month_add = {1: 1,
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
    day_of_week = day_of_week + month_add[input_month]

    # Tag addieren
    day_of_week = day_of_week + input_day

    # Zuweisung Jahrzehnt zu Offset
    century_add = {18: 2,
                   19: 0,
                   20: 6,
                   21: 4}

    # Addiere Offset
    century = int(input_year / 100)
    day_of_week = day_of_week + century_add[century]

    # Bei Schaltjahr wird für Januar und Februar 1 subtrahiert
    if check_leap_year(input_year):
        if input_month == 1 or input_month == 2:
            day_of_week -= 1

    # Wochentag ergibt sich aus Reduzieren Modulo 7
    day_of_week = day_of_week % 7

    # Array mit Wochentagen
    day_of_week_names = ["Samstag", "Sonntag", "Montag",
                         "Dienstag", "Mittwoch", "Donnerstag",
                         "Freitag"]

    # gebe Wochentag aus
    print(day_of_week_names[day_of_week])


# Funktion zur Schaltjahrprüfung (aus vorheriger Aufgabe)
def check_leap_year(year_input):
    # Ist Jahreszahl durch 400 teilbar?
    if year_input % 400 == 0:
        return True
    # sonst prüfe, ob Jahreszahl durch 4, aber nicht durch 100
    # teilbar ist
    elif year_input % 4 == 0 and year_input % 100 != 0:
        return True
    # Wenn keine Bedingung zutrifft
    else:
        return False


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu Demonstrations- und
# Testzwecken aufgerufen.
calc_day_of_week(1, 1, 1817)
