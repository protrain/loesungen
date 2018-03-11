# Klasse zur Berechnung vom BMI
class Health:
    # Statische Methode zur Berechnung der Kategorie in
    # Abhängigkeit vom BMI, der an die Methode übergeben wird
    # Die Kategorie wird als Text zurückgegeben.
    @staticmethod
    def getCategory(bmi):
        # Gebe Kategorie in Abhängigkeit zum Wert zurück
        if bmi < 18.5:
            return "untergewichtig"
        elif bmi >= 18.5 and bmi <= 25:
            return "normalgewichtig"
        elif bmi > 25 and bmi <= 30:
            return "übergewichtig"
        else:
            return "fettleibig"

    # Statische Methode zur Berechnung des BMI.
    # Die Methode erhält die Körpergröße sowie das Gewicht
    # als Eingabe und gibt den berechneten BMI als
    # Fließkommazahl zurück
    @staticmethod
    def computeBMI(weight, height):
        return weight / (height * height)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testwerte
tWeight = 57
tHeight = 1.80

# Werte berechnen
bmi = Health.computeBMI(tWeight, tHeight)
category = Health.getCategory(bmi)

print "Mit einem BMI von " + str(bmi) + " sind Sie " + category + "."



