from collections import Counter
from log_pdf import PDF
import seaborn as sns


# Aufgabe 0: Log Analyse und Apache verstehen

    # Unter dem Begriff Logging verstehen wir die Aufzeichnung von Fehlern und Ereignissen von Software.
    # Jede Software, die du benutzt, hat eine Logging-Systematik implementiert, die dir bei der Fehlersuche hilft, wenn etwas mal nicht funktioniert.
    # Fehlermeldungen und Ereignisse werden meistens in eine oder mehrere Dateien geschrieben, sogenannte Log Files.
    # In der folgenden Aufgabe werden wir uns genau so ein Log File anschauen und es analysieren.
    # Bevor wir loslegen, starte eine kurze Recherche und beantworte folgende Fragen:
    # Was ist ein Apache HTTP Server?
    # Welches Format haben Apache Access Logs?
    # Welche Informationen sind in einer Access Log Zeile enthalten?
    # Tip 1: https://en.wikipedia.org/wiki/Apache_HTTP_Server#Feature_overview
    # Tip 2: https://httpd.apache.org/docs/2.2/logs.html#common%20
    # Tip 3: https://www.sumologic.com/blog/apache-access-log/

# Aufgabe 1: Apache Logs analysieren

    # Lade die zip-Datei herunter und speichere alle enthaltenen Files in einem Cloud9 Folder für dieses Projekt.
    # Öffne die Datei apache_logs in einem Python Skript namens log_analysis.py und lese alle Zeilen in eine Liste ein.
    # Schau dir die erste Zeile der Datei an und schreibe in einem Kommentar auf, welche Informationen wir in jeder Log Zeile haben.

log_list = []
with open("apache_logs", "r") as file:
    #for line in file:
        #log_list.append(line)

    log_list = file.readlines()    

# Jede Zeile des Logfiles enthält die IP Adresse des anfragenden Clients, user-ID des Clients, das Datum der Anfrage, Anfragetyp und Quelle, http status code, größe des  zurückgegebenen Paketes, genauere Angaben zur Herkunft der Anfrage und welcher Browser dazu verwendet wird.


# Aufgabe 2: HTTP Status Code des ersten Log Eintrags

    # Speichere die erste Zeile des Log Files in eine separate Variable first_line.
    # Splitte die Zeile in ihre Einzelteile mit dem split()-Befehl.
    # Extrahiere nun den HTTP Status Code.
    # Welcher Status Code wurde für diese Anfrage an den HTTP Server zurückgegeben?
    # Was bedeutet der HTTP Status Code?
    
    
    
first_line = log_list[0]
splitted = first_line.split()
print(f'Bei dem ersten Eintrag des Logfile wurde der Statuscode: {splitted[8]} zurückgegeben. Er bedeutet, dass die Anfrage erfolgreich war.')
print()

# Aufgabe 3: HTTP Status Code Analyse

    # Analysiere nun alle Log Zeilen und speichere alle HTTP Status Codes in einer Liste mit dem Namen status_codes.
    # Zähle, wie oft der Status Code 200 vorkommt und speichere den Wert in status_200.
    # Zähle, wie oft der Status Code 404 vorkommt und speichere den Wert in status_404.
    # Importiere nun die Klasse Counter aus dem Modul collections.
    # https://docs.python.org/3/library/collections.html#collections.Counter
    # Benutze die Counter Klasse, um für jeden Status Code in status_codes die Anzahl an Vorkommen zu bestimmen.
    # Welche sind die 3 häufigsten HTTP Status Codes?
    
    
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

    # Um deine Webapplikation für Benutzer zu verbessern, musst du herausfinden, welche Anfragen nicht funktioniert haben.
    # Filtere deshalb die Log Zeilen nach dem Status Code 404 und speichere alle Zeilen, die diesen Status Code beinhalten, in der Liste lines_with_404.
    # Benutze für das filtern die filter()-Funktion und lambda.
    # Speichere in einer neuen Liste namens resource_list die angefragten URL Paths (resource requested).
    # Benutze hier wieder die split()-Methode.
    # Tip: https://www.sumologic.com/blog/apache-access-log/
    # Wieviele verschiedene Fehlerquellen hast du gefunden?
    # Welche sind die 3 häufigsten Fehlerquellen bei den Anfragen auf unseren Apache Server?
    # Tip: https://docs.python.org/3/library/collections.html#collections.Counter
    
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

    # Ziel der Aufgabe ist es einen Log Report zu erstellen, der zwei Abbildungen beinhaltet.
    # Installiere hierfür das Python Modul fpdf mit pip: https://pypi.org/project/fpdf/
    # Das Skript log_pdf.py aus dem LMS beinhaltet eine Klasse PDF, mit der du deinen Log Report erstellen kannst.
    # Importiere die Klasse PDF aus dem Modul log_pdf in dein Skript.
    # Erstelle ein Histogram mit seaborn für deine Liste status_codes und speichere den Plot in der Datei status_codes.png.
    # Erstelle ein Histogram mit seaborn für deine Liste resource_list und speichere den Plot in der Datei resource_list.png.
    # Erstelle eine Liste plots, die zwei Strings enthält: status_codes.png, resource_list.png
    # Erstelle eine Instanz der Klasse PDF mit dem Namen log_report.
    # Erstelle nun eine for-Schleife über die Elemente plot in deiner Liste plots und rufe in der for-Schleife den folgenden Befehl auf:

    # log_report.print_page(plot)

    # Um den PDF Report nun zu erstellen, füge die folgende Zeile in deinen Code: 

    # log_report.output("LogReport.pdf", "F") 

    # Schaue dir den PDF Report an. Was könnte noch verbessert werden?


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