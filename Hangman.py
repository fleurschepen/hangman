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
print(word_to_guess)

correctly_guessed_letters = []
wrongly_guessed_letters = []
wrongly_guessed_words = []
guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)
guessedinput = ""


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
    global guessedinput
    guessedinput = word_to_guess if all(letter in correctly_guessed_letters for letter in word_to_guess) else guessedinput


def one_letter_left_to_guess():
    letters_to_guess = len(list(dict.fromkeys(word_to_guess))) - len(correctly_guessed_letters)
    return letters_to_guess == 1


while word_to_guess != guessedinput and guesses < 6:
    print_game_state()

    input_string = ""

    if guesses == 5:
        input_string = "Last guess!!! "
    else:
        input_string = "What is your guess? "

    if one_letter_left_to_guess():
        input_string += "You only have one letter left!!! "

    # if guesses == 5 and one_letter_left_to_guess():
    #     input_string = "Last guess and one letter left!!!"
    # elif guesses == 5:
    #     input_string = "Last guess!!!"
    # elif not one_letter_left_to_guess():
    #     input_string = "What is your guess?"
    # else:
    #     input_string = "One letter left!!! What is your guess? "

    guessedinput = input(input_string).lower()

    if len(guessedinput) > 1 :
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

    check_guessed_letters()
    guesses = len(wrongly_guessed_letters) + len(wrongly_guessed_words)

if guessedinput == word_to_guess:
    print(f"Yes! The word was '{guessedinput}'. You win!!! 🎉\n This means {to_guess[1]}")
else:
    print(hangman[guesses])
    print(f"RIP, you died!!! ☠️ The word was {word_to_guess} which means {to_guess[1]}")