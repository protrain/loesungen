# Definiere Variablen für RGB-Farbwert
r = 75
g = 0
b = 130

# Normiere die rGB-Farbe
r_norm = r / 255.0
g_norm = g / 255.0
b_norm = b / 255.0

# Bestimme daraus w
w = max(r_norm, g_norm, b_norm)

# Berechne CMYK
c = (w - r_norm) / w
m = (w - g_norm) / w
y = (w - b_norm) / w
k = 1 - w

# Gebe beide Farbwerte aus
print("RGB(" + str(r) + ", " + str(g) + ", " + str(b) + ")")
print("CMYK(" + str(c) + ", " + str(m) + ", " + str(y) + ", " + str(k) + ")")
