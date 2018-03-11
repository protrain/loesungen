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
    def addTemperature(self, month, value):
        # Nur arbeiten, wenn gültiger Monat angegeben wurde
        if month > 0 and month < 13:
            # Füge Temperatur hinzu
            self.__temperatures[month - 1] = value

    # Funktion zur Ausgabe des Graphen. Die Ausgabe erfolgt
    # direkt auf der Konsole.
    def plotGraph(self):
        # Nur arbeiten, wenn alle Monate ausgefüllt sind
        if self.__isComplete():
            # Hole minimale und maximale Temperaturwerte
            # zur Höhenbestimmung
            maxTemperature = self.__getMaxTemperature()
            minTemperature = self.__getMinTemperature()

            # Nutze i zum Temperaturvergleich und Balkenzeichnen.
            # Beginne mit höchster Temperatur (oberste Raute) bis
            # zur niedrigsten (unterster Balkenwert)
            for i in range(maxTemperature, minTemperature - 1, -1):
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
                print row

    # Methode zur Prüfung auf Vollzähligkeit der Werte
    # Als Ergebnis wird ein 'True' oder 'False' ausgegeben.
    def __isComplete(self):
        # Prüfe, ob alle Monatswerte über dem
        # Initialwert -1000 liegen
        for temperature in self.__temperatures:
            if temperature == -1000:
                return False

        return True

    # Methode zur Bestimmung und Rückgabe der maximalen
    # Temperatur
    def __getMaxTemperature(self):
        max = -1000
        # Gehe alle Monate durch.
        for temperature in self.__temperatures:
            # Liegt aktuelle Temperatur über dem aktuellen
            # Maximum, ist es das neue Maximum
            if temperature > max:
                max = temperature
        # Am Ende liegt das Maximum vor.
        return max

    # Methode zur Bestimmung und Rückgabe der minimalen
    # Temperatur
    def __getMinTemperature(self):
        # Wähle unrealistischen Startwert, der immer
        # unterboten werden kann.
        min = 1000
        # Gehe alle Monate durch
        for temperature in self.__temperatures:
            # Liegt aktuelle Temperatur über dem aktuellen
            # Minimum, ist es das neue Minimum.
            if temperature < min:
                min = temperature
        # Am Ende liegt das Minimum vor.
        return min


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Erzeuge Temperaturanzeige
tg = TemperatureGraph(2017)

# Füge Werte aus Beispiel hinzu
tg.addTemperature(1, 2)
tg.addTemperature(2, -3)
tg.addTemperature(3, 7)
tg.addTemperature(4, 8)
tg.addTemperature(5, 14)
tg.addTemperature(6, 16)
tg.addTemperature(7, 17)
tg.addTemperature(8, 18)
tg.addTemperature(9, 14)
tg.addTemperature(10, 9)
tg.addTemperature(11, 5)
tg.addTemperature(12, 2)

# Zeichne Graphen
tg.plotGraph()
