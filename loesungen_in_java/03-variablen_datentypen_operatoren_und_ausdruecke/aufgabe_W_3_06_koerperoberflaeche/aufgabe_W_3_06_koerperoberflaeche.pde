// Körpergröße in cm
int height = 180;

// Körpergewicht in kg
int weight = 58;

// Berechnung der Körperoberfläche nach der Formel von Mosteller
// in Quadratmeter (m^2)
float a = height * weight / 3600.0;
float b = sqrt(a);

// Ausgabe des Ergebnisses
println(
  "Ein " + height + " cm großer und " + weight + " kg schwerer Mensch "
  + "verfügt über ca " + b + " m^2 Haut."
);

