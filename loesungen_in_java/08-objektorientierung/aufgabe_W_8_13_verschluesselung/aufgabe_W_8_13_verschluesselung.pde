// Klasse, die die Schiebeverschlüsselung realisiert
public class ShiftCipher {
  // Deklaration privater Variablen
  private int key;

  // Konstruktor, der den Schlüssel zur Voraussetzung
  // der Instanziierung eines Objekts macht. Der an die
  // Funktion übergebene Schlüssel wird für die Lebens-
  // dauer intern gespeichert.
  public ShiftCipher(int key) {
    this.key = key;
  }

  // Öffentliche Methode zum Verschlüsseln eines übergebenen
  // Texts. Das Ergebnis der Verschlüsselung wird von der
  // Methode zurückgeliefert.
  public String encipher(String plain) {
    // Hier wird verschlüsselter String gespeichert
    String enciphered = "";

    // Gehe jeden Buchstaben durch
    for (int i = 0; i < plain.length(); i++) {
      // Hole Buchstaben
      char c = plain.charAt(i);

      // bestimme Position
      int pos = getPositionInAlphabet("" + c);

      // Addiere mit Key
      int newPos = pos + this.key;

      // Wenn neue Position kleiner als Alphabet ist,
      // addiere mit 26 (= innerhalb von 1 bis 26)
      if (newPos >= 26) {
        newPos = (newPos + 26) % 26;
      }

      // Hole neuen Buchstaben
      char newC = getLetterInPosition(newPos);

      // Füge dem String hinzu
      enciphered = enciphered + newC;
    }

    // Gebe verschlüsselten String zurück
    return enciphered;
  }

  // Öffentliche Methode zum Entschlüsseln eines Texts, der
  // an die Methode übergeben wird. Mithilfe
  // des intern gespeicherten Schlüssels liefert
  // die Methode das Ergebnis (den Klartext) wieder
  // zurück.
  public String decipher(String input) {
    String output = "";

    // Gehe jeden Buchstaben durch
    for (int i = 0; i < input.length(); i++) {
      char c = input.charAt(i);

      // Bestimme Position
      int pos = getPositionInAlphabet("" + c);

      // Subtrahiere mit Key
      int newPos = pos - this.key;

      // Wenn neue Position kleiner als Alphabet ist,
      // addiere mit 26 (= innerhalb von 0 bis 25)
      if (newPos < 0) {
        newPos = (newPos + 26) % 26;
      }

      // Hole neuen Buchstaben
      char newC = getLetterInPosition(newPos);

      // Füge dem String hinzu
      output = output + newC + " ";
    }

    // Gebe entschlüsselten String zurück
    return output;
  }

  // Private Methode, die zu einem Buchstaben die Position
  // im Alphabet berechnet und zurückgibt.
  private int getPositionInAlphabet(String letter) {
    // Wandle Buchstabe in Kleinbuchstaben um
    letter = letter.toLowerCase();

    // String zur Zuordnung von Buchstaben
    // zu ihrer Alphabetsposition
    String letterPosition = "abcdefghijklmnopqrstuvwxyz";
    // Hole Position im lateinischen Alphabet
    int posNumber = letterPosition.indexOf(letter);
    return posNumber;
  }

  // Private Methode, um einen Buchstaben von der angegebenen
  // Position des Alphabets zurückzuliefern.
  private char getLetterInPosition(int position) {
    // String zur Zuordnung von
    // Alphabetsposition zu Buchstaben
    String alphabet = "abcdefghijklmnopqrstuvwxyz";
    // Gebe Buchstaben zurück
    return alphabet.charAt(position);
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
// instanziiert und verwendet.
public void setup() {
  ShiftCipher sc = new ShiftCipher(3);
  String encrypted = sc.encipher("abcdefghijklmnopqrstuvwxyz");
  println(encrypted);
  println(sc.decipher(encrypted));

  sc = new ShiftCipher(3);
  encrypted = sc.encipher("DieserTextIstVerschluesselt");
  println(encrypted);
  println(sc.decipher(encrypted));
}

