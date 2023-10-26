# In diesem Projekt arbeiten wir mit der Datamuse API, einer nützlichen Ressource für sprachbezogene Aufgaben. Die Aufgaben sind wie folgt strukturiert:

# Aufgabe 1: Datamuse API kennenlernen
# Du startest mit einer Einführung in die Datamuse API. Deine Aufgabe ist es, die Verwendungsmöglichkeiten der API zu erkunden, die Basis-URL zu finden und zwei wichtige Endpunkte der API zu identifizieren.

# Aufgabe 2: Wörter mit ähnlicher Bedeutung
# Die nächste Aufgabe verlangt, die top 5 Wörter zu finden, die eine ähnliche Bedeutung wie "on top of" haben. Die gefundenen synonymen Wörter werden mit ihren zugehörigen Scores in einer Liste ausgegeben.

# Aufgabe 3: Wortgewandt sein - Funktion synonym_words
# Hier wird eine Funktion namens "synonym_words" entwickelt, die es erlaubt, synonyme Wörter zu einem gegebenen Wort und die Anzahl der gewünschten Ergebnisse zu erhalten. Die Funktion wird mit "on top of" getestet.

# Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words
# In dieser Aufgabe erstellst du die Funktion "rhyme_words". Diese Funktion ermöglicht das Finden von Wörtern, die sich auf ein gegebenes Wort reimen. Sie gibt die Top 5 reimenden Wörter zusammen mit ihren Scores zurück und wird mit dem Wort "grape" getestet.

# Aufgabe 5: Finde Antonyme
# Die letzte Aufgabe befasst sich mit Antonymen, Wörtern mit gegensätzlicher Bedeutung. Du erstellst die Funktion "antonym_words", um Antonyme für ein gegebenes Wort zu finden. Die Aufgabe besteht darin, die Funktion mit dem Wort "bright" zu testen.

# Zusätzlich wird gefordert, ein separates Modul namens "word_module.py" zu erstellen, in dem die erstellten Funktionen kopiert und in einem "if name == "main" Block getestet werden. Diese Struktur ermöglicht die Verwendung der Funktionen sowohl innerhalb des Moduls als auch in anderen Modulen.

# Durch diese Aufgaben erhältst du einen umfassenden Einblick in die Verwendung der Datamuse API für Synonyme, Reime und Antonyme, und du entwickelst modularen Code, der leicht wiederverwendet werden kann.

import requests


# Aufgabe 1: Datamuse API kennenlernen
    
"""Datamuse wird hauptsächlich zur Texterkennung und Gestaltung verwendet"""
"""Der Base URL lautet: https://api.datamuse.com/words"""
"""Es gibt den Endpunkt 'words'(Texterkennung) und den Endpunkt 'sug'(Autovervollständigung)"""


# Aufgabe 2: Wörter mit einer ähnlichen Bedeutung
    
muse_url = 'https://api.datamuse.com/words'
r = requests.get(muse_url, params = {"ml": "on+top+of", "max": 5})
muse_dict = r.json()
#print(muse_dict)
print()


# mit for-loop
#for i in muse_dict[:5]:
#    print(i["word"], i["score"])
#print()
# mit list comprehension
# top_five = [(i["word"], i["score"]) for i in muse_dict]
#print(top_five)

# Aufgabe 3: Wortgewandt sein - Funktion synonym_words

def synonym_words(word, num_results):
    #word_pa = word.replace(" ", "+")
    syn_url = 'https://api.datamuse.com/words'
    params = {"ml": word, "max": num_results}
    muse_syn = requests.get(syn_url, params).json()
    #print(muse_syn)
   
   
    # mit for-loop
    #results = []
    #for i in muse_syn:
    #    results.append((i["word"], i["score"]))
   
    # mit list comprehension
    results = [(i["word"], i["score"]) for i in muse_syn]
    return results
    
#word = "on top of"
#print(synonym_words(word, 5))


# Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words

def rhyme_words(word, num_results):
    
    rhyme_url = 'https://api.datamuse.com/words'
    params = {"rel_rhy": word, "max": num_results}
    
    muse_rhyme = requests.get(rhyme_url, params).json()
    results = [(i["word"], i["score"]) for i in muse_rhyme]
    return results
   
#print(rhyme_words("grape", 6))


# Aufgabe 5: Finde Antonyme

def antonym_words(word, num_results):
    #Importiere mit der import Funktion dann alle Funktionen aus dem word_module Modul in dein ursprüngliches Pythonskript (z.B. data_muse.py) und teste auch hier nochmal die Funktionen similar_words, rhyme_words und antonym_words (aber dieses mal eben jene aus dem Modul word_module.py).
    
    
    ant_url = 'https://api.datamuse.com/words'
    params = {"rel_ant": word, "max": num_results}
    
    muse_ant = requests.get(ant_url, params).json()

    
#print(antonym_words("bright", 6))
