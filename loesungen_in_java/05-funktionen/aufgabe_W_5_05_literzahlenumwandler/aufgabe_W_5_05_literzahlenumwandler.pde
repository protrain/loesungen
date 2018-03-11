// Funktion zur Umrechnung von Volumenangaben
// Erhält das Volumen als Fließkommazahl und gibt den berechneten
// Wert mit der Einheit als String zurück
String volumeConverter(float volume) {
  if(volume >= 1.0f) {          // ist das Volumen größer oder gleich 1.0
    return volume + " l";       // dann Rückgabe Wert mit Einheit "l"
  }                             // sonst prüfe,
  else if(volume >= 0.1f) {     // ob Volumen größer oder gleich 0.1 
    int result = (int)(volume * 100) / 1; // Umrechnen Wert auf cl
    return result + " cl";      // Rückgabe Wert mit Einheit "cl"
  }                             // ansonsten prüfe, ob Volumen größer
  else if(volume >= 0.001f) {   // oder gleich 0.001f
    int result = (int)(volume * 1000) / 1; // Umrechnen Wert auf ml
    return result + " ml";      // Rückgabe Wert mit Einheit "ml"
  }
  else                          // ansonsten gib Fehlermeldung als Wert 
    return "Number too small!"; // der Umwandlung zurück
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  println(volumeConverter(1.0));
  println(volumeConverter(0.42));
  println(volumeConverter(0.023));
  println(volumeConverter(0.00023));
}

