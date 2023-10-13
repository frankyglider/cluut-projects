import seaborn as sns
from textblob import TextBlob as tb
import json

# Projekt: Twitter Stimmungsanalyse

# Ein Kollege hat dir eine Datei mit einer Reihe von Tweets über verschiedene Themen übergeben.
# Die Datei ist schon im JSON Format und besteht aus einer Liste von Tweets, wobei zu jedem Tweet ein Thema, der Benutzer und der Text des Tweets gespeichert sind.
# Da der Kollege nicht so gut programmieren kann möchte er, dass du für ihn zwei kleine Aufgaben erledigst:
#     1. Filtere die Tweets nach dem Thema "obama" und benutze das Paket "TextBlob" um die Stimmung der "obama" Tweets zu berechnen.
#        Lade zuerst die Datei "data.json" in deine IDE hoch.
#        Das Paket "TextBlob" kannst du wie gewohnt über "pip" installieren. Wie du die Stimmung eines Tweets automatisch berechnen kannst, kannst du unter https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis nachlesen. Dich interessiert dabei der Wert "polarity".
#        Füge zu jedem Tweet einen neuen Schlüssel "sentiment" und gebe ihm den Wert:
#            "negative" wenn der "polarity"-Wert kleiner als -0.2 ist.
#            "positive" wenn der "polarity"-Wert größer als 0.2 ist.
#            "neutral" wenn der "polarity"-Wert dazwischen liegt.
#        Schreibe die nach "obama" gefilterte liste mit dem zusätzlichen "sentiment"-Feld in eine neue JSON Datei.





with open("data.json", "r") as fh:
    twitter = json.load(fh)

#for line in twitter:
    #print(line)



fil_obama = [x for x in twitter if x["topic"] == "obama"]
print(fil_obama)
fil_obama = []
for tweet in twitter:
    if tweet["topic"] == "obama":
        fil_obama.append(tweet)
print()

for x in fil_obama:
    print(x)
    sentiment = tb(x["tweet"]).sentiment.polarity
    if sentiment < -0.2:
        x.update({"sentiment": "negative"})
    elif sentiment > 0.2:
        x.update({"sentiment": "positive"})
    else:
        x.update({"sentiment": "neutral"})
    
        
        
for i in fil_obama:
    print(i)
    
with open("twitter_sen.json", "w") as fh:
    json.dump(fil_obama, fh)
print()   

sentilist = []            
for dic in fil_obama:
  for key, val in dic.items():
      if key == "sentiment":
          sentilist.append(val)
print(sentilist)


#    2. Benutze "Seaborn" um ein Histogramm zu erstellen welches anzeigt, wie viele Tweets über das Thema "obama" negativ, positiv und neutral sind.
#        Erstelle dafür erst eine Liste mit allen Sentiments und visualisiere dann das Histogramm mit der "histplot" Funktion.
#        Speichere die Grafik in eine Datei und sieh sie dir an.


sns.set_theme()
sentiplot = sns.histplot(data = sentilist)
sentiplot.set(title = "Sentiment Tweets")
sentiplot.get_figure().savefig("sentiplot.png")