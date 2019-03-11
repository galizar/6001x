print('Please think of a number between 0 and 100!')
high = 100
low = 0
guess = 50

def calc_guess(h, l):
    return int((h + l) / 2)

while True:
    print('Is your secret number {}?'.format(guess))
    direction = input("Enter 'h' if my guess is too high, 'l' if too low or 'c' if it's correct: ")

    if direction == 'h':
        high = guess
        guess = calc_guess(high, low)
    elif direction == 'l':
        low = guess
        guess = calc_guess(high, low)
    elif direction == 'c':
        print('Game over. Your secret number was {}'.format(guess))
        break
    else:
        print('Mmm. I did not understand your input. May you try again please?')
