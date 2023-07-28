# Klasse, die eine Webseite repräsentiert
class Website:
    # Konstruktor, welcher die Webseiten-URL erwartet
    def __init__(self, url):
        self.__url = url
        self.__linked_by_websites = []
    
    def get_linked_by_websites(self):
        return self.__linked_by_websites
    
    def get_url(self):
        return self.__url
    
    # Funktion, welche eine verlinkte Webseite hinzufügt 
    def add_link(self, website):
        self.__linked_by_websites.append(website)
  
    # Funktion, welche die Gesamtanzahl an Links zu dieser
    # Webseite zurückliefert
    def get_total_links(self):
        # Warteschlange an Links, die wir noch durchgehen müssen
        queue = []
        
        # Füge Webseiten zu Warteschlange hinzu
        for linked_by_website in self.get_linked_by_websites():
            queue.append(linked_by_website)
        
        link_count = 0
                
        # Gehe alle Webseiten durch, bis die Warteschlange leer ist
        while len(queue) > 0:          
            # Hole erste Webseite aus der Warteschlange
            website = queue.pop(0);        
                              
            # Erhöhe Linkzähler
            link_count += 1
            
            # Füge Webseiten zu Warteschlange hinzu
            for linked_by_website in website.get_linked_by_websites():
                queue.append(linked_by_website)
            
        return link_count
    

# Klasse, die ein Suchmaschinenranking realisiert
class SearchRanking:
    # Konstruktor, welcher einen Array der zu rankenden
    # Webseiten erwartet.
    def __init__(self, websites):
        self.websites = websites

    # Funktion, welche das erste Suchergebnis bestimmt und ausgibt
    def print_number_one(self):
        # Speichere das größte Ergebnis
        number_one_count = -1
        number_one = None
        
        # Gehe alle Webseiten durch
        for website in self.websites:
            num_links = website.get_total_links()
                        
            # Wenn der aktuelle Wert größer ist
            if (num_links > number_one_count):
                # Setze Webseite an Spitze
                number_one = website
                number_one_count = num_links
                
        print("{} ({} Links)".format(
            number_one.get_url(), 
            number_one_count
        ))


# Startpunkt des Hauptprogramms
# Hier werden die implementierten Klassen zu Demonstrations- und
# Testzwecken instanziiert und verwendet.
def setup():
    # Baue Webseiten und füge Verlinkungen hinzu
    ergebnis1 = Website("https://erste.website")
    ergebnis2 = Website("https://protrain.github.io")
    ergebnis3 = Website("https://dritte.website")
    
    link1 = Website("https://hilfe.programmieren")
    ergebnis1.add_link(link1)
    ergebnis2.add_link(link1)
        
    link2 = Website("https://mega.influencer")
    ergebnis2.add_link(link2)
    
    link2.add_link(Website("https://website1"))
    link2.add_link(Website("https://website2"))
    link3 = Website("https://website3")
    link2.add_link(link3)
        
    link4 = Website("https://website4")
    link3.add_link(link4)

    # Baue Testranking Nummer 1
    websites = [ergebnis1, ergebnis3]
    ranking = SearchRanking(websites)
    ranking.print_number_one()
        
    # Baue Testranking Nummer 2
    websites2 = [ergebnis1, ergebnis2, ergebnis3]
    ranking = SearchRanking(websites2)
    ranking.print_number_one()


# Bei der Ausführungn in einer reinen Python-Umgebung, muss die
# folgende Anweisung ergänzt werden
#setup()
