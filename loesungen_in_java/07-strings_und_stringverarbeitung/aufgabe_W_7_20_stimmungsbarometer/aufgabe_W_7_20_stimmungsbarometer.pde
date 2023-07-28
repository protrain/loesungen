// Dateipfade zu den SentiWS-Datensatz-Dateien. Diese ggf.
// anpassen. Der Datensatz muss noch heruntergeladen werden,
// bevor das Programm ausgeführt werden kann.
// Siehe: https://github.com/protrain/loesungen
String basePath = "../../../externe_daten/sentiws/data/";
String pathPositive = basePath+"SentiWS_v2.0_Positive.txt";
String pathNegative = basePath+"SentiWS_v2.0_Negative.txt";

// Wir speichern die HashMap als globale Variable, damit wir sie
// nur einmal zur Laufzeit berechnen müssen. Andernfalls geht
// wertvolle Rechenzeit verloren.
HashMap<String, Float> emotions = null;

// Funktion, welche den Emotionsdatensatz importiert und für die
// weitere Nutzung vorverarbeitet
// Diese Funktionsvariation erzeugt dabei ein neues HashMap-Objekt
HashMap<String, Float> importEmotions(String filepath) {
  HashMap<String, Float> hashMap = new HashMap<String, Float>();

  return importEmotions(filepath, hashMap);
}

// Funktion, welche den Emotionsdatensatz importiert und für die
// weitere Nutzung vorverarbeitet
// Diese Funktionsvariation nutzt dabei das übergebene HashMap-
// Objekt weiter.
HashMap<String, Float> importEmotions(String filepath, HashMap<String, Float> hashMap) {
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
    hashMap.put(word, emotionScore);

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
      hashMap.put(wordVariation, emotionScore);
    }
  }

  return hashMap;
}

// Funktion, welche die Datenbanken importiert
void importEmotions() {
  // Wir generieren die HashMap nur, wenn sie noch nicht vorher
  // erstellt wurde.
  if (emotions == null) {
    // Lade Tabellen im TSV-Format
    emotions = importEmotions(pathPositive);
    // Hier verwenden wir die HashMap für die zweite Tabelle
    // weiter
    importEmotions(pathNegative, emotions);
  }
}

// Funktion, welche die Satzzeichen aus einem Wort entfernt
String removePunctuation(String word) {
  if (word.length() <= 1) {
    return word;
  }
  
  // Liste alle Satzzeichen auf, die wir entfernen wollen
  // Diese dürfen aber nur an vorderer oder hinterer Stelle
  // sein.
  char[] punctuations = {'.', ',', '-', '!', ':', ';'};

  // Entferne zunächst Leerzeichen an vorderer und hinterer
  // Stelle
  word = word.trim();

  // Entnehme vorderstes und hinterstes Zeichen
  char wordFirstChar = word.charAt(0);
  int wordLastCharPosition = word.length()-1;
  char wordLastChar = word.charAt(wordLastCharPosition);

  // Gehe alle Satzzeichen durch
  for (char punctuation : punctuations) {
    // Wir prüfen zunächst das Ende des Wortes
    if (wordLastChar == punctuation) {
      // Zeichen gefunden, wird entfernt
      word = word.substring(0, wordLastCharPosition);

      // Da wir nichts mehr zu entfernen haben, stoppen
      // wir die Schleife
      break;
    }
  }

  for (char punctuation : punctuations) {
    // Jetzt prüfen wir den Anfang des Wortes
    if (wordFirstChar == punctuation) {
      // Zeichen gefunden, wird entfernt
      word = word.substring(1);

      // Da wir nichts mehr zu entfernen haben, stoppen
      // wir die Schleife
      break;
    }
  }

  return word;
}

// Funktion, welche die Emotionsbewertung zurückliefert
float getEmotionScore(String word) {
  // Da die Datenbank noch nicht initalisiert wurde, machen
  // wir das einmal
  if (emotions == null) {
    importEmotions();
  }

  // Entferne Satzzeichen am Anfang und Ende des Wortes.
  word = removePunctuation(word);

  // Schaue nach, ob das Wort in Datensatz existiert
  float emotionScore;
  try {
    emotionScore = emotions.get(word);
  } 
  catch (NullPointerException e1) {
    // Prüfe, ob das Wort nicht noch in Kleinschreibung
    // vorhanden ist
    try {
      emotionScore = emotions.get(word.toLowerCase());
    } 
    catch (NullPointerException e2) {
      // Wort wurde nicht gefunden
      emotionScore = 0.0;
    }
  }

  return emotionScore;
}

// Funktion, welche aus einem Text die Grundstimmung
String determineSentiment(String text) {
  // Trenne den Text nach Leerzeichen auf
  String[] words = text.split(" ");

  // Emotionsbewertung aller Wörter
  float emotionScore = 0.0;

  // Gehe alle Wörter durch
  for (String word : words) {
    // Füge Emotionsbewertung hinzu
    emotionScore = emotionScore + getEmotionScore(word);
  }

  if (emotionScore == 0.0) {
    return "Keine Tendenz: "+emotionScore;
  } else if (emotionScore < 0.0) {
    return "Negative Tendenz: "+emotionScore;
  } else {
    return "Positive Tendenz: "+emotionScore;
  }
}


// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  importEmotions();
  
  String satz1 = "Die Schreiberlinge brillieren mit "
                 + "hervorragenden Einfällen! War sehr "
                 + "hilfreich für mich!";
  
  String satz2 = "Unverantwortlich, dass diese Autoren meinen , "
                + "sie könnten meinen Hass mit Zahlen messen.";

  println(satz1);
  println(determineSentiment(satz1));
  println();
  println(satz2);
  println(determineSentiment(satz2));
}
