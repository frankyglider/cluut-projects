import requests


# Aufgabe 1: Datamuse API kennenlernen

    # Wir arbeiten in diesem Projekt mit der Datamuse API: https://www.datamuse.com/api/
    # Finde heraus, für was die Datamuse API genutzt werden kann.
    # Was ist die Base URL?
    # Welche zwei Funktionen (Endpoints) bietet die API?
    
"""Datamuse wird hauptsächlich zur Texterkennung und Gestaltung verwendet"""
"""Der Base URL lautet: https://api.datamuse.com/words"""
"""Es gibt den Endpunkt 'words'(Texterkennung) und den Endpunkt 'sug'(Autovervollständigung)"""

# Aufgabe 2: Wörter mit einer ähnlichen Bedeutung

    # Finde nun die top 5 Wörter, die eine ähnliche Bedeutung haben wie "on top of".
    # Printe eine Liste mit synonymen Wörtern und Scores.

    
muse_url = 'https://api.datamuse.com/words'
r = requests.get(muse_url, params = {"ml": "on+top+of", "max": 5})
muse_dict = r.json()
#print(muse_dict)
print()


# as for-loop
#for i in muse_dict[:5]:
#    print(i["word"], i["score"])
#print()
# as list comprehension
# top_five = [(i["word"], i["score"]) for i in muse_dict]
#print(top_five)

# Aufgabe 3: Wortgewandt sein - Funktion synonym_words

    # Erstelle eine Funktion synonym_words, die die Parameter word und num_results entgegennimmt.
    # Die Funktion benutzt die Datamuse API, um synonyme Wörter zu word zu sammeln.
    # Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (synonymes Wort, Score) enthält.
    # Teste die Funktion erneut mit dem Wort "on top of" und vergleiche das Ergebnis mit Aufgabe 2.

def synonym_words(word, num_results):
    #word_pa = word.replace(" ", "+")
    syn_url = 'https://api.datamuse.com/words'
    params = {"ml": word, "max": num_results}
    muse_syn = requests.get(syn_url, params).json()
    #print(muse_syn)
   
   
    # mit for loop
    #results = []
    #for i in muse_syn:
    #    results.append((i["word"], i["score"]))
   
    # mit list comprehension
    results = [(i["word"], i["score"]) for i in muse_syn]
    return results
    
#word = "on top of"
#print(synonym_words(word, 5))


# Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words

    # Erstelle eine Funktion rhyme_words, die die Parameter word und num_results entgegennimmt.
    # Die Funktion benutzt die Datamuse API, um reimbare Wörter zu word zu sammeln.
    # Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (reimbares Wort, Score) enthält.
    # Teste die Funktion mit dem Wort "grape". Was sind die Top 5 Wörter, die sich auf "grape" reimen?
    
def rhyme_words(word, num_results):
    
    rhyme_url = 'https://api.datamuse.com/words'
    params = {"rel_rhy": word, "max": num_results}
    
    muse_rhyme = requests.get(rhyme_url, params).json()
    results = [(i["word"], i["score"]) for i in muse_rhyme]
    return results
   
#print(rhyme_words("grape", 6))


# Aufgabe 5: Finde Antonyme

    # Antonyme sind in der Sprachwissenschaft mit gegensätzlicher Bedeutung, z.b. früh --> spät.
    # Erstelle eine Funktion antonym_words, die die Parameter word und num_results entgegennimmt.
    # Die Funktion benutzt die Datamuse API, um Antonyme zu word zu sammeln.
    # Die Funktion gibt eine Liste der Länge num_results zurück, die nur die Antonyme enthält.
    # Teste die Funktion mit dem Wort "bright".

def antonym_words(word, num_results):
    #Importiere mit der import Funktion dann alle Funktionen aus dem word_module Modul in dein ursprüngliches Pythonskript (z.B. data_muse.py) und teste auch hier nochmal die Funktionen similar_words, rhyme_words und antonym_words (aber dieses mal eben jene aus dem Modul word_module.py).
    
    
    
    ant_url = 'https://api.datamuse.com/words'
    params = {"rel_ant": word, "max": num_results}
    
    muse_ant = requests.get(ant_url, params).json()
from word_module import * 


    results = [i["word"] for i in muse_ant]
    return results
    
#print(antonym_words("bright", 6))


# Aufgabe 6: Clean-Up: Erstelle ein Modul

    # Erstelle ein neues Modul (also eine neue Datei) mit dem Namen word_module.py.
    # Kopiere alle bisher erstellten Funktionen (synonyme_words, rhyme_words und antonym_words) in diese Datei.
    # Erstelle in diesem Modul einen if __name__ == "__main__" block und teste deine Funktionen similar_words, rhyme_words und antonym_words in word_module.py.
    # Schaue dir hierfür zunächst die offizielle Python Dokumentation an: https://docs.python.org/3/library/__main__.html
    # Zusätzliche Hilfestellung findest du in diesem Beispiel: https://www.learnpython.dev/02-introduction-to-python/190-apis/final-exercise/


    # Wird der Code aus dem if __name__ == "__main__" Block in data_muse.py auch ausgeführt?
    # Wofür kannst du den if __name__ == "__main__" Block benutzen?



print(synonym_words("on top of", 5))
#print()
#print(rhyme_words("grape", 6))
#print()
#print(antonym_words("bright", 6))
#print()
print(__name__)