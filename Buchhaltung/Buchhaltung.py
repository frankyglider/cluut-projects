# Diese Aufgabenreihe konzentriert sich auf die Arbeit mit Daten in Python. Zuerst geht es darum, einen Datensatz aus einer Datei zu analysieren und in ein DataFrame zu importieren.
# Dann werden die Gesamtsummen der Einnahmen und Ausgaben berechnet, um zu verstehen, wie viel Geld gespart wurde. 
# Anschließend werden die Ausgaben nach Kategorien gruppiert, um festzustellen, wofür das meiste Geld ausgegeben wird.
# Schließlich wird ein Barplot erstellt, der die Ausgaben pro Kategorie visualisiert. 
# Diese Aufgaben sollen helfen, Daten zu analysieren, finanzielle Muster zu identifizieren und diese Muster grafisch darzustellen.



import seaborn as sns
import pandas as pd

# Aufgabe 1: Budget Daten verstehen und einlesen.

budget_csv = pd.read_csv("budget.csv", sep = ";")
print(budget_csv)
print()
print(budget_csv.info())


# Aufgabe 2: Gesamtsumme für Einnahmen und Ausgaben berechnen
 
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

budget_out = budget_csv[["Category", "Out"]].groupby("Category").sum()
budget_out = budget_out[1:]
print(budget_out)
print()


# Aufgabe 4: Visualisiere die Ausgaben pro Kategorie

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

budget_csv["Date"] = pd.to_datetime(budget_csv["Date"], format = "%Y-%m-%d")
out_per_month = budget_csv[["Date", "Out"]].groupby(pd.Grouper(key = "Date", freq = "1M")).sum()
print(out_per_month)


x = pd.date_range(start = out_per_month.index[0], freq = "M", periods = 3)
res = x.month_name()
#print(res)
sns.set_theme()
o_p_m_sns = sns.barplot(data = out_per_month, x = res, y = "Out")
o_p_m_sns.set(title = "Ausgaben pro Monat", xlabel = "Monat", ylabel = "Ausgaben")
o_p_m_sns.figure.savefig("expenses_per_month.png", bbox_inches = "tight")
