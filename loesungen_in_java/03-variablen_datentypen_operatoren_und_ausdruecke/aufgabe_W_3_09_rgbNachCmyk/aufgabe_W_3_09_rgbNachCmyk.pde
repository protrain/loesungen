// Definiere Variablen für RGB-Farbwert
int r = 75;
int g = 0;
int b = 130;

// Normiere die RGB-Farbe
float rNorm = r / 255.0f;
float gNorm = g / 255.0f;
float bNorm = b / 255.0f;

// Bestimme daraus w
float w = max(rNorm, gNorm, bNorm);

// Berechne CMYK
float c = (w - rNorm) / w;
float m = (w - gNorm) / w;
float y = (w - bNorm) / w;
float k = 1 - w;

// Gebe beide Farbwerte aus
println("RGB(" + r + ", " + g + ", " + b + ")");
println("CMYK(" + c + ", " + m + ", " + y + ", " + k + ")");
