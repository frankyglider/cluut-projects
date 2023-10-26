# Projekt: Twitter Stimmungsanalyse

# Aufgabenbeschreibung:

# Ein Kollege hat dir eine Datei mit einer Reihe von Tweets über verschiedene Themen übergeben. Die Datei ist im JSON-Format und enthält eine Liste von Tweets, wobei jedes Tweet ein Thema, einen Benutzer und den Text des Tweets enthält. Dein Kollege möchte, dass du zwei Aufgaben für ihn erledigst:

#     Filtern und Sentiment-Analyse für "obama" Tweets:
#         Filtere die Tweets nach dem Thema "obama".
#         Verwende das Paket "TextBlob", um die Stimmung der "obama" Tweets zu berechnen. Das Paket "TextBlob" kann über "pip" installiert werden.
#         Berechne die Stimmung für jeden "obama" Tweet anhand des "polarity"-Werts.
#         Füge jedem Tweet einen neuen Schlüssel "sentiment" hinzu, basierend auf dem "polarity"-Wert:
#             "negative", wenn "polarity" < -0.2.
#             "positive", wenn "polarity" > 0.2.
#             "neutral", wenn -0.2 <= "polarity" <= 0.2.
#         Speichere die gefilterte Liste von "obama"-Tweets mit dem zusätzlichen "sentiment"-Feld in eine neue JSON-Datei.

#     Erstellung eines Sentiment-Histogramms:
#         Verwende die Python-Bibliothek "Seaborn", um ein Histogramm zu erstellen, das anzeigt, wie viele "obama" Tweets als negativ, positiv und neutral eingestuft sind.
#         Erstelle eine Liste mit allen Sentiments (negativ, positiv, neutral).
#         Visualisiere das Histogramm mit der "histplot" Funktion von Seaborn.
#         Speichere die Grafik in einer Datei und betrachte sie.


import seaborn as sns
from textblob import TextBlob as tb
import json

# Öffnet die JSON-Datei und liest die Twitter-Daten ein
with open("data.json", "r") as fh:
    twitter = json.load(fh)

# Filtert Tweets, die zum Thema "obama" gehören
fil_obama = [x for x in twitter if x["topic"] == "obama"]
print(fil_obama)
# Alternative Methode zur Filterung von "obama" Tweets
fil_obama = []
for tweet in twitter:
    if tweet["topic"] == "obama":
        fil_obama.append(tweet)
print()

# Durchläuft die "obama" Tweets und analysiert ihre Stimmung
for x in fil_obama:
    print(x)
    sentiment = tb(x["tweet"]).sentiment.polarity

    # Weist jedem Tweet basierend auf der Stimmung ein Sentiment zu: negativ, positiv oder neutral
    if sentiment < -0.2:
        x.update({"sentiment": "negative"})
    elif sentiment > 0.2:
        x.update({"sentiment": "positive"})
    else:
        x.update({"sentiment": "neutral"})

# Gibt die "obama" Tweets mit zugeordnetem Sentiment aus
for i in fil_obama:
    print(i)

# Speichert die "obama" Tweets mit Sentiment in einer neuen JSON-Datei
with open("twitter_sen.json", "w") as fh:
    json.dump(fil_obama, fh)
print()

# Erstellt eine Liste der Sentiments aus den "obama" Tweets
sentilist = []
for dic in fil_obama:
    for key, val in dic.items():
        if key == "sentiment":
            sentilist.append(val)
print(sentilist)

# Konfiguriert die Seaborn-Visualisierung
sns.set_theme()

# Erstellt ein Histogramm (histplot) der Sentiments
sentiplot = sns.histplot(data=sentilist)
sentiplot.set(title="Sentiment der Tweets")

# Speichert das Histogramm als Bild
sentiplot.get_figure().savefig("sentiplot.png")
