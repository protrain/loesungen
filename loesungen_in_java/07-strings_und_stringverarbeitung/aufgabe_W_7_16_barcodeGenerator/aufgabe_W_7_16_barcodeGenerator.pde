// Funktion zum Zeichnen von Linien für ein übergebenes
// Ziffern-Array. Der Funktion wird die codierte String-
// sowie die Startkoordinate übergeben.
void drawDigitLines(String coding, int startX) {
  // Variablen zum Zeichnen der Linien
  int x = startX;
  int y1 = 10;
  int y2 = 130;
  int lineWidth = 3;       // Breite für eine Linie

  // Linienbreite festlegen
  strokeWeight(lineWidth);

  // Linientyp festlegen
  strokeCap(SQUARE);

  for (int i = 0; i < coding.length(); i++) {
    // Farbe setzen
    if (coding.charAt(i) == '1') {
      stroke(0);
    }
    else {
      stroke(255);
    }
    line(x, y1, x, y2);
    x = x + lineWidth;     // Eine Linie weiterspringen
  }
}


// Überladung der Funktion, falls drawDigitLines nur mit
// einem Parameter aufgerufen wird. Die Funktion erhält
// den codierten String. Die Startkoordinate wird von
// der Funktion geeignet gewählt und damit die Basisfunktion
// aufgerufen.
void drawDigitLines(String coding) {
  drawDigitLines(coding, 20);
}

// Funktion, die eine codierte Nummer als Ziffern-Array zurück-
// gibt. Die Funktion erhält als Parameter den darzustellenden
// Zahlenwert sowie eine boolesche Variable für die Steuerung der
// Seitencodierung:
// leftside == true => linke Seite
// leftside == false => rechte Seite
String getNumberCode(int number, boolean leftSide) {
  // Generiere Nummern für rechte Seite
  String output = "";
  if (number == 0) {
    output = "0001101";
  }
  else if (number == 1) {
    output = "0011001";
  }
  else if (number == 2) {
    output = "0010011";
  }
  else if (number == 3) {
    output = "0111101";
  }
  else if (number == 4) {
    output = "0100011";
  }
  else if (number == 5) {
    output = "0110001";
  }
  else if (number == 6) {
    output = "0101111";
  }
  else if (number == 7) {
    output = "0111011";
  }
  else if (number == 8) {
    output = "0110111";
  }
  else if (number == 9) {
    output = "0001011";
  }

  // Wenn für rechte Seite bestimmt, dann invertieren
  if (leftSide == false) {
    // Gehe alle Array-Elemente durch
    String temp = "";
    for (int i = 0; i < output.length(); i++) {
      if (output.charAt(i) == '1') {
        temp = temp + "0";
      }
      else {
        temp = temp + "1";
      }
    }
    output = temp;
  }

  return output;
}

// Überladung der Funktion, die eine codierte Nummer als
// Ziffern-Array zurückgibt. Die Funktion erhält als
// Parameter nur den darzustellenden Zahlenwert für die linke
// Codierungsseite
String getNumberCode(int number) {
  return getNumberCode(number, true);
}

// Funktion zum Generieren eines Barcodes aus 11 Ziffern.
// An die Funktion wird ein String mit den Nummern übergeben.
// Die Funktion liefert den Barcode als String zurück.
// Die Prüfziffer wird in der Funktion berechnet
String getBarcode(String numbers) {
  final String QUIET_ZONE = "0000000";
  final String START_END_PATTERN = "101";
  final String MIDDLE_PATTERN = "01010";

  if (numbers.length() != 11) {
    println("Die angegebene Nummernfolge hat nicht genau 11 Zeichen.");
    println("Der Barcode ist daher nicht korrekt.");
  }

  // Prüfziffer berechnen
  int checksum = 0;
  int temp = 0;
  for (int i = 0; i < 10; i = i + 2) {
    temp = temp + Integer.parseInt("" + numbers.charAt(i));
  }

  checksum = temp * 3;
  temp = 0;

  for (int i = 1; i < 10; i = i + 2) {
    temp = temp + Integer.parseInt("" + numbers.charAt(i));
  }

  checksum = checksum + temp;
  checksum = checksum % 10;

  if (checksum > 0) {
    checksum = 10 - checksum;
  }

  println("Code: " + numbers + checksum);

  // Generiere Barcode
  String barcode = QUIET_ZONE + START_END_PATTERN;
  int i = 1; // Anzahl bearbeiteter Ziffern
  boolean leftSide = true;

  for (int pos = 0; i <= numbers.length(); pos = pos + 1) {
    if (i == 12) {
      break;
    }

    int number = Integer.parseInt("" + numbers.charAt(pos));
    barcode = barcode + getNumberCode(number, leftSide);

    // Wenn an der Mitte angekommen, dann Mitte-Muster anfügen
    // und Codierung für rechte Seite aktivieren
    if (i == 6) {
      leftSide = false;
      barcode = barcode + MIDDLE_PATTERN;
    }
    i = i + 1;
  }
  // Zusammensetzen des Barcodes
  barcode = barcode + getNumberCode(checksum, false) +
      START_END_PATTERN + QUIET_ZONE;
  println(barcode);
  return barcode;
}

// Funktion zum Zeichnen des Barcodes. Der Funktion wird
// die Nummer als String übergeben.
public void drawBarcode(String numbers) {
  drawDigitLines(getBarcode(numbers));
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Stringverarbeitungsfunktion zu
// Demonstrations- und Testzwecken aufgerufen.
void setup() {
  size(400, 200);
  stroke(0);
  fill(0);
  background(255, 255, 255);

  drawBarcode("98765432110");
}

