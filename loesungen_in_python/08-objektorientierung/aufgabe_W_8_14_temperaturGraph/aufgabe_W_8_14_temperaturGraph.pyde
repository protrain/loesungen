# Klasse zur Realisierung eines Temperaturgraphen
class TemperatureGraph:

    # Konstruktor, der vorschreibt, dass Instanzen dieser
    # Klasse nur mit Angabe der Jahreszahl generiert werden
    # können.
    def __init__(self, year):
        self.__year = year
        self.__temperatures = []

        # Initialisiere alle Monate mit unmöglichen
        # Temperaturen (für Vollständigkeitscheck)
        for i in range(0, 12):
            self.__temperatures.append(-1000)

    # Methode, die das Hinzufügen einer Temperatur in
    # Verbindung mit dem Monat ermöglicht.
    # Dazu werden Monat und Wert an die Methode übergeben.
    def add_temperature(self, month, value):
        # Nur arbeiten, wenn gültiger Monat angegeben wurde
        if month > 0 and month < 13:
            # Füge Temperatur hinzu
            self.__temperatures[month - 1] = value

    # Funktion zur Ausgabe des Graphen. Die Ausgabe erfolgt
    # direkt auf der Konsole.
    def plot_graph(self):
        # Nur arbeiten, wenn alle Monate ausgefüllt sind
        if self.__is_complete():
            # Hole minimale und maxmale Temperaturwerte
            # zur Höhenbestimmung
            max_temp_temperature = self.__get_max_temperature()
            min_temp_temperature = self.__get_min_temperature()

            # Nutze i zum Temperaturvergleich und Balkenzeichnen.
            # Beginne mit höchster Temperatur (oberste Raute) bis
            # zur niedrigsten (unterster Balkenwert)
            for i in range(max_temp_temperature, min_temp_temperature - 1, -1):
                # Gehe alle Monate durch
                row = ""
                for j in range(0, len(self.__temperatures)):
                    # Wenn Temperatur über den Vergleichswert,
                    # dann Balken zeichnen
                    if self.__temperatures[j] >= i:
                        row += " #"
                    # Sonst nur Leerzeile zeichnen
                    else:
                        row += "  "
                # Nach Monatsvergleich Zeile ausgeben mit Zeilen-
                # umbruch für nächstniedrigere Temperaturstufe
                print(row)

    # Methode zur Prüfung auf Vollzähligkeit der Werte
    # Als Ergebnis wird ein 'True' oder 'False' ausgegeben.
    def __is_complete(self):
        # Prüfe, ob alle Monatswerte über dem
        # Initialwert -1000 liegen
        for temperature in self.__temperatures:
            if temperature == -1000:
                return False

        return True

    # Methode zur Bestimmung und Rückgabe der max_tempimalen
    # Temperatur
    def __get_max_temperature(self):
        max_temp = -1000
        # Gehe alle Monate durch.
        for temperature in self.__temperatures:
            # Liegt aktuelle Temperatur über dem aktuellen
            # Maximum, ist es das neue Maximum
            if temperature > max_temp:
                max_temp = temperature
        # Am Ende liegt das Maximum vor.
        return max_temp

    # Methode zur Bestimmung und Rückgabe der min_tempimalen
    # Temperatur
    def __get_min_temperature(self):
        # Wähle unrealistischen Startwert, der immer
        # unterboten werden kann.
        min_temp = 1000
        # Gehe alle Monate durch
        for temperature in self.__temperatures:
            # Liegt aktuelle Temperatur über dem aktuellen
            # Minimum, ist es das neue Minimum.
            if temperature < min_temp:
                min_temp = temperature
        # Am Ende liegt das Minimum vor.
        return min_temp


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Erzeuge Temperaturanzeige
tg = TemperatureGraph(2017)

# Füge Werte aus Beispiel hinzu
tg.add_temperature(1, 2)
tg.add_temperature(2, -3)
tg.add_temperature(3, 7)
tg.add_temperature(4, 8)
tg.add_temperature(5, 14)
tg.add_temperature(6, 16)
tg.add_temperature(7, 17)
tg.add_temperature(8, 18)
tg.add_temperature(9, 14)
tg.add_temperature(10, 9)
tg.add_temperature(11, 5)
tg.add_temperature(12, 2)

# Zeichne Graphen
tg.plot_graph()
