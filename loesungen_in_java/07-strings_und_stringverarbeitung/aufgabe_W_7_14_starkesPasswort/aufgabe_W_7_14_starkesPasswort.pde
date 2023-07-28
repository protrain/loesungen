// Funktion prüft, ob ein als String übergebenes Passwort
// die Regeln für ein starkes Passwort erfüllt. Die Funktion
// gibt einen Wahrheitswert mit dem Ergebnis der Prüfung zurück.
boolean isStrong(String password) {
  // Enthält mindestens acht Zeichen
  if (password.length() < 8) {
    return false;
  }

  // Zähle einzelne Zeichentypen
  int lowercase = 0;
  int uppercase = 0;
  int number = 0;
  int special = 0;

  // Gehe String durch
  for (int i = 0; i < password.length(); i++) {
    char c = password.charAt(i);

    // Bestimme Character-Code
    int charCode = charToNumber(c);

    // ist ein Kleinbuchstabe
    if (charCode >= charToNumber('a') && charCode <= charToNumber('z'))
      lowercase += 1;
    // ist ein Großbuchstabe
    else if (charCode >= charToNumber('A') && charCode <= charToNumber('Z'))
      uppercase += 1; 
    // ist eine Ziffer
    else if (charCode >= charToNumber('0') && charCode <= charToNumber('9'))
      number += 1; 
    // ist ein Sonderzeichen (! oder *)
    else if (charCode == charToNumber('!') || charCode == charToNumber('*'))
      special += 1;
  }

  // Sind alle Zeichen gezählt, werte aus
  // Gebe true zurück, wenn alle Bedingungen erfüllt sind
  if (lowercase > 0 && uppercase > 0 && number > 0 && special > 0) {
    return true;
  }
  else {
    return false;
  }
}

// Funktion zum Konvertieren eines Buchstabens in Character-Code. Die
// Funktion erhält das Zeichen, für den der Code zurückgeliefert wird.
int charToNumber(char c) {
  return (int)c;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  //println(isStrong("eVJo2!8IrRo"));
  //println(isStrong("aH6*LauTp21u"));
  //println(isStrong("o1hKeaZG*!o"));
  //println(isStrong("Passwort123"));
  println(isStrong("!2Bcv"));
}

