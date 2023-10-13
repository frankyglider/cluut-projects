from datetime import time
import time

# Aufgabe 1: Die Supermarkt Klasse
#
#     Erstelle zunächst eine Klasse Supermarket, mit den Attributen name (str), street (str), city (str).
#     Jeder Supermarkt soll auch die Attribute employees und products haben, die zunächst als leere Liste implementiert werden sollen.
    
class Supermarket:
    """Class to build a supermarket"""
    def __init__(self, name, street, city):
        self.name = str(name).title()
        self.street = str(street).title()
        self.city = str(city).title()
        self.employees = []
        self.products = []
        
# Aufgabe 2: Die Mitarbeiter Klasse

#     Erstelle eine Klasse Employee mit den Attributen name (str), age (int), pers_id (int), job (str).


#    Jeder Mitarbeiter soll sich höflich den Kunden deines Supermarket vorstellen und einmal im Jahr seinen Geburtstag feiern können.
#    Implementiere daher 2 Methoden, greet_customer und celebrate_birthday, die folgende Funktionen haben:
#        greet_customer: Gibt folgenden Text aus: "Guten Tag. Mein Name ist __ und ich bin ___ in diesem Supermarkt. Es ist momentan __ Uhr - wie kann ich Ihnen helfen?"
#        celebrate_birthday: Inkrementiert das Alter des Mitarbeiters und gibt den Text "Juhu! Heute werde ich _ Jahre!" aus.
        
class Employee:
    """Class to describe employees"""
    def __init__(self, name, age, pers_id, job):
        self.name = str(name).title()
        self.age = age
        self.pers_id = str(pers_id)
        self.job = str(job).title()
    
    def greet_customer(self):
        """Greets the customer of the supermarket"""
        time_1 = time.strftime('%H:%M', time.localtime())
        print(f'Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {time_1} Uhr - wie kann ich Ihnen helfen?')
        
    def celebrate_birthday(self):
        """Outputs a celebration message"""
        self.age += 1
        print(f'Juhu! Heute werde ich {self.age} Jahre!')
        



# Aufgabe 3: Die Produkt Klasse
# 
#     Erstelle eine Klasse Product mit den Attributen name (str), prod_id (int), category (str), price (float).
#         Jedes Produkt gehört in eine der folgenden Kategorien: food, drinks, others
#         Überprüfe schon beim Erstellen eines neuen Objekts, ob die Kategorie richtig gesetzt ist. 
#         Falls eine falsche Eingabe bei der Objekterstellung gemacht wurde, wähle stets die Kategorie others.


#     Implementiere eine Methode apply_discount, die den Parameter discount (float) hat und eine Prozentzahl entgegennimmt.
#         Teste in der Methode, ob discount zwischen 0 und 100 ist und wende den discount auf den Preis des Produkts an.
#         Sollte ein fehlerhafter discount eingegeben worden sein, printe eine Warnung und berechne einen 5%-Rabatt.




class Product:
    """Class to edit products"""
    def __init__(self, name, prod_id, category, price):
        self.name = str(name).title()
        self.prod__id = int(prod_id)
        self.price = float(price)
        
        if category == "food" or category == "drinks":
            self.category = category
        else:
            self.category = "others"
    
    
    def apply_discount(self, discount):
        """Method of reducing some prices"""
        
        if 0 <= discount <= 100:
            self.price = round(self.price - (self.price * (discount/100)), 2)
            print(f'You get {discount}% off this article. New price: {self.price}€.')
                
        else:
            self.price = round(self.price - (self.price * 0.05), 2)
            print(f'Discount not available, but you\'re lucky ! You get 5% off ! New Price for {self.name}: {self.price}€')
            
            

if __name__ == "__main__":
    # Testing the class
    my_market = Supermarket("Denn's", "Schanzenstraße 119", "Hamburg")
    print(my_market.street)
    print()
    employee_1 = Employee("Lea", 23, "dfg1563", "ceo")
    print(employee_1.job)
    print()
    employee_1.greet_customer()
    print()
    employee_1.celebrate_birthday()
    print()
    apple = Product("apple", "5115", "food", "0.85")
    print(apple.price)
    print()
    apple.apply_discount(101)
    #print(apple_discount)
    
    