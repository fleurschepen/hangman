from Randomword import randomword
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

word_to_guess = randomword()
guess_mode = "letter"
correctly_guessed_letters = []
wrongly_guessed_letters = []
wrongly_guessed_words = []
guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)
guessed_word = ""


def print_guess():
    word = ""

    for letter in word_to_guess:
        if letter in correctly_guessed_letters:
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
    guessed = input("What is your guess? ").lower()
    if len(guessed) > 1 :
        if not guessed.isalpha():
            print("\nThat's not a (normal?) word 😜")
        elif guessed in wrongly_guessed_words:
            print(f"\nYou already guessed '{guessed}'!")
        elif guessed != word_to_guess:
            wrongly_guessed_words.append(guessed)
            print(f"\nUh oh! It wasn't '{guessed}', sad times 😢")
    else:
        if not guessed.isalpha():
            print("\nThat's not a letter 😜")
        elif guessed in wrongly_guessed_letters or guessed in correctly_guessed_letters:
            print(f"\nYou already guessed '{guessed}'!")
        elif guessed in word_to_guess:
            correctly_guessed_letters.append(guessed)
            print(f"\nYes! It contains '{guessed}', well done 👏")
        else:
            wrongly_guessed_letters.append(guessed)
            print(f"\nUh oh! It doesn't contain '{guessed}', sad times 😢")

    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessed == word_to_guess:
    print(f"Yes! The word was '{guessed}'. You win!!! 🎉")
else:
    print(hangman[guesses])
    print(f"RIP, you died!!! ☠️ the word was {word_to_guess}")