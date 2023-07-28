// Funktion, welche ein 3x3 Pixel großen
// Bildarray in Binärwerte umwandelt.
//
// Als Ergebnis liefert die Funktion
// das Array mit den Binärwerten zurück.
int[][] convertImageToBinaryArray(int[][] imagePixels) {
    // Das reduzierte Bild muss genau drei Pixel hoch und 
    // drei Pixel breit sein, ansonsten brechen wir die
    // Berechnung ab.
    int imageHeight = imagePixels.length;
    if (imageHeight != 3) {
        return null;
    }
    int imageWidth = imagePixels[0].length;
    if (imageWidth != 3) {
        return null;
    }
    
    // Extrahiere mittleres Pixel
    int centerPixel = imagePixels[1][1];
    
    // Definiere Vergleichs-Array. Hier werden wir die Bild-Pixel
    // in binäre Werte umwandeln. Der binäre Wert gibt dabei an,
    // ob der Pixelwert kleiner oder größer gleich dem mittleren
    // Pixel ist.
    int[][] binaryPixels = new int[3][3];
    
    // Vergleiche mittleres Pixel mit den umliegenden Pixeln
    for (int y = 0; y < imageHeight; y++) {        
        for (int x = 0; x < imageWidth; x++) {        
            
            // Hole Pixel an aktueller Position
            int current_pixel = imagePixels[y][x];
            
            // Setze die binären Werte
            if (current_pixel < centerPixel) {
                // Pixel hat kleineren Wert, daher ist der Binär-
                // Wert gleich 0
                binaryPixels[y][x] = 0;
            } else {
                // current_pixel muss an dieser Stelle größer gleich
                // centerPixel sein, daher können wir den Binär-
                // Wert auf 1 setzen
                binaryPixels[y][x] = 1;
            }
        }
    }
                
    return binaryPixels;
}

// Funktion, welche überprüft, ob sich ein Gesicht im Bild-
// Array befindet.
//
// Als Ergebnis liefert die Funktion True (Gesicht erkannt)
// oder False (kein Gesicht erkannt) zurück
boolean containsFace(int[][] imagePixels) {
    // Wandle Bild in Binärwerte um
    int[][] binaryPixels = convertImageToBinaryArray(imagePixels);
    
    //print("Binary Pixels { {}".format(binaryPixels));
    
    // Detektiere geforderte Binärpixelreihen
    if (binaryPixels[0][0] == 0
        && binaryPixels[0][1] == 0
        && binaryPixels[0][2] == 0
        && binaryPixels[1][0] == 0
        && binaryPixels[1][1] == 1
        && binaryPixels[1][2] == 0) {
          return true;
        }
        
    return false;
}
    

// Startpunkt des Hauptprogramms
// Hier wird die implementierte Funktion zu Demonstrations- und
// Testzwecken aufgerufen.
void setup() {
  // Definiere die Pixel vom Eingangsbild
  // Person mit dunkler Haut
  int[][] image1 = {
                     {53,174,89},
                     {93,190,33},
                     {195,170,213}
                   };
  
  // Person mit heller Haut
  int[][] image2 = {
                     {83,191,102},
                     {150,193,177},
                     {202,198,212}
                   };
  
  // Landschaft
  int[][] image3 = {
                     {143,82,122},
                     {167,137,35},
                     {126,154,151}
                   };
  
  println(containsFace(image1));
  println(containsFace(image2));
  println(containsFace(image3));
}
