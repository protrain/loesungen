for (int i = 0; i <= 6; i++) {
  // Erzeuge Leerzeichen
  for (int j = 0; j < i; j++) {
    print("     ");
  }

  // Gebe Dominosteine aus
  for (int j = i; j <= 6; j++) {
    print("(" + i + "|" + j + ")");
  }

  // Zeilenumbruch
  println();
}

