import requests


# Aufgabe 6: Clean-Up und Modulerstellung

# Ziel:
# In dieser Aufgabe wird ein Python-Modul erstellt, um die Funktionalität eines bestehenden Skripts zu organisieren. Dies fördert die Wiederverwendbarkeit und die klare Trennung von Aufgaben. Anschließend werden die Funktionen aus dem Modul in das ursprüngliche Python-Skript importiert und getestet.

# Schritte:

#     Erstellen eines Moduls: Ein neues Modul, mit dem Namen "word_module.py", wird erstellt. Dieses Modul wird verwendet, um die bisher erstellten Funktionen zu organisieren. Diese Funktionen sind: synonyme_words, rhyme_words und antonym_words.

#     Modultest: Im "word_module.py" wird ein if __name__ == "__main__"-Block erstellt. Innerhalb dieses Blocks werden die Funktionen similar_words, rhyme_words und antonym_words getestet. Dies ermöglicht es, die Funktionalität des Moduls eigenständig zu überprüfen.

#     Importieren des Moduls: Das ursprüngliche Python-Skript (z.B. "data_muse.py") importiert nun das Modul "word_module.py". Dies erfolgt mit der import-Anweisung.

#     Erneuter Test im Hauptskript: Die importierten Funktionen (similar_words, rhyme_words, antonym_words) aus "word_module.py" werden auch im ursprünglichen Skript getestet, um sicherzustellen, dass sie ordnungsgemäß funktionieren.

#     if name == "main" Block:
#         Der Code innerhalb des if __name__ == "__main__"-Blocks in "data_muse.py" wird ebenfalls ausgeführt. Dies ist besonders nützlich, wenn das Skript sowohl eigenständig ausgeführt werden kann (z.B. für Tests) als auch als Modul in anderen Skripten verwendet wird.
#         Dieser Block ermöglicht es, unterschiedliche Aktionen auszuführen, basierend darauf, ob das Skript als Hauptprogramm oder als Modul in ein anderes Skript importiert wird.


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