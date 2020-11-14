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
    guess_mode = input("Do you want to guess a word? ").lower()
    if guess_mode == "yes":
        guessed_word = input("Word: ").lower()
        if not guessed_word.isalpha():
            print("\nThat's not a (normal?) word 😜")
        elif guessed_word in wrongly_guessed_words:
            print(f"\nYou already guessed '{guessed_word}'!")
        elif guessed_word != word_to_guess:
            wrongly_guessed_words.append(guessed_word)
            print(f"\nUh oh! It wasn't '{guessed_word}', sad times 😢")
    else:
        guessed_letter = input("Letter: ").lower()
        if not guessed_letter.isalpha() or len(guessed_letter)>1:
            print("\nThat's not a letter 😜")
        elif guessed_letter in wrongly_guessed_letters or guessed_letter in correctly_guessed_letters:
            print(f"\nYou already guessed '{guessed_letter}'!")
        elif guessed_letter in word_to_guess:
            correctly_guessed_letters.append(guessed_letter)
            print(f"\nYes! It contains '{guessed_letter}', well done 👏")
        else:
            wrongly_guessed_letters.append(guessed_letter)
            print(f"\nUh oh! It doesn't contain '{guessed_letter}', sad times 😢")

    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessed_word == word_to_guess:
    print(f"Yes! The word was '{guessed_word}'. You win!!! 🎉")
else:
    print(hangman[guesses])
    print(f"RIP, you died!!! ☠️ the word was {word_to_guess}")