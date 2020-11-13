def randomword():
    from nltk.corpus import words
    import random
    word_list = words.words()
    word = word_list[random.randint(0,len(word_list))]
    return(word)
print(randomword())