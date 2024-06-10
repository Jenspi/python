# HANGMAN Python 3.x version // Jennifer Spicer // October 14, 2019
# Hangman ASCII art credit goes to chrishorton on github: bit.ly/32h9PhV
import random

wordbank = ["tremendous", "pollution", "stupendous", "dance", "beginner", "husky", "bread", "religion", "reset",
            "celery", "military", "pear", "wholesale", "responsible", "fly", "lonely", "damaged", "sofa", "circle",
            "roll", "trust", "aromatic", "judge", "laugh", "creep", "apple", "imaginary", "delete", "goofy", "potato",
            "salve", "butter", "stranger", "zephyr", "convict", "boring", "intelligent", "grass", "dress", "opposite",
            "ant", "thankful", "kittens", "cook", "rot", "alarm", "yard", "arrogant", "mask", "loud"]

word = wordbank[random.randint(0, len(wordbank) - 1)]
# print(word) #for testing purposes
underscores = ["_ "] * len(word)
letters_guessed = []
wrong_guesses = 0
playing = True

man = ['''
  +---+
  |   |
      |
      | 6 mistakes allowed left!
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      | 5 mistakes allowed left!
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   | 4 mistakes allowed left!
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   | 3 mistakes allowed left!
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  | 2 mistakes allowed left!
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  | 1 mistake allowed left!
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

def reset():
    global word, underscores, letters_guessed, wrong_guesses, playing

    playing = True
    word = wordbank[random.randint(0, len(wordbank) - 1)]
    print(word)
    underscores = ["_ "] * len(word)
    letters_guessed = []
    wrong_guesses = 0

def incorrect():
    print("\n// Incorrect guess! //")
    global wrong_guesses
    wrong_guesses += 1

def won():
    global playing
    playing = False
    print(man[wrong_guesses])
    print("[LETTERS/WORDS GUESSED]: " + ", ".join(letters_guessed))
    print("\n" + " ".join(word))
    print("YOU WIN!")
    reset()
    userInput = input("Play again? Y/N ")
    if userInput.lower() == "y" or userInput.lower() == "yes":
        game()

def lost():
    global playing
    playing = False
    print(man[wrong_guesses])
    print("[LETTERS/WORDS GUESSED]: " + ", ".join(letters_guessed))
    print("\n" + " ".join(word))
    print("GAME OVER! Better luck next time.")
    reset()
    userInput = input("Play again? Y/N ")
    if userInput.lower() == "y" or userInput.lower() == "y":
        game()

def game():
    global playing
while playing:
    print(man[wrong_guesses])
    print("[LETTERS GUESSED]: " + ", ".join(letters_guessed))
    print("\n" + "".join(underscores))
    userInput = (input("Guess a letter: ")).lower()

    if userInput.lower() == "quit":
        playing = False
        print("Thanks for playing :)")

    # if input was already guessed
    if userInput in letters_guessed:
        print("// Letter already guessed! //")

    # if user's input is as long as the word, or is one letter
    if len(userInput) == len(word) or len(userInput) == 1:
        letters_guessed.append(userInput)
        # if user's guess is as long as word
        if len(userInput) == len(word):
            if userInput == word:
                won()
                break
            elif userInput != word:
                incorrect()
        # else if guess is a single letter
        elif len(userInput) == 1:
            if userInput not in word:
                incorrect()
                # check to see if amount of tries is up
                if wrong_guesses >= 6:
                    lost()
                    break
            # if guess is correct, place letter in correct spot
            elif userInput in word:
                for x in range(len(word)):
                    if userInput == word[x]:
                        underscores[x] = userInput + " "

    # if the user's guess isn't one letter or as long as the word, give error
    elif (len(userInput) < len(word) or len(userInput) > len(word)) and len(userInput) != 1 and userInput != "quit":
        print("Not valid input! Try guessing the whole word (" + str(
            len(word)) + " letters total in this case) or one letter at a time.")

game()