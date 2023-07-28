int tag = 0;

// Bestimme Uhrzeit, zu der Ebbe ist
float ebbeStunde = 4;
float ebbeMinute = 47;

println("Tag "+tag+" - Ebbe: "+int(ebbeStunde)+" Uhr und "
    +int(ebbeMinute)+" Minuten");

// Berechne Ebbezeit als Kommazahl
float ebbeKomma = (ebbeStunde + ebbeMinute / 60.0);

// Berechne Zeit zwischen Ebbe und Ebbe als Kommazahl
float tideStunden = 12.0;
float tideMinuten = 25.0;
float tideKomma = tideStunden + tideMinuten / 60.0;

for (int i = 0; i < 5; i++) {
  // Berechne daraus Uhrzeit als Kommazahl, zu der Flut ist
  float flutKomma = (ebbeKomma + tideKomma / 2.0);

  // Berechne den Tag
  tag = int(flutKomma) / 24;

  // Berechne Stunden und Minuten aus der Kommazahl
  int flutStunde = int(flutKomma) % 24;
  int flutMinute = int(flutKomma % 1 * 60);

  println("Tag "+tag+" - Flut: "+flutStunde+" Uhr und "
      +flutMinute+" Minuten");

  // Berechne die nächste Ebbe
  ebbeKomma = (ebbeKomma + tideKomma);

  // Berechne den Tag
  tag = int(ebbeKomma) / 24;

  // Berechne Stunden und Minuten aus der Kommazahl
  ebbeStunde = int(ebbeKomma) % 24;
  ebbeMinute = int(ebbeKomma % 1 * 60);

  println("Tag "+tag+" - Ebbe: "+int(ebbeStunde)+" Uhr und "
      +int(ebbeMinute)+" Minuten");
}
