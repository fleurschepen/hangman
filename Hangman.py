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

to_guess = randomword()
word_to_guess = to_guess[0].lower()
guess_mode = "letter"
correctly_guessed_letters = []
wrongly_guessed_letters = []
wrongly_guessed_words = []
guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)
guessedinput = ""


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


while word_to_guess != guessedinput and guesses < 6:
    print(hangman[guesses])
    print_guess()
    guessedinput = input("What is your guess? ").lower()
    if len(guessedinput) > 1:
        print(guessedinput)
        if not guessedinput.isalpha():
            print("\nThat's not a (normal?) word 😜")
        elif guessedinput in wrongly_guessed_words:
            print(f"\nYou already guessed '{guessedinput}'!")
        elif guessedinput != word_to_guess:
            wrongly_guessed_words.append(guessedinput)
            print(f"\nUh oh! It wasn't '{guessedinput}', sad times 😢")
    else:
        if not guessedinput.isalpha():
            print("\nThat's not a letter 😜")
        elif guessedinput in wrongly_guessed_letters or guessedinput in correctly_guessed_letters:
            print(f"\nYou already guessed '{guessedinput}'!")
        elif guessedinput in word_to_guess:
            correctly_guessed_letters.append(guessedinput)
            print(f"\nYes! It contains '{guessedinput}', well done 👏")
        else:
            wrongly_guessed_letters.append(guessedinput)
            print(f"\nUh oh! It doesn't contain '{guessedinput}', sad times 😢")

    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessedinput == word_to_guess:
    print(f"Yes! The word was '{guessedinput}'. You win!!! 🎉\n This means {to_guess[1]}")
else:
    print(hangman[guesses])
    print(f"RIP, you died!!! ☠️ the word was {word_to_guess} which means {to_guess[1]}")