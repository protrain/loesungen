# Definiere Variablen für RGB-Farbwert
r = 75
g = 0
b = 130

# Normiere die RGB-Farbe
rNorm = r / 255.0
gNorm = g / 255.0
bNorm = b / 255.0

# Bestimme daraus w
w = max(rNorm, gNorm, bNorm)

# Berechne CMYK
c = (w - rNorm) / w
m = (w - gNorm) / w
y = (w - bNorm) / w
k = 1 - w

# Gebe beide Farbwerte aus
print "RGB(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
print "CMYK(" + str(c) + ", " + str(m) + ", " + str(y) + ", " + str(k) + ")"

