# Bei der Ausführung in einer reinen Python-Umgebung, kann die
# folgende Funktion die Processing-Funktion loadStrings ersetzen
#def load_strings(filename):
#    with open(filename, mode="r", encoding="utf-8", ) as f:
#        return f.read().splitlines()

# Klasse, welche die Autovervollständigung realisiert
class AutoCompletion:
    
    # Konstruktor, welcher den Suchindex generiert
    def __init__(self):
        # Dictionary, welche wir für die Postleitzahlsuche nutzen
        self.search_idx = {}
        self.generate_search_index()
    
    # Private Funktion, welche den Suchindex der
    # Postleitzahlen generiert
    def generate_search_index(self):    
        # Lade CSV-Datei mit allen Postleitzahlen und Städten
        zip_city_csv = loadStrings("zip_city_de.csv")
        
        # Gehe jeden Eintrag einzeln durch
        header_removed = False
        for csv_line in zip_city_csv:
            if header_removed == False:
                # Wir ignorieren die erste Zeile der CSV-Datei
                header_removed = True
                continue
            
            # Trenne PLZ und Stadt
            line_split = csv_line.split(";")
            plz = line_split[0]
            city = line_split[1]
            
            # Füge Zuordnung zu Suchindex hinzu
            self.add_to_search_index(plz, city)
    
  # Private Funktion, welche eine PLZ-Stadt-Zuordnung dem
  # Suchindex hinzufügt
    def add_to_search_index(self, plz, city):
        if len(plz) > 1:
            # Füge für alle Variationen der PLZ hinzu
            plz_search_query = ""
            for i in range(0, len(plz)):
                # Generiere Variation
                plz_search_query = plz[:i]
                
                # Wenn Suchergebnis noch nicht existiert
                if plz_search_query not in self.search_idx:
                    # Generiere Suchergebnis neu
                    self.search_idx[plz_search_query] = []      
                    
                # Füge Suchbegriff zu Index hinzu
                self.search_idx[plz_search_query].append((plz, city))
            
    # Funktion, welche die Suchergebnisse für einen Such-
    # begriff zurückgibt
    def print_search_results(self, search_query):
        if search_query not in self.search_idx:
            print("Kein Suchergebnis")
            return
            
        # Hole Ergebnisse für Suchbegriff
        search_result = self.search_idx[search_query]
        
        # Gehe alle Suchergebnisse durch
        for plz, city in search_result:
            # Gebe Ergebnis aus
            print("{}: {}".format(plz, city))
            
# Startpunkt des Hauptprogramms
# Hier wird die implementierte Funktion zu
# Demonstrations- und Testzwecken aufgerufen.
def setup():
    ac = AutoCompletion()
    
    ac.print_search_results("324")
    print("")
    ac.print_search_results("6666")
    print("")
    ac.print_search_results("plz")
    print("")
    ac.print_search_results("12345")


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
