// Funktion, die die Position eines Buchstabens
// im Alphabet zurückgibt.
// Erhält ein Zeichen als String und gibt dessen
// Position im Alphabet zurück
int getPosInAlphabet(String letter) {
  // Wandle Eingabe in einen Kleinbuchstaben um
  letter = letter.toLowerCase();

  // String mit dem gesamten Alphabet
  String alphabet = "abcdefghijklmnopqrstuvwxyz1234567890";

  // Gebe Stelle zurück, an der der Buchstabe im String vorkommt
  // (= Stelle im Alphabets-Array der Aufgabe)
  return alphabet.indexOf(letter);
}

// Funktion zur Ausgabe des Morsecodes für einen Eingabetext
// Übergeben wird der Eingabetext
void printMorseCode(String input) {
  // Setze Eingabe auf Lowercase
  input = input.toLowerCase();

  // Entferne alle Leerzeichen aus dem String
  input = input.replace(" ", "");

  // Entferne Punkt und Komma aus dem String
  input = input.replace(",", "");
  input = input.replace(".", "");

  String output = "";
  // Array für Morsezeichen (von Zeichen A bis 0)
  // Reihenfolge legt Funktion getPosInAlphabet fest
  String[] morsecode = {
    ".-",     // A
    "-...",   // B
    "-.-.",   // C
    "-..",    // D
    ".",      // E
    "..-.",   // F
    "--.",    // G
    "....",   // H
    "..",     // I
    ".---",   // J
    "-.-",    // K
    ".-..",   // L
    "--",     // M
    "-.",     // N
    "---",    // O
    ".--.",   // P
    "--.-",   // Q
    ".-.",    // R
    "...",    // S
    "-",      // T
    "..-",    // U
    "...-",   // V
    ".--",    // W
    "-..-",   // X
    "-.--",   // Y
    "--..",   // Z
    ".----",  // 1
    "..---",  // 2
    "...--",  // 3
    "....-",  // 4
    ".....",  // 5
    "-....",  // 6
    "--...",  // 7
    "---..",  // 8
    "----.",  // 9
    "-----"   // 0
  };

  // Gib den zu "morsenden" Text zunächst als Text aus
  println(input);

  // Lese Zeichen für Zeichen aus
  for (int i = 0; i < input.length(); i++) {
    // Hole Position in Alphabets-Array
    int pos = getPosInAlphabet("" + input.charAt(i));

    // gebe Zeichen aus
    print(morsecode[pos] + " ");
  }

  println();
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  printMorseCode("Wozu Worte drucken, es gibt doch Schreiber");
}

