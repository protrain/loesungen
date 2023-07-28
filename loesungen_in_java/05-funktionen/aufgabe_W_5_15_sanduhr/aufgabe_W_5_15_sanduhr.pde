// Funktion zur Ausgabe einer Sanduhr auf der Konsole
// Die maximale Breite wird als Integer-Wert an die
// Funktion übergeben. Die Funktion hat keinen Rückgabewert
void printSandglass(int width) {
  if(width > 2) {               // nur wenn die Breite > 2 ist
    int height = width;         // Höhe wird mit Breite initialisiert
      if(width % 2 == 0)        // ist die Breite eine gerade Zahl
        height--;               // muss die Höhe um eins minimiert werden

    // wiederhole für alle Zeilen des oberen Dreiecks 
    for (int i = 0; i < height / 2 + 1; i++)  { // mit der halben Höhe
      // Rücke mit zunehmender Zeilenzahl i ein
      for (int j = 0; j < i; j++)
        print(" ");            // Schreibe Leerzeichen

      // Die Variable width gibt die Anzahl an #-Zeichen an,
      // die mit jeder Zeile i um 2 verringert wird
      for (int j = 0; j < width - (2 * i); j++)
        print("#");            // Schreibe Lattenzaun-Zeichen

      println();               // wechsle in die nächste Zeile
    }

    // wiederhole für alle Zeilen des unteren Dreiecks
    for (int i = height / 2 - 1; i >= 0; i--)  {
      // Rücke mit zunehmender Zeilenzahl i ein
      for(int j=0; j<i; j++)
        print(" ");           // Schreibe Leerzeichen

      // Die Variable width gibt die Anzahl an #-Zeichen an,
      // die mit jeder Zeile um 2 erhöht wird
      for (int j = 0; j < width - (2 * i); j++)
        print("#");           // Schreibe Lattenzaun-Zeichen

      println();              // wechsle in die nächste Zeile
    }
  }
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  printSandglass(8);
}

