size(140, 140)

stroke(0)                   # Linienfarbe Schwarz
strokeWeight(80)            # Strichstärke 80 Pixel
line(70, 50, 70, 90)        # Körper als dicke Linie

noStroke()
fill(255)
ellipse(50, 50, 40, 40)     # Linkes Auge
ellipse(90, 50, 40, 40)     # Rechtes Auge
arc(70, 50, 80, 80, 0, PI)  # Kinn als Halbkreis

fill(0)
ellipse(58, 50, 8, 8)       # Linke Pupille
ellipse(82, 50, 8, 8)       # Rechte Pupille
quad(70, 58,                # Oberer Punkt des Schnabels
     73, 64,                # Rechter Punkt des Schnabels
     70, 70,                # Unterer Punkt des Schnabels
     67, 64)                # Linker Punkt des Schnabels

