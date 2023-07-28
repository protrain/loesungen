size(600, 600)
background(182, 191, 216)

# Skalierungsfaktor für den Gamecontroller
factor = 25

# Verschiebe Koordinatensystem
translate(50, 50)

# Male Grundgerüst
fill(53, 74, 126)
stroke(53, 74, 126)
rect(0, 0, 13 * factor, 3 * factor)
rect(0, 0, 5 * factor, 8 * factor)
rect(9 * factor, 0, 4 * factor, 8 * factor)

# Plus
fill(200)
stroke(200)
rect(2 * factor, 2 * factor, 1 * factor, 3 * factor)
rect(1 * factor, 3 * factor, 3 * factor, 1 * factor)

# Mittlerer Button
rect(6 * factor, 1 * factor, 2 * factor, 1 * factor)

# Button rechts
fill(141, 155, 191)
stroke(141, 155, 191)
rect(10 * factor, 1 * factor, 1 * factor, 1 * factor)
rect(11 * factor, 3 * factor, 1 * factor, 1 * factor)
