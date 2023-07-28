# Definiere Konstanten für das Geschlecht
class Gender:
    FEMALE = 1
    NONBINARY = 0
    MALE = -1

# Klasse, welche eine Person repräsentiert
class Person (object):
    # Konstruktor für die Person
    def __init__(self,
                name,
                gender,
                expression,
                upper_hips,
                hip_swing,
                stability
    ):
        self.name = name
        self.gender = gender
        self.expression = expression
        self.upper_hips = upper_hips
        self.hip_swing = hip_swing
        self.stability = stability

    def get_expression(self):
        return self.expression

    def get_upper_hips(self):
        return self.upper_hips

    def get_hip_swing(self):
        return self.hip_swing

    def get_stability(self):
        return self.stability


# Abstrakte Klasse, welche einen Tanz repräsentiert
class Dance (object):
    # Konstruktor, welcher die beiden involvierten Personen
    # erwartet
    def __init__(self, person_a, person_b):
        self.person_a = person_a
        self.person_b = person_b

    def get_person_a(self):
        return self.person_a

    def get_person_b(self):
        return self.person_b

    # Private Funktion, welche die Paarharmonie in einer
    # Kategorie berechnet
    @staticmethod
    def get_harmony_subscore(score_person_a, score_person_b):
        # Berechne positive Differenz
        min_score = min(score_person_a, score_person_b)
        max_score = max(score_person_a, score_person_b)
        difference = max_score - min_score

        # Ziehe Differenz von Maximalpunktzahl ab
        return 10 - difference

    # Methode zur Bestimmung der Paarharmonie
    def get_harmony_score(self):
        # Gesamtsumme aller Wertungen
        score_sum = 0

        # Gehe alle Wertungen durch
        p_a_expression = self.person_a.get_expression()
        p_b_expression = self.person_b.get_expression()
        score_sum += self.get_harmony_subscore(p_a_expression,
                                              p_b_expression)

        __scores = self.get_relevant_criteria_scores()
        relevant_score_p_a, relevant_score_p_b = __scores
        score_sum += self.get_harmony_subscore(relevant_score_p_a,
                                              relevant_score_p_b)

        return score_sum / 2

    # Methode zur Bestimmung des Paarausdrucks
    def get_expression_score(self):
        score_person_a = self.person_a.get_expression()
        score_person_b = self.person_b.get_expression()

        return max(score_person_a, score_person_b)

    # Methode zur Bestimmung der Körperhaltungswertung.
    def get_posture_score(self):
        score_person_a = self.get_relevant_criteria_scores()[0]
        score_person_b = self.get_relevant_criteria_scores()[1]

        return (score_person_a + score_person_b) / 2

    # Methode zur Rückgabe der für Tanz relevanten Kriterums-
    # werte. Da diese in jedem Tanz anders ist, müssen wir sie
    # in den Unterklassen ausformulieren.
    def get_relevant_criteria_scores(self):
        return NotImplemented

    # Methode, welche die Wertung der Jury zurückgibt
    def get_jury_score(self):
        sum = self.get_harmony_score()
        sum += self.get_expression_score()
        sum += self.get_posture_score()
        return int(sum)


class StandardDance (Dance):
    def __init__(self, person_a, person_b):
        # Rufe die Superklasse zur Initialisierung auf
        Dance.__init__(self, person_a, person_b)

    def get_relevant_criteria_scores(self):
        scores = []
        scores.append(self.get_person_a().get_stability())
        scores.append(self.get_person_b().get_stability())

        return scores


class LatinDance (Dance):
    def __init__(self, person_a, person_b):
        # Rufe die Superklasse zur Initialisierung auf
        Dance.__init__(self, person_a, person_b)

    def get_relevant_criteria_scores(self):
        scores = []
        scores.append(self.get_person_a().get_hip_swing())
        scores.append(self.get_person_b().get_hip_swing())

        return scores


class SwingDance (Dance):
    def __init__(self, person_a, person_b):
        # Rufe die Superklasse zur Initialisierung auf
        Dance.__init__(self, person_a, person_b)

    def get_relevant_criteria_scores(self):
        scores = []
        scores.append(self.get_person_a().get_upper_hips())
        scores.append(self.get_person_b().get_upper_hips())

        return scores

# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    p_a = Person(
        "Francis",
        Gender.NONBINARY,
        7,
        10,
        5,
        5
    )
  
    p_b = Person(
        "Tom",
        Gender.MALE,
        4,
        7,
        6,
        7
    )
    
    ld = LatinDance(p_a, p_b)
    std = StandardDance(p_a, p_b)
    swd = SwingDance(p_a, p_b)
    print("LatinDance {}".format(ld.get_jury_score()))
    print("StandardDance {}".format(std.get_jury_score()))
    print("SwingDance {}".format(swd.get_jury_score()))


# Bei der Ausführung in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
