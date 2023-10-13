import requests


# Aufgabe 6: Clean-Up: Erstelle ein Modul

    # Erstelle ein neues Modul (also eine neue Datei) mit dem Namen word_module.py.
    # Kopiere alle bisher erstellten Funktionen (synonyme_words, rhyme_words und antonym_words) in diese Datei.
    # Erstelle in diesem Modul einen if __name__ == "__main__" block und teste deine Funktionen similar_words, rhyme_words und antonym_words in word_module.py.
    # Schaue dir hierfür zunächst die offizielle Python Dokumentation an: https://docs.python.org/3/library/__main__.html
    # Zusätzliche Hilfestellung findest du in diesem Beispiel: https://www.learnpython.dev/02-introduction-to-python/190-apis/final-exercise/
    # Importiere mit der import Funktion dann alle Funktionen aus dem word_module Modul in dein ursprüngliches Pythonskript (z.B. data_muse.py) und teste auch hier nochmal die Funktionen similar_words, rhyme_words und antonym_words (aber dieses mal eben jene aus dem Modul word_module.py).


    # Wird der Code aus dem if __name__ == "__main__" Block in data_muse.py auch ausgeführt?
    # Wofür kannst du den if __name__ == "__main__" Block benutzen?

def synonym_words(word, num_results):
    
    syn_url = 'https://api.datamuse.com/words'
    params = {"ml": word, "max": num_results}
    muse_syn = requests.get(syn_url, params).json()
    
    results = [(i["word"], i["score"]) for i in muse_syn]
    return results
    
#print(synonym_words("on top of", 5))
print()

def rhyme_words(word, num_results):
    
    rhyme_url = 'https://api.datamuse.com/words'
    params = {"rel_rhy": word, "max": num_results}
    muse_rhyme = requests.get(rhyme_url, params).json()
    
    results = [(i["word"], i["score"]) for i in muse_rhyme]
    return results
    
#print(rhyme_words("grape", 6))
print()

def antonym_words(word, num_results):
    
    ant_url = 'https://api.datamuse.com/words'
    params = {"rel_ant": word, "max": num_results}
    muse_ant = requests.get(ant_url, params).json()
    
    results = [i["word"] for i in muse_ant]
    return results
    
#print(antonym_words("bright", 6))


print(__name__)
if __name__ == "__main__":
    print(synonym_words("on top of", 5))
    print()
    print(rhyme_words("grape", 6))
    print()
    print(antonym_words("bright", 6))
    print()
    print(__name__)