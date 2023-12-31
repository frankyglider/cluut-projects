import pandas as pd
import statistics
from collections import Counter
from supermarket import *


# Aufgabe 4: Mitarbeiter und Produkte aus altem System einlesen

with open("employees.csv", "r") as fh:
    df_employees = pd.read_csv(fh, sep = ";")
    #print(df_employees)
#print(type(df_employees))
print()

# Erstellen einer Liste von Tupeln mit Informationen über Mitarbeiter
df_employees.rename(columns = {'JOB_ID':'Job_id'}, inplace = True)
#print(df_employees)

df_employees = df_employees[["Name", "Age", "Pers_id", "Job_id"]]
#print(df_employees)

employees = list(df_employees.itertuples(name = None, index = False))
print(employees)

# Erstellen einer Liste von Tupeln mit Informationen über Produkte
with open("products.csv", "r") as fh:
    df_products = pd.read_csv(fh, sep = ";")
    #print(df_products)

df_products.rename(columns = {'PRICE': 'Price'}, inplace = True)

df_products = df_products[["Name", "Prod_id", "Category", "Price"]]
print(df_products)

products = list(df_products.itertuples(name = None, index = False))
#print(products)


# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen

my_supermarket = Supermarket("supermarkt deluxe", "marienplatz 1", "münchen")
print(my_supermarket.name)

my_supermarket.employees = [Employee(*item) for item in employees]
#print(my_supermarket.employees)
my_supermarket.products = [Product(*item) for item in products]
#print(my_supermarket.products)


# Aufgabe 6: Supermarkt Management

# Anzahl der Mitarbeiter

print(f'Mein Supermarkt hat aktuell {len(my_supermarket.employees)} Produkte.')
print()

# Ermitteln des teuersten Produktes im Supermarkt

# take second element for sort
def takeSecond(elem):
    return elem[1]

# list
most_exp = [(prod.name, prod.price) for prod in my_supermarket.products]

# sort list with key
most_exp.sort(key=takeSecond, reverse = True)
most_exp = most_exp[0]

print(f'The most expensive Product is: {most_exp[0]}. The price is: {most_exp[1]}.')
print()

# Durchschnittspreis der Produkte

average_price = statistics.mean([prod.price for prod in my_supermarket.products])
print(f'The average price of all listed products in our supermarket is: {average_price:.2f}€.')
print()

# Anzahl der Produkte pro Kategorie

category_list = [prod.category for prod in my_supermarket.products]

c = Counter(category_list)
print(f'We have {c["food"]} Items for the category "food" in our supermarket.')
print(f'We have {c["drinks"]} Items for the category "drinks" in our supermarket.')
print(f'We have {c["others"]} Items for the category "others" in our supermarket.')


# Ermitteln des ältesten AN

oldest_emp = [(emp.name, emp.age) for emp in my_supermarket.employees]

oldest_emp.sort(key=takeSecond, reverse = True)
oldest_emp = oldest_emp[0]

print(f'The oldest employee is {oldest_emp[0]} with a age of {oldest_emp[1]} years.')