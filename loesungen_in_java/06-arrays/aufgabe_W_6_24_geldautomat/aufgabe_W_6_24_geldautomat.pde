// Wir wollen 2305 Euro ausgeben
int betrag = 2305;

// Wir haben einen Kontostand von 500 Euro
int kontostand = 5000;

// Betrag muss größer als 0 Euro sein und darf maximal
// der Kontostand sein. Außerdem müssen wir den Beitrag in
// Fünf-Euro-Scheinen aufteilen können.
if (betrag > 0 && betrag < kontostand && betrag % 5 == 0) {
  // Liste der möglichen Scheinarten
  int[] scheine = {
    500,
    200,
    100,
    50,
    20,
    10,
    5
  };

  // Beitrag, den wir noch ausgeben müssen
  int restBetrag = betrag;

  // Gehe alle Scheinarten durch
  for (int i = 0; i < scheine.length; i = i + 1) {
    // Anzahl der Scheine, die wir für die aktuelle
    // Scheinart bekommen
    int numScheine = restBetrag / scheine[i];

    // Gebe die Anzahl der Scheine aus, wenn wir diese
    // Scheinart ausgeben können
    if (numScheine > 0) {
      println(numScheine + "x" + scheine[i]);
    }

    // Bestimme den Restbetrag, den wir mit der aktuellen
    // Scheinart nicht ausgeben konnten
    restBetrag = restBetrag % scheine[i];
  }
}
