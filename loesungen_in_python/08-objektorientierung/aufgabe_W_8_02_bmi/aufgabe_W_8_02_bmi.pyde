# Klasse zur Berechnung vom BMI
# Eigentlich unsinnig, aber da die Beispiele eigentlich für Java sind
# und dort alles in Klassen steckt, hier also auch eine Klasse
class Health:
    # Statische Methode zur Berechnung der Kategorie in
    # Abhängigkeit vom BMI, der an die Methode übergeben wird
    # Die Kategorie wird als Text zurückgegeben.
    @staticmethod
    def get_category(bmi):
        """ Gebe Kategorie in Abhängigkeit zum Wert zurück """
        if bmi < 18.5:
            return "untergewichtig"
        elif bmi <= 25:
            return "normalgewichtig"
        elif bmi <= 30:
            return "übergewichtig"
        else:
            return "fettleibig"

    # Statische Methode zur Berechnung des BMI.
    # Die Methode erhält die Körpergröße sowie das Gewicht
    # als Eingabe und gibt den berechneten BMI als
    # Fließkommazahl zurück
    @staticmethod
    def compute_BMI(weight, height):
        return weight / float(height ** 2)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testwerte
weight = 57
height = 1.80

# Werte berechnen
bmi = Health.compute_BMI(weight, height)
category = Health.get_Category(bmi)

print "Mit einem BMI von %s sind Sie %s." % (bmi,  category)



