def randomword():
    from nltk.corpus import words
    import random
    import requests

    word = ""
    while len(word) < 5:
        word_list = words.words()
        word = word_list[random.randint(0, len(word_list))]

        # print(word)
        url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/frequency"

        headers = {
            'x-rapidapi-key': "",  # ADD ME
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        if "frequency" in response_json:
            if not response_json["frequency"]["perMillion"] > 2:
                word = ""
        else:
            word = ""

    return word


print(randomword())
