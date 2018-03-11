// Importieren des Typs BigInteger aus der
// java.math-Bibliothek
import java.math.BigInteger;

// Funktion zur Generierung der IBAN-Prüfziffer
// Die IBAN wird als String übergeben. Als Ergebnis
// wird die IBAN inklusive Prüfziffer als String
// zurückgegeben
String generateIBANChecksum(String bigNum) {
  // Wandle in BigInteger um, damit solch eine lange
  // Zahl verarbeitet werden kann
  BigInteger number = new BigInteger(bigNum);

  // Berechne die Prüfziffer, indem die Nummer modulo 97
  // gerechnet wird. Für die Modulo-Rechnung muss der Wert
  // 97 vorher in ein BigInteger konvertiert werden
  int checksum = number
    .mod(new BigInteger("97"))
    .intValue();

  // Subtrahiere von 98
  checksum = 98 - checksum;

  // Ist Resultat kleiner 10, stelle 0 voran
  if (checksum < 10) {
    return "0" + checksum;
  }
  else { // ansonsten gib das Resultat zurück
    return "" + checksum;
  }
}


// Funktion zum Generieren der IBAN
// Die Kontonummer und Bankleitzahl werden als Strings an die
// Funktion übergeben. Das Ergebnis wird als String
// zurückgegeben.
String generateGermanIBAN(String kontonummer, String blz) {
  // Generiere Checksumme, indem zunächst ein String bestehend
  // aus Bankleitzahl, Kontonummer sowie der Zeichenfolge "131400"
  // aneinandergehängt werden, bevor die Prüfziffer hierfür
  // berechnet wird
  String checksum = generateIBANChecksum(
    blz + kontonummer + "131400"
  );

  // Gebe IBAN-Nummer zurück
  return "DE" + checksum + blz + kontonummer;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println(generateGermanIBAN("1234567890", "70090100"));
}

