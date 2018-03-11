// Masse in kg
int m = 80;

// Verteilungsfaktor im Körper (Frauen: 0.6, Männer: 0.7, Kinder: 0.8)
float r = 0.7f;

// Volumen des Getränks in ml
int V = 500;

// Alkoholvolumenanteil in Prozent
float e = 0.05f;

// Führe Berechnung durch
float A = V * e * 0.8;
float c = A / (m * r);

println(c);

