// Variablen deklarieren und initialisieren
int a = 1;
int b = 2;
int c = 3;

// Variable deklarieren, die den maximalen Wert halten soll
int maxi = -2147483648; // kleinste erlaubte Integer-Zahl

// Maximum bestimmen
if (a > b) {            // a > b
  if (a > c) {          // a > b > c
    maxi = a;
  }
  else {                // c > a > b
    maxi = c;
  }
}
else {                  // b > a
  if (b > c) {          // b > a > c
    maxi = b;
  }
  else {                // c > b > a
    maxi = c;
  }
}

// Ausgabe des Maximums in der Konsole
println(
  "Der größte Wert in der Menge {" + a + ", " + b + ", " + c +
    "} lautet: " + maxi
);

