def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(letter in letters_guessed for letter in secret_word)


def getGuessedWord(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_positions = [letter in letters_guessed for letter in secret_word]
    guessed_word = ''

    for letter, guessed in zip(secret_word, guessed_positions):
        if guessed:
            guessed_word += f'{letter}'
        else:
            guessed_word += '_ '

    return guessed_word


def getAvailableLetters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

    return ''.join([letter for letter in ALPHABET if letter not in letters_guessed])
