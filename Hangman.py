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
correctly_guessed_letters = []
wrongly_guessed_letters = []
wrongly_guessed_words = []
guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)
guessed = ""


def print_game_state():
    word = ""

    for letter in word_to_guess:
        word += letter if letter in correctly_guessed_letters else "_"

    guessed_ext = []
    guessed_ext.extend(wrongly_guessed_letters)
    guessed_ext.extend(wrongly_guessed_words)
    guessed_str = ""

    for i, wrong_guess in enumerate(guessed_ext):
        guessed_str += wrong_guess if i == 0 else ", " + wrong_guess

    return print(f"{hangman[guesses]}\n\nGuessing: {word}\nGuessed: {guessed_str}\n")


def check_guessed_letters():
    global guessed
    guessed = word_to_guess if all(letter in correctly_guessed_letters for letter in word_to_guess) else guessed


def one_letter_left_to_guess():
    letters_to_guess = len(list(dict.fromkeys(word_to_guess))) - len(correctly_guessed_letters)
    return letters_to_guess == 1


while word_to_guess != guessed and guesses < 6:
    print_game_state()
    guessed = input(
        "What is your guess? " if not one_letter_left_to_guess() else "One letter left!!! What's the word? "
    ).lower()

    if len(guessed) > 1:
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

    check_guessed_letters()
    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessed == word_to_guess:
    print(f"Yes! The word was '{guessed}'. You win!!! 🎉")
else:
    print(hangman[guesses])
    print(f"RIP, you died!!! ☠️ the word was {word_to_guess}")
