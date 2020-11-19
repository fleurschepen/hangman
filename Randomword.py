def randomword():
    from nltk.corpus import words
    from PyDictionary import PyDictionary
    import random
    word = ""
    definition = None
    while len(word) < 5 or definition is None:
        word_list = words.words()
        word = word_list[random.randint(0,len(word_list))]
        definition = PyDictionary.meaning(word,disable_errors=True)
    return(word, definition)
