# Fahrkartenautomat
# Programmiere einen Fahrkartenautomaten der wie folgt funktioniert:
# Der Automat liest eine json Datei ein in festgelegt wird welche Tickets es gibt und was sie kosten, so wie welche Münzen/Geldscheine der Automat akzeptiert. Die Datei sieht so aus und ist auch an die Aufgabe angehängt:


{
    "tickets": 
        [
            { 
                "name": "Einzelfahrkarte", 
                "price": 4 
                
            }, 
            { 
                "name": "Tageskarte (1 Person)", 
                "price": 15 
                
            }, 
            { 
                "name": "Tageskarte (Gruppe)", 
                "price": 25 
                
            }, 
            { 
                "name": "Monatskarte", 
                "price": 99 
                
            }
        ], 
    "accepted_cash": [1, 2, 5, 10, 20, 50] 
}

import json

# Zuerst werden dem Benutzer die Tickets angezeigt zusammen mit einer Nummer, über die er dann die Fahrkarte auswählen kann.
# Der Benutzer kann dann eine Fahrkarte auswählen.
# Es wird überprüft, ob der Benutzer eine gültige Nummer eingegeben hat, wenn nicht, wird das Programm beendet. (Ein Programm beendest du mit der Funktion "exit()").
# Bei einer gültigen Nummer wird dem Benutzer sowohl der Preis der Fahrkarte angezeigt, wie auch die Geldscheine/Münzen, die der Automat annimmt.
# Nun kann der Benutzer nach und nach Münzen/Geldscheine in den Automaten einwerfen.
# Jedes mal wenn der Benutzer etwas eingeworfen hat, wird überprüft, ob die Münze/der Geldschein überhaupt angenommen werden kann. Außerdem wird überprüft, ob der Benutzer schon genügend Geld eingeworfen hat.
# Wenn die Münze/der Geldschein gültig ist, wird der fehlende Betrag berechnet und dem Benutzer ausgegeben.
# Sobald genug Geld eingeworfen wurde, bedankt sich der Automat und gibt an wie viel Rückgeld der Benutzer erhalten wird so fern er zu viel bezahlt hat.
#
# Lade die Datei tickets.json in die Cloud9 IDE über "File" -> "Upload Local Files" hoch, oder kopiere den Inhalt manuell in eine neue Datei. Achte darauf, dass die Datei sich im Hauptverzeichnis befinden muss, damit dein Programm sie findet.
# Implementiere anschließend den Automaten.


with open("tickets-211215-172151.json", "r") as fh:
    x = json.load(fh)

# Erdtellt eine Liste der Fahrkarten (für Output ohne eckige Klammen)
fahrkarten = []
for count, ticket in enumerate(x["tickets"]):
    available = str(count +1), ticket["name"]
    fahrkarten.append(":".join(available))

print(fahrkarten)
# Fordert den Kunden auf eine Fahrkarte auszuwählen
print(f'Herzlich willkommen bei Ihrer Bahn.\nBitte wählen Sie eines der verfügbaren Tickets:\n\n{", ".join(fahrkarten)}.')
print()

cash = ", ".join(str(n) for n in x["accepted_cash"])

#print(cash)
#print(fahrkarten)

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


accepted_cash = x["accepted_cash"]

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