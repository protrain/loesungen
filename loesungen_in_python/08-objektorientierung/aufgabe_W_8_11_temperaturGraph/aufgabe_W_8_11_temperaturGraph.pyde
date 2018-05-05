class TemperatureGraph:
    """ Klasse zur Realisierung eines Temperaturgraphen """

    def __init__(self, year):
        """ Initialisierer, der vorschreibt, dass Instanzen dieser
        Klasse nur mit Angabe der Jahreszahl generiert werden
        können. """
        self.year = year
        # Initialisiere alle Monate mit unmöglichen
        # Temperaturen (für Vollständigkeitscheck)
        self.temperatures = [None] * 12

    def add_temperature(self, month, value):
        """ Methode, die das Hinzufügen einer Temperatur in
        Verbindung mit dem Monat ermöglicht.
        Dazu werden Monat und Wert an die Methode übergeben. """

        # Nur arbeiten, wenn gültiger Monat angegeben wurde
        if 0 < month < 13:
            # Füge Temperatur hinzu
            self.temperatures[month - 1] = value

    def plot_graph(self):
        """ Funktion zur Ausgabe des Graphen. Die Ausgabe erfolgt
        direkt auf der Konsole. """
        # Nur arbeiten, wenn alle Monate ausgefüllt sind
        if self._is_complete():
            # Hole minimale und maximale Temperaturwerte
            # zur Höhenbestimmung
            max_temperature = max(self.temperature)
            min_temperature = min(self.temperature)

            # Nutze i zum Temperaturvergleich und Balkenzeichnen.
            # Beginne mit höchster Temperatur (oberste Raute) bis
            # zur niedrigsten (unterster Balkenwert)
            for i in range(max_temperature, min_temperature - 1, -1):
                # Gehe alle Monate durch
                row = ""
                for temperature in self.temperatures:
                    # Wenn Temperatur über den Vergleichswert,
                    # dann Balken zeichnen
                    if temperature >= i:
                        row += " #"
                    # Sonst nur Leerzeile zeichnen
                    else:
                        row += "  "
                # Nach Monatsvergleich Zeile ausgeben mit Zeilen-
                # umbruch für nächstniedrigere Temperaturstufe
                print row

    def _is_complete(self):
        """ Methode zur Prüfung auf Vollzähligkeit der Werte
        Als Ergebnis wird ein 'True' oder 'False' ausgegeben. """
        # Prüfe, ob alle Monatswerte nicht None sind
        for temperature in self.temperatures:
            if temperature is None:
                return False

        return True

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
