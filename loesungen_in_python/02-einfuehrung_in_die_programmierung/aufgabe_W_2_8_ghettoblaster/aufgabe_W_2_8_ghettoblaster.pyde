size(400, 400)
smooth()

background(255)

# Henkel
# Schwarze Fläche mit Rundungen oben
stroke(0)
strokeWeight(5)
fill(0)
rect(75, 45, 250, 65, 15, 15, 0, 0)
# Weiße Fläche ohne Rundungen
noStroke()
fill(255)
rect(85, 65, 230, 50)

# Körper (300x100 Pixel groß)
stroke(0)
fill(217)
rect(50, 100, 300, 180, 15)

# Frequenzanzeiger
# graue Grundfläche (280x40 Pixel)
fill(89)
noStroke()
rect(60, 120, 280, 40, 10)

# oranges Display links
fill(219, 106, 28)
rect(80, 125, 60, 30)

# weiße Frequenzlinien rechts
stroke(255)
strokeCap(SQUARE)
strokeWeight(2)
line(160, 138, 320, 138)
line(160, 142, 320, 142)

# grauer Trenner darunter
stroke(89)
strokeWeight(4)
line(75, 170, 330, 170)

# Blaue Lautsprecherboxen
stroke(65, 91, 139)
fill(90, 126, 187)
strokeWeight(10)

# X-Mitte der Box
# = 300 (Breite)/2 + 50 (X-Startposition)
# = 200
# Linke X-Hälftenmitte also 300/4+50 = 125
# Y-Mitte der Box: 180/2+100=190
# Linke untere Y-Hälftenmitte: 180/4*3+100=235
ellipse(125, 225, 80, 80)
ellipse(275, 225, 80, 80)

