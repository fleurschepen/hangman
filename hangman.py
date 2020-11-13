hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_to_guess = "getmefromanapi".lower()
guess_mode = "letter"
correctly_guessed_letters = []
wrongly_guessed_letters = []
wrongly_guessed_words = []
guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)
guessed_word = ""


def print_guess():
    indexes_for_guessed_letters = []

    while len(indexes_for_guessed_letters) < len(correctly_guessed_letters):
        indexes_for_guessed_letters.append([])

    for i, correctly_guessed_letter in enumerate(correctly_guessed_letters):
        for j, letter in enumerate(word_to_guess):
            if correctly_guessed_letter == letter:
                indexes_for_guessed_letters[i].append(j)

    word = ""

    for i, letter in enumerate(word_to_guess):
        letter_guessed = False

        for j, index in enumerate(indexes_for_guessed_letters):
            if i in index:
                letter_guessed = True

        if letter_guessed:
            word += letter
        else:
            word += "_"

    guessed = []
    guessed.extend(wrongly_guessed_letters)
    guessed.extend(wrongly_guessed_words)
    guessed_str = ""

    for i, wrong_guess in enumerate(guessed):
        if i == 0:
            guessed_str += wrong_guess
        else:
            guessed_str += ", " + wrong_guess

    return print(f"\nGuessing: {word}\nGuessed: {guessed_str}\n")


while word_to_guess != guessed_word and guesses < 6:
    print(hangman[guesses])
    print_guess()
    guess_mode = input("Letter/Word? ").lower()
    if guess_mode == "letter":
        guessed_letter = input("Letter: ").lower()
        if not guessed_letter.isalpha():
            print("\nThat's not a letter 😜")
        elif guessed_letter in wrongly_guessed_letters or guessed_letter in correctly_guessed_letters:
            print(f"\nYou already guessed '{guessed_letter}'!")
        elif guessed_letter in word_to_guess:
            correctly_guessed_letters.append(guessed_letter)
            print(f"\nYes! It contains '{guessed_letter}', well done 👏")
        else:
            wrongly_guessed_letters.append(guessed_letter)
            print(f"\nUh oh! It doesn't contain '{guessed_letter}', sad times 😢")
    else:
        guessed_word = input("Word: ").lower()
        if not guessed_word.isalpha():
            print("\nThat's not a (normal?) word 😜")
        elif guessed_word in wrongly_guessed_words:
            print(f"\nYou already guessed '{guessed_word}'!")
        elif guessed_word != word_to_guess:
            wrongly_guessed_words.append(guessed_word)
            print(f"\nUh oh! It wasn't '{guessed_word}', sad times 😢")

    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessed_word == word_to_guess:
    print(f"Yes! The word was '{guessed_word}'. You win!!! 🎉")
else:
    print(hangman[guesses])
    print("RIP, you died!!! ☠️")
