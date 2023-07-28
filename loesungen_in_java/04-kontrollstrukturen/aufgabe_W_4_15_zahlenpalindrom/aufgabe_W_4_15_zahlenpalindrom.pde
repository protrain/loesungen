int number = 12321;
//int number = 12345;

// Zunächst bestimmen wir die Anzahl der Dezimalstellen der
// Palindrom-Zahl
int i = number;

// Anzahl der Dezimalstellen
int size = 0;
while (i > 0) {
  // Teile durch 10 (nehme letzte Zahl weg)
  i = i / 10;

  // Erhöhe Dezimalstellenzahl
  size = size + 1;
}

// Ist Zahl ein Palindrom?
boolean isPalindrom = false;

// Gehe size/2-Schritte durch (wenn wir vorne mit hinten vergleichen,
// sind wir ab der Hälfte durch)
for (i = size; i > size / 2; i = i - 1) {
  // Bestimme vordere Zahl
  // Schneide i Stellen vorne weg
  int firstDigit = number % int(pow(10, i));

  // Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
  // Ziffer da ist
  while (firstDigit / 10 != 0) {
    firstDigit = firstDigit / 10;
  }

  // Bestimme hintere Zahl
  // Schneide i Stellen vorne weg, hier allerdings in umgekehrter
  // Reihenfolge
  int lastDigit = number % int(pow(10, size - i + 1));

  // Gehe Zahl so lange "hoch" (durch 10 teilen), bis nur noch eine
  // Ziffer da ist
  while (lastDigit / 10 != 0) {
    lastDigit = lastDigit / 10;
  }

  // Prüfe, ob beide Ziffern übereinstimmen
  if (firstDigit == lastDigit) {
    isPalindrom = true;
  }
  else {
    isPalindrom = false;
    // Aus Schleife springen, damit Variable
    // nicht verändert werden kann
    break;
  }
}

// Erzeuge Ausgabe je nach Fall
if (isPalindrom) {
  println("Die Zahl " + number + " ist ein Palindrom");
}
else {
  println("Die Zahl " + number + " ist kein Palindrom");
}

