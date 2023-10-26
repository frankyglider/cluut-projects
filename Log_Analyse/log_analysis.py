from collections import Counter
from log_pdf import PDF
import seaborn as sns


# Log-Analyse und Apache verstehen

# In dieser Aufgabe geht es um das Verständnis von Log-Dateien und die Bedeutung des Apache HTTP Servers. Log-Dateien zeichnen Fehler und Ereignisse von Software auf. Der Apache HTTP Server ist eine weit verbreitete Webserver-Software. Access Logs des Apache-Servers enthalten Informationen über jede Serveranfrage, einschließlich IP-Adresse, Anfragedatum, Typ der Anfrage, HTTP-Statuscode und mehr.

# Aufgabe 1: Apache Logs analysieren
# Die Aufgabe beginnt mit dem Herunterladen und Speichern von Apache-Log-Dateien. Diese Logs werden in einem Python-Skript namens "log_analysis.py" geöffnet und gelesen. In jeder Log-Zeile werden Informationen wie die IP-Adresse des Clients, Datum der Anfrage, Anfragetyp, HTTP-Statuscode und mehr festgehalten.

# Aufgabe 2: HTTP-Statuscode des ersten Log-Eintrags
# Die erste Zeile des Log-Files wird in eine separate Variable gespeichert, analysiert und der HTTP-Statuscode wird extrahiert. Dieser Statuscode gibt an, ob die Anfrage erfolgreich war (z.B. Statuscode 200 für "OK") oder auf einen Fehler hinweist.

# Aufgabe 3: HTTP-Statuscode-Analyse
# Alle Log-Zeilen werden analysiert, und die Häufigkeit verschiedener HTTP-Statuscodes wird ermittelt. Insbesondere wird gezählt, wie oft der Statuscode 200 (erfolgreiche Anfrage) und der Statuscode 404 (Ressource nicht gefunden) vorkommen. Die collections.Counter-Klasse wird für diese Aufgabe verwendet.

# Aufgabe 4: Fehlerbehebung auf dem HTTP Server
# Um die Webanwendung zu verbessern, werden alle Log-Zeilen nach dem Statuscode 404 (Fehler) gefiltert, und die Anfragen mit diesem Statuscode werden in einer separaten Liste gespeichert. Zusätzlich werden die angeforderten URL-Pfade extrahiert und analysiert. Es wird ermittelt, wie viele verschiedene Fehlerquellen es gibt und welche die häufigsten sind.

# Bonus-Aufgabe: Log-Report
# In dieser Bonus-Aufgabe wird ein Log-Report erstellt. Dazu werden Histogramme für die Statuscodes und angeforderten URL-Pfade erstellt und in einer PDF-Datei gespeichert. Die fpdf-Bibliothek wird verwendet, um den Report zu erstellen.

# Der Log-Report enthält zwei Abbildungen: ein Histogramm für die Statuscodes und ein Histogramm für die angeforderten URL-Pfade. Schließlich wird ein PDF-Report generiert.
# Ziel: Analyse und Berichterstattung über Apache-Log-Daten, um Fehlerquellen und Statuscodes zu verstehen und zu visualisieren.


# Aufgabe 1: Apache Logs analysieren

log_list = []
with open("apache_logs", "r") as file:
    #for line in file:
        #log_list.append(line)

    log_list = file.readlines()    

# Jede Zeile des Logfiles enthält die IP Adresse des anfragenden Clients, user-ID des Clients, das Datum der Anfrage, Anfragetyp und Quelle, http status code, größe des  zurückgegebenen Paketes, genauere Angaben zur Herkunft der Anfrage und welcher Browser dazu verwendet wird.


# Aufgabe 2: HTTP Status Code des ersten Log Eintrags
    
first_line = log_list[0]
splitted = first_line.split()
print(f'Bei dem ersten Eintrag des Logfile wurde der Statuscode: {splitted[8]} zurückgegeben. Er bedeutet, dass die Anfrage erfolgreich war.')
print()


# Aufgabe 3: HTTP Status Code Analyse
    
status_codes = []

for line in log_list:
    codes = line.split()
    status_codes.append(codes[8])
    
#print(status_codes)

# Mengen an statuscodes mit dem Wert '200'
status_200 = status_codes.count("200")
print(f'Den Statuscode: 200 gibt es {status_200} mal.')
print()
# Mengen an statuscodes mit dem Wert '404'
status_404 = status_200 = status_codes.count("404")
print(f'Den Statuscode: 404 gibt es {status_404} mal.')
print()
counted_codes = Counter(status_codes)
counted_codes_first_three = counted_codes.most_common(3)
print(f'Die drei häufigsten Statuscodes sind: {counted_codes_first_three[0][0]} mit einer Anzahl von {counted_codes_first_three[0][1]}, {counted_codes_first_three[1][0]} mit einer Anzahl von {counted_codes_first_three[1][1]} und {counted_codes_first_three[2][0]} mit einer Anzahl von {counted_codes_first_three[2][1]}.')
print()


# Aufgabe 4: Fehlerbehebung auf dem HTTP Server
    
lines_with_404 = list(filter(lambda x: x.split()[8] == "404", log_list))
print(len(lines_with_404))
print()


resource_list = [line.split()[6] for line in lines_with_404]
print(len(set(resource_list)))

# mit for-loop
#resource_list = []
#
#for line in lines_with_404:
#    urls = line.split()
#    resource_list.append(urls[6])
#     
#print(resource_list)


most_three = Counter(resource_list).most_common(3)
print(most_three)
print()
print(f'Die drei häufigsten Fehlerquellen sind: {most_three[0][0]} mit einer Anzahl von {most_three[0][1]}, {most_three[1][0]} mit einer Anzahl von {most_three[1][1]} und {most_three[2][0]} mit einer Anzahl von {most_three[2][1]}.')


# Bonus Aufgabe: Log Report

sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})

# Plot zur übersicht über die Statuscodes    
status_plot = sns.histplot(status_codes)
status_plot.set_title("Überblick über Statuscodes im Logfile")
status_plot.set(xlabel = "Statuscodes", ylabel = "Häufigkeit")
status_plot.figure.savefig("status_codes.png", bbox_inches = "tight")
status_plot.figure.clf()

# Plot zur Übersicht über Fehlerrecourcen
recource_plot = sns.histplot(y = resource_list)
recource_plot.set_title("Übersicht über Fehlerrecourcen")
recource_plot.set(xlabel = "Source", ylabel = "Resource Namen")
recource_plot.figure.set_figheight(11)
recource_plot.figure.set_figwidth(8)
recource_plot.figure.savefig("resource_list.png", bbox_inches = "tight")
recource_plot.figure.clf()

plots = ["status_codes.png", "resource_list.png"]



log_report = PDF()
    
for plot in plots:
    log_report.print_page(plot)
        
log_report.output("LogReport.pdf", "F")