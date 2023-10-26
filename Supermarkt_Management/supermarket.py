# Diese Aufgabenreihe konzentriert sich auf das Erstellen von Python-Klassen, um einen virtuellen Supermarkt zu modellieren. Hier ist eine ausführliche Beschreibung:

# Aufgabe 1: Supermarkt-Klasse

#     In dieser Aufgabe geht es darum, eine Python-Klasse mit dem Namen "Supermarket" zu erstellen. Diese Klasse repräsentiert einen Supermarkt und hat Attribute wie den Namen des Supermarkts, die Straße und die Stadt, in der er sich befindet. Zusätzlich sollte die Klasse leere Listen für Mitarbeiter und Produkte haben.

# Aufgabe 2: Mitarbeiter-Klasse

#     In dieser Aufgabe erstellen Sie eine weitere Python-Klasse namens "Employee", um die Mitarbeiter des Supermarkts zu modellieren. Die Mitarbeiter haben Eigenschaften wie ihren Namen, ihr Alter, ihre Personalnummer und ihren Job. Sie sollen in der Lage sein, sich höflich den Kunden des Supermarkts vorzustellen und ihren Geburtstag zu feiern. Dafür müssen die Methoden "greet_customer" und "celebrate_birthday" implementiert werden, um Kunden zu begrüßen und den Geburtstag des Mitarbeiters zu feiern.

# Aufgabe 3: Produkt-Klasse

#     Diese Aufgabe befasst sich mit der Erstellung der "Product"-Klasse, um die Produkte im Supermarkt darzustellen. Produkte haben Eigenschaften wie den Namen, die Produkt-ID, die Kategorie und den Preis. Jedes Produkt gehört zu einer der Kategorien: "food", "drinks" oder "others". Bei der Erstellung eines Produkts soll überprüft werden, ob die Kategorie korrekt gesetzt ist, andernfalls wird die Kategorie auf "others" gesetzt. Die Klasse sollte auch eine Methode "apply_discount" enthalten, um Rabatte auf den Produktpreis anzuwenden.

# Aufgabe 4: Mitarbeiter und Produkte einlesen

#     In dieser Aufgabe geht es darum, Mitarbeiter- und Produktinformationen aus CSV-Dateien zu importieren und sie in Listen zu speichern. Die Informationen stammen aus zwei Dateien: "employees.csv" und "products.csv".

# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen

#     Hier erstellen Sie einen konkreten Supermarkt, "my_supermarket", mit festgelegten Werten für den Namen, die Straße und die Stadt. Sie erstellen Mitarbeiter- und Produktobjekte aus den zuvor eingelesenen Daten und fügen sie dem Supermarkt hinzu.

# Aufgabe 6: Supermarkt-Management

#     Diese Aufgabe erfordert eine Analyse des erstellten Supermarkts. Sie müssen Fragen wie die Anzahl der Mitarbeiter, das teuerste Produkt, die durchschnittlichen Produktkosten und die Anzahl der Produkte in jeder Kategorie beantworten. Es wird empfohlen zu überlegen, ob es sinnvoll ist, zukünftig weitere Methoden in den Klassen zu implementieren, um diese Informationen leichter abzurufen.

# Insgesamt handelt es sich um eine Übung zur Erstellung von Python-Klassen und zur Modellierung eines Supermarkts und seiner Bestandteile. Sie werden auch mit CSV-Dateien arbeiten, um Daten zu importieren und den Supermarkt zu verwalten.

from datetime import time
import time


# Aufgabe 1: Erstellen der Supermarktklasse
    
class Supermarket:
    """Class to build a supermarket"""
    def __init__(self, name, street, city):
        self.name = str(name).title()
        self.street = str(street).title()
        self.city = str(city).title()
        self.employees = []
        self.products = []
        

# Aufgabe 2: Erstellen der Mitarbeiterklasse

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
        


# Aufgabe 3: Erstellen der Produktklasse

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
    # Testen der Klasse
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