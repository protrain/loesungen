# Klasse zur Berechnung vom bmi
class Health:
    # Statische Methode zur Berechnung der Kategorie in
    # Abhängigkeit vom bmi, der an die Methode übergeben wird
    # Die Kategorie wird als Text zurückgegeben.
    @staticmethod
    def get_category(bmi):
        # Gebe Kategorie in Abhängigkeit zum Wert zurück
        if bmi < 18.5:
            return "untergewichtig"
        elif bmi >= 18.5 and bmi <= 25:
            return "normalgewichtig"
        elif bmi > 25 and bmi <= 30:
            return "übergewichtig"
        else:
            return "fettleibig"

    # Statische Methode zur Berechnung des bmi.
    # Die Methode erhält die Körpergröße sowie das Gewicht
    # als Eingabe und gibt den berechneten bmi als
    # Fließkommazahl zurück
    @staticmethod
    def compute_bmi(weight, height):
        return weight / (height * height)


# Startpunkt des Hauptprogramms
# Hier wird die implementierte Klasse zu Demonstrations- und Testzwecken
# instanziiert und verwendet.

# Testwerte
t_weight = 57
t_height = 1.80

# Werte berechnen
bmi = Health.compute_bmi(t_weight, t_height)
category = Health.get_category(bmi)

print("Mit einem bmi von " + str(bmi) + " sind Sie " + category + ".")
