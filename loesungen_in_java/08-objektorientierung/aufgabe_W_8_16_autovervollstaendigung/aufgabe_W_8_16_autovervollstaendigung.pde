// Klasse, welche die Autovervollständigung realisiert
class AutoCompletion {
  // HashMap, welche wir für die Postleitzahlsuche nutzen
  private HashMap<String, HashMap<String, String>> searchIndex;
  
  // Konstruktor, welcher den Suchindex generiert
  public AutoCompletion() {
    this.generateSearchIndex();
  }
  
  // Private Funktion, welche den Suchindex der
  // Postleitzahlen generiert
  private void generateSearchIndex() {
    this.searchIndex =
      new HashMap<String, HashMap<String, String>>();
    
    // Lade CSV-Datei mit allen Postleitzahlen und Städten
    String[] zipCityCSV = loadStrings("zip_city_de.csv");

    // Gehe jeden Eintrag einzeln durch
    boolean headerRemoved = false;
    for (String line : zipCityCSV) {
      if (headerRemoved == false) {
        // Wir ignorieren die erste Zeile der CSV-Datei
        headerRemoved = true;
        continue;
      }
      
      // Trenne PLZ und Stadt
      String[] lineSplit = line.split(";");
      String plz = lineSplit[0];
      String city = lineSplit[1];
      
      // Füge Zuordnung zu Suchindex hinzu
      this.addToSearchIndex(plz, city);
    }
  }
  
  // Private Funktion, welche eine PLZ-Stadt-Zuordnung dem
  // Suchindex hinzufügt
  private void addToSearchIndex(String plz, String city) {
    if (plz.length() > 1) {
      // Füge für alle Variationen der PLZ hinzu
      String plzSearchQuery = "";
      for (int i = 0; i < plz.length(); i++) {
        // Füge Ziffer hinzu
        plzSearchQuery += plz.charAt(i);
        
        // Wenn Suchergebnis noch nicht existiert
        if (this.searchIndex.get(plzSearchQuery) == null) {
           // Generiere Suchergebnis neu
           HashMap<String, String> searchResult =
             new HashMap<String, String>();
           this.searchIndex.put(plzSearchQuery, searchResult);
        }
        
        // Füge Suchbegriff zu Index hinzu
        this.searchIndex.get(plzSearchQuery).put(plz, city);
      }
    }
  }
  
  // Funktion, welche die Suchergebnisse für einen Such-
  // begriff zurückgibt
  public void printSearchResults(String searchQuery) {
    // Hole Ergebnisse für Suchbegriff
    HashMap<String, String> searchResult = 
      this.searchIndex.get(searchQuery);
     
    if (searchResult == null) {
      println("Kein Suchergebnis");
      return;
    }
    
    // Gehe alle Suchergebnisse durch
    for (String plz : searchResult.keySet()) {
      // Hole Stadt
      String city = searchResult.get(plz);
      
      // Gebe Ergebnis aus
      println(plz + ": " + city);
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu
// Demonstrations- und Testzwecken aufgerufen.
public void setup() {
  AutoCompletion ac = new AutoCompletion();
  
  ac.printSearchResults("324");
  println();
  ac.printSearchResults("6666");
  println();
  ac.printSearchResults("plz");
  println();
  ac.printSearchResults("12345");
}
