import seaborn as sns
import pandas as pd

# Aufgabe 1: Budget Daten verstehen und einlesen.
# 
#     Lade die Datei budget.csv herunter und öffne sie in Cloud9.
#     Analysiere den Datensatz und finde folgende Punkte heraus:
#     Um welche Daten handelt es sich?
#     Wie viele Zeilen und Spalten sind im Datensatz enthalten?
#     Gibt es auf den ersten Blick bereits auffällige Datenpunkte?
# 
#     Lade nun den Datensatz mithilfe von pandas und der read_csv() Methode in ein DataFrame.
#     Benutze die Methode info(), um einen Überblick über das DataFrame zu bekommen.
#     Welche Datentypen haben wir in den einzelnen Spalten?


budget_csv = pd.read_csv("budget.csv", sep = ";")
print(budget_csv)
print()
print(budget_csv.info())


# Aufgabe 2: Gesamtsumme für Einnahmen und Ausgaben berechnen
# 
#     Mario und Laura sind daran interessiert, wie hoch ihre Einnahmen und Ausgaben in den letzten Monaten waren.
#     Berechne daher zuerst die Summe der Einnahmen und die Summe der Ausgaben für den ganzen Datensatz.
#     Wie viel konnten Mario und Laura in den letzten Monaten sparen und zur Seite legen?
#     Tipp: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
#     
total_in = round(budget_csv["In"].sum(), 2)
print(f'Die Gesamtsumme aller Einnahmen betrugen {total_in}€')
print()
total_out = round(budget_csv["Out"].sum(), 2)
print(f'Die Gesamtsumm aller Ausgaben betrugen {total_out}€')
print()
total_savings = total_in - total_out
print(f'Mario und Julia konnten {round(total_savings, 2)}€ zur Seite legen.')
print()


# Aufgabe 3: Ausgaben pro Kategorie
# 
#     Lass uns einen Blick auf die einzelnen Ausgaben werfen und verstehen, wo Mario und Laura am meisten ausgegeben haben.
#     Gruppiere die Ausgaben anhand der Kategorie und lasse dir die Summe der Ausgaben pro Kategorie anzeigen.
#     Wofür geben Mario und Laura am meisten Geld aus?
#     Tipp: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
    
    

budget_out = budget_csv[["Category", "Out"]].groupby("Category").sum()
budget_out = budget_out[1:]
print(budget_out)
print()


# Aufgabe 4: Visualisiere die Ausgaben pro Kategorie
# 
#     Benutze nun seaborn, um einen Barplot für die Ausgaben pro Kategorie zu erstellen.
#     Die Kategorie soll auf der y-Achse sein, die Höhe der Ausgaben auf der x-Achse.
#     Mache folgende Anpassungen an den Chart:
#         Titel: Ausgaben pro Kategorie         
#         x-Achsen Benennung: Höhe der Ausgaben
#         y-Achsen Benennung: Kategorie
#         Seaborn Theme: default
# 
# 
#     Speichere den Plot in der Datei expenses_per_category.png
#     Tipp: Benutze Code-Teile aus den vorherigen Hausaufgaben
#     Tipp: Benutze bbox_inches='tight' in deinem savefig() Befehl, um ein schönes Plottingergebnis zu erhalten.


x = pd
sns.set_theme()
budget_sns = sns.barplot(data = budget_out, y = budget_out.index, x = "Out")
budget_sns.set(title = "Ausgaben pro Kategorie", xlabel = "Höhe der Ausgaben", ylabel = "Kategorie")
budget_sns.get_figure().savefig("expenses_per_category.png", bbox_inches = "tight")
budget_sns.figure.clf()
print(budget_out.columns.tolist())
print(budget_out.index[1:])
print()


# Bonusaufgabe: Ausgaben pro Monat
# 
#     Mario und Laura wollen verstehen, ob sich ihre Ausgaben über die Monate hinweg verändert haben.
#     Gruppiere die Ausgaben nun pro Monat und speichere das Ergebnis in einem neuen DataFrame ab.
#     Tipp: Convertiere zuerst deine Date-Spalte in das pandas datetime Format: https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
#     Tipp: Benutze den pandas Grouper, um die Gruppierung pro Monat zu erzielen: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html?highlight=grouper


budget_csv["Date"] = pd.to_datetime(budget_csv["Date"], format = "%Y-%m-%d")
out_per_month = budget_csv[["Date", "Out"]].groupby(pd.Grouper(key = "Date", freq = "1M")).sum()
print(out_per_month)

 
#     Erstelle einen weiteren Plot, der die Ausgaben pro Monat aus deinem neuen DataFrame abbildet.
#     Benutze hierfür nochmal den Barplot von seaborn.
#     Wir möchten in diesem Plot die Monatsnamen auf der x-Achse und die Höhe der Ausgaben auf der y-Achse.
#     Speichere den Plot in der Datei expenses_per_month.png.
#     Passe die Achsenbenennung und den Titel des Plots entsprechend an.
#     Tipp: Benutze die Methode month_name(), um die Monatsnamen aus deinem DataFrameIndex zu bekommen: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html



x = pd.date_range(start = out_per_month.index[0], freq = "M", periods = 3)
res = x.month_name()
#print(res)
sns.set_theme()
o_p_m_sns = sns.barplot(data = out_per_month, x = res, y = "Out")
o_p_m_sns.set(title = "Ausgaben pro Monat", xlabel = "Monat", ylabel = "Ausgaben")
o_p_m_sns.figure.savefig("expenses_per_month.png", bbox_inches = "tight")
