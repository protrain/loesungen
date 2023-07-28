// Funktion, welche den Emotionsdatensatz importiert und für die
// weitere Nutzung vorverarbeitet
HashMap<String, Float> importEmotions(String filepath) {  
  HashMap<String, Float> output = new HashMap<String, Float>();
  
  // Lese die Datensatzdatei als String-Array ein
  String[] lines = loadStrings(filepath);
  
  // Gehe jede Zeile einzeln durch
  for (String line : lines) {
    // Trenne die Zeile mittels Tabulatorzeichen in die einzelnen
    // Spalten auf
    String[] columns = line.split("\t");
    
    // Wir lesen nur Zeilen mit mindestens zwei Spalten aus
    if (columns.length < 2) {
      continue;
    }
    
    // Lese Wort ein und entferne das Kürzel am Ende
    String word = columns[0];
    int stopPosition = word.indexOf("|");
    word = word.substring(0, stopPosition);
    
    // Lese Emotionsbewertung als Float ein
    float emotionScore = Float.parseFloat(columns[1]);
    
    // Füge Hauptwort hinzu
    output.put(word, emotionScore);
    
    if (columns.length == 2) {
       // Wort hat keine Variationen, daher gehen wir in
       // die nächste Iteration
       continue; 
    }
    
    // Lese Wortvariationen als einzelne Arrayelemente ein.
    // Die Einträge sind hier mit Komma getrennt, daher
    // brauchen wir die split-Funktion.
    String[] wordVariations = columns[2].split(",");
        
    // Füge Wortvariationen hinzu
    for (String wordVariation : wordVariations) {
      output.put(wordVariation, emotionScore);
    }
  }
  
  return output;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Lade Testtabelle im TSV-Format
  HashMap<String, Float> emotions = importEmotions("testdata.txt");
  
  println(emotions.get("erster"));
  println(emotions.get("zweit"));
  println(emotions.get("Dritter"));
}
