// Funktion zur Berechnung des Bogenmaßes
// Erhält die Gradzahl als Fließkommazahl und
// liefert das Bogenmaß zurück
float toRadians(float degree) {
  float radian = degree / 180 * PI;
  return radian;
}

// Funktion zur Berechnung der Distanz zwischen zwei GPS-
// Koordinaten. Übergeben werden Breitengrad und Längengrad der
// ersten und der zweiten Koordinate
float gpsDistance(float lat1, float lon1, float lat2, float lon2) {
  // Umrechnen in Bogenmaß
  lat1 = toRadians(lat1);
  lon1 = toRadians(lon1);
  lat2 = toRadians(lat2);
  lon2 = toRadians(lon2);

  // Berechne die Entfernung mithilfe vordefinierter
  // mathematischer Funktionen
  float c = acos(
    sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)
  );
  float d = c * 6378.137;

  return d;
}

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // GPS-Koordinaten Kölner Dom
  float kdLat = 50.94157;
  float kdLon = 6.95821;

  // GPS-Koordinaten Düsseldorfer Fernsehturm
  float ftLat = 51.21795;
  float ftLon = 6.76165;

  println(gpsDistance(kdLat, kdLon, ftLat, ftLon));

  // GPS-Koordinaten Hamburger Elbphilharmonie
  float hhLat = 53.54125;
  float hhLon = 9.9841;

  // GPS-Koordinaten Münchener Frauenkirche
  float muLat = 48.13663;
  float muLon = 11.57715;

  println(gpsDistance(hhLat, hhLon, muLat, muLon));
}

