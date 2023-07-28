// Gehe alle PIN-Zahlen durch
for (int i = 0; i <= 9999; i++) {
  // Füge je nach Zahlengröße fehlende Nullen hinzu
  if (i < 10) {
    print("000");
  }
  else if (i < 100) {
    print("00");
  }
  else if (i < 1000) {
    print("0");
  }

  // Gebe PIN-Zahl aus (mit Zeilenumbruch)
  println(i);

  // Verlangsamung der Ausgabe (kann auch auskommentiert werden)
  delay(1);
}

