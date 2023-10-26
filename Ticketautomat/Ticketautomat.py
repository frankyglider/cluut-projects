# In dieser Aufgabe soll ein Programm erstellt werden, das die Funktionalität eines Fahrkartenautomaten simuliert. 
# Dazu wird eine JSON-Datei eingelesen, die Informationen über verfügbare Tickets und deren Preise enthält. 
# Die Benutzer können ein Ticket auswählen, den Preis und die akzeptierten Münzen/Geldscheine anzeigen lassen und dann Münzen/Geldscheine einwerfen.

import json

with open("tickets.json", "r") as fh:
    ticket_data = json.load(fh)

# Erstellt eine Liste der Fahrkarten (für Output ohne eckige Klammen)
fahrkarten = []
for count, ticket in enumerate(x["tickets"]):
    available = str(count +1), ticket["name"]
    fahrkarten.append(":".join(available))

print(fahrkarten)
# Fordert den Kunden auf eine Fahrkarte auszuwählen
print(f'Herzlich willkommen bei Ihrer Bahn.\nBitte wählen Sie eines der verfügbaren Tickets:\n\n{", ".join(fahrkarten)}.')
print()

cash = ", ".join(str(n) for n in ticket_data["accepted_cash"])

# Beendet das Skript, sollte keine gültige Nummer eingegeben worden sein
choice = int(input())

if choice > len(fahrkarten) or choice <= 0:
    print(f'Ihre Auswahl ({choice}) ist nicht Verfügbar. Der Bestellvorgang wird abgebrochen.')
    exit()


# Informiert den Kunden über Auswahl, Preis und akzeptierte Barmittel
selection = x["tickets"][choice-1]["name"]
ticket_price = x["tickets"][choice-1]["price"]
print(f'Sie haben sich für {selection} entschieden.')
print(f'Der Preis beträgt {ticket_price}€.')
print()
print(f'Es werden folgende Barmittel (€) in Münzen und Noten akzeptiert: {cash}.\nSie können nun mit der Bezahlung beginnen.')
print()


accepted_cash = ticket_data["accepted_cash"]

# Überprüft, ob Einzahlung akzeptiert wird und errechnet fehlendes Geld und Rückgeld
total_bezahlt = 0
while total_bezahlt < ticket_price:
    geld_einwurf = int(input())
    if geld_einwurf in accepted_cash:
        total_bezahlt += geld_einwurf
        if total_bezahlt < ticket_price:
            print(f'Es fehlen noch {ticket_price - total_bezahlt}€ bis der Preis von {ticket_price}€ erreicht ist.')
    else:
        print("Bitte verwenden Sie nur die angegebenen Zahlungsmittel.")
        
print(f'Der zu bezahlende Betrag von {ticket_price}€ wurde erreicht. Bitte entnehmen Sie Ihr Ticket.\nIhr Rückgeld beträgt: {total_bezahlt - ticket_price}€.\nVielen Dank und gute Fahrt !')