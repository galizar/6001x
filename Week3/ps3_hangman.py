# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

from hangman_utils import *

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))

    guessed_letters = []
    available_letters = getAvailableLetters(guessed_letters)
    guessed_word = getGuessedWord(secretWord, guessed_letters)
    guesses_left = 8

    while True:
        print('-------------')
        print('You have {} guesses left.'.format(guesses_left))
        print('Available letters: ', available_letters)
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        guessed_letters.append(guess)

        if guess == "":
            print('Mmm you did not write anything.')

        elif guess not in available_letters:
            if guess in ALPHABET:
                print("Oops! You've already guessed that letter: ", guessed_word)
            else:
                print('Are you sure what you wrote is a letter?')

        elif guess in secretWord:
            available_letters = getAvailableLetters(guessed_letters)
            guessed_word = getGuessedWord(secretWord, guessed_letters)
            print('Good guess: ', guessed_word)

            if guessed_word == secretWord:
                print('-------------')
                print('Congratulations, you won!')
                break

        else:
            guesses_left -= 1
            available_letters = getAvailableLetters(guessed_letters)
            print('Oops! That letter is not in my word: ', guessed_word)

            if not guesses_left:
                print('-------------')
                print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))
                break
