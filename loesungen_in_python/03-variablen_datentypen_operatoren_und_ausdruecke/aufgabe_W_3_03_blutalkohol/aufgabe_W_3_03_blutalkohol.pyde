# Masse in kg
m = 80.0

# Verteilungsfaktor im Körper (Frauen: 0.6, Männer: 0.7, Kinder: 0.8)
r = 0.7

# Volumen des Getränks in ml
V = 500

# Alkoholvolumenanteil in Prozent
e = 0.05

# Führe Berechnung durch
A = V * e * 0.8
c = A / (m * r)

print c

