// Funktion, welches einen Buchstaben entgegennimmt
// und die Leetspeak-Variante davon zurückliefert.
// Sofern keine Leetspeak-Variante existiert,
// wird der gleiche Buchstabe zurückgeliefert.
public String getLeetChar(char inputChar) {
  // Wandle Char in String um, damit wir weiter
  // arbeiten können
  String inputCharUpper = "" + inputChar;
  // Wandle Buchstaben in Großbuchstaben um
  inputCharUpper = inputCharUpper.toUpperCase();
  
  // Generiere Zuordnung von Buchstaben zu Leet
  switch (inputCharUpper) {
    case "A":
      // Da wir direkt in die return-Anweisung gehen
      // benötigen wir keine break-Anweisung hier
      return "4";
    case "E":
      return "3";
    case "G":
      return "6";
    case "H":
      return "#";
    case "I":
      return "1";
    case "S":
      return "$";
    case "O":
      return "0";
    case "T":
      return "7";
    case "Z":
      return "2";
    default:
      // Nichts gefunden
      return "" + inputChar;
  }
}

// Funktion, welche einen Text als String entgegennimmt
// und dann die Leetspeak-Variante zurückliefert
public String getLeetspeak(String inputString) {
  String outputString = "";
  
  // Gehe jeden Buchstaben der Eingabestrings durch
  for (int i = 0; i < inputString.length(); i++) {
    // Wandle Buchstaben in Leetspeak um
    char inputChar = inputString.charAt(i);
    outputString += getLeetChar(inputChar);
  }
  
  return outputString;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
public void setup() {
  println(getLeetspeak("It's my job to keep punkrock elite"));
  println(getLeetspeak("An apple a day keeps hunger away"));
  println(getLeetspeak("abcdefghijklmnopqrstuvwxyz"));
}
