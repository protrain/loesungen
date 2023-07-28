# Funktion, welche prüft, ob wir es bei zwei aufeinander
# folgenden Tageszahlen mit einem neuen Monat zu tun haben.
def is_new_month(day_now, day_previous):
    if day_now < day_previous:
        # Bei einem aufeinanderfolgenden Tag ist der aktuelle
        # Tag nicht kleiner als der vorherige, außer wir haben
        # es mit einem neuen Monat zu tun (wie hier der Fall).
        return True

    return False


# Funktion, welche die Durchschnittstemperatur berechnet. Als
# Eingabe wird ein Array mit den Tagen und ein Array mit den
# zugehörigen Temperaturen übergeben.
def get_monthly_average_temp(days, temps):
    if len(days) != len(temps):
        # Beide Arrays sind nicht gleich groß, daher können wir
        # keine Berechnung durchführen
        return None

    # Ausgabearray mit den Durchschnittstemperaturen
    monthly_average_temps = []
    # Aktueller Monat im Array
    current_month = 0

    # Summe der aktuell gesammelten Temperaturen
    temp_sum = 0.0

    # Anzahl der aktuell gesammelten Temperaturen
    temps_count = 0

    day_previous = 0

    # Gehe beide Arrays durch
    for i in range(0, len(days)):
        # Hole Tag und Temperatur
        day = days[i]
        temp = temps[i]
            
        # Wenn wir einen neuen Monat haben, dann berechnen wir die
        # Durchschnittswerte und speichern sie in den Ausgabearray
        if is_new_month(day, day_previous):
            temp_average = temp_sum / temps_count
            monthly_average_temps.append(temp_average)
                    
            # Setze die Zähler zurück
            temps_count = 0
            temp_sum = 0.0
            
            # Wir sind jetzt im neuen Monat
            current_month += 1
            
            # Abbruch, wenn wir über 12 Monate sind
            if current_month > 12:
                break
    
        # Addiere die Temperaturen auf, aber erst nachdem wir die
        # Tageszahl geprüft haben
        temp_sum += temp
        temps_count += 1
        
        # Wir speichern vorherigen Tag für die
        # nächste Iteration
        day_previous = day

    # Berechne noch den Durchschnitt für die letzte Iteration,
    # sofern noch nicht geschehen
    if temps_count > 0:
        temp_average = temp_sum / temps_count
        monthly_average_temps.append(temp_average)

    return monthly_average_temps


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    days_a =  [1, 2, 7, 13, 14, 15, 21, 28, 31, 1, 2, 3, 4, 5]
    temps_a = [11.1, 11.2, 13.3, 15.1, 15.2, 15.3, 16.7, 17.1]
    temps_a += [18.9, 17.1, 17.0, 16.9, 17.0, 16.9]

    print(get_monthly_average_temp(days_a, temps_a))

    days_b =  [1, 2, 7, 14, 21, 28, 1, 2, 5]
    temps_b = [11, 11, 11, 11, 11, 11, 5, 11, 11]

    print(get_monthly_average_temp(days_b, temps_b))


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
